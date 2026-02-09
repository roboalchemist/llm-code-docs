# Source: https://braintrust.dev/docs/admin/architecture.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Architecture

Braintrust allows you to log raw data while you run your AI applications, including inputs, outputs, and prompts.
Because of the sensitivity of this data, we support running the logging stack in your AWS account, ensuring that
data never leaves your account, and never flows through Braintrust's infrastructure. This component is referred to
as the *data plane*.

At its core, the data plane deployment works by installing an API layer along with a database in your environment.
On [AWS](/admin/self-hosting/aws), this is packaged as [AWS Lambda](https://aws.amazon.com/lambda/) functions, a [Postgres database](https://www.postgresql.org/),
and other services in a [VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html), packaged up
as a [Terraform module](https://github.com/braintrustdata/terraform-aws-braintrust-data-plane). Braintrust also provides Terraform modules for [GCP](https://github.com/braintrustdata/terraform-google-braintrust-data-plane) and [Azure](https://github.com/braintrustdata/terraform-azure-braintrust-data-plane) using Kubernetes.

When you log from Braintrust's TypeScript or Python library, it sends the events directly to the data plane, never touching Braintrust's
servers. And when you visit the UI (on [https://www.braintrustdata.com/app](https://www.braintrustdata.com/app)), your browser runs requests against the data plane directly.

<img src="https://mintcdn.com/braintrust/W8ewLAD2vistUEen/images/architecture.png?fit=max&auto=format&n=W8ewLAD2vistUEen&q=85&s=60eb620702a2abb8ffb926c3b0af5b80" alt="Architecture diagram" data-og-width="2154" width="2154" data-og-height="1248" height="1248" data-path="images/architecture.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/W8ewLAD2vistUEen/images/architecture.png?w=280&fit=max&auto=format&n=W8ewLAD2vistUEen&q=85&s=0376983798f415a09ce146422e05eae8 280w, https://mintcdn.com/braintrust/W8ewLAD2vistUEen/images/architecture.png?w=560&fit=max&auto=format&n=W8ewLAD2vistUEen&q=85&s=16aa3f4e699855dc795f092d7034c1f9 560w, https://mintcdn.com/braintrust/W8ewLAD2vistUEen/images/architecture.png?w=840&fit=max&auto=format&n=W8ewLAD2vistUEen&q=85&s=f7578421bbb4cab7b7d89baad18fd403 840w, https://mintcdn.com/braintrust/W8ewLAD2vistUEen/images/architecture.png?w=1100&fit=max&auto=format&n=W8ewLAD2vistUEen&q=85&s=a6d494a10121e97e2f4f55d2c6b31200 1100w, https://mintcdn.com/braintrust/W8ewLAD2vistUEen/images/architecture.png?w=1650&fit=max&auto=format&n=W8ewLAD2vistUEen&q=85&s=720da4c8c28180f550e846ac659068ac 1650w, https://mintcdn.com/braintrust/W8ewLAD2vistUEen/images/architecture.png?w=2500&fit=max&auto=format&n=W8ewLAD2vistUEen&q=85&s=0b2732cf72465a8d242ca98f54078046 2500w" />

## Brainstore

Brainstore is Braintrust's high-performance database for ingesting and querying AI data. It uses object storage and a streaming Rust engine to load spans in real time, cutting down on latency and enabling deep search capabilities.

Braintrust automatically uses Brainstore on our hosted platform and requires it when setting up the Braintrust data plane on your own infrastructure. Check out the [self-hosting guide](/admin/self-hosting) for more information.
