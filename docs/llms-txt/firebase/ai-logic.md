# Source: https://firebase.google.com/docs/ai-logic.md.txt

# Gemini APIusingFirebase AI Logic

plat_iosplat_androidplat_webplat_flutterplat_unity  
Build AI-powered mobile and web apps and features with theGeminiandImagenmodels usingFirebase AI Logic  

Firebase AI Logicgives you access to the latest generative AI models from Google: theGeminimodels andImagenmodels.

If you need to call theGemini APIorImagen APIdirectly from your mobile or web app --- rather than server-side --- you can use theFirebase AI Logicclient SDKs. These client SDKs are built specifically for use with mobile and web apps, offering security options against unauthorized clients as well as integrations with other Firebase services.

**These client SDKs are available in Swift for Apple platforms, Kotlin \& Java for Android, JavaScript for web, Dart for Flutter, and Unity.**

With these client SDKs, you can add AI personalization to apps, build an AI chat experience, create AI-powered optimizations and automation, and much more!

[Get started](https://firebase.google.com/docs/ai-logic/get-started)

<br />

**Need more flexibility or server-side integration?**   
[Genkit](https://genkit.dev/)is Firebase's open-source framework for sophisticated server-side AI development with broad access to models from Google, OpenAI, Anthropic, and more. It includes more advanced AI features and dedicated local tooling.

## Key capabilities

|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Multimodal and natural language input             | The[Geminimodels](https://firebase.google.com/docs/ai-logic/models)are multimodal, so prompts sent to theGemini APIcan include text, images, PDFs, video, and audio. SomeGeminimodels can also generate multimodal*output* . Both theGeminiandImagenmodels can be prompted with natural language input.                                                                                                                                                                                                                                                                              |
| Growing suite of capabilities                     | With the SDKs, you can call theGemini APIorImagen APIdirectly from your mobile or web app to[build AI chat experiences](https://firebase.google.com/docs/ai-logic/chat),[generate images,](https://firebase.google.com/docs/ai-logic/generate-images-imagen)use tools (like[function calling](https://firebase.google.com/docs/ai-logic/function-calling)and[grounding with Google Search](https://firebase.google.com/docs/ai-logic/grounding-google-search)),[stream multimodal input and output (including audio)](https://firebase.google.com/docs/ai-logic/live-api), and more. |
| Security and abuse prevention for production apps | Use[Firebase App Check](https://firebase.google.com/docs/ai-logic/app-check)to help protect the APIs that access theGeminiandImagenmodels from abuse by unauthorized clients. Firebase AI Logicalso has[rate limits per user](https://firebase.google.com/docs/ai-logic/faq-and-troubleshooting#rate-limits-per-user)*by default*, and these per-user rate limits are fully configurable.                                                                                                                                                                                            |
| Robust infrastructure                             | Take advantage of scalable infrastructure that's built for use with mobile and web apps, like[managing files withCloud Storage for Firebase](https://firebase.google.com/docs/ai-logic/solutions/cloud-storage), managing structured data with Firebase database offerings (like[Cloud Firestore](https://firebase.google.com/docs/firestore)), and dynamically setting run-time configurations with[Firebase Remote Config](https://firebase.google.com/docs/ai-logic/solutions/remote-config).                                                                                     |

## How does it work?

Firebase AI Logicprovides client SDKs, a proxy service, and other features which allow you to access Google's generative AI models to build AI features in your mobile and web apps.

#### Support for Google models and "Gemini API" providers

We support all the latestGeminimodels andImagenmodels, and you choose your preferred "Gemini API" provider to access these models. We support both theGemini Developer APIandVertex AIGemini API. Learn about the[differences between using the two API providers](https://firebase.google.com/docs/ai-logic/faq-and-troubleshooting#differences-between-gemini-api-providers).

And if you choose to use theGemini Developer API, you can take advantage of their "free tier" to get you up and running fast.

#### Mobile \& web client SDKs

You send requests to the models directly from your mobile or web app using ourFirebase AI Logicclient SDKs, available in Swift for Apple platforms, Kotlin \& Java for Android, JavaScript for Web, Dart for Flutter, and Unity.

If you have both of theGemini APIproviders set up in your Firebase project, then you can switch between API providers just by enabling the other API and changing a few lines of initialization code.

Additionally, our client SDK for Web offers experimental access to[hybrid and on-device inference for web apps](https://firebase.google.com/docs/ai-logic/hybrid-on-device-inference)running on Chrome on desktop. This configuration allows your app to use the on-device model when it's available, but fall back seamlessly to the cloud-hosted model when needed.

#### Proxy service

Our proxy service acts as a gateway between the client and your chosenGemini APIprovider (and Google's models). It provides services and integrations that are important for mobile and web apps. For example, you can[set upFirebase App Check](https://firebase.google.com/docs/ai-logic/app-check)to help protect your chosen API provider and your backend resources from abuse by unauthorized clients.

This is particularly critical if you chose to use theGemini Developer APIbecause our proxy service and thisApp Checkintegration make sure that yourGeminiAPI key stays on the server and is*not*embedded in your apps' codebase.

## Implementation path

|---|---------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | Set up your Firebase project and connect your app to Firebase | Use the guided workflow in the[**Firebase AI Logic**page](https://console.firebase.google.com/project/_/ailogic)of theFirebaseconsole to set up your project (including enabling the required APIs for your chosenGemini APIprovider), register your app with your Firebase project, and then add your Firebase configuration to your app.                                                                                                                                                                                                                                                                                                                                                                                                                              |
|   | Install the SDK and initialize                                | Install theFirebase AI LogicSDK that's specific to your app's platform, and then initialize the service and create a model instance in your app.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|   | Send prompt requests to theGeminiandImagenmodels              | Use the SDKs to send text-only or multimodal prompts to aGeminimodel to generate[text and code](https://firebase.google.com/docs/ai-logic/generate-text),[structured output (like JSON)](https://firebase.google.com/docs/ai-logic/generate-structured-output)and[images](https://firebase.google.com/docs/ai-logic/generate-images-gemini). Alternatively, you can also prompt anImagenmodel to[generate images](https://firebase.google.com/docs/ai-logic/generate-images-imagen). Build richer experiences with[multi-turn chat](https://firebase.google.com/docs/ai-logic/chat),[bidirectional streaming (including audio)](https://firebase.google.com/docs/ai-logic/live-api), and[function calling](https://firebase.google.com/docs/ai-logic/function-calling). |
|   | Prepare for production                                        | Implement important integrations for mobile and web apps, like protecting the API from abuse with[Firebase App Check](https://firebase.google.com/docs/ai-logic/app-check)and using[Firebase Remote Config](https://firebase.google.com/docs/ai-logic/solutions/remote-config)to update parameters in your code remotely (most importantly, model name).                                                                                                                                                                                                                                                                                                                                                                                                                |

## Next steps

#### Get started with accessing a model from your mobile or web app

[Go to Getting Started guide](https://firebase.google.com/docs/ai-logic/get-started)

<br />

#### Learn more about the supported models

Learn about the[models available for various use cases](https://firebase.google.com/docs/ai-logic/models)and their[quotas](https://firebase.google.com/docs/ai-logic/quotas)and[pricing](https://firebase.google.com/docs/ai-logic/pricing).

<br />