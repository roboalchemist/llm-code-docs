# Source: https://docs.api7.ai/hub/grpc-web.md

# grpc-web

gRPC is a high-performance RPC framework based on HTTP/2 and Protocol Buffers, but it is not natively supported by browsers. gRPC-Web defines a browser-compatible protocol for sending gRPC requests over HTTP/1.1 or HTTP/2.

The `grpc-web` plugin translates gRPC-Web requests into native gRPC calls and forwards them to upstream gRPC services.

<!-- -->

<br />

## Request Handling[â](#request-handling "Direct link to Request Handling")

The `grpc-web` plugin processes client requests with specific HTTP methods, content types, and CORS rules.

### Supported HTTP Methods[â](#supported-http-methods "Direct link to Supported HTTP Methods")

The plugin supports:

* `POST` for gRPC-Web requests
* `OPTIONS` for CORS preflight checks

See [CORS support](https://github.com/grpc/grpc-web/blob/master/doc/browser-features.md#cors-support) for details.

### Supported Content Types[â](#supported-content-types "Direct link to Supported Content Types")

The plugin recognizes the following content types:

* `application/grpc-web`
* `application/grpc-web-text`
* `application/grpc-web+proto`
* `application/grpc-web-text+proto`

It automatically decodes messages in binary or base64 text format and translates them into standard gRPC for the upstream server. See [Protocol differences vs gRPC over HTTP2](https://github.com/grpc/grpc/blob/master/doc/PROTOCOL-WEB.md#protocol-differences-vs-grpc-over-http2) for more details.

### CORS Handling[â](#cors-handling "Direct link to CORS Handling")

The plugin automatically handles cross-origin requests. By default:

* All origins (`*`) are allowed
* `POST` requests are permitted
* Accepted request headers: `content-type`, `x-grpc-web`, `x-user-agent`
* Exposed response headers: `grpc-status`, `grpc-message`

## Examples[â](#examples "Direct link to Examples")

The following examples demonstrate how to configure and use the `grpc-web` plugin with a gRPC-Web client.

### Prerequisites[â](#prerequisites "Direct link to Prerequisites")

Before proceeding with the examples, complete the following preliminary steps to set up an upstream server and gRPC-Web client.

#### Start an Upstream Server[â](#start-an-upstream-server "Direct link to Start an Upstream Server")

Start a [grpcbin server](https://github.com/moul/grpcbin) in Docker to serve as the example upstream:

```
docker run -d \
  --name grpcbin \
  -p 9000:9000 \
  moul/grpcbin
```

#### Generate gRPC-Web client code[â](#generate-grpc-web-client-code "Direct link to Generate gRPC-Web client code")

Download the protocol buffer definition `hello.proto`:

```
curl -O https://raw.githubusercontent.com/moul/pb/refs/heads/master/hello/hello.proto
```

Install [`protobuf`](https://github.com/protocolbuffers/protobuf/releases) and [`protoc-gen-grpc-web`](https://github.com/grpc/grpc-web/releases).

Generate the gRPC-Web client code from `hello.proto`:

```
protoc \
  --js_out=import_style=commonjs:. \
  --grpc-web_out=import_style=commonjs,mode=grpcwebtext:. \
  hello.proto
```

You should see two files generated in the current directory: `hello_pb.js` for protocol buffers message classes and `hello_grpc_web_pb.js` for gRPC-Web client stubs.

#### Create a Client[â](#create-a-client "Direct link to Create a Client")

Create a Node.js project and install the required dependencies:

```
npm init -y
npm install xhr2 grpc-web google-protobuf 
```

Create a client file:

client.js

```
const XMLHttpRequest = require('xhr2');
const { HelloServiceClient } = require('./hello_grpc_web_pb');
const { HelloRequest } = require('./hello_pb');

global.XMLHttpRequest = XMLHttpRequest;

function sayHello(){
  const client = new HelloServiceClient('http://127.0.0.1:9080/grpc/web', null, {
    format: 'text',
  });
  const req = new HelloRequest();
  req.setGreeting('jack');

  const call = client.sayHello(req, {}, (err, resp) => {
    if (err) {
      console.error('grpc error:', err.code, err.message);
    } else {
      console.log('reply:', resp.getReply());
    }
  });

  call.on('metadata', (metadata) => {
    console.log('Response headers:', metadata);
  });
}

function lotsOfReplies() {
  const client = new HelloServiceClient('http://127.0.0.1:9080/grpc/web', null, {
    format: 'text',
  });
  const req = new HelloRequest();
  req.setGreeting('rep');
  const stream = client.lotsOfReplies(req, {});

  stream.on('metadata', (metadata) => {
    console.log('Response headers:', metadata);
  });
}

lotsOfReplies()
sayHello()
```

You can later run the client with `node client.js` to send both unary and server-streaming requests to your gRPC server via the gateway.

### Proxy gRPC-Web (Prefix Match Route)[â](#proxy-grpc-web-prefix-match-route "Direct link to Proxy gRPC-Web (Prefix Match Route)")

The following examples demonstrate how to configure and use the `grpc-web` plugin with the gRPC-Web client set up previously.

Create a route with the `grpc-web` plugin as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id": "grpc-web-route",
  "uri": "/grpc/web/*",
  "plugins": {
    "grpc-web": {}
  },
  "upstream": {
    "scheme": "grpc",
    "type": "roundrobin",
    "nodes": {
      "192.168.10.103:9000": 1
    }
  }
}'
```

â¶ Configure the `uri` to prefix-match the route requested in `client.js`.

â· Enable the `grpc-web` plugin.

â¸ Set the upstream scheme to `grpc`.

â¹ Replace with your upstream server address.

understand the uri

In APISIX versions prior to 3.15.0 and API7 Enterprise versions prior to 3.8.21, the route URI must use a prefix match because gRPC-Web clients include the package name, service name, and method name in the request URI. Using an absolute URI match in these versions will prevent the request from matching the route. [Absolute URI routes](#proxy-grpc-web-absolute-uri) are supported in later versions.

In this example, the route URI must be configured as `/grpc/web/*` to correctly match client requests such as `/grpc/web/hello.HelloService/SayHello`. Using a broader prefix like `/grpc/*` would prevent the gateway from correctly extracting the full service path, resulting in errors such as `unknown service web/hello.HelloService`.

Run the client to send requests to the gateway route:

```
node client.js
```

You should see a reply from the upstream gRPC server:

```
Response headers: {
  ...
  'access-control-allow-origin': '*',
  'access-control-expose-headers': 'grpc-message,grpc-status'
}
Response headers: {
  ...
  'access-control-allow-origin': '*',
  'access-control-expose-headers': 'grpc-message,grpc-status'
}
reply: hello jack
```

### Proxy gRPC-Web (Absolute URI)[â](#proxy-grpc-web-absolute-uri "Direct link to Proxy gRPC-Web (Absolute URI)")

This example applies to APISIX 3.15.0 and later, and API7 Enterprise 3.8.21 and later.

When an absolute URI is used, the gateway does not automatically strip the URI path prefix. To forward requests correctly to the upstream gRPC server, use the `proxy-rewrite` plugin to adjust the request path.

Create a route with the `grpc-web` plugin as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id": "grpc-web-route",
  "uri": "/grpc/web/hello.HelloService/SayHello",
  "plugins": {
    "grpc-web": {},
    "proxy-rewrite": {
      "uri": "/hello.HelloService/SayHello",
      "set_ngx_uri": "true"
    }
  },
  "upstream": {
    "scheme": "grpc",
    "type": "roundrobin",
    "nodes": {
      "192.168.10.103:9000": 1
    }
  }
}'
```

â¶ Configure the `uri` to use the absolute path, including the base prefix and the gRPC full service path.

â· Configure `proxy-rewrite` to rewrite the path and strip the route prefix.

â¸ Set `set_ngx_uri` to `true` to update the requested path to the URI defined in the `proxy-rewrite` plugin. Without this setting, the gateway will not correctly forward the request to the upstream, resulting in errors such as `unknown service grpc/web/hello.HelloService`.

â¹ Set the upstream scheme to `grpc`.

âº Replace with your upstream server address.

Run the client to send requests to the gateway route:

```
node client.js
```

You should see a reply from the upstream gRPC server:

```
Response headers: {
  ...
  'access-control-allow-origin': '*',
  'access-control-expose-headers': 'grpc-message,grpc-status'
}
Response headers: {
  ...
  'access-control-allow-origin': '*',
  'access-control-expose-headers': 'grpc-message,grpc-status'
}
reply: hello jack
```
