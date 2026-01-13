# Source: https://docs.datadoghq.com/tracing/guide/tutorial-enable-go-host.md

---
title: >-
  Tutorial - Enabling Tracing for a Go Application on the Same Host as the
  Datadog Agent
description: >-
  Step-by-step tutorial to enable distributed tracing for a Go application
  running on the same host as the Datadog Agent.
breadcrumbs: >-
  Docs > APM > Tracing Guides > Tutorial - Enabling Tracing for a Go Application
  on the Same Host as the Datadog Agent
source_url: https://docs.datadoghq.com/guide/tutorial-enable-go-host/index.html
---

# Tutorial - Enabling Tracing for a Go Application on the Same Host as the Datadog Agent

## Overview{% #overview %}

This tutorial walks you through the steps for enabling tracing on a sample Go application installed on a host. In this scenario, you install a Datadog Agent on the same host as the application.

For other scenarios, including applications in containers or on cloud infrastructure, Agent in a container, and applications written in different languages, see the other [Enabling Tracing tutorials](https://docs.datadoghq.com/tracing/guide/#enabling-tracing-tutorials).

See [Tracing Go Applications](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/go/) for general comprehensive tracing setup documentation for Go.

### Prerequisites{% #prerequisites %}

- A Datadog account and [organization API key](https://docs.datadoghq.com/account_management/api-app-keys/)
- A physical or virtual Linux host with root access when using `sudo`. The host has the following requirements:
  - Git
  - Curl
  - Go version 1.18+
  - Make and GCC

## Install the Agent{% #install-the-agent %}

If you haven't installed a Datadog Agent on your machine, go to [**Integrations > Agent**](https://app.datadoghq.com/account/settings/agent/latest?platform=overview) and select your operating system. For example, on most Linux platforms, you can install the Agent by running the following script, replacing `<YOUR_API_KEY>` with your [Datadog API key](https://docs.datadoghq.com/account_management/api-app-keys/):

```shell
DD_AGENT_MAJOR_VERSION=7 DD_API_KEY=<YOUR_API_KEY> DD_SITE="datadoghq.com" bash -c "$(curl -L https://install.datadoghq.com/scripts/install_script.sh)"
```

To send data to a Datadog site other than `datadoghq.com`, replace the `DD_SITE` environment variable with [your Datadog site](https://docs.datadoghq.com/getting_started/site/).

Verify that the Agent is running and sending data to Datadog by going to [**Events > Explorer**](https://app.datadoghq.com/event/explorer), optionally filtering by the `Datadog` Source facet, and looking for an event that confirms the Agent installation on the host:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-python-host-agent-verify.ce96a3342b4a17c0bd057b314716daba.png?auto=format"
   alt="Event Explorer showing a message from Datadog indicating the Agent was installed on a host." /%}

{% alert level="info" %}
If after a few minutes you don't see your host in Datadog (under **Infrastructure > Host map**), ensure you used the correct API key for your organization, available at [**Organization Settings > API Keys**](https://app.datadoghq.com/organization-settings/api-keys).
{% /alert %}

## Install and run a sample Go application{% #install-and-run-a-sample-go-application %}

Next, install a sample application to trace. The code sample for this tutorial can be found at [github.com/DataDog/apm-tutorial-golang.git](https://github.com/DataDog/apm-tutorial-golang). Clone the git repository by running:

```shell
git clone https://github.com/DataDog/apm-tutorial-golang.git
```

Build the sample application using the following command. The command might take a while the first time you run it:

```shell
make runNotes
```

The sample `notes` application is a basic REST API that stores data in an in-memory database. Use `curl` to send a few API requests:

{% dl %}

{% dt %}
`curl localhost:8080/notes`
{% /dt %}

{% dd %}
Returns `[]` because there is nothing in the database yet
{% /dd %}

{% dt %}
`curl -X POST 'localhost:8080/notes?desc=hello'`
{% /dt %}

{% dd %}
Adds a note with the description `hello` and an ID value of `1`. Returns `{"id":1,"description":"hello"}`.
{% /dd %}

{% dt %}
`curl localhost:8080/notes/1`
{% /dt %}

{% dd %}
Returns the note with `id` value of `1`: `{"id":1,"description":"hello"}`
{% /dd %}

{% dt %}
`curl -X POST 'localhost:8080/notes?desc=otherNote'`
{% /dt %}

{% dd %}
Adds a note with the description `otherNote` and an ID value of `2`. Returns `{"id":2,"description":"otherNote"}`
{% /dd %}

{% dt %}
`curl localhost:8080/notes`
{% /dt %}

{% dd %}
Returns the contents of the database: `[{"id":1,"description":"hello"},{"id";2,"description":"otherNote"}]`
{% /dd %}

{% /dl %}

Run more API calls to see the application in action. When you're done, run the following command to exit the application:

```shell
make exitNotes
```

## Install Datadog tracing{% #install-datadog-tracing %}

**Note**: This documentation uses v2 of the Go tracer, which Datadog recommends for all users. If you are using v1, see the [migration guide](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/go/migration) to upgrade to v2.

Next, install the Go tracer. From your `apm-tutorial-golang` directory, run:

```shell
go get github.com/DataDog/dd-trace-go/v2/ddtrace
```

Now that the tracing library has been added to `go.mod`, enable tracing support.

Uncomment the following imports in `apm-tutorial-golang/cmd/notes/main.go`:

In the `cmd/notes/main.go` file:

```go
  sqltrace "github.com/DataDog/dd-trace-go/contrib/database/sql/v2"
  chitrace "github.com/DataDog/dd-trace-go/contrib/go-chi/chi/v2" 
  httptrace "github.com/DataDog/dd-trace-go/contrib/net/http/v2"
  "github.com/DataDog/dd-trace-go/v2/ddtrace/tracer"
  "fmt"
```



Change the import:

```go
_ "github.com/mattn/go-sqlite3"
```

to:

```go
"github.com/mattn/go-sqlite3"
```



In the `main()` function, uncomment the following lines:

In the `cmd/notes/main.go` file:

```go
tracer.Start()
defer tracer.Stop()
```

In the `cmd/notes/main.go` file:

```go
client = httptrace.WrapClient(client, httptrace.RTWithResourceNamer(func(req *http.Request) string {
		return fmt.Sprintf("%s %s", req.Method, req.URL.Path)
	}))
```

In the `cmd/notes/main.go` file:

```go
r.Use(chitrace.Middleware(chitrace.WithService("notes")))
```

In `setupDB()`, uncomment the following lines:

In the `cmd/notes/main.go` file:

```go
sqltrace.Register("sqlite3", &sqlite3.SQLiteDriver{}, sqltrace.WithService("db"))
db, err := sqltrace.Open("sqlite3", "file::memory:?cache=shared")
```

Comment out the following line:

In the `cmd/notes/main.go` file:

```go
db, err := sql.Open("sqlite3", "file::memory:?cache=shared")
```



Once you've made these changes, run:

```shell
go mod tidy
```



## Launch the Go application and explore automatic instrumentation{% #launch-the-go-application-and-explore-automatic-instrumentation %}

To start generating and collecting traces, launch the application again with `make runNotes`.

Use `curl` to again send requests to the application:

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

Wait a few moments, and take a look at your Datadog UI. Navigate to [**APM > Traces**](https://app.datadoghq.com/apm/traces). The Traces list shows something like this:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-go-host-traces2.a4c96e77ce9bab870c5aca8b6586fdf0.png?auto=format"
   alt="Traces view shows trace data coming in from host." /%}

There are entries for the database (`db`) and the `notes` app. The traces list shows all the spans, when they started, what resource was tracked with the span, and how long it took.

If you don't see traces, clear any filter in the **Traces** Search field (sometimes it filters on an environment variable such as `ENV` that you aren't using).

### Examine a trace{% #examine-a-trace %}

On the Traces page, click on a `POST /notes` trace, and you'll see a flame graph that shows how long each span took and what other spans occurred before a span completed. The bar at the top of the graph is the span you selected on the previous screen (in this case, the initial entry point into the notes application).

The width of a bar indicates how long it took to complete. A bar at a lower depth represents a span that completes during the lifetime of a bar at a higher depth.

The flame graph for a `POST` trace looks something like this:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-go-host-post-flame.15c3bd9a147f4bd3225aeea40068792f.png?auto=format"
   alt="A flame graph for a POST trace." /%}

A `GET /notes` trace looks something like this:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-go-host-get-flame.ef3917fad9625764ca7790a4b2c57084.png?auto=format"
   alt="A flame graph for a GET trace." /%}

## Tracing configuration{% #tracing-configuration %}

You can configure the tracing library to add tags to the telemetry it sends to Datadog. Tags help group, filter, and display data meaningfully in dashboards and graphs. To add tags, specify environment variables when running the application. The project `Makefile` includes the environment variables `DD_ENV`, `DD_SERVICE`, and `DD_VERSION`, which are set to enable [Unified Service Tagging](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/):

In the `Makefile` file:

```go
run: build
  DD_TRACE_SAMPLE_RATE=1 DD_SERVICE=notes DD_ENV=dev DD_VERSION=0.0.1 ./cmd/notes/notes &
```

{% alert level="danger" %}
The `Makefile` also sets the `DD_TRACE_SAMPLE_RATE` environment variable to `1`, which represents a 100% sample rate. A 100% sample rate ensures that all requests to the notes service are sent to the Datadog backend for analysis and display for the purposes of this tutorial. In an actual production or high-volume environment, you wouldn't specify this high of a rate. Setting a high sample rate with this variable in the application overrides the Agent configuration and results in a very large volume of data being sent to Datadog. For most use cases, allow the Agent to automatically determine the sampling rate.
{% /alert %}

For more information on available configuration options, see [Configuring the Go Tracing Library](https://docs.datadoghq.com/tracing/trace_collection/library_config/go/).

### Use automatic tracing libraries{% #use-automatic-tracing-libraries %}

Datadog has several fully supported libraries for Go that allow for automatic tracing when implemented in the code. In the `cmd/notes/main.go` file, you can see the `go-chi`, `sql`, and `http` libraries being aliased to the corresponding Datadog libraries: `chitrace`, `sqltrace`, and `httptrace` respectively:

In the `main.go` file:

```go
import (
  ...
  sqltrace "github.com/DataDog/dd-trace-go/contrib/database/sql/v2"
  chitrace "github.com/DataDog/dd-trace-go/contrib/go-chi/chi/v2"
  httptrace "github.com/DataDog/dd-trace-go/contrib/net/http/v2"
  ...
)
```

In `cmd/notes/main.go`, the Datadog libraries are initialized with the `WithService` option. For example, the `chitrace` library is initialized as follows:

In the `main.go` file:

```go
r := chi.NewRouter()
r.Use(middleware.Logger)
r.Use(chitrace.Middleware(chitrace.WithService("notes")))
r.Mount("/", nr.Register())
```

Using `chitrace.WithService("notes")` ensures that all elements traced by the library fall under the service name `notes`.

The `main.go` file contains more implementation examples for each of these libraries. For an extensive list of libraries, see [Go Compatibility Requirements](https://docs.datadoghq.com/tracing/trace_collection/compatibility/go/#library-compatibility).

### Use custom tracing with context{% #use-custom-tracing-with-context %}

In cases where code doesn't fall under a supported library, you can create spans manually.

Remove the comments around the `makeSpanMiddleware` function in `notes/notesController.go`. It generates middleware that wraps a request in a span with the supplied name. To use this function, comment out the following lines:

In the `notes/notesController.go` file:

```go
  r.Get("/notes", nr.GetAllNotes)                // GET /notes
  r.Post("/notes", nr.CreateNote)                // POST /notes
  r.Get("/notes/{noteID}", nr.GetNoteByID)       // GET /notes/123
  r.Put("/notes/{noteID}", nr.UpdateNoteByID)    // PUT /notes/123
  r.Delete("/notes/{noteID}", nr.DeleteNoteByID) // DELETE /notes/123
```

Remove the comments around the following lines:

In the `notes/notesController.go` file:

```go
  r.Get("/notes", makeSpanMiddleware("GetAllNotes", nr.GetAllNotes))               // GET /notes
  r.Post("/notes", makeSpanMiddleware("CreateNote", nr.CreateNote))                // POST /notes
  r.Get("/notes/{noteID}", makeSpanMiddleware("GetNote", nr.GetNoteByID))          // GET /notes/123
  r.Put("/notes/{noteID}", makeSpanMiddleware("UpdateNote", nr.UpdateNoteByID))    // PUT /notes/123
  r.Delete("/notes/{noteID}", makeSpanMiddleware("DeleteNote", nr.DeleteNoteByID)) // DELETE /notes/123
```

Also remove the comment around the following import:

In the `notes/notesController.go` file:

```go
"github.com/DataDog/dd-trace-go/v2/ddtrace/tracer"
```

There are several examples of custom tracing in the sample application. Here are a couple more examples. Remove the comments to enable these spans:

The `doLongRunningProcess` function creates child spans from a parent context:

In the `notes/notesHelper.go` file:

```go
func doLongRunningProcess(ctx context.Context) {
	childSpan, ctx := tracer.StartSpanFromContext(ctx, "traceMethod1")
	childSpan.SetTag(ext.ResourceName, "NotesHelper.doLongRunningProcess")
	defer childSpan.Finish()

	time.Sleep(300 * time.Millisecond)
	log.Println("Hello from the long running process in Notes")
	privateMethod1(ctx)
}
```

The `privateMethod1` function demonstrates creating a completely separate service from a context:

In the `notes/notesHelper.go` file:

```go
func privateMethod1(ctx context.Context) {
	childSpan, _ := tracer.StartSpanFromContext(ctx, "manualSpan1",
		tracer.SpanType("web"),
		tracer.ServiceName("noteshelper"),
	)
	childSpan.SetTag(ext.ResourceName, "privateMethod1")
	defer childSpan.Finish()

	time.Sleep(30 * time.Millisecond)
	log.Println("Hello from the custom privateMethod1 in Notes")
}
```

Uncomment the following imports:

In the `notes/notesHelper.go` file:

```go
  "github.com/DataDog/dd-trace-go/v2/ddtrace/ext"
  "github.com/DataDog/dd-trace-go/v2/ddtrace/tracer"
```

Launch the application with `make runNotes` and try the `curl` commands again to observe the custom spans and traces you've just configured:

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

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/privatemethod1.b6081b47233f88fbc2b38ef69c264002.png?auto=format"
   alt="A flame graph displaying custom traces for privteMethod1 and doLongRunningProcess" /%}

For more information on custom tracing, see [Go Custom Instrumentation](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/go/).

## Examine distributed traces{% #examine-distributed-traces %}

Tracing a single application is a great start, but the real value in tracing is seeing how requests flow through your services. This is called *distributed tracing*.

The sample project includes a second application called `calendar` that returns a random date whenever it is invoked. The `POST` endpoint in the notes application has a second query parameter named `add_date`. When it is set to `y`, the notes application calls the calendar application to get a date to add to the note.

To enable tracing in the calendar application, uncomment the following lines in `cmd/calendar/main.go`:

In the `cmd/calendar/main.go` file:

```go
  chitrace "github.com/DataDog/dd-trace-go/contrib/go-chi/chi/v2"
  "github.com/DataDog/dd-trace-go/v2/ddtrace/tracer"
```

In the `cmd/calendar/main.go` file:

```go
  tracer.Start()
  defer tracer.Stop()
```

In the `cmd/calendar/main.go` file:

```go
  r.Use(chitrace.Middleware(chitrace.WithService("calendar")))
```

1. If the notes application is still running, use `make exitNotes` to stop it.

1. Run `make run` to start the sample application.

1. Send a POST request with the `add_date` parameter:

   ```shell
   curl -X POST 'localhost:8080/notes?desc=hello_again&add_date=y'
```



1. In the Trace Explorer, click this latest `notes` trace to see a distributed trace between the two services:

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-go-host-distributed.e2788e7116cc2a1554b5b714407b536a.png?auto=format"
      alt="A flame graph for a distributed trace." /%}

This flame graph combines interactions from multiple applications:

- The first span is a POST request sent by the user and handled by the `chi` router through the supported `go-chi` library.
- The second span is a `createNote` function that was manually traced by the `makeSpanMiddleware` function. The function created a span from the context of the HTTP request.
- The next span is the request sent by the notes application using the supported `http` library and the client initialized in the `main.go` file. This GET request is sent to the calendar application. The calendar application spans appear in blue because they are separate service.
- Inside the calendar application, a `go-chi` router handles the GET request and the `GetDate` function is manually traced with its own span under the GET request.
- Finally, the purple `db` call is its own service from the supported `sql` library. It appears at the same level as the `GET /Calendar` request because they are both called by the parent span `CreateNote`.

## Troubleshooting{% #troubleshooting %}

If you're not receiving traces as expected, set up debug mode for the Go tracer. Read [Enable debug mode](https://docs.datadoghq.com/tracing/troubleshooting/tracer_debug_logs/?code-lang=go) to find out more.

## Further reading{% #further-reading %}

- [Additional tracing library configuration options](https://docs.datadoghq.com/tracing/trace_collection/library_config/go/)
- [Detailed tracing library setup instructions](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/go/)
- [Supported Go frameworks for automatic instrumentation](https://docs.datadoghq.com/tracing/trace_collection/compatibility/go/)
- [Manually configuring traces and spans](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/go/)
- [Ingestion mechanisms](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/)
- [Tracing library open source code repository](https://github.com/DataDog/dd-trace-Go)
- [Instrumenting Amazon API Gateway](https://docs.datadoghq.com/tracing/trace_collection/proxy_setup/apigateway)
