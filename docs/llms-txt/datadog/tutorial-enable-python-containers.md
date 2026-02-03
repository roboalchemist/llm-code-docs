# Source: https://docs.datadoghq.com/tracing/guide/tutorial-enable-python-containers.md

---
title: >-
  Tutorial - Enabling Tracing for a Python Application and Datadog Agent in
  Containers
description: >-
  Step-by-step tutorial to enable distributed tracing for a Python application
  and Datadog Agent running in separate containers.
breadcrumbs: >-
  Docs > APM > Tracing Guides > Tutorial - Enabling Tracing for a Python
  Application and Datadog Agent in Containers
---

# Tutorial - Enabling Tracing for a Python Application and Datadog Agent in Containers

## Overview{% #overview %}

This tutorial walks you through the steps for enabling tracing on a sample Python application installed in a container. In this scenario, the Datadog Agent is also installed in a container.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-python-containers-overview.1e74a83c775e300adcb0a88dfec5ceb8.png?auto=format"
   alt="Diagram showing installation scenario for this tutorial" /%}

For other scenarios, including the application and Agent on a host, the application in a container and Agent on a host, and on applications written in other languages, see the other [Enabling Tracing tutorials](https://docs.datadoghq.com/tracing/guide/#enabling-tracing-tutorials).

See [Tracing Python Applications](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/python/) for general comprehensive tracing setup documentation for Python.

### Prerequisites{% #prerequisites %}

- A Datadog account and [organization API key](https://docs.datadoghq.com/account_management/api-app-keys/)
- Git
- Python that meets the [tracing library requirements](https://docs.datadoghq.com/tracing/trace_collection/compatibility/python/)

## Install the sample Dockerized Python application{% #install-the-sample-dockerized-python-application %}

The code sample for this tutorial is on GitHub, at [github.com/Datadog/apm-tutorial-python](https://github.com/DataDog/apm-tutorial-python). To get started, clone the repository:

```sh
git clone https://github.com/DataDog/apm-tutorial-python.git
```

The repository contains a multi-service Python application pre-configured to be run within Docker containers. The sample app is a basic notes app with a REST API to add and change data.

### Starting and exercising the sample application{% #starting-and-exercising-the-sample-application %}

1. Build the application's container by running:

   ```sh
   docker-compose -f docker/containers/exercise/docker-compose.yaml build notes_app
```

1. Start the container:

   ```sh
   docker-compose -f docker/containers/exercise/docker-compose.yaml up db notes_app
```

The application is ready to use when you see the following output in the terminal:

   ```
   notes          |  * Debug mode: on
   notes          | INFO:werkzeug:WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
   notes          |  * Running on all addresses (0.0.0.0)
   notes          |  * Running on http://127.0.0.1:8080
   notes          |  * Running on http://192.168.32.3:8080
   notes          | INFO:werkzeug:Press CTRL+C to quit
   notes          | INFO:werkzeug: * Restarting with stat
   notes          | WARNING:werkzeug: * Debugger is active!
   notes          | INFO:werkzeug: * Debugger PIN: 143-375-699
   ```

You can also verify that it's running by viewing the running containers with the `docker ps` command.

1. Open up another terminal and send API requests to exercise the app. The notes application is a REST API that stores data in a Postgres database running in another container. Send it a few commands:

{% dl %}

{% dt %}
`curl -X GET 'localhost:8080/notes'`
{% /dt %}

{% dd %}
`{}`
{% /dd %}

{% dt %}
`curl -X POST 'localhost:8080/notes?desc=hello'`
{% /dt %}

{% dd %}
`(1, hello)`
{% /dd %}

{% dt %}
`curl -X GET 'localhost:8080/notes?id=1'`
{% /dt %}

{% dd %}
`(1, hello)`
{% /dd %}

{% dt %}
`curl -X GET 'localhost:8080/notes'`
{% /dt %}

{% dd %}
`{"1", "hello"}`
{% /dd %}

{% dt %}
`curl -X PUT 'localhost:8080/notes?id=1&desc=UpdatedNote'`
{% /dt %}

{% dd %}
`(1, UpdatedNote)`
{% /dd %}

{% dt %}
`curl -X DELETE 'localhost:8080/notes?id=1'`
{% /dt %}

{% dd %}
`Deleted`
{% /dd %}

{% /dl %}

### Stop the application{% #stop-the-application %}

After you've seen the application running, stop it so that you can enable tracing on it.

1. Stop the containers:

   ```sh
   docker-compose -f docker/containers/exercise/docker-compose.yaml down
```



1. Remove the containers:

   ```sh
   docker-compose -f docker/containers/exercise/docker-compose.yaml rm
```

## Enable tracing{% #enable-tracing %}

Now that you have a working Python application, configure it to enable tracing.

1. Add the Python tracing package to your project. Open the file `apm-tutorial-python/requirements.txt`, and add `ddtrace` to the list if it is not already there:

   ```
   flask==2.2.2
   psycopg2-binary==2.9.3
   requests==2.28.1
   ddtrace
   ```

1. Within the notes application Dockerfile, `docker/containers/exercise/Dockerfile.notes`, change the CMD line that starts the application to use the `ddtrace` package:

   ```
   # Run the application with Datadog 
   CMD ["ddtrace-run", "python", "-m", "notes_app.app"]
   ```

This automatically instruments the application with Datadog services.

1. Apply [Universal Service Tags](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/), which identify traced services across different versions and deployment environments so that they can be correlated within Datadog, and you can use them to search and filter. The three environment variables used for Unified Service Tagging are `DD_SERVICE`, `DD_ENV`, and `DD_VERSION`. Add the following environment variables in the Dockerfile:

   ```
   ENV DD_SERVICE="notes"
   ENV DD_ENV="dev"
   ENV DD_VERSION="0.1.0"
   ```

1. Add Docker labels that correspond to the Universal Service Tags. This allows you also to get Docker metrics once your application is running.

   ```
   LABEL com.datadoghq.tags.service="notes"
   LABEL com.datadoghq.tags.env="dev"
   LABEL com.datadoghq.tags.version="0.1.0"
   ```

To check that you've set things up correctly, compare your Dockerfile file with the one provided in the sample repository's solution file, `docker/containers/solution/Dockerfile.notes`.

## Add the Agent container{% #add-the-agent-container %}

Add the Datadog Agent in the services section of the `docker/containers/exercise/docker-compose.yaml` file:

1. Add the Agent configuration, and specify your own [Datadog API key](https://docs.datadoghq.com/account_management/api-app-keys/) and [site](https://docs.datadoghq.com/getting_started/site/):

   ```yaml
     datadog:
       container_name: dd-agent
       image: "gcr.io/datadoghq/agent:latest"
       environment:
          - DD_API_KEY=<DD_API_KEY>
          - DD_SITE=datadoghq.com  # Default. Change to eu.datadoghq.com, us3.datadoghq.com, us5.datadoghq.com as appropriate for your org
          - DD_APM_ENABLED=true    # Enable APM
       volumes: 
          - /var/run/docker.sock:/var/run/docker.sock:ro 
          - /proc/:/host/proc/:ro
          - /sys/fs/cgroup/:/host/sys/fs/cgroup:ro
   ```

1. Add the environment variable `DD_AGENT_HOST` and specify the hostname of the Agent container to the section for each container with code that you want to monitor, in this case, the `notes_app` container:

   ```yaml
       environment:
        - DD_AGENT_HOST=datadog
   ```

To check that you've set things up correctly, compare your `docker-compose.yaml` file with the one provided in the sample repository's solution file, `docker/containers/solution/docker-compose.yaml`.

## Launch the containers to see automatic tracing{% #launch-the-containers-to-see-automatic-tracing %}

Now that the Tracing Library is installed, restart your application and start receiving traces. Run the following commands:

```
docker-compose -f docker/containers/exercise/docker-compose.yaml build notes_app
docker-compose -f docker/containers/exercise/docker-compose.yaml up db datadog notes_app
```

You can tell the Agent is working by observing continuous output in the terminal, or by opening the [Events Explorer](https://app.datadoghq.com/event/explorer) in Datadog and seeing the start event for the Agent:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-python-container-agent-start-event.711f8214000243bf309cbeb509536274.png?auto=format"
   alt="Agent start event shown in Events Explorer" /%}

With the application running, send some curl requests to it:

{% dl %}

{% dt %}
`curl -X POST 'localhost:8080/notes?desc=hello'`
{% /dt %}

{% dd %}
`(1, hello)`
{% /dd %}

{% dt %}
`curl -X GET 'localhost:8080/notes?id=1'`
{% /dt %}

{% dd %}
`(1, hello)`
{% /dd %}

{% dt %}
`curl -X PUT 'localhost:8080/notes?id=1&desc=UpdatedNote'`
{% /dt %}

{% dd %}
`(1, UpdatedNote)`
{% /dd %}

{% dt %}
`curl -X DELETE 'localhost:8080/notes?id=1'`
{% /dt %}

{% dd %}
`Deleted`
{% /dd %}

{% /dl %}

Wait a few moments, and go to [**APM > Traces**](https://app.datadoghq.com/apm/traces) in Datadog, where you can see a list of traces corresponding to your API calls:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-python-container-traces.6f06b94c0afc4ba49fc02535aa8b50f0.png?auto=format"
   alt="Traces from the sample app in APM Trace Explorer" /%}

If you don't see traces after several minutes, clear any filter in the Traces Search field (sometimes it filters on an environment variable such as `ENV` that you aren't using).

### Examine a trace{% #examine-a-trace %}

On the Traces page, click on a `POST /notes` trace to see a flame graph that shows how long each span took and what other spans occurred before a span completed. The bar at the top of the graph is the span you selected on the previous screen (in this case, the initial entry point into the notes application).

The width of a bar indicates how long it took to complete. A bar at a lower depth represents a span that completes during the lifetime of a bar at a higher depth.

The flame graph for a `POST` trace looks something like this:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-python-container-post-flame.5a7a3d2dd7ddb2f59fcf85ab9b46ebcd.png?auto=format"
   alt="A flame graph for a POST trace." /%}

A `GET /notes` trace looks something like this:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-python-container-get-flame.690b04e6318e1c0fcd4beb717e04f0da.png?auto=format"
   alt="A flame graph for a GET trace." /%}

## Add custom instrumentation to the Python application{% #add-custom-instrumentation-to-the-python-application %}

Automatic instrumentation is convenient, but sometimes you want more fine-grained spans. Datadog's Python DD Trace API allows you to specify spans within your code using annotations or code.

The following steps walk you through adding annotations to the code to trace some sample methods.

1. Open `notes_app/notes_helper.py`.

1. Add the following import:

   ```python
   from ddtrace import tracer
```



1. Inside the `NotesHelper` class, add a tracer wrapper called `notes_helper` to better see how the `notes_helper.long_running_process` method works:

   ```python
   class NotesHelper:
   
       @tracer.wrap(service="notes_helper")
       def long_running_process(self):
           time.sleep(.3)
           logging.info("Hello from the long running process")
           self.__private_method_1()
```



Now, the tracer automatically labels the resource with the function name it is wrapped around, in this case, `long_running_process`.

1. Rebuild the containers by running:

   ```sh
   docker-compose -f docker/containers/exercise/docker-compose.yaml build notes_app
   docker-compose -f docker/containers/exercise/docker-compose.yaml up db datadog notes_app
```



1. Resend some HTTP requests, specifically some `GET` requests.

1. On the Trace Explorer, click on one of the new `GET` requests, and see a flame graph like this:

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-python-container-custom-flame.b8d6d0c3a17901e0b0357584d00d4203.png?auto=format"
      alt="A flame graph for a GET trace with custom instrumentation." /%}

Note the higher level of detail in the stack trace now that the `get_notes` function has custom tracing.

For more information, read [Custom Instrumentation](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/python/).

## Add a second application to see distributed traces{% #add-a-second-application-to-see-distributed-traces %}

Tracing a single application is a great start, but the real value in tracing is seeing how requests flow through your services. This is called *distributed tracing*.

The sample project includes a second application called `calendar_app` that returns a random date whenever it is invoked. The `POST` endpoint in the Notes application has a second query parameter named `add_date`. When it is set to `y`, Notes calls the calendar application to get a date to add to the note.

1. Configure the calendar app for tracing by adding `dd_trace` to the startup command in the Dockerfile, like you previously did for the notes app. Open `docker/containers/exercise/Dockerfile.calendar` and update the CMD line like this:

   ```
   CMD ["ddtrace-run", "python", "-m", "calendar_app.app"] 
   ```

1. Apply Universal Service Tags, just like we did for the notes app. Add the following environment variables in the `Dockerfile.calendar` file:

   ```
   ENV DD_SERVICE="calendar"
   ENV DD_ENV="dev"
   ENV DD_VERSION="0.1.0"
   ```

1. Again, add Docker labels that correspond to the Universal Service Tags, allowing you to also get Docker metrics once your application runs.

   ```
   LABEL com.datadoghq.tags.service="calendar"
   LABEL com.datadoghq.tags.env="dev"
   LABEL com.datadoghq.tags.version="0.1.0"
   ```

1. Add the Agent container hostname, `DD_AGENT_HOST`, to the calendar application container to send traces to the correct location. Open `docker/containers/exercise/docker-compose.yaml` and add the following lines to the `calendar_app` section:

   ```yaml
       environment:
        - DD_AGENT_HOST=datadog
   ```

To check that you've set things up correctly, compare your setup with the Dockerfile and `docker-config.yaml` files provided in the sample repository's `docker/containers/solution` directory.

1. Build the multi-service application by restarting the containers. First, stop all running containers:

   ```
   docker-compose -f docker/containers/exercise/docker-compose.yaml down
   ```

Then run the following commands to start them:

   ```
   docker-compose -f docker/containers/exercise/docker-compose.yaml build
   docker-compose -f docker/containers/exercise/docker-compose.yaml up
   ```

1. Send a POST request with the `add_date` parameter:

{% dl %}

{% dt %}
`curl -X POST 'localhost:8080/notes?desc=hello_again&add_date=y'`
{% /dt %}

{% dd %}
`(2, hello_again with date 2022-11-06)`
{% /dd %}

{% /dl %}

In the Trace Explorer, click this latest trace to see a distributed trace between the two services:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-python-container-distributed.270003eee43f25508962b8bd1daa8c48.png?auto=format"
   alt="A flame graph for a distributed trace." /%}

## Add more custom instrumentation{% #add-more-custom-instrumentation %}

You can add custom instrumentation by using code. Suppose you want to further instrument the calendar service to better see the trace:

1. Open `notes_app/notes_logic.py`.

1. Add the following import

   ```python
   from ddtrace import tracer
   ```

1. Inside the `try` block, at about line 28, add the following `with` statement:

   ```python
   with tracer.trace(name="notes_helper", service="notes_helper", resource="another_process") as span:
   ```

Resulting in this:

   ```python
   def create_note(self, desc, add_date=None):
           if (add_date):
               if (add_date.lower() == "y"):
                   try:
                       with tracer.trace(name="notes_helper", service="notes_helper", resource="another_process") as span:
                           self.nh.another_process()
                       note_date = requests.get(f"http://localhost:9090/calendar")
                       note_date = note_date.text
                       desc = desc + " with date " + note_date
                       print(desc)
                   except Exception as e:
                       print(e)
                       raise IOError("Cannot reach calendar service.")
           note = Note(description=desc, id=None)
           note.id = self.db.create_note(note)
```



1. Rebuild the containers:

   ```
   docker-compose -f docker/containers/exercise/docker-compose.yaml build notes_app
   docker-compose -f docker/containers/exercise/docker-compose.yaml up
   ```

1. Send some more HTTP requests, specifically `POST` requests, with the `add_date` argument.

1. In the Trace Explorer, click into one of these new `POST` traces to see a custom trace across multiple services:

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-python-container-cust-dist.193727619f776590833bde5b6e0c61b8.png?auto=format"
      alt="A flame graph for a distributed trace with custom instrumentation." /%}
Note the new span labeled `notes_helper.another_process`.

If you're not receiving traces as expected, set up debug mode in the `ddtrace` Python package. Read [Enable debug mode](https://docs.datadoghq.com/tracing/troubleshooting/tracer_debug_logs/#enable-debug-mode) to find out more.

## Further reading{% #further-reading %}

- [Additional tracing library configuration options](https://docs.datadoghq.com/tracing/trace_collection/library_config/python/)
- [Detailed tracing library setup instructions](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/python/)
- [Supported Python frameworks for automatic instrumentation](https://docs.datadoghq.com/tracing/trace_collection/compatibility/python/)
- [Manually configuring traces and spans](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/python/)
- [Tracing library open source code repository](https://github.com/DataDog/dd-trace-py)
