# Source: https://fly.io/docs/kubernetes/services/

Title: Configure FKS Services

URL Source: https://fly.io/docs/kubernetes/services/

Markdown Content:
Configure FKS Services · Fly Docs
===============

[Skip to content](https://fly.io/docs/kubernetes/services/#main-content-start)

[](https://fly.io/)[](https://fly.io/docs/)

[**Need a Logo?** View Our Brand Assets](https://fly.io/docs/about/brand/)

Search

Open main menu[](https://fly.io/)[](https://fly.io/docs/)

[Pricing](https://fly.io/pricing/)[Support](https://fly.io/docs/about/support/)

[Sign In](https://fly.io/app/sign-in/)[Sign Up](https://fly.io/app/sign-up/)

[Getting Started](https://fly.io/docs/getting-started/launch)Toggle Getting Started section
*   [Quickstart: Launch your app](https://fly.io/docs/getting-started/launch/)
*   [Launch HelloFly Demo App](https://fly.io/docs/getting-started/launch-demo)
*   [Deep Dive Demo App](https://fly.io/docs/deep-dive/)
*   [Choose a Language or Framework](https://fly.io/docs/getting-started/get-started-by-framework/)
*   [Fly.io Essentials](https://fly.io/docs/getting-started/essentials/)
*   [Migrate from Heroku](https://fly.io/docs/getting-started/migrate-from-heroku/)
*   [Troubleshoot Deployments](https://fly.io/docs/getting-started/troubleshooting/)

[Guides (Blueprints)](https://fly.io/docs/blueprints/)Toggle Guides (Blueprints) section
*   [Guides Overview](https://fly.io/docs/blueprints/)

[Apps on Fly.io](https://fly.io/docs/apps/overview)Toggle Apps on Fly.io section
*   [Fly Apps Overview](https://fly.io/docs/apps/overview/)
*   [Fly Launch](https://fly.io/docs/launch/)
*   [Secrets](https://fly.io/docs/apps/secrets/)
*   [Production Checklist](https://fly.io/docs/apps/going-to-production/)

[Languages & Frameworks](https://fly.io/docs/languages-and-frameworks/)Toggle Languages & Frameworks section
*   [Elixir](https://fly.io/docs/elixir/)
*   [Rails](https://fly.io/docs/rails/getting-started/)
*   [Laravel](https://fly.io/docs/laravel/)
*   [Django](https://fly.io/docs/django/getting-started/)
*   [JavaScript](https://fly.io/docs/js/)
*   [Rust](https://fly.io/docs/rust/)
*   [Python](https://fly.io/docs/python/)
*   [More...](https://fly.io/docs/languages-and-frameworks/)

[Fly Machines](https://fly.io/docs/machines/overview)Toggle Fly Machines section
*   [Introduction to Fly Machines](https://fly.io/docs/machines/overview/)
*   [Machines API](https://fly.io/docs/machines/api/)
*   [Run a New Machine](https://fly.io/docs/machines/flyctl/fly-machine-run/)
*   [Update a Machine](https://fly.io/docs/machines/flyctl/fly-machine-update/)
*   [Machine Sizing](https://fly.io/docs/machines/guides-examples/machine-sizing/)
*   [Machine Restart Policy](https://fly.io/docs/machines/guides-examples/machine-restart-policy/)
*   [Machine States](https://fly.io/docs/machines/machine-states/)
*   [Run User Code on Fly Machines](https://fly.io/docs/machines/guides-examples/functions-with-machines/)
*   [One App Per Customer - Why?](https://fly.io/docs/machines/guides-examples/one-app-per-user-why/)
*   [The Machine Runtime Environment](https://fly.io/docs/machines/runtime-environment/)

[Managed Postgres](https://fly.io/docs/mpg)Toggle Managed Postgres section
*   [Create and Connect to a Managed Postgres Cluster](https://fly.io/docs/mpg/create-and-connect/)
*   [Cluster Configuration Options](https://fly.io/docs/mpg/configuration/)
*   [Phoenix with Managed Postgres](https://fly.io/docs/mpg/guides-examples/phoenix-guide/)
*   [Monitoring and Metrics](https://fly.io/docs/mpg/metrics/)
*   [Import data from another postgres cluster](https://fly.io/docs/mpg/import/)
*   [Supported Postgres Extensions](https://fly.io/docs/mpg/extensions/)

[Fly GPUs](https://fly.io/docs/gpus/gpu-quickstart)Toggle Fly GPUs section
*   [GPU Quickstart](https://fly.io/docs/gpus/gpu-quickstart/)
*   [Getting Started with GPU Machines](https://fly.io/docs/gpus/getting-started-gpus/)
*   [Python GPU Dev Machine](https://fly.io/docs/gpus/python-gpu-example/)

[Databases & Storage](https://fly.io/docs/database-storage-guides/)Toggle Databases & Storage section
*   [Fly Managed Postgres](https://fly.io/docs/mpg/)
*   [Tigris Object Storage](https://fly.io/docs/tigris/)
*   [Upstash for Redis®](https://fly.io/docs/upstash/redis/)

[Fly Volumes](https://fly.io/docs/volumes/overview)Toggle Fly Volumes section
*   [Fly Volumes Overview](https://fly.io/docs/volumes/overview/)
*   [Create and Manage Volumes](https://fly.io/docs/volumes/volume-manage/)
*   [Manage Volume Snapshots](https://fly.io/docs/volumes/snapshots/)
*   [Volume States](https://fly.io/docs/volumes/volume-states/)

[Fly Kubernetes](https://fly.io/docs/kubernetes/fks-quickstart)Toggle Fly Kubernetes section
*   [Fly Kubernetes Quickstart](https://fly.io/docs/kubernetes/fks-quickstart/)
*   [Fly Kubernetes Features](https://fly.io/docs/kubernetes/fks-features/)
*   [Create an FKS Cluster](https://fly.io/docs/kubernetes/clusters/)
*   [Connect to an FKS Cluster](https://fly.io/docs/kubernetes/connect-clusters/)
*   [Configure FKS Services](https://fly.io/docs/kubernetes/services/)
*   [Use GPUs with FKS](https://fly.io/docs/kubernetes/using-gpus/)
*   [Use Volumes with FKS](https://fly.io/docs/kubernetes/using-volumes/)

[Networking](https://fly.io/docs/networking/)Toggle Networking section
*   [Connect to an App Service](https://fly.io/docs/networking/app-services/)
*   [Public Networking](https://fly.io/docs/networking/services/)
*   [Private Networking](https://fly.io/docs/networking/private-networking/)
*   [Custom Private Networks](https://fly.io/docs/networking/custom-private-networks/)
*   [Flycast - Private Proxy Services](https://fly.io/docs/networking/flycast/)
*   [Egress IP Addresses](https://fly.io/docs/networking/egress-ips/)
*   [Dynamic Request Routing](https://fly.io/docs/networking/dynamic-request-routing/)
*   [Custom Domains](https://fly.io/docs/networking/custom-domain/)
*   [Understanding Cloudflare](https://fly.io/docs/networking/understanding-cloudflare/)
*   [Request Headers](https://fly.io/docs/networking/request-headers/)
*   [Run UDP Services](https://fly.io/docs/networking/udp-and-tcp/)
*   [TLS Support](https://fly.io/docs/networking/tls/)

[Monitoring](https://fly.io/docs/monitoring/)Toggle Monitoring section
*   [Metrics](https://fly.io/docs/monitoring/metrics/)
*   [Sentry Error Tracking](https://fly.io/docs/monitoring/sentry/)
*   [Logging](https://fly.io/docs/monitoring/logging-overview/)Toggle Logging section
    *   [Live Tail Logs](https://fly.io/docs/monitoring/live-tail-logs/)
    *   [Logs API Options](https://fly.io/docs/monitoring/logs-api-options/)
    *   [Search Logs](https://fly.io/docs/monitoring/search-logs/)
    *   [Export Logs](https://fly.io/docs/monitoring/exporting-logs/)
    *   [Error Codes](https://fly.io/docs/monitoring/error-codes/)

[Security](https://fly.io/docs/security/)Toggle Security section
*   [Organization Roles and Permissions](https://fly.io/docs/security/org-roles-permissions/)
*   [SSO for Organizations](https://fly.io/docs/security/sso/)
*   [Remove a Member from an Org](https://fly.io/docs/security/remove-org-member/)
*   [TLS Termination](https://fly.io/docs/security/tls-termination/)
*   [App Security by Arcjet](https://fly.io/docs/security/arcjet/)
*   [Access Tokens](https://fly.io/docs/security/tokens/)
*   [OpenID Connect](https://fly.io/docs/reference/openid-connect/)
*   [Shared Responsibility Model](https://fly.io/docs/security/shared-responsibility/)
*   [Security Practices and Compliance](https://fly.io/docs/security/security-at-fly-io/)

[Reference](https://fly.io/docs/reference/)Toggle Reference section
*   [flyctl](https://fly.io/docs/flyctl/)
*   [App Config Reference (fly.toml)](https://fly.io/docs/reference/configuration/)
*   [Architecture](https://fly.io/docs/reference/architecture/)
*   [Autoscaling](https://fly.io/docs/reference/autoscaling/)
*   [AWS to Fly Overview](https://fly.io/docs/reference/aws-to-fly-guide/)
*   [Builders](https://fly.io/docs/reference/builders/)
*   [Content Encoding](https://fly.io/docs/reference/content-encoding/)
*   [Fly Launch](https://fly.io/docs/reference/fly-launch/)
*   [Health Checks](https://fly.io/docs/reference/health-checks/)
*   [Load Balancing](https://fly.io/docs/reference/load-balancing/)
*   [Machine Migration](https://fly.io/docs/reference/machine-migration/)
*   [Multiple Processes in Apps](https://fly.io/docs/app-guides/multiple-processes/)
*   [Fly Proxy](https://fly.io/docs/reference/fly-proxy/)
*   [Fly Proxy Autostop/Autostart](https://fly.io/docs/reference/fly-proxy-autostop-autostart/)
*   [Regions](https://fly.io/docs/reference/regions/)
*   [Suspend/Resume](https://fly.io/docs/reference/suspend-resume/)

[About](https://fly.io/docs/about/)Toggle About section
*   [Pricing](https://fly.io/docs/about/pricing/)
*   [Billing](https://fly.io/docs/about/billing/)
*   [Cost Management](https://fly.io/docs/about/cost-management/)
*   [Free Trial](https://fly.io/docs/about/free-trial/)
*   [Support](https://fly.io/docs/about/support/)
*   [Engineering Jobs](https://fly.io/docs/hiring/)
*   [Healthcare on Fly.io](https://fly.io/docs/about/healthcare/)
*   [Extensions Program](https://fly.io/docs/about/extensions/)
*   [Extensions API](https://fly.io/docs/reference/extensions_api/)
*   [Merch](https://fly.io/docs/about/merch/)
*   [Open Source](https://fly.io/docs/about/open-source/)
*   [Using Our Brand](https://fly.io/docs/about/brand/)
*   [Privacy Policy](https://fly.io/legal/privacy-policy/)
*   [Terms of Service](https://fly.io/legal/terms-of-service/)

--- title: Configure FKS Services layout: docs toc: false nav: firecracker --- <div class= "important icon"> Fly Kubernetes is in closed beta and not recommended for critical production usage. To report issues or provide feedback, email us at beta@fly.io. </div> A [Kubernetes Service](https://kubernetes.io/docs/concepts/services-networking/service/+external) exposes applications running on your cluster. Fly Kubernetes supports ClusterIP and LoadBalancer Services. You can create a Service with a service configuration file. Here's an example ClusterIP service: ```yaml apiVersion: v1 kind: Service metadata: name: fksdemo-service spec: selector: app: fksdemo ports: - name: http protocol: TCP port: 80 targetPort: 8080 ``` Using kubectl, create the service: ``` > kubectl apply -f service.yaml ``` To view your service: ``` > kubectl get svc NAME TYPE CLUSTER-IP EXTERNAL-IP PORT(S) AGE kubernetes ClusterIP fdaa:3:dde8:0:1::3a <none> 443/TCP 32h fksdemo-service ClusterIP fdaa:3:dde8:0:1::3b <none> 80/TCP 11s ``` ## Exposing Services publicly Services can be exposed to the public internet with a Service of type LoadBalancer. ``` apiVersion: v1 kind: Service metadata: name: fksdemo-service-public spec: selector: app: fksdemo ports: - name: http protocol: TCP port: 80 targetPort: 8080 type: LoadBalancer ``` The domain name and IP address to access the Service over the internet can be found using kubectl. In the below output, the values are found under the `EXTERNAL-IP` column. ``` > kubectl get svc NAME TYPE CLUSTER-IP EXTERNAL-IP PORT(S) AGE kubernetes ClusterIP fdaa:3:dde8:0:1::3a <none> 443/TCP 32h fksdemo-service ClusterIP fdaa:3:dde8:0:1::3b <none> 80/TCP 26m fksdemo-service-public LoadBalancer fdaa:3:dde8:0:1::3c fksdemo-service-public.svc.fks-default-vz5dlqz7v4ylrnpq.fly.dev,2a09:8280:1::31:ab8:0,137.66.25.254 80/TCP 8s ``` ## Fly.io connection Handlers Fly.io connection handlers modify your connection before it reaches your application. Learn more about [connection handlers](/docs/networking/services/#connection-handlers). Connection handlers are supported with a custom annotation to a Service object. The annotations have the form: ```yaml "service.fly.io/<exposed port name/number>-handlers": "<handler1,handler2,...handlerN>" ``` The example below adds an HTTP and TLS handler for port 443. ```yaml apiVersion: v1 kind: Service metadata: name: fksdemo-service annotations: "service.fly.io/https-handlers": "http,tls" # can replace https with 443 spec: selector: app: fksdemo ports: - name: http protocol: TCP port: 80 targetPort: 8080 - name: https protocol: TCP port: 443 targetPort: 8080 ``` ### TLS Options [TLS options](https://fly.io/docs/reference/configuration/#services-ports-tls_options) are used to configure the TLS settings of a service with a TLS connection handler. Fly's edge will use these settings to terminate TLS for your application. Refer to the [documentation](https://fly.io/docs/reference/configuration/#services-ports-tls_options) for details. TLS options are set using custom annotations. There are 3 annotations, one for each setting: * `service.fly.io/<exposed port name/number>-tls-alpn` - Sets the ALPN for negotiation with clients. Values must be comma-separated. * `service.fly.io/<exposed port name/number>-tls-versions` - Sets which TLS versions are allowed. Values must be comma-separated. * `service.fly.io/<exposed port name/number>-tls-default-self-signed` - If true, serves a self-signed certificate if none exists. The most common use case for TLS options is to support gRPC. For example: ```yaml apiVersion: v1 kind: Service metadata: name: fksdemo-service annotations: "service.fly.io/https-handlers": "tls" "service.fly.io/https-tls-alpn": "h2" spec: selector: app: fksdemo ports: - name: http protocol: TCP port: 80 targetPort: 8080 - name: https protocol: TCP port: 443 targetPort: 8080 ``` ## Concurrency limits [Concurrency limits](/docs/reference/configuration/#services-concurrency) are used to limit the load on your application. By default, the soft limit is set to 20 and the hard limit is set to 25. Learn more about [concurrency limits](/docs/reference/configuration/#services-concurrency). They can be configured on your Services using custom annotations. There are 3 annotations used to configure the limits: * `service.fly.io/concurrency-kind` - sets the metric used to measure concurrency * `service.fly.io/concurrency-limit-soft` - sets the concurrency soft limit * `service.fly.io/concurrency-limit-hard` - sets the concurrency hard limit Below is an example of setting this in your Service ```yaml apiVersion: v1 kind: Service metadata: name: fksdemo-service annotations: "service.fly.io/concurrency-kind": "connections" "service.fly.io/concurrency-limit-soft": 20 "service.fly.io/concurrency-limit-hard": 25 ``` ## Not supported We currently do not support: * NodePort Services * UDP protocol ## Related topics - [Create an FKS cluster](/docs/kubernetes/clusters/) - [Connect to an FKS cluster](/docs/kubernetes/connect-clusters/) 

[Docs](https://fly.io/docs/)[Fly Kubernetes](https://fly.io/docs/kubernetes)Configure FKS Services
Configure FKS Services
======================

Fly Kubernetes is in closed beta and not recommended for critical production usage. To report issues or provide feedback, email us at [beta@fly.io](mailto:beta@fly.io).

A [Kubernetes Service](https://kubernetes.io/docs/concepts/services-networking/service/) exposes applications running on your cluster. Fly Kubernetes supports ClusterIP and LoadBalancer Services.

You can create a Service with a service configuration file. Here’s an example ClusterIP service:

 Wrap text  Copy to clipboard 

```
apiVersion: v1
kind: Service
metadata:
  name: fksdemo-service
spec:
  selector:
    app: fksdemo
  ports:
    - name: http
      protocol: TCP
      port: 80
      targetPort: 8080
```

Using kubectl, create the service:

 Wrap text  Copy to clipboard 

```
> kubectl apply -f service.yaml
```

To view your service:

 Wrap text  Copy to clipboard 

```
> kubectl get svc
NAME              TYPE        CLUSTER-IP            EXTERNAL-IP   PORT(S)   AGE
kubernetes        ClusterIP   fdaa:3:dde8:0:1::3a   <none>        443/TCP   32h
fksdemo-service   ClusterIP   fdaa:3:dde8:0:1::3b   <none>        80/TCP    11s
```

[](https://fly.io/docs/kubernetes/services/#exposing-services-publicly)Exposing Services publicly
-------------------------------------------------------------------------------------------------

Services can be exposed to the public internet with a Service of type LoadBalancer.

 Wrap text  Copy to clipboard 

```
apiVersion: v1
kind: Service
metadata:
  name: fksdemo-service-public
spec:
  selector:
    app: fksdemo
  ports:
    - name: http
      protocol: TCP
      port: 80
      targetPort: 8080
  type: LoadBalancer
```

The domain name and IP address to access the Service over the internet can be found using kubectl. In the below output, the values are found under the `EXTERNAL-IP` column.

 Wrap text  Copy to clipboard 

```
> kubectl get svc
NAME                     TYPE           CLUSTER-IP            EXTERNAL-IP                                                                                           PORT(S)   AGE
kubernetes               ClusterIP      fdaa:3:dde8:0:1::3a   <none>                                                                                                443/TCP   32h
fksdemo-service          ClusterIP      fdaa:3:dde8:0:1::3b   <none>                                                                                                80/TCP    26m
fksdemo-service-public   LoadBalancer   fdaa:3:dde8:0:1::3c   fksdemo-service-public.svc.fks-default-vz5dlqz7v4ylrnpq.fly.dev,2a09:8280:1::31:ab8:0,137.66.25.254   80/TCP    8s
```

[](https://fly.io/docs/kubernetes/services/#fly-io-connection-handlers)Fly.io connection Handlers
-------------------------------------------------------------------------------------------------

Fly.io connection handlers modify your connection before it reaches your application. Learn more about [connection handlers](https://fly.io/docs/networking/services/#connection-handlers).

Connection handlers are supported with a custom annotation to a Service object. The annotations have the form:

 Wrap text  Copy to clipboard 

```
"service.fly.io/<exposed port name/number>-handlers": "<handler1,handler2,...handlerN>"
```

The example below adds an HTTP and TLS handler for port 443.

 Wrap text  Copy to clipboard 

```
apiVersion: v1
kind: Service
metadata:
  name: fksdemo-service
  annotations:
    "service.fly.io/https-handlers": "http,tls" # can replace https with 443
spec:
  selector:
    app: fksdemo
  ports:
    - name: http
      protocol: TCP
      port: 80
      targetPort: 8080
    - name: https
      protocol: TCP
      port: 443
      targetPort: 8080
```

### [](https://fly.io/docs/kubernetes/services/#tls-options)TLS Options

[TLS options](https://fly.io/docs/reference/configuration/#services-ports-tls_options) are used to configure the TLS settings of a service with a TLS connection handler. Fly’s edge will use these settings to terminate TLS for your application. Refer to the [documentation](https://fly.io/docs/reference/configuration/#services-ports-tls_options) for details.

TLS options are set using custom annotations. There are 3 annotations, one for each setting:

*   `service.fly.io/<exposed port name/number>-tls-alpn` - Sets the ALPN for negotiation with clients. Values must be comma-separated. 
*   `service.fly.io/<exposed port name/number>-tls-versions` - Sets which TLS versions are allowed. Values must be comma-separated. 
*   `service.fly.io/<exposed port name/number>-tls-default-self-signed` - If true, serves a self-signed certificate if none exists. 

The most common use case for TLS options is to support gRPC. For example:

 Wrap text  Copy to clipboard 

```
apiVersion: v1
kind: Service
metadata:
  name: fksdemo-service
  annotations:
    "service.fly.io/https-handlers": "tls"
    "service.fly.io/https-tls-alpn": "h2"
spec:
  selector:
    app: fksdemo
  ports:
    - name: http
      protocol: TCP
      port: 80
      targetPort: 8080
    - name: https
      protocol: TCP
      port: 443
      targetPort: 8080
```

[](https://fly.io/docs/kubernetes/services/#concurrency-limits)Concurrency limits
---------------------------------------------------------------------------------

[Concurrency limits](https://fly.io/docs/reference/configuration/#services-concurrency) are used to limit the load on your application. By default, the soft limit is set to 20 and the hard limit is set to 25. Learn more about [concurrency limits](https://fly.io/docs/reference/configuration/#services-concurrency).

They can be configured on your Services using custom annotations. There are 3 annotations used to configure the limits:

*   `service.fly.io/concurrency-kind` - sets the metric used to measure concurrency 
*   `service.fly.io/concurrency-limit-soft` - sets the concurrency soft limit 
*   `service.fly.io/concurrency-limit-hard` - sets the concurrency hard limit 

Below is an example of setting this in your Service

 Wrap text  Copy to clipboard 

```
apiVersion: v1
kind: Service
metadata:
  name: fksdemo-service
  annotations:
    "service.fly.io/concurrency-kind": "connections"
    "service.fly.io/concurrency-limit-soft": 20 
    "service.fly.io/concurrency-limit-hard": 25
```

[](https://fly.io/docs/kubernetes/services/#not-supported)Not supported
-----------------------------------------------------------------------

We currently do not support:

*   NodePort Services 
*   UDP protocol 

[](https://fly.io/docs/kubernetes/services/#related-topics)Related topics
-------------------------------------------------------------------------

*   [Create an FKS cluster](https://fly.io/docs/kubernetes/clusters/)
*   [Connect to an FKS cluster](https://fly.io/docs/kubernetes/connect-clusters/)

Copy page as markdown or[Open in ChatGPT](https://chatgpt.com/?hints=search&q=Read+https%3A%2F%2Fraw.githubusercontent.com%2Fsuperfly%2Fdocs%2Fmain%2Fkubernetes%2Fservices.html.markerb)

[Report an issue](https://github.com/superfly/docs/issues/new?body=I+found+an+issue+with+this+document.%0A%0ATitle%3A+Configure+FKS+Services%0ALocation%3A+https%3A%2F%2Ffly.io%2Fdocs%2Fkubernetes%2Fservices%2F%0ASource%3A+https%3A%2F%2Fgithub.com%2Fsuperfly%2Fdocs%2Fblob%2Fmain%2Fkubernetes%2Fservices.html.markerb%0A%0A%23%23%23+Describe+the+issue%0A%0A%3C%21--+Describe+the+issue+and+include+the+section+you%27re+referring+to%2C+if+applicable.+Provide+lots+of+detail+about+the+issue+that+you+found.++--%3E%0A%0A%23%23%23+Additional+info%0A%0A%3C%21--+Add+any+other+context+about+the+issue+here.+If+applicable%2C+add+screenshots+to+help+explain+the+issue.+--%3E%0A&title=Issue+with+the+%22Configure+FKS+Services%22+doc) or [edit this page on GitHub](https://github.com/superfly/docs/edit/main/kubernetes/services.html.markerb)
