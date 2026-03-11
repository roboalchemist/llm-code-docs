# Source: https://grpc-ecosystem.github.io/grpc-gateway/docs/tutorials/generating_stubs/using_buf/

Title: Generating stubs using buf

URL Source: https://grpc-ecosystem.github.io/grpc-gateway/docs/tutorials/generating_stubs/using_buf/

Markdown Content:
Generating stubs using buf | gRPC-Gateway
===============

[gRPC-Gateway](https://grpc-ecosystem.github.io/grpc-gateway/)[](https://grpc-ecosystem.github.io/grpc-gateway/docs/tutorials/generating_stubs/using_buf/#)

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

1.   [Tutorials](https://grpc-ecosystem.github.io/grpc-gateway/docs/tutorials/generating_stubs/using_buf/)
2.   [Generating stubs](https://grpc-ecosystem.github.io/grpc-gateway/docs/tutorials/generating_stubs/using_buf/)
3.   Generating stubs using buf

[](https://grpc-ecosystem.github.io/grpc-gateway/docs/tutorials/generating_stubs/using_buf/#generating-stubs-using-buf) Generating stubs using buf
==================================================================================================================================================

[Buf](https://github.com/bufbuild/buf) is a tool that provides various protobuf utilities such as linting, breaking change detection and generation. Please find installation instructions on [https://docs.buf.build/installation/](https://docs.buf.build/installation/).

It is configured through a 
```plaintext
buf.yaml
```
 file that should be checked in to the root of your Protobuf file hierarchy. Buf will automatically read this file if present. Configuration can also be provided via the command-line flag 
```plaintext
--config
```
, which accepts a path to a 
```plaintext
.json
```
 or 
```plaintext
.yaml
```
 file, or direct JSON or YAML data. As opposed to 
```plaintext
protoc
```
, where all 
```plaintext
.proto
```
 files are manually specified on the command-line, buf operates by recursively discovering all 
```plaintext
.proto
```
 files under configuration and building them.

The following is an example of a valid configuration, and you would put it in the root of your Protobuf file hierarchy, e.g. in 
```plaintext
proto/buf.yaml
```
 relative to the root of your repository.

```
version: v1
name: buf.build/myuser/myrepo
```

To generate type and gRPC stubs for Go, create the file 
```plaintext
buf.gen.yaml
```
:

```
version: v1
plugins:
  - plugin: go
    out: proto
    opt: paths=source_relative
  - plugin: go-grpc
    out: proto
    opt: paths=source_relative
```

We use the 
```plaintext
go
```
 and 
```plaintext
go-grpc
```
 plugins to generate Go types and gRPC service definitions. We’re outputting the generated files relative to the 
```plaintext
proto
```
 folder, and we’re using the 
```plaintext
paths=source_relative
```
 option, which means that the generated files will appear in the same directory as the source 
```plaintext
.proto
```
 file.

Then run

```
$ buf generate
```

This will have generated a 
```plaintext
*.pb.go
```
 and a 
```plaintext
*_grpc.pb.go
```
 file for each protobuf package in our 
```plaintext
proto
```
 file hierarchy.

[Next](https://grpc-ecosystem.github.io/grpc-gateway/docs/tutorials/creating_main.go/)

* * *

[Back to top](https://grpc-ecosystem.github.io/grpc-gateway/docs/tutorials/generating_stubs/using_buf/#top)

Copyright © the gRPC-Gateway Authors. Distributed by a [BSD 3-Clause License.](https://github.com/grpc-ecosystem/grpc-gateway/tree/main/LICENSE)

[Edit this page on GitHub](https://github.com/grpc-ecosystem/grpc-gateway/tree/main/docs/docs/tutorials/generating_stubs/using_buf.md)
