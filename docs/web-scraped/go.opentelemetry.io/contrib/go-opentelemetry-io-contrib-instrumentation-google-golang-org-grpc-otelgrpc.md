# Source: https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc

Title: otelgrpc package - go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc - Go Packages

URL Source: https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc

Markdown Content:
Package otelgrpc is the instrumentation library for [google.golang.org/grpc](https://pkg.go.dev/google.golang.org/grpc).

Use [NewClientHandler](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#NewClientHandler) with [grpc.WithStatsHandler](https://pkg.go.dev/google.golang.org/grpc#WithStatsHandler) to instrument a gRPC client.

Use [NewServerHandler](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#NewServerHandler) with [grpc.StatsHandler](https://pkg.go.dev/google.golang.org/grpc#StatsHandler) to instrument a gRPC server.

*   [Constants](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#pkg-constants)
*   [func NewClientHandler(opts ...Option) stats.Handler](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#NewClientHandler)
*   [func NewServerHandler(opts ...Option) stats.Handler](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#NewServerHandler)
*   [type Event](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#Event)
*   [type Filter](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#Filter)
*   [type InterceptorFilter](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#InterceptorFilter)deprecated
*   [type InterceptorInfo](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#InterceptorInfo)
*   [type InterceptorType](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#InterceptorType)
*   [type Option](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#Option)
*       *   [func WithFilter(f Filter) Option](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#WithFilter)
    *   [func WithInterceptorFilter(f InterceptorFilter) Option](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#WithInterceptorFilter)deprecated
    *   [func WithMessageEvents(events ...Event) Option](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#WithMessageEvents)
    *   [func WithMeterProvider(mp metric.MeterProvider) Option](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#WithMeterProvider)
    *   [func WithMetricAttributes(a ...attribute.KeyValue) Option](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#WithMetricAttributes)
    *   [func WithMetricAttributesFn(fn func(ctx context.Context) []attribute.KeyValue) Option](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#WithMetricAttributesFn)
    *   [func WithPropagators(p propagation.TextMapPropagator) Option](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#WithPropagators)
    *   [func WithPublicEndpoint() Option](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#WithPublicEndpoint)
    *   [func WithPublicEndpointFn(fn func(context.Context, *stats.RPCTagInfo) bool) Option](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#WithPublicEndpointFn)
    *   [func WithSpanAttributes(a ...attribute.KeyValue) Option](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#WithSpanAttributes)
    *   [func WithSpanOptions(opts ...trace.SpanStartOption) Option](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#WithSpanOptions)deprecated
    *   [func WithTracerProvider(tp trace.TracerProvider) Option](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#WithTracerProvider)

*   [NewClientHandler](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#example-NewClientHandler)
*   [NewClientHandler (WithMetricAttributesFn_baggage)](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#example-NewClientHandler-WithMetricAttributesFn_baggage)
*   [NewClientHandler (WithMetricAttributesFn_interceptor)](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#example-NewClientHandler-WithMetricAttributesFn_interceptor)
*   [NewServerHandler](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#example-NewServerHandler)
*   [NewServerHandler (WithMetricAttributesFn_baggage)](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#example-NewServerHandler-WithMetricAttributesFn_baggage)
*   [NewServerHandler (WithMetricAttributesFn_metadata)](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#example-NewServerHandler-WithMetricAttributesFn_metadata)

[View Source](https://github.com/open-telemetry/opentelemetry-go-contrib/blob/instrumentation/google.golang.org/grpc/otelgrpc/v0.65.0/instrumentation/google.golang.org/grpc/otelgrpc/config.go#L18)

const ScopeName = "go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc"

ScopeName is the instrumentation scope name.

Version is the current release version of the gRPC instrumentation.

This section is empty.

#### func [NewClientHandler](https://github.com/open-telemetry/opentelemetry-go-contrib/blob/instrumentation/google.golang.org/grpc/otelgrpc/v0.65.0/instrumentation/google.golang.org/grpc/otelgrpc/stats_handler.go#L162)[¶](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#NewClientHandler "Go to NewClientHandler")added in v0.45.0

NewClientHandler creates a stats.Handler for a gRPC client.

package main

import (
	"google.golang.org/grpc"

	"go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc"
)

func main() {
	_, _ = grpc.NewClient("localhost", grpc.WithStatsHandler(otelgrpc.NewClientHandler()))
}

ExampleNewClientHandler_withMetricAttributesFn_baggage demonstrates how to add a dynamic client-side attribute using W3C baggage to the auto-instrumented metrics.

package main

import (
	"context"

	"go.opentelemetry.io/otel/attribute"
	"go.opentelemetry.io/otel/baggage"
	"google.golang.org/grpc"

	"go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc"
)

func main() {
	// Baggage must be set in the context before making the call, e.g.,
	// ...
	// member, err := baggage.NewMember("traffic.type", "internal")
	// ...
	// bag, err := baggage.New(member)
	// ...
	// ctx := baggage.ContextWithBaggage(ctx, bag)
	// ...

	_, _ = grpc.NewClient("localhost", grpc.WithStatsHandler(otelgrpc.NewClientHandler(
		otelgrpc.WithMetricAttributesFn(func(ctx context.Context) []attribute.KeyValue {
			bag := baggage.FromContext(ctx)
			if trafficType := bag.Member("traffic.type"); trafficType.Value() != "" {
				return []attribute.KeyValue{
					attribute.String("traffic.type", trafficType.Value()),
				}
			}

			return nil
		}),
	)))
}

ExampleNewClientHandler_withMetricAttributesFn_interceptor demonstrates how to add a dynamic client-side attribute using gRPC interceptors to the auto-instrumented metrics.

package main

import (
	"context"

	"go.opentelemetry.io/otel/attribute"
	"google.golang.org/grpc"

	"go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc"
)

func main() {
	// should be centralized, example only
	type retryAttemptKey struct{}

	// a gRPC client interceptor must populate that key with the actual retry attempt, e.g.,
	// ...
	// interceptor := func(ctx context.Context, method string, req, reply any,
	//     cc *grpc.ClientConn, invoker grpc.UnaryInvoker, opts ...grpc.CallOption) error {
	//     ...
	//     ctx = context.WithValue(ctx, retryAttemptKey{}, attempt)
	//     return invoker(ctx, method, req, reply, cc, opts...)
	// }
	// ...

	_, _ = grpc.NewClient("localhost", grpc.WithStatsHandler(otelgrpc.NewClientHandler(
		otelgrpc.WithMetricAttributesFn(func(ctx context.Context) []attribute.KeyValue {
			if attempt, ok := ctx.Value(retryAttemptKey{}).(int); ok {
				return []attribute.KeyValue{
					// Caution: example only.
					// This must be a controlled, bounded and very limited set of numbers
					// so that you don't end up with very high cardinality.
					attribute.Int("retry.attempt", attempt),
				}
			}

			return nil
		}),
	)))
}

#### func [NewServerHandler](https://github.com/open-telemetry/opentelemetry-go-contrib/blob/instrumentation/google.golang.org/grpc/otelgrpc/v0.65.0/instrumentation/google.golang.org/grpc/otelgrpc/stats_handler.go#L47)[¶](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#NewServerHandler "Go to NewServerHandler")added in v0.45.0

NewServerHandler creates a stats.Handler for a gRPC server.

package main

import (
	"google.golang.org/grpc"

	"go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc"
)

func main() {
	_ = grpc.NewServer(grpc.StatsHandler(otelgrpc.NewServerHandler()))
}

ExampleNewServerHandler_withMetricAttributesFn_baggage demonstrates how to add a dynamic server-side attribute using W3C baggage to the auto-instrumented metrics.

package main

import (
	"context"

	"go.opentelemetry.io/otel/attribute"
	"go.opentelemetry.io/otel/baggage"
	"go.opentelemetry.io/otel/propagation"
	"google.golang.org/grpc"

	"go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc"
)

func main() {
	// The client must set baggage in context beforehand and have baggage propagators configured to
	// inject it into the headers (see https://pkg.go.dev/go.opentelemetry.io/otel/propagation#section-documentation), e.g.,
	//
	// conn, err := grpc.NewClient(
	// ...
	// grpc.WithStatsHandler(otelgrpc.NewClientHandler(
	//	    otelgrpc.WithPropagators(propagation.NewCompositeTextMapPropagator(
	//			  propagation.Baggage{},
	//		)),
	//	)),
	//)
	// ...
	// member, err := baggage.NewMember("tenant.tier", "premium")
	// ...
	// bag, err := baggage.New(member)
	// ...
	// ctx := baggage.ContextWithBaggage(ctx, bag)
	// ...

	_ = grpc.NewServer(grpc.StatsHandler(otelgrpc.NewServerHandler(
		// Propagators are required to extract baggage from incoming request headers.
		otelgrpc.WithPropagators(propagation.NewCompositeTextMapPropagator(
			propagation.TraceContext{},
			propagation.Baggage{},
		)),
		otelgrpc.WithMetricAttributesFn(func(ctx context.Context) []attribute.KeyValue {
			bag := baggage.FromContext(ctx)
			if tier := bag.Member("tenant.tier"); tier.Value() != "" {
				return []attribute.KeyValue{
					attribute.String("tenant.tier", tier.Value()),
				}
			}

			return nil
		}),
	)))
}

ExampleNewServerHandler_withMetricAttributesFn_metadata demonstrates how to add a dynamic server-side attribute using gRPC metadata to the auto-instrumented metrics.

package main

import (
	"context"

	"go.opentelemetry.io/otel/attribute"
	"google.golang.org/grpc"
	"google.golang.org/grpc/metadata"

	"go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc"
)

func main() {
	// The client must set metadata in the outgoing context beforehand, e.g.,
	// ...
	// ctx := metadata.NewOutgoingContext(context.Background(), metadata.Pairs("origin", "some-origin"))
	// ...
	_ = grpc.NewServer(grpc.StatsHandler(otelgrpc.NewServerHandler(
		otelgrpc.WithMetricAttributesFn(func(ctx context.Context) []attribute.KeyValue {
			md, ok := metadata.FromIncomingContext(ctx)
			if ok {
				if origins := md.Get("origin"); len(origins) > 0 && origins[0] != "" {
					return []attribute.KeyValue{attribute.String("origin", origins[0])}
				}
			}

			// Some use-cases might require to fallback to a default.
			return []attribute.KeyValue{attribute.String("origin", "unknown")}
		}),
	)))
}

Event type that can be recorded, see WithMessageEvents.

const (
 ReceivedEvents [Event](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#Event) = [iota](https://pkg.go.dev/builtin#iota) SentEvents )

Different types of events that can be recorded, see WithMessageEvents.

Filter is a predicate used to determine whether a given request in should be instrumented by the attached RPC tag info. A Filter must return true if the request should be instrumented.

type InterceptorFilter func(*[InterceptorInfo](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#InterceptorInfo)) [bool](https://pkg.go.dev/builtin#bool)

InterceptorFilter is a predicate used to determine whether a given request in interceptor info should be instrumented. A InterceptorFilter must return true if the request should be traced.

Deprecated: Use stats handlers instead.

InterceptorInfo is the union of some arguments to four types of gRPC interceptors.

type InterceptorType [uint8](https://pkg.go.dev/builtin#uint8)

InterceptorType is the flag to define which gRPC interceptor the InterceptorInfo object is.

const (
	
	UndefinedInterceptor [InterceptorType](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#InterceptorType) = [iota](https://pkg.go.dev/builtin#iota)
	UnaryClient
	StreamClient
	UnaryServer
	StreamServer
)

type Option interface {
	
}

Option applies an option value for a config.

func WithFilter(f [Filter](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#Filter)) [Option](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#Option)

WithFilter returns an Option to use the request filter.

func WithInterceptorFilter(f [InterceptorFilter](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#InterceptorFilter)) [Option](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#Option)

WithInterceptorFilter returns an Option to use the request filter.

Deprecated: Use stats handlers instead.

func WithMessageEvents(events ...[Event](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#Event)) [Option](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#Option)

WithMessageEvents configures the Handler to record the specified events (span.AddEvent) on spans. By default only summary attributes are added at the end of the request.

Valid events are:

*   ReceivedEvents: Record the number of bytes read after every gRPC read operation.
*   SentEvents: Record the number of bytes written after every gRPC write operation.

WithMeterProvider returns an Option to use the MeterProvider when creating a Meter. If this option is not provide the global MeterProvider will be used.

WithMetricAttributes returns an Option to add custom attributes to the metrics.

WithMetricAttributesFn returns an Option to add dynamic custom attributes to the handler's metrics. The function is called once per RPC and the returned attributes are applied to all metrics recorded by this handler.

The context parameter is the standard gRPC request context and provides access to request-scoped data.

WithPropagators returns an Option to use the Propagators when extracting and injecting trace context from requests.

func WithPublicEndpoint() [Option](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#Option)

WithPublicEndpoint configures the Handler to link the span with an incoming span context. If this option is not provided, then the association is a child association instead of a link.

WithPublicEndpointFn runs with every request, and allows conditionally configuring the Handler to link the span with an incoming span context. If this option is not provided or returns false, then the association is a child association instead of a link. Note: WithPublicEndpoint takes precedence over WithPublicEndpointFn.

WithSpanAttributes returns an Option to add custom attributes to the spans.

WithSpanOptions configures an additional set of trace.SpanOptions, which are applied to each new span.

Deprecated: It is only used by the deprecated interceptor, and is unused by [NewClientHandler](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#NewClientHandler) and [NewServerHandler](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc#NewServerHandler).

WithTracerProvider returns an Option to use the TracerProvider when creating a Tracer.
