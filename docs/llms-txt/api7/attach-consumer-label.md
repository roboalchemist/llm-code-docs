# Source: https://docs.api7.ai/hub/attach-consumer-label.md

# attach-consumer-label

The `attach-consumer-label` plugin attaches custom consumer-related labels, in addition to `X-Consumer-Username` and `X-Credential-Identifier`, to authenticated requests, for upstream services to differentiate between consumers and implement additional logics.

## Example[â](#example "Direct link to Example")

### Attach Consumer Labels[â](#attach-consumer-labels "Direct link to Attach Consumer Labels")

The following example demonstrates how you can attach custom labels to request headers before authenticated requests are forwarded to upstream services. If the request is rejected, you should not see any consumer labels attached to request headers. If a certain label value is not configured on the consumer but referenced in the `attach-consumer-label` plugin, the corresponding header will also not be attached.

Create a consumer `john` with custom labels:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "username": "john",
    "labels": {
      "department": "devops",
      "company": "api7"
    }
  }'
```

â¶ Label the `department` information for the consumer.

â· Label the `company` information for the consumer.

Configure the `key-auth` credential for the consumer `john`:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers/john/credentials" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "cred-john-key-auth",
    "plugins": {
      "key-auth": {
        "key": "john-key"
      }
    }
  }'
```

Create a route enabling the `key-auth` and `attach-consumer-label` plugins:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "attach-consumer-label-route",
    "uri": "/get",
    "plugins": {
      "key-auth": {},
      "attach-consumer-label": {
        "headers": {
          "X-Consumer-Department": "$department",
          "X-Consumer-Company": "$company",
          "X-Consumer-Role": "$role"
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

â¶ Attach the `department` consumer label value in the `X-Consumer-Department` request header.

â· Attach the `company` consumer label value in the `X-Consumer-Company` request header.

â¸ Attach the `role` consumer label value in the `X-Consumer-Role` request header. As the `role` label is not configured on the consumer, it is expected that the header will not appear in the request forwarded to the upstream service.

tip

The consumer label references must be prefixed by a dollar sign (`$`).

To verify, send a request to the route with the valid credential:

```
curl -i "http://127.0.0.1:9080/get" -H 'apikey: john-key'
```

You should see an `HTTP/1.1 200 OK` response similar to the following:

```
{
  "args": {}, 
  "headers": {
    "Accept": "*/*", 
    "Apikey": "john-key", 
    "Host": "127.0.0.1",
    "X-Consumer-Username": "john",
    "X-Credential-Identifier": "cred-john-key-auth", 
    "X-Consumer-Company": "api7",
    "X-Consumer-Department": "devops",
    "User-Agent": "curl/8.6.0", 
    "X-Amzn-Trace-Id": "Root=1-66e5107c-5bb3e24f2de5baf733aec1cc", 
    "X-Forwarded-Host": "127.0.0.1"
  }, 
  "origin": "192.168.65.1, 205.198.122.37", 
  "url": "http://127.0.0.1/get"
}
```
