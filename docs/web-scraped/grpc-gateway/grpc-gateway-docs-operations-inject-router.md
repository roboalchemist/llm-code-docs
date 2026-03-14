# Source: https://grpc-ecosystem.github.io/grpc-gateway/docs/operations/inject_router/

Title: Adding custom routes to the mux

URL Source: https://grpc-ecosystem.github.io/grpc-gateway/docs/operations/inject_router/

Markdown Content:
Adding custom routes to the mux | gRPC-Gateway
===============

[gRPC-Gateway](https://grpc-ecosystem.github.io/grpc-gateway/)[](https://grpc-ecosystem.github.io/grpc-gateway/docs/operations/inject_router/#)

*   [gRPC-Gateway](https://grpc-ecosystem.github.io/grpc-gateway/)
*   [Overview](https://grpc-ecosystem.github.io/grpc-gateway/docs/overview/)
    *   [Background](https://grpc-ecosystem.github.io/grpc-gateway/docs/overview/background/)
    *   [How do I use this?](https://grpc-ecosystem.github.io/grpc-gateway/docs/overview/usage/)

*   [Mapping](https://grpc-ecosystem.github.io/grpc-gateway/docs/mapping/)
    *   [Examples](https://grpc-ecosystem.github.io/grpc-gateway/docs/mapping/examples/)
    *   [HttpBody Messages](https://grpc-ecosystem.github.io/grpc-gateway/docs/mapping/httpbody_messages/)
    *   [Binary file uploads](https://grpc-ecosystem.github.io/grpc-gateway/docs/mapping/binary_file_uploads/)
    *   [Patch feature](https://grpc-ecosystem.github.io/grpc-gateway/docs/mapping/patch_feature/)
    *   [gRPC API Configuration](https://grpc-ecosystem.github.io/grpc-gateway/docs/mapping/grpc_api_configuration/)
    *   [Customizing OpenAPI Output](https://grpc-ecosystem.github.io/grpc-gateway/docs/mapping/customizing_openapi_output/)
    *   [Customizing your gateway](https://grpc-ecosystem.github.io/grpc-gateway/docs/mapping/customizing_your_gateway/)
    *   [Custom marshalers](https://grpc-ecosystem.github.io/grpc-gateway/docs/mapping/custom_marshalers/)

*   [Operations](https://grpc-ecosystem.github.io/grpc-gateway/docs/operations/)
    *   [Adding custom routes to the mux](https://grpc-ecosystem.github.io/grpc-gateway/docs/operations/inject_router/)
    *   [Health check](https://grpc-ecosystem.github.io/grpc-gateway/docs/operations/health_check/)
    *   [Tracing](https://grpc-ecosystem.github.io/grpc-gateway/docs/operations/tracing/)
    *   [AWS gateway integration](https://grpc-ecosystem.github.io/grpc-gateway/docs/operations/aws_gateway_integration/)
    *   [Extracting the HTTP path pattern for a request](https://grpc-ecosystem.github.io/grpc-gateway/docs/operations/annotated_context/)
    *   [Logging the request body pattern for a request](https://grpc-ecosystem.github.io/grpc-gateway/docs/operations/logging/)

*   [Development](https://grpc-ecosystem.github.io/grpc-gateway/docs/development/)
    *   [gRPC-Gateway v2 migration guide](https://grpc-ecosystem.github.io/grpc-gateway/docs/development/grpc-gateway_v2_migration_guide/)
    *   [Installation for Cygwin](https://grpc-ecosystem.github.io/grpc-gateway/docs/development/installation_for_cygwin/)

*   [Contributing](https://grpc-ecosystem.github.io/grpc-gateway/docs/contributing/)
    *   [Getting started](https://grpc-ecosystem.github.io/grpc-gateway/docs/contributing/getting_started/)
    *   [Google Season of Docs](https://grpc-ecosystem.github.io/grpc-gateway/docs/contributing/2020_season_of_docs/)

*   [Tutorials](https://grpc-ecosystem.github.io/grpc-gateway/docs/tutorials/)
    *   [Introduction to the gRPC-Gateway](https://grpc-ecosystem.github.io/grpc-gateway/docs/tutorials/introduction/)
    *   [Creating a simple hello world with gRPC](https://grpc-ecosystem.github.io/grpc-gateway/docs/tutorials/simple_hello_world/)
    *   [Generating stubs](https://grpc-ecosystem.github.io/grpc-gateway/docs/tutorials/generating_stubs/)
        *   [Generating stubs using buf](https://grpc-ecosystem.github.io/grpc-gateway/docs/tutorials/generating_stubs/using_buf/)
        *   [Generating stubs using protoc](https://grpc-ecosystem.github.io/grpc-gateway/docs/tutorials/generating_stubs/using_protoc/)

    *   [Creating main.go](https://grpc-ecosystem.github.io/grpc-gateway/docs/tutorials/creating_main.go/)
    *   [Adding gRPC-Gateway annotations to an existing proto file](https://grpc-ecosystem.github.io/grpc-gateway/docs/tutorials/adding_annotations/)
    *   [Learn More](https://grpc-ecosystem.github.io/grpc-gateway/docs/tutorials/learn_more/)

*   [FAQ](https://grpc-ecosystem.github.io/grpc-gateway/docs/faq/)
*   [Related projects](https://grpc-ecosystem.github.io/grpc-gateway/docs/related_projects/)
*   [Custom Query Parameter Parsing in gRPC-Gateway](https://grpc-ecosystem.github.io/grpc-gateway/docs/using_custom_query_parser/)
*   [Using arbitrary messages in response description](https://grpc-ecosystem.github.io/grpc-gateway/docs/mapping/using_ref_with_responses/)

 This site uses [Just the Docs](https://github.com/pmarsceill/just-the-docs), a documentation theme for Jekyll.

*   [gRPC-Gateway on GitHub](https://github.com/grpc-ecosystem/grpc-gateway)

1.   [Operations](https://grpc-ecosystem.github.io/grpc-gateway/docs/operations/inject_router/)
2.   Adding custom routes to the mux

[](https://grpc-ecosystem.github.io/grpc-gateway/docs/operations/inject_router/#adding-custom-routes-to-the-mux) Adding custom routes to the mux
================================================================================================================================================

The gRPC-Gateway allows you to add custom routes to the serve mux, for example, if you want to support a use case that isn’t supported by the gRPC-Gateway, like file uploads.

[](https://grpc-ecosystem.github.io/grpc-gateway/docs/operations/inject_router/#example) Example
------------------------------------------------------------------------------------------------

```
package main

import (
	"context"
	"net/http"

	pb "github.com/grpc-ecosystem/grpc-gateway/v2/examples/internal/helloworld"
	"github.com/grpc-ecosystem/grpc-gateway/v2/runtime"
)

func main() {
	ctx := context.TODO()
	mux := runtime.NewServeMux()
	// Register generated routes to mux
	err := pb.RegisterGreeterHandlerServer(ctx, mux, &GreeterServer{})
	if err != nil {
		panic(err)
	}
	// Register custom route for  GET /hello/{name}
	err = mux.HandlePath("GET", "/hello/{name}", func(w http.ResponseWriter, r *http.Request, pathParams map[string]string) {
		w.Write([]byte("hello " + pathParams["name"]))
	})
	if err != nil {
		panic(err)
	}
	http.ListenAndServe(":8080", mux)
}

// GreeterServer is the server API for Greeter service.
type GreeterServer struct {

}

// SayHello implement to say hello
func (h *GreeterServer) SayHello(ctx context.Context, req *pb.HelloRequest) (*pb.HelloReply, error) {
	return &pb.HelloReply{
		Message: "hello " + req.Name,
	}, nil
}
```

* * *

[Back to top](https://grpc-ecosystem.github.io/grpc-gateway/docs/operations/inject_router/#top)

Copyright © the gRPC-Gateway Authors. Distributed by a [BSD 3-Clause License.](https://github.com/grpc-ecosystem/grpc-gateway/tree/main/LICENSE)

[Edit this page on GitHub](https://github.com/grpc-ecosystem/grpc-gateway/tree/main/docs/docs/operations/inject_router.md)
