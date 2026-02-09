# Source: https://docs.datadoghq.com/tracing/guide/tutorial-enable-java-gke.md

---
title: Tutorial - Enabling Tracing for a Java Application on Google Kubernetes Engine
description: >-
  Step-by-step tutorial to enable distributed tracing for a Java application
  deployed on Google Kubernetes Engine with Datadog APM.
breadcrumbs: >-
  Docs > APM > Tracing Guides > Tutorial - Enabling Tracing for a Java
  Application on Google Kubernetes Engine
---

# Tutorial - Enabling Tracing for a Java Application on Google Kubernetes Engine

## Overview{% #overview %}

This tutorial walks you through the steps for enabling tracing on a sample Java application installed in a cluster on Google Kubernetes Engine (GKE). In this scenario, the Datadog Agent is also installed in the cluster.

For other scenarios, including on a host, in a container, on other cloud infrastructure, and on applications written in other languages, see the other [Enabling Tracing tutorials](https://docs.datadoghq.com/tracing/guide/#enabling-tracing-tutorials).

See [Tracing Java Applications](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/java/) for general comprehensive tracing setup documentation for Java.

### Prerequisites{% #prerequisites %}

- A Datadog account and [organization API key](https://docs.datadoghq.com/account_management/api-app-keys/)
- Git
- Kubectl
- GCloud - Set the `USE_GKE_GCLOUD_AUTH_PLUGIN` environment variable and configure additional properties for your GCloud project by running these commands:
  ```sh
  export USE_GKE_GCLOUD_AUTH_PLUGIN=True
  gcloud config set project <PROJECT_NAME>
  gcloud config set compute/zone <COMPUTE_ZONE>
  gcloud config set compute/region <COMPUTE_REGION>
```
- Helm - Install by running these commands:
  ```sh
  curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
  chmod 700 get_helm.sh
  ./get_helm.sh
```
Configure Helm by running these commands:
  ```sh
  helm repo add datadog-crds https://helm.datadoghq.com
  helm repo add kube-state-metrics https://prometheus-community.github.io/helm-charts
  helm repo add datadog https://helm.datadoghq.com
  helm repo update
```

## Install the sample Kubernetes Java application{% #install-the-sample-kubernetes-java-application %}

The code sample for this tutorial is on GitHub, at [github.com/DataDog/apm-tutorial-java-host](https://github.com/DataDog/apm-tutorial-java-host). To get started, clone the repository:

```sh
git clone https://github.com/DataDog/apm-tutorial-java-host.git
```

The repository contains a multi-service Java application pre-configured to run inside a Kubernetes cluster. The sample app is a basic notes app with a REST API to add and change data. The `docker-compose` YAML files to make the containers for the Kubernetes pods are located in the `docker` directory. This tutorial uses the `service-docker-compose-k8s.yaml` file, which builds containers for the application.

In each of the `notes` and `calendar` directories, there are two sets of Dockerfiles for building the applications, either with Maven or with Gradle. This tutorial uses the Maven build, but if you are more familiar with Gradle, you can use it instead with the corresponding changes to build commands.

Kubernetes configuration files for the `notes` app, the `calendar` app, and the Datadog Agent are in the `kubernetes` directory.

The process of getting the sample application involves building the images from the `docker` folder, uploading them to a registry, and creating kubernetes resources from the `kubernetes` folder.

### Starting the cluster{% #starting-the-cluster %}

1. If you don't already have a GKE cluster that you want to re-use, create one by running the following command, replacing the `<VARIABLES>` with the values you want to use:

   ```sh
   gcloud container clusters create <CLUSTER_NAME> --num-nodes=1 --network=<NETWORK> --subnetwork=<SUBNETWORK>
```

**Note**: For a list of available networks and subnetworks, use the following command:

   ```sh
   gcloud compute networks subnets list
```



1. Connect to the cluster by running:

   ```sh
   gcloud container clusters get-credentials <CLUSTER_NAME>
   gcloud config set container/cluster <CLUSTER_NAME>
```

1. To facilitate communication with the applications that will be deployed, [edit the network's firewall rules](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#add_firewall_rules) to ensure that the GKE cluster allows TCP traffic on ports `30080` and `30090`.

### Build and upload the application image{% #build-and-upload-the-application-image %}

If you're not familiar with Google Container Registry (GCR), it might be helpful to read [Quickstart for Container Registry](https://cloud.google.com/container-registry/docs/quickstart).

In the sample project's `/docker` directory, run the following commands:

1. Authenticate with GCR by running:

   ```sh
   gcloud auth configure-docker
```



1. Build a Docker image for the sample app, adjusting the platform setting to match yours:

   ```sh
   DOCKER_DEFAULT_PLATFORM=linux/amd64 docker-compose -f service-docker-compose-k8s.yaml build notes
```



1. Tag the container with the GCR destination:

   ```sh
   docker tag docker-notes:latest gcr.io/<PROJECT_ID>/notes-tutorial:notes
```



1. Upload the container to the GCR registry:

   ```sh
   docker push gcr.io/<PROJECT_ID>/notes-tutorial:notes
```

Your application is containerized and available for GKE clusters to pull.

### Configure the application locally and deploy{% #configure-the-application-locally-and-deploy %}

1. Open `kubernetes/notes-app.yaml` and update the `image` entry with the URL for the GCR image, where you pushed the container in step 4 above:

   ```yaml
       spec:
         containers:
           - name: notes-app
             image: gcr.io/<PROJECT_ID>/notes-tutorial:notes
             imagePullPolicy: Always
```



1. From the `/kubernetes` directory, run the following command to deploy the `notes` app:

   ```sh
   kubectl create -f notes-app.yaml
```



1. To exercise the app, you need to know its external IP address to call its REST API. First, find the `notes-app-deploy` pod in the list output by the following command, and note its node:

   ```sh
   kubectl get pods -o wide
```

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-java-gke-pods.d8b9e3b1496129cb5af64dd62a8a4fb1.png?auto=format"
      alt="Output of the kubectl command showing the notes-app-deploy pod and its associated node name" /%}

Then find that node name in the output from the following command, and note the external IP value:

   ```sh
   kubectl get nodes -o wide
```

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-java-gke-external-ip.723d834c2a84fbc6f05bc2ec6e352da9.png?auto=format"
      alt="Output of the kubectl command showing the external IP value for the node" /%}

In the examples shown, the `notes-app` is running on node `gke-java-tracing-gke-default-pool-ccbd5526-dd3d`, which has an external IP of `35.196.6.199`.

1. Open up another terminal and send API requests to exercise the app. The notes application is a REST API that stores data in an in-memory H2 database running on the same container. Send it a few commands:

{% dl %}

{% dt %}
`curl '<EXTERNAL_IP>:30080/notes'`
{% /dt %}

{% dd %}
`[]`
{% /dd %}

{% dt %}
`curl -X POST '<EXTERNAL_IP>:30080/notes?desc=hello'`
{% /dt %}

{% dd %}
`{"id":1,"description":"hello"}`
{% /dd %}

{% dt %}
`curl '<EXTERNAL_IP>:30080/notes?id=1'`
{% /dt %}

{% dd %}
`{"id":1,"description":"hello"}`
{% /dd %}

{% dt %}
`curl '<EXTERNAL_IP>:30080/notes'`
{% /dt %}

{% dd %}
`[{"id":1,"description":"hello"}]`
{% /dd %}

{% /dl %}
After you've seen the application running, stop it so that you can enable tracing on it:
```sh
kubectl delete -f notes-app.yaml
```

## Enable tracing{% #enable-tracing %}

Now that you have a working Java application, configure it to enable tracing.

1. Add the Java tracing package to your project. Because the Agent runs in a GKE cluster, ensure that the Dockerfiles are configured properly, and there is no need to install anything. Open the `notes/dockerfile.notes.maven` file and uncomment the line that downloads `dd-java-agent`:

   ```
   RUN curl -Lo dd-java-agent.jar 'https://dtdg.co/latest-java-tracer'
   ```

1. Within the same `notes/dockerfile.notes.maven` file, comment out the `ENTRYPOINT` line for running without tracing. Then uncomment the `ENTRYPOINT` line, which runs the application with tracing enabled:

   ```
   ENTRYPOINT ["java" , "-javaagent:../dd-java-agent.jar", "-Ddd.trace.sample.rate=1", "-jar" , "target/notes-0.0.1-SNAPSHOT.jar"]
   ```

This automatically instruments the application with Datadog services.
Important alert (level: danger): The flags on these sample commands, particularly the sample rate, are not necessarily appropriate for environments outside this tutorial. For information about what to use in your real environment, read Tracing configuration.
1. [Universal Service Tags](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/) identify traced services across different versions and deployment environments so that they can be correlated within Datadog, and so you can use them to search and filter. The three environment variables used for Unified Service Tagging are `DD_SERVICE`, `DD_ENV`, and `DD_VERSION`. For applications deployed with Kubernetes, these environment variables can be added within the deployment YAML file, specifically for the deployment object, pod spec, and pod container template.

For this tutorial, the `kubernetes/notes-app.yaml` file already has these environment variables defined for the notes application for the deployment object, the pod spec, and the pod container template, for example:

   ```yaml
   ...
   spec:
     replicas: 1
     selector:
       matchLabels:
         name: notes-app-pod
         app: java-tutorial-app
     template:
       metadata:
         name: notes-app-pod
         labels:
           name: notes-app-pod
           app: java-tutorial-app
           tags.datadoghq.com/env: "dev"
           tags.datadoghq.com/service: "notes"
           tags.datadoghq.com/version: "0.0.1"
      ...
   ```

### Rebuild and upload the application image{% #rebuild-and-upload-the-application-image %}

Rebuild the image with tracing enabled using the same steps as before in the `docker` directory:

```sh
gcloud auth configure-docker
DOCKER_DEFAULT_PLATFORM=linux/amd64 docker-compose -f service-docker-compose-k8s.yaml build notes
docker tag docker-notes:latest gcr.io/<PROJECT_ID>/notes-tutorial:notes
docker push gcr.io/<PROJECT_ID>/notes-tutorial:notes
```



Your application with tracing enabled is containerized and available for GKE clusters to pull.

## Install and run the Agent using Helm{% #install-and-run-the-agent-using-helm %}

Next, deploy the Agent to GKE to collect the trace data from your instrumented application:

1. Open `kubernetes/datadog-values.yaml` to see the minimum required configuration for the Agent and APM on GKE. This configuration file is used by the command you run next.

1. From the `/kubernetes` directory, run the following command, inserting your API key and cluster name:

   ```sh
   helm upgrade -f datadog-values.yaml --install --debug latest --set datadog.apiKey=<DD_API_KEY> --set datadog.clusterName=<CLUSTER_NAME> --set datadog.site=datadoghq.com datadog/datadog
```



For more secure deployments that do not expose the API Key, read [this guide on using secrets](https://github.com/DataDog/helm-charts/blob/main/charts/datadog/README.md#create-and-provide-a-secret-that-contains-your-datadog-api-and-app-keys). Also, if you use a [Datadog site](https://docs.datadoghq.com/getting_started/site/) other than `us1`, replace `datadoghq.com` with your site.

## Launch the app to see automatic tracing{% #launch-the-app-to-see-automatic-tracing %}

Using the same steps as before, deploy the `notes` app with `kubectl create -f notes-app.yaml` and find the external IP address for the node it runs on.

Run some curl commands to exercise the app:

{% dl %}

{% dt %}
`curl '<EXTERNAL_IP>:30080/notes'`
{% /dt %}

{% dd %}
`[]`
{% /dd %}

{% dt %}
`curl -X POST '<EXTERNAL_IP>:30080/notes?desc=hello'`
{% /dt %}

{% dd %}
`{"id":1,"description":"hello"}`
{% /dd %}

{% dt %}
`curl '<EXTERNAL_IP>:30080/notes?id=1'`
{% /dt %}

{% dd %}
`{"id":1,"description":"hello"}`
{% /dd %}

{% dt %}
`curl '<EXTERNAL_IP>:30080/notes'`
{% /dt %}

{% dd %}
`[{"id":1,"description":"hello"}]`
{% /dd %}

{% /dl %}

Wait a few moments, and go to [**APM > Traces**](https://app.datadoghq.com/apm/traces) in Datadog, where you can see a list of traces corresponding to your API calls:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-java-container-traces2.598507141baa139ec3a2f5fc5b0157b0.png?auto=format"
   alt="Traces from the sample app in APM Trace Explorer" /%}

The `h2` is the embedded in-memory database for this tutorial, and `notes` is the Spring Boot application. The traces list shows all the spans, when they started, what resource was tracked with the span, and how long it took.

If you don't see traces after several minutes, clear any filter in the Traces Search field (sometimes it filters on an environment variable such as `ENV` that you aren't using).

### Examine a trace{% #examine-a-trace %}

On the Traces page, click on a `POST /notes` trace to see a flame graph that shows how long each span took and what other spans occurred before a span completed. The bar at the top of the graph is the span you selected on the previous screen (in this case, the initial entry point into the notes application).

The width of a bar indicates how long it took to complete. A bar at a lower depth represents a span that completes during the lifetime of a bar at a higher depth.

The flame graph for a `POST` trace looks something like this:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-java-container-post-flame.ae5793d5bdb1aae29a05ca4e18354109.png?auto=format"
   alt="A flame graph for a POST trace." /%}

A `GET /notes` trace looks something like this:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-java-container-get-flame.efcf077c819998237efdf7ca3cc99912.png?auto=format"
   alt="A flame graph for a GET trace." /%}

### Tracing configuration{% #tracing-configuration %}

The Java tracing library uses Java's built-in agent and monitoring support. The flag `-javaagent:../dd-java-agent.jar` in the Dockerfile tells the JVM where to find the Java tracing library so it can run as a Java Agent. Learn more about Java Agents at [https://www.baeldung.com/java-instrumentation](https://www.baeldung.com/java-instrumentation).

The `dd.trace.sample.rate` flag sets the sample rate for this application. The ENTRYPOINT command in the Dockerfile sets its value to `1`, which means that 100% of all requests to the `notes` service are sent to the Datadog backend for analysis and display. For a low-volume test application, this is fine. Do not do this in production or in any high-volume environment, because this results in a very large volume of data. Instead, sample some of your requests. Pick a value between 0 and 1. For example, `-Ddd.trace.sample.rate=0.1` sends traces for 10% of your requests to Datadog. Read more about [tracing configuration settings](https://docs.datadoghq.com/tracing/trace_collection/library_config/java/) and [sampling mechanisms](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/?tab=java).

Notice that the sampling rate flag in the command appears *before* the `-jar` flag. That's because this is a parameter for the Java Virtual Machine, not your application. Make sure that when you add the Java Agent to your application, you specify the flag in the right location.

## Add manual instrumentation to the Java application{% #add-manual-instrumentation-to-the-java-application %}

Automatic instrumentation is convenient, but sometimes you want more fine-grained spans. Datadog's Java DD Trace API allows you to specify spans within your code using annotations or code.

The following steps walk you through modifying the build scripts to download the Java tracing library and adding some annotations to the code to trace into some sample methods.

1. Delete the current application deployments:

   ```sh
   kubectl delete -f notes-app.yaml
```



1. Open `/notes/src/main/java/com/datadog/example/notes/NotesHelper.java`. This example already contains commented-out code that demonstrates the different ways to set up custom tracing on the code.

1. Uncomment the lines that import libraries to support manual tracing:

   ```java
   import datadog.trace.api.Trace;
   import datadog.trace.api.DDTags;
   import io.opentracing.Scope;
   import io.opentracing.Span;
   import io.opentracing.Tracer;
   import io.opentracing.tag.Tags;
   import io.opentracing.util.GlobalTracer;
   import java.io.PrintWriter;
   import java.io.StringWriter
   ```

1. Uncomment the lines that manually trace the two public processes. These demonstrate the use of `@Trace` annotations to specify aspects such as `operationName` and `resourceName` in a trace:

   ```java
   @Trace(operationName = "traceMethod1", resourceName = "NotesHelper.doLongRunningProcess")
   // ...
   @Trace(operationName = "traceMethod2", resourceName = "NotesHelper.anotherProcess")
   ```

1. You can also create a separate span for a specific code block in the application. Within the span, add service and resource name tags and error handling tags. These tags result in a flame graph showing the span and metrics in Datadog visualizations. Uncomment the lines that manually trace the private method:

   ```java
           Tracer tracer = GlobalTracer.get();
           // Tags can be set when creating the span
           Span span = tracer.buildSpan("manualSpan1")
               .withTag(DDTags.SERVICE_NAME, "NotesHelper")
               .withTag(DDTags.RESOURCE_NAME, "privateMethod1")
               .start();
           try (Scope scope = tracer.activateSpan(span)) {
               // Tags can also be set after creation
               span.setTag("postCreationTag", 1);
               Thread.sleep(30);
               Log.info("Hello from the custom privateMethod1");
   ```

And also the lines that set tags on errors:

   ```java
        } catch (Exception e) {
            // Set error on span
            span.setTag(Tags.ERROR, true);
            span.setTag(DDTags.ERROR_MSG, e.getMessage());
            span.setTag(DDTags.ERROR_TYPE, e.getClass().getName());
   
            final StringWriter errorString = new StringWriter();
            e.printStackTrace(new PrintWriter(errorString));
            span.setTag(DDTags.ERROR_STACK, errorString.toString());
            Log.info(errorString.toString());
        } finally {
            span.finish();
        }
   ```

1. Update your Maven build by opening `notes/pom.xml` and uncommenting the lines configuring dependencies for manual tracing. The `dd-trace-api` library is used for the `@Trace` annotations, and `opentracing-util` and `opentracing-api` are used for manual span creation.

1. Rebuild the application and upload it to GCR following the same steps as before, running these commands in the `docker` directory:

   ```sh
   gcloud auth configure-docker
   DOCKER_DEFAULT_PLATFORM=linux/amd64 docker-compose -f service-docker-compose-k8s.yaml build notes
   docker tag docker-notes:latest  gcr.io/<PROJECT_NAME>/notes-tutorial:notes
   docker push gcr.io/<PROJECT_NAME>/notes-tutorial:notes
```

1. Using the same steps as before, deploy the `notes` app with `kubectl create -f notes-app.yaml` and find the external IP address for the node it runs on.

1. Resend some HTTP requests, specifically some `GET` requests.

1. On the Trace Explorer, click on one of the new `GET` requests, and see a flame graph like this:

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-java-container-custom-flame.3faa56c8907d0876ffdf0f8ff95cf532.png?auto=format"
      alt="A flame graph for a GET trace with custom instrumentation." /%}

Note the higher level of detail in the stack trace now that the `getAll` function has custom tracing.

The `privateMethod` around which you created a manual span now shows up as a separate block from the other calls and is highlighted by a different color. The other methods where you used the `@Trace` annotation show under the same service and color as the `GET` request, which is the `notes` application. Custom instrumentation is valuable when there are key parts of the code that need to be highlighted and monitored.

For more information, read [Custom Instrumentation](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/java/).

## Add a second application to see distributed traces{% #add-a-second-application-to-see-distributed-traces %}

Tracing a single application is a great start, but the real value in tracing is seeing how requests flow through your services. This is called *distributed tracing*.

The sample project includes a second application called `calendar` that returns a random date whenever it is invoked. The `POST` endpoint in the Notes application has a second query parameter named `add_date`. When it is set to `y`, Notes calls the calendar application to get a date to add to the note.

1. Configure the `calendar` app for tracing by adding `dd-java-agent` to the startup command in the Dockerfile, like you previously did for the notes app. Open `calendar/dockerfile.calendar.maven` and see that it is already downloading `dd-java-agent`:

   ```
   RUN curl -Lo dd-java-agent.jar 'https://dtdg.co/latest-java-tracer'
   ```

1. Within the same `calendar/dockerfile.calendar.maven` file, comment out the `ENTRYPOINT` line for running without tracing. Then uncomment the `ENTRYPOINT` line, which runs the application with tracing enabled:

   ```
   ENTRYPOINT ["java" , "-javaagent:../dd-java-agent.jar", "-Ddd.trace.sample.rate=1", "-jar" , "target/calendar-0.0.1-SNAPSHOT.jar"]
   ```
Important alert (level: danger): Again, the flags, particularly the sample rate, are not necessarily appropriate for environments outside this tutorial. For information about what to use in your real environment, read Tracing configuration.
1. Build both applications and publish them to GCR. From the `docker` directory, run:

   ```sh
   gcloud auth configure-docker
   DOCKER_DEFAULT_PLATFORM=linux/amd64 docker-compose -f service-docker-compose-k8s.yaml build calendar
   docker tag docker-calendar:latest  gcr.io/<PROJECT_NAME>/calendar-tutorial:calendar
   docker push gcr.io/<PROJECT_NAME>/calendar-tutorial:calendar
```



1. Open `kubernetes/calendar-app.yaml` and update the `image` entry with the URL for the GCR image, where you pushed the `calendar` app in the previous step:

   ```yaml
       spec:
         containers:
           - name: calendar-app
             image: gcr.io/<PROJECT_ID>/calendar-tutorial:calendar
             imagePullPolicy: Always
```



1. From the `kubernetes` directory, deploy both `notes` and `calendar` apps, now with custom instrumentation, on the cluster:

   ```sh
   kubectl create -f notes-app.yaml
   kubectl create -f calendar-app.yaml
```



1. Using the method you used before, find the external IP of the `notes` app.

1. Send a POST request with the `add_date` parameter:

{% dl %}

{% dt %}
`curl -X POST '<EXTERNAL_IP>:30080/notes?desc=hello_again&add_date=y'`
{% /dt %}

{% dd %}
`{"id":1,"description":"hello_again with date 2022-11-06"}`
{% /dd %}

{% /dl %}

In the Trace Explorer, click this latest trace to see a distributed trace between the two services:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-java-container-distributed.b52699b2e5afbb870e36d38586a62d3a.png?auto=format"
   alt="A flame graph for a distributed trace." /%}

Note that you didn't change anything in the `notes` application. Datadog automatically instruments both the `okHttp` library used to make the HTTP call from `notes` to `calendar`, and the Jetty library used to listen for HTTP requests in `notes` and `calendar`. This allows the trace information to be passed from one application to the other, capturing a distributed trace.

When you're done exploring, clean up all resources and delete the deployments:

```sh
kubectl delete -f notes-app.yaml
kubectl delete -f calendar-app.yaml
```



See [the documentation for GKE](https://cloud.google.com/kubernetes-engine/docs/how-to/deleting-a-cluster) for information about deleting the cluster.

## Troubleshooting{% #troubleshooting %}

If you're not receiving traces as expected, set up debug mode for the Java tracer. Read [Enable debug mode](https://docs.datadoghq.com/tracing/troubleshooting/tracer_debug_logs/#enable-debug-mode) to find out more.

## Further reading{% #further-reading %}

- [Additional tracing library configuration options](https://docs.datadoghq.com/tracing/trace_collection/library_config/java/)
- [Detailed tracing library setup instructions](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/java/)
- [Supported Java frameworks for automatic instrumentation](https://docs.datadoghq.com/tracing/trace_collection/compatibility/java/)
- [Manually configuring traces and spans](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/java/)
- [Tracing library open source code repository](https://github.com/DataDog/dd-trace-java)
