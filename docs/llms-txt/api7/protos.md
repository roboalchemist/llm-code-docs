# Source: https://docs.api7.ai/apisix/key-concepts/protos.md

# Protos

In this document, you will learn the basic concept of protos in APISIX and why you may need them.

Explore additional resources at the end of the document for more information on related topics.

## Overview[â](#overview "Direct link to Overview")

In APISIX, *proto* objects contain [protocol buffer (protobuf)](https://protobuf.dev) definitions which define the service interface and message types used in communication with upstream [gRPC](https://grpc.io) services.

The following diagram illustrates the concept of a proto object using an example of APISIX transcoding between HTTP and gRPC. In this example, the route `/grpc-echo` is associated with the plugin `grpc-transcode` and a proto object:

![Diagram of APISIX transcoding between HTTP and gRPC](https://static.api7.ai/uploads/2023/05/06/8X50cIcx_protos.svg)

<br />

The gRPC server is registered with `EchoService` defined in `echo.proto` file, which echoes back string input from incoming requests.

To enable gRPC communication between APISIX and server, the protocol buffer definitions specified in the `echo.proto` file are added to the proto object in APISIX. This ensures that APISIX and the gRPC server agree on the specifications of data exchange, allowing APISIX to effectively communicate with the gRPC server and relay the responses back to the client over HTTP.

To learn more about how to use `grpc-transcode` for protocol transcoding, see [Transcode HTTP to gRPC](https://docs.api7.ai/apisix/how-to-guide/transformation/transcode-http-to-grpc.md).

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* Key Concepts - [Routes](https://docs.api7.ai/apisix/key-concepts/routes.md)
* How-To Guide - [Transcode HTTP to gRPC](https://docs.api7.ai/apisix/how-to-guide/transformation/transcode-http-to-grpc.md)
* Admin API - [Protos](https://docs.api7.ai/apisix/reference/admin-api/.md#tag/Proto)
