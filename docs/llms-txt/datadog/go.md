# Source: https://docs.datadoghq.com/feature_flags/server/go.md

# Source: https://docs.datadoghq.com/security/code_security/software_composition_analysis/setup_runtime/compatibility/go.md

# Source: https://docs.datadoghq.com/security/application_security/setup/gcp/cloud-run/go.md

# Source: https://docs.datadoghq.com/security/application_security/setup/aws/lambda/go.md

# Source: https://docs.datadoghq.com/security/application_security/setup/compatibility/go.md

# Source: https://docs.datadoghq.com/security/application_security/setup/go.md

# Source: https://docs.datadoghq.com/data_streams/setup/language/go.md

# Source: https://docs.datadoghq.com/profiler/profiler_troubleshooting/go.md

# Source: https://docs.datadoghq.com/profiler/enabling/go.md

# Source: https://docs.datadoghq.com/tracing/other_telemetry/connect_logs_and_traces/go.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/dynamic_instrumentation/enabling/go.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/library_config/go.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/compatibility/go.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/go.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/go.md

---
title: Tracing Go Applications
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > APM > Application Instrumentation > Add the Datadog Tracing Library >
  Tracing Go Applications
---

# Tracing Go Applications

## Compatibility requirements{% #compatibility-requirements %}

The Go Tracer requires Go `1.18+` and Datadog Agent `>= 5.21.1`. For a full list of Datadog's Go version and framework support (including legacy and maintenance versions), see the [Compatibility Requirements](https://docs.datadoghq.com/tracing/compatibility_requirements/go) page.

**Note**: This documentation uses v2 of the Go tracer, which Datadog recommends for all users. If you are using v1, see the [migration guide](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/go/migration) to upgrade to v2.

## Getting started{% #getting-started %}

Before you begin, make sure you've already [installed and configured the Agent](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/?tab=datadoglibraries#install-and-configure-the-agent).

There are two ways to instrument your Go application:

1. **Compile-time instrumentation**:

   - Ensures maximum coverage of your tracing instrumentation.
   - Does not require source code modifications, making ideal for integrating at the CI/CD level.

1. **Manual instrumentation**:

Use dd-trace-go in conjunction with our integration packages to automatically generate spans about libraries of your choosing. This option:

   - Gives you complete control over which parts of your application are traced.
   - Requires modifying the application's source code.

Refer to the instructions in the section corresponding to your preference below:

{% tab title="Compile-time instrumentation" %}
### Overview{% #overview %}

[Orchestrion](https://github.com/DataDog/orchestrion) automatically adds instrumentation to Go applications during compilation, eliminating the need for code changes. It provides comprehensive tracing coverage and enables exclusive security features:

- Comprehensive tracing coverage:
  - Instruments your code and all dependencies, including the Go standard library
  - Instruments your code during compilation, preventing gaps in tracing coverage due to overlooked manual instrumentation
- Exclusive [App and API Protection](https://docs.datadoghq.com/security/application_security/exploit-prevention) **Exploit Prevention** feature. [Exploit Prevention](https://docs.datadoghq.com/security/application_security/exploit-prevention/) is a Runtime Application Self-Protection (RASP) implementation and includes RASP methods such as Local File Inclusion (LFI).

### Requirements{% #requirements %}

- Supports the two latest Go runtime releases (matching [Go's official release policy](https://go.dev/doc/devel/release#policy)).
- Applications must be managed using [go modules](https://pkg.go.dev/cmd/go#hdr-Modules__module_versions__and_more). Module vendoring is supported.

### Install Orchestrion{% #install-orchestrion %}

To install and set up Orchestrion:

1. Install Orchestrion:

   ```sh
   go install github.com/DataDog/orchestrion@latest
   ```
Important alert (level: info): Ensure that `$(go env GOBIN)` or `$(go env GOPATH)/bin` is in your `$PATH`.
1. Register Orchestrion in your project's `go.mod`:

   ```sh
   orchestrion pin
   ```

Refer to the output of `orchestrion pin -help` for more information about available customization options.

1. Commit changes to your version control system (unless you are integrating `orchestrion` directly in your CI/CD pipeline):

   ```sh
   git add go.mod go.sum orchestrion.tool.go
   git commit -m "chore: enable orchestrion"
   ```

Now you can manage your dependency on `orchestrion` like any other dependency using the `go.mod` file.

### Usage{% #usage %}

Use one of these methods to enable Orchestrion in your build process:

#### Prepend `orchestrion` to your usual `go` commands:{% #prepend-orchestrion-to-your-usual-go-commands %}

```sh
orchestrion go build .
orchestrion go run .
orchestrion go test ./...
```

#### Add the `-toolexec="orchestrion toolexec"` argument to your `go` commands:{% #add-the--toolexecorchestrion-toolexec-argument-to-your-go-commands %}

```sh
go build -toolexec="orchestrion toolexec" .
go run -toolexec="orchestrion toolexec" .
go test -toolexec="orchestrion toolexec" ./...
```

#### Modify the `$GOFLAGS` environment variable to inject Orchestrion, and use `go` commands normally:{% #modify-the-goflags-environment-variable-to-inject-orchestrion-and-use-go-commands-normally %}

```sh
# Make sure to include the quotes as shown below, as these are required for
# the Go toolchain to parse GOFLAGS properly!
export GOFLAGS="${GOFLAGS} '-toolexec=orchestrion toolexec'"
go build .
go run .
go test ./...
```

### Trace Customization{% #trace-customization %}

#### Setting up Unified Service Tagging{% #setting-up-unified-service-tagging %}

Applications instrumented by `orchestrion` support Unified Service Tagging (UST). You can set UST tags for your traces by setting the corresponding environment variable in your application's **runtime** environment:

| Unified Tag | Environment  |
| ----------- | ------------ |
| `env`       | `DD_ENV`     |
| `service`   | `DD_SERVICE` |
| `version`   | `DD_VERSION` |

For more information, refer to the [Unified Service Tagging documentation](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/).

#### Tracer configuration{% #tracer-configuration %}

Refer to [Library Configuration](https://docs.datadoghq.com/tracing/trace_collection/library_config/go/#traces) for configuration instructions.

#### Create custom trace spans{% #create-custom-trace-spans %}

Custom trace spans can be automatically created for any function annotated with the `//dd:span` directive comment:

In the `example.go` file:

```go
//dd:span custom_tag:tag_value
func CriticalPathFunction() {
  // ... implementation details ...
}
```

This also works with function literal expressions:

In the `example.go` file:

```go
//dd:span custom_tag:tag_value
handler := func(w http.ResponseWriter, r *http.Request) {
  // ... implementation details ...
}
```

#### Operation Name{% #operation-name %}

The name of the operation (`span.name`) is determined automatically using the following precedence:

1. An explicit `span.name:customOperationName` tag specified as a directive argument
1. The function's declared name (this does not apply to function literal expressions, which are anonymous)
1. The value of the very first tag provided to the directive arguments list

In the `example.go` file:

```go
//dd:span tag-name:spanName other-tag:bar span.name:operationName
func tracedFunction() {
  // This function will be represented as a span named "operationName"
}

//dd:span tag-name:spanName other-tag:bar
func otherTracedFunction() {
  // This function will be represented as a span named "otherTracedFunction"
}

//dd:span tag-name:spanName other-tag:bar
tracedFunction := func() {
  // This function will be represented as a span named "spanName"
}
```

#### Error Results{% #error-results %}

If the annotated function returns an `error` result, any error returned by the function will be automatically attached to the corresponding trace span:

In the `example.go` file:

```go
//dd:span
func failableFunction() (any, error) {
  // This span will have error information attached automatically.
  return nil, errors.ErrUnsupported
}
```

#### Prevent instrumentation of some code{% #prevent-instrumentation-of-some-code %}

You can use the `//orchestrion:ignore` directive to prevent `orchestrion` from performing *any* modification on the annotated code.

This can be used to prevent caller-side instrumentation from being applied to specific locations:

In the `example.go` file:

```go
import "database/sql"

// Caller-side instrumentation normally happens within this function...
func normal() {
  // The following assignment will NOT be modified to add any caller-side
  // instrumentation as it is opted out by the orchestrion:ignore directive:
  //orchestrion:ignore
  db, err := sql.Open("driver-name", "database=example")
  // ...
}

// Caller-side instrumentation will NOT happen in the following function
// as it is annotated with orchestrion:ignore.
//orchestrion:ignore
func excluded() {
  // The following assignment will NOT be modified to add any caller-side
  // instrumentation as the surrounding context is excluded by an
  // orchestrion:ignore directive:
  db, err := sql.Open("driver-name", "database=example")
  // ...
}
```

Some of the instrumentation performed by `orchestrion` is done callee-side (or library-side), meaning the integration is added directly within the dependency itself. In such cases, it is not possible to locally opt out of such integrations.

#### Use the tracing library{% #use-the-tracing-library %}

You can use the [tracing library](https://pkg.go.dev/github.com/DataDog/dd-trace-go/v2/ddtrace) in your Orchestrion-built application. This is useful for instrumenting frameworks not yet supported by Orchestrion. However, be aware that this may result in duplicated trace spans in the future as Orchestrion support expands. Review the [release notes](https://github.com/DataDog/orchestrion/releases) when updating your `orchestrion` dependency to stay informed about new features and adjust your manual instrumentation as necessary.

#### Use the continuous profiler{% #use-the-continuous-profiler %}

Your Orchestrion-built application includes [continuous profiler](https://docs.datadoghq.com/profiler) instrumentation. To enable the profiler, set the environment variable `DD_PROFILING_ENABLED=true` at runtime.

#### Remove integrations{% #remove-integrations %}

You can remove integrations by modifying the imports in the `orchestrion.tool.go` file. You can also create your own `orchestrion.tool.go` file before you run `orchestrion`. You might do this if you don't want an integration, or if you want to reduce the number of transitive dependencies for integrations your program doesn't use. By default, Orchestrion imports `github.com/DataDog/dd-trace-go/orchestrion/all/v2`, which imports every library for which there is an Orchestrion integration. You can replace this import with imports of only the integrations you want to use. See [the tracer source code](https://github.com/DataDog/dd-trace-go/blob/main/orchestrion/all/orchestrion.tool.go) for the list of supported integrations.

**Note**: If you choose to import specific integrations, you must manually update `orchestrion.tool.go` each time you want to add a new integration.

### Troubleshooting{% #troubleshooting %}

To troubleshoot builds that `orchestrion` manages, see [Troubleshooting Go Compile-Time Instrumentation](https://docs.datadoghq.com/tracing/troubleshooting/go_compile_time/).
{% /tab %}

{% tab title="Manual instrumentation" %}
### Add the tracer library to your application{% #add-the-tracer-library-to-your-application %}

First, import and start the tracer in your code following the [Library Configuration](https://docs.datadoghq.com/tracing/trace_collection/library_config/go/) documentation. Refer to the [API documentation](https://pkg.go.dev/github.com/DataDog/dd-trace-go/v2/ddtrace) (or the [API documentation v1](https://pkg.go.dev/gopkg.in/DataDog/dd-trace-go.v1/ddtrace)) for configuration instructions and details about using the API.

### Activate Go integrations to create spans{% #activate-go-integrations-to-create-spans %}

Activate [Go integrations](https://docs.datadoghq.com/tracing/compatibility_requirements/go) to generate spans. Datadog has a series of pluggable packages which provide out-of-the-box support for instrumenting a series of libraries and frameworks. A list of these packages can be found in the [Compatibility Requirements](https://docs.datadoghq.com/tracing/compatibility_requirements/go) page. Import these packages into your application and follow the configuration instructions listed alongside each integration.
{% /tab %}

## Further reading{% #further-reading %}

- [Tracer library source code](https://github.com/DataDog/dd-trace-go/tree/v1)
- [Tracer library API documentation](https://pkg.go.dev/github.com/DataDog/dd-trace-go/v2/ddtrace)
- [Tracer library API documentation for v2](https://pkg.go.dev/github.com/DataDog/dd-trace-go/v2/ddtrace)
- [Orchestrion source code](https://github.com/DataDog/orchestrion)
- [Explore your services, resources and traces](https://docs.datadoghq.com/tracing/glossary/)
