# Source: https://render.com/docs/deploy-openclaw.md

# Deploy OpenClaw on Render — Run your personal agentic assistant on Render.


> *OpenClaw is a rapidly evolving project.*
>
> Before deploying, make sure you understand and are comfortable with the risks of integrating experimental agentic software with your other systems, and of providing secure credentials to this tool.

[OpenClaw](https://github.com/openclaw/openclaw) is a personal agentic assistant that integrates with a variety of messaging platforms, such as WhatsApp and Slack.

Note that some capabilities of OpenClaw expect a macOS environment, such as integrations with the macOS Notes and Reminders apps. These capabilities are not supported on Render.

## What you'll deploy

Your OpenClaw deployment consists of a single Render web service that includes:

- *OpenClaw gateway* - The core AI assistant runtime
- *Proxy server* - A lightweight Go wrapper that provides token authentication and health checks.
- *Persistent disk* - Retains your configuration, sessions, and workspace files across deploys.

> *This template uses paid Render resources. It requires adding a payment method.*
>
> Render's *Standard* instance type is the smallest instance type that supports OpenClaw. A persistent disk is required to preserve data and configuration across deploys.
>
> For details, see the [pricing page](/pricing#services).

## 1. Sign up for Render

Signing up is fast and free:

## 2. Copy the example template

Render provides a template that simplifies deploying OpenClaw using a [Render Blueprint](infrastructure-as-code):

1. Open the [render-examples/openclaw-render template](https://github.com/render-examples/openclaw-render) on GitHub.
2. Click *Use this template > Create a new repository* in the top right.
3. In the form that appears, set configuration options for your new repo, then click *Create repository*.

## 3. Create a Render Blueprint

Your newly created repo contains a `render.yaml` file that defines your OpenClaw web service:

```yaml
# An excerpt from render.yaml
services:
  - type: web
    name: openclaw
    runtime: docker
    plan: standard
    healthCheckPath: /health
    # ...
```

The full file in your repo includes all required environment variables and configuration.

To deploy using [Blueprints](infrastructure-as-code):

1. In the [Render Dashboard](https://dashboard.render.com), click *New > Blueprint*:

   [image: Selecting Blueprint from the New menu]

2. If you haven't yet, connect your GitHub account to Render. This enables Render to fetch the `render.yaml` file from your repo.

3. Under *Connect a repository*, click the *Connect* button for the repo you created earlier.

   This opens a Blueprint creation form.

4. Provide a *Blueprint Name* and confirm that you're pulling the *Branch* you expect from your repo.

5. You'll be prompted to enter values for environment variables for various AI providers:

   [image: Blueprint creation form showing openclaw service]

    Provide API keys for each provider you intend to use.

6. Review the costs associated with your Blueprint, then click *Deploy Blueprint*. Render kicks off the initial sync, which creates your web service.

## 4. Access the Control UI

1. After your web service's deploy completes, navigate to your web service's page in the Render Dashboard. Its `onrender.com` URL appears at the top:

    [image: Web service URL in the Render Dashboard]

2. When you first visit this URL, the following dialog appears:

    [image: OpenClaw auth dialog]

3. Obtain your service's `OPENCLAW_GATEWAY_TOKEN` from its *Environment* page in the Render Dashboard. This value was generated automatically as part of your Blueprint's first sync.

> *Your gateway token is a secret credential!*
>
>     Do not share this token with anyone. If you believe it's been compromised, replace its value from your service's *Environment* page.

4. Paste your token in the *Gateway Token* field and click *Continue*.

You're all set! Your browser redirects to the OpenClaw Control UI:

[image: OpenClaw Control UI]

You're up and running with OpenClaw on Render! To start connecting messaging channels, customizing your assistant's behavior, and exploring available skills, see the [official OpenClaw documentation](https://docs.openclaw.ai).

---

##### Appendix: Glossary definitions

###### web service

Deploy this *service type* to host a dynamic application at a public URL.

Ideal for full-stack web apps and API servers.

Related article: https://render.com/docs/web-services.md

###### persistent disk

A high-performance SSD that you can attach to a service to preserve filesystem changes across deploys and restarts.

Disables [zero-downtime deploys](/deploys#zero-downtime-deploys) for the service.

Related article: https://render.com/docs/disks.md

###### instance type

Specifies the RAM and CPU available to your service's *instances*.

Common instance types for a new web service include:

- *Free*: 512 MB RAM / 0.1 CPU
- *Starter*: 512 MB RAM / 0.5 CPU
- *Standard*: 2 GB RAM / 1 CPU

For the full list, see the [pricing page](/pricing#services).

###### environment variable

Config values you can apply to a service to customize its behavior at build and runtime, such as `NODE_VERSION` or `OPENAI_API_KEY`.

Render sets some environment variables for your service by [default](environment-variables).

Related article: https://render.com/docs/configure-environment-variables.md