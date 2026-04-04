# Source: https://grpc-ecosystem.github.io/grpc-gateway/docs/operations/tracing/

Title: Tracing

URL Source: https://grpc-ecosystem.github.io/grpc-gateway/docs/operations/tracing/

Markdown Content:
[](https://grpc-ecosystem.github.io/grpc-gateway/docs/operations/tracing/#with-opencensusio-and-aws-x-ray) With [OpenCensus.io](https://opencensus.io/) and [AWS X-ray](https://aws.amazon.com/xray/)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [](https://grpc-ecosystem.github.io/grpc-gateway/docs/operations/tracing/#adding-tracing-using-aws-xray-as-the-exporter) Adding tracing using AWS-Xray as the exporter

This example uses the AWS-Xray exporter with a global trace setting. Note that AWS X-ray exporter does not handle any metrics only tracing.

1.   Add the following imports

```
xray "contrib.go.opencensus.io/exporter/aws"
"go.opencensus.io/plugin/ocgrpc"
"go.opencensus.io/plugin/ochttp"
"go.opencensus.io/trace"
```

1.   Register the AWS X-ray exporter for the GRPC server

```
xrayExporter, err := xray.NewExporter(
    xray.WithVersion("latest"),
    // Add your AWS region.
    xray.WithRegion("ap-southeast-1"),
)
if err != nil {
    // Handle any error.
}
// Do not forget to call Flush() before the application terminates.
defer xrayExporter.Flush()

// Register the trace exporter.
trace.RegisterExporter(xrayExporter)
```

1.   Add a global tracing configuration

```
// Always trace in this example.
// In production this can be set to a trace.ProbabilitySampler.
trace.ApplyConfig(trace.Config{DefaultSampler: trace.AlwaysSample()})
```

1.   Add `ocgrpc.ClientHandler` for tracing the gRPC client calls

```
conn, err := grpc.NewClient(
    // Other options goes here.
    // Add ocgrpc.ClientHandler for tracing the grpc client calls.
    grpc.WithStatsHandler(&ocgrpc.ClientHandler{}),
)
```

1.   Wrap the gateway mux with the OpenCensus HTTP handler

```
gwmux := runtime.NewServeMux()

openCensusHandler := &ochttp.Handler{
		Handler: gwmux,
}

gwServer := &http.Server{
    Addr: "0.0.0.0:10000",
    Handler: openCensusHandler,
    }),
}
```

### [](https://grpc-ecosystem.github.io/grpc-gateway/docs/operations/tracing/#without-a-global-configuration) Without a global configuration

In this example we have added the [gRPC Health Checking Protocol](https://github.com/grpc/grpc/blob/master/doc/health-checking.md) and we do not wish to trace any health checks.

1.   Follow step `1`, `2` and `4` from the previous section.

2.   Since we are not using a global configuration we can decide what paths we want to trace.

```
gwmux := runtime.NewServeMux()

openCensusHandler := &ochttp.Handler{
    Handler: gwmux,
    GetStartOptions: func(r *http.Request) trace.StartOptions {
        startOptions := trace.StartOptions{}
        if strings.HasPrefix(r.URL.Path, "/api") {
            // This example will always trace anything starting with /api.
            startOptions.Sampler = trace.AlwaysSample()
        }
        return startOptions
    },
}
```

1.   No global configuration means we have to use the [per span sampler](https://opencensus.io/tracing/sampling/#per-span-sampler).

#### [](https://grpc-ecosystem.github.io/grpc-gateway/docs/operations/tracing/#a-method-we-want-to-trace) A method we want to trace

```
func (s *service) Name(ctx context.Context, req *pb.Request) (*pb.Response, error) {
    // Here we add the span ourselves.
    ctx, span := trace.StartSpan(ctx, "name.to.use.in.trace", trace.
    // Select a sampler that fits your implementation.
    WithSampler(trace.AlwaysSample()))
    defer span.End()
    /// Other stuff goes here.
}
```

#### [](https://grpc-ecosystem.github.io/grpc-gateway/docs/operations/tracing/#a-method-we-do-not-wish-to-trace) A method we do not wish to trace

```
func (s *service) Check(ctx context.Context, in *health.HealthCheckRequest) (*health.HealthCheckResponse, error) {
    // Note no span here.
    return &health.HealthCheckResponse{Status: health.HealthCheckResponse_SERVING}, nil
}
```

[](https://grpc-ecosystem.github.io/grpc-gateway/docs/operations/tracing/#opentracing-support) OpenTracing Support
------------------------------------------------------------------------------------------------------------------

If your project uses [OpenTracing](https://github.com/opentracing/opentracing-go) and you’d like spans to propagate through the gateway, you can add some middleware which parses the incoming HTTP headers to create a new span correctly.

```
import (
	"github.com/opentracing/opentracing-go"
	"github.com/opentracing/opentracing-go/ext"
)

var grpcGatewayTag = opentracing.Tag{Key: string(ext.Component), Value: "grpc-gateway"}

func tracingWrapper(h http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		parentSpanContext, err := opentracing.GlobalTracer().Extract(
			opentracing.HTTPHeaders,
			opentracing.HTTPHeadersCarrier(r.Header))
		if err == nil || err == opentracing.ErrSpanContextNotFound {
			serverSpan := opentracing.GlobalTracer().StartSpan(
				"ServeHTTP",
				// this is magical, it attaches the new span to the parent parentSpanContext, and creates an unparented one if empty.
				ext.RPCServerOption(parentSpanContext),
				grpcGatewayTag,
			)
			r = r.WithContext(opentracing.ContextWithSpan(r.Context(), serverSpan))
			defer serverSpan.Finish()
		}
		h.ServeHTTP(w, r)
	})
}

// Then just wrap the mux returned by runtime.NewServeMux() like this
if err := http.ListenAndServe(":8080", tracingWrapper(mux)); err != nil {
	log.Fatalf("failed to start gateway server on 8080: %v", err)
}
```

Finally, don’t forget to add a tracing interceptor when registering the services. E.g.

```
import (
	"google.golang.org/grpc"
	"github.com/grpc-ecosystem/go-grpc-middleware/tracing/opentracing"
)

opts := []grpc.DialOption{
	grpc.WithUnaryInterceptor(
		grpc_opentracing.UnaryClientInterceptor(
			grpc_opentracing.WithTracer(opentracing.GlobalTracer()),
		),
	),
}
if err := pb.RegisterMyServiceHandlerFromEndpoint(ctx, mux, serviceEndpoint, opts); err != nil {
	log.Fatalf("could not register HTTP service: %v", err)
}
```

[](https://grpc-ecosystem.github.io/grpc-gateway/docs/operations/tracing/#opentelemetry) OpenTelemetry
------------------------------------------------------------------------------------------------------

If your project uses [OpenTelemetry](https://opentelemetry.io/) and you would like spans to propagate through the gateway, you can refer to the [OpenTelemetry gRPC-Gateway Boilerplate](https://github.com/iamrajiv/opentelemetry-grpc-gateway-boilerplate) project. This repository provides a sample project that showcases the integration of OpenTelemetry with gRPC-Gateway to set up an OpenTelemetry-enabled gRPC-Gateway REST server. The project includes a simple `SayHello` method implemented on the gRPC server that returns a greeting message to the client.

* * *
