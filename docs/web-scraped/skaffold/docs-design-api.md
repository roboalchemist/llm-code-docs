# Source: https://skaffold.dev/docs/design/api/

Title: Skaffold API

URL Source: https://skaffold.dev/docs/design/api/

Published Time: Thu, 13 Nov 2025 20:49:27 GMT

Markdown Content:
Skaffold API | Skaffold
===============
[Skaffold](https://skaffold.dev/)

*   [](https://github.com/GoogleContainerTools/skaffold)
*   [](https://skaffold.dev/docs/resources/#community)
*   [](https://groups.google.com/forum/#!forum/skaffold-users)
*   [Documentation](https://skaffold.dev/docs/)
*   [skaffold.yaml](https://skaffold.dev/docs/references/yaml/)
*   [Versions](https://skaffold.dev/docs/design/api/#)[v1.0](https://skaffold-v1.web.app/)[v2.0](https://skaffold-v2.web.app/) 

*   [Documentation](https://skaffold.dev/docs/ "Skaffold 2.0 Documentation")
    *   - [x] [Installing Skaffold](https://skaffold.dev/docs/install/) 
    *   - [x] [Upgrading from Skaffold v1 to Skaffold v2 [NEW]](https://skaffold.dev/docs/upgrading/) 
    *   - [x] [Quickstart](https://skaffold.dev/docs/quickstart/) 
    *   - [x] [Guides](https://skaffold.dev/docs/workflows/) 
        *   - [x] [Getting Started With Your Project](https://skaffold.dev/docs/workflows/getting-started-with-your-project/) 
        *   - [x] [Continuous Development](https://skaffold.dev/docs/workflows/dev/ "skaffold dev") 
        *   - [x] [Debugging](https://skaffold.dev/docs/workflows/debug/ "Debugging With Skaffold") 
        *   - [x] [Continuous Delivery](https://skaffold.dev/docs/workflows/ci-cd/) 
        *   - [x] [Managing ARM workloads [NEW]](https://skaffold.dev/docs/workflows/handling-platforms/) 

    *   - [x] [Skaffold Pipeline Stages](https://skaffold.dev/docs/pipeline-stages/) 
    *   - [x] [Init](https://skaffold.dev/docs/init/) 
    *   - [x] [Build](https://skaffold.dev/docs/builders/) 
        *   - [x] [Builder types](https://skaffold.dev/docs/builders/builder-types/) 
            *   - [x] [Docker](https://skaffold.dev/docs/builders/builder-types/docker/ "Docker Build") 
            *   - [x] [Jib](https://skaffold.dev/docs/builders/builder-types/jib/ "Jib Build") 
            *   - [x] [Bazel](https://skaffold.dev/docs/builders/builder-types/bazel/) 
            *   - [x] [Custom](https://skaffold.dev/docs/builders/builder-types/custom/ "Custom Build Script") 
            *   - [x] [Buildpacks](https://skaffold.dev/docs/builders/builder-types/buildpacks/ "Cloud Native Buildpacks") 
            *   - [x] [ko](https://skaffold.dev/docs/builders/builder-types/ko/) 

        *   - [x] [Environments](https://skaffold.dev/docs/builders/build-environments/ "Build environments") 
            *   - [x] [Local build](https://skaffold.dev/docs/builders/build-environments/local/) 
            *   - [x] [In cluster](https://skaffold.dev/docs/builders/build-environments/in-cluster/ "In cluster build") 
            *   - [x] [Google Cloud Build](https://skaffold.dev/docs/builders/build-environments/cloud-build/) 

        *   - [x] [Cross/multi-platform](https://skaffold.dev/docs/builders/cross-platform/ "Cross-platform and multi-platform build support") 

    *   - [x] [Deploy [UPDATED]](https://skaffold.dev/docs/deployers/) 
        *   - [x] [Kubectl](https://skaffold.dev/docs/deployers/kubectl/) 
        *   - [x] [Kpt [UPDATED]](https://skaffold.dev/docs/deployers/kpt/) 
        *   - [x] [Helm [UPDATED]](https://skaffold.dev/docs/deployers/helm/) 
        *   - [x] [Docker](https://skaffold.dev/docs/deployers/docker/) 
        *   - [x] [Google Cloud Run [NEW]](https://skaffold.dev/docs/deployers/cloudrun/) 

    *   - [x] [Render [NEW]](https://skaffold.dev/docs/renderers/) 
        *   - [x] [Raw YAML](https://skaffold.dev/docs/renderers/rawyaml/) 
        *   - [x] [Kpt [NEW]](https://skaffold.dev/docs/renderers/kpt/) 
        *   - [x] [Kustomize](https://skaffold.dev/docs/renderers/kustomize/) 
        *   - [x] [Helm [UPDATED]](https://skaffold.dev/docs/renderers/helm/) 

    *   - [x] [Test](https://skaffold.dev/docs/testers/) 
        *   - [x] [Container Structure Test](https://skaffold.dev/docs/testers/structure/) 
        *   - [x] [Custom Test](https://skaffold.dev/docs/testers/custom/) 

    *   - [x] [Tag](https://skaffold.dev/docs/taggers/) 
    *   - [x] [File Sync](https://skaffold.dev/docs/filesync/) 
    *   - [x] [Log Tailing](https://skaffold.dev/docs/log-tailing/) 
    *   - [x] [Verify [NEW]](https://skaffold.dev/docs/verify/) 
    *   - [x] [Deploy Status Checking](https://skaffold.dev/docs/status-check/) 
    *   - [x] [Lifecycle Hooks](https://skaffold.dev/docs/lifecycle-hooks/) 
    *   - [x] [Port Forwarding](https://skaffold.dev/docs/port-forwarding/) 
    *   - [x] [Cleanup](https://skaffold.dev/docs/cleanup/) 
    *   - [x] [Custom Actions](https://skaffold.dev/docs/custom-actions/) 
    *   - [x] [Architecture and Design](https://skaffold.dev/docs/design/) 
        *   - [x] [Skaffold Pipeline](https://skaffold.dev/docs/design/config/) 
        *   - [x] [Global Configuration](https://skaffold.dev/docs/design/global-config/) 
        *   - [x] [Skaffold API](https://skaffold.dev/docs/design/api/) 

    *   - [x] [Environment Management](https://skaffold.dev/docs/environment/) 
        *   - [x] [Load ENV from a file](https://skaffold.dev/docs/environment/env-file/ "Load environment variables from a file") 
        *   - [x] [Local Cluster](https://skaffold.dev/docs/environment/local-cluster/) 
        *   - [x] [Image Repository Handling](https://skaffold.dev/docs/environment/image-registries/) 
        *   - [x] [Profiles](https://skaffold.dev/docs/environment/profiles/) 
        *   - [x] [Kube-context Activation](https://skaffold.dev/docs/environment/kube-context/) 
        *   - [x] [Templated Fields](https://skaffold.dev/docs/environment/templating/) 

    *   - [x] [Tutorials](https://skaffold.dev/docs/tutorials/) 
        *   - [x] [Build and deploy on Kubernetes](https://skaffold.dev/docs/tutorials/build-and-deploy-to-kubernetes/ "Use Skaffold to build and deploy an application on Kubernetes") 
        *   - [x] [Manage CRDs w/ Skaffold - Configuring Which K8s Resources & Fields Skaffold Manages](https://skaffold.dev/docs/tutorials/skaffold-resource-selector/) 
        *   - [x] [Build Dependencies](https://skaffold.dev/docs/tutorials/artifact-dependencies/ "Defining dependencies between artifacts") 
        *   - [x] [Config Dependencies](https://skaffold.dev/docs/tutorials/config-dependencies/ "Importing configuration as dependencies") 
        *   - [x] [Custom Build Script](https://skaffold.dev/docs/tutorials/custom-builder/ "Building Artifacts with a Custom Build Script") 
        *   - [x] [Developer Journey](https://skaffold.dev/docs/tutorials/developer-journey/ "Developer Journey with Buildpacks") 
        *   - [x] [Go integration test coverage profiles](https://skaffold.dev/docs/tutorials/go-integration-coverage/) 
        *   - [x] [Overriding the buildpacks run image](https://skaffold.dev/docs/tutorials/buildpacks-override/ "Override the run image in buildpacks builder") 
        *   - [x] [Skaffold in CI/CD](https://skaffold.dev/docs/tutorials/ci_cd/ "Using Skaffold for CI/CD with GitLab") 

    *   - [x] [References](https://skaffold.dev/docs/references/) 
        *   - [x] [CLI](https://skaffold.dev/docs/references/cli/) 
        *   - [x] [skaffold.yaml](https://skaffold.dev/docs/references/yaml/) 
        *   - [x] [API](https://skaffold.dev/docs/references/api/) 
            *   - [x] [gRPC API](https://skaffold.dev/docs/references/api/grpc/) 
            *   - [x] [HTTP API](https://skaffold.dev/docs/references/api/swagger/) 

        *   - [x] [API V2](https://skaffold.dev/docs/references/api-v2/) 
            *   - [x] [gRPC API](https://skaffold.dev/docs/references/api-v2/grpc/) 
            *   - [x] [HTTP API](https://skaffold.dev/docs/references/api-v2/swagger/) 

        *   - [x] [Privacy Settings](https://skaffold.dev/docs/references/privacy/) 
        *   - [x] [Deprecation Policy](https://skaffold.dev/docs/references/deprecation/) 

    *   - [x] [Resources](https://skaffold.dev/docs/resources/) 
        *   - [x] [Skaffold Feedback](https://skaffold.dev/docs/resources/feedback/) 
        *   - [x] [Telemetry](https://skaffold.dev/docs/resources/telemetry/) 

[Edit this page](https://github.com/GoogleContainerTools/skaffold/edit/main/docs-v2/content/en/docs/design/api.md)[Create documentation issue](https://github.com/GoogleContainerTools/skaffold/issues/new?title=Skaffold%20API)

**Maturity**[`beta`](https://skaffold.dev/docs/references/deprecation)
**Applicable**[`dev`](https://skaffold.dev/docs/references/cli#skaffold-dev)[`debug`](https://skaffold.dev/docs/references/cli#skaffold-debug)
**Not applicable**[`run`](https://skaffold.dev/docs/references/cli#skaffold-run)[`build`](https://skaffold.dev/docs/references/cli#skaffold-build)[`test`](https://skaffold.dev/docs/references/cli#skaffold-test)[`deploy`](https://skaffold.dev/docs/references/cli#skaffold-deploy)[`render`](https://skaffold.dev/docs/references/cli#skaffold-render)

*   [Connecting to the Skaffold API](https://skaffold.dev/docs/design/api/#connecting-to-the-skaffold-api)
*   [gRPC Server](https://skaffold.dev/docs/design/api/#grpc-server)
    *   [HTTP server](https://skaffold.dev/docs/design/api/#http-server)

*   [API Structure](https://skaffold.dev/docs/design/api/#api-structure)
    *   [Event API](https://skaffold.dev/docs/design/api/#event-api)
    *   [State API](https://skaffold.dev/docs/design/api/#state-api)
    *   [Control API](https://skaffold.dev/docs/design/api/#control-api)

1.   [Documentation](https://skaffold.dev/docs/)
2.   [Architecture and Design](https://skaffold.dev/docs/design/)
3.   Skaffold API

Skaffold API beta
=================

When running [`skaffold dev`](https://skaffold.dev/docs/workflows/dev/) or [`skaffold debug`](https://skaffold.dev/docs/workflows/debug/), Skaffold starts a server that exposes an API over the lifetime of the Skaffold process. Besides the CLI, this API is the primary way tools like IDEs integrate with Skaffold for **retrieving information about the pipeline** and for **controlling the phases in the pipeline**.

To retrieve information about the Skaffold pipeline, the Skaffold API provides two main functionalities:

*   A [streaming event log](https://skaffold.dev/docs/design/api/#events-api) created from the different phases in a pipeline run, and

*   A snapshot of the [overall state](https://skaffold.dev/docs/design/api/#state-api) of the pipeline at any given time during the run.

To control the individual phases of the Skaffold, the Skaffold API provides [fine-grained control](https://skaffold.dev/docs/design/api/#control-api) over the individual phases of the pipeline (build, deploy, and sync).

Connecting to the Skaffold API
------------------------------

The Skaffold API is `gRPC` based, and it is also exposed via the gRPC gateway as a JSON over HTTP service.

The API can be enabled via setting the `--rpc-port` or `--rpc-http-port` flags (or both) depending on whether you want to enable the gRPC API or the HTTP REST API, respectively.

#### Note

 The `--enable-rpc` flag is now deprecated in favor of `--rpc-port` and `--rpc-http-port` flags. 

For reference, we generate the server’s [gRPC service definitions and message protos](https://skaffold.dev/docs/references/api/grpc/) as well as the [Swagger based HTTP API Spec](https://skaffold.dev/docs/references/api/swagger/).

gRPC Server
-----------

The gRPC API can be started by specifying the `--rpc-port` flag. If the specified port is not available, Skaffold will exit with failure.

### HTTP server

The HTTP REST API can be started by specifying the `--rpc-http-port` flag. If the specified port is not available, Skaffold will exit with failure.

Starting the HTTP REST API will also start the gRPC API as it proxies the requests to the gRPC API. By default, Skaffold chooses a random available port for gRPC, but it can be customized (see below).

#### Creating a gRPC Client

To connect to the `gRPC` server at the specified port, create a client using the following code snippet.

#### Note

 The skaffold gRPC server is not compatible with HTTPS, so connections need to be marked as insecure with `grpc.WithInsecure()`

```golang
import (
  "log"
  pb "github.com/GoogleContainerTools/skaffold/proto/v1"
  "google.golang.org/grpc"
)

func main(){
  conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure())
  if err != nil {
    log.Fatalf("fail to dial: %v", err)
  }
  defer conn.Close()
  client := pb.NewSkaffoldServiceClient(conn)
}
```

API Structure
-------------

Skaffold’s API exposes the three main endpoints:

*   Event API - continuous stream of lifecycle events
*   State API - retrieve the current state
*   Control API - control build/deploy/sync

### Event API

Skaffold provides a continuous development mode, [`skaffold dev`](https://skaffold.dev/docs/workflows/dev/), which rebuilds and redeploys your application on changes. In a single development loop, one or more container images may be built and deployed.

Skaffold exposes events for clients to be notified when phases within a development loop start, succeed, or fail. Tools that integrate with Skaffold can use these events to kick off parts of a development workflow depending on them.

Example scenarios:

*   port-forwarding events are used by Cloud Code to automatically attach debuggers to running containers.
*   using an event indicating a frontend service has been deployed and port-forwarded successfully to kick off a suite of Selenium tests against the newly deployed service.

**Event API Contract**

| protocol | endpoint | encoding |
| --- | --- | --- |
| HTTP | `http://localhost:{HTTP_RPC_PORT}/v1/events` | newline separated JSON using chunk transfer encoding over HTTP |
| gRPC | `client.Events(ctx)` method on the [`SkaffoldService`](https://skaffold.dev/docs/references/api/#skaffoldservice) | protobuf 3 over HTTP |

**Examples**

Using `curl` and `HTTP_RPC_PORT=50052`, an example output of a `skaffold dev` execution on our [getting-started example](https://github.com/GoogleContainerTools/skaffold/tree/main/examples/getting-started)

```bash
curl localhost:50052/v1/events
{"result":{"timestamp":"2019-10-16T18:26:11.385251549Z","event":{"metaEvent":{"entry":"Starting Skaffold: {Version:v0.39.0-16-g5bb7c9e0 ConfigVersion:skaffold/v1 GitVersion: GitCommit:5bb7c9e078e4d522a5ffc42a2f1274fd17d75902 GitTreeState:dirty BuildDate:2019-10-03T15:01:29Z GoVersion:go1.13rc1 Compiler:gc Platform:linux/amd64}"}}}}
{"result":{"timestamp":"2019-10-16T18:26:11.436231589Z","event":{"buildEvent":{"artifact":"gcr.io/k8s-skaffold/skaffold-example","status":"In Progress"}},"entry":"Build started for artifact gcr.io/k8s-skaffold/skaffold-example"}}
{"result":{"timestamp":"2019-10-16T18:26:12.010124246Z","event":{"buildEvent":{"artifact":"gcr.io/k8s-skaffold/skaffold-example","status":"Complete"}},"entry":"Build completed for artifact gcr.io/k8s-skaffold/skaffold-example"}}
{"result":{"timestamp":"2019-10-16T18:26:12.391721823Z","event":{"deployEvent":{"status":"In Progress"}},"entry":"Deploy started"}}
{"result":{"timestamp":"2019-10-16T18:26:12.847239740Z","event":{"deployEvent":{"status":"Complete"}},"entry":"Deploy complete"}}
..
```

To get events from the API using `gRPC`, first create a [`gRPC` client](https://skaffold.dev/docs/design/api/#creating-a-grpc-client). then, call the `client.Events()` method:

```golang
func main() {
  ctx, ctxCancel := context.WithCancel(context.Background())
  defer ctxCancel()
  // `client` is a gRPC client with connection to localhost:50051.
  logStream, err := client.Events(ctx, &empty.Empty{})
  if err != nil {
  	log.Fatalf("could not get events: %v", err)
  }
  for {
  	entry, err := logStream.Recv()
  	if err == io.EOF {
  		break
  	}
  	if err != nil {
  		log.Fatal(err)
  	}
  	log.Println(entry)
  }
}
```

Each [Entry](https://skaffold.dev/docs/references/api/grpc/#proto.LogEntry) in the log contains an [Event](https://skaffold.dev/docs/references/api/grpc/#proto.Event) in the `LogEntry.Event` field and a string description of the event in `LogEntry.entry` field.

### State API

The State API provides a snapshot of the current state of the following components:

*   build state per artifacts
*   deploy state
*   file sync state
*   status check state per resource
*   port-forwarded resources

**State API Contract**

| protocol | endpoint | encoding |
| --- | --- | --- |
| HTTP | `http://localhost:{HTTP_RPC_PORT}/v1/state` | newline separated JSON using chunk transfer encoding over HTTP |
| gRPC | `client.GetState(ctx)` method on the [`SkaffoldService`](https://skaffold.dev/docs/references/api/grpc/#skaffoldservice) | protobuf 3 over HTTP |

**Examples**

Using `curl` and `HTTP_RPC_PORT=50052`, an example output of a `skaffold dev` execution on our [microservices example](https://github.com/GoogleContainerTools/skaffold/tree/main/examples/microservices)

```bash
curl localhost:50052/v1/state | jq
 {
   "buildState": {
     "artifacts": {
       "gcr.io/k8s-skaffold/leeroy-app": "Complete",
       "gcr.io/k8s-skaffold/leeroy-web": "Complete"
     }
   },
   "deployState": {
     "status": "Complete"
   },
   "forwardedPorts": {
     "9000": {
       "localPort": 9000,
       "remotePort": 8080,
       "namespace": "default",
       "resourceType": "deployment",
       "resourceName": "leeroy-web"
     },
     "50055": {
       "localPort": 50055,
       "remotePort": 50051,
       "namespace": "default",
       "resourceType": "service",
       "resourceName": "leeroy-app"
     }
   },
   "statusCheckState": {
     "status": "Succeeded"
   },
   "fileSyncState": {
     "status": "Not Started"
   }
 }
```

To retrieve the state from the server using `gRPC`, first create [`gRPC` client](https://skaffold.dev/docs/design/api/#creating-a-grpc-client). Then, call the `client.GetState()` method:

```golang
func main() {
  // Create a gRPC client connection to localhost:50051.
  // See code above
  ctx, ctxCancel := context.WithCancel(context.Background())
  defer ctxCancel()
  grpcState, err = client.GetState(ctx, &empty.Empty{})
  ...
}
```

### Control API

By default, [`skaffold dev`](https://skaffold.dev/docs/workflows/dev/) will automatically build artifacts, deploy manifests and sync files on every source code change. However, this behavior can be paused and individual actions can be gated off by user input through the Control API.

With this API, users can tell Skaffold to wait for user input before performing any of these actions, even if the requisite files were changed on the filesystem. By doing so, users can “queue up” changes while they are iterating locally, and then have Skaffold rebuild and redeploy only when asked. This can be very useful when builds are happening more frequently than desired, when builds or deploys take a long time or are otherwise very costly, or when users want to integrate other tools with `skaffold dev`.

The automation can be turned off or on using the Control API, or with `auto-build` flag for building, `auto-deploy` flag for deploys, and the `auto-sync` flag for file sync. If automation is turned off for a phase, Skaffold will wait for a request to the Control API before executing the associated action.

Each time a request is sent to the Control API by the user, the specified actions in the payload are executed immediately. This means that _even if there are new file changes_, Skaffold will wait for another user request before executing any of the given actions again.

**Control API Contract**

| protocol | endpoint |
| --- | --- |
| HTTP, method: POST | `http://localhost:{HTTP_RPC_PORT}/v1/execute`, the [Execution Service](https://skaffold.dev/docs/references/api/swagger/#/SkaffoldService/Execute) |
| gRPC | `client.Execute(ctx)` method on the [`SkaffoldService`](https://skaffold.dev/docs/references/api/grpc/#skaffoldservice) |
| HTTP, method: PUT | `http://localhost:{HTTP_RPC_PORT}/v1/build/auto_execute`, the [Auto Build Service](https://skaffold.dev/docs/references/api/swagger/#/SkaffoldService/AutoBuild) |
| gRPC | `client.AutoBuild(ctx)` method on the [`SkaffoldService`](https://skaffold.dev/docs/references/api/grpc/#skaffoldservice) |
| HTTP, method: PUT | `http://localhost:{HTTP_RPC_PORT}/v1/sync/auto_execute`, the [Auto Sync Service](https://skaffold.dev/docs/references/api/swagger/#/SkaffoldService/AutoSync) |
| gRPC | `client.AutoSync(ctx)` method on the [`SkaffoldService`](https://skaffold.dev/docs/references/api/grpc/#skaffoldservice) |
| HTTP, method: PUT | `http://localhost:{HTTP_RPC_PORT}/v1/deploy/auto_execute`, the [Auto Deploy Service](https://skaffold.dev/docs/references/api/swagger/#/SkaffoldService/AutoDeploy) |
| gRPC | `client.AutoDeploy(ctx)` method on the [`SkaffoldService`](https://skaffold.dev/docs/references/api/grpc/#skaffoldservice) |

**Examples**

Using our [Quickstart example](https://skaffold.dev/docs/quickstart/), we can start skaffold with `skaffold dev --auto-build=false`. When we change `main.go`, Skaffold will notice file changes but will not rebuild the image until it receives a request to the Control API with `{"build": true}`:

```bash
curl -X POST http://localhost:50052/v1/execute -d '{"build": true}'
```

At this point, Skaffold will wait to deploy the newly built image until we invoke the Control API with `{"deploy": true}`:

```bash
curl -X POST http://localhost:50052/v1/execute -d '{"deploy": true}'
```

These steps can also be combined into a single request:

```bash
curl -X POST http://localhost:50052/v1/execute -d '{"build": true, "deploy": true}'
```

We can make Skaffold start noticing file changes automatically again by issuing the requests:

```bash
curl -X PUT http://localhost:50052/v1/build/auto_execute -d '{"enabled": true}'
curl -X PUT http://localhost:50052/v1/deploy/auto_execute -d '{"enabled": true}'
```

To access the Control API via the `gRPC`, create [`gRPC` client](https://skaffold.dev/docs/design/api/#creating-a-grpc-client) as before. Then, use the `client.Execute()` method with the desired payload to trigger it once:

```golang
func main() {
    ctx, ctxCancel := context.WithCancel(context.Background())
    defer ctxCancel()
    // `client` is the gRPC client with connection to localhost:50051.
    _, err = client.Execute(ctx, &pb.UserIntentRequest{
        Intent: &pb.Intent{
            Build:  true,
            Sync:   true,
            Deploy: true,
        },
    })
    if err != nil {
        log.Fatalf("error when trying to execute phases: %v", err)
    }
}
```

Use the `client.AutoBuild()`,`client.AutoSync()` and `client.AutoDeploy()` method to enable or disable auto build, auto sync and auto deploy:

```golang
func main() {
    ctx, ctxCancel := context.WithCancel(context.Background())
    defer ctxCancel()
    // `client` is the gRPC client with connection to localhost:50051.
    _, err = client.AutoBuild(ctx, &pb.TriggerRequest{
		State: &pb.TriggerState{
			Val: &pb.TriggerState_Enabled{
				Enabled: true,
			},
		},
	})    if err != nil {
        log.Fatalf("error when trying to auto trigger phases: %v", err)
    }
}
```

 Last modified November 13, 2025: [chore: Skaffold 2.17 release (#9912) (561ce51e)](https://github.com/GoogleContainerTools/skaffold/commit/561ce51e1e2c4174b375e694a676585cea7c2b65)

*   [](https://github.com/GoogleContainerTools/skaffold)
*   [](https://skaffold.dev/docs/resources/#community)
*   [](https://groups.google.com/forum/#!forum/skaffold-users)
*   [](https://forms.gle/BMTbGQXLWSdn7vEs6)

© 2025 Skaffold Authors All Rights Reserved

[Privacy Policy](https://policies.google.com/privacy)
