# Source: https://docs.datadoghq.com/tracing/guide/tutorial-enable-java-admission-controller.md

---
title: >-
  Tutorial - Enabling Tracing for a Java Application with the Admission
  Controller
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > APM > Tracing Guides > Tutorial - Enabling Tracing for a Java
  Application with the Admission Controller
source_url: >-
  https://docs.datadoghq.com/guide/tutorial-enable-java-admission-controller/index.html
---

# Tutorial - Enabling Tracing for a Java Application with the Admission Controller

## Overview{% #overview %}

This tutorial walks you through the steps to enable tracing for Java Application using the Datadog Admission Controller.

For other scenarios, including on a host, in a container, on cloud infrastructure, and on applications written in other languages, see the other [Enabling Tracing tutorials](https://docs.datadoghq.com/tracing/guide/#enabling-tracing-tutorials).

See [Tracing Java Applications](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/java) for general comprehensive tracing setup documentation for Java.

### Prerequisites{% #prerequisites %}

- A Datadog account and [organization API key](https://docs.datadoghq.com/account_management/api-app-keys)
- Git
- Docker
- Curl
- Kubernetes v1.14+

## Install the sample application{% #install-the-sample-application %}

To demonstrate how to instrument your app with the Datadog Admission Controller, this tutorial uses a Java app built with Spring. You can find the code for the app in the [springblog GitHub repository](https://github.com/DataDog/springblog).

To get started, clone the repository:

```shell
git clone https://github.com/DataDog/springblog.git
```

The repository contains a multi-service Java application pre-configured to be run within Docker and Kubernetes. The sample app is a basic Spring app using REST.

## Start and run the sample application{% #start-and-run-the-sample-application %}

1. Switch to to the `/k8s` subdirectory in the springblog repo:

   ```shell
   cd springblog/k8s/
```



1. Deploy the workload with the `depl.yaml` file:

   ```shell
   kubectl apply -f ./depl.yaml
```



1. Verify that it is running with the following command:

   ```shell
   kubectl get pods
```



You should see something like this:

   ```
   NAME                                       READY   STATUS        RESTARTS        AGE
   springback-666db7b6b8-dzv7c                1/1     Terminating   0               2m41s
   springfront-797b78d6db-p5c84               1/1     Terminating   0               2m41s
   ```

The service is started and listens on port 8080. It exposes an `/upstream` endpoint.

1. Check that communication takes place by running the following curl command:

   ```shell
   curl localhost:8080/upstream
   Quote{type='success', values=Values{id=6, quote='Alea jacta est'}}
```



1. To stop the application, run this command from the `springblog/k8s` directory so you can enable tracing on it:

   ```shell
   kubectl delete -f ./depl-with-lib-inj.yaml
```

## Instrument your app with Datadog Admission Controller{% #instrument-your-app-with-datadog-admission-controller %}

After you have your application working, instrument it using the Datadog Admission Controller. In containerized environments, the process is generally:

1. Install the [Datadog Cluster Agent](https://docs.datadoghq.com/containers/cluster_agent).
1. Add [Unified Service Tags](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging) in pod definition.
1. [Annotate](https://docs.datadoghq.com/tracing/trace_collection/library_injection_local) your pod for library injection.
1. [Label](https://docs.datadoghq.com/tracing/trace_collection/library_injection_local) your pod to instruct the Datadog Admission controller to mutate the pod.

There's no need to add the tracing library because it's automatically injected. You don't need to redeploy your app yet. This section of the tutorial steps you through the process of adding Datadog variables and deploying a new image or version of your app.

1. From the `k8s` subdirectory, use the following command to install the Datadog Cluster Agent, specifying the `values-with-lib-inj.yaml` config file and your [Datadog API key](https://docs.datadoghq.com/account_management/api-app-keys/):

   ```shell
   helm install datadog-agent -f values-with-lib-inj.yaml --set datadog.site='datadoghq.com' --set datadog.apiKey=$DD_API_KEY datadog/datadog
```


Important alert (level: danger): For more detailed information, read Installing the Datadog Agent on Kubernetes with Helm
1. You can check the Datadog Cluster Agent is running with the following command:

   ```shell
   kubectl get pods
```



You should see something like this:

   ```
   NAME                                                READY   STATUS    RESTARTS  AGE
   datadog-agent-4s8rb                                 3/3     Running   0	        30s
   datadog-agent-cluster-agent-5666cffc44-d8qxk        1/1     Running   0         30s
   datadog-agent-kube-state-metrics-86f46b8484-mlqp7   1/1     Running   0         30s
   ```

1. Add [Unified Service Tags](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging) to the pod by adding the following block to the [`depl.yaml` file](https://github.com/DataDog/springblog/blob/main/k8s/depl.yaml):

   ```yaml
   labels:
     tags.datadoghq.com/env: "dev"
     tags.datadoghq.com/service: "springfront"
     tags.datadoghq.com/version: "12"
```



1. Configure the Datadog Admission Controller to inject a Java tracing library to the app container by adding the following annotation to the pod:

   ```yaml
   annotations:
     admission.datadoghq.com/java-lib.version: "<CONTAINER IMAGE TAG>"
```



Replace `<CONTAINER IMAGE TAG>` with the desired library version. Available versions are listed in the [Java source repository](https://github.com/DataDog/dd-trace-java/releases)
Important alert (level: danger): Exercise caution when using the `latest` tag, as major library releases may introduce breaking changes.
The final pod definition should look like the excerpt below. See also the full [YAML file](https://github.com/DataDog/springblog/blob/main/k8s/depl-with-lib-inj.yaml) in the sample repo. The instructions you added to instrument the app are highlighted:

   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
   name: springfront
   labels:
       tags.datadoghq.com/env: "dev"
       tags.datadoghq.com/service: "springfront"
       tags.datadoghq.com/version: "12"
   spec:
   replicas: 1
   selector:
       matchLabels:
       name: springfront
   minReadySeconds: 15
   strategy:
       type: RollingUpdate
       rollingUpdate:
       maxUnavailable: 1
       maxSurge: 1
   template:
       metadata:
       labels:
           name: springfront
           tags.datadoghq.com/env: "dev"
           tags.datadoghq.com/service: "springfront"
           tags.datadoghq.com/version: "12"
       annotations:
           admission.datadoghq.com/java-lib.version: "<CONTAINER IMAGE TAG>"
```

1. Run the sample app with the following command:

   ```shell
   kubectl apply -f depl-with-lib-inj.yaml
```



1. Run the following command to show that the app and Agent are running:

   ```shell
   kubectl get pods
```



You should see something like this:

   ```
   NAME                                                READY   STATUS    RESTARTS   AGE
   datadog-agent-4s8rb                                 3/3     Running   0          28m
   datadog-agent-cluster-agent-5666cffc44-d8qxk        1/1     Running   0          28m
   datadog-agent-kube-state-metrics-86f46b8484-mlqp7   1/1     Running   0          28m
   springback-666db7b6b8-sb4tp                         1/1     Running   0          27m
   springfront-797b78d6db-mppbg                        1/1     Running   0          27m
   ```

1. Run the following command to see details of the pod:

   ```shell
   kubectl describe pod springfront
```



You should see something like this:

   ```
   Events:
   Type    Reason     Age   From               Message
   ----    ------     ----  ----               -------
   Normal  Scheduled  32s   default-scheduler  Successfully assigned default/springfront-797b78d6db-jqjdl to docker-desktop
   Normal  Pulling    31s   kubelet            Pulling image "gcr.io/datadoghq/dd-lib-java-init:latest"
   Normal  Pulled     25s   kubelet            Successfully pulled image "gcr.io/datadoghq/dd-lib-java-init:latest" in 5.656167878s
   Normal  Created    25s   kubelet            Created container datadog-lib-java-init
   Normal  Started    25s   kubelet            Started container datadog-lib-java-init
   Normal  Pulling    25s   kubelet            Pulling image "pejese/springfront:v2"
   Normal  Pulled     2s    kubelet            Successfully pulled image "pejese/springfront:v2" in 22.158699094s
   Normal  Created    2s    kubelet            Created container springfront
   Normal  Started    2s    kubelet            Started container springfront
   ```

As you can see, an init-container is added to your pod. This container includes the Datadog Java tracing libraries to a volume mount. Also `JAVA_TOOL_OPTIONS` is modified to include `javaagent`. And Datadog-specific environment variables are added to the container:

   ```gdscript3
   Environment:
   DD_ENV:              dev
   DD_VERSION:          12
   DD_SERVICE:          springfront
   DD_ENTITY_ID:         (v1:metadata.uid)
   DD_TRACE_AGENT_URL:  unix:///var/run/datadog/apm.socket
   URL:                 http://springback:8088
   JAVA_TOOL_OPTIONS:    -javaagent:/datadog-lib/dd-java-agent.jar
   Mounts:
   /datadog-lib from datadog-auto-instrumentation (rw)
   /var/run/datadog from datadog (rw)
   /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-qvmtk (ro)
   ```

1. Verify that the Datadog tracing library is injected into the pod by checking the pod logs. For example:

   ```shell
   kubectl logs -f springfront-797b78d6db-jqjdl
```



You should see something like this:

   ```
   Defaulted container "springfront" out of: springfront, datadog-lib-java-init (init)
   Picked up JAVA_TOOL_OPTIONS:  -javaagent:/datadog-lib/dd-java-agent.jar
   ```

## View APM traces in Datadog{% #view-apm-traces-in-datadog %}

1. Run the following command:

   ```shell
   curl localhost:8080/upstream
```



1. Open the Datadog UI and see the two services reporting under the [Software Catalog](https://app.datadoghq.com/services):

   {% image
      source="?auto=format"
      alt="Springback and springfront services in the Software Catalog." /%}



1. Explore Traces and see the associated Service Map:

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-admission-controller-traces.7755354fe1e4a0abe5d0f3850bcc4278.png?auto=format"
      alt="The flame graph that represents the service." /%}

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-admission-controller-service-map.d11c110295436fcf04c9d79aaa66d391.png?auto=format"
      alt="The service map that represents the service." /%}

## Clean up the environment{% #clean-up-the-environment %}

Clean up your environment with the following command:

```shell
kubectl delete -f depl-with-lib-inj.yaml
```

Library injection with the Admission Controller simplifies service instrumentation, enabling you to view APM traces without changing or rebuilding your application. To learn more, read [Datadog Library injection](https://docs.datadoghq.com/tracing/trace_collection/admission_controller).

## Troubleshooting{% #troubleshooting %}

If you're not receiving traces as expected, set up debug mode for the Java tracer. To learn more, read [Enable debug mode](https://docs.datadoghq.com/tracing/troubleshooting/tracer_debug_logs/#enable-debug-mode).

## Further reading{% #further-reading %}

- [Additional tracing library configuration options](https://docs.datadoghq.com/tracing/trace_collection/library_config/java/)
- [Detailed tracing library setup instructions](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/java/)
- [Supported Java frameworks for automatic instrumentation](https://docs.datadoghq.com/tracing/trace_collection/compatibility/java/)
- [Manually configuring traces and spans](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/java/)
- [Tracing library open source code repository](https://github.com/DataDog/dd-trace-java)
- [Troubleshooting the Datadog Cluster Agent](https://docs.datadoghq.com/containers/cluster_agent/troubleshooting/)
- [Use library injection to auto-instrument and trace your Kubernetes applications with Datadog APM](https://www.datadoghq.com/blog/auto-instrument-kubernetes-tracing-with-datadog/)
