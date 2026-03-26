# Source: https://docs.api7.ai/apisix/how-to-guide/security/waf/integrate-with-coraza.md

# Integrate with Coraza

With rapid development of technology, it has become increasingly crucial to secure APIs. APISIX supports the integration with [Coraza](https://coraza.io/) by using [coraza-proxy-wasm](https://github.com/corazawaf/coraza-proxy-wasm) to provide reliable security protection and ensure the integrity and reliability of API services.

Coraza is an open-source, enterprise-grade, high-performance [Web Application Firewall (WAF)](https://en.wikipedia.org/wiki/Web_application_firewall). It is designed to safeguard web applications against various cyberattacks by filtering and monitoring HTTP/HTTPS communications between web applications and the internet. Integrating with [Coraza](https://coraza.io/), APISIX significantly enhances APISIX's ability to protect upstream services.

<br />

![Integration with Coraza](https://static.api7.ai/uploads/2024/03/20/WslLnSuA_coraza.png)

<br />

This guide will show you how to enable [coraza-proxy-wasm](https://github.com/corazawaf/coraza-proxy-wasm) to integrate APISIX with Coraza WAF to protect upstream services.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Install [Docker](https://docs.docker.com/get-docker/).
* Install [cURL](https://curl.se/) to send requests to the services for validation.
* Install [ZIP](https://infozip.sourceforge.net/Zip.html) to unzip the `coraza-proxy-wasm` binary from the [release page](https://github.com/corazawaf/coraza-proxy-wasm/releases).
* Follow the [Getting Started tutorial](https://docs.api7.ai/apisix/getting-started/.md) to start a new APISIX instance in Docker.

## Download `coraza-proxy-wasm`[â](#download-coraza-proxy-wasm "Direct link to download-coraza-proxy-wasm")

Download `coraza-proxy-wasm` from the [release page](https://github.com/corazawaf/coraza-proxy-wasm/releases) and unzip it:

```
wget https://github.com/corazawaf/coraza-proxy-wasm/releases/download/0.4.0/coraza-proxy-wasm-0.4.0.zip
unzip coraza-proxy-wasm-0.4.0.zip
```

Copy `coraza-proxy-wasm.wasm` into the `/usr/local/bin` directory:

```
docker cp /path/to/coraza-proxy-wasm.wasm apisix-quickstart:/usr/local/bin/
```

## Load `coraza-proxy-wasm` in APISIX[â](#load-coraza-proxy-wasm-in-apisix "Direct link to load-coraza-proxy-wasm-in-apisix")

Update the `config.yaml` [configuration file](https://docs.api7.ai/apisix/reference/configuration-files.md#configyaml-and-configyamlexample) by adding `coraza-proxy-wasm` configurations:

```
docker exec apisix-quickstart /bin/bash -c "echo '
wasm:
  plugins:
    - name: coraza-filter
      priority: 7999
      file: /usr/local/bin/coraza-proxy-wasm.wasm
' >> /usr/local/apisix/conf/config.yaml"
```

â¶ `name`: the name of the APISIX plugin corresponding to `coraza-proxy-wasm`.

â· `priority`: the [execution priority](https://docs.api7.ai/apisix/key-concepts/plugins.md#plugins-execution-order) of the plugin.

â¸ `file`: the absolute path to `coraza-proxy-wasm`.

[Reload APISIX](https://docs.api7.ai/apisix/reference/apisix-cli.md#apisix-reload) for configuration changes to take effect:

```
docker exec apisix-quickstart apisix reload
```

## Configure Specific Security Rules[â](#configure-specific-security-rules "Direct link to Configure Specific Security Rules")

Create a route and enable `coraza-filter`:

* Admin API
* ADC

```
curl -i "http://127.0.0.1:9180/apisix/admin/routes/" -X PUT -d '
{
  "id": "getting-started-waf",
  "uri": "/anything/*",
  "plugins": {
    "coraza-filter": {
      "conf": {
        "directives_map": {
          "default": [
            "SecDebugLogLevel 9",
            "SecRuleEngine On",
            "SecRule REQUEST_URI \"@beginsWith /anything/archive\" \"id:101,phase:1,t:lowercase,deny\""
          ]
        },
        "default_directives": "default"
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

â¶ `SecDebugLogLevel`: configure the debug log level. For details, see [SecDebugLogLevel](https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual-\(v2.x\)#secdebugloglevel).

â· `SecRuleEngine`: configure the rules engine. For details, see [SecRuleEngine](https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual-\(v2.x\)#secruleengine).

â¸ `SecRule`: check the URI value of your HTTP request to see if the URI value begins with `/anything/archive`. If matched, the request will be rejected. For details, see [SecRule](https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual-\(v2.x\)#SecRule).

adc.yaml

```
services:
  - name: httpbin Service
    routes:
      - uris:
          - /anything/*
        name: getting-started-waf
        plugins:
          coraza-filter:
            conf:
              directives_map:
                default:
                  - SecDebugLogLevel 9
                  - SecRuleEngine On
                  - SecRule REQUEST_URI "@beginsWith /anything/archive" "id:101,phase:1,t:lowercase,deny"
              default_directives: default
    upstream:
      type: roundrobin
      nodes:
        - host: httpbin.org
          port: 80
          weight: 1
```

â¶ `SecDebugLogLevel`: configure the debug log level. For details, see [SecDebugLogLevel](https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual-\(v2.x\)#secdebugloglevel).

â· `SecRuleEngine`: configure the rules engine. For details, see [SecRuleEngine](https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual-\(v2.x\)#secruleengine).

â¸ `SecRule`: check the URI value of your HTTP request to see if the URI value begins with `/anything/archive`. If matched, the request will be rejected. For details, see [SecRule](https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual-\(v2.x\)#SecRule).

Synchronize the configuration to APISIX:

```
adc sync -f adc.yaml
```

### Verify[â](#verify "Direct link to Verify")

Send a request to the route to verify if the HTTP request with a URI beginning with `anything/archive` will be rejected:

```
curl -i "http://localhost:9080/anything/archive/test"
```

You should receive an `HTTP/1.1 403 Forbidden` response.

Send a request to the route to verify if the HTTP request with a URI beginning with `anything` will be allowed:

```
curl -i "http://localhost:9080/anything/public"
```

You should receive an `HTTP/1.1 200 OK` response.

## Configure OWASP Core Rule Set[â](#configure-owasp-core-rule-set "Direct link to Configure OWASP Core Rule Set")

You can also configure the entire [OWASP Core Rule Set (CRS)](https://owasp.org/www-project-modsecurity-core-rule-set) on the route as such:

* Admin API
* ADC

```
curl -i "http://127.0.0.1:9180/apisix/admin/routes/" -X PUT -d '
{
  "id": "getting-started-waf",
  "uri": "/anything/*",
  "plugins": {
    "coraza-filter": {
      "conf": {
        "directives_map": {
          "default": [
            "SecDebugLogLevel 9",
            "SecRuleEngine On",
            "Include @crs-setup-conf",
            "Include @owasp_crs/*.conf"
          ]
        },
        "default_directives": "default"
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

â¶ Include `@crs-setup-conf` to support CRS.

â· Include all CRS rules. You could also include a specific rule, such as `@owasp_crs/REQUEST-941-APPLICATION-ATTACK-XSS.conf`. See [all available rules](https://github.com/corazawaf/coraza-proxy-wasm/tree/main/wasmplugin/rules/crs).

adc.yaml

```
services:
  - name: httpbin Service
    routes:
      - uris:
          - /anything/*
        name: getting-started-waf
        plugins:
          coraza-filter:
            conf:
              directives_map:
                default:
                  - SecDebugLogLevel 9
                  - SecRuleEngine On
                  - Include @crs-setup-conf
                  - Include @owasp_crs/*.conf
              default_directives: default
    upstream:
      type: roundrobin
      nodes:
        - host: httpbin.org
          port: 80
          weight: 1
```

â¶ Include `@crs-setup-conf` to support CRS.

â· Include all CRS rules. You could also include a specific rule, such as `@owasp_crs/REQUEST-941-APPLICATION-ATTACK-XSS.conf`. See [all available rules](https://github.com/corazawaf/coraza-proxy-wasm/tree/main/wasmplugin/rules/crs).

Synchronize the configuration to APISIX:

```
adc sync -f adc.yaml
```

### Verify[â](#verify-1 "Direct link to Verify")

Send a request with a potential XSS attack to the route:

```
curl -i "http://localhost:9080/anything/public" -H "Cookie: <body onload='alert(xss)'>"
```

You should receive an `HTTP/1.1 403 Forbidden` response and observe the following in log:

```
2023/12/21 02:27:14 [emerg] 130#130: *116868 [client ""] Coraza: Warning. NoScript XSS InjectionChecker: HTML Injection [file "@owasp_crs/REQUEST-941-APPLICATION-ATTACK-XSS.conf"] [line "7529"] [id "941160"] [rev ""] [msg "NoScript XSS InjectionChecker: HTML Injection"] [data "Matched Data: <body  found within REQUEST_COOKIES_NAMES:<body onload: <body onload"] [severity "critical"] [ver "OWASP_CRS/4.0.0-rc2"] [maturity "0"] [accuracy "0"] [tag "application-multi"] [tag "language-multi"] [tag "platform-multi"] [tag "attack-xss"] [tag "paranoia-level/1"] [tag "OWASP_CRS"] [tag "capec/1000/152/242"] [hostname ""] [uri "/anything/public"] [unique_id "vXZLznnuwaZHkjIBXyN"], client: 172.24.0.1, server: _, request: "GET /anything/public HTTP/1.1", host: "localhost:9080"
2023/12/21 02:27:14 [emerg] 130#130: *116868 [client ""] Coraza: Warning. Javascript method detected [file "@owasp_crs/REQUEST-941-APPLICATION-ATTACK-XSS.conf"] [line "8023"] [id "941390"] [rev ""] [msg "Javascript method detected"] [data "Matched Data: alert( found within REQUEST_COOKIES:<body onload: 'alert(xss)'>"] [severity "critical"] [ver "OWASP_CRS/4.0.0-rc2"] [maturity "0"] [accuracy "0"] [tag "application-multi"] [tag "language-multi"] [tag "attack-xss"] [tag "paranoia-level/1"] [tag "OWASP_CRS"] [tag "capec/1000/152/242"] [hostname ""] [uri "/anything/public"] [unique_id "vXZLznnuwaZHkjIBXyN"], client: 172.24.0.1, server: _, request: "GET /anything/public HTTP/1.1", host: "localhost:9080"
2023/12/21 02:27:14 [emerg] 130#130: *116868 [client ""] Coraza: Access denied (phase 1). Inbound Anomaly Score Exceeded in phase 1 (Total Score: 10) [file "@owasp_crs/REQUEST-949-BLOCKING-EVALUATION.conf"] [line "11098"] [id "949111"] [rev ""] [msg "Inbound Anomaly Score Exceeded in phase 1 (Total Score: 10)"] [data ""] [severity "emergency"] [ver "OWASP_CRS/4.0.0-rc2"] [maturity "0"] [accuracy "0"] [tag "anomaly-evaluation"] [hostname ""] [uri "/anything/public"] [unique_id "vXZLznnuwaZHkjIBXyN"], client: 172.24.0.1, server: _, request: "GET /anything/public HTTP/1.1", host: "localhost:9080"
```

This verifies that the CRS rules are in effect to protect your route.

## Next Steps[â](#next-steps "Direct link to Next Steps")

APISIX also supports the integration with Chaitin WAF and other WAFs provided by popular cloud vendors. See other guides in this chapter to learn more (coming soon).
