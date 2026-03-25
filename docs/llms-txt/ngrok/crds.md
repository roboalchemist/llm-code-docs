# Source: https://ngrok.com/docs/getting-started/kubernetes/crds.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kubernetes Custom Resources Quickstart

> Leverage ngrok’s custom Kubernetes CRDs for the simplest path, with the least amount of YAML, to exposing your Kubernetes services to the public internet.

This quickstart uses the [ngrok Kubernetes Operator](/k8s) and [ngrok's custom resources](/k8s/crds) (CRs) to make the services you've deployed to Kubernetes available on the public internet.

Use this method if you:

* Want the easiest path, requiring the least amount of YAML, to create ingress for your resources compared to [Ingress](/getting-started/kubernetes/ingress) or [Gateway API](/getting-started/kubernetes/gateway-api) resources.
* Are okay with using Kubernetes-native resources, but not necessarily following Kubernetes standards.

<Note>
  The ngrok Kubernetes Operator is available to all ngrok users at no additional charge.
  You only incur costs if the resources provisioned by the controller incur a cost
  Find more details on the [pricing page](https://ngrok.com/pricing), or, if you're a free user, the [free plan limits](/pricing-limits/free-plan-limits/).
</Note>

## What you'll need

* An ngrok account and a [reserved domain](https://dashboard.ngrok.com/domains)
* A running K8s cluster with `kubectl` access with at least one service
  * If you don't have a cluster yet, see our [local cluster guide](/k8s/guides/local-cluster/) for some options
* [`kubectl`](https://kubernetes.io/docs/reference/kubectl/) and [Helm](https://helm.sh/docs/intro/install/) 3.0.0 or later installed locally

## 1. Install the ngrok Kubernetes Operator

### Add the ngrok Helm chart

```bash  theme={null}
helm repo add ngrok https://charts.ngrok.com
helm repo update
```

<Note>
  Whenever you want to update the Operator or install a new version, you must run `helm repo update` to fetch the latest charts.
</Note>

### Get your ngrok API key and authtoken

You can get both these from the ngrok dashboard:

* Your [authtoken](https://dashboard.ngrok.com/get-started/your-authtoken)
* An [API key](https://dashboard.ngrok.com/api)

The ngrok Kubernetes Operator provisions these as a Kubernetes secret, then uses the authtoken to create tunnels.
The Operator uses your API key to manage resources via the [ngrok API](/api/).

<Tabs>
  <Tab title="Linux">
    ```bash  theme={null}
    export NGROK_AUTHTOKEN=your copied auth token goes here
    export NGROK_API_KEY=your copied api key goes here
    ```
  </Tab>

  <Tab title="PowerShell">
    ```powershell  theme={null}
    $env:NGROK_AUTHTOKEN = "your copied auth token goes here"
    $env:NGROK_API_KEY   = "your copied api key goes here"
    ```
  </Tab>
</Tabs>

### Install the Operator

We recommend installing the Operator into the default `ngrok-operator` namespace.
You can change this depending in the commands blow based on your cluster configuration, but by default, the Operator works with `Gateway` and routing resources in all namespaces.

You can choose between passing your credentials directly with Helm or creating a Kubernetes `Secret` resource that you pass to the Helm chart.
The simple method only takes one command, but with the secure method, you:

* Prevent anyone with `kubectl` access to the cluster from viewing your API key and authtoken with `helm get values`.
* Integrate more cleanly with infrastructure as code (IaC) tools and processes.

<Tabs>
  <Tab title="Simple">
    ```bash  theme={null}
    helm install ngrok-operator ngrok/ngrok-operator \
    --namespace ngrok-operator \
    --create-namespace \
    --set credentials.apiKey=$NGROK_API_KEY \
    --set credentials.authtoken=$NGROK_AUTHTOKEN
    ```
  </Tab>

  <Tab title="More secure">
    First, prepare new environment variables.

    ```bash  theme={null}
    export ENCODED_NGROK_AUTHTOKEN=$(echo -n "$NGROK_AUTHTOKEN" | base64)
    export ENCODED_NGROK_API_KEY=$(echo -n "$NGROK_API_KEY" | base64)
    ```

    Apply a `Secret` resource with your encoded credentials.

    ```bash  theme={null}
    kubectl apply -f -<<EOF
    apiVersion: v1
    kind: Secret
    metadata:
      name: ngrok-operator-credentials
      namespace: ngrok-operator
    data:
      API_KEY: "$ENCODED_NGROK_API_KEY"
      AUTHTOKEN: "$ENCODED_NGROK_AUTHTOKEN"
    EOF
    ```

    Next, install the Operator and reference the `Secret` resource.

    ```bash  theme={null}
    helm install ngrok-operator ngrok/ngrok-operator \
    --namespace ngrok-operator \
    --create-namespace \
    --set credentials.secret.name=ngrok-operator-credentials \
    ```
  </Tab>
</Tabs>

## 2. Get your domain

Head over to the [**Domains** section](https://dashboard.ngrok.com/domains) and click **+ New Domain** to grab a new domain.
You can choose between a static domain with an ngrok-branded TLD like `.ngrok.app` or `.ngrok.io`, or you can [bring a custom domain](/universal-gateway/custom-domains/).

We'll refer to this as `$YOUR_DOMAIN` from here on out.

## 3. Deploy a sample service

If you don't already have an app to try out, try out this sample manifest, which installs our [TinyLlama image](https://github.com/ngrok-samples/tinyllama) onto your cluster.
Save the YAML below into a file named `deployment.yaml`.

If you already have a deployment, you can skip this step, but you'll need to adapt the Operator configuration and test requests.

```yaml title="deployment.yaml" theme={null}
apiVersion: apps/v1
kind: Deployment
metadata:
  name: tinyllama
  namespace: default
spec:
  replicas: 1
  selector:
    matchLabels:
      app: tinyllama
  template:
    metadata:
      labels:
        app: tinyllama
    spec:
      containers:
        - name: tinyllama
          image: ghcr.io/ngrok-samples/tinyllama:main
          ports:
            - containerPort: 8080
          resources:
            requests:
              cpu: "1"
              memory: "2Gi"
            limits:
              cpu: "2"
              memory: "3Gi"
---
apiVersion: v1
kind: Service
metadata:
  name: tinyllama
  namespace: default
spec:
  selector:
    app: tinyllama
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
  type: ClusterIP
```

Add the deployment and service to your cluster with `kubectl`.

```bash  theme={null}
kubectl apply -f deployment.yaml
```

## 4. Create your endpoint manifest

You have two options to expose your Kubernetes service with ngrok's CRDs. The primary two types are `CloudEndpoint` and `AgentEndpoint`.

1. A single `AgentEndpoint` resource: This option is simplest, but is typically limited to exposing one service on a hostname.
2. A pair of `CloudEndpoint` and `AgentEndpoint` resources: This option allows you to route traffic to any number of Kubernetes services from a single hostname depending on their path, headers, and more using [expressions](/traffic-policy/concepts/expressions/) and the [`forward-internal` Traffic Policy action](/traffic-policy/actions/forward-internal).

When using other types of configuration with the Operator such as `Ingress` and Gateway API resources, the Operator translates all of them into
`CloudEndpoint` and `AgentEndpoint` resources. Using the `CloudEndpoint`/`AgentEndpoint` resources directly gives you maximum control over your ngrok Operator configuration.
For more information about cloud and Agent Endpoints, see [the endpoint types page](/universal-gateway/types/).

This manifest exposes a Kubernetes service named `tinyllama` listening on port `80` on `$YOUR_DOMAIN`.
If you already have a different deployment on your cluster, you'll need to change the backend service name and port.

<Tabs>
  <Tab title="AgentEndpoint">
    ```yaml title="ngrok-crds.yaml" theme={null}
    apiVersion: ngrok.k8s.ngrok.com/v1alpha1
    kind: AgentEndpoint
    metadata:
      name: tinyllama-endpoint
    spec:
      url: https://$YOUR_DOMAIN
      upstream:
        url: http://tinyllama.default:80
    ```
  </Tab>

  <Tab title="CloudEndpoint + AgentEndpoint">
    ```yaml title="ngrok-crds.yaml" theme={null}
    apiVersion: ngrok.k8s.ngrok.com/v1alpha1
    kind: CloudEndpoint
    metadata:
      name: tinyllama-cloud-endpoint
    spec:
      url: $YOUR_DOMAIN
    trafficPolicy:
      policy:
        on_http_request:
          - actions:
            - type: forward-internal
              config:
                url: http://tinyllama.internal
    ---
    apiVersion: ngrok.k8s.ngrok.com/v1alpha1
    kind: AgentEndpoint
    metadata:
      name: tinyllama-endpoint
    spec:
      url: http://tinyllama.internal
      upstream:
        url: http://tinyllama.default:80
    ```
  </Tab>
</Tabs>

Apply the manifest with `kubectl -n ngrok-operator apply -f ngrok-crds.yaml`.

The ngrok Kubernetes Operator watches your cluster for `AgentEndpoint` and `CloudEndpoint` resources you create, and provisions a new Agent Endpoint to forward traffic into your Service.

You can now send a request to `$NGROK_DOMAIN` with your browser or `curl`.
Your Kubernetes service is now available to anyone on the public internet.

## 4. Secure your app with Traffic Policy

In cases where you need to restrict access to your API or app, [Traffic Policy](/traffic-policy) and the [`restrict-ips`](/traffic-policy/actions/restrict-ips) let you quickly allow only certain addresses to access your endpoint.

First, copy your public IP address via the [`ip4v.ngrok.com` mini-app](https://ipv4.ngrok.com/).

<Tabs>
  <Tab title="AgentEndpoint">
    Add a `trafficPolicy.inline` field followed by the Traffic Policy rule itself.

    ```yaml title="ngrok-crds.yaml" theme={null}
    apiVersion: ngrok.k8s.ngrok.com/v1alpha1
    kind: AgentEndpoint
    metadata:
      name: tinyllama-endpoint
    spec:
      url: https://$YOUR_DOMAIN
      upstream:
        url: http://tinyllama.default:80
      trafficPolicy:
        inline:
          on_http_request:
            - actions:
                - type: restrict-ips
                  config:
                    enforce: true
                    allow:
                      - $YOUR_PUBLIC_IP
    ```
  </Tab>

  <Tab title="CloudEndpoint + AgentEndpoint">
    Insert the new rule above your existing `forward-internal` action to require authentication before forwarding traffic to your internal Agent Endpoint.

    ```yaml title="ngrok-crds.yaml" theme={null}
    apiVersion: ngrok.k8s.ngrok.com/v1alpha1
    kind: CloudEndpoint
    metadata:
      name: tinyllama-cloud-endpoint
    spec:
      url: $YOUR_DOMAIN
      trafficPolicy:
        policy:
          on_http_request:
            - actions:
                - type: restrict-ips
                  config:
                    enforce: true
                    allow:
                      - $YOUR_PUBLIC_IP
            - actions:
              - type: forward-internal
                config:
                  url: http://tinyllama.internal
    ---
    apiVersion: ngrok.k8s.ngrok.com/v1alpha1
    kind: AgentEndpoint
    metadata:
      name: tinyllama-endpoint
    spec:
      url: http://tinyllama.internal
      upstream:
        url: http://tinyllama.default:80
    ```
  </Tab>
</Tabs>

Re-apply the manifest with `kubectl apply -f ngrok-crds.yaml`.

## 5. Start sending requests

You can now verify that your Kubernetes service is accessible from the public internet and that your Traffic Policy rules are in place.
If you deployed the `tinyllama` service:

* Chat with the LLM in your browser: `https://$YOUR_DOMAIN`
* Send a completions request to the API:

  ```bash  theme={null}
  curl http://$YOUR_DOMAIN/v1/completions \
  	-H "Content-Type: application/json" \
  	-d '{
  			"model": "tinyllama-1.1b-chat-v1.0.Q5_K_M",
  			"prompt": "Why is the sky blue?",
  			"max_tokens": 128
  		}'
  ```

## What's next?

Learn more about using ngrok with your Kubernetes deployments:

* Read the [guide to ngrok's CRDs](/k8s/guides/using-crds), including how to create a Cloud Endpoint
* [Route requests to many upstream services](/k8s/guides/how-to/request-routing/) based on the path, headers, and query parameters
* Deploy an [API gateway](/guides/api-gateway/get-started) in one or [multiple clouds](/guides/api-gateway/multicloud/)
* [Learn how to configure HTTP/HTTPS/TCP/TLS traffic](/k8s/guides/endpoint-types/) with `CloudEndpoint` and `AgentEndpoint`.

For more ways to filter and manage traffic:

* [Traffic Policy overview](/traffic-policy)
* [Traffic Policy concepts](/traffic-policy/concepts/)
* All [available actions](/traffic-policy/actions/)

Finally, explore the [Traffic Inspector in your dashboard](https://dashboard.ngrok.com/traffic-inspector) for real-time observability of traffic flowing through your endpoint.

```
```


Built with [Mintlify](https://mintlify.com).