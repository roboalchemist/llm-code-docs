# Source: https://docs.api7.ai/hub/ip-restriction.md

# Source: https://docs.api7.ai/cloud/references/plugins/security/ip-restriction.md

# Source: https://docs.api7.ai/cloud/guides/security/ip-restriction.md

# Source: https://docs.api7.ai/apisix/production/security/ip-restriction.md

# Source: https://docs.api7.ai/cloud/references/plugins/security/ip-restriction.md

# Source: https://docs.api7.ai/cloud/guides/security/ip-restriction.md

# Source: https://docs.api7.ai/apisix/production/security/ip-restriction.md

# IP Restriction

IP restriction is a commonly used technique for access control. By limiting resources to specific IP addresses, organizations can adhere to the principle of least privilege, prevent unauthorized access, and stay compliant with security requirements.

APISIX supports IP restrictions in the following ways:

* Restricting access to upstream resources by IPs
* Restricting access to Admin API by IPs

This guide will show you how to configure APISIX for these practices.

## Restrict Access to Upstream Resource by IP[â](#restrict-access-to-upstream-resource-by-ip "Direct link to Restrict Access to Upstream Resource by IP")

In this section, you will learn how to control client access to upstream resources by IPs, using the `ip-restriction` plugin. You will also learn how to expose the real client IP to APISIX when APISIX is behind a reverse proxy, such that the `ip-restriction` plugin can evaluate access based on the real client IP.

### Restrict by the Original Remote Address[â](#restrict-by-the-original-remote-address "Direct link to Restrict by the Original Remote Address")

Create a route with the `ip-restriction` plugin and configure the IP whitelist:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ip-restriction-route",
    "uri": "/anything",
    "plugins": {
      "ip-restriction": {
        "whitelist": [
          "192.168.0.1/24"
        ]
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

â¶ Configure a list of IP addresses that are allowed to access the upstream resource. The configuration supports both IPv4 and IPv6 formats.

Send a request to the route:

```
curl -i "http://127.0.0.1:9080/anything"
```

If your IP is allowed, you should receive an `HTTP/1.1 200 OK` response. If not, you should receive an `HTTP/1.1 403 Forbidden` response with the following error message:

```
{"message":"Your IP address is not allowed"}
```

You can also configure the `ip-restriction` plugin with a list of IP addresses to blacklist. However, note that the whitelist and the blacklist cannot be configured simultaneously. See the [plugin doc](https://docs.api7.ai/hub/ip-restriction.md) for more information.

### Restrict by the Modified Remote Address[â](#restrict-by-the-modified-remote-address "Direct link to Restrict by the Modified Remote Address")

Sometimes APISIX could be behind a reverse proxy. As a result, the client IP recognized by APISIX is the proxy IP, instead of the real client IP. To pass the real client IP to APISIX for the purpose of IP restriction, you can use the [`ip-restriction`](https://docs.api7.ai/hub/ip-restriction.md) plugin in conjunction with the [`real-ip`](https://docs.api7.ai/hub/real-ip.md) plugin.

Create a route and configure both plugins as follows:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ip-restriction-route",
    "uri": "/anything",
    "plugins": {
      "ip-restriction": {
        "whitelist": [
          "192.168.1.241"
        ]
      },
      "real-ip": {
        "source": "arg_realip"
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

â¶ Configure an IP address to whitelist.

â· Obtain client IP address from the URL parameter `realip` using the [built-in variables](https://docs.api7.ai/apisix/reference/built-in-variables.md).

Send a request to the route:

```
curl -i "http://127.0.0.1:9080/anything?realip=192.168.1.241"
```

You should receive an `HTTP/1.1 200 OK` response.

Send another request with a different IP address:

```
curl -i "http://127.0.0.1:9080/anything?realip=192.168.10.24"
```

You should receive an `HTTP/1.1 403 Forbidden` response.

## Restrict Admin API Access by IP[â](#restrict-admin-api-access-by-ip "Direct link to Restrict Admin API Access by IP")

By restricting [Admin API](https://docs.api7.ai/apisix/reference/admin-api/.md) access to authorized personnel, organizations minimize the attack surface and ensure that only individuals with the necessary expertise and responsibilities can make critical changes. This helps maintain a higher level of control and overall security across the infrastructure.

To restrict IP addresses that should have [administrative view and write access](https://docs.api7.ai/apisix/production/security/admin-api-key.md#key-requirement-and-permissions) to APISIX Admin API, update the configuration file `config.yaml` with the following:

```
deployment:
  admin:
    admin_key_required: true
    allow_admin:
      - 127.0.0.0/24
      # - "::/64"
```

â¶ Configure a list of IP addresses that are allowed to access Admin API. The configuration supports both IPv4 and IPv6 formats.

Note that all IP addresses would be allowed to access Admin API if `allow_admin` is not configured with any IP, and is advised against in a production environment.

[Reload APISIX](https://docs.api7.ai/apisix/reference/apisix-cli.md#apisix-reload) for configuration file changes to take effect.
