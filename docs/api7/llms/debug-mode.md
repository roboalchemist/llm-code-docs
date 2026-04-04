# Source: https://docs.api7.ai/apisix/how-to-guide/troubleshooting/debug-mode.md

# Use Debug Mode

APISIX provides a debug mode to help developers better understand and troubleshoot the runtime behavior of the gateway. The complete configuration options can be found in [`debug.yaml`](https://github.com/apache/apisix/blob/master/conf/debug.yaml).

This guide will show you how to enable the debug mode to inspect what plugins are enabled on the requested route and how to add hooks to log input arguments and returned values of APISIX module's functions.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Install [Docker](https://docs.docker.com/get-docker/).
* Install [cURL](https://curl.se/) to send requests to APISIX for validation.
* Follow the [Getting Started tutorial](https://docs.api7.ai/apisix/getting-started/.md) to start a new APISIX instance in Docker or on Kubernetes.

## Enable Basic Debug Mode[â](#enable-basic-debug-mode "Direct link to Enable Basic Debug Mode")

Enabling the basic debug mode will allow you to inspect what plugins are enabled on the requested route in the `Apisix-Plugins` header.

By default, the debug mode is turned off. To enable the debug mode, you can set `basic.enable` to `true` in your `debug.yaml` file.

```
docker exec apisix-quickstart /bin/sh -c "echo '
basic:
  enable: true
#END
' > /usr/local/apisix/conf/debug.yaml"
```

The `debug.yaml` file is loaded into memory at startup and monitored for changes at a regular interval, so that you do not need to manually reload APISIX after updating the file.

info

The `debug.yaml` configurations should end with `#END`, or else APISIX will not load the configurations.

You can also use the `#END` flag as a breakpoint for APISIX to only load configurations up to the specified point.

To verify, create a route without any plugin:

* Admin API
* ADC

```
curl -i "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id": "getting-started-anything",
  "uri": "/anything",
  "upstream": {
    "type": "roundrobin",
    "nodes": {
      "httpbin.org:80": 1
    }
  }
}'
```

adc.yaml

```
services:
  - name: httpbin Service
    routes:
      - uris:
          - /anything
        name: getting-started-anything
    upstream:
      type: roundrobin
      nodes:
        - host: httpbin.org
          port: 80
          weight: 1
```

Synchronize the configuration to APISIX:

```
adc sync -f adc.yaml
```

Send a request to the route:

```
curl -i "http://127.0.0.1:9080/anything"
```

You should receive an `HTTP/1.1 200 OK` response and observe the following headers:

```
Content-Type: application/json
Content-Length: 390
Connection: keep-alive
Apisix-Plugins: no plugin
...
```

* Admin API
* ADC

Update the route with a plugin:

```
curl -i "http://127.0.0.1:9180/apisix/admin/routes/getting-started-anything" -X PATCH -d '
{
  "plugins": {
    "limit-count": {
      "count": 5,
      "time_window": 10,
      "rejected_code": 429
    }
  }
}'
```

Additionally, add a [global plugin](https://docs.api7.ai/apisix/key-concepts/plugin-global-rules.md):

```
curl -i "http://127.0.0.1:9180/apisix/admin/global_rules" -X PUT -d '{
  "id": "global-prometheus",
  "plugins": {
    "prometheus":{}
  }
}'
```

Update the route with a plugin and add another [global plugin](https://docs.api7.ai/apisix/key-concepts/plugin-global-rules.md):

adc.yaml

```
services:
  - name: httpbin Service
    routes:
      - uris:
          - /anything
        name: getting-started-anything
        plugins:
          limit-count:
            count: 5
            time_window: 10
            rejected_code: 429
    upstream:
      type: roundrobin
      nodes:
        - host: httpbin.org
          port: 80
          weight: 1
global_rules:
  prometheus: {}
```

Synchronize the configuration to APISIX:

```
adc sync -f adc.yaml
```

Send another request to the route:

```
curl -i "http://127.0.0.1:9080/anything"
```

You should receive an `HTTP/1.1 200 OK` response with headers similar to the following:

```
Content-Type: application/json
Content-Length: 388
Connection: keep-alive
X-RateLimit-Limit: 5
X-RateLimit-Remaining: 4
X-RateLimit-Reset: 10
Apisix-Plugins: limit-count, prometheus
...
```

info

If the plugin information cannot be included in a response header (e.g. L4 stream plugins), the debug information will be logged in the error log at the `warn` severity level.

## Configure Advanced Debug Mode[â](#configure-advanced-debug-mode "Direct link to Configure Advanced Debug Mode")

There are a few other advanced options in `debug.yaml` that you can configure.

### Log Function Input Arguments and Returned Values[â](#log-function-input-arguments-and-returned-values "Direct link to Log Function Input Arguments and Returned Values")

You can add hooks to [APISIX phases](https://docs.api7.ai/apisix/key-concepts/plugins.md#plugins-execution-lifecycle) to log input arguments and return values with the following configuration:

debug.yaml

```
basic:
  enable: true
hook_conf:
  enable: true
  name: hook_phase
  log_level: warn
  is_print_input_args: true
  is_print_return_value: true
hook_phase:
  apisix:
    - http_access_phase
    - http_header_filter_phase
    - http_body_filter_phase
    - http_log_phase
#END
```

â¶ Enable hook debug trace to log the target module function's input arguments or returned values.

â· Name of module and function list.

â¸ Severity level for input arguments and returned values in the error log.

â¹ Log the input arguments.

âº Log the return values.

â» Name of module and function list.

To verify, send a request to the route:

```
curl -i "http://127.0.0.1:9080/anything"
```

You should receive an `HTTP/1.1 200 OK` response and see the following information in the error log:

```
call require("apisix").http_access_phase() args:{}
call require("apisix").http_access_phase() return:{}
call require("apisix").http_header_filter_phase() args:{}
call require("apisix").http_header_filter_phase() return:{}
call require("apisix").http_body_filter_phase() args:{}
call require("apisix").http_body_filter_phase() return:{}
call require("apisix").http_log_phase() args:{}
call require("apisix").http_log_phase() return:{}
```

### Apply Advanced Debug Settings Dynamically[â](#apply-advanced-debug-settings-dynamically "Direct link to Apply Advanced Debug Settings Dynamically")

You can also log function input arguments and returned values dynamically when a certain header is present with the following configuration:

debug.yaml

```
docker exec apisix-quickstart /bin/sh -c "echo '
basic:
  enable: true
http_filter:
  enable: true
  enable_header_name: X-APISIX-Dynamic-Debug
hook_conf:
  enable: true
  name: hook_phase
  log_level: warn
  is_print_input_args: true
  is_print_return_value: true
hook_phase:
  apisix:
    - http_access_phase
    - http_header_filter_phase
    - http_body_filter_phase
    - http_log_phase
#END
```

â¶ Enable HTTP filter to dynamically apply advanced debug settings.

â· Log input arguments and returned values only when the request has the `X-APISIX-Dynamic-Debug` header.

To verify, send a request to the route without any header:

```
curl -i "http://127.0.0.1:9080/anything"
```

You should receive an `HTTP/1.1 200 OK` response but observe no debugging information in the error log.

Send another request with the debug header:

```
curl -i "http://127.0.0.1:9080/anything" -H "X-APISIX-Dynamic-Debug: 1"
```

You should receive an `HTTP/1.1 200 OK` response and see the following information in the error log:

```
call require("apisix").http_access_phase() args:{}
call require("apisix").http_access_phase() return:{}
call require("apisix").http_header_filter_phase() args:{}
call require("apisix").http_header_filter_phase() return:{}
call require("apisix").http_body_filter_phase() args:{}
call require("apisix").http_body_filter_phase() return:{}
call require("apisix").http_log_phase() args:{}
call require("apisix").http_log_phase() return:{}
```

## Manage `debug.yaml` by Environments[â](#manage-debugyaml-by-environments "Direct link to manage-debugyaml-by-environments")

You may wish to have different `debug.yaml` files for each environment, such as using `conf/debug-dev.yaml` for development and `conf/debug-prod.yaml` for production. This can be done by setting the `APISIX_PROFILE` variable.

For more details, see [Manage Configuration Files by Environments](https://docs.api7.ai/apisix/reference/configuration-files.md#manage-configuration-files-by-environments).

## Next Steps[â](#next-steps "Direct link to Next Steps")

You have now learned how to leverage the debug mode in APISIX for troubleshooting and the various debugging options it offers. You can find the complete configuration options in [`debug.yaml`](https://github.com/apache/apisix/blob/master/conf/debug.yaml).
