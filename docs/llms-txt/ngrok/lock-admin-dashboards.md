# Source: https://ngrok.com/docs/universal-gateway/examples/lock-admin-dashboards.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Secure Admin Dashboards

> Add multiple layers of protection and authentication to your dashboards to prevent threat actors from even attempting attacks.

export const domain_0 = undefined

Even if your admin dashboards and internal tools already have built-in authentication, you can make them even secure using ngrok and Traffic Policy to restrict specific types of traffic from even hitting your endpoint.

You can restrict access to specific IP addresses, block traffic from problematic sources, restrict requests to only your geographical area, or all the above.
In this example, this guide assumes that your admin tool is part of your public-facing service, available on a path like `/admin`.

## 1. Start an endpoint for your service

Start an internal [Agent Endpoint](/universal-gateway/agent-endpoints/), replacing `$PORT` based on where your service listens.
You can also use one of the [SDKs](/agent-sdks) or the [Kubernetes Operator](/k8s).

```bash  theme={null}
ngrok http $PORT --url https://service.internal
```

## 2. Reserve a domain

Navigate to the [**Domains** section](https://dashboard.ngrok.com/domains) of the ngrok dashboard and click **New +** to reserve a free static domain like {<code>{domain_0}</code> || `https://your-service.ngrok.app`} or a [custom domain](/universal-gateway/custom-domains/) you already own.

We'll refer to this domain as `$NGROK_DOMAIN` from here on out.

## 3. Create a Cloud Endpoint

Navigate to the [**Endpoints** section](https://dashboard.ngrok.com/endpoints?sortBy=updatedAt\&orderBy=desc) of the ngrok dashboard, then click **New +** and **Cloud Endpoint**.

In the **URL** field, enter the domain you just reserved to finish creating your [Cloud Endpoint](/universal-gateway/cloud-endpoints/).

## 4. Restrict access to your admin path with Traffic Policy

While viewing your new Cloud Endpoint in the dashboard, copy the policy below and paste it into the Traffic Policy editor.
You may need to change:

* `/admin`: Replace with the path of your admin tools.
* `1.2.3.4/5.6.7.8`: Replace with public IPs of your admins.
* `US`: Replace with the country code where your admins would log in to.

```yaml  theme={null}
on_http_request:
  - expressions:
      - "req.url.path.includes('/admin')"
      - "conn.client_ip.geo.location.country_code != 'US' || req.user_agent.is_bot || 'proxy.anonymous.tor, blocklist.co.greensnow' in conn.client_ip.categories"
    actions:
      - type: deny
  - expressions:
      - "req.url.path.includes('/admin')"
    actions:
      - type: restrict-ips
        config:
          allow:
            - 1.2.3.4/32
            - 5.6.7.8/32
  - actions:
      - type: forward-internal
        config:
          url: https://service.internal
```

**What's happening here?** Your policy checks every HTTP request and filters out only those to the `/admin` path, first denying all requests from non-U.S. traffic, bot traffic, Tor networks, and all IPs on the GreenSnow blocklist.
For all requests not immediately denied, ngrok then also restricts access to only specific and trusted IP addresses before forwarding to your upstream service.

ngrok forwards all requests to paths other than `/admin` without these filters or actions.

## 5. Try out your restricted admin tools

Visit the domain you reserved either in the browser or in the terminal using a tool like `curl`.
You should see the app or service at the port connected to your internal Agent Endpoint.

## What's next?

* Explore other examples of using the [`forward-internal`](/traffic-policy/actions/forward-internal/#examples) and [`deny`](/traffic-policy/actions/deny/#examples-on_http_request).
* View who's trying to access your admin tools in [Traffic Inspector](https://dashboard.ngrok.com/traffic-inspector).


Built with [Mintlify](https://mintlify.com).