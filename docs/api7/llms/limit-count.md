# Source: https://docs.api7.ai/hub/limit-count.md

# Source: https://docs.api7.ai/cloud/references/plugins/traffic-management/limit-count.md

# Source: https://docs.api7.ai/cloud/guides/traffic-management/limit-count.md

# Source: https://docs.api7.ai/cloud/references/plugins/traffic-management/limit-count.md

# Source: https://docs.api7.ai/cloud/guides/traffic-management/limit-count.md

# Rate Limiting (Limit Count)

The Limit Count plugin limits the number of requests can be handled (in the given time period) for a [service](https://docs.api7.ai/cloud/concepts/service.md) or [route](https://docs.api7.ai/cloud/concepts/route.md).

info

The quota configured on API7 Cloud is for individual gateway instances. It's exclusive instead of shared (among all of your instances).

You can configure the Limit Count plugin in a service or a route.

1. If you configure the Limit Count plugin only for a service, it'll affect all routes in this Service.
2. If you configure the Limit Count plugin only for a route, then the Limit Count plugin only affects this route.
3. If you configure the Limit Count plugin for both a service and a route, the Limit Count plugin in route takes precedence.

> When you configure the Limit Count plugin in service, all routes in it won't share the rating quota, they don't affect each other.

## How to Configure Limit Count Plugin[â](#how-to-configure-limit-count-plugin "Direct link to How to Configure Limit Count Plugin")

You can configure the Limit Count plugin when creating or updating a service or route.

![Limit Count Plugin](https://static.api7.ai/2023/01/03/63b3dec96c55d.png)

In the above image, you can see:

1. Apache APISIX only accepts five requests in `1` minute.
2. The status code will be `429` if Apache APISIX rejects the request.
3. The response body will be `Too many requests` if Apache APISIX rejects the request.

## How to Test the Limit Count Plugin[â](#how-to-test-the-limit-count-plugin "Direct link to How to Test the Limit Count Plugin")

First, deploy a gateway instance and connect to the API7 Cloud. Please see [Add a gateway instance and connect it to the API7 Cloud](https://docs.api7.ai/cloud/getting-started/add-gateway-instance.md) to learn the details.

Then we can send a bunch of requests to verify the Limit Count plugin.

```
for ((i=0; i<6; i++)); do
  curl http://127.0.0.1:9080/v1/json -H 'Host: cloud.httpbin.org' -s -o/dev/null -w 'status code: %{http_code}\n'
done
```

```
status code: 200
status code: 200
status code: 200
status code: 200
status code: 200
status code: 429
```

```
curl http://127.0.0.1:9080/v1/json -H 'Host: cloud.httpbin.org' -s
```

```
{"error_msg":"Too many requests"}
```

As you can see, Apache APISIX rejects the 6th request as expected, and we sent another request to check the response body, which is also expected.

## What's Next[â](#whats-next "Direct link to What's Next")

* [Limit Count Plugin Reference](https://docs.api7.ai/cloud/references/plugins/traffic-management/limit-count.md)
* [Apache APISIX Limit Count Plugin](https://apisix.apache.org/docs/apisix/next/plugins/limit-count)
