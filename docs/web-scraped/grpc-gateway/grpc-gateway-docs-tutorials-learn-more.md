# Source: https://grpc-ecosystem.github.io/grpc-gateway/docs/tutorials/learn_more/

Title: Learn More

URL Source: https://grpc-ecosystem.github.io/grpc-gateway/docs/tutorials/learn_more/

Markdown Content:
Learn More | gRPC-Gateway
===============

[gRPC-Gateway](https://grpc-ecosystem.github.io/grpc-gateway/)[](https://grpc-ecosystem.github.io/grpc-gateway/docs/tutorials/learn_more/#)

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

1.   [Tutorials](https://grpc-ecosystem.github.io/grpc-gateway/docs/tutorials/learn_more/)
2.   Learn More

[](https://grpc-ecosystem.github.io/grpc-gateway/docs/tutorials/learn_more/#learn-more) Learn More
==================================================================================================

[](https://grpc-ecosystem.github.io/grpc-gateway/docs/tutorials/learn_more/#how-it-works) How it works
------------------------------------------------------------------------------------------------------

When the HTTP request arrives at the gRPC-Gateway, it parses the JSON data into a protobuf message. It then makes a normal Go gRPC client request using the parsed protobuf message. The Go gRPC client encodes the protobuf structure into the protobuf binary format and sends it to the gRPC server. The gRPC Server handles the request and returns the response in the protobuf binary format. The Go gRPC client parses it into a protobuf message and returns it to the gRPC-Gateway, which encodes the protobuf message to JSON and returns it to the original client.

[](https://grpc-ecosystem.github.io/grpc-gateway/docs/tutorials/learn_more/#googleapihttp) google.api.http
----------------------------------------------------------------------------------------------------------

Read more about 
```plaintext
google.api.http
```
 in [the source file documentation](https://github.com/googleapis/googleapis/blob/master/google/api/http.proto).

[](https://grpc-ecosystem.github.io/grpc-gateway/docs/tutorials/learn_more/#http-and-grpc-transcoding) HTTP and gRPC Transcoding
--------------------------------------------------------------------------------------------------------------------------------

Read more about HTTP and gRPC Transcoding on [AIP 127](https://google.aip.dev/127).

* * *

[Back to top](https://grpc-ecosystem.github.io/grpc-gateway/docs/tutorials/learn_more/#top)

Copyright © the gRPC-Gateway Authors. Distributed by a [BSD 3-Clause License.](https://github.com/grpc-ecosystem/grpc-gateway/tree/main/LICENSE)

[Edit this page on GitHub](https://github.com/grpc-ecosystem/grpc-gateway/tree/main/docs/docs/tutorials/learn_more.md)
