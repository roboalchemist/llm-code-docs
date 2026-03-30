# Source: https://docs.api7.ai/hub/body-transformer.md

# body-transformer

The `body-transformer` plugin performs template-based transformations to transform the request and/or response bodies from one format to another.

## Examples[â](#examples "Direct link to Examples")

The examples below demonstrate how you can configure `body-transformer` for different scenarios.

The transformation template uses [lua-resty-template](https://github.com/bungle/lua-resty-template) syntax. See the [template syntax](https://github.com/bungle/lua-resty-template#template-syntax) to learn more.

You can also use auxiliary functions `_escape_json()` and `_escape_xml()` to escape special characters such as double quotes, `_body` to access request body, and `_ctx` to access context variables.

In all cases, you should ensure that the transformation template is a valid JSON string.

### Transform between JSON and XML SOAP[â](#transform-between-json-and-xml-soap "Direct link to Transform between JSON and XML SOAP")

The following example demonstrates how to transform the request body from JSON to XML and the response body from XML to JSON when working with a SOAP upstream service.

Start the sample SOAP service:

```
cd /tmp
git clone https://github.com/spring-guides/gs-soap-service.git
cd gs-soap-service/complete
./mvnw spring-boot:run
```

Create the request and response transformation templates:

```
req_template=$(cat <<EOF | awk '{gsub(/"/,"\\\"");};1' | awk '{$1=$1};1' | tr -d '\r\n'
<?xml version="1.0"?>
<soap-env:Envelope xmlns:soap-env="http://schemas.xmlsoap.org/soap/envelope/">
 <soap-env:Body>
  <ns0:getCountryRequest xmlns:ns0="http://spring.io/guides/gs-producing-web-service">
   <ns0:name>{{_escape_xml(name)}}</ns0:name>
  </ns0:getCountryRequest>
 </soap-env:Body>
</soap-env:Envelope>
EOF
)

rsp_template=$(cat <<EOF | awk '{gsub(/"/,"\\\"");};1' | awk '{$1=$1};1' | tr -d '\r\n'
{% if Envelope.Body.Fault == nil then %}
{
  "status":"{{_ctx.var.status}}",
  "currency":"{{Envelope.Body.getCountryResponse.country.currency}}",
  "population":{{Envelope.Body.getCountryResponse.country.population}},
  "capital":"{{Envelope.Body.getCountryResponse.country.capital}}",
  "name":"{{Envelope.Body.getCountryResponse.country.name}}"
}
{% else %}
{
  "message":{*_escape_json(Envelope.Body.Fault.faultstring[1])*},
  "code":"{{Envelope.Body.Fault.faultcode}}"
  {% if Envelope.Body.Fault.faultactor ~= nil then %}
  , "actor":"{{Envelope.Body.Fault.faultactor}}"
  {% end %}
}
{% end %}
EOF
)
```

`awk` and `tr` are used above to manipulate the template such that the template would be a valid JSON string.

Create a route with `body-transformer` using the templates created previously:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "body-transformer-route",
    "methods": ["POST"],
    "uri": "/ws",
    "plugins": {
      "body-transformer": {
        "request": {
          "template": "'"$req_template"'",
          "input_format": "json"
        },
        "response": {
          "template": "'"$rsp_template"'",
          "input_format": "xml"
        }
      },
      "proxy-rewrite": {
        "headers": {
          "set": {
            "Content-Type": "text/xml"
          }
        }
      }
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "localhost:8080": 1
      }
    }
  }'
```

â¶ Set the request input format as JSON, so that the plugin will apply the JSON decoder internally.

â· Set the response input format as XML, so that the plugin will apply the XML decoder internally.

â¸ Set the `Content-Type` header to `text/xml` for the upstream service to respond properly.

tip

If it is cumbersome to adjust complex text files to be valid transformation templates, you can use the base64 utility to encode the files, such as the following:

```
"body-transformer": {
  "request": {
    "template": "'"$(base64 -w0 /path/to/request_template_file)"'"
  },
  "response": {
    "template": "'"$(base64 -w0 /path/to/response_template_file)"'"
  }
}
```

Send a request with a valid JSON body:

```
curl "http://127.0.0.1:9080/ws" -X POST -d '{"name": "Spain"}'
```

The JSON body sent in the request will be transformed into XML before being forwarded to the upstream SOAP service, and the response body will be transformed back from XML to JSON.

You should see a response similar to the following:

```
{
  "status": "200",
  "currency": "EUR",
  "population": 46704314,
  "capital": "Madrid",
  "name": "Spain"
}
```

### Modify Request Body[â](#modify-request-body "Direct link to Modify Request Body")

The following example demonstrates how to dynamically modify the request body.

Create a route with `body-transformer`:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "body-transformer-route",
    "uri": "/anything",
    "plugins": {
      "body-transformer": {
        "request": {
          "template": "{\"foo\":\"{{name .. \" world\"}}\",\"bar\":{{age+10}}}"
        }
      }
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org:80": 1
      }
    }
  }'
```

â¶ Set a template that appends "world" to the name and adds 10 to the age and set them as values to "foo" and "bar" respectively.

Send a request to the route:

```
curl "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -d '{"name":"hello","age":20}' \
  -i
```

You should see a response of the following:

```
{
  "args": {},
  "data": "{\"foo\":\"hello world\",\"bar\":30}",
  ...
  "json": {
    "bar": 30,
    "foo": "hello world"
  },
  "method": "POST",
  ...
}
```

### Generate Request Body Using Variables[â](#generate-request-body-using-variables "Direct link to Generate Request Body Using Variables")

The following example demonstrates how to generate request body dynamically using the `ctx` context variables.

Create a route with `body-transformer`:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "body-transformer-route",
    "uri": "/anything",
    "plugins": {
      "body-transformer": {
        "request": {
          "template": "{\"foo\":\"{{_ctx.var.arg_name .. \" world\"}}\"}"
        }
      }
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org:80": 1
      }
    }
  }'
```

â¶ Set a template which accesses the request argument using the [NGINX variable](https://docs.api7.ai/apisix/reference/built-in-variables.md#nginx-variables) `arg_name`.

Send a request to the route with `name` argument:

```
curl -i "http://127.0.0.1:9080/anything?name=hello"
```

You should see a response like this:

```
{
  "args": {
    "name": "hello"
  },
  ...,
  "json": {
    "foo": "hello world"
  },
...
}
```

### Transform Body from YAML to JSON[â](#transform-body-from-yaml-to-json "Direct link to Transform Body from YAML to JSON")

The following example demonstrates how to transform request body from YAML to JSON.

Create the request transformation template:

```
req_template=$(cat <<EOF | awk '{gsub(/"/,"\\\"");};1'
{%
    local yaml = require("tinyyaml")
    local body = yaml.parse(_body)
%}
{"foobar":"{{body.foobar.foo .. " " .. body.foobar.bar}}"}
EOF
)
```

Create a route with `body-transformer` that uses the template:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "body-transformer-route",
    "uri": "/anything",
    "plugins": {
      "body-transformer": {
        "request": {
          "template": "'"$req_template"'"
        }
      }
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org:80": 1
      }
    }
  }'
```

Send a request to the route with a YAML body:

```
body='
foobar:
  foo: hello
  bar: world'

curl "http://127.0.0.1:9080/anything" -X POST \
  -d "$body" \
  -H "Content-Type: text/yaml" \
  -i
```

You should see a response similar to the following, which verifies that the YAML body was appropriately transformed to JSON:

```
{
  "args": {},
  "data": "{\"foobar\":\"hello world\"}",
  ...
  "json": {
    "foobar": "hello world"
  },
...
}
```

### Transform Form URL Encoded Body to JSON[â](#transform-form-url-encoded-body-to-json "Direct link to Transform Form URL Encoded Body to JSON")

The following example demonstrates how to transform `form-urlencoded` body to JSON.

Create a route with `body-transformer` as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "body-transformer-route",
    "uri": "/anything",
    "plugins": {
      "body-transformer": {
        "request": {
          "input_format": "encoded",
          "template": "{\"foo\":\"{{name .. \" world\"}}\",\"bar\":{{age+10}}}"
        }
      }
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org:80": 1
      }
    }
  }'
```

â¶ Set the `input_format` to `encoded`.

â· Set a template which appends string `world` to the `name` input, add 10 to the `age` input, and form a new JSON object.

Send a POST request to the route with an encoded body:

```
curl "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d 'name=hello&age=20'
```

You should see a response similar to the following:

```
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "{\"foo\":\"hello world\",\"bar\":30}": ""
  }, 
  "headers": {
    ...
  }, 
  ...
}
```

### Transform GET Request Query Parameter to Body[â](#transform-get-request-query-parameter-to-body "Direct link to Transform GET Request Query Parameter to Body")

The following example demonstrates how to transform a GET request query parameter to request body. Note that this does not transform the HTTP method. To transform the method, see [`proxy-rewrite`](https://docs.api7.ai/hub/proxy-rewrite.md).

Create a route with `body-transformer` as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "body-transformer-route",
    "uri": "/anything",
    "plugins": {
      "body-transformer": {
        "request": {
          "input_format": "args",
          "template": "{\"message\": \"hello {{name}}\"}"
        }
      }
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org:80": 1
      }
    }
  }'
```

â¶ Set the `input_format` to `args`.

â· Set a template which adds a message to the request.

Send a GET request to the route:

```
curl "http://127.0.0.1:9080/anything?name=john"
```

You should see a response similar to the following:

```
{
  "args": {}, 
  "data": "{\"message\": \"hello john\"}",
  "files": {},
  "form": {},
  "headers": {
    ...
  },
  "json": {
    "message": "hello john"
  }, 
  "method": "GET",
  ...
}
```

### Transform Plain Media Type[â](#transform-plain-media-type "Direct link to Transform Plain Media Type")

The following example demonstrates how to transform requests with `plain` media type.

Create a route with `body-transformer` as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "body-transformer-route",
    "uri": "/anything",
    "plugins": {
      "body-transformer": {
        "request": {
          "input_format": "plain",
          "template": "{\"message\": \"{* string.gsub(_body, \"not \", \"\") *}\"}"
        }
      }
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org:80": 1
      }
    }
  }'
```

â¶ Set the `input_format` to `plain`.

â· Set a template which removes `not` and a subsequent space from the body string.

Send a POST request to the route:

```
curl "http://127.0.0.1:9080/anything" -X POST \
  -d 'not actually json' \
  -i
```

You should see a response similar to the following:

```
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "{\"message\": \"actually json\"}": ""
  },
  "headers": {
    ...
  }, 
  ...
}
```

### Transform Multipart Media Type[â](#transform-multipart-media-type "Direct link to Transform Multipart Media Type")

The following example demonstrates how to transform requests with `multipart` media type.

Create a request transformation template which adds a `status` to the body based on the `age` provided in the request body:

```
req_template=$(cat <<EOF | awk '{gsub(/"/,"\\\"");};1'
{%
  local core = require 'apisix.core'
  local cjson = require 'cjson'
  
  if tonumber(context.age) > 18 then
      context._multipart:set_simple("status", "adult")
  else
      context._multipart:set_simple("status", "minor")
  end
  
  local body = context._multipart:tostring()
%}{* body *}
EOF
)
```

Create a route with `body-transformer` as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "body-transformer-route",
    "uri": "/anything",
    "plugins": {
      "body-transformer": {
        "request": {
          "input_format": "multipart",
          "template": "'"$req_template"'"
        }
      }
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org:80": 1
      }
    }
  }'
```

â¶ Set the `input_format` to `multipart`.

â· Set to the previously created request template.

Send a multipart POST request to the route:

```
curl -X POST \
  -F "name=john" \
  -F "age=10" \
  "http://127.0.0.1:9080/anything"
```

You should see a response similar to the following:

```
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "age": "10", 
    "name": "john", 
    "status": "minor"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Content-Length": "361", 
    "Content-Type": "multipart/form-data; boundary=------------------------qtPjk4c8ZjmGOXNKzhqnOP", 
    ...
  }, 
  ...
}
```

### Transform Response Body Based on Consumer Identity[â](#transform-response-body-based-on-consumer-identity "Direct link to Transform Response Body Based on Consumer Identity")

The following example demonstrates how to customize response body transformations based on different consumer identities. The example shows how to return different response formats to different consumers while filtering sensitive fields and renaming properties.

Create the response transformation template that applies different transformations based on the consumer identity:

```
rsp_template=$(cat <<EOF | awk '{gsub(/"/,"\\\"");};1' | awk '{$1=$1};1' | tr -d '\r\n'
{% local consumer_name = _ctx.consumer and _ctx.consumer.username or "" %}
{% if consumer_name == "consumerA" then %}
{
  "user_id": {* user_id *},
  "display_name": {* _escape_json(username) *},
  "email": {* _escape_json(email) *}
}
{% elseif consumer_name == "consumerB" then %}
{
  "user_id": {* user_id *},
  "email": {* _escape_json(email) *},
  "balance": {* balance *}
}
{% else %}
{* _body *}
{% end %}
EOF
)
```

Create three consumers with `key-auth` configured:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "username": "consumerA",
    "plugins": {
      "key-auth": {
        "key": "consumerA"
      }
    }
  }'

curl "http://127.0.0.1:9180/apisix/admin/consumers" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "username": "consumerB",
    "plugins": {
      "key-auth": {
        "key": "consumerB"
      }
    }
  }'

curl "http://127.0.0.1:9180/apisix/admin/consumers" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "username": "consumerC",
    "plugins": {
      "key-auth": {
        "key": "consumerC"
      }
    }
  }'
```

Create a route with `body-transformer`, `key-auth`, and `mocking` plugins:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "body-transformer-route",
    "uri": "/mock",
    "plugins": {
      "key-auth": {},
      "mocking": {
        "response_example": "{\"user_id\":1001,\"username\":\"john_doe\",\"email\":\"john@example.com\",\"phone\":\"+1-555-0123\",\"balance\":1250.50}"
      },
      "body-transformer": {
        "response": {
          "input_format": "json",
          "template": "'"$rsp_template"'"
        }
      }
    }
  }'
```

â¶ Configure the [`mocking`](https://docs.api7.ai/hub/mocking.md) plugin to return a sample upstream response.

â· Set the response input format as JSON.

â¸ Set the transformation template that customizes the response based on consumer identity.

Send requests with different `apikey` headers to verify the response transformations:

Send a request as `consumerA`:

```
curl "http://127.0.0.1:9080/mock" -H "apikey: consumerA"
```

You should see a response similar to the following, which demonstrates these transformations:

* The `username` field has been renamed to `display_name`
* The sensitive `phone` and `balance` fields have been filtered out

```
{
  "user_id": 1001,
  "display_name": "john_doe",
  "email": "john@example.com"
}
```

Send a request as `consumerB`:

```
curl "http://127.0.0.1:9080/mock" -H "apikey: consumerB"
```

You should see a response similar to the following, which demonstrates these transformations:

* The `username` and `phone` fields have been filtered out
* The `balance` field has been preserved

```
{
  "user_id": 1001,
  "email": "john@example.com",
  "balance": 1250.50
}
```

Send a request as `consumerC`:

```
curl "http://127.0.0.1:9080/mock" -H "apikey: consumerC"
```

You should see a response similar to the following, which shows that the original response is returned unchanged:

```
{
  "user_id": 1001,
  "username": "john_doe",
  "email": "john@example.com",
  "phone": "+1-555-0123",
  "balance": 1250.50
}
```

### Transform Nested Response Body Based on Consumer Identity[â](#transform-nested-response-body-based-on-consumer-identity "Direct link to Transform Nested Response Body Based on Consumer Identity")

The following example demonstrates how to customize response body transformations based on different consumer identities. The example shows how to extract nested fields, reorganize data structures, and flatten nested objects while providing different response formats to different consumers based on their identity.

Create the response transformation template that extracts and reorganizes nested JSON fields based on the consumer identity:

```
rsp_template=$(cat <<EOF | awk '{gsub(/"/,"\\\"");};1' | awk '{$1=$1};1' | tr -d '\r\n'
{% local consumer_name = _ctx.consumer and _ctx.consumer.username or "" %}
{% if consumer_name == "consumerA" then %}
{
  "user_id": {* id *},
  "user_name": {* _escape_json(name) *},
  "email": {* _escape_json(profile.email) *},
  "location": {
    "city": {* _escape_json(profile.address.city) *},
    "country": {* _escape_json(profile.address.country) *}
  },
  "created_at": {* _escape_json(metadata.created_at) *}
}
{% elseif consumer_name == "consumerB" then %}
{
  "id": {* id *},
  "name": {* _escape_json(name) *},
  "status": {* _escape_json(status) *},
  "profile": {
    "email": {* _escape_json(profile.email) *},
    "address": {
      "city": {* _escape_json(profile.address.city) *}
    }
  }
}
{% else %}
{* _body *}
{% end %}
EOF
)
```

Create consumers with `key-auth` configured:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "username": "consumerA",
    "plugins": {
      "key-auth": {
        "key": "consumerA"
      }
    }
  }'

curl "http://127.0.0.1:9180/apisix/admin/consumers" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "username": "consumerB",
    "plugins": {
      "key-auth": {
        "key": "consumerB"
      }
    }
  }'

curl "http://127.0.0.1:9180/apisix/admin/consumers" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "username": "consumerC",
    "plugins": {
      "key-auth": {
        "key": "consumerC"
      }
    }
  }'
```

Create a route with `body-transformer`, `key-auth`, and `mocking` plugins using the nested structure template:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "body-transformer-route",
    "uri": "/mock",
    "plugins": {
      "key-auth": {},
      "mocking": {
        "response_example": "{\"id\":123,\"name\":\"John Doe\",\"status\":\"active\",\"profile\":{\"email\":\"john@example.com\",\"address\":{\"city\":\"New York\",\"country\":\"USA\"}},\"metadata\":{\"created_at\":\"2024-01-01\",\"tags\":[\"vip\",\"premium\"]}}"
      },
      "body-transformer": {
        "response": {
          "input_format": "json",
          "template": "'"$rsp_template"'"
        }
      }
    }
  }'
```

â¶ Configure the [`mocking`](https://docs.api7.ai/hub/mocking.md) plugin to return a sample nested upstream response.

â· Set the response input format as JSON.

â¸ Set the transformation template that handles nested JSON structures based on consumer identity.

Send a request as `consumerA` to verify the nested structure transformation:

```
curl "http://127.0.0.1:9080/mock" -H "apikey: consumerA"
```

You should see a response similar to the following, which demonstrates these nested field transformations:

* `profile.email` has been extracted to top-level `email`
* `profile.address.city` and `profile.address.country` have been combined into a new `location` object
* `metadata.created_at` has been extracted to top-level `created_at`

```
{
  "user_id": 123,
  "user_name": "John Doe",
  "email": "john@example.com",
  "location": {
    "city": "New York",
    "country": "USA"
  },
  "created_at": "2024-01-01"
}
```

Send a request as `consumerB` to verify the nested structure transformation:

```
curl "http://127.0.0.1:9080/mock" -H "apikey: consumerB"
```

You should see a response similar to the following, which demonstrates these transformations:

* The original `profile` object structure has been preserved
* `profile.address.country` and `metadata` fields have been filtered out

```
{
  "id": 123,
  "name": "John Doe",
  "status": "active",
  "profile": {
    "email": "john@example.com",
    "address": {
      "city": "New York"
    }
  }
}
```

Send a request as `consumerC` to verify the nested structure transformation:

```
curl "http://127.0.0.1:9080/mock" -H "apikey: consumerC"
```

You should see a response similar to the following, which shows that the original nested response is returned unchanged:

```
{
  "id": 123,
  "name": "John Doe",
  "status": "active",
  "profile": {
    "email": "john@example.com",
    "address": {
      "city": "New York",
      "country": "USA"
    }
  },
  "metadata": {
    "created_at": "2024-01-01",
    "tags": ["vip", "premium"]
  }
}
```
