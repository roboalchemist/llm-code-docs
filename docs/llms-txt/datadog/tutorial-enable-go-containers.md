# Source: https://docs.datadoghq.com/tracing/guide/tutorial-enable-go-containers.md

---
title: >-
  Tutorial - Enabling Tracing for a Go Application and Datadog Agent in
  Containers
description: >-
  Step-by-step tutorial to enable distributed tracing for a Go application and
  Datadog Agent running in separate containers.
breadcrumbs: >-
  Docs > APM > Tracing Guides > Tutorial - Enabling Tracing for a Go Application
  and Datadog Agent in Containers
---

# Tutorial - Enabling Tracing for a Go Application and Datadog Agent in Containers

## Overview{% #overview %}

This tutorial walks you through the steps for enabling tracing on a sample Go application installed on a container. In this scenario, the Datadog Agent is also installed in a container.

For other scenarios, including the application and Agent on a host, the application and Agent on cloud infrastructure, and on applications written in other languages, see the other [Enabling Tracing tutorials](https://docs.datadoghq.com/tracing/guide/#enabling-tracing-tutorials).

See [Tracing Go Applications](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/go/) for general comprehensive tracing setup documentation for Go. **Note**: This documentation uses v2 of the Go tracer, which Datadog recommends for all users. If you are using v1, see the [migration guide](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/go/migration) to upgrade to v2.

### Prerequisites{% #prerequisites %}

- A Datadog account and [organization API key](https://docs.datadoghq.com/account_management/api-app-keys/)
- Git
- Docker
- Curl
- Go version 1.18+
- Make and GCC

## Install the sample containerized Go application{% #install-the-sample-containerized-go-application %}

The code sample for this tutorial is on GitHub, at [github.com/DataDog/apm-tutorial-golang.git](https://github.com/DataDog/apm-tutorial-golang). To get started, clone the git repository:

```shell
git clone https://github.com/DataDog/apm-tutorial-golang.git
```

The repository contains a multi-service Go application pre-configured to be run within Docker containers. The sample app consists of a basic notes app and a calendar app, each with a REST API to add and change data. The `docker-compose` YAML files are located in the `docker` directory.

This tutorial uses the `all-docker-compose.yaml` file, which builds containers for both the notes and calendar applications and the Datadog Agent.

### Starting and exercising the sample application{% #starting-and-exercising-the-sample-application %}

1. Build the application containers by running:

   ```shell
      docker-compose -f all-docker-compose.yaml build
```



1. Start the containers:

   ```shell
      docker-compose -f all-docker-compose.yaml up -d
```

1. Verify that the containers are running with the `docker ps` command. You should see something like this:

   ```shell
      CONTAINER ID   IMAGE                           COMMAND                  CREATED              STATUS                          PORTS                    NAMES
      0a4704ebed09   docker-notes                    "./cmd/notes/notes"      About a minute ago   Up About a minute               0.0.0.0:8080->8080/tcp   notes
      9c428d7f7ad1   docker-calendar                 "./cmd/calendar/caleâ¦"   About a minute ago   Up About a minute               0.0.0.0:9090->9090/tcp   calendar
      b2c2bafa6b36   gcr.io/datadoghq/agent:latest   "/bin/entrypoint.sh"     About a minute ago   Up About a minute (unhealthy)   8125/udp, 8126/tcp       datadog-ag
      
```



1. The sample `notes` application is a basic REST API that stores data in an in-memory database. Use `curl` to send a few API requests:

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
   Adds a note with the description `hello` and an ID value of `1`. Returns `{"id":1,"description":"hello"}`
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

1. Run more API calls to see the application in action. When you're done, shut down and remove the containers and make sure they've been removed:

   ```shell
      docker-compose -f all-docker-compose.yaml down
      docker-compose -f all-docker-compose.yaml rm
```

## Enable tracing{% #enable-tracing %}

Next, configure the Go application to enable tracing. Because the Agent runs in a container, there's no need to install anything.

To enable tracing support, uncomment the following imports in `apm-tutorial-golang/cmd/notes/main.go`:

In the `cmd/notes/main.go` file:

```go
    sqltrace "github.com/DataDog/dd-trace-go/contrib/database/sql/v2"
    chitrace "github.com/DataDog/dd-trace-go/contrib/go-chi/chi/v2"
    httptrace "github.com/DataDog/dd-trace-go/contrib/net/http/v2" 
    "github.com/DataDog/dd-trace-go/v2/ddtrace/tracer" 
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

Uncomment the following line:

In the `cmd/notes/main.go` file:

```go
db, err := sql.Open("sqlite3", "file::memory:?cache=shared")
```



## Add the Agent container{% #add-the-agent-container %}

Add the Datadog Agent in the services section of your `all-docker-compose.yaml` file to add the Agent to your build:

1. Uncomment the Agent configuration, and specify your own [Datadog API key](https://docs.datadoghq.com/account_management/api-app-keys/):

In the `docker/all-docker-compose.yaml` file:

   ```yaml
        datadog-agent:
        container_name: datadog-agent
        image: "gcr.io/datadoghq/agent:latest"
        pid: host
        environment:
          - DD_API_KEY=<DD_API_KEY_HERE>
          - DD_APM_ENABLED=true
          - DD_APM_NON_LOCAL_TRAFFIC=true
        volumes:
          - /var/run/docker.sock:/var/run/docker.sock
          - /proc/:/host/proc/:ro
          - /sys/fs/cgroup:/host/sys/fs/cgroup:ro
      
```



1. Uncomment the `depends_on` fields for `datadog-agent` in the `notes` container.

1. Observe that in the `notes` service section, the `DD_AGENT_HOST` environment variable is set to the hostname of the Agent container. Your `notes` container section should look like this:

In the `docker/all-docker-compose.yaml` file:

   ```yaml
      notes:
       container_name: notes
       restart: always
       build:
         context: ../
         dockerfile: ../dockerfile.notes
       ports:
         - 8080:8080
       labels:
         - com.datadoghq.tags.service="notes"
         - com.datadoghq.tags.env="dev"
         - com.datadoghq.tags.version="0.0.1"
       environment:
         - DD_SERVICE=notes
         - DD_ENV=dev
         - DD_VERSION=0.0.1
         - DD_AGENT_HOST=datadog-agent
   #     - CALENDAR_HOST=calendar
       depends_on:
   #     - calendar
         - datadog-agent
      
```
You'll configure the `calendar` sections and variables later in this tutorial.

## Launch the containers to explore automatic instrumentation{% #launch-the-containers-to-explore-automatic-instrumentation %}

Now that the Tracing Library is installed, spin up your application containers and start receiving traces. Run the following commands:

```shell
docker-compose -f all-docker-compose.yaml build
docker-compose -f all-docker-compose.yaml up -d
```

To start generating and collecting traces, launch the application again with `make run`.

You can tell the Agent is working by observing continuous output in the terminal, or by opening the [Events Explorer](https://app.datadoghq.com/event/explorer) in Datadog and seeing the start event for the Agent:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-python-container-agent-start-event.711f8214000243bf309cbeb509536274.png?auto=format"
   alt="Agent start event shown in Events Explorer" /%}

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

In the `docker/all-docker-compose.yaml` file:

```go
environment:
  - DD_API_KEY=<DD_API_KEY_HERE>
  - DD_APM_ENABLED=true
  - DD_APM_NON_LOCAL_TRAFFIC=true
```

For more information on available configuration options, see [Configuring the Go Tracing Library](https://docs.datadoghq.com/tracing/trace_collection/library_config/go/).

### Use automatic tracing libraries{% #use-automatic-tracing-libraries %}

Datadog has several fully supported libraries for Go that allow for automatic tracing when implemented in the code. In the `cmd/notes/main.go` file, you can see the `go-chi`, `sql`, and `http` libraries being aliased to the corresponding Datadog libraries: `chitrace`, `sqltrace`, and `httptrace` respectively:

In the `cmd/notes/main.go` file:

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

In the `cmd/notes/main.go` file:

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

For more information on custom tracing, see [Go Custom Instrumentation](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/go/).

## Add a second application to see distributed traces{% #add-a-second-application-to-see-distributed-traces %}

Tracing a single application is a great start, but the real value in tracing is seeing how requests flow through your services. This is called *distributed tracing*.

The sample project includes a second application called `calendar` that returns a random date whenever it is invoked. The `POST` endpoint in the notes application has a second query parameter named `add_date`. When it is set to `y`, the notes application calls the calendar application to get a date to add to the note.

To enable tracing in the calendar application:

1. Uncomment the following lines in `cmd/calendar/main.go`:

In the `cmd/calendar/main.go` file:

   ```go
      chitrace "github.com/DataDog/dd-trace-go/contrib/go-chi/chi/v2" // 2.x
       "github.com/DataDog/dd-trace-go/v2/ddtrace/tracer" // 2.x
      
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

1. Open `docker/all-docker-compose.yaml` and uncomment the `calendar` service to set up the Agent host and Unified Service Tags for the app and for Docker:

In the `docker/all-docker-compose.yaml` file:

   ```yaml
      calendar:
        container_name: calendar
        restart: always
        build:
          context: ../
          dockerfile: ../dockerfile.calendar
        labels:
          - com.datadoghq.tags.service="calendar"
          - com.datadoghq.tags.env="dev"
          - com.datadoghq.tags.version="0.0.1"
        environment:
          - DD_SERVICE=calendar
          - DD_ENV=dev
          - DD_VERSION=0.0.1
          - DD_AGENT_HOST=datadog-agent
        ports:
          - 9090:9090
        depends_on:
          - datadog-agent
      
```



1. In the `notes` service section, uncomment the `CALENDAR_HOST` environment variable and the `calendar` entry in `depends_on` to make the needed connections between the two apps. Your notes service should look like this:

In the `docker/all-docker-compose.yaml` file:

   ```yaml
      notes:
        container_name: notes
        restart: always
        build:
          context: ../
          dockerfile: ../dockerfile.notes
        ports:
          - 8080:8080
        labels:
          - com.datadoghq.tags.service="notes"
          - com.datadoghq.tags.env="dev"
          - com.datadoghq.tags.version="0.0.1"
        environment:
          - DD_SERVICE=notes
          - DD_ENV=dev
          - DD_VERSION=0.0.1
          - DD_AGENT_HOST=datadog-agent
          - CALENDAR_HOST=calendar
        depends_on:
          - calendar
          - datadog-agent
      
```



1. Stop all running containers:

   ```shell
      docker-compose -f all-docker-compose.yaml down
```



1. Spin up your application containers:

   ```shell
      docker-compose -f all-docker-compose.yaml build
      docker-compose -f all-docker-compose.yaml up -d
```



1. Send a POST request with the `add_date` parameter:

   ```go
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
