# Source: https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer

Title: tracer package - github.com/DataDog/dd-trace-go/ddtrace/tracer - Go Packages

URL Source: https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer

Markdown Content:
Package tracer contains Datadog's core tracing client. It is used to trace requests as they flow across web servers, databases and microservices, giving developers visibility into bottlenecks and troublesome requests. To start the tracer, simply call the start method along with an optional set of options. By default, the trace agent is considered to be found at "localhost:8126". In a setup where this would be different (let's say 127.0.0.1:1234), we could do:

tracer.Start(tracer.WithAgentAddr("127.0.0.1:1234"))
defer tracer.Stop()

The tracing client can perform trace sampling. While the trace agent already samples traces to reduce bandwidth usage, client sampling reduces performance overhead. To make use of it, the package comes with a ready-to-use rate sampler that can be passed to the tracer. To use it and keep only 30% of the requests, one would do:

s := tracer.NewRateSampler(0.3)
tracer.Start(tracer.WithSampler(s))

More precise control of sampling rates can be configured using sampling rules. This can be applied based on span name, service or both, and is used to determine the sampling rate to apply.

rules := []tracer.SamplingRule{
      // sample 10% of traces with the span name "web.request"
      tracer.NameRule("web.request", 0.1),
      // sample 20% of traces for the service "test-service"
      tracer.ServiceRule("test-service", 0.2),
      // sample 30% of traces when the span name is "db.query" and the service
      // is "postgres.db"
      tracer.NameServiceRule("db.query", "postgres.db", 0.3),
      // sample 100% of traces when service and name match these regular expressions
      {Service: regexp.MustCompile("^test-"), Name: regexp.MustCompile("http\\..*"), Rate: 1.0},
}
tracer.Start(tracer.WithSamplingRules(rules))
defer tracer.Stop()

Sampling rules can also be configured at runtime using the DD_TRACE_SAMPLING_RULES environment variable. When set, it overrides rules set by tracer.WithSamplingRules. The value is a JSON array of objects. Each object must have a "sample_rate", and the "name" and "service" fields are optional.

export DD_TRACE_SAMPLING_RULES='[{"name": "web.request", "sample_rate": 1.0}]'

All spans created by the tracer contain a context hereby referred to as the span context. Note that this is different from Go's context. The span context is used to package essential information from a span, which is needed when creating child spans that inherit from it. Thus, a child span is created from a span's span context. The span context can originate from within the same process, but also a different process or even a different machine in the case of distributed tracing.

To make use of distributed tracing, a span's context may be injected via a carrier into a transport (HTTP, RPC, etc.) to be extracted on the other end and used to create spans that are direct descendants of it. A couple of carrier interfaces which should cover most of the use-case scenarios are readily provided, such as HTTPCarrier and TextMapCarrier. Users are free to create their own, which will work with our propagation algorithm as long as they implement the TextMapReader and TextMapWriter interfaces. An example alternate implementation is the MDCarrier in our gRPC integration.

As an example, injecting a span's context into an HTTP request would look like this:

req, err := http.NewRequest("GET", "http://example.com", nil)
// ...
err := tracer.Inject(span.Context(), tracer.HTTPHeadersCarrier(req.Header))
// ...
http.DefaultClient.Do(req)

Then, on the server side, to continue the trace one would do:

sctx, err := tracer.Extract(tracer.HTTPHeadersCarrier(req.Header))
// ...
span := tracer.StartSpan("child.span", tracer.ChildOf(sctx))

In the same manner, any means can be used as a carrier to inject a context into a transport. Go's context can also be used as a means to transport spans within the same process. The methods StartSpanFromContext, ContextWithSpan and SpanFromContext exist for this reason.

Some libraries and frameworks are supported out-of-the-box by using one of our integrations. You can see a list of supported integrations here: [https://godoc.org/gopkg.in/DataDog/dd-trace-go.v1/contrib](https://godoc.org/gopkg.in/DataDog/dd-trace-go.v1/contrib)

A basic example demonstrating how to start the tracer, as well as how to create a root span and a child span that is a descendant of it.

*   [Constants](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#pkg-constants)
*   [Variables](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#pkg-variables)
*   [func ContextWithSpan(ctx context.Context, s Span) context.Context](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#ContextWithSpan)
*   [func Extract(carrier interface{}) (ddtrace.SpanContext, error)](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#Extract)
*   [func Inject(ctx ddtrace.SpanContext, carrier interface{}) error](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#Inject)
*   [func Start(opts ...StartOption)](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#Start)
*   [func Stop()](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#Stop)
*   [type FinishOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#FinishOption)
*       *   [func FinishTime(t time.Time) FinishOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#FinishTime)
    *   [func NoDebugStack() FinishOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#NoDebugStack)
    *   [func StackFrames(n, skip uint) FinishOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#StackFrames)
    *   [func WithError(err error) FinishOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#WithError)

*   [type HTTPHeadersCarrier](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#HTTPHeadersCarrier)
*       *   [func (c HTTPHeadersCarrier) ForeachKey(handler func(key, val string) error) error](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#HTTPHeadersCarrier.ForeachKey)
    *   [func (c HTTPHeadersCarrier) Set(key, val string)](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#HTTPHeadersCarrier.Set)

*   [type Propagator](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#Propagator)
*       *   [func NewPropagator(cfg *PropagatorConfig) Propagator](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#NewPropagator)

*   [type PropagatorConfig](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#PropagatorConfig)
*   [type RateSampler](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#RateSampler)
*       *   [func NewAllSampler() RateSampler](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#NewAllSampler)
    *   [func NewRateSampler(rate float64) RateSampler](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#NewRateSampler)

*   [type Sampler](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#Sampler)
*   [type SamplingRule](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#SamplingRule)
*       *   [func NameRule(name string, rate float64) SamplingRule](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#NameRule)
    *   [func NameServiceRule(name string, service string, rate float64) SamplingRule](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#NameServiceRule)
    *   [func RateRule(rate float64) SamplingRule](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#RateRule)
    *   [func ServiceRule(service string, rate float64) SamplingRule](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#ServiceRule)

*   [type Span](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#Span)
*       *   [func SpanFromContext(ctx context.Context) (Span, bool)](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#SpanFromContext)
    *   [func StartSpan(operationName string, opts ...StartSpanOption) Span](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#StartSpan)
    *   [func StartSpanFromContext(ctx context.Context, operationName string, opts ...StartSpanOption) (Span, context.Context)](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#StartSpanFromContext)

*   [type StartOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#StartOption)
*       *   [func WithAgentAddr(addr string) StartOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#WithAgentAddr)
    *   [func WithAnalytics(on bool) StartOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#WithAnalytics)
    *   [func WithAnalyticsRate(rate float64) StartOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#WithAnalyticsRate)
    *   [func WithDebugMode(enabled bool) StartOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#WithDebugMode)
    *   [func WithDogstatsdAddress(addr string) StartOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#WithDogstatsdAddress)
    *   [func WithEnv(env string) StartOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#WithEnv)
    *   [func WithGlobalTag(k string, v interface{}) StartOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#WithGlobalTag)
    *   [func WithHTTPClient(client *http.Client) StartOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#WithHTTPClient)
    *   [func WithHTTPRoundTripper(r http.RoundTripper) StartOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#WithHTTPRoundTripper)
    *   [func WithLogger(logger ddtrace.Logger) StartOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#WithLogger)
    *   [func WithPrioritySampling() StartOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#WithPrioritySampling)
    *   [func WithPropagator(p Propagator) StartOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#WithPropagator)
    *   [func WithRuntimeMetrics() StartOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#WithRuntimeMetrics)
    *   [func WithSampler(s Sampler) StartOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#WithSampler)
    *   [func WithSamplingRules(rules []SamplingRule) StartOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#WithSamplingRules)
    *   [func WithService(name string) StartOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#WithService)
    *   [func WithServiceName(name string) StartOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#WithServiceName)
    *   [func WithServiceVersion(version string) StartOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#WithServiceVersion)

*   [type StartSpanOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#StartSpanOption)
*       *   [func AnalyticsRate(rate float64) StartSpanOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#AnalyticsRate)
    *   [func ChildOf(ctx ddtrace.SpanContext) StartSpanOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#ChildOf)
    *   [func Measured() StartSpanOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#Measured)
    *   [func ResourceName(name string) StartSpanOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#ResourceName)
    *   [func ServiceName(name string) StartSpanOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#ServiceName)
    *   [func SpanType(name string) StartSpanOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#SpanType)
    *   [func StartTime(t time.Time) StartSpanOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#StartTime)
    *   [func Tag(k string, v interface{}) StartSpanOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#Tag)
    *   [func WithSpanID(id uint64) StartSpanOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#WithSpanID)

*   [type TextMapCarrier](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#TextMapCarrier)
*       *   [func (c TextMapCarrier) ForeachKey(handler func(key, val string) error) error](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#TextMapCarrier.ForeachKey)
    *   [func (c TextMapCarrier) Set(key, val string)](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#TextMapCarrier.Set)

*   [type TextMapReader](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#TextMapReader)
*   [type TextMapWriter](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#TextMapWriter)

*   [Package](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#example-package)

[View Source](https://github.com/DataDog/dd-trace-go/blob/v1.24.1/ddtrace/tracer/textmap.go#L70)

const (
	
	DefaultBaggageHeaderPrefix = "ot-baggage-"

	
	DefaultTraceIDHeader = "x-datadog-trace-id"

	
	DefaultParentIDHeader = "x-datadog-parent-id"

	
	DefaultPriorityHeader = "x-datadog-sampling-priority"
)

[View Source](https://github.com/DataDog/dd-trace-go/blob/v1.24.1/ddtrace/tracer/propagator.go#L42)

var (
	
	ErrInvalidCarrier = [errors](https://pkg.go.dev/errors).[New](https://pkg.go.dev/errors#New)("invalid carrier")

	
	ErrInvalidSpanContext = [errors](https://pkg.go.dev/errors).[New](https://pkg.go.dev/errors#New)("invalid span context")

	
	ErrSpanContextCorrupted = [errors](https://pkg.go.dev/errors).[New](https://pkg.go.dev/errors#New)("span context corrupted")

	ErrSpanContextNotFound = [errors](https://pkg.go.dev/errors).[New](https://pkg.go.dev/errors#New)("span context not found")
)

ContextWithSpan returns a copy of the given context which includes the span s.

Extract extracts a SpanContext from the carrier. The carrier is expected to implement TextMapReader, otherwise an error is returned. If the tracer is not started, calling this function is a no-op.

Inject injects the given SpanContext into the carrier. The carrier is expected to implement TextMapWriter, otherwise an error is returned. If the tracer is not started, calling this function is a no-op.

func Start(opts ...[StartOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#StartOption))

Start starts the tracer with the given set of options. It will stop and replace any running tracer, meaning that calling it several times will result in a restart of the tracer by replacing the current instance with a new one.

func Stop()

Stop stops the started tracer. Subsequent calls are valid but become no-op.

FinishOption is a configuration option for FinishSpan. It is aliased in order to help godoc group all the functions returning it together. It is considered more correct to refer to it as the type as the origin, ddtrace.FinishOption.

FinishTime sets the given time as the finishing time for the span. By default, the current time is used.

func NoDebugStack() [FinishOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#FinishOption)

NoDebugStack prevents any error presented using the WithError finishing option from generating a stack trace. This is useful in situations where errors are frequent and performance is critical.

func StackFrames(n, skip [uint](https://pkg.go.dev/builtin#uint)) [FinishOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#FinishOption)

StackFrames limits the number of stack frames included into erroneous spans to n, starting from skip.

WithError marks the span as having had an error. It uses the information from err to set tags such as the error message, error type and stack trace. It has no effect if the error is nil.

HTTPHeadersCarrier wraps an http.Header as a TextMapWriter and TextMapReader, allowing it to be used using the provided Propagator implementation.

ForeachKey implements TextMapReader.

Set implements TextMapWriter.

Propagator implementations should be able to inject and extract SpanContexts into an implementation specific carrier.

func NewPropagator(cfg *[PropagatorConfig](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#PropagatorConfig)) [Propagator](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#Propagator)

NewPropagator returns a new propagator which uses TextMap to inject and extract values. It propagates trace and span IDs and baggage. To use the defaults, nil may be provided in place of the config.

PropagatorConfig defines the configuration for initializing a propagator.

RateSampler is a sampler implementation which randomly selects spans using a provided rate. For example, a rate of 0.75 will permit 75% of the spans. RateSampler implementations should be safe for concurrent use.

func NewAllSampler() [RateSampler](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#RateSampler)

NewAllSampler is a short-hand for NewRateSampler(1). It is all-permissive.

NewRateSampler returns an initialized RateSampler with a given sample rate.

type Sampler interface {
	Sample(span [Span](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#Span)) [bool](https://pkg.go.dev/builtin#bool)
}

Sampler is the generic interface of any sampler. It must be safe for concurrent use.

SamplingRule is used for applying sampling rates to spans that match the service name, operation name or both. For basic usage, consider using the helper functions ServiceRule, NameRule, etc.

NameRule returns a SamplingRule that applies the provided sampling rate to spans that match the operation name provided.

NameServiceRule returns a SamplingRule that applies the provided sampling rate to spans matching both the operation and service names provided.

RateRule returns a SamplingRule that applies the provided sampling rate to all spans.

ServiceRule returns a SamplingRule that applies the provided sampling rate to spans that match the service name provided.

Span is an alias for ddtrace.Span. It is here to allow godoc to group methods returning ddtrace.Span. It is recommended and is considered more correct to refer to this type as ddtrace.Span instead.

SpanFromContext returns the span contained in the given context. A second return value indicates if a span was found in the context. If no span is found, a no-op span is returned.

func StartSpan(operationName [string](https://pkg.go.dev/builtin#string), opts ...[StartSpanOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#StartSpanOption)) [Span](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#Span)

StartSpan starts a new span with the given operation name and set of options. If the tracer is not started, calling this function is a no-op.

StartSpanFromContext returns a new span with the given operation name and options. If a span is found in the context, it will be used as the parent of the resulting span. If the ChildOf option is passed, the span from context will take precedence over it as the parent span.

type StartOption func(*config)

StartOption represents a function that can be provided as a parameter to Start.

WithAgentAddr sets the address where the agent is located. The default is localhost:8126. It should contain both host and port.

func WithAnalytics(on [bool](https://pkg.go.dev/builtin#bool)) [StartOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#StartOption)

WithAnalytics allows specifying whether Trace Search & Analytics should be enabled for integrations.

WithAnalyticsRate sets the global sampling rate for sampling APM events.

func WithDebugMode(enabled [bool](https://pkg.go.dev/builtin#bool)) [StartOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#StartOption)

WithDebugMode enables debug mode on the tracer, resulting in more verbose logging.

func WithDogstatsdAddress(addr [string](https://pkg.go.dev/builtin#string)) [StartOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#StartOption)

WithDogstatsdAddress specifies the address to connect to for sending metrics to the Datadog Agent. If not set, it defaults to "localhost:8125" or to the combination of the environment variables DD_AGENT_HOST and DD_DOGSTATSD_PORT. This option is in effect when WithRuntimeMetrics is enabled.

WithEnv sets the environment to which all traces started by the tracer will be submitted. The default value is the environment variable DD_ENV, if it is set.

func WithGlobalTag(k [string](https://pkg.go.dev/builtin#string), v interface{}) [StartOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#StartOption)

WithGlobalTag sets a key/value pair which will be set as a tag on all spans created by tracer. This option may be used multiple times.

WithHTTPClient specifies the HTTP client to use when emitting spans to the agent.

WithHTTPRoundTripper is deprecated. Please consider using WithHTTPClient instead. The function allows customizing the underlying HTTP transport for emitting spans.

WithLogger sets logger as the tracer's error printer.

func WithPropagator(p [Propagator](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#Propagator)) [StartOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#StartOption)

WithPropagator sets an alternative propagator to be used by the tracer.

func WithRuntimeMetrics() [StartOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#StartOption)

WithRuntimeMetrics enables automatic collection of runtime metrics every 10 seconds.

func WithSampler(s [Sampler](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#Sampler)) [StartOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#StartOption)

WithSampler sets the given sampler to be used with the tracer. By default an all-permissive sampler is used.

func WithSamplingRules(rules [][SamplingRule](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#SamplingRule)) [StartOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#StartOption)

WithSamplingRules specifies the sampling rates to apply to spans based on the provided rules.

WithService sets the default service name for the program.

WithServiceName is deprecated. Please use WithService. If you are using an older version and you are upgrading from WithServiceName to WithService, please note that WithService will determine the service name of server and framework integrations.

func WithServiceVersion(version [string](https://pkg.go.dev/builtin#string)) [StartOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#StartOption)

WithServiceVersion specifies the version of the service that is running. This will be included in spans from this service in the "version" tag.

StartSpanOption is a configuration option for StartSpan. It is aliased in order to help godoc group all the functions returning it together. It is considered more correct to refer to it as the type as the origin, ddtrace.StartSpanOption.

AnalyticsRate sets a custom analytics rate for a span. It decides the percentage of events that will be picked up by the App Analytics product. It's represents a float64 between 0 and 1 where 0.5 would represent 50% of events.

ChildOf tells StartSpan to use the given span context as a parent for the created span.

func Measured() [StartSpanOption](https://pkg.go.dev/github.com/DataDog/dd-trace-go@v1.24.1/ddtrace/tracer#StartSpanOption)

Measured marks this span to be measured for metrics and stats calculations.

ResourceName sets the given resource name on the started span. A resource could be an SQL query, a URL, an RPC method or something else.

ServiceName sets the given service name on the started span. For example "http.server".

SpanType sets the given span type on the started span. Some examples in the case of the Datadog APM product could be "web", "db" or "cache".

StartTime sets a custom time as the start time for the created span. By default a span is started using the creation time.

Tag sets the given key/value pair as a tag on the started Span.

WithSpanID sets the SpanID on the started span, instead of using a random number. If there is no parent Span (eg from ChildOf), then the TraceID will also be set to the value given here.

TextMapCarrier allows the use of a regular map[string]string as both TextMapWriter and TextMapReader, making it compatible with the provided Propagator.

ForeachKey conforms to the TextMapReader interface.

Set implements TextMapWriter.

type TextMapReader interface {
	
	
	
	ForeachKey(handler func(key, val [string](https://pkg.go.dev/builtin#string)) [error](https://pkg.go.dev/builtin#error)) [error](https://pkg.go.dev/builtin#error)
}

TextMapReader allows iterating over sets of key/value pairs. Carriers implementing TextMapReader are compatible to be used with Datadog's TextMapPropagator.

type TextMapWriter interface {
	Set(key, val [string](https://pkg.go.dev/builtin#string))
}

TextMapWriter allows setting key/value pairs of strings on the underlying data structure. Carriers implementing TextMapWriter are compatible to be used with Datadog's TextMapPropagator.
