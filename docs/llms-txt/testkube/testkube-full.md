# Testkube: Cloud-Native Continuous Testing Platform
> Testkube is a cloud-native continuous testing platform that helps engineering teams keep pace with AI-powered development and release velocity.

Testkube enables developers, QA engineers, SREs, and platform teams to run any type of test — functional, load, security, custom scripts — directly inside Kubernetes. It scales with your infrastructure, works with your existing tools, and supports GitOps, CI/CD pipelines, and on-prem deployments.

We integrate deeply with Kubernetes-native workflows, helping teams unify and simplify testing across the software delivery lifecycle.

## Core concepts
- [What is Testkube?](https://testkube.io/docs/overview): Overview of the platform and key benefits
- [How Testkube Works](https://testkube.io/docs/core-concepts/architecture): Explains the Kubernetes-native test execution model
- [Supported Test Types](https://testkube.io/docs/test-types/overview): Includes Cypress, Postman, JMeter, K6, SoapUI, custom scripts, and more
- [Test Workflows](https://testkube.io/docs/architecture/test-workflows): How tests are triggered and managed
- [Test Results & Insights](https://testkube.io/docs/using-testkube/analyzing-results): Observability and test reporting features

## Use Cases

### Accelerate Application Delivery
- [Scheduling & Triggers Outside CI/CD](https://testkube.io/use-cases/test-with-ci-cd-pipelines): Trigger tests manually, on a schedule, via Kubernetes events or CI/CD pipelines.
- [Ephemeral Environment Testing](https://testkube.io/use-cases/ephemeral-clusters): Run complete test suites in short‑lived clusters or namespaces, and preserve results centrally.
- [GitOps‑Based Test Automation](https://testkube.io/use-cases/gitops): Trigger tests automatically when Kubernetes resources (e.g. via ArgoCD) change, using Kubernetes CRDs.

### Improve Application Quality
- [Geo‑Distributed Load & Functional Testing](https://testkube.io/use-cases/geo-distributed-load-functional-testing): Run tests from clusters in multiple regions using your own infrastructure.
- [Load Testing Orchestration](https://testkube.io/use-cases/load-testing-orchestration): Scale k6 or other tools across clusters using advanced Testkube workflows—including setup/teardown, parameterization, and sharding.

### Reduce Infrastructure Costs
- [Optimize Kubernetes Resource Usage](https://testkube.io/use-cases/optimize-kubernetes-resource-usage): Use Testkube’s dashboard to monitor per-test CPU/memory/storage usage and identify inefficiencies.
- [Leverage Existing Kubernetes Infrastructure](https://testkube.io/use-cases/leverage-k8s-infrastructure-for-test-execution): Replace expensive third‑party testing platforms by running all tests within your clusters.

### Test Smarter Across Every Kubernetes Environment
- [Multi‑Cluster & Distributed Consistency](https://testkube.io/use-cases/geo-distributed-clusters): Centralized control plane runs consistent tests across multi‑cluster and multi‑cloud environments.
- [Uniform Testing Across Local, Cloud & CI](https://testkube.io/use-cases): Unified orchestration across developer environments (KinD or local), CI/CD pipelines, staging, and production.

## Who it's for
- Developers: Trigger tests from CLI, API, CI, or IDE
- QA Engineers: Centralize test management across environments
- SREs & Platform Teams: Reuse infra, scale tests, automate debugging

## Product documentation
- [Documentation Home](https://testkube.io/docs)
- [Install Testkube](https://testkube.io/docs/installing-testkube/overview)
- [Configure Agents](https://testkube.io/docs/agent/overview)
- [Bring Your Own Test Tool](https://testkube.io/docs/test-types/overview)

## Open source and cloud
- [GitHub Repository](https://github.com/kubeshop/testkube): OSS core, stars, issues, roadmap
- [Testkube Cloud](https://cloud.testkube.io): Managed version with multi-cluster management and advanced features

## Company
- [About Testkube](https://testkube.io/about)
- [Blog](https://testkube.io/blog): Engineering insights and tutorials
- [Contact](https://testkube.io/contact): Reach out for support or demo
