# Source: https://lobehub.com/docs/self-hosting/start

---
title: Build Your Own LobeHub - Choose Your Deployment Platform
description: >-
  Explore multiple deployment platforms like Vercel, Docker, Docker Compose, and
  more to deploy LobeHub. Choose the platform that best suits your needs.
tags:
  - LobeHub
  - Deployment Platform
  - Vercel
  - Docker
  - Docker Compose
  - Alibaba Cloud
---

# Build Your Own LobeHub

LobeHub can be self-hosted on your own infrastructure, giving you complete control over your data, customization, and deployment environment. Whether you're deploying for a team, organization, or personal use, LobeHub supports multiple deployment methods.

<PlatformCards urlPrefix={'platform'} />

## Architecture Overview

LobeHub consists of several key components:

### Core Services

- **Next.js application** — Hybrid SSR/SPA frontend with API routes
- **PostgreSQL database** — Stores conversations, agents, files, and user data
- **Redis** (optional) — Session storage and caching
- **S3-compatible storage** — File uploads and knowledge base documents

### Optional Services

- **RustFS / MinIO** — Self-hosted S3-compatible storage
- **Langfuse** — LLM observability and tracing
- **OpenTelemetry** — Distributed tracing
- **Searxng** — Privacy-focused web search

## Choosing a Deployment Method

### Docker Compose (Recommended)

**Best for:** Self-hosted installations, full infrastructure control, team deployments.

**Pros:**

- Complete stack in one command
- Easy updates with `docker compose pull`
- Includes PostgreSQL, Redis, RustFS, Searxng
- Full feature support — no timeout limits, WebSocket support

**Cons:**

- Requires server management
- Need to handle backups and monitoring

### Vercel

**Best for:** Quick deployments, serverless scaling, low maintenance.

**Pros:**

- One-click deployment
- Automatic HTTPS and CDN
- Scales automatically
- Free tier available

**Cons:**

- Requires an external PostgreSQL database
- 10-second serverless function timeout limit
- No WebSocket support
- Less control over infrastructure

### Cloud Platforms (Zeabur, Sealos, Dokploy)

Similar to Vercel with regional options. Good for specific geographic requirements with various pricing and feature differences.

## Feature Comparison

| Feature           | Docker       | Vercel      | Cloud Platforms |
| ----------------- | ------------ | ----------- | --------------- |
| Full control      | ✅            | ❌           | ⚠️              |
| Custom domain     | ✅            | ✅           | ✅               |
| One-click deploy  | ❌            | ✅           | ✅               |
| Auto-scaling      | ❌            | ✅           | ✅               |
| Free tier         | ✅            | ✅           | Varies          |
| Function timeout  | Unlimited    | 10s         | Varies          |
| WebSocket support | ✅            | ❌           | Varies          |
| File storage      | Local/RustFS | External S3 | Varies          |
| Database          | Included     | External    | Varies          |

## Prerequisites

Before deploying LobeHub, gather the following:

### Required

**AI provider API keys** — At minimum, you need an API key from one AI provider:

- **OpenAI** — `OPENAI_API_KEY` from [platform.openai.com](https://platform.openai.com/account/api-keys)
- **Anthropic** — `ANTHROPIC_API_KEY` from [console.anthropic.com](https://console.anthropic.com/)
- **Google** — `GOOGLE_API_KEY` from [aistudio.google.com](https://aistudio.google.com/app/apikey)

See [AI Provider Configuration](/docs/self-hosting/environment-variables/model-provider) for the full list of supported providers.

**Database (for server deployment)** — PostgreSQL 14+ is required:

- **Managed options**: Neon, Supabase, Railway, Vercel Postgres
- **Self-hosted**: Docker (included in Docker Compose), AWS RDS, Google Cloud SQL

### Optional but Recommended

**Redis** — Improves performance for session storage, rate limiting, and caching. Use Upstash, Redis Cloud, or self-hosted Redis.

**S3-compatible storage** — Required for file uploads and knowledge bases:

- **AWS S3** — Production-ready, scalable
- **Cloudflare R2** — No egress fees
- **RustFS / MinIO** — Self-hosted S3 alternative (included in Docker Compose)

**Authentication provider** — For SSO and team features (Google OAuth, GitHub OAuth, Microsoft Azure AD, Auth0, Keycloak). See [Authentication Setup](/docs/self-hosting/auth) for configuration.

## Security Considerations

<Callout type={'warning'}>
  Never commit API keys or secrets to version control. Always use environment variables.
</Callout>

Essential security measures:

1. **Use HTTPS** — Always deploy with SSL/TLS certificates
2. **Secure your database** — Use strong passwords and restrict network access
3. **Environment variables** — Store secrets securely (never in code)
4. **Authentication** — Enable Better Auth for multi-user deployments
5. **Regular updates** — Keep LobeHub and dependencies up to date

Authentication options:

- **Open access** — No authentication (single-user deployments only)
- **Better Auth** — Built-in auth with email/password, OAuth, magic links
- **Reverse proxy** — Use Authelia, Authentik, or similar

## Next Steps

1. **Choose your deployment method** — Docker for maximum control or Vercel for simplicity
2. **Gather API keys** — Obtain API keys from your chosen AI providers
3. **Set up infrastructure** — Provision database, Redis, and storage as needed
4. **Configure environment variables** — See the [environment variable reference](/docs/self-hosting/environment-variables)
5. **Deploy** — Follow the platform-specific guide above
6. **Configure authentication** — Set up [Better Auth](/docs/self-hosting/auth) for multi-user access


<!-- Navigation -->

## Documentation Sections

- [Usage Guideline](/docs/usage)
- [Self Hosting](/docs/self-hosting)
- [Development](/docs/development)

## Self Hosting


**Overview**

- [Introduction](/docs/self-hosting/start)
- **Get Started**
  - [Deploy with Vercel](/docs/self-hosting/platform/vercel)
  - [Deploy with Docker](/docs/self-hosting/platform/docker)
  - [Deploy with Docker Compose](/docs/self-hosting/platform/docker-compose)
  - [Deploy with Zeabur](/docs/self-hosting/platform/zeabur)
  - [Deploy with SealOS](/docs/self-hosting/platform/sealos)
  - [Deploy with RepoCloud](/docs/self-hosting/platform/repocloud)
  - [Deploy with Dokploy](/docs/self-hosting/platform/dokploy)
- **General Example**
  - [Integrating with Azure OpenAI](/docs/self-hosting/examples/azure-openai)
  - [Integrating with Ollama](/docs/self-hosting/examples/ollama)

**Configuration**

- **Authentication**
  - [Email](/docs/self-hosting/auth/email)
  - [SSO Providers](/docs/self-hosting/auth/providers)
  - [Legacy (Clerk / Next Auth)](/docs/self-hosting/auth/legacy)
- **Advanced**
  - [Auto Sync With Latest](/docs/self-hosting/advanced/upstream-sync)
  - [Desktop](/docs/self-hosting/advanced/desktop)
  - [Model List](/docs/self-hosting/advanced/model-list)
  - [Feature Flags](/docs/self-hosting/advanced/feature-flags)
  - [Settings URL Share](/docs/self-hosting/advanced/settings-url-share)
  - [Knowledge Base](/docs/self-hosting/advanced/knowledge-base)
  - [Online Search](/docs/self-hosting/advanced/online-search)
  - [S3 Object Storage](/docs/self-hosting/advanced/s3)
  - [Redis Cache](/docs/self-hosting/advanced/redis)
  - [Data Analytics](/docs/self-hosting/advanced/analytics)
  - [Observability](/docs/self-hosting/advanced/observability)
- **Environment Variables**
  - [Basic](/docs/self-hosting/environment-variables/basic)
  - [Model Provider](/docs/self-hosting/environment-variables/model-provider)
  - [Authentication](/docs/self-hosting/environment-variables/auth)
  - [S3 Storage](/docs/self-hosting/environment-variables/s3)
  - [Redis](/docs/self-hosting/environment-variables/redis)
  - [Analytics](/docs/self-hosting/environment-variables/analytics)
- **FAQ**
  - [Empty Response with `OPENAI_PROXY_URL` Environment Variable](/docs/self-hosting/faq/no-v1-suffix)
  - [`UNABLE_TO_VERIFY_LEAF_SIGNATURE` Error When Using Proxy](/docs/self-hosting/faq/proxy-with-unable-to-verify-leaf-signature)
  - [AI Image Generation Timeout on Vercel](/docs/self-hosting/faq/vercel-ai-image-timeout)
- **Migration**
  - [Upgrade to V2](/docs/self-hosting/migration/v2)

<!-- End Navigation -->

