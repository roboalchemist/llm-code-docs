# Source: https://ngrok.com/docs/universal-gateway/endpoints.md

# Source: https://ngrok.com/docs/getting-started/kubernetes/endpoints.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kubernetes Endpoints Quickstart

> Connect any API or app to your Kubernetes clusters for local service projection, cross-cluster communication, and much more.

This quickstart uses the [ngrok Kubernetes Operator](/k8s) and the ngrok agent to create a [Kubernetes-bound Endpoint](/universal-gateway/kubernetes-endpoints/), which is accessible to other pods in your cluster as a native Service. ngrok then handles all routing to the upstream service, which can be running anywhere, like your development laptop or a cloud-based developer environment.

When you use Kubernetes Endpoints, you can:

* View changes to your local services immediately by [projecting your local development environment](https://ngrok.com/blog-post/kubernetes-dev-loop-projection) into a remote development or staging cluster.
* Allow services in multiple clusters to communicate over a service mesh that doesn't require firewalls, VPNs, or port forwarding.
* Securely access your customer's APIs or databases (via [site-to-site connectivity](/guides/site-to-site-connectivity/)).
* Allow your Kubernetes-deployed services to call a webhook URL exposed with ngrok to speed up local development or CI jobs.

You also don't need to expose your local services to the public internet or modify the ingress rules to remote clusters.

<Note>
  The ngrok Kubernetes Operator is available to all ngrok users at no additional charge.
  You only incur costs if the resources provisioned by the controller incur a cost.
  Find more details on the [pricing page](https://ngrok.com/pricing), or, if you're a free user, the [free plan limits](/pricing-limits/free-plan-limits/).
</Note>

## What you'll need

* An ngrok account
* The [ngrok CLI](/getting-started/#2-install-the-ngrok-agent-cli) installed on your local machine
* A running K8s cluster with `kubectl` access with at least one service
  * If you don't have a cluster yet, see the [local cluster guide](/k8s/guides/local-cluster/) for some options
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
    --set credentials.authtoken=$NGROK_AUTHTOKEN \
    --set bindings.enabled=true
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
    --set bindings.enabled=true
    ```
  </Tab>
</Tabs>

## 2. Start an Agent Endpoint

On your local machine, start a new Agent Endpoint, replacing `$PORT` with the port your upstream service listens on.

```bash  theme={null}
ngrok http $PORT --url http://hello-world.default --binding kubernetes
```

The URL of a Kubernetes Endpoint has three parts, which determine how ngrok exposes it inside your cluster: the scheme (`http`, `tcp`, or `tls`), the service name, and the namespace.
In this example, ngrok provisions the `http://hello-world.default` URL into a Kubernetes service named `hello-world` in the `default` namespace.

Behind the scenes, your ngrok Kubernetes Operator continuously polls the ngrok API for new endpoints with the `kubernetes` binding.
When it detects your new `http://hello-world.default` endpoint, it provisions a `ClusterIP` Kubernetes service that routes directly to that endpoint.

<Tip>
  You can also start agent-based Kubernetes Endpoints with:

  * The [SDKs](/agent-sdks/)
  * A second cluster
  * Cloud Endpoints with the [ngrok dashboard](https://dashboard.ngrok.com/endpoints)
  * The [API](/api)
</Tip>

## 3. Add Traffic Policy to manipulate requests (optional)

Kubernetes Endpoints support the entire breadth of [Traffic Policy](/traffic-policy), which lets you filter, manage, and orchestrate traffic as it passes between your local service and your cluster.

Because a Kubernetes Endpoint is only accessible inside of clusters where you've installed the ngrok Kubernetes Operator with your account's credentials, you don't need to add authentication.
Instead, you can add a header to your local service's response to demo how it works.

```yaml title="hello-world.yaml" theme={null}
on_http_respons:
  - actions:
      - type: add-header
        config:
          headers:
           x-hello-world: Hello, world!
```

Run your Agent Endpoint again with the new Traffic Policy file.

```bash  theme={null}
ngrok http $PORT --url http://hello-world.default --binding kubernetes --traffic-policy-file hello-world.yaml
```

## 4. Start making requests

You can now access your non-Kubernetes service from within your cluster.
Test it out by running a temporary `curl` image on your cluster:

```bash  theme={null}
kubectl run -i --tty --rm debug --restart=Never --image=appropriate/curl -- /bin/sh
```

From within that new pod, `curl` your endpoint to get a response from your service.

```bash  theme={null}
curl -i http://hello-world.default
```

The `-i` flag outputs response headers, which will show any headers you added through your Traffic Policy.

## What's next?

First, read up on the rest of the Kubernetes Endpoints docs:

* [Kubernetes Endpoints](/universal-gateway/kubernetes-endpoints/)
* [Using Endpoint Bindings with the Operator](/k8s/guides/bindings/)

Ready to replace Telepresence with ngrok's Kubernetes Endpoints?
Read the [blog post](https://ngrok.com/blog-post/kubernetes-dev-loop-projection) on the process and *why* it's easier for both platform engineers and API/app developers.

Kubernetes Endpoints also support [Traffic Policy](/traffic-policy):

* [Traffic Policy overview](/traffic-policy)
* [Traffic Policy concepts](/traffic-policy/concepts/)
* All [available actions](/traffic-policy/actions/), including a few most relevant to these types of endpoints:
  * [`add-headers`](/traffic-policy/actions/add-headers/)
  * [`rate-limit`](/traffic-policy/actions/rate-limit/)
  * [`verify-webhook`](/traffic-policy/actions/verify-webhook/)

Finally, explore the [Traffic Inspector in your dashboard](https://dashboard.ngrok.com/traffic-inspector) for real-time observability of traffic flowing through your endpoint.


Built with [Mintlify](https://mintlify.com).