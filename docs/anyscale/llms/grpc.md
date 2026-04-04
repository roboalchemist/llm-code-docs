# Source: https://docs.anyscale.com/services/grpc.md

# Use gRPC with Anyscale services

[View Markdown](/services/grpc.md)

# Use gRPC with Anyscale services

This tutorial walks you through deploying Ray Serve applications using gRPC in an Anyscale service. You can find all the code in this tutorial in the [GitHub repo](https://github.com/anyscale/docs_examples/tree/942d08de592d2011fdd647566adbb84a174e5c7e/grpc_services_v2).

note

Anyscale clouds on Google Cloud require Ray 2.38.0 or later.

For more information on integrating gRPC services into Ray Serve apps, see the [Ray Serve gRPC service docs](https://docs.ray.io/en/latest/serve/advanced-guides/grpc-guide.html).

important

The Ray Serve docs focus on local development and testing. The pattern `grpc.insecure_channel("localhost:9000")` used for defining client code doesn't work on Anyscale. You must always query Anyscale services using secure connections. See [Send test requests to the service](#test-requests).

warning

gRPC services aren't compatible with high-throughput serving. Don't enable `RAY_SERVE_THROUGHPUT_OPTIMIZED=1` for services that use `grpc_options`. See [High-throughput serving](/runtime/serve.md#high-throughput).

## Build an image with gRPC protobufs and servicer functions[​](#build-image "Direct link to Build an image with gRPC protobufs and servicer functions")

To run gRPC services, Ray Serve needs to access gRPC servicer functions. To make them available in an Anyscale service, you must build a container image that includes both your custom Protocol Buffers and Ray Serve application code.

First, define a `user_defined_protos.proto` file like the following:

```
syntax = "proto3";

option java_multiple_files = true;
option java_package = "io.ray.examples.user_defined_protos";
option java_outer_classname = "UserDefinedProtos";

package userdefinedprotos;

message UserDefinedMessage {
  string name = 1;
}

message UserDefinedResponse {
  string greeting = 1;
}

service UserDefinedService {
  rpc __call__(UserDefinedMessage) returns (UserDefinedResponse);
}
```

Next, define a Ray Serve application in `deployment.py`:

```
from ray import serve
from user_defined_protos_pb2 import UserDefinedMessage, UserDefinedResponse


@serve.deployment
class GrpcDeployment:
    def __call__(self, user_message: UserDefinedMessage) -> UserDefinedResponse:
        greeting = f"Hello {user_message.name}!"
        user_response = UserDefinedResponse(greeting=greeting)
        return user_response


grpc_app = GrpcDeployment.options(name="grpc-deployment").bind()
```

Define the [`Dockerfile`](https://github.com/anyscale/docs_examples/blob/942d08de592d2011fdd647566adbb84a174e5c7e/grpc_services_v2/Dockerfile) with the protobuf and deployment definitions:

```
# Use Anyscale base image
FROM anyscale/ray:2.38.0-py310

WORKDIR /home/ray

# Copy protobuf and deployment definitions into the Docker image
COPY user_defined_protos.proto /home/ray/user_defined_protos.proto
COPY deployment.py /home/ray/deployment.py

# Add working directory into Python path so any nodes can import them
ENV PYTHONPATH=/home/ray

# Ensure that the protobuf version is up to date
RUN pip install --upgrade protobuf

# Build Python code from .proto file
RUN python -m grpc_tools.protoc -I=. --python_out=. --grpc_python_out=. ./user_defined_protos.proto
```

Create these three files locally, then build and push the Docker image with the following command:

```
# Build the Docker image
docker build . -t my-registry/my-image:tag

# Push the Docker image to your registry
docker push my-registry/my-image:tag
```

### Deploy a service using the custom Docker image[​](#deploy-custom "Direct link to Deploy a service using the custom Docker image")

Create a service definition file called `service.yaml`:

note

Anyscale uses port `9000`. You can't use the `grpc_options.port` option on Anyscale to change the port.

```
name: grpc-service
image_uri: REGISTRY/IMAGE:TAG  # Replace with your image
cloud: CLOUD_NAME  # Replace with your cloud name

grpc_options:
  service_names:
    # The prefix of the fully qualified gRPC service name in your .proto file.
    - userdefinedprotos.UserDefinedService
  grpc_servicer_functions:
    - user_defined_protos_pb2_grpc.add_UserDefinedServiceServicer_to_server

applications:
  - name: grpc_app
    route_prefix: /grpc_app
    import_path: deployment:grpc_app
    runtime_env: { }
```

Ensure `grpc_options.service_names` matches the service name in the `.proto` file.

note

`grpc_options.service_names` is used to route gRPC services based on their prefixes. Often, you can provide the package name (for example, `userdefinedprotos`) followed by a `.` and the service name (for example, `UserDefinedService`). If your `.proto` file contains multiple gRPC services, you can use the package name (for example, `userdefinedprotos`) for routing, as all services in the same `.proto` file share the same package name as a prefix.

Deploy the Anyscale service:

```
anyscale service deploy -f service.yaml
```

Your terminal displays the following message. Visit the provided URL to open the Anyscale console and view the service dashboard. Record the bearer token and URL from the example query for the following step.

```
% anyscale service deploy -f service.yaml
(anyscale +1.8s) Starting new service 'grpc-service'.
(anyscale +4.1s) Service 'grpc-service' deployed.
(anyscale +4.1s) View the service in the UI: 'EXAMPLE_UI_URL'
(anyscale +4.1s) Query the service once it's running using the following curl command:
(anyscale +4.1s) curl -H 'Authorization: Bearer EXAMPLE_API_TOKEN' EXAMPLE_BASE_URL
```

Wait until the service is running to continue. You can view the status in the Anyscale console or run the following command:

```
anyscale service status --name grpc-service
```

### Send test requests to the service[​](#test-requests "Direct link to Send test requests to the service")

Once the service is **Running**, query it with your API token and base URL.

Create a `test_client.py` script using the following example code. You must update the code to include the URL and bearer token for your service. The Anyscale console displays these values in sample queries. See [Get an example query](/services/query.md#example-query).

note

You must use secure channels when communicating with Anyscale services. Anyscale refuses requests to establish insecure connections, for example using `grpc.insecure_channel()`.

```
import grpc
from user_defined_protos_pb2_grpc import UserDefinedServiceStub
from user_defined_protos_pb2 import UserDefinedMessage


# Replace URL and token with your own.
url = "grpc-service-XXXXX.cld-XXXXXXXXXXXXXXXX.s.anyscaleuserdata.com"
token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

credentials = grpc.ssl_channel_credentials()
channel = grpc.secure_channel(url, credentials)
stub = UserDefinedServiceStub(channel)
request = UserDefinedMessage(name="Ray")
auth_token_metadata = ("authorization", f"Bearer {token}")
metadata = (
    ("application", "grpc_app"),
    auth_token_metadata,
)
response, call = stub.__call__.with_call(request=request, metadata=metadata)
print(call.trailing_metadata())  # Request ID is returned in the trailing metadata
print("Output type:", type(response))  # Response is a type of UserDefinedMessage
print("Full output:", response)
```

Run the script to test the service:

```
python test_client.py
```

Your terminal displays a response such as the following:

```
(_Metadatum(key='request_id', value='ff6e0810-dd22-488c-ad0e-9f9949bed5be'),)
Output type: <class 'user_defined_protos_pb2.UserDefinedResponse'>
Full output: greeting: "Hello Ray!"
```
