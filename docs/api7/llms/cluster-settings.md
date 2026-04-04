# Source: https://docs.api7.ai/cloud/guides/product/cluster-settings.md

# Tweak Cluster Settings

The [Cluster](https://docs.api7.ai/cloud/concepts/cluster.md) provided by API7 Cloud is also dynamic, with some cluster level settings. This guide will show you how to tweak the cluster settings to satisfy your personalized needs.

## Prepare the Environment[â](#prepare-the-environment "Direct link to Prepare the Environment")

Also, what we'll adjust are cluster scope settings. We still need to deploy a gateway instance and create a [service](https://docs.api7.ai/cloud/concepts/service.md) and [route](https://docs.api7.ai/cloud/concepts/route.md), since we will verify the setting changes via API requests.

### Deploy Apache APISIX[â](#deploy-apache-apisix "Direct link to Deploy Apache APISIX")

Please refer to [How to Deploy Apache APISIX](https://docs.api7.ai/cloud/guides/product/how-to-deploy-apache-apisix.md) to learn how to deploy Apache APISIX and connect it to API7 Cloud. In this guide, we'll deploy an Apache APISIX instance on Docker.

### Create Service and Route[â](#create-service-and-route "Direct link to Create Service and Route")

We'll create a Service with the following details in this guide.

1. The Service name is `cp-setting-app`.
2. The path prefix is `/v1`.
3. The HTTP Host is `cp-setting.httpbin.org`.
4. The upstream URL is `https://httpbin.org`.

Besides, we'll create a route inside the `cp-setting-app` Service.

1. The route name is `anything`.
2. The path is `/anyting` (exact match), and strip the path prefix.
3. It accepts the GET and POST methods.

note

If you don't know how to configure a service and route, please refer to the [Getting Started](https://docs.api7.ai/cloud/getting-started/.md) guides first.

## Tweak Cluster Settings[â](#tweak-cluster-settings "Direct link to Tweak Cluster Settings")

## Client Settings[â](#client-settings "Direct link to Client Settings")

### Maximum Request Body Size[â](#maximum-request-body-size "Direct link to Maximum Request Body Size")

By default, the maximum API request body size is not limited, and thus the backend service might be overwhelmed by these large messages.

API7 Cloud allows you to configure an explicit limitation for the request Apache APISIX will reject an API request with a too large body directly.

![CP Maximum Request Body Size](https://static.api7.ai/uploads/2023/01/12/u3h3VuXQ_cluster-maximum-request-body-size.png)

In this case, we restrict the **Maximum Request Body Size** to `16` bytes. Now let's verify it.

```
curl http://127.0.0.1:9080/v1/anything -H 'Host: cp-setting.httpbin.org' -i -d '{"message": "hello world"}'
```

```
HTTP/1.1 413 Request Entity Too Large
Date: Mon, 29 Aug 2022 05:45:00 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 180
Connection: close
Server: APISIX/2.15.0

<html>
<head><title>413 Request Entity Too Large</title></head>
<body>
<center><h1>413 Request Entity Too Large</h1></center>
<hr><center>openresty</center>
</body>
</html>
```

The API request we sent has a body whose size is `26`, and Apache APISIX rejected it. The status code is `413`.

Now let's send another API request with a more petite body (size is `16`), and Apache APISIX will typically forward the request to the backend.

```
curl http://127.0.0.1:9080/v1/anything -H 'Host: cp-setting.httpbin.org' -i -d '{"status": "OK"}'
```

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 550
Connection: keep-alive
Date: Mon, 29 Aug 2022 05:47:19 GMT
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
Server: APISIX/2.15.0
X-APISIX-Upstream-Status: 200

{
  "args": {},
  "data": "",
  "files": {},
  "form": {
    "{\"status\": \"OK\"}": ""
  },
  "headers": {
    "Accept": "*/*",
    "Content-Length": "16",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "cp-setting.httpbin.org",
    "User-Agent": "curl/7.76.1",
    "X-Amzn-Trace-Id": "Root=1-630c52e7-52caa56523b543220dbcc30e",
    "X-Forwarded-Host": "cp-setting.httpbin.org"
  },
  "json": null,
  "method": "POST",
  "origin": "172.17.0.1, 61.241.66.251",
  "url": "https://cp-setting.httpbin.org/anything"
}
```

tip

Set **Maximum Request Body Size** to `0` can disable the API request body size restriction.

### Real IP Replacement[â](#real-ip-replacement "Direct link to Real IP Replacement")

The client IP address that Apache APISIX sees might not be the actual one if there are other proxy components in front of it (e.g., Cloud Load Balancer). However, users may want to use the actual client IP address to make critical decisions and decide if the current API request should succeed.

API7 Cloud allows users to configure the real IP replacement rule to fetch the desired IP from API requests (e.g., header, query string).

![CP Real IP Replacement](https://static.api7.ai/uploads/2023/01/12/V4FY522L_cluster-real-ip-replacement.png)

In this case, if a request is sent from `172.17.0.1`, Apache APISIX will try to replace the client IP address from the HTTP header `X-My-Client-IP`. The mechanism we expose the port `9080` to the host decides that the original client IP address the Apache APISIX seen is its container address, not `127.0.0.1` (when we send API requests from the host).

important

It's recommended to set the **Trusted Addresses** field to avoid the IP address being tampered with accidentally.

To check if the IP replacement takes effect, we configure the Response Rewrite plugin on the `cp-setting-app`, and let it echo. After the replacement, the client IP (the variable `$remote_addr`).

![CP Add Response Rewrite Plugin](https://static.api7.ai/2022/12/30/cp-add-resp-rewrite-plugin.png)

Let's send a request to check if the IP replacement takes effect.

```
curl http://127.0.0.1:9080/v1/anything -H 'Host: cp-setting.httpbin.org' -v -H 'X-My-Client-IP: 10.0.5.3'
```

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 462
Connection: keep-alive
Date: Wed, 31 Aug 2022 06:21:27 GMT
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
Server: APISIX/2.15.0
X-APISIX-Upstream-Status: 200
X-My-Client-IP: 10.0.5.3

{
  "args": {},
  "data": "",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Host": "cp-setting.httpbin.org",
    "User-Agent": "curl/7.76.1",
    "X-Amzn-Trace-Id": "Root=1-630efde7-10025c9b58850e3a01a2ffb7",
    "X-Forwarded-Host": "cp-setting.httpbin.org",
    "X-My-Client-Ip": "10.0.5.3"
  },
  "json": null,
  "method": "GET",
  "origin": "172.17.0.1, 61.241.66.251",
  "url": "http://cp-setting.httpbin.org/anything"
}
```

The `X-My-Client-IP` is shown in the response headers, and the value is the same as the one we carry in the request header `X-My-Client-IP`. This means the remote IP address replacement takes effect in Apache APISIX.

tip

Apache APISIX adds the `X-Real-IP` header when it forwards requests to the backend. The value is also affected by the client's IP replacement. You won't see it in the `anything` API response body since HTTPBIN removes it.

## Observability Settings[â](#observability-settings "Direct link to Observability Settings")

![CP Upload Prometheus Metrics](https://static.api7.ai/uploads/2023/01/12/F4kqxxh9_cluster-setting-upload-prometheus-metrics.png)

### Upload Prometheus Metrics[â](#upload-prometheus-metrics "Direct link to Upload Prometheus Metrics")

You can also opt to disable to upload Prometheus metrics from gateway instances if you don't want to expose these gateway metrics to API7 Cloud, or you already have an APM system.

### Show All Upstream Status in Response Header[â](#show-all-upstream-status-in-response-header "Direct link to Show All Upstream Status in Response Header")

By default, Apache APISIX will show the upstream status code in the HTTP response header `X-APISIX-Upstream-Status` if the upstream is abnormal and the status code is `5XX`. You can also enable the **Show All Upstream Status in Response Header**. After that, whatever the upstream status code is, it will be shown in `X-APISIX-Upstream-Status`.

```
curl http://127.0.0.1:9080/v1/anything -H 'Host: cp-setting.httpbin.org' -i
```

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 428
Connection: keep-alive
Date: Mon, 29 Aug 2022 06:25:25 GMT
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
Server: APISIX/2.15.0
X-APISIX-Upstream-Status: 200

{
  "args": {},
  "data": "",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Host": "cp-setting.httpbin.org",
    "User-Agent": "curl/7.76.1",
    "X-Amzn-Trace-Id": "Root=1-630c5bd5-0bcdde1d56a3ace44df32a62",
    "X-Forwarded-Host": "cp-setting.httpbin.org"
  },
  "json": null,
  "method": "GET",
  "origin": "172.17.0.1, 61.241.66.251",
  "url": "https://cp-setting.httpbin.org/anything"
}
```

### Rotate Logs[â](#rotate-logs "Direct link to Rotate Logs")

The error log and access log files generated by the Apache APISIX will grow over time if you don't rotate them. These files may cause a full disk problem, especially when you deploy Apache APISIX on bare metal. API7 Cloud allows you to configure the log rotate in cluster settings.

![CP Log Rotate](https://static.api7.ai/uploads/2023/01/12/JqIGbw3G_cluster-log-rotate.png)

In this case, we hope Apache APISIX generates a log file every `10` seconds or if the number of log entries reaches `1000`. The Apache APISIX will compress generated log file.

Wait for a while after saving the settings, and execute the following command to see the log files.

```
docker exec -it <Apache APISIX Container ID> ls -l logs/
```

## API Proxy Settings[â](#api-proxy-settings "Direct link to API Proxy Settings")

![CP API Proxy Settings](https://static.api7.ai/uploads/2023/01/12/3LAa64uk_cluster-api-proxy-settings.png)

### Enable Request Buffering[â](#enable-request-buffering "Direct link to Enable Request Buffering")

By default, Apache APISIX will read the API request body in advance before forwarding it to the backend, Apache APISIX may use the disk to buffer the content if the memory buffer size is not sufficient to hold the whole API request body may hurt the performance due to the slow disk.

You can disable the **Enable Request Buffering** option in the cluster settings. After that, Apache APISIX will forward the API request body synchronously.

important

When you disable the request buffering, the retry mechanism cannot work for API requests with the request body. Since Apache APISIX doesn't buffer them.

### Server Header Customization[â](#server-header-customization "Direct link to Server Header Customization")

You can rewrite the `Server` header in API response in cluster settings if you have the following needs:

1. avoid showing the specific Apache APISIX version to clients, or
2. show a custom server name due to the business needs

#### Avoid showing Apache APISIX version[â](#avoid-showing-apache-apisix-version "Direct link to Avoid showing Apache APISIX version")

![CP Hide Apache APISIX Version](https://static.api7.ai/uploads/2023/01/12/D7xd0VEE_cluster-hide-apisix-version.png)

Now let's send a request to verify it.

```
curl http://127.0.0.1:9080/v1/anything -H 'Host: cp-setting.httpbin.org' -i
```

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 428
Connection: keep-alive
Date: Mon, 29 Aug 2022 07:01:47 GMT
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
Server: APISIX
X-APISIX-Upstream-Status: 200

{
  "args": {},
  "data": "",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Host": "cp-setting.httpbin.org",
    "User-Agent": "curl/7.76.1",
    "X-Amzn-Trace-Id": "Root=1-630c645b-5e1c6fc4761664a9444ba956",
    "X-Forwarded-Host": "cp-setting.httpbin.org"
  },
  "json": null,
  "method": "GET",
  "origin": "172.17.0.1, 61.241.66.251",
  "url": "https://cp-setting.httpbin.org/anything"
}
```

As you can see, the version information is not in the `Server` header.

#### Show a Custom Server Name[â](#show-a-custom-server-name "Direct link to Show a Custom Server Name")

![CP Custom Server Name](https://static.api7.ai/uploads/2023/01/12/YBNeFs6y_cluster-custom-server-name.png)

Let's send an API request to check if the change takes effect.

```
curl http://127.0.0.1:9080/v1/anything -H 'Host: cp-setting.httpbin.org' -i
```

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 428
Connection: keep-alive
Date: Mon, 29 Aug 2022 07:05:09 GMT
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
Server: My-API-Gateway
X-APISIX-Upstream-Status: 200

{
  "args": {},
  "data": "",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Host": "cp-setting.httpbin.org",
    "User-Agent": "curl/7.76.1",
    "X-Amzn-Trace-Id": "Root=1-630c6525-6e7d0e2f7cc339d85018653a",
    "X-Forwarded-Host": "cp-setting.httpbin.org"
  },
  "json": null,
  "method": "GET",
  "origin": "172.17.0.1, 61.241.66.251",
  "url": "https://cp-setting.httpbin.org/anything"
}
```

As you can see, the `Server` header is `My-API-Gateway`.

### URI Handling[â](#uri-handling "Direct link to URI Handling")

You may want to apply some changes for URI. Currently, API7 Cloud allows users to delete the tailing slash, so that URIs like `/v1/anything/` will have the same effect as `/v1/anything`.

![CP Delete Tailing Slash](https://static.api7.ai/uploads/2023/01/12/tGtNgEuP_cluster-delete-tail-slash.png)

Now let's send an API request to `/v1/anything/`.

```
curl http://127.0.0.1:9080/v1/anything/ -H 'Host: cp-setting.httpbin.org' -i
```

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 428
Connection: keep-alive
Date: Mon, 29 Aug 2022 07:26:02 GMT
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
Server: APISIX
X-APISIX-Upstream-Status: 200

{
  "args": {},
  "data": "",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Host": "cp-setting.httpbin.org",
    "User-Agent": "curl/7.76.1",
    "X-Amzn-Trace-Id": "Root=1-630c6a09-181abf2d04ab2e4a278efa9b",
    "X-Forwarded-Host": "cp-setting.httpbin.org"
  },
  "json": null,
  "method": "GET",
  "origin": "172.17.0.1, 61.241.66.251",
  "url": "https://cp-setting.httpbin.org/anything"
}
```

The API request is handled by Apache APISIX just like `/v1/anything`.

## See Also[â](#see-also "Direct link to See Also")

* [Apache APISIX Client Control Plugin](https://apisix.apache.org/docs/apisix/plugins/client-control/)
* [Apache APISIX Real IP Plugin](https://apisix.apache.org/docs/apisix/plugins/real-ip/)
* [Apache APISIX Log Rotate Plugin](https://apisix.apache.org/docs/apisix/plugins/log-rotate/)
* [Apache APISIX Proxy Control Plugin](https://apisix.apache.org/docs/apisix/plugins/proxy-control/)
* [Apache APISIX Static Configuration](https://github.com/apache/apisix/blob/master/conf/config-default.yaml)
