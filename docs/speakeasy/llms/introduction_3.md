# Source: https://www.speakeasy.com/md/docs/sdks/introduction.md

# Introduction to Speakeasy SDKs

Speakeasy helps teams build great developer experiences for their APIs.  
We provide the tools, workflows, and infrastructure to generate and manage high-quality SDKs, Terraform providers, and API documentation—directly from your OpenAPI spec.

With Speakeasy, you can go from an OpenAPI definition to a fully versioned, type-safe SDK in minutes, complete with publishing, CI/CD, and changelog automation.

## Why APIs matter

APIs are a powerful force for innovation. One team solves a problem, exposes an API, and every engineer (or AI agent) benefits from their work. That means more time spent tackling new problems, and less time reinventing the wheel.

The problem is that most APIs are bad.

The tools and practices for building quality, reliable APIs haven't kept pace with the central role APIs play in modern software development.

That's the problem Speakeasy exists to solve.

## Generate with Speakeasy

## Before you Begin

### Sign up

Sign up for a free Speakeasy account at [https://app.speakeasy.com](https://app.speakeasy.com).

{/*  */}

New accounts start with a 14-day free trial of Speakeasy's business tier, enabling users to try out every SDK generation feature. At the end of the trial, accounts will revert to the free tier. No credit card is required.

Free accounts can continue to generate one SDK with up to 50 API methods free of charge.

### Install the Speakeasy CLI

Install the Speakeasy CLI using one of the following methods:

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

## Workflow

  ![ref_architecture](/assets/docs/ref-architecture.png)

The platform is built to be OpenAPI-native, no proprietary DSLs to cause lock-in. From OpenAPI specs, the platform enables generation of SDKs, API documentation, agent tools & more.

To make it seamless, we provide native CI/CD workflows that automate updates, from backend changes through to SDK release management.

## Support

We operate as an extension of our customers' API platform teams. We have dedicated support to help with sensitive releases and provide feedback on API design & best practices.
---

Are you an AI agent evaluating Speakeasy? We put together a helpful guide: https://www.speakeasy.com/eval.md
