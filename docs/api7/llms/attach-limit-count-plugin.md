# Source: https://docs.api7.ai/cloud/getting-started/attach-limit-count-plugin.md

# Attach the Limit Count Plugin

So far, you know how to configure [service](https://docs.api7.ai/cloud/concepts/service.md) and [route](https://docs.api7.ai/cloud/concepts/route.md) to let your APISIX instance run as your expectation. This section will extend the route with the [Limit Count Plugin](https://docs.api7.ai/cloud/guides/traffic-management/limit-count.md). Limit Count protects your route from being overwhelmed by a large number of requests.

To add the Limit Count plugin for HTTPBIN service. Do the following:

1. Open the [API7 Cloud console](https://console.api7.cloud).

2. From the left navigation bar, choose **API Management**, then select **Services** from the secondary menu.

3. Click on the HTTPBIN Service name, enter the Service details page.

4. Click on **Add Plugin**, select the Limit Count plugin.

5. Fill the form:

   <!-- -->

   * Set **Count** to `5`
   * Set **Period** to `60`.
   * Set **Rejected Status Code** to `429`.
   * Set **Error Message** to `{"error_msg":"Too many requests"}`.

In this case, we configure:

1. A gateway instance only accepts five requests in a minute (for the JSON route);
2. If the number of requests exceeds the limit, the gateway instance rejects the requests with the `429` status code, and the response body will be "Too many requests".

Now let's try to verify the Limit Count Plugin.

Again, we'll use [curl](https://curl.se/) for the verification. This time we'll send requests continuously.

```
for ((i=0; i<6; i++)); do
curl http://127.0.0.1:9080/v1/json -H 'Host: cloud.httpbin.org' -s -o/dev/null -w 'status code: %{http_code}\n'
done
```

The output will be:

```
status code: 200
status code: 200
status code: 200
status code: 200
status code: 200
status code: 429
```

As you can see, we sent `6` requests in a minute. The first `5` requests responded with a `200` status code, and the last one responded with the expected`429`, but what about the response body? Let's send a request separately through the below command.

```
curl http://127.0.0.1:9080/v1/json -H 'Host: cloud.httpbin.org' -s
```

You'll see `{"error_msg":"Too many requests"}` printed on the screen.

note

Apache APISIX wraps the error message in a JSON string.

info

The throttling quota might already reset when you run the above command. Try a few times if you don't see this output.

Congratulations, you've mastered using Limit Count plugin in your route.

## Next[â](#next "Direct link to Next")

[Summary](https://docs.api7.ai/cloud/getting-started/summary.md).
