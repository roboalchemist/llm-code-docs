# Source: https://docs.api7.ai/enterprise/best-practices/devops-adc.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/best-practices/devops-adc.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/best-practices/devops-adc.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/best-practices/devops-adc.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/best-practices/devops-adc.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/best-practices/devops-adc.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/best-practices/devops-adc.md

# Source: https://docs.api7.ai/enterprise/3.8.x/best-practices/devops-adc.md

# Source: https://docs.api7.ai/enterprise/3.7.x/best-practices/devops-adc.md

# Source: https://docs.api7.ai/enterprise/3.6.x/best-practices/devops-adc.md

# Source: https://docs.api7.ai/enterprise/3.5.x/best-practices/devops-adc.md

# Source: https://docs.api7.ai/enterprise/3.4.x/best-practices/devops-adc.md

# Source: https://docs.api7.ai/enterprise/3.3.x/best-practices/devops-adc.md

# Manage API7 Enterprise Declaratively

The API7 Declarative CLI (ADC) provides tooling to configure API7 Enterprise declaratively instead of the Admin API or the dashboard.

ADC uses a YAML file (`adc.yaml`) as the source of truth for configuring API7 Enterprise.

It is quite easy for DevOps teams to integrate with existing version control systems and CI/CD pipelines.

This document guides you in setting up ADC and using it to manage API7 Enterprise. You will learn how to:

1. Configure ADC and connect it to an API7 Enterprise instance
2. Sync configurations to the connected instance
3. Modify configurations, view modifications, and sync modifications

note

1. `adc convert` supports converting an OpenAPI 3.0 definition file to an ADC configuration file (`adc.yaml`). However, this conversion can be incomplete, and you might need to modify the converted configuration file to include authorization policies, bind to a service ID, and so on. API7.ai plans to improve this in the future.
2. Regardless of your version control system or firewall policies, ADC can work if it has access to the Admin API. The examples in the document have ADC installed on a local computer.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

1. [Install API7 Enterprise](https://docs.api7.ai/enterprise/3.3.x/getting-started/install-api7-ee.md).

## Install ADC[â](#install-adc "Direct link to Install ADC")

ADC binaries are available for macOS, Linux, and Windows. Download and install the appropriate binary by running:

```
export ADC_VERSION="0.8.0"
export ADC_OS="darwin" # or linux, windows
export ADC_ARC="arm64" # or amd64

wget "https://run.api7.ai/adc/release/adc_${ADC_VERSION}_${ADC_OS}_${ADC_ARC}.tar.gz"
tar -zxvf "adc_${ADC_VERSION}_${ADC_OS}_${ADC_ARC}.tar.gz"
mv adc /usr/local/bin/adc
```

To ensure ADC is installed correctly, run:

```
adc help
```

You will receive a response as shown below:

```
Usage: adc [options] [command]

Options:
  -V, --version   output the version number
  -h, --help      display help for command

Commands:
  ping [options]  Verify connectivity with the backend
  dump [options]  Dump configurations from the backend
  diff [options]  Show the difference between local and backend configurations
  sync [options]  Sync local configurations to the backend
  convert         Convert other API specs to ADC configurations
  lint [options]  Check provided configuration files, local execution only, ensuring inputs meet ADC requirements
  help [command]  display help for command
```

## Generate API Token[â](#generate-api-token "Direct link to Generate API Token")

Before you start using ADC, you first need an API token to access the Admin API. You can either:

1. Generate a token from the dashboard: Login -> Profile -> Token -> Generate New Token
2. Generate a token [through the Admin API](https://docs.api7.ai/enterprise/reference/admin-api#tag/Tokens)

## Configure ADC[â](#configure-adc "Direct link to Configure ADC")

ADC can be configured through flags (imperative) or through environment variables (declarative).

This example configures the control plane address and the token so that ADC can connect to the API7 Enterprise instance.

Create a `.env` file with the following content:

```
ADC_BACKEND=api7ee

# replace with your control plane address
ADC_SERVER=https://152.42.234.39:7443

# replace with your ADC token
ADC_TOKEN=a7ee-6baF8488i8wJ5aj7mEo3BT705573eC8GH905qGrdn889zUWcR37df66a34e9954b61918c5dfd13abce3e
```

ADC also supports the `ADC_CA_CERT_FILE`, `ADC_TLS_CLIENT_CERT_FILE`, `ADC_TLS_CLIENT_KEY_FILE`, and `ADC_TLS_SKIP_VERIFY` environment variables for TLS configurations.

To verify this configuration, run:

```
adc ping
```

You should receive a response as shown below:

```
Connected to the backend successfully!
```

tip

Run `adc ping -h` to get a list of the available flags. You can either configure ADC through environment variables as shown above or through equivalent flags.

## Sync Configuration[â](#sync-configuration "Direct link to Sync Configuration")

The API7 Enterprise configuration is defined in a YAML file (`adc.yaml`) and synced by ADC.

The example below defines three services:

adc.yaml

```
services:
  - name: SOAP Service
    description: "This Service is for SOAP requests"
    upstream:
      name: default
      scheme: https
      type: roundrobin
      hash_on: vars
      nodes:
        - host: apps.learnwebservices.com
          port: 443
          weight: 1
          priority: 0
      retry_timeout: 0
      pass_host: pass
    routes:
      - uris:
          - /services/hello
        name: SOAP proxy
        methods:
          - POST
      - uris:
          - /SayHello
        name: REST to SOAP
        methods:
          - POST
        plugins:
          soap:
            wsdl_url: https://apps.learnwebservices.com/services/hello?wsdl
  - name: httpbin Service
    description: "This is the httpbin Services proxy service"
    labels:
      app: httpbin
      custom_key: custom_value
    routes:
      - name: Generate UUID
        methods:
          - GET
        uris:
          - /uuid
      - name: Anything
        methods:
          - GET
        uris:
          - /anything
        plugins:
          key-auth:
            _meta:
              disable: false
      - name: Rate Limited IP
        methods:
          - GET
        uris:
          - /ip
        plugins:
          limit-count:
            _meta:
              disable: false
            count: 2
            time_window: 10
            rejected_code: 429
            policy: local
    upstream:
      name: default
      scheme: http
      type: roundrobin
      hash_on: vars
      nodes:
        - host: httpbin.org
          port: 80
          weight: 1
          priority: 0
      retry_timeout: 0
      pass_host: pass
  - name: SSE Service
    labels:
      service: sse
    upstream:
      scheme: https
      nodes:
        - host: www.esegece.com
          port: 2053
          weight: 1
          priority: 0
      type: roundrobin
      pass_host: node
    plugins:
      proxy-buffering:
        disable_proxy_buffering: true
    routes:
      - name: SSE API
        uris:
          - /sse
        methods:
          - GET
consumers:
  - username: tom
    plugins:
      key-auth:
        key: tomskey
ssls: []
global_rules: {}
```

To sync this configuration to the connected instance, run:

```
adc sync -f adc.yaml
```

A successful sync will yield the following response:

```
â Load local configuration
â Load remote configuration
â Diff configuration
â Sync configuration
```

Test the created "httpbin Service" by sending a request to the route:

```
curl "152.42.234.39:9080/uuid" -v
```

```
*   Trying 152.42.234.39:9080...
* Connected to 152.42.234.39 (152.42.234.39) port 9080
> GET /uuid HTTP/1.1
> Host: 152.42.234.39:9080
> User-Agent: curl/8.4.0
> Accept: */*
>
< HTTP/1.1 200 OK
< Content-Type: application/json
< Content-Length: 53
< Connection: keep-alive
< Date: Wed, 17 Apr 2024 09:56:22 GMT
< Access-Control-Allow-Origin: *
< Access-Control-Allow-Credentials: true
< Server: API7/3.2.8
<

{
  "uuid": "22b888f4-9e96-4d09-93a2-408b14e772fe"
}

* Connection #0 to host 152.42.234.39 left intact
```

The `/anything` route has the `key-auth` plugin enabled. Send a request to the route without the key:

```
curl "152.42.234.39:9080/anything"
```

You will be unable to complete the request and receive the following message:

```
{ "message": "Missing API key found in request" }
```

Now, add the key to the header:

```
curl "152.42.234.39:9080/anything" -H "apikey: tomskey"
```

Now the request is authenticated properly and you will receive the required response:

```
{
  "args": {},
  "data": "",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Apikey": "tomskey",
    "Host": "152.42.234.39",
    "User-Agent": "curl/8.4.0",
    "X-Amzn-Trace-Id": "Root=1-661f9d57-42c4a66b07b361713713da44",
    "X-Forwarded-Host": "152.42.234.39"
  },
  "json": null,
  "method": "GET",
  "origin": "182.255.32.50, 152.42.234.39",
  "url": "http://152.42.234.39/anything"
}
```

## Modify Configuration[â](#modify-configuration "Direct link to Modify Configuration")

To modify the configuration, simply update the `adc.yaml` file. Since it is the single source of truth, any modifications you make will be synced and applied by the connected instance.

The example below adds a new `/headers` route to the "httpbin Service":

```
services:
  - name: SOAP Service
    description: ""
    upstream:
      name: default
      scheme: https
      type: roundrobin
      hash_on: vars
      nodes:
        - host: apps.learnwebservices.com
          port: 443
          weight: 1
          priority: 0
      retry_timeout: 0
      pass_host: pass
    routes:
      - uris:
          - /services/hello
        name: SOAP proxy
        methods:
          - POST
      - uris:
          - /SayHello
        name: REST to SOAP
        methods:
          - POST
        plugins:
          soap:
            wsdl_url: https://apps.learnwebservices.com/services/hello?wsdl
  - name: httpbin Service
    description: ""
    labels:
      app: httpbin
      custom_key: custom_value
    routes:
      - name: Get Headers
        methods:
          - GET
        uris:
          - /headers
      - name: Generate UUID
        methods:
          - GET
        uris:
          - /uuid
      - name: Anything
        methods:
          - GET
        uris:
          - /anything
        plugins:
          key-auth:
            _meta:
              disable: false
      - name: Rate Limited IP
        methods:
          - GET
        uris:
          - /ip
        plugins:
          limit-count:
            _meta:
              disable: false
            count: 2
            time_window: 10
            rejected_code: 429
            policy: local
    upstream:
      name: default
      scheme: http
      type: roundrobin
      hash_on: vars
      nodes:
        - host: httpbin.org
          port: 80
          weight: 1
          priority: 0
      retry_timeout: 0
      pass_host: pass
  - name: SSE Service
    labels:
      service: sse
    upstream:
      scheme: https
      nodes:
        - host: www.esegece.com
          port: 2053
          weight: 1
          priority: 0
      type: roundrobin
      pass_host: node
    plugins:
      proxy-buffering:
        disable_proxy_buffering: true
    routes:
      - name: SSE API
        uris:
          - /sse
        methods:
          - GET
consumers:
  - username: tom
    plugins:
      key-auth:
        key: tomskey
ssls: []
global_rules: {}
```

Before syncing this modified configuration, you can check what modifications will be made with the `diff` subcommand:

```
adc diff -f ./adc.yaml
```

The output will indicate the exact changes being made with this modified configuration:

```
â Load local configuration
â Load remote configuration
â Diff configuration
  âº update consumer: "tom"
    update route: "REST to SOAP"
    update route: "SOAP proxy"
    update route: "Rate Limited IP"
    update route: "Anything"
    update route: "Generate UUID"
    create route: "Get Headers"
    update service: "SSE Service"
    update route: "SSE API"
    Summary: 1 will be created, 8 will be updated, 0 will be deleted
â Write detailed diff results to file
```

As mentioned in the output, the `diff` subcommand also generates a `diff.yaml` file showing the changes in detail:

diff.yaml

```
- resourceType: consumer
  type: update
  resourceId: tom
  resourceName: tom
  oldValue:
    username: tom
    description: ""
    plugins:
      key-auth:
        key: tomskey
  newValue:
    username: tom
    plugins:
      key-auth:
        key: tomskey
  diff:
    added: {}
    deleted: {}
    updated: {}
- resourceType: route
  type: update
  resourceId: bef0a3351a392e74c960f9a58c1d025d803f2aef
  resourceName: REST to SOAP
  oldValue:
    uris:
      - /SayHello
    name: REST to SOAP
    methods:
      - POST
    enable_websocket: false
    plugins:
      soap:
        wsdl_url: https://apps.learnwebservices.com/services/hello?wsdl
  newValue:
    uris:
      - /SayHello
    name: REST to SOAP
    methods:
      - POST
    plugins:
      soap:
        wsdl_url: https://apps.learnwebservices.com/services/hello?wsdl
  diff:
    added: {}
    deleted: {}
    updated: {}
  parentId: 602dfcf4c39218f87d40c5d1df8b531b49ca88e8
- resourceType: route
  type: update
  resourceId: da37e65d428446d156279156ac3248c00d0a1533
  resourceName: SOAP proxy
  oldValue:
    uris:
      - /services/hello
    name: SOAP proxy
    methods:
      - POST
    enable_websocket: false
  newValue:
    uris:
      - /services/hello
    name: SOAP proxy
    methods:
      - POST
  diff:
    added: {}
    deleted: {}
    updated: {}
  parentId: 602dfcf4c39218f87d40c5d1df8b531b49ca88e8
- resourceType: route
  type: update
  resourceId: b586591b59c13461ed8932228cb23e53040c09d4
  resourceName: Rate Limited IP
  oldValue:
    uris:
      - /ip
    name: Rate Limited IP
    methods:
      - GET
    enable_websocket: false
    plugins:
      limit-count:
        _meta:
          disable: false
        count: 2
        policy: local
        rejected_code: 429
        time_window: 10
  newValue:
    name: Rate Limited IP
    methods:
      - GET
    uris:
      - /ip
    plugins:
      limit-count:
        _meta:
          disable: false
        count: 2
        time_window: 10
        rejected_code: 429
        policy: local
  diff:
    added: {}
    deleted: {}
    updated: {}
  parentId: 5ce4033cfe1015450e0b81186f7d54b9327cc302
- resourceType: route
  type: update
  resourceId: 5f2de5df1a292b4c8a73f0ec23271233d75707c6
  resourceName: Anything
  oldValue:
    uris:
      - /anything
    name: Anything
    methods:
      - GET
    enable_websocket: false
    plugins:
      key-auth:
        _meta:
          disable: false
  newValue:
    name: Anything
    methods:
      - GET
    uris:
      - /anything
    plugins:
      key-auth:
        _meta:
          disable: false
  diff:
    added: {}
    deleted: {}
    updated: {}
  parentId: 5ce4033cfe1015450e0b81186f7d54b9327cc302
- resourceType: route
  type: update
  resourceId: ed048a2f75fe33eab67319810fbb94bb778d7d97
  resourceName: Generate UUID
  oldValue:
    uris:
      - /uuid
    name: Generate UUID
    methods:
      - GET
    enable_websocket: false
  newValue:
    name: Generate UUID
    methods:
      - GET
    uris:
      - /uuid
  diff:
    added: {}
    deleted: {}
    updated: {}
  parentId: 5ce4033cfe1015450e0b81186f7d54b9327cc302
- resourceType: route
  resourceId: 6b124aff482499cbf7bdad5a56b13205b24ba58e
  resourceName: Get Headers
  type: create
  newValue:
    name: Get Headers
    methods:
      - GET
    uris:
      - /headers
  parentId: 5ce4033cfe1015450e0b81186f7d54b9327cc302
- resourceType: service
  type: update
  resourceId: 54154d3cdf6379ab8686890d27fabb6bf8fa3ace
  resourceName: SSE Service
  oldValue:
    name: SSE Service
    description: ""
    labels:
      service: sse
    upstream:
      name: default
      scheme: https
      type: roundrobin
      hash_on: vars
      nodes:
        - host: www.esegece.com
          port: 2053
          weight: 1
          priority: 0
      retry_timeout: 0
      pass_host: node
    plugins:
      proxy-buffering:
        disable_proxy_buffering: true
  newValue:
    name: SSE Service
    labels:
      service: sse
    upstream:
      scheme: https
      nodes:
        - host: www.esegece.com
          port: 2053
          weight: 1
          priority: 0
      type: roundrobin
      pass_host: node
    plugins:
      proxy-buffering:
        disable_proxy_buffering: true
  diff:
    added: {}
    deleted:
      upstream: {}
    updated: {}
  subEvents:
    - &a1
      resourceType: route
      type: update
      resourceId: 6b808fa543c7c3391321b813d0dc2d658ab02c10
      resourceName: SSE API
      oldValue:
        uris:
          - /sse
        name: SSE API
        methods:
          - GET
        enable_websocket: false
      newValue:
        name: SSE API
        uris:
          - /sse
        methods:
          - GET
      diff:
        added: {}
        deleted: {}
        updated: {}
      parentId: 54154d3cdf6379ab8686890d27fabb6bf8fa3ace
- *a1
```

If the changes look good, run the `sync` subcommand to sync the modified configuration to the connected instance:

```
adc sync -f ./adc.yaml
```

Send a request to test this newly created route:

```
curl "152.42.234.39:9080/headers"
```

You will receive a similar response from the upstream:

```
{
  "headers": {
    "Accept": "*/*",
    "Host": "152.42.234.39",
    "User-Agent": "curl/8.4.0",
    "X-Amzn-Trace-Id": "Root=1-661f9edd-188a0adf5d3bf0a509f5b034",
    "X-Forwarded-Host": "152.42.234.39"
  }
}
```

## Next Steps[â](#next-steps "Direct link to Next Steps")

ADC is still under development and will be improved continuously. See the ADC Reference document for a complete list of available subcommands.
