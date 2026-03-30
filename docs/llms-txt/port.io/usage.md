# Source: https://docs.port.io/actions-and-automations/setup-backend/webhook/port-execution-agent/usage.md

# Usage

To make use of the **Port execution agent**, you need to configure:

* [Self-Service Action invocation method](/actions-and-automations/setup-backend/.md#invocation-method-structure-fields) / Change Log destination `type` field value should be equal to `WEBHOOK`.
* [Self-Service Action invocation method](/actions-and-automations/setup-backend/.md#invocation-method-structure-fields) / Change Log `agent` field value should be equal to `true`.

For example:

```
{ "type": "WEBHOOK", "agent": true, "url": "URL_TO_API_INSIDE_YOUR_NETWORK" }
```

When using the execution agent, in the `url` field you need to provide a URL to a service (for example, a REST API) that will accept the invocation event.

* The service can be a private service running inside your private network;
* Or, it can be a public accessible service from the public internet (**note** in this scenario, the execution agent needs corresponding outbound network rules that will allow it to contact the public service).

Once configured, the Port Agent will run in your environment and trigger webhooks for self-service actions or software catalog changes.

![Port Execution Agent Logs](/assets/images/portAgentLogs-cd791551e6c705b1439d3a4fc76e285f.png)

Advanced configuration

For a complete list of all available configuration parameters and their descriptions, see the [Port Agent Helm chart README](https://github.com/port-labs/helm-charts/tree/main/charts/port-agent).

## Streamer types[â](#streamer-types "Direct link to Streamer types")

The Port Agent supports two streamer mechanisms for receiving and processing action runs:

### Kafka streamer (default)[â](#kafka-streamer-default "Direct link to Kafka streamer (default)")

The default and recommended streamer mechanism that uses Kafka for real-time event streaming.

**When to use:**

* Where higher latency is acceptable

Install the agent with Kafka streamer:

```
helm upgrade --install my-port-agent port-labs/port-agent \
    --create-namespace --namespace port-agent \
    --set env.normal.PORT_ORG_ID="YOUR_ORG_ID" \
    --set env.normal.STREAMER_NAME=KAFKA \
    --set env.normal.KAFKA_CONSUMER_GROUP_ID="YOUR_CONSUMER_GROUP_ID" \
    --set env.secret.PORT_CLIENT_ID="YOUR_CLIENT_ID" \
    --set env.secret.PORT_CLIENT_SECRET="YOUR_CLIENT_SECRET"
```

### Polling streamer[â](#polling-streamer "Direct link to Polling streamer")

An alternative streamer mechanism that polls the Port API via HTTP to retrieve pending action runs.

**When to use:**

* When Kafka connectivity is restricted or unavailable in your environment
* For simpler network configurations requiring only HTTP access
* Where higher latency is acceptable

**Considerations:**

* **Polling-based:** Can take a few seconds longer to pick up new action runs compared to Kafka.
* **Secrets not supported:** Encrypted user inputs and organization secrets (`.secrets.*`) cannot be used in the payload when using polling mode. You can [control the payload](/actions-and-automations/setup-backend/webhook/port-execution-agent/control-the-payload.md) to load secrets from your environment instead.

**Configuration:**

For the Helm installation, set:

```
--set env.normal.STREAMER_NAME=POLLING
```

Note: POLLING streamer does not require `KAFKA_CONSUMER_GROUP_ID`.

## When to use polling vs Kafka[â](#when-to-use-polling-vs-kafka "Direct link to When to use polling vs Kafka")

### Comparison[â](#comparison "Direct link to Comparison")

| Aspect             | Polling                        | Kafka                                        |
| ------------------ | ------------------------------ | -------------------------------------------- |
| Horizontal scaling | â Unlimited pods              | â Limited by partition count                |
| Latency            | Based on the polling intervals | Real-time                                    |
| Dynamic scaling    | â Add/remove pods instantly   | â Requires support ticket to add partitions |

## Self-signed certificate configuration[â](#self-signed-certificate-configuration "Direct link to Self-signed certificate configuration")

For self-hosted 3rd-party applications with self-signed certificates, the agent can be configured to trust custom CA certificates. The `selfSignedCertificate` parameters control this behavior.

### Option 1: Provide certificate in Helm values[â](#option-1-provide-certificate-in-helm-values "Direct link to Option 1: Provide certificate in Helm values")

Use this option to provide the certificate content directly in your Helm values file or via the `--set-file` flag.

**How to use:**

1. Set `selfSignedCertificate.enabled` to `true`
2. Provide the certificate content in `selfSignedCertificate.certificate`
3. Keep `selfSignedCertificate.secret.useExistingSecret` as `false` (default)

**Method A: Inline certificate in values.yaml**

Configure in your `values.yaml`:

```
selfSignedCertificate:
  enabled: true
  certificate: |
    -----BEGIN CERTIFICATE-----
    <YOUR_CERTIFICATE_CONTENT>
    -----END CERTIFICATE-----
  secret:
    name: ""
    key: crt
    useExistingSecret: false
```

Install with:

```
helm install my-port-agent port-labs/port-agent \
   --create-namespace --namespace port-agent \
   -f values.yaml
```

**Method B: Reference certificate file using `--set-file`**

Configure in your `custom_values.yaml`:

```
selfSignedCertificate:
  enabled: true
  certificate: ""
  secret:
    name: ""
    key: crt
    useExistingSecret: false
```

Install with:

```
helm install my-port-agent port-labs/port-agent \
   --create-namespace --namespace port-agent \
   -f custom_values.yaml \
   --set selfSignedCertificate.enabled=true \
   --set-file selfSignedCertificate.certificate=/PATH/TO/CERTIFICATE.crt
```

### Option 2: Use existing Kubernetes secret[â](#option-2-use-existing-kubernetes-secret "Direct link to Option 2: Use existing Kubernetes secret")

Use this option to reference a pre-existing Kubernetes secret that you manage separately. The secret must contain the certificate data.

**How to use:**

1. Set `selfSignedCertificate.enabled` to `true`.
2. Set `selfSignedCertificate.secret.useExistingSecret` to `true`.
3. Specify the secret name in `selfSignedCertificate.secret.name`.
4. Specify the key within the secret in `selfSignedCertificate.secret.key` (defaults to `crt`).
5. Leave `selfSignedCertificate.certificate` empty.

**Complete configuration:**

```
selfSignedCertificate:
  enabled: true
  certificate: ""
  secret:
    name: my-ca-cert
    key: ca.crt
    useExistingSecret: true
```

### Automatic configuration[â](#automatic-configuration "Direct link to Automatic configuration")

When `selfSignedCertificate.enabled` is set to `true`, the Helm chart automatically:

* Mounts the certificate to `/usr/local/share/ca-certificates/cert.crt`
* Sets `SSL_CERT_FILE` and `REQUESTS_CA_BUNDLE` environment variables to point to the certificate

### Multiple certificates[â](#multiple-certificates "Direct link to Multiple certificates")

For environments requiring multiple custom certificates, use the `extraVolumes` and `extraVolumeMounts` parameters alongside the built-in `selfSignedCertificate` feature. One certificate must be provided via `selfSignedCertificate`, and additional certificates can be mounted as extra volumes.

**Configuration:**

```
selfSignedCertificate:
  enabled: true
  secret:
    name: primary-cert
    key: ca.crt
    useExistingSecret: true

extraVolumes:
  - name: additional-certs
    secret:
      secretName: secondary-certs
extraVolumeMounts:
  - name: additional-certs
    mountPath: /usr/local/share/ca-certificates/cert2.crt
    subPath: cert2.crt
    readOnly: true
```

Certificate requirements

* Each certificate must be provided in PEM format as a separate file
* Certificates must be mounted to `/usr/local/share/ca-certificates/` with a `.crt` file extension

## Overriding configurations[â](#overriding-configurations "Direct link to Overriding configurations")

You can override default values using the `--set` flag during agent installation/upgrade:

```
helm upgrade --install my-port-agent port-labs/port-agent \
    --create-namespace --namespace port-agent \
    --set env.normal.PORT_ORG_ID="YOUR_ORG_ID" \
    --set env.normal.KAFKA_CONSUMER_GROUP_ID="YOUR_CONSUMER_GROUP_ID" \
    --set env.secret.PORT_CLIENT_ID="YOUR_CLIENT_ID" \
    --set env.secret.PORT_CLIENT_SECRET="YOUR_CLIENT_SECRET" \
    --set secret.useExistingSecret=false \
    --set replicaCount=2 \
    --set resources.limits.memory="512Mi"
```

## Extra environment variables[â](#extra-environment-variables "Direct link to Extra environment variables")

To pass extra environment variables to the agent's runtime, you can use the `env.normal` section for non-sensitive variables.

Using Helm's `--set` flag:

```
helm upgrade --install my-port-agent port-labs/port-agent \
  # Standard installation flags
  # ...
  --set env.normal.HTTP_PROXY=http://my-proxy.com:1111 \
  --set env.normal.HTTPS_PROXY=http://my-proxy.com:2222
```

Using the `values.yaml` file:

```
# The rest of the configuration
# ...
env:
  normal:
    HTTP_PROXY: "http://my-proxy.com:1111"
    HTTPS_PROXY: "http://my-proxy.com:2222"
    NO_PROXY: "127.0.0.1,localhost"
```

### Proxy configuration[â](#proxy-configuration "Direct link to Proxy configuration")

#### `HTTP_PROXY`, `HTTPS_PROXY` & `ALL_PROXY`[â](#http_proxy-https_proxy--all_proxy "Direct link to http_proxy-https_proxy--all_proxy")

`HTTP_PROXY`, `HTTPS_PROXY`, and `ALL_PROXY` are environment variables used to specify a proxy server for handling HTTP, HTTPS, or all types of requests, respectively. The values assigned to these settings should be the URL of the proxy server.

For example:

```
HTTP_PROXY=http://my-proxy.com:1111
HTTPS_PROXY=http://my-proxy.com:2222
ALL_PROXY=http://my-proxy.com:3333
```

#### `NO_PROXY`[â](#no_proxy "Direct link to no_proxy")

`NO_PROXY` allows blacklisting certain addresses from being handled through a proxy. This variable accepts a comma-separated list of hostnames or URLs.

For example:

```
NO_PROXY=http://127.0.0.1,google.com
```

For more information, see the Requests [proxy configuration documentation](https://requests.readthedocs.io/en/latest/user/advanced/#proxies).

### SSL verification[â](#ssl-verification "Direct link to SSL verification")

By default, the agent verifies SSL certificates for all outgoing webhook requests. To disable verification (e.g. when targeting internal services with self-signed certificates), set `WEBHOOK_VERIFY_SSL` to `false`.

```
WEBHOOK_VERIFY_SSL=false
```

## Next Steps[â](#next-steps "Direct link to Next Steps")

Follow one of the guides below:

* [GitLab Pipeline Trigger](/actions-and-automations/setup-backend/gitlab-pipeline/.md) - Create an action that triggers GitLab Pipeline execution.
