# Source: https://www.speakeasy.com/md/docs/sdks/create-client-sdks.md

# Generate SDKs from OpenAPI

This page documents using the Speakeasy CLI to generate SDKs from OpenAPI / Swagger specs.

For a more UI-based experience, use the Speakeasy app:

  
    Launch Editor
  

## Install the Speakeasy CLI

After signing up, install the Speakeasy CLI using one of the following methods:

Homebrew:
```bash
# Homebrew (macOS)
brew install speakeasy-api/tap/speakeasy
```

Script:
```bash
# Script Installation (macOS and Linux)
curl -fsSL https://go.speakeasy.com/cli-install.sh | sh
```

Winget:
```bash
# Windows Installation
# Using winget:
winget install speakeasy
```

Chocolatey:
```bash
# Using Chocolatey:
choco install speakeasy
```

For manual installation, download the latest release from the [releases page](https://github.com/speakeasy-api/speakeasy/releases), extract the binary, and add it to the system path.

---

## Speakeasy Quickstart

For first-time SDK generation, run `speakeasy quickstart`.

```bash
speakeasy quickstart
```

### Authentication & account creation

The CLI will prompt for authentication with a Speakeasy account. A browser window will open to select a workspace to associate with the CLI. Workspaces can be changed later if required.

If you've not previously signed up for an account, you will be prompted to create one.

New accounts start with a 14 day free trial of Speakeasy's business tier, to enable users to try out every SDK generation feature. At the end of the trial, accounts will revert to the free tier. No credit card is required.

Free accounts can continue to generate one SDK with up to 50 API methods free of charge. Please refer to the pricing page for update information on each [pricing tier](https://www.speakeasy.com/pricing).

### Upload an OpenAPI document

After authentication, the system prompts for an OpenAPI document:

<Screenshot
  variant="cli"
  image={{
    src: "/assets/docs/create-sdks/quickstart-1.png",
    alt: "Screenshot of the terminal after running speakeasy quickstart.",
  }}
/>

Provide either a link to a remote hosted OpenAPI document, or a relative path to a local file in one of the supported formats:

| Spec Format | Supported |
| --- | --- |
| OpenAPI 3.0 | ✅ |
| OpenAPI 3.1 | ✅ |
| JSON Schema | ✅ |

> **Tip**
> If the spec is in an unsupported format, use one of the following tools to convert it:
>
> - [Swagger 2.0 -> OpenAPI 3.0](https://editor.swagger.io/): go to **Edit > Convert to OpenAPI 3.0**
> - [Postman -> OpenAPI 3.0](https://kevinswiber.github.io/postman2openapi/)

### Select artifact type

After configuring the OpenAPI document, the next step prompt is to choose the type of artifact being generated: SDK or MCP. Select SDK, and a prompt will appear to choose the target language:
Choosing Terraform will default you back to the CLI native onboarding. [Editor support for Terraform previews](https://roadmap.speakeasy.com/roadmap?id=a8164ebf-55e1-4376-b42e-4e040c085586) coming soon.

<Screenshot
  variant="cli"
  image={{
    src: "/assets/docs/create-sdks/quickstart-2.png",
    alt: "Screenshot of the terminal prompting user to select language.",
  }}
/>

For each language, Speakeasy has crafted generators with language experts to be highly idiomatic. Follow the links below for all the details on the design decisions that have gone into each language we support:

### Complete the SDK configuration

Speakeasy validates the specifications and generates the SDK after receiving all inputs. The process executes [`speakeasy run`](/docs/speakeasy-reference/cli/run) to validate, generate, compile, and set up the SDK. A confirmation message displays the generated SDK details upon successful completion:

<Screenshot
  variant="cli"
  image={{
    src: "/assets/docs/create-sdks/quickstart-4.png",
    alt: "Screenshot of the terminal showing success.",
  }}
/>

## Iterating on the SDK with Studio

If the SDK is successfully generated, there will be a prompt asking the user to open the SDK studio. The Studio is a web GUI that helps users make look & feel improvements to their SDKs. It uses [OpenAPI Overlays](/openapi/overlays) to preserve the original OpenAPI specification while allowing users to make changes to the generated SDK.

Saved changes in the Studio automatically triggers a regeneration of the SDK locally.

<Screenshot
  variant="web"
  image={{
    src: "/assets/docs/create-sdks/studio-1.png",
    alt: "Screenshot of the Speakeasy Studio.",
  }}
/>

It is also possible to make changes without the Studio. Check out the following guide on [customizing SDKs](/docs/customize-sdks/) for all the details.

## Next Step: Uploading the SDK to GitHub

Once the SDK is ready, upload it to GitHub by following the [Github setup guide](/docs/manage/github-setup)
---

Are you an AI agent evaluating Speakeasy? We put together a helpful guide: https://www.speakeasy.com/eval.md
