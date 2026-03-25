# Source: https://help.aikido.dev/miscellaneous-info/aikido-broker-for-internal-applications.md

# Aikido Broker for Internal Applications

Use the Aikido Broker to scan and monitor applications that live on internal networks and are not reachable from the internet.

The broker runs inside your infrastructure and forwards Aikido’s requests to the internal URLs you allow.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FNxTgqxHi4NaTopv0jHR6%2Fbroker.png?alt=media&#x26;token=637758cc-7728-4256-9e4d-98ad69838599" alt=""><figcaption></figcaption></figure>

## When to use the Broker

Use the broker with any Aikido scan on applications or services that only exists inside your company network, including:

* Code scanning on on-prem GitLab or other local code platforms
* Container scanning on private or on-prem container registries
* AI pentesting on internal applications
* Front-end and API testing scans on internal domains or services

## Requirements

To run the Aikido Broker you need:

* [Docker and Docker compose](https://docs.docker.com/engine/install/) installed
  * Optionally Kubernetes 1.19+
* Network access to the applications you want Aikido to scan
* Outbound HTTPS access to `*.aikidobroker.com`
* WebSocket (wss) support for reliable connection
  * corporate proxy/firewall must preserve `Connection: Upgrade` and `Upgrade: websocket` headers
* Enough CPU (1 core) and memory (1 GB) to run a small container

## Installation

{% stepper %}
{% step %}

### Generate and set a broker client token

Go to [Broker Clients page](https://app.aikido.dev/settings/integrations/broker/clients) and create a new broker client secret. Save the Client Secret for next step.

{% hint style="info" %}
If you're unable to access this page, reach out to support in the Aikido dashboard
{% endhint %}
{% endstep %}

{% step %}

### Add resources (internal URL's)

Define which internal URLs Aikido is allowed to access through the broker.

These are the applications and APIs you want Aikido to scan, for example:

* <https://api.internal.corp.local>
* <http://service-a.internal:8080>
* <https://10.0.5.20>

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FuDRUrJZaPzm8Yug4mSqU%2FScreenshot%202026-02-11%20at%2017.08.56.png?alt=media&#x26;token=23b1d18a-3dc6-4bee-8cc9-be1dcb11ec56" alt="" width="563"><figcaption></figcaption></figure>

You can manage these resources in the Aikido UI by selecting an existing broker from the list or by creating a new one.

After you save the resources, a unique Broker URL is generated for each resource. Use this Broker URL in place of the original URL within Aikido.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FDIxZM2BdVIkVVgWW8UJQ%2FScreenshot%202026-02-11%20at%2017.09.05.png?alt=media&#x26;token=5468f34e-8e28-4f2e-9471-fdd3647b506f" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Start the broker

Bring up the broker service on a machine with access to the internal applications you want Aikido to access. Make sure to replace the `CLIENT_SECRET` value with the one generated on clients page.

{% tabs %}
{% tab title="Docker" %}

```shellscript
docker run -d \
  --name aikido-broker \
  --restart=on-failure:3 \
  --network host \
  -e CLIENT_SECRET="AIK_BROKER_XXX_YYY_ZZZZ" \
  -e ALLOWED_INTERNAL_SUBNETS="192.168.0.0/16,10.0.0.0/8,172.16.0.0/12,127.0.0.0/8" \
  aikidosecurity/broker-client:latest
```

You can check if the Broker is running expected with `docker logs aikido-broker`

{% hint style="warning" %}
On Windows and Mac OS: Use `host.docker.internal` instead of `localhost` or `127.0.0.1` to connect to local services.
{% endhint %}
{% endtab %}

{% tab title="Kubernetes" %}
Aikido provides a [Helm chart to deploy the Broker](https://github.com/AikidoSec/helm-charts/tree/main/broker-client) within a Kubernetes environment.

```shellscript
helm repo add aikido https://aikidosec.github.io/helm-charts
helm repo update
helm install broker-client aikido/broker-client \
  --set config.clientSecret="AIK_BROKER_XXX_YYY_ZZZZ" \
  --namespace aikido \
  --create-namespace
```

Set [additional parameters](https://github.com/AikidoSec/helm-charts/blob/main/broker-client/values.yaml) by using a `values.yaml` file and running the command with `helm install broker-client aikido/broker-client -f values.yaml`

You can check if the Broker is running with `kubectl logs -n aikido -l app.kubernetes.io/name=broker-client`
{% endtab %}
{% endtabs %}
{% endstep %}

{% step %}

### Wait for broker to stabilize

Give it about 30 seconds to connect to Aikido and register.

Once it is up and connected, Aikido can start reaching the internal resources you configured.
{% endstep %}
{% endstepper %}

## Configuration

You can control how the broker reaches your internal services and how it resolves hostnames.

#### ALLOWED\_INTERNAL\_SUBNETS

List of CIDR ranges that the broker is allowed to call.

Use this to:

* Limit the broker to specific internal networks
* Prevent accidental access to unrelated infrastructure

Example:

```
ALLOWED_INTERNAL_SUBNETS=10.0.0.0/8,192.168.1.0/24
```

#### DNS\_SERVERS

Optional list of DNS servers the broker should use to resolve internal hostnames.

Use this if:

* You have internal DNS zones (for example \*.corp.local)
* Your internal services are not resolvable with public DNS

Example:

```
DNS_SERVERS=10.0.0.10,10.0.0.11
```

#### NODE\_EXTRA\_CA\_CERTS for Custom CA (internal TLS)

If your internal services use certificates signed by a private CA, provide that CA so the broker can validate TLS correctly.

Typical use cases:

* Internal services with self-signed certificates
* Internal PKI for service-to-service encryption

How you configure this depends on your deployment, but at a high level you will:

* Mount your custom CA file into the broker container
* Point the broker to that CA file using the provided environment variable or config option

When you add custom certificates the broker must be able to read them inside the container. Mount the certificate folder into the container with an extra `-v` flag and point the broker to the certificate file with the `NODE_EXTRA_CA_CERTS` variable. Here is a short example:

```
docker run -d \
  --name aikido-broker \
  --restart=on-failure:3 \
  --network host \
  -v /path/to/corporate-ca.crt:/certs/corporate-ca.crt:ro \
  -e CLIENT_SECRET="{secret}" \
  -e ALLOWED_INTERNAL_SUBNETS="192.168.0.0/16,10.0.0.0/8,172.16.0.0/12,127.0.0.0/8" \
  -e NODE_EXTRA_CA_CERTS=/certs/corporate-ca.crt \
  aikidosecurity/broker-client:latest
```

#### Proxy &#x20;

If your internal network requires a proxy to reach certain hosts or the internet, configure the broker to use that proxy.

This is useful when:

* Outbound traffic in your network must go through an HTTP or HTTPS proxy
* Internal segments are only reachable via a central proxy

Configure the proxy URL through the broker’s proxy setting or environment variables: `HTTP_PROXY, HTTPS_PROXY, ALL_PROXY`&#x20;

You can also configure the client so that requests to certain hosts do not go via the proxy by setting the `NO_PROXY` environment variable (`-e NO_PROXY=noproxy.dev,my-domain.internal`). It's value should be a comma separated list of hosts to bypass the proxy.

#### NODE\_TLS\_REJECT\_UNAUTHORIZED

When the broker keeps running into issues due to self signed TLS certificates, you can tell the broker to disable TLS verification, by passing the 'NODE\_TLS\_REJECT\_UNAUTHORIZED' environment variable with value 0:

```
docker run -d \
  --name aikido-broker \
  --restart=on-failure:3 \
  --network host \
  -e CLIENT_SECRET="{secret}" \
  -e ALLOWED_INTERNAL_SUBNETS="192.168.0.0/16,10.0.0.0/8,172.16.0.0/12,127.0.0.0/8" \
  -e NODE_TLS_REJECT_UNAUTHORIZED=0 \
  aikidosecurity/broker-client:latest
```

## How to use Broker resources with Aikido

After you install the broker and add your internal URLs as resources, the broker generates a unique Aikido URL for each resource. These URLs act as secure entry points for Aikido to reach your internal services through the broker.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FksmQKP138piXBLNppbrv%2FScreenshot%202025-11-17%20at%2010.20.50.png?alt=media&#x26;token=950e23b4-b4e8-4da7-bff9-42e9ec9c70c9" alt=""><figcaption></figcaption></figure>

**Use these Aikido Broker URLs in all Aikido scans.**

This is important because:

* Aikido cannot reach your internal network directly
* The broker maps the Aikido URL to your internal service
* Using the internal URL directly will not work

#### Example

When configuring a Domains and API scan (front-end scan), use the Broker URL instead of the internal address.

For example:

* Do not use <http://my-internal-app.test:8000>
* Use the generated broker URL, such as: <https://4948_c562ddc641.aikidobroker.com>

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FOKc95OLba6AsXQ9xyUyy%2FScreenshot%202025-11-17%20at%2010.25.48.png?alt=media&#x26;token=20fe9b24-ccf8-4827-ae89-51d008f6a602" alt=""><figcaption></figcaption></figure>

## Troubleshooting

### Run troubleshooting command

Run this command first. It runs a quick health check on your broker setup (DNS, connectivity, and other common failure points) and usually surfaces the root cause right away.

{% tabs %}
{% tab title="Docker" %}

```bash
docker exec -it aikido-broker node /app/diagnostics.cjs
```

{% endtab %}

{% tab title="Kubernetes" %}

```bash
kubectl exec <pod> -c broker-client -- node /app/diagnostics.cjs
```

{% endtab %}
{% endtabs %}

### Check logs

Check the Docker logs for warning messages and errors:

{% tabs %}
{% tab title="Docker" %}

```bash
docker logs aikido-broker
```

{% endtab %}

{% tab title="Kubernetes" %}

```
kubectl logs -n aikido -l app.kubernetes.io/name=broker-client
```

{% endtab %}
{% endtabs %}

### Error: Cannot access another client's resources

The cached client id no longer matches the `CLIENT_SECRET` organization. Delete the `config/client_id` file and try again.&#x20;
