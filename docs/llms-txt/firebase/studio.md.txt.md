# Source: https://firebase.google.com/docs/studio.md.txt

# Firebase Studio

# Firebase Studio

Rapidly prototype, build, and ship full-stack AI-infused
apps quickly and efficiently, right from your browser.
[Video](https://www.youtube.com/watch?v=vVAui3_rvD8)

Firebase Studio is an agentic cloud-based development environment
that helps you build and ship production-quality full-stack AI
apps, including APIs, backends, frontends, mobile, and more.
Firebase Studio unifies
[Project IDX](https://firebase.google.com/docs/studio/idx-is-firebase-studio) with specialized
AI agents and assistance from Gemini in Firebase
to provide a collaborative workspace accessible from anywhere,
containing everything you need to develop an application.
You can import your existing projects or start something new
with templates supporting a variety of languages and frameworks.
[Learn how to get started](https://firebase.google.com/docs/studio/get-started) [Try
Firebase Studio now](https://studio.firebase.google.com)

> [!WARNING]
> **Preview:** Firebase Studio is in Preview, which means that the product is not subject to any SLA or deprecation policy and could change in backwards-incompatible ways.

## Key capabilities

|---|---|
| **Import projects from source control, local archive, or Figma design** | [Bring your own apps to Firebase Studio](https://firebase.google.com/docs/studio/get-started-import): import a local archive, connect a public or private source code repository, or generate code from a Figma design and import it with the [Builder.io Figma plugin](https://www.builder.io/c/docs/builder-figma-plugin). |
| **Quick project setup with built-in templates and samples** | Firebase Studio provides [extensive framework and language support](https://firebase.google.com/docs/studio/get-started-template) with a large library of templates and sample apps, including popular languages like Go, Java, .NET, Node.js, and Python Flask, and frameworks like Next.js, React, Angular, Vue.js, Android, Flutter, and more. Start with a template or sample app from the [template gallery](https://firebase.google.com/docs/https://studio.firebase.google.com//templates) and/or create your own [custom template](https://firebase.google.com/docs/studio/custom-templates) to share. |
| **Rapid natural language prototyping** | Use Gemini in Firebase to prototype and publish full-stack web applications with [the App Prototyping agent](https://firebase.google.com/docs/studio/get-started-ai). Generate entire apps with multimodal prompts, including natural language, images, drawings. Enhance your app using a gallery of stock images from [Unsplash](https://unsplash.com). If your app needs a database or authentication, the App Prototyping agent sets up Cloud Firestore and Firebase Authentication. |
| **Always-available AI assistance from Gemini in Firebase** | Use AI coding assistance from [Gemini in Firebase](https://firebase.google.com/docs/studio/ai-assistance) across all development surfaces: interactive chat, code generation, tool running, and inline code suggestions. [Gemini in Firebase](https://firebase.google.com/docs/studio/try-gemini) can help you write code and documentation, fix bugs, write and run unit tests, manage and resolve dependencies, work with Docker containers, and more. |
| **Familiar and highly customizable development environment** | Firebase Studio is built on the popular Code OSS project and runs a full [virtual machine (VM)](https://cloud.google.com/workstations) powered by Google Cloud. You can customize almost every aspect of your online development environment with [Nix](https://firebase.google.com/docs/studio/customize-workspace), including system packages, language tooling, IDE configurations, app previews, and IDE configuration---and share the project and its entire development environment configuration with a [custom template](https://firebase.google.com/docs/studio/custom-templates). |
| **Built-in tools, emulators, and deployment methods with deep Firebase and Google Cloud integration** | [Preview your web and Android apps right in the browser](https://firebase.google.com/docs/studio/preview-apps) and take advantage of [built-in runtime services and tools](https://firebase.google.com/docs/studio/debug) for emulation, testing, and debugging. Firebase Studio seamlessly integrates with [Firebase and Google Cloud services](https://firebase.google.com/docs/studio/google-integrations). For example, you could use the [Firebase Local Emulator Suite](https://firebase.google.com/docs/emulator-suite) directly from Firebase Studio to thoroughly test Firebase and Google Cloud services like Firebase Authentication, Cloud Functions, Cloud Firestore, Cloud Storage, Firebase App Hosting, and Firebase Hosting before you [publish your app](https://firebase.google.com/docs/studio/deploy-app). |

## How does it work?

Firebase Studio supports multiple modes to cater to different development
styles:

- **Coding with full control** : Work directly in a Code OSS-based IDE where
  you can import existing repositories or start new projects, and use extensions
  from the [Open VSX Registry](https://open-vsx.org/).
  Gemini in Firebase
  provides workspace-aware AI assistance with code completion, code
  generation, testing, tool-running, and documentation. You can completely
  customize your workspaces, deployment approach, and target runtime
  environment with support for extensible configuration using
  [Nix](https://nixos.org/).

- **Prompting without coding: The App Prototyping agent, also known as
  Prototyper** lets you create new workspaces to
  prototype and refine app ideas with
  Gemini in Firebase---without writing any code. Work with the
  agent using multimodal prompts to iteratively develop a full-stack app
  (currently works for web apps), test and debug, and share your work with
  others, right from your browser. You can immediately roll changes back if
  needed, add new features, test, publish to Firebase App Hosting and
  monitor your app's performance with built-in observability.

You can seamlessly transition between coding and prompting to harness the
strengths of each. For example, you can start with a prototype in
the App Prototyping agent that covers the basics, like app structure and
user flow, then switch to
Code to implement more custom logic and integration.

This flexibility lets you iterate quickly and build apps that meet your
specific needs---all from Firebase Studio.

> [!NOTE]
> **Note:** The App Prototyping agent can help you **build web apps with
> Next.js**. Support for other platforms and frameworks is coming soon!

## Pricing, quotas, and limits

Access to Firebase Studio is available at no cost, but you can increase the
number of workspaces you can create by joining the
[Google Developer Program](https://developers.google.com/profile/u/_/dashboard).
Certain integrations (like Firebase App Hosting) may require a
Cloud Billing account.

Learn more at [Firebase Studio pricing, quotas, and limits](https://firebase.google.com/docs/studio/pricing).

## How Firebase Studio uses your data

Your use of Firebase Studio is governed by the [Google Terms of
Service](https://policies.google.com/terms).

However, note that your use of generative AI features within
Firebase Studio is governed by the [Generative AI Prohibited Use
Policy](https://policies.google.com/terms/generative-ai/use-policy) and the
[Gemini API Additional Terms of
Service](https://ai.google.dev/gemini-api/terms) (specifically governed by
[Gemini API Additional Terms of Service: Unpaid
Services](https://ai.google.dev/gemini-api/terms#unpaid-services)).

To block the use of your *prompts and responses* for model training, do not
use the App Prototyping agent, and do not use Gemini in Firebase within
Firebase Studio. To block the use of your *code* for model training,
[turn off code
completion](https://firebase.google.com/docs/studio/set-up-gemini#adjust-code-complete)
and [code
indexing](https://firebase.google.com/docs/studio/set-up-gemini#adjust-code-indexing)
in your Firebase Studio settings.

## Next steps

- [Start prototyping your new app with Firebase Studio](https://firebase.google.com/docs/studio/get-started-ai).
- [Learn more about Firebase Studio workspaces](https://firebase.google.com/docs/studio/get-started-workspace).