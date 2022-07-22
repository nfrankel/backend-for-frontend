local http    = require('resty.http')
local core    = require('apisix.core')
local json    = require('cjson.safe')
local get_var = require('resty.ngxvar').fetch
local log  = core.log

local plugin_name = 'bff-plugin'
local data_endpoints = {
    products = '/products',
    news = '/news',
    info = {
        catalog = '/catalog/info',
        news = '/news/info'
    }
}

local _M = {
    version = 1.0,
    priority = 100,
    name = plugin_name,
    schema = {},
}

local function fetch_data_from(path)
    local httpc = http.new()
    local server_port = get_var('server_port')
    local res, err = httpc:request_uri('http://localhost:' .. server_port .. path)
    if not res then
        log.error("Error happened in fetching data", err)
        return { error = err }
    end
    return res.body
end

local function fetch_all_data()
    local data = {}
    for key, value in pairs(data_endpoints) do
        if type(value) == 'string' then
            local body = fetch_data_from(value)
            data[key] = json.decode(body)
        else
            local data_key = {}
            for nested_key, nested_value in pairs(value) do
                print('value: ', nested_value)
                local body2 = fetch_data_from(nested_value)
                data_key[nested_key] = json.decode(body2)
            end
            data[key] = data_key
        end
    end
    return core.response.exit(200, json.encode(data))
end

function _M.api()
    return {
        {
            methods = { 'GET' },
            uri = "/",
            handler = fetch_all_data,
        }
    }
end

return _M
