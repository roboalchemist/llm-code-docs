# Source: https://skaffold.dev/docs/port-forwarding/

Title: Port Forwarding

URL Source: https://skaffold.dev/docs/port-forwarding/

Markdown Content:
Port Forwarding | Skaffold
===============
[Skaffold](https://skaffold.dev/)

*   [](https://github.com/GoogleContainerTools/skaffold)
*   [](https://skaffold.dev/docs/resources/#community)
*   [](https://groups.google.com/forum/#!forum/skaffold-users)
*   [Documentation](https://skaffold.dev/docs/)
*   [skaffold.yaml](https://skaffold.dev/docs/references/yaml/)
*   [Versions](https://skaffold.dev/docs/port-forwarding/#)[v1.0](https://skaffold-v1.web.app/)[v2.0](https://skaffold-v2.web.app/) 

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

[Edit this page](https://github.com/GoogleContainerTools/skaffold/edit/main/docs-v2/content/en/docs/port-forwarding.md)[Create documentation issue](https://github.com/GoogleContainerTools/skaffold/issues/new?title=Port%20Forwarding)

**Applicable**[`dev`](https://skaffold.dev/docs/references/cli#skaffold-dev)[`debug`](https://skaffold.dev/docs/references/cli#skaffold-debug)
**Not applicable**[`run`](https://skaffold.dev/docs/references/cli#skaffold-run)[`build`](https://skaffold.dev/docs/references/cli#skaffold-build)[`test`](https://skaffold.dev/docs/references/cli#skaffold-test)[`deploy`](https://skaffold.dev/docs/references/cli#skaffold-deploy)[`render`](https://skaffold.dev/docs/references/cli#skaffold-render)

*       *   [Automatic Port Forwarding](https://skaffold.dev/docs/port-forwarding/#automatic-port-forwarding)
    *   [User-Defined Port Forwarding](https://skaffold.dev/docs/port-forwarding/#UDPF)

1.   [Documentation](https://skaffold.dev/docs/)
2.   Port Forwarding

Port Forwarding
===============

Skaffold has built-in support for forwarding ports from exposed Kubernetes resources on your cluster to your local machine when running in `dev`, `debug`, `deploy`, or `run` modes.

### Automatic Port Forwarding

Skaffold supports automatic port forwarding the following classes of resources:

*   `user`: explicit port-forwards defined in the `skaffold.yaml` (called [_user-defined port forwards_](https://skaffold.dev/docs/port-forwarding/#UDPF))
*   `services`: ports exposed on services deployed by Skaffold.
*   `debug`: debugging ports as enabled by `skaffold debug` for Skaffold-built images.
*   `pods`: all `containerPort`s on deployed pods for Skaffold-built images.

Skaffold enables certain classes of forwards by default depending on the Skaffold command used. These defaults can be overridden with the `--port-forward` flag, and port-forwarding can be disabled with `--port-forward=off`.

| Command-line | Default modes |
| --- | --- |
| `skaffold dev` | `user` |
| `skaffold dev --port-forward` | `user`, `services` |
| `skaffold dev --port-forward=off` | _no ports forwarded_ |
| `skaffold debug` | `user`, `debug` |
| `skaffold debug --port-forward` | `user`, `services`, `debug`(_see note below_) |
| `skaffold debug --port-forward=off` | _no ports forwarded_ |
| `skaffold deploy` | `off` |
| `skaffold deploy --port-forward` | `user`, `services` |
| `skaffold run` | `off` |
| `skaffold run --port-forward` | `user`, `services` |

#### Compatibility Note

 Note that `skaffold debug --port-forward` previously enabled the equivalent of `pods` as Skaffold did not have an equivalent of `debug`. We have replaced `pods` as it caused confusion. 

### User-Defined Port Forwarding

Users can define additional resources to port forward in the skaffold config, to enable port forwarding for

*   additional resource types supported by `kubectl port-forward` e.g.`Deployment`or `ReplicaSet`.
*   additional pods running containers which run images not built by Skaffold.

For example:

```yaml
portForward:
- resourceType: deployment
  resourceName: myDep
  namespace: mynamespace
  port: 8080
  localPort: 9000 # *Optional*
```

For this example, Skaffold will attempt to forward port 8080 to `localhost:9000`. If port 9000 is unavailable, Skaffold will forward to a random open port.

#### Note about forwarding System Ports

Skaffold will request matching local ports only when the remote port is `> 1023`. So a service on port `8080` would still map to port `8080` (if available), but a service on port `80` will be mapped to some port `≥ 1024`.

User-defined port-forwards in the `skaffold.yaml` are unaffected and can bind to system ports.

#### Note about user-defined port-forwarding for Docker deployments

 When [deploying to Docker](https://skaffold.dev/docs/deployers/docker/) with a user-defined port-forward in the `skaffold.yaml`, the `resourceType` of `portForward` must be set to `container`. Otherwise, Skaffold will not tell the Docker daemon to expose that port. 

Skaffold will run `kubectl port-forward` on each of these resources in addition to the automatic port forwarding described above. Acceptable resource types include: `Service`, `Pod` and Controller resource type that has a pod spec: `ReplicaSet`, `ReplicationController`, `Deployment`, `StatefulSet`, `DaemonSet`, `Job`, `CronJob`.

| Field | Values | Mandatory |
| --- | --- | --- |
| resourceType | `pod`, `service`, `deployment`, `replicaset`, `statefulset`, `replicationcontroller`, `daemonset`, `job`, `cronjob`, `container` | Yes |
| resourceName | Name of the resource to forward. | Yes |
| namespace | The namespace of the resource to port forward. | No. Defaults to current namespace, or `default` if no current namespace is defined |
| port | Port is the resource port that will be forwarded. | Yes |
| address | Address is the address on which the forward will be bound. | No. Defaults to `127.0.0.1` |
| localPort | LocalPort is the local port to forward too. | No. Defaults to value set for `port`. |

Skaffold will run `kubectl port-forward` on all user defined resources. `kubectl port-forward` will select one pod created by that resource to forward too.

For example, forwarding a deployment that creates 3 replicas could look like this:

```yaml
portForward:
- resourceType: deployment
  resourceName: myDep
  namespace: mynamespace
  port: 8080
  localPort: 9000
```

![Image 2: portforward_deployment](https://skaffold.dev/images/portforward.png)

If you want the port forward to to be available from other hosts and not from the local host only, you can bind the port forward to the address `0.0.0.0`:

```yaml
portForward:
- resourceType: deployment
  resourceName: myDep
  namespace: mynamespace
  port: 8080
  address: 0.0.0.0
  localPort: 9000
```

 Last modified November 13, 2025: [chore: Skaffold 2.17 release (#9912) (561ce51e)](https://github.com/GoogleContainerTools/skaffold/commit/561ce51e1e2c4174b375e694a676585cea7c2b65)

*   [](https://github.com/GoogleContainerTools/skaffold)
*   [](https://skaffold.dev/docs/resources/#community)
*   [](https://groups.google.com/forum/#!forum/skaffold-users)
*   [](https://forms.gle/BMTbGQXLWSdn7vEs6)

© 2025 Skaffold Authors All Rights Reserved

[Privacy Policy](https://policies.google.com/privacy)
