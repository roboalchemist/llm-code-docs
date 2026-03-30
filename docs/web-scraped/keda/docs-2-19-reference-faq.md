# Source: https://keda.sh/docs/2.19/reference/faq/

Title: KEDA | FAQ

URL Source: https://keda.sh/docs/2.19/reference/faq/

Markdown Content:
FAQ Latest

General [](https://keda.sh/docs/2.19/reference/faq/#general)
------------------------------------------------------------

KEDA stands for Kubernetes Event-driven Autoscaler. It is built to be able to activate a Kubernetes deployment (i.e. no pods to a single pod) and subsequently to more pods based on events from various event sources.

KEDA is designed, tested and is supported to be run on any Kubernetes cluster that runs Kubernetes v1.17.0 or above.

It uses a CRD (custom resource definition) and the Kubernetes metric server so you will have to use a Kubernetes version which supports these.

> 💡 Kubernetes v1.16 is supported with KEDA v2.4.0 or below

Yes! KEDA v2.0 is suited for production workloads, but we still support v1.5 if you are running that as well..

Best Practices [](https://keda.sh/docs/2.19/reference/faq/#best-practices)
--------------------------------------------------------------------------

KEDA allows you to use multiple triggers as part of the same `ScaledObject` or `ScaledJob`.

By doing this, your autoscaling becomes better:

*   All your autoscaling rules are in one place
*   You will not have multiple `ScaledObject`’s or `ScaledJob`’s interfering with each other

KEDA will start scaling as soon as when one of the triggers meets the criteria. Horizontal Pod Autoscaler (HPA) will calculate metrics for every scaler and use the highest desired replica count to scale the workload to.

We recommend not to combine using KEDA’s `ScaledObject` with a Horizontal Pod Autoscaler (HPA) to scale the same workload.

They will compete with each other resulting given KEDA uses Horizontal Pod Autoscaler (HPA) under the hood and will result in odd scaling behavior.

If you are using a Horizontal Pod Autoscaler (HPA) to scale on CPU and/or memory, we recommend using the [CPU scaler](https://keda.sh/docs/latest/scalers/cpu/)&[Memory scaler](https://keda.sh/docs/latest/scalers/memory/) scalers instead.

Features [](https://keda.sh/docs/2.19/reference/faq/#features)
--------------------------------------------------------------

KEDA will scale a container using metrics from a scaler, but unfortunately there is no scaler today for HTTP workloads out-of-the-box.

We do, however, provide some alternative approaches:

*   Use our HTTP add-on scaler which is currently in experimental stage ([GitHub](https://github.com/kedacore/http-add-on))
*   Use [Prometheus scaler](https://keda.sh/docs/latest/scalers/prometheus/) to create scale rule based on metrics around HTTP events 
    *   Read [Anirudh Garg’s blog post](https://dev.to/anirudhgarg_99/scale-up-and-down-a-http-triggered-function-app-in-kubernetes-using-keda-4m42) to learn more.

Polling interval really only impacts the time-to-activation (scaling from 0 to 1) but once scaled to one it’s really up to the HPA (horizontal pod autoscaler) which polls KEDA.

As default, KEDA v2.10 or above sets `readOnlyRootFilesystem=true` as default without any other manual intervention.

If you are running KEDA v2.9 or below, you can’t run KEDA with `readOnlyRootFilesystem=true` as default because Metrics adapter generates self-signed certificates during deployment and stores them on the root file system. To overcome this, you can create a secret/configmap with a valid CA, cert and key and then mount it to the Metrics Deployment. To use your certificate, you need to reference it in the container `args` section, e.g.:

```
args:
  - '--client-ca-file=/cabundle/service-ca.crt'
  - '--tls-cert-file=/certs/tls.crt'
  - '--tls-private-key-file=/certs/tls.key'
```

It is also possible to run KEDA with `readOnlyRootFilesystem=true` by creating an emptyDir volume and mounting it to the path where, by default, metrics server writes its generated cert. The corresponding helm command is:

```
helm install keda kedacore/keda --namespace keda --set 'volumes.metricsApiServer.extraVolumes[0].name=keda-volume' --set 'volumes.metricsApiServer.extraVolumeMounts[0].name=keda-volume' --set 'volumes.metricsApiServer.extraVolumeMounts[0].mountPath=/apiserver.local.config/certificates/' --set 'securityContext.metricServer.readOnlyRootFilesystem=true'
```

By default, Keda listens on TLS v1.1 and TLSv1.2, with the default Golang ciphersuites. In some environments, these ciphers may be considered less secure, for example CBC ciphers.

As an alternative, you can configure the minimum TLS version to be v1.3 to increase security. Since all modern clients support this version, there should be no impact in most scenarios.

You can set this with args - e.g.:

```
args:
  - '--tls-min-version=VersionTLS13'
```

Kubernetes [](https://keda.sh/docs/2.19/reference/faq/#kubernetes)
------------------------------------------------------------------

The target metric value is used by the Horizontal Pod Autoscaler (HPA) to make scaling decisions.

The current target value on the Horizontal Pod Autoscaler (HPA) often does not match with the metrics on the system you are scaling on. This is because of how the Horizontal Pod Autoscaler’s (HPA) [scaling algorithm](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#algorithm-details) works.

By default, KEDA scalers use average metrics (the `AverageValue` metric type). This means that the HPA will use the average value of the metric between the total amount of pods. As of KEDA v2.7, ScaledObjects also support the `Value` metric type. You can learn more about it [here](https://keda.sh/docs/latest/concepts/scaling-deployments/#triggers).

Kubernetes allows you to autoscale based on custom & external metrics which are fundamentally different:

*   **Custom metrics** are metrics that come from applications solely running on the Kubernetes cluster (Prometheus)
*   **External metrics** are metrics that represent the state of an application/service that is running outside of the Kubernetes cluster (AWS, Azure, GCP, Datadog, etc.)

Because KEDA primarily serves metrics for metric sources outside of the Kubernetes cluster, it uses external metrics and not custom metrics.

This is why KEDA registers the `v1beta1.external.metrics.k8s.io` namespace in the API service. However, this is just an implementation detail as both offer the same functionality.

Read [about the different metric APIs](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#support-for-metrics-apis) or [this article](https://cloud.google.com/kubernetes-engine/docs/concepts/custom-and-external-metrics) by Google Cloud to learn more.

Unfortunately, you cannot do that.

Kubernetes currently only supports one metric server serving `external.metrics.k8s.io` metrics per cluster. This is because only one API Service can be registered to handle external metrics.

If you want to know what external metric server is currently registered, you can use the following command:

```
~  kubectl  get APIService/v1beta1.external.metrics.k8s.io
NAME                              SERVICE                                       AVAILABLE   AGE
v1beta1.external.metrics.k8s.io   keda-system/keda-operator-metrics-apiserver   True        457d
```

Once a new metric server is installed, it will overwrite the existing API Server registration and take over the `v1beta1.external.metrics.k8s.io` namespace. This will cause the previously installed metric server to be ignored.

There is an [open proposal](https://github.com/kubernetes-sigs/custom-metrics-apiserver/issues/70) to allow multiple metric servers in the same cluster, but it’s not implemented yet.

Unfortunately, you cannot do that.

This is a limitation that is because Kubernetes does not allow you to run multiple metric servers in the same cluster that serve external metrics.

Also, KEDA does not allow you to share a single metric server across multiple operator installations.

Learn more in the “Can I run multiple metric servers serving external metrics in the same cluster?” FAQ entry.

There are several ways to get involved.

*   Pick up an issue to work on. A good place to start might be issues which are marked as [Good First Issue](https://github.com/kedacore/keda/labels/good%20first%20issue) or [Help Wanted](https://github.com/kedacore/keda/labels/help%20wanted)
*   We are always looking to add more scalers.
*   We are always looking for more samples, documentation, etc.
*   Please join us in our [weekly standup](https://github.com/kedacore/keda#community).

All scalers have their code [here](https://github.com/kedacore/keda/tree/main/pkg/scalers).

Website [](https://keda.sh/docs/2.19/reference/faq/#website)
------------------------------------------------------------

Yes. The search actually supports wildcard search. We’ve made our search to automatically perform wildcard filtering on the fly so you don’t have to append special symbols within your search query.

Integrations [](https://keda.sh/docs/2.19/reference/faq/#integrations)
----------------------------------------------------------------------

### Microsoft Azure

No, KEDA only takes a dependency on standard Kubernetes constructs and can run on any Kubernetes cluster whether in OpenShift, AKS, GKE, EKS or your own infrastructure.

No, KEDA can scale up/down any container that you specify in your deployment. There has been work done in the Azure Functions tooling to make it easy to scale an Azure Function container.

There are a few reasons for this:

*   Run functions on-premises (potentially in something like an ‘intelligent edge’ architecture)
*   Run functions alongside other Kubernetes apps (maybe in a restricted network, app mesh, custom environment, etc.)
*   Run functions outside of Azure (no vendor lock-in)
*   Specific need for more control (GPU enabled compute clusters, policies, etc.)
