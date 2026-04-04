# Source: https://grpc-ecosystem.github.io/grpc-gateway/docs/mapping/httpbody_messages/

Title: HttpBody Messages

URL Source: https://grpc-ecosystem.github.io/grpc-gateway/docs/mapping/httpbody_messages/

Markdown Content:
HttpBody Messages | gRPC-Gateway
===============

[gRPC-Gateway](https://grpc-ecosystem.github.io/grpc-gateway/)[](https://grpc-ecosystem.github.io/grpc-gateway/docs/mapping/httpbody_messages/#)

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

1.   [Mapping](https://grpc-ecosystem.github.io/grpc-gateway/docs/mapping/httpbody_messages/)
2.   HttpBody Messages

[](https://grpc-ecosystem.github.io/grpc-gateway/docs/mapping/httpbody_messages/#httpbody-messages) HttpBody Messages
=====================================================================================================================

The [HTTPBody](https://github.com/googleapis/googleapis/blob/master/google/api/httpbody.proto) messages allow a response message to be specified with custom data content and a custom content-type header. The values included in the HTTPBody response will be used verbatim in the returned message from the gateway. Make sure you format your response carefully!

[](https://grpc-ecosystem.github.io/grpc-gateway/docs/mapping/httpbody_messages/#example-usage) Example Usage
-------------------------------------------------------------------------------------------------------------

1.   Define your service in gRPC with an httpbody response message

```
import "google/api/httpbody.proto";
import "google/api/annotations.proto";
import "google/protobuf/empty.proto";

service HttpBodyExampleService {
	rpc HelloWorld(google.protobuf.Empty) returns (google.api.HttpBody) {
		option (google.api.http) = {
			get: "/helloworld"
		};
	}
	rpc Download(google.protobuf.Empty) returns (stream google.api.HttpBody) {
		option (google.api.http) = {
			get: "/download"
		};
	}
}
```

1.   Generate gRPC and reverse-proxy stubs and implement your service.

[](https://grpc-ecosystem.github.io/grpc-gateway/docs/mapping/httpbody_messages/#example-service-implementation) Example service implementation
-----------------------------------------------------------------------------------------------------------------------------------------------

```
func (*HttpBodyExampleService) Helloworld(ctx context.Context, in *empty.Empty) (*httpbody.HttpBody, error) {
	return &httpbody.HttpBody{
		ContentType: "text/html",
		Data:        []byte("Hello World"),
	}, nil
}

func (HttpBodyExampleService) Download(_ *empty.Empty, stream HttpBodyExampleService_DownloadServer) error {
	msgs := []*httpbody.HttpBody{
		{
			ContentType: "text/html",
			Data:        []byte("Hello 1"),
		},
		{
			ContentType: "text/html",
			Data:        []byte("Hello 2"),
		},
	}

	for _, msg := range msgs {
		if err := stream.Send(msg); err != nil {
			return err
		}
	}

	return nil
}
```

* * *

[Back to top](https://grpc-ecosystem.github.io/grpc-gateway/docs/mapping/httpbody_messages/#top)

Copyright © the gRPC-Gateway Authors. Distributed by a [BSD 3-Clause License.](https://github.com/grpc-ecosystem/grpc-gateway/tree/main/LICENSE)

[Edit this page on GitHub](https://github.com/grpc-ecosystem/grpc-gateway/tree/main/docs/docs/mapping/httpbody_messages.md)
