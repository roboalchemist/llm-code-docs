# Source: https://skaffold.dev/docs/tutorials/go-integration-coverage/

Title: Go integration test coverage profiles

URL Source: https://skaffold.dev/docs/tutorials/go-integration-coverage/

Published Time: Thu, 13 Nov 2025 20:49:27 GMT

Markdown Content:
Go integration test coverage profiles | Skaffold
===============
[Skaffold](https://skaffold.dev/)

*   [](https://github.com/GoogleContainerTools/skaffold)
*   [](https://skaffold.dev/docs/resources/#community)
*   [](https://groups.google.com/forum/#!forum/skaffold-users)
*   [Documentation](https://skaffold.dev/docs/)
*   [skaffold.yaml](https://skaffold.dev/docs/references/yaml/)
*   [Versions](https://skaffold.dev/docs/tutorials/go-integration-coverage/#)[v1.0](https://skaffold-v1.web.app/)[v2.0](https://skaffold-v2.web.app/) 

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

[Edit this page](https://github.com/GoogleContainerTools/skaffold/edit/main/docs-v2/content/en/docs/tutorials/go-integration-coverage.md)[Create documentation issue](https://github.com/GoogleContainerTools/skaffold/issues/new?title=Go%20integration%20test%20coverage%20profiles)

*   [Background](https://skaffold.dev/docs/tutorials/go-integration-coverage/#background)
*   [Steps](https://skaffold.dev/docs/tutorials/go-integration-coverage/#steps)
*   [The example application](https://skaffold.dev/docs/tutorials/go-integration-coverage/#the-example-application)
*   [Sending signals for writing coverage profile data files](https://skaffold.dev/docs/tutorials/go-integration-coverage/#sending-signals-for-writing-coverage-profile-data-files)
*   [Building the binary and the container image](https://skaffold.dev/docs/tutorials/go-integration-coverage/#building-the-binary-and-the-container-image)
*   [Running the integration tests](https://skaffold.dev/docs/tutorials/go-integration-coverage/#running-the-integration-tests)
*   [Copying coverage profile data files](https://skaffold.dev/docs/tutorials/go-integration-coverage/#copying-coverage-profile-data-files)
*   [Profiles](https://skaffold.dev/docs/tutorials/go-integration-coverage/#profiles)
*   [Running the steps](https://skaffold.dev/docs/tutorials/go-integration-coverage/#running-the-steps)
*   [References](https://skaffold.dev/docs/tutorials/go-integration-coverage/#references)

1.   [Documentation](https://skaffold.dev/docs/)
2.   [Tutorials](https://skaffold.dev/docs/tutorials/)
3.   Go integration test coverage profiles

Go integration test coverage profiles
=====================================

This tutorial describes how to use Skaffold to collect [coverage profile data](https://go.dev/testing/coverage/) from Go applications when running [integration tests](https://go.dev/testing/coverage/#glos-integration-test). These more comprehensive tests, often called end-to-end tests, are run against a deployed application, typically testing multiple user journeys.

Background
----------

Go 1.20 introduced support for collecting coverage profile data from running Go applications. To enable coverage collection, build the binary with the `-cover` flag. The application records coverage profile data in a local directory set by the `GOCOVERDIR` environment variable.

When the application runs on Kubernetes, there is an additional challenge of copying the coverage profile data files to permanent storage before the pod terminates.

By default, the coverage profile data files are written on application exit. This tutorial shows how you can send a signal to write these files without exiting the application, and then copy the files out of the pods.

Steps
-----

Skaffold orchestrates the steps of:

1.   Building binary and the container image, with support for collecting coverage profiles.
2.   Deploying the application to a Kubernetes cluster.
3.   Running the integration tests.
4.   Sending the signal to write coverage profile data files.
5.   Collecting the counter-data files from the application pods.

For steps 3-5, this tutorial uses Skaffold [lifecycle hooks](https://skaffold.dev/docs/lifecycle-hooks/) to run these steps automatically.

The example application
-----------------------

This tutorial refers to the files in the [`go-integration-coverage`](https://github.com/GoogleContainerTools/skaffold/tree/main/examples/go-integration-coverage) example.

You may find it helpful to refer to these files as you go through this tutorial.

Sending signals for writing coverage profile data files
-------------------------------------------------------

By default, coverage profile data files are only written on application exit, specifically on return from `main.main()` or by calling `os.Exit()`. This is problematic in a Kubernetes pod, as the application exit triggers pod termination.

To work around this, add a signal handler to the application. This handler writes the coverage profile data files when it receives the configured signal, using the functions in the built-in [`coverage` package](https://pkg.go.dev/runtime/coverage). It also clears (resets) the counters, which can be useful if you want separate coverage profile reports for different sets of tests.

The snippet below is a Go function that sets up a signal handler. It uses the [`SIGUSR1`](https://www.gnu.org/software/libc/manual/html_node/Miscellaneous-Signals.html) signal, but you can use another signal in your application.

```go
// Note: This snippet omits error handling for brevity.
func SetupCoverageSignalHandler() {
	coverDir, exists := os.LookupEnv("GOCOVERDIR")
	if !exists {
		return
	}
	c := make(chan os.Signal)
	signal.Notify(c, syscall.SIGUSR1)
	go func() {
		for {
			<-c
			coverage.WriteCountersDir(coverDir)
			coverage.ClearCounters() // only works with -covermode=atomic
        }
	}()
}
```

You can call this function from your `main.main()` function to set up the signal handler early on in the application lifecycle.

If the `GOCOVERDIR` environment variable is not set, the function returns without setting up the signal handler. This means that you can control enabling and disabling the signal handler by whether this environment variable is set.

Building the binary and the container image
-------------------------------------------

To build the container image with support for coverage profile collection, compile the binary with the `-cover` flag, and optionally also the `-covermode` flag.

The image must contain the `tar` command to enable copying the counter-data files from the pod.

The following snippet shows how to configure the image build using the Skaffold [ko builder](https://skaffold.dev/docs/builders/builder-types/ko/):

```yaml
build:
  artifacts:
  - image: foo
    ko:
      fromImage: gcr.io/distroless/base-debian11:debug
      flags: ["-cover", "-covermode=atomic"]
```

Using other builders is also possible, by adding the flags to the `go build` command or by setting the `GOFLAGS` environment variable.

Running the integration tests
-----------------------------

The integration tests can be implemented in a number of ways, since they do not run in-process with the application.

For instance, you can implement them using Go tests, a shell script with a sequence of `curl` commands against an HTTP server, or other integration and end-to-end test frameworks.

Use Skaffold post-deploy hooks to run the tests automatically after deploying the application. These hooks can run either on the [`host`](https://skaffold.dev/docs/lifecycle-hooks/#before-deploy-and-after-deploy) where you run Skaffold, or in the deployed [`container`](https://skaffold.dev/docs/lifecycle-hooks/#before-deploy-and-after-deploy-1).

This tutorial uses a `host` hook that runs a shell script. The shell script sets up port-forwarding to the service and then runs the integration test. The arguments to the shell script are used to configure port forwarding.

For this tutorial, the integration test is simply a `curl` command that sends a HTTP request to the application.

```yaml
hooks:
      after:
      - host:
          command: ["./integration-test/run.sh", "service/go-integration-coverage", "default", "4503", "80"]
          os: [darwin, linux]
```

The arguments to the shell script are:

1.   the Kubernetes resource to port-forward to, e.g., `service/myapp` or `deployment/myapp` (required),
2.   the namespace of the Kubernetes resource (defaults to `default`),
3.   the local port (defaults to `4503`), and
4.   the remote port (defaults to `8080`).

After running the integration tests, a `container` hook sends `SIGUSR1` to the application process (PID 1) using the `kill` command:

```yaml
- container:
          command: ["kill", "-USR1", "1"]
          podName: go-integration-coverage-*
          containerName: app
```

The `podName` and `containerName` fields are required and must match the values from the Pod spec in your Kubernetes manifest.

If you create multiple pods, the hook will run in all matching pods.

Copying coverage profile data files
-----------------------------------

A `host` post-deploy hook runs a shell script that copies the counter-data files from the pods to the host where you run Skaffold:

```yaml
- host:
          command: ["./integration-test/coverage.sh"]
          os: [darwin, linux]
```

First, the shell script below locates all pods deployed by the Skaffold run using a selector on the [`skaffold.dev/run-id` label](https://skaffold.dev/docs/tutorials/skaffold-resource-selector/).

Next, the script iterates over the pods and uses `kubectl exec` to run `tar` in the containers to package up the counter-data files and pipe them to the host. On the other end of the pipe, `tar` extracts the files to a report directory on the host where you run Skaffold.

Finally, the `go tool covdata` command reports the coverage as percentage on the terminal.

Skaffold provides the [`SKAFFOLD_KUBE_CONTEXT` and `SKAFFOLD_RUN_ID` environment variables](https://skaffold.dev/docs/lifecycle-hooks/#environment-variables) to the shell script.

Profiles
--------

The Go binary must be compiled with the `-cover` flag to collect coverage metrics. However, you may not want to use this flag when compiling for production use.

Additionally, to simplify metrics reporting, you may want to only specify one replica in the Kubernetes Deployment resource.

Skaffold [profiles](https://skaffold.dev/docs/environment/profiles/) enable different configurations for different contexts.

The `skaffold.yaml` file for this tutorial contains a `coverage` profile that overrides the base configuration as follows:

1.   Specify a base image that contains the `tar` command. `tar` is required to copy the coverage profile data files from the pod.

2.   Build the Go binary with the [`-cover` and `-covermode` flags](https://go.dev/blog/cover).

3.   Patch the Deployment resource to add a volume and volume mount to the pod template spec for the coverage profile data files. This tutorial uses [Kustomize](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/) to patch the resource, but you can use another tool for this in your own environment.

4.   Add post-deploy hooks for running integration tests and collecting coverage profile data.

To activate the profile, add the flag `--profile coverage` to Skaffold commands.

Running the steps
-----------------

To run the steps, follow the instructions in the [README.md](https://github.com/GoogleContainerTools/skaffold/tree/main/examples/go-integration-coverage).

References
----------

*   [Go: Coverage profiling support for integration tests](https://go.dev/testing/coverage/)
*   [`runtime/coverage` package in the Go standard library](https://pkg.go.dev/runtime/coverage)

 Last modified November 13, 2025: [chore: Skaffold 2.17 release (#9912) (561ce51e)](https://github.com/GoogleContainerTools/skaffold/commit/561ce51e1e2c4174b375e694a676585cea7c2b65)

*   [](https://github.com/GoogleContainerTools/skaffold)
*   [](https://skaffold.dev/docs/resources/#community)
*   [](https://groups.google.com/forum/#!forum/skaffold-users)
*   [](https://forms.gle/BMTbGQXLWSdn7vEs6)

© 2025 Skaffold Authors All Rights Reserved

[Privacy Policy](https://policies.google.com/privacy)
