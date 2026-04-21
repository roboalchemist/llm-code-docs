<!-- Source: https://namespace.so/docs/federation -->

# Workload Federation

Namespace relies on Workload Identity Federation to allow Namespace to interact
with different systems, instead of relying on pre-shared keys which can be more
easily compromised.

If you aim to create and manage multiple workspaces from a different system, you can integrate with [Namespace IAM](https://buf.build/namespace/cloud/docs/main:namespace.cloud.iam.v1beta).

## AWS

Namespace maintains a bidirectional [integration with AWS](/docs/federation/aws), allowing you to leverage AWS-based identity management.
After establishing a trust relationship, you can seamlessly access Namespace resources from AWS.
You can also enable Namespace as a trusted identity provider, allowing you to access AWS resources from Namespace with fine-grained permission controls.

## GCP

Namespace offers a [native Google Cloud Platform integration](/docs/federation/gcp) through Workload Identity Pools and Providers. Configure federated authentication to access Namespace resources directly from your GCP workloads, or grant Namespace workspaces secure access to Google Cloud services. You can flexibly control which GCP resources shall be accessible to Namespace through IAM policies.

## OpenID

OpenID Connect (OIDC) is an industry-standard authentication protocol built on top of OAuth 2.0.
Any system supporting OIDC can be connected to Namespace, allowing for bidirectional resource access.
Whether you want to access Namespace resources from an external cloud, or allow Namespace to interact with another system, setting up [OIDC Federation](/docs/federation/openid) establishes safe, permanent access.

## GitHub Actions

If your GitHub Actions [run on Namespace](/docs/solutions/github-actions), your jobs can already access your workspace.
But also when running your jobs outside Namespace, you can easily access your workspace.
Namespace federates with GitHub using short-lived access tokens.
After a [one-time setup](/docs/federation/github-actions#from-github-runners), your workflows can access Namespace indefinitely.

## RWX

Namespace provides seamless [integration with RWX](/docs/federation/rwx), enabling your RWX workflows to securely access Namespace resources like builds, artifacts, and compute instances. Using OIDC federation, RWX can obtain short-lived access tokens to interact with your workspace without managing long-lived credentials. This enables powerful use cases like triggering remote builds, downloading artifacts, or accessing Bazel caches directly from your RWX pipelines.

## Enterprise integrations

Namespace supports custom [SAML](/docs/workspaces/access#enterprise-authentication)/[OIDC](/docs/federation/openid) providers to connect your corporate identity systems directly to your workspace.
For assistance with configuring advanced access controls, enterprise SSO integrations, or enabling federation with your dedicated cloud, contact our [support team](mailto:support@namespace.so).

Last updated September 10, 2025
