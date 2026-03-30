# Source: https://firebase.google.com/docs/ai-logic/solutions/overview.md.txt

As you develop your app with Firebase AI Logic, you might want to go beyond
the basics discussed in the main guides. The solutions outlined in this section
offer guidance on more advanced use cases.

## Protect your app from unauthorized clients

For mobile and web apps, you need to protect the Gemini API and
your project resources from abuse by unauthorized clients.
You can use Firebase App Check to verify that all API calls are from your
actual app.

[See the Firebase App Check guide](https://firebase.google.com/docs/ai-logic/app-check)

> [!IMPORTANT]
> **Important:** We strongly recommend [implementing App Check into your app](https://firebase.google.com/docs/ai-logic/app-check) as early as possible, even during development, so that every version of your app is protected from API abuse.

## Update values in your app without releasing a new version of your app

If you need to dynamically change values in your app without releasing a new
version of your app, you can use Firebase Remote Config. Examples include
changing the model name, system instructions, prompts, safety settings, or input
for a request.

[See the Remote Config solution](https://firebase.google.com/docs/ai-logic/solutions/remote-config)

> [!IMPORTANT]
> **Important:** We strongly recommend implementing Remote Config for [remotely changing the model name in your app](https://firebase.google.com/docs/ai-logic/change-model-name-remotely) as new models are released or others retired.

## Dynamically and conditionally set runtime configurations

If you want to set configurations based on runtime conditions, you can use
[Firebase Remote Config](https://firebase.google.com/docs/remote-config). One example is changing the
location where you run the Vertex AI service and generative model based on an
end-user's location.

[See the Remote Config solution](https://firebase.google.com/docs/ai-logic/solutions/remote-config)

## Manage files and include large files in multimodal requests

By using Cloud Storage for Firebase, you can take advantage of a fast, secure,
and scalable infrastructure for file storage and management. Plus, you can
include larger files in your multimodal requests using a
Cloud Storage for Firebase URL.

[See the Cloud Storage for Firebase solution](https://firebase.google.com/docs/ai-logic/solutions/cloud-storage)

<br />

We're actively working on other solutions and guides, so check back soon!