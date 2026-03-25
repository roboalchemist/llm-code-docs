# Source: https://ngrok.com/docs/agent/web-inspection-interface.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# ngrok Agent Web Inspection Interface

> Learn how to use the ngrok agent's web inspection interface at localhost:4040 to view HTTP requests and responses in real-time.

The ngrok agent ships with a realtime inspection interface which allows you to see what traffic is sent to your upstream service and what responses it is returning.

The Web Inspection Interface is only available in the ngrok standalone agent and not in the ngrok Agent SDKs. If you are interested in viewing traffic across all endpoints, longer retention periods, or sharing traffic events with other teammates, check out the [Traffic Inspector in the ngrok Dashboard](/obs/traffic-inspection/#ngrok-traffic-inspector) instead.

## Inspecting requests

Every HTTP request through your endpoints will be displayed in the inspection interface. After you start the ngrok agent, open [http://localhost:4040](http://localhost:4040) in a browser on the same machine. You will see all of the details of every request and response including the time, duration, source IP, headers, query parameters, request payload and response body as well as the raw bytes on the wire.

The inspection interface has a few limitations. If an entity-body is too long, ngrok may only capture the initial portion of the request body. Furthermore, ngrok does not display provisional 100 responses from a server.

Inspection is only supported for HTTP endpoints. TCP and TLS endpoints do not support any inspection and will not show up in the inspection interface.

###### Detailed introspection of HTTP requests and responses

<img src="https://mintcdn.com/ngrok/xK-DuyYN6snvqzBj/img/docs/inspect2.png?fit=max&auto=format&n=xK-DuyYN6snvqzBj&q=85&s=2a72412c88ff9501344a878172efc618" alt="" width="689" height="501" data-path="img/docs/inspect2.png" />

## Request body validation

ngrok has special support for the most common data interchange formats in use on the web. Any XML or JSON data in request or response bodies is automatically pretty-printed and checked for syntax errors.

###### The location of a JSON syntax error is highlighted

<img src="https://mintcdn.com/ngrok/CVwQ3NYweNUKVdSR/img/docs/syntax.png?fit=max&auto=format&n=CVwQ3NYweNUKVdSR&q=85&s=b25dce6c75b46af2adc60a89d883ab38" alt="" width="520" height="581" data-path="img/docs/syntax.png" />

## Filtering requests

Your upstream service may receive many requests, but you are often only interested in inspecting some of them. You can filter the requests that ngrok displays to you. You can filter based on the request path, response status code, size of the response body, duration of the request and the value of any header.

###### Click the filter bar for filtering options

<img src="https://mintcdn.com/ngrok/xK-DuyYN6snvqzBj/img/docs/inspect-filter-select.png?fit=max&auto=format&n=xK-DuyYN6snvqzBj&q=85&s=c4ecdd7af294c60cbc8fe4d87cdbc4a9" alt="" width="331" height="187" data-path="img/docs/inspect-filter-select.png" />

You may specify multiple filters. If you do, requests will only be shown if they much all filters.

###### Filter requests by path and status code

<img src="https://mintcdn.com/ngrok/xK-DuyYN6snvqzBj/img/docs/inspect-filter.png?fit=max&auto=format&n=xK-DuyYN6snvqzBj&q=85&s=4f006e375f356284a478048f5c39b9b0" alt="" width="605" height="175" data-path="img/docs/inspect-filter.png" />

## Replaying requests

Developing for webhooks issued by external APIs can often slow down your development cycle by requiring you do some work, like dialing a phone, to trigger the hook request. ngrok allows you to replay any request with a single click, dramatically speeding up your iteration cycle. Click the **Replay** button at the top-right corner of any request on the web inspection UI to replay it.

Replay works via the local agent sending the request directly to your upstream service. As such, the replayed request will not be subject to any policies that exist on your Cloud Endpoint since those are applied prior to the request reaching the local agent. If you are interested in replaying the original request before the endpoint policies are applied and testing new policies, please use the [Traffic Inspector in the ngrok Dashboard](/obs/traffic-inspection/#ngrok-traffic-inspector).

###### Replay any request against your web server with one click

<img src="https://mintcdn.com/ngrok/CVwQ3NYweNUKVdSR/img/docs/replay2.png?fit=max&auto=format&n=CVwQ3NYweNUKVdSR&q=85&s=c13a904138bff33f0a45949bc8e1ad2c" alt="" width="586" height="282" data-path="img/docs/replay2.png" />

## Replaying modified requests

Sometimes you want to modify a request before you replay it to test a new behavior in your upstream service.

###### Click the dropdown arrow on the 'Replay' button to modify a request before it is replayed

<img src="https://mintcdn.com/ngrok/CVwQ3NYweNUKVdSR/img/docs/replay-modify-button.png?fit=max&auto=format&n=CVwQ3NYweNUKVdSR&q=85&s=d9123945f70d7c961ba03dc4e00323c0" alt="" width="588" height="180" data-path="img/docs/replay-modify-button.png" />

The replay editor allows you to modify every aspect of the HTTP request before replaying it, including the method, path, headers, trailers, and request body.

###### The request replay modification editor

<img src="https://mintcdn.com/ngrok/CVwQ3NYweNUKVdSR/img/docs/replay-modify.png?fit=max&auto=format&n=CVwQ3NYweNUKVdSR&q=85&s=e1ff26c559fc8655cf461791f7ce3a23" alt="" width="625" height="784" data-path="img/docs/replay-modify.png" />

## ngrok Agent status page

ngrok's local web interface has a dedicated status page that shows configuration and metrics information about the running ngrok process. You can access it at [http://localhost:4040/status](http://localhost:4040/status).

The status page displays the configuration of each running endpoint and any global configuration options that ngrok has parsed from its configuration file.

###### Endpoint and global configuration

<img src="https://mintcdn.com/ngrok/CVwQ3NYweNUKVdSR/img/docs/status-configuration.png?fit=max&auto=format&n=CVwQ3NYweNUKVdSR&q=85&s=8dc45a776b10fdc49094a7e179b757ff" alt="" width="489" height="729" data-path="img/docs/status-configuration.png" />

The status page also display metrics about the traffic through each endpoint. It display connection rates and connection duration percentiles for all endpoints. For HTTP endpoints, it also displays http request rates and http response duration percentiles.

###### Endpoint traffic metrics

<img src="https://mintcdn.com/ngrok/CVwQ3NYweNUKVdSR/img/docs/status-metrics.png?fit=max&auto=format&n=CVwQ3NYweNUKVdSR&q=85&s=4c771bd9b760fa08f4a83c183625663c" alt="" width="566" height="675" data-path="img/docs/status-metrics.png" />


Built with [Mintlify](https://mintlify.com).