# Source: https://docs.datadoghq.com/tracing/guide/tutorial-enable-java-container-agent-host.md

---
title: >-
  Tutorial - Enabling Tracing for a Java Application in a Container and an Agent
  on a Host
description: >-
  Step-by-step tutorial to enable distributed tracing for a containerized Java
  application with the Datadog Agent on the host.
breadcrumbs: >-
  Docs > APM > Tracing Guides > Tutorial - Enabling Tracing for a Java
  Application in a Container and an Agent on a Host
---

# Tutorial - Enabling Tracing for a Java Application in a Container and an Agent on a Host

## Overview{% #overview %}

This tutorial walks you through the steps for enabling tracing on a sample Java application installed in a container. In this scenario, the Datadog Agent is installed on a host.

For other scenarios, including the application and Agent on a host, the application and the Agent in containers or cloud infrastructure, and applications written in different languages, see the other [Enabling Tracing tutorials](https://docs.datadoghq.com/tracing/guide/#enabling-tracing-tutorials).

See [Tracing Java Applications](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/java/) for general comprehensive tracing setup documentation for Java.

### Prerequisites{% #prerequisites %}

- A Datadog account and [organization API key](https://docs.datadoghq.com/account_management/api-app-keys/)
- Git
- Docker version 20.10 or greater
- Curl

## Install the Agent{% #install-the-agent %}

If you haven't installed a Datadog Agent on your machine, install one now.

1. Go to [**Integrations > Agent**](https://app.datadoghq.com/account/settings/agent/latest?platform=overview) and select your operating system. For example, on most Linux platforms, you can install the Agent by running the following script, replacing `<YOUR_API_KEY>` with your [Datadog API key](https://docs.datadoghq.com/account_management/api-app-keys/):

   ```shell
   DD_AGENT_MAJOR_VERSION=7 DD_API_KEY=<YOUR_API_KEY> DD_SITE="datadoghq.com" bash -c "$(curl -L https://install.datadoghq.com/scripts/install_script.sh)"

```

To send data to a Datadog site other than `datadoghq.com`, replace the `DD_SITE` environment variable with [your Datadog site](https://docs.datadoghq.com/getting_started/site/).

1. Ensure your Agent is configured to receive trace data from containers. Open its [configuration file](https://docs.datadoghq.com/agent/configuration/agent-configuration-files/?tab=agentv6v7) and ensure `apm_config:` is uncommented, and `apm_non_local_traffic` is uncommented and set to `true`.

1. Start the Agent service on the host. The command [depends on the operating system](https://docs.datadoghq.com/agent/configuration/agent-commands/?tab=agentv6v7#start-the-agent), for example:

**MacOS**: `launchctl start com.datadoghq.agent`**Linux**: `sudo service datadog-agent start`

1. Verify that the Agent is running and sending data to Datadog by going to [**Events > Explorer**](https://app.datadoghq.com/event/explorer), optionally filtering by the `Datadog` Source facet, and looking for an event that confirms the Agent installation on the host:

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-python-host-agent-verify.ce96a3342b4a17c0bd057b314716daba.png?auto=format"
      alt="Event Explorer showing a message from Datadog indicating the Agent was installed on a host." /%}

{% alert level="info" %}
If after a few minutes you don't see your host in Datadog (under **Infrastructure > Host map**), ensure you used the correct API key for your organization, available at [**Organization Settings > API Keys**](https://app.datadoghq.com/organization-settings/api-keys).
{% /alert %}

## Install the sample Dockerized Java application{% #install-the-sample-dockerized-java-application %}

The code sample for this tutorial is on GitHub at [github.com/Datadog/apm-tutorial-java-host](https://github.com/DataDog/apm-tutorial-java-host). To get started, clone the repository:

```sh
git clone https://github.com/DataDog/apm-tutorial-java-host.git
```

The repository contains a multi-service Java application pre-configured to be run within Docker containers. The sample app is a basic notes app with a REST API to add and change data.

For this tutorial, the `docker-compose` YAML files are located in the folder `apm-tutorial-java-host/docker`. The instructions that follow assume that your Agent is running on a Linux host, and so use the `service-docker-compose-linux.yaml` file. If your Agent is on a macOS or Windows host, follow the same directions but use the `service-docker-compose.yaml` file instead. The Linux file contains Linux-specific Docker settings that are described in the in-file comments.

In each of the `notes` and `calendar` directories, there are two sets of Dockerfiles for building the applications, either with Maven or with Gradle. This tutorial uses the Maven build, but if you are more familiar with Gradle, you can use it instead with the corresponding changes to build commands.

### Starting and exercising the sample application{% #starting-and-exercising-the-sample-application %}

1. Build the application's container by running the following from inside the `/docker` directory:

   ```sh
   docker-compose -f service-docker-compose-linux.yaml build notes
```

1. Start the container:

   ```sh
   docker-compose -f service-docker-compose-linux.yaml up notes
```

You can verify that it's running by viewing the containers with the `docker ps` command.

1. Open up another terminal and send API requests to exercise the app. The `notes` application is a REST API that stores data in an in-memory H2 database running in the same container. Send it a few commands:

{% dl %}

{% dt %}
`curl 'localhost:8080/notes'`
{% /dt %}

{% dd %}
`[]`
{% /dd %}

{% dt %}
`curl -X POST 'localhost:8080/notes?desc=hello'`
{% /dt %}

{% dd %}
`{"id":1,"description":"hello"}`
{% /dd %}

{% dt %}
`curl localhost:8080/notes/1`
{% /dt %}

{% dd %}
`{"id":1,"description":"hello"}`
{% /dd %}

{% dt %}
`curl localhost:8080/notes`
{% /dt %}

{% dd %}
`[{"id":1,"description":"hello"}]`
{% /dd %}

{% /dl %}

### Stop the application{% #stop-the-application %}

After you've seen the application running, stop it so that you can enable tracing on it.

1. Stop the containers:

   ```sh
   docker-compose -f service-docker-compose-linux.yaml down
```



1. Remove the containers:

   ```sh
   docker-compose -f service-docker-compose-linux.yaml rm
```

## Enable tracing{% #enable-tracing %}

Now that you have a working Java application, configure it to enable tracing.

1. Add the Java tracing package to your project. Open the `notes/dockerfile.notes.maven` file and uncomment the line that downloads `dd-java-agent`:

   ```
   RUN curl -Lo dd-java-agent.jar 'https://dtdg.co/latest-java-tracer'
   ```

1. Within the same `notes/dockerfile.notes.maven` file, comment out the `ENTRYPOINT` line for running without tracing. Then uncomment the `ENTRYPOINT` line, which runs the application with tracing enabled:

   ```
   ENTRYPOINT ["java" , "-javaagent:../dd-java-agent.jar", "-Ddd.trace.sample.rate=1", "-jar" , "target/notes-0.0.1-SNAPSHOT.jar"]
   ```

This automatically instruments the application with Datadog services.
Important alert (level: danger): The flags on these sample commands, particularly the sample rate, are not necessarily appropriate for environments outside this tutorial. For information about what to use in your real environment, read Tracing configuration.
1. [Universal Service Tags](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/) identify traced services across different versions and deployment environments so that they can be correlated within Datadog, and so you can use them to search and filter. The three environment variables used for Unified Service Tagging are `DD_SERVICE`, `DD_ENV`, and `DD_VERSION`. For applications deployed with Docker, these environment variables can be added within the Dockerfile or the `docker-compose` file. For this tutorial, the `service-docker-compose-linux.yaml` file already has these environment variables defined:

   ```yaml
     environment:
       - DD_SERVICE=notes
       - DD_ENV=dev
       - DD_VERSION=0.0.1
   ```

1. You can also see that Docker labels for the same Universal Service Tags `service`, `env`, and `version` values are set in the Dockerfile. This allows you also to get Docker metrics once your application is running.

   ```yaml
     labels:
       - com.datadoghq.tags.service="notes"
       - com.datadoghq.tags.env="dev"
       - com.datadoghq.tags.version="0.0.1"
   ```

## Configure the container to send traces to the Agent{% #configure-the-container-to-send-traces-to-the-agent %}

1. Open the compose file for the containers, `docker/service-docker-compose-linux.yaml`.

1. In the `notes` container section, add the environment variable `DD_AGENT_HOST` and specify the hostname of the Agent. For Docker 20.10 and later, use `host.docker.internal` to indicate that it's the host that is also running Docker:

   ```yaml
       environment:
        - DD_AGENT_HOST=host.docker.internal
   ```

If your Docker is older than 20.10, run the following command and use the returned IP anywhere that's configured to `host.docker.internal`:

   ```sh
   docker network inspect bridge --format='{{(index .IPAM.Config 0).Gateway}}'
   ```

1. **On Linux**: Observe that the YAML also specifies an `extra_hosts`, which allows communication on Docker's internal network. If your Docker is older than 20.10, remove this `extra_hosts` configuration line.

The `notes` section of your compose file should look something like this:

```yaml
  notes:
    container_name: notes
    restart: always
    build:
      context: ../
      dockerfile: notes/dockerfile.notes.maven
    ports:
      - 8080:8080
    extra_hosts:                             # Linux only
      - "host.docker.internal:host-gateway"  # Linux only
    labels:
      - com.datadoghq.tags.service="notes"
      - com.datadoghq.tags.env="dev"
      - com.datadoghq.tags.version="0.0.1"
    environment:
      - DD_SERVICE=notes
      - DD_ENV=dev
      - DD_VERSION=0.0.1
      - DD_AGENT_HOST=host.docker.internal
```

## Launch the containers to see automatic tracing{% #launch-the-containers-to-see-automatic-tracing %}

Now that the Tracing Library is installed and the Agent is running, restart your application to start receiving traces. Run the following commands:

```
docker-compose -f service-docker-compose.yaml build notes
docker-compose -f service-docker-compose.yaml up notes
```

With the application running, send some curl requests to it:

{% dl %}

{% dt %}
`curl localhost:8080/notes`
{% /dt %}

{% dd %}
`[]`
{% /dd %}

{% dt %}
`curl -X POST 'localhost:8080/notes?desc=hello'`
{% /dt %}

{% dd %}
`{"id":1,"description":"hello"}`
{% /dd %}

{% dt %}
`curl localhost:8080/notes/1`
{% /dt %}

{% dd %}
`{"id":1,"description":"hello"}`
{% /dd %}

{% dt %}
`curl localhost:8080/notes`
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

If you don't see traces after several minutes, check that the Agent is running. Clear any filter in the Traces Search field (sometimes it filters on an environment variable such as `ENV` that you aren't using).

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

The following steps walk you through adding annotations to the code to trace some sample methods.

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

1. Rebuild the containers (on Linux use `service-docker-compose-linux.yaml`):

   ```sh
   docker-compose -f service-docker-compose.yaml build notes
   docker-compose -f service-docker-compose.yaml up notes
   ```

1. Resend some HTTP requests, specifically some `GET` requests.

1. On the Trace Explorer, click on one of the new `GET` requests, and see a flame graph like this:

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-java-container-custom-flame.3faa56c8907d0876ffdf0f8ff95cf532.png?auto=format"
      alt="A flame graph for a GET trace with custom instrumentation." /%}

Note the higher level of detail in the stack trace now that the `getAll` function has custom tracing.

For more information, read [Custom Instrumentation](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/java/).

## Add a second application to see distributed traces{% #add-a-second-application-to-see-distributed-traces %}

Tracing a single application is a great start, but the real value in tracing is seeing how requests flow through your services. This is called *distributed tracing*.

The sample project includes a second application called `calendar` that returns a random date whenever it is invoked. The `POST` endpoint in the Notes application has a second query parameter named `add_date`. When it is set to `y`, Notes calls the calendar application to get a date to add to the note.

1. Configure the calendar app for tracing by adding `dd-java-agent` to the startup command in the Dockerfile, like you previously did for the notes app. Open `calendar/Dockerfile.calendar.maven` and see that it is already downloading `dd-java-agent`:

   ```
   RUN curl -Lo dd-java-agent.jar 'https://dtdg.co/latest-java-tracer'
   ```

1. Within the same `calendar/dockerfile.calendar.maven` file, comment out the `ENTRYPOINT` line for running without tracing. Then uncomment the `ENTRYPOINT` line, which runs the application with tracing enabled:

   ```
   ENTRYPOINT ["java" , "-javaagent:../dd-java-agent.jar", "-Ddd.trace.sample.rate=1", "-jar" , "target/calendar-0.0.1-SNAPSHOT.jar"]
   ```
Important alert (level: danger): Again, the flags, particularly the sample rate, are not necessarily appropriate for environments outside this tutorial. For information about what to use in your real environment, read Tracing configuration.
1. Open `docker/service-docker-compose-linux.yaml` and uncomment the environment variables for the `calendar` service to set up the Agent host and Unified Service Tags for the app and for Docker. As you did with the `notes` container, set the `DD_AGENT_HOST` value to match what your Docker requires, and remove `extra_hosts` if not on Linux:

   ```yaml
     calendar:
       container_name: calendar
       restart: always
       build:
         context: ../
         dockerfile: calendar/dockerfile.calendar.maven
       ports:
         - 9090:9090
       labels:
         - com.datadoghq.tags.service="calendar"
         - com.datadoghq.tags.env="dev"
         - com.datadoghq.tags.version="0.0.1"
       environment:
         - DD_SERVICE=calendar
         - DD_ENV=dev
         - DD_VERSION=0.0.1
         - DD_AGENT_HOST=host.docker.internal
       extra_hosts:                            # Linux only
         - "host.docker.internal:host-gateway" # Linux only
   ```

1. In the `notes` service section, uncomment the `CALENDAR_HOST` environment variable and the `calendar` entry in `depends_on` to make the needed connections between the two apps:

   ```yaml
     notes:
     ...
       environment:
         - DD_SERVICE=notes
         - DD_ENV=dev
         - DD_VERSION=0.0.1
         - DD_AGENT_HOST=host.docker.internal
         - CALENDAR_HOST=calendar
       depends_on:
         - calendar
   ```

1. Build the multi-service application by restarting the containers. First, stop all running containers:

   ```
   docker-compose -f service-docker-compose-linux.yaml down
   ```

Then run the following commands to start them:

   ```
   docker-compose -f service-docker-compose-linux.yaml build
   docker-compose -f service-docker-compose-linux.yaml up
   ```

1. Send a POST request with the `add_date` parameter:

{% dl %}

{% dt %}
`curl -X POST 'localhost:8080/notes?desc=hello_again&add_date=y'`
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

## Troubleshooting{% #troubleshooting %}

If you're not receiving traces as expected, set up debug mode for the Java tracer. Read [Enable debug mode](https://docs.datadoghq.com/tracing/troubleshooting/tracer_debug_logs/#enable-debug-mode) to find out more.

## Further reading{% #further-reading %}

- [Additional tracing library configuration options](https://docs.datadoghq.com/tracing/trace_collection/library_config/java/)
- [Detailed tracing library setup instructions](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/java/)
- [Supported Java frameworks for automatic instrumentation](https://docs.datadoghq.com/tracing/trace_collection/compatibility/java/)
- [Manually configuring traces and spans](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/java/)
- [Tracing library open source code repository](https://github.com/DataDog/dd-trace-java)
