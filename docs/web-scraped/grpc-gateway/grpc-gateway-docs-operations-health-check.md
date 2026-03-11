# Source: https://grpc-ecosystem.github.io/grpc-gateway/docs/operations/health_check/

Title: Health check

URL Source: https://grpc-ecosystem.github.io/grpc-gateway/docs/operations/health_check/

Markdown Content:
[](https://grpc-ecosystem.github.io/grpc-gateway/docs/operations/health_check/#with-the-grpc-health-checking-protocol) With the [gRPC Health Checking Protocol](https://github.com/grpc/grpc/blob/master/doc/health-checking.md)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To use the gRPC health checking protocol you must add the two health checking methods, `Watch` and `Check`.

[](https://grpc-ecosystem.github.io/grpc-gateway/docs/operations/health_check/#registering-the-health-server) Registering the health server
-------------------------------------------------------------------------------------------------------------------------------------------

1.   Add `google.golang.org/grpc/health/grpc_health_v1` to your imports
2.   Register the health server with `grpc_health_v1.RegisterHealthServer(grpcServer, yourService)`

[](https://grpc-ecosystem.github.io/grpc-gateway/docs/operations/health_check/#adding-the-health-check-methods) Adding the health check methods
-----------------------------------------------------------------------------------------------------------------------------------------------

1.   Check method

```
func (s *serviceServer) Check(ctx context.Context, in *health.HealthCheckRequest) (*health.HealthCheckResponse, error) {
	return &health.HealthCheckResponse{Status: health.HealthCheckResponse_SERVING}, nil
}
```

1.   Watch method

```
func (s *serviceServer) Watch(in *health.HealthCheckRequest, _ health.Health_WatchServer) error {
    // Example of how to register both methods but only implement the Check method.
	return status.Error(codes.Unimplemented, "unimplemented")
}
```

1.   You can test the functionality with [GRPC health probe](https://github.com/grpc-ecosystem/grpc-health-probe).

[](https://grpc-ecosystem.github.io/grpc-gateway/docs/operations/health_check/#adding-healthz-endpoint-to-runtimeservemux) Adding `/healthz` endpoint to runtime.ServeMux
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To automatically register a `/healthz` endpoint in your `ServeMux` you can use the `ServeMuxOption``WithHealthzEndpoint` which takes in a connection to your registered gRPC server.

This endpoint will forward a request to the `Check` method described above to really check the health of the whole system, not only the gateway itself. If your server doesn’t implement the health checking protocol each request to `/healthz` will result in the following:

```
{"code":12,"message":"unknown service grpc.health.v1.Health","details":[]}
```

If you’ve implemented multiple services in your server you can target specific services with the `?service=<service>` query parameter. This will then be added to the `health.HealthCheckRequest` in the `Service` property. With that you can write your own logic to handle that in the health checking methods.

Analogously, to register an `{/endpoint/path}` endpoint in your `ServeMux` with a user-defined endpoint path, you can use the `ServeMuxOption``WithHealthEndpointAt`, which accepts a connection to your registered gRPC server together with a custom `endpointPath string` parameter.

* * *
