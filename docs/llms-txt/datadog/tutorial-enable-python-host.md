# Source: https://docs.datadoghq.com/tracing/guide/tutorial-enable-python-host.md

---
title: >-
  Tutorial - Enabling Tracing for a Python Application on the Same Host as the
  Datadog Agent
description: >-
  Step-by-step tutorial to enable distributed tracing for a Python application
  running on the same host as the Datadog Agent.
breadcrumbs: >-
  Docs > APM > Tracing Guides > Tutorial - Enabling Tracing for a Python
  Application on the Same Host as the Datadog Agent
source_url: https://docs.datadoghq.com/guide/tutorial-enable-python-host/index.html
---

# Tutorial - Enabling Tracing for a Python Application on the Same Host as the Datadog Agent

## Overview{% #overview %}

This tutorial walks you through the steps for enabling tracing on a sample Python application installed on a host. In this scenario, you install a Datadog Agent on the same host as the application.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-python-host-overview.2f1ae624fe3254c8ca926674366382ab.png?auto=format"
   alt="Diagram showing installation scenario for this tutorial" /%}

For other scenarios, including applications in containers, Agent in a container, and applications written in different languages, see the other [Enabling Tracing tutorials](https://docs.datadoghq.com/tracing/guide/#enabling-tracing-tutorials).

See [Tracing Python Applications](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/python/) for general comprehensive tracing setup documentation for Python.

### Prerequisites{% #prerequisites %}

- A Datadog account and [organization API key](https://docs.datadoghq.com/account_management/api-app-keys/)
- Git
- Python that meets the [tracing library requirements](https://docs.datadoghq.com/tracing/trace_collection/compatibility/python/)

## Install the Agent{% #install-the-agent %}

If you haven't installed a Datadog Agent on your machine, go to [**Integrations > Agent**](https://app.datadoghq.com/account/settings/agent/latest?platform=overview) and select your operating system. For example, on most Linux platforms, you can install the Agent by running the following script, replacing `<YOUR_API_KEY>` with your [Datadog API key](https://docs.datadoghq.com/account_management/api-app-keys/):

```shell
DD_AGENT_MAJOR_VERSION=7 DD_API_KEY=<YOUR_API_KEY> DD_SITE="datadoghq.com" bash -c "$(curl -L https://install.datadoghq.com/scripts/install_script.sh)"
```

To send data to a Datadog site other than `datadoghq.com`, replace the `DD_SITE` environment variable with [your Datadog site](https://docs.datadoghq.com/getting_started/site/).

If you have an Agent already installed on the host, ensure it is at least version 7.28. The minimum version of Datadog Agent required to use `ddtrace` to trace Python applications is documented in the [tracing library developer docs](https://ddtrace.readthedocs.io/en/stable/versioning.html).

Verify that the Agent is running and sending data to Datadog by going to [**Events > Explorer**](https://app.datadoghq.com/event/explorer), optionally filtering by the `Datadog` Source facet, and looking for an event that confirms the Agent installation on the host:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-python-host-agent-verify.ce96a3342b4a17c0bd057b314716daba.png?auto=format"
   alt="Event Explorer showing a message from Datadog indicating the Agent was installed on a host." /%}

{% alert level="info" %}
If after a few minutes you don't see your host in Datadog (under **Infrastructure > Host map**), ensure you used the correct API key for your organization, available at [**Organization Settings > API Keys**](https://app.datadoghq.com/organization-settings/api-keys).
{% /alert %}

## Install and run a sample Python application{% #install-and-run-a-sample-python-application %}

Next, install a sample application to trace. The code sample for this tutorial can be found at [github.com/Datadog/apm-tutorial-python](https://github.com/DataDog/apm-tutorial-python). Clone the git repository by running:

```shell
git clone https://github.com/DataDog/apm-tutorial-python.git
```

Setup, configure, and install Python dependencies for the sample using either Poetry or pip. Run one of the following:

{% tab title="Poetry" %}

```shell
poetry install
```

{% /tab %}

{% tab title="pip" %}

```shell
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

{% /tab %}

Start the application by running:

{% tab title="Poetry" %}

```shell
poetry run python -m notes_app.app
```

{% /tab %}

{% tab title="pip" %}

```shell
python -m notes_app.app
```

{% /tab %}

The sample `notes_app` application is a basic REST API that stores data in an in-memory database. Open another terminal and use `curl` to send a few API requests:

{% dl %}

{% dt %}
`curl -X GET 'localhost:8080/notes'`
{% /dt %}

{% dd %}
Returns `{}` because there is nothing in the database yet
{% /dd %}

{% dt %}
`curl -X POST 'localhost:8080/notes?desc=hello'`
{% /dt %}

{% dd %}
Adds a note with the description `hello` and an ID value of `1`. Returns `( 1, hello)`.
{% /dd %}

{% dt %}
`curl -X GET 'localhost:8080/notes?id=1'`
{% /dt %}

{% dd %}
Returns the note with `id` value of `1`: `( 1, hello)`
{% /dd %}

{% dt %}
`curl -X POST 'localhost:8080/notes?desc=otherNote'`
{% /dt %}

{% dd %}
Adds a note with the description `otherNote` and an ID value of `2`. Returns `( 2, otherNote)`
{% /dd %}

{% dt %}
`curl -X GET 'localhost:8080/notes'`
{% /dt %}

{% dd %}
Returns the contents of the database: `{ "1": "hello", "2": "otherNote" }`
{% /dd %}

{% dt %}
`curl -X PUT 'localhost:8080/notes?id=1&desc=UpdatedNote'`
{% /dt %}

{% dd %}
Updates the description value for the first note to `UpdatedNote`.
{% /dd %}

{% dt %}
`curl -X DELETE 'localhost:8080/notes?id=1'`
{% /dt %}

{% dd %}
Removes the first note from the database.
{% /dd %}

{% /dl %}

Run more API calls to see the application in action. When you're done, type Ctrl+C to stop the application.

## Install Datadog tracing{% #install-datadog-tracing %}

Next, install the tracing library by using Poetry or pip (minimum version 18). From your `apm-tutorial-python` directory, run:

{% tab title="Poetry" %}

```shell
poetry add ddtrace
poetry install
```

{% /tab %}

{% tab title="pip" %}

```shell
pip install ddtrace
```

{% /tab %}

## Launch the Python application with automatic instrumentation{% #launch-the-python-application-with-automatic-instrumentation %}

To start generating and collecting traces, restart the sample application in a slightly different way than previously. Run:

{% tab title="Poetry" %}

```shell
DD_SERVICE=notes DD_ENV=dev DD_VERSION=0.1.0 \
 poetry run ddtrace-run python -m notes_app.app
```

{% /tab %}

{% tab title="pip" %}

```shell
DD_SERVICE=notes DD_ENV=dev DD_VERSION=0.1.0 \
 ddtrace-run python -m notes_app.app
```

{% /tab %}

That command sets the `DD_SERVICE`, `DD_VERSION`, and `DD_ENV` environment variables to enable [Unified Service Tagging](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/#non-containerized-environment), enabling data correlation across Datadog.

Use `curl` to again send requests to the application:

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
`( 1, hello)`
{% /dd %}

{% dt %}
`curl -X GET 'localhost:8080/notes?id=1'`
{% /dt %}

{% dd %}
`( 1, hello)`
{% /dd %}

{% dt %}
`curl -X POST 'localhost:8080/notes?desc=newNote'`
{% /dt %}

{% dd %}
`( 2, newNote)`
{% /dd %}

{% dt %}
`curl -X GET 'localhost:8080/notes'`
{% /dt %}

{% dd %}
`{ "1": "hello", "2": "newNote" }`
{% /dd %}

{% /dl %}

Wait a few moments, and take a look at your Datadog UI. Navigate to [**APM > Traces**](https://app.datadoghq.com/apm/traces)). The Traces list shows something like this:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-python-host-traces.1d1dba2e7012e69c0a6b5f1473917ef7.png?auto=format"
   alt="Traces view shows trace data coming in from host." /%}

If you don't see traces, clear any filter in the Traces Search field (sometimes it filters on an environment variable such as `ENV` that you aren't using).

### Examine a trace{% #examine-a-trace %}

In the Traces page, click on a `POST /notes` trace and you'll see a flame graph that shows how long each span took and what other spans occurred before a span completed. The bar at the top of the graph is the span you selected on the previous screen (in this case, the initial entry point into the notes application).

The width of a bar indicates how long it took to complete. A bar at a lower depth represents a span that completes during the lifetime of a bar at a higher depth.

The flame graph for a `POST` trace looks something like this:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-python-host-post-flame.b915a52304d1ef26b5dd2a736f2b8c3c.png?auto=format"
   alt="A flame graph for a POST trace." /%}

A `GET /notes` trace looks something like this:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-python-host-get-flame.fa9ebb1f0dc0f38dfc9e34b3f230bc0e.png?auto=format"
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

1. Resend some HTTP requests, specifically some `GET` requests.

1. On the Trace Explorer, click on one of the new `GET` requests, and see a flame graph like this:

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-python-host-custom-flame.7ea026c836e78c3d401f20f2a4f819af.png?auto=format"
      alt="A flame graph for a GET trace with custom instrumentation." /%}

Note the higher level of detail in the stack trace now that the `get_notes` function has custom tracing.

For more information, read [Custom Instrumentation](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/python/).

## Add a second application to see distributed traces{% #add-a-second-application-to-see-distributed-traces %}

Tracing a single application is a great start, but the real value in tracing is seeing how requests flow through your services. This is called *distributed tracing*.

The sample project includes a second application called `calendar_app` that returns a random date whenever it is invoked. The `POST` endpoint in the Notes application has a second query parameter named `add_date`. When it is set to `y`, Notes calls the calendar application to get a date to add to the note.

1. Start the calendar application by running:

   {% tab title="Poetry" %}

   ```shell
   DD_SERVICE=notes DD_ENV=dev DD_VERSION=0.1.0 \
   poetry run ddtrace-run python -m calendar_app.app
   ```

   {% /tab %}

   {% tab title="pip" %}

   ```shell
   DD_SERVICE=calendar DD_ENV=dev DD_VERSION=0.1.0 \
   ddtrace-run python -m calendar_app.app
   ```

   {% /tab %}

1. Send a POST request with the `add_date` parameter:

   {% dl %}
   
   {% dt %}
`curl -X POST 'localhost:8080/notes?desc=hello_again&add_date=y'`
   {% /dt %}

   {% dd %}
`(2, hello_again with date 2022-11-06)`
   {% /dd %}

      {% /dl %}

1. In the Trace Explorer, click this latest trace to see a distributed trace between the two services:

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-python-host-distributed.fcf92e6dccfcab4d990f1948dd871807.png?auto=format"
      alt="A flame graph for a distributed trace." /%}

## Add more custom instrumentation{% #add-more-custom-instrumentation %}

You can add custom instrumentation by using code. Suppose you want to further instrument the calendar service to better see the trace:

1. Open `notes_app/notes_logic.py`.

1. Add the following import:

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



1. Send more HTTP requests, specifically `POST` requests, with the `add_date` argument.

1. In the Trace Explorer, click into one of these new `POST` traces to see a custom trace across multiple services:

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-python-host-cust-dist.48c8d46dc2a4bba9bc96736a83b5a1f4.png?auto=format"
      alt="A flame graph for a distributed trace with custom instrumentation." /%}
Note the new span labeled `notes_helper.another_process`.

If you're not receiving traces as expected, set up debug mode in the `ddtrace` Python package. Read [Enable debug mode](https://docs.datadoghq.com/tracing/troubleshooting/tracer_debug_logs/#enable-debug-mode) to find out more.

## Further reading{% #further-reading %}

- [Additional tracing library configuration options](https://docs.datadoghq.com/tracing/trace_collection/library_config/python/)
- [Detailed tracing library setup instructions](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/python/)
- [Supported Python frameworks for automatic instrumentation](https://docs.datadoghq.com/tracing/trace_collection/compatibility/python/)
- [Manually configuring traces and spans](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/python/)
- [Tracing library open source code repository](https://github.com/DataDog/dd-trace-py)
