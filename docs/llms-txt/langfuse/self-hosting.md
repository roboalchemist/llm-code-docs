# Source: https://langfuse.com/self-hosting.md

---
title: Self-host Langfuse (Open Source LLM Observability)
description: Self-host Langfuse - This guide shows you how to deploy open-source LLM observability with Docker, Kubernetes, or VMs on your own infrastructure.
label: "Version: v3"
---

import { Callout } from "nextra/components";

# Self-host Langfuse

<Callout type="info">
  Looking for a managed solution? Consider [Langfuse
  Cloud](https://cloud.langfuse.com) maintained by the Langfuse team.
</Callout>

Langfuse is open source and can be self-hosted using Docker.
This section contains guides for different deployment scenarios.
Some add-on features require a [license key](/self-hosting/license-key).

When self-hosting Langfuse, you run the same infrastructure that powers Langfuse Cloud. Read ["Why Langfuse?"](/why) to learn more about why this is important to us.

## Deployment Options [#deployment-options]

### Langfuse Cloud

[Langfuse Cloud](https://cloud.langfuse.com) is a fully managed version of Langfuse that is hosted and maintained by the Langfuse team. Generally, it is the easiest and fastest way to get started with Langfuse at affordable [pricing](/pricing).

### Low-scale deployments

You can [run Langfuse on a VM or locally using Docker Compose](/self-hosting/deployment/docker-compose).
This is recommended for testing and low-scale deployments and lacks high-availability, scaling capabilities, and backup functionality.

### Production-scale deployments

For production and high-availability deployments, we recommend one of the following options:

- [Kubernetes (Helm)](/self-hosting/deployment/kubernetes-helm)
- [AWS (Terraform)](/self-hosting/deployment/aws)
- [Azure (Terraform)](/self-hosting/deployment/azure)
- [GCP (Terraform)](/self-hosting/deployment/gcp)
- [Railway](/self-hosting/deployment/railway)

## Architecture

Langfuse only depends on open source components and can be deployed locally, on cloud infrastructure, or on-premises.



```mermaid
flowchart TB
    User["UI, API, SDKs"]
    subgraph vpc["VPC"]
        Web["Web Server<br/>(langfuse/langfuse)"]
        Worker["Async Worker<br/>(langfuse/worker)"]
        Postgres@{ img: "/images/logos/postgres_icon.svg", label: "Postgres - OLTP\n(Transactional Data)", pos: "b", w: 60, h: 60, constraint: "on" }
        Cache@{ img: "/images/logos/redis_icon.png", label: "Redis\n(Cache, Queue)", pos: "b", w: 60, h: 60, constraint: "on" }
        Clickhouse@{ img: "/images/logos/clickhouse_icon.svg", label: "Clickhouse - OLAP\n(Observability Data)", pos: "b", w: 60, h: 60, constraint: "on" }
        S3@{ img: "/images/logos/s3_icon.svg", label: "S3 / Blob Storage\n(Raw events, multi-modal attachments)", pos: "b", w: 60, h: 60, constraint: "on" }
    end
    LLM["LLM API/Gateway<br/>(optional; BYO; can be same VPC or VPC-peered)"]

    User --> Web
    Web --> S3
    Web --> Postgres
    Web --> Cache
    Web --> Clickhouse
    Web -..->|"optional for playground"| LLM

    Cache --> Worker
    Worker --> Clickhouse
    Worker --> Postgres
    Worker --> S3
    Worker -..->|"optional for evals"| LLM
```





Langfuse consists of two application containers, storage components, and an optional LLM API/Gateway.

- [**Application Containers**](/self-hosting/deployment/infrastructure/containers)
  - Langfuse Web: The main web application serving the Langfuse UI and APIs.
  - Langfuse Worker: A worker that asynchronously processes events.
- **Storage Components**:
  - [Postgres](/self-hosting/deployment/infrastructure/postgres): The main database for transactional workloads.
  - [Clickhouse](/self-hosting/deployment/infrastructure/clickhouse): High-performance OLAP database which stores traces, observations, and scores.
  - [Redis/Valkey cache](/self-hosting/deployment/infrastructure/cache): A fast in-memory data structure store. Used for queue and cache operations.
  - [S3/Blob Store](/self-hosting/deployment/infrastructure/blobstorage): Object storage to persist all incoming events, multi-modal inputs, and large exports.
- [**LLM API / Gateway**](/self-hosting/deployment/infrastructure/llm-api): Some features depend on an external LLM API or gateway.

Langfuse can be deployed within a VPC or on-premises in high-security environments.
Internet access is optional.
See [networking](/self-hosting/security/networking) documentation for more details.



## Optimized for performance, reliability, and uptime

Langfuse self-hosted is optimized for production environments. It is the exact same codebase as Langfuse Cloud, just deployed on your own infrastructure. The Langfuse teams serves thousands of teams with Langfuse Cloud with high availability ([status page](https://status.langfuse.com)) and performance.

Some of the optimizations include:

- **Queued trace ingestion**: All traces are received in batches by the Langfuse Web container and immediately written to S3. Only a reference is persisted in Redis for queueing. Afterwards, the Langfuse Worker will pick up the traces from S3 and ingest them into Clickhouse. This ensures that high spikes in request load do not lead to timeouts or errors constrained by the database.
- **Caching of API keys**: API keys are cached in-memory in Redis. Thereby, the database is not hit on every API call and unauthorized requests can be rejected with very low resource usage.
- **Caching of prompts (SDKs and API)**: Even though prompts are cached client-side by the Langfuse SDKs and only revalidated in the background ([docs](/docs/prompts)), they need to be fetched from the Langfuse on first use. Thus, API response times are very important. Prompts are cached in a read-through cache in Redis. Thereby, hot prompts can be fetched from Langfuse without hitting a database.
- **OLAP database**: All read-heavy analytical operations are offloaded to an OLAP database (Clickhouse) for fast query performance.
- **Multi-modal traces in S3**: Multi-modal traces can include large videos or arbitrary files. To enable support for these, they are directly uploaded to S3/Blob Storage from the client SDKs. Learn more [here](/docs/tracing-features/multi-modality).
- **Recoverability of events**: All incoming tracing and evaluation events are persisted in S3/Blob Storage first. Only after successful processing, the events are written to the database. This ensures that even if the database is temporarily unavailable, the events are not lost and can be processed later.
- **Background migrations**: Long-running migrations that are required by an upgrade but not blocking for regular operations are offloaded to a background job. This massively reduces the downtime during an upgrade. Learn more [here](/self-hosting/upgrade/background-migrations).

If you have any feedback or questions regarding the architecture, please reach out to us.

## Features

Langfuse supports many configuration options and self-hosted features.
For more details, please refer to the [configuration guide](/self-hosting/configuration).



import {
  Lock,
  Shield,
  Network,
  Users,
  Brush,
  Workflow,
  UserCog,
  Route,
  Mail,
  ServerCog,
  Activity,
  Eye,
  Zap,
} from "lucide-react";

import { Cards } from "nextra/components";

<Cards num={3}>
  <Cards.Card
    icon={<Lock size="24" />}
    title="Authentication & SSO"
    href="/self-hosting/security/authentication-and-sso"
    arrow
  />
  <Cards.Card
    icon={<UserCog size="24" />}
    title="Automated Access Provisioning"
    href="/self-hosting/administration/automated-access-provisioning"
    arrow
  />
  <Cards.Card
    icon={<Zap size="24" />}
    title="Caching"
    href="/self-hosting/configuration/caching"
    arrow
  />
  <Cards.Card
    icon={<Route size="24" />}
    title="Custom Base Path"
    href="/self-hosting/configuration/custom-base-path"
    arrow
  />
  <Cards.Card
    icon={<Shield size="24" />}
    title="Encryption"
    href="/self-hosting/configuration/encryption"
    arrow
  />
  <Cards.Card
    icon={<Workflow size="24" />}
    title="Headless Initialization"
    href="/self-hosting/administration/headless-initialization"
    arrow
  />
  <Cards.Card
    icon={<Network size="24" />}
    title="Networking"
    href="/self-hosting/security/networking"
    arrow
  />
  <Cards.Card
    icon={<Users size="24" />}
    title="Organization Creators (EE)"
    href="/self-hosting/administration/organization-creators"
    arrow
  />
  <Cards.Card
    icon={<ServerCog size="24" />}
    title="Organization Management API (EE)"
    href="/self-hosting/administration/organization-management-api"
    arrow
  />
  <Cards.Card
    icon={<Activity size="24" />}
    title="Health and Readiness Check"
    href="/self-hosting/configuration/health-readiness-endpoints"
    arrow
  />
  <Cards.Card
    icon={<Eye size="24" />}
    title="Observability via OpenTelemetry"
    href="/self-hosting/configuration/observability"
    arrow
  />
  <Cards.Card
    icon={<Mail size="24" />}
    title="Transactional Emails"
    href="/self-hosting/configuration/transactional-emails"
    arrow
  />
  <Cards.Card
    icon={<Brush size="24" />}
    title="UI Customization (EE)"
    href="/self-hosting/administration/ui-customization"
    arrow
  />
</Cards>



## Subscribe to updates

import { ProductUpdateSignup } from "@/components/productUpdateSignup";

Release notes are published on [GitHub](https://github.com/langfuse/langfuse/releases). Langfuse uses tagged semver releases ([versioning policy](/self-hosting/upgrade/versioning)).

You can subscribe to our mailing list to get notified about new releases and new major versions.

<ProductUpdateSignup source="self-host" className="mt-3 mb-3 max-w-sm" />

You can also watch the GitHub releases to get notified about new releases:

<Frame className="max-w-md block">
  ![Langfuse
  releases](https://static.langfuse.com/docs-legacy-gifs/github-watch-changelog.gif)
</Frame>

## Support



If you experience any issues when self-hosting Langfuse, please:

1. Check out [Troubleshooting & FAQ](/self-hosting/troubleshooting-and-faq) page.
2. Use [Ask AI](/ask-ai) to get instant answers to your questions.
3. Ask the maintainers on [GitHub Discussions](/gh-support).
4. Create a bug report or feature request on [GitHub](/issues).


