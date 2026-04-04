# Source: https://firebase.google.com/docs/ai-logic.md.txt

# Gemini API using Firebase AI Logic

Build AI-powered mobile and web apps and features with the Gemini and Imagen models using Firebase AI Logic
[Video](https://www.youtube.com/watch?v=EpRSIFVtMng)

Firebase AI Logic gives you access to the latest generative AI models from
Google: the Gemini models and Imagen models.

If you need to call the Gemini API or Imagen API directly
from your mobile or web app --- rather than server-side --- you can use the
Firebase AI Logic client SDKs. These client SDKs are built
specifically for use with mobile and web apps, offering security options against
unauthorized clients as well as integrations with other Firebase services.

**These client SDKs are available in
Swift for Apple platforms, Kotlin \& Java for Android, JavaScript for web,
Dart for Flutter, and Unity.**

With these client SDKs, you can add AI personalization to apps, build an AI chat
experience, create AI-powered optimizations and automation, and much more!

[Get started](https://firebase.google.com/docs/ai-logic/get-started)

<br />

**Need more flexibility or server-side integration?**   

[Genkit](https://genkit.dev/) is Firebase's open-source
framework for sophisticated server-side AI development with broad access to
models from Google, OpenAI, Anthropic, and more. It includes more advanced AI
features and dedicated local tooling.

## Key capabilities

|---|---|
| Multimodal and natural language input | The [Gemini models](https://firebase.google.com/docs/ai-logic/models) are multimodal, so prompts sent to the Gemini API can include text, images, PDFs, video, and audio. Some Gemini models can also generate multimodal *output* . Both the Gemini and Imagen models can be prompted with natural language input. |
| Growing suite of capabilities | With the SDKs, you can call the Gemini API or Imagen API directly from your mobile or web app to [build AI chat experiences](https://firebase.google.com/docs/ai-logic/chat), [generate images,](https://firebase.google.com/docs/ai-logic/generate-images-imagen) use tools (like [function calling](https://firebase.google.com/docs/ai-logic/function-calling) and [grounding with Google Search](https://firebase.google.com/docs/ai-logic/grounding-google-search)), [stream multimodal input and output (including audio)](https://firebase.google.com/docs/ai-logic/live-api), and more. |
| Security and abuse prevention for production apps | Use [Firebase App Check](https://firebase.google.com/docs/ai-logic/app-check) to help protect the APIs that access the Gemini and Imagen models from abuse by unauthorized clients. Firebase AI Logic also has [rate limits per user](https://firebase.google.com/docs/ai-logic/faq-and-troubleshooting#rate-limits-per-user) *by default*, and these per-user rate limits are fully configurable. |
| Robust infrastructure | Take advantage of scalable infrastructure that's built for use with mobile and web apps, like [managing files with Cloud Storage for Firebase](https://firebase.google.com/docs/ai-logic/solutions/cloud-storage), managing structured data with Firebase database offerings (like [Cloud Firestore](https://firebase.google.com/docs/firestore)), and dynamically setting run-time configurations with [Firebase Remote Config](https://firebase.google.com/docs/ai-logic/solutions/remote-config). |

## How does it work?

Firebase AI Logic provides client SDKs, a proxy service, and other features
which allow you to access Google's generative AI models to build AI features in
your mobile and web apps.

#### Support for Google models and "Gemini API" providers

We support all the latest Gemini models and Imagen models,
and you choose your preferred "Gemini API" provider to access these models.
We support both the Gemini Developer API and
Vertex AI Gemini API. Learn about the
[differences between using the two API providers](https://firebase.google.com/docs/ai-logic/faq-and-troubleshooting#differences-between-gemini-api-providers).

And if you choose to use the Gemini Developer API, you can take
advantage of their "free tier" to get you up and running fast.

#### Mobile \& web client SDKs

You send requests to the models directly from your mobile or web app using our
Firebase AI Logic client SDKs, available in
Swift for Apple platforms, Kotlin \& Java for Android, JavaScript for Web,
Dart for Flutter, and Unity.

If you have both of the Gemini API providers set up in your Firebase
project, then you can switch between API providers just by enabling the other
API and changing a few lines of initialization code.

Additionally, several of our client SDKs offer access to
[hybrid and on-device inference](https://firebase.google.com/docs/ai-logic/hybrid). This configuration
allows your app to use the on-device model when it's available, but fall back
seamlessly to the cloud-hosted model when needed (and vice-versa).

#### Proxy service

Our proxy service acts as a gateway between the client and your chosen
Gemini API provider (and Google's models). It provides services and
integrations that are important for mobile and web apps. For example, you can
[set up Firebase App Check](https://firebase.google.com/docs/ai-logic/app-check) to help protect your
chosen API provider and your backend resources from abuse by unauthorized
clients.

This is particularly critical if you chose to use the
Gemini Developer API because our proxy service and this App Check
integration make sure that your Gemini API key stays on the server and
is *not* embedded in your apps' codebase.

## Implementation path

|---|---|---|
|   | Set up your Firebase project and connect your app to Firebase | Use the guided workflow in the [**Firebase AI Logic** page](https://console.firebase.google.com/project/_/ailogic) of the Firebase console to set up your project (including enabling the required APIs for your chosen Gemini API provider), register your app with your Firebase project, and then add your Firebase configuration to your app. |
|   | Install the SDK and initialize | Install the Firebase AI Logic SDK that's specific to your app's platform, and then initialize the service and create a model instance in your app. |
|   | Send prompt requests to the Gemini and Imagen models | Use the SDKs to send text-only or multimodal prompts to a Gemini model to generate [text and code](https://firebase.google.com/docs/ai-logic/generate-text), [structured output (like JSON)](https://firebase.google.com/docs/ai-logic/generate-structured-output) and [images](https://firebase.google.com/docs/ai-logic/generate-images-gemini). Alternatively, you can also prompt an Imagen model to [generate images](https://firebase.google.com/docs/ai-logic/generate-images-imagen). Build richer experiences with [multi-turn chat](https://firebase.google.com/docs/ai-logic/chat), [bidirectional streaming (including audio)](https://firebase.google.com/docs/ai-logic/live-api), and [function calling](https://firebase.google.com/docs/ai-logic/function-calling). |
|   | Prepare for production | Implement important integrations for mobile and web apps, like protecting the API from abuse with [Firebase App Check](https://firebase.google.com/docs/ai-logic/app-check) and using [Firebase Remote Config](https://firebase.google.com/docs/ai-logic/solutions/remote-config) to update parameters in your code remotely (most importantly, model name). |

## Next steps

#### Get started with accessing a model from your mobile or web app

[Go to Getting Started guide](https://firebase.google.com/docs/ai-logic/get-started)


#### Learn more about the supported models

Learn about the [models available for various use cases](https://firebase.google.com/docs/ai-logic/models) and their [quotas](https://firebase.google.com/docs/ai-logic/quotas) and [pricing](https://firebase.google.com/docs/ai-logic/pricing).

<br />