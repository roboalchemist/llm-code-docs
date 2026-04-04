# Source: https://docs.api7.ai/enterprise/api-security/block-ip.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/api-security/block-ip.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/api-security/block-ip.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/api-security/block-ip.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/api-security/block-ip.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/api-security/block-ip.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/api-security/block-ip.md

# Source: https://docs.api7.ai/enterprise/3.8.x/api-security/block-ip.md

# Source: https://docs.api7.ai/enterprise/3.7.x/api-security/block-ip.md

# Source: https://docs.api7.ai/enterprise/3.6.x/api-security/block-ip.md

# Source: https://docs.api7.ai/enterprise/3.5.x/api-security/block-ip.md

# Source: https://docs.api7.ai/enterprise/3.4.x/api-security/block-ip.md

# Source: https://docs.api7.ai/enterprise/3.3.x/api-security/block-ip.md

# Restrict IP Addresses from APIs

You can configure access controls based on IP addresses to prevent unwanted users from accessing your APIs.

This guide will walk you through configuring theÂ `ip-restriction`Â plugin on a [gateway group](https://docs.api7.ai/enterprise/3.3.x/key-concepts/gateway-groups.md) as a [global rule](https://docs.api7.ai/enterprise/3.3.x/key-concepts/plugins.md), to block IP addresses in a blacklist. If a request comes from an IP address in the blacklist, the API7 Gateway will deny the request with aÂ `403`Â response code. The IP address of the request can be either the actual client IP address or theÂ `X-Forwarded-For`Â address.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

1. [Install API7 Enterprise](https://docs.api7.ai/enterprise/3.3.x/getting-started/install-api7-ee.md).
2. [Have a running API on the gateway group](https://docs.api7.ai/enterprise/3.3.x/getting-started/launch-your-first-api.md).

## Configure IP Address Restriction on a Gateway Group[â](#configure-ip-address-restriction-on-a-gateway-group "Direct link to Configure IP Address Restriction on a Gateway Group")

When malicious actors are identified, add their IP addresses to the blacklist to restrict their access to your APIs.

* Dashboard
* ADC
* Ingress Controller

1. Select **Plugin Settings** of your gateway group from the side navigation bar.
2. Select **Plugin Global Rules**, then click **Enable Plugin**.
3. Search for the `ip-restriction` plugin, then click **Enable**.
4. In the dialog box, do the following:

* Add the following configuration to the **JSON Editor** to add the IP address `127.0.0.1` to the blacklist:

  ```
  {
    "blacklist": ["127.0.0.1"],
    "message": "Sorry, your IP address is not allowed."
  }
  ```

* Click **Enable**.

To use ADC to configure the plugin, create the following configuration:

adc.yaml

```
services:
  - name: httpbin API
    upstream:
      name: default
      scheme: http
      nodes:
        - host: httpbin.org
          port: 80
          weight: 100
    routes:
      - uris:
          - /ip
        name: security-ip
        methods:
          - GET
global_rules:
  ip-restriction:
    _meta:
      disable: false
    blacklist:
      - 127.0.0.1
    message: Sorry, your IP address is not allowed.
```

Synchronize the configuration to API7 Gateway:

```
adc sync -f adc.yaml
```

Create a Kubernetes manifest file for a route:

httpbin-route.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  name: httpbin-route
  # namespace: api7    # replace with your namespace
spec:
  http:
    - name: httpbin-route
      match:
        paths:
          - /ip
        methods:
          - GET
      backends:
        - serviceName: httpbin
          servicePort: 80
```

Create another manifest file for a global `ip-restriction` plugin:

global-ip-restriction.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixGlobalRule
metadata:
  name: global-ip-restriction
  # namespace: api7    # replace with your namespace
spec:
  plugins:
    - name: ip-restriction
      enable: true
      config:
        blacklist:
          - "127.0.0.1"
        message: Sorry, your IP address is not allowed.
```

Apply the configurations to your cluster:

```
kubectl apply -f httpbin-route.yaml -f global-ip-restriction.yaml
```

### Validate[â](#validate "Direct link to Validate")

Send a request from the restricted IP address. For this example, `127.0.0.1` was configured as a blacklisted IP address:

```
curl -i "http://127.0.0.1:9080/ip" 
```

You will receive a `403 Forbidden` response with the following message:

```
{"error_msg":"Sorry, your IP address is not allowed."}
```

## Additional Resource(s)[â](#additional-resources "Direct link to Additional Resource(s)")

* Key Concepts

  <!-- -->

  * [Services](https://docs.api7.ai/enterprise/3.3.x/key-concepts/services.md)
  * [Routes](https://docs.api7.ai/enterprise/3.3.x/key-concepts/routes.md)
  * [Plugins](https://docs.api7.ai/enterprise/3.3.x/key-concepts/plugins.md)
