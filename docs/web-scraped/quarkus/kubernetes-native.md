# Source: https://quarkus.io/kubernetes-native

Title: Kubernetes Native

URL Source: https://quarkus.io/kubernetes-native

Markdown Content:
### Quarkus applications are designed to run in containers.

![Image 1](https://quarkus.io/assets/images/about/icon-kube-native.svg)![Image 2](https://quarkus.io/assets/images/about/icon-kube-native-dark.svg)

The combination of Quarkus and Kubernetes provides an ideal environment for creating scalable, fast, and lightweight applications. Quarkus significantly increases developer productivity with tooling, pre-built integrations, application services, and more.

What does it mean to be a Kubernetes-native framework?
------------------------------------------------------

### Single-step Deployments

Quarkus makes it easy to deploy microservice applications to Kubernetes without having to understand the intricacies of the underlying Kubernetes framework. Extensions are available for Kubernetes, and Kubernetes distributions, to facilitate this process with only a minimal amount of configuration variables needed.

Using the Quarkus Kubernetes extension, developers can perform or automate a single-step deployment using Jib, Docker, and Source-to-Image (S2i) including the creation of DeploymentConfig to trigger automatic redeployments.

[Read the "Kubernetes extension" guide](https://quarkus.io/guides/deploying-to-kubernetes)

Additionally, Quarkus includes extensions that make it easy to deploy serverless microservices to cloud providers including AWS Lambda, Azure Functions, and Google Cloud Functions as well as Knative to take advantage of Quarkus application’s fast startup times.

[Read the "Kubernetes extension" guide](https://quarkus.io/guides/deploying-to-kubernetes)

### Tracing & Debugging

Quarkus provides developers the tools and capabilities to troubleshoot distributed microservices applications in Kubernetes including tracing and debugging.

Quarkus utilizes [OpenTelemetry](https://opentelemetry.io/) which is a vendor-agnostic API to help developers easily instrument tracing into their codebase. Distributed tracing helps pinpoint where failures occur and what causes poor performance.

[Read the "Using OpenTelemetry" guide](https://quarkus.io/guides/opentelemetry)

### Application Health

Quarkus leverages SmallRye Health, an implementation of the MicroProfile Health specification. This allows applications to provide information about their state to external viewers in a Kubernetes environment where automated processes must be able to determine whether the application should be discarded or restarted.

[Read the "Smallrye Health" guide](https://quarkus.io/guides/microprofile-health)

### Application Metrics

Quarkus utilizes the [Micrometer](https://micrometer.io/) metrics library for runtime and application metrics. It provides a simple facade for the most popular monitoring systems to instrument your JVM-based application code without vendor lock-in. Application-specific and built-in metrics can be exposed using Micrometer.

[Read the "Micrometer Metrics" guide](https://quarkus.io/guides/micrometer#support-for-the-microprofile-metrics-api)

### Application Configuration

Quarkus includes an extension that allows developers to use Kubernetes ConfigMaps and Secrets as a configuration source, without having to mount them into the Pod running the Quarkus application or make any other modifications to their Kubernetes Deployment (or Openshift DeploymentConfig).

[Read the "Kubernetes Config" guide](https://quarkus.io/guides/kubernetes-config)
