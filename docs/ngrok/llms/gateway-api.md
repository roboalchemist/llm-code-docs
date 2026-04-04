# Source: https://ngrok.com/docs/getting-started/kubernetes/gateway-api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kubernetes Gateway API Quickstart

> Use ngrok with the Kubernetes Gateway API for advanced routing, policy control, and future-proof ingress configuration.

This quickstart uses the [ngrok Kubernetes Operator](/k8s) and [Gateway API resources](https://gateway-api.sigs.k8s.io/) to make the services you've deployed to Kubernetes available on the public internet.

Use this method if you:

* Want precise, Kubernetes-native control over routing behavior.
* Are building on a multi-team platform where the separation of concerns between the [roles and personas](https://gateway-api.sigs.k8s.io/concepts/roles-and-personas/) (infrastructure provider, cluster Operator, application developer) matters.
* Want to align with the Kubernetes community's vision for the future of ingress.

<Note>
  The ngrok Kubernetes Operator is available to all ngrok users at no additional charge.
  You only incur costs if the resources provisioned by the controller incur a cost.
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

## Install the Gateway API custom resource definitions

You can select either the [standard or experimental](https://gateway-api.sigs.k8s.io/guides/) set of Gateway API CRDs depending on your preference.
Either version will work with the ngrok Kubernetes Operator.

<Tabs>
  <Tab title="Standard">
    ```bash  theme={null}
    kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.4.1/standard-install.yaml
    ```
  </Tab>

  <Tab title="Experimental">
    ```
    kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.4.1/experimental-install.yaml
    ```
  </Tab>
</Tabs>

After installing the Gateway API CRDs, create the following `GatewayClass` so that you can mark which Gateway API resources the ngrok Operator should handle:

```bash  theme={null}
kubectl apply -f -<<EOF
apiVersion: gateway.networking.k8s.io/v1
kind: GatewayClass
metadata:
  name: ngrok
spec:
  controllerName: ngrok.com/gateway-controller
EOF
```

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

## 4. Define your `Gateway` and `HTTPSRoute` resources

This manifest exposes the `tinyllama` sample service on `$YOUR_DOMAIN`.
If you already have a different deployment on your cluster, you'll need to change the `backendRefs` name and port.

```yaml title="gwapi.yaml" theme={null}
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: ngrok-gateway
  namespace: default
spec:
  gatewayClassName: ngrok
  listeners:
    - name: http
      protocol: HTTP
      port: 80
      hostname: "$NGROK_DOMAIN"
      allowedRoutes:
        namespaces:
          from: All
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: tinyllama-route
  namespace: default
spec:
  parentRefs:
    - group: gateway.networking.k8s.io
      kind: Gateway
      name: ngrok-gateway
      namespace: default
  hostnames:
    - "$NGROK_DOMAIN"
  rules:
    - matches:
      - path:
          type: PathPrefix
          value: /
      backendRefs:
        - name: tinyllama
          port: 80
```

Apply the manifest with `kubectl apply -f gwapi.yaml`.

The ngrok Kubernetes Operator watches your cluster for `Gateway` and `HTTPRoute` resources that reference the `ngrok` GatewayClass, and immediately provisions a new Agent Endpoint.

You can now send a request to `$NGROK_DOMAIN` with your browser or `curl`.
Your Kubernetes service is now available to anyone on the public internet.

## 4. Secure your app with Traffic Policy

In cases where you need to restrict access to your API or app, [Traffic Policy](/traffic-policy) and the [`restrict-ips`](/traffic-policy/actions/restrict-ips) let you quickly allow only certain addresses to access your endpoint.

First, copy your public IP address via the [`ip4v.ngrok.com` mini-app](https://ipv4.ngrok.com/).

To add the rule, create a new `NgrokTrafficPolicy` resource and add it to your `Gateway` resource as an annotation.
This way, the rule runs on all requests matching any of the hostnames from the listeners on your `Gateway`.
Be sure to replace `$YOUR_PUBLIC_IP` with the value you just copied.

```yaml title="gwapi.yaml" theme={null}
apiVersion: ngrok.k8s.ngrok.com/v1alpha1
kind: NgrokTrafficPolicy
metadata:
  name: restrict-ips
  namespace: default
spec:
  policy:
    on_http_request:
      - actions:
          - type: restrict-ips
            config:
              enforce: true
              allow:
                - $YOUR_PUBLIC_IP
---
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: ngrok-gateway
  namespace: default
  annotations:
    k8s.ngrok.com/traffic-policy: restrict-ips
spec:
  gatewayClassName: ngrok
  listeners:
    - name: http
      protocol: HTTP
      port: 80
      hostname: "$NGROK_DOMAIN"
      allowedRoutes:
        namespaces:
          from: Same
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: tinyllama-route
  namespace: default
spec:
  parentRefs:
    - group: gateway.networking.k8s.io
      kind: Gateway
      name: ngrok-gateway
      namespace: default
  hostnames:
    - "$NGROK_DOMAIN"
  rules:
    - matches:
      - path:
          type: PathPrefix
          value: /
      backendRefs:
        - name: tinyllama
          port: 80
```

Re-apply the manifest with `kubectl apply -f gwapi.yaml`.

You can also add Traffic Policy as an [`ExtensionRef` filter](/k8s/guides/using-gwapi/#use-ngroktrafficpolicy-on-httproutes) if you want to run certain rules only on a single route.

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

* Read the [guide to using Gateway API](/k8s/guides/using-gwapi) with ngrok
* [Route requests to many upstream services](/k8s/guides/how-to/request-routing/) based on the path, headers, and query parameters
* Explore [TLS](/k8s/guides/how-to/tls-routing/) or [TCP](/k8s/guides/how-to/tcp-routing/) routing with Gateway API
* [Deploy an API gateway in one or multiple clouds](/guides/api-gateway/multicloud/)

For more ways to filter and manage traffic:

* [Traffic Policy overview](/traffic-policy)
* [Traffic Policy concepts](/traffic-policy/concepts/)
* All [available actions](/traffic-policy/actions/)

Finally, explore the [Traffic Inspector in your dashboard](https://dashboard.ngrok.com/traffic-inspector) for real-time observability of traffic flowing through your endpoint.


Built with [Mintlify](https://mintlify.com).