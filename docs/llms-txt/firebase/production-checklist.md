# Source: https://firebase.google.com/docs/ai-logic/production-checklist.md.txt

<br />

When you're ready to launch your app and have real end users interact with your generative AI features, make sure to review this checklist of best practices and important considerations.
| You can complete many of these checklist items as soon as you start to seriously develop your app and well before launch.  
| **Most importantly, you should enable[Firebase App Check](https://firebase.google.com/docs/ai-logic/app-check)to help secure your app and configure[Firebase Remote Config](https://firebase.google.com/docs/ai-logic/solutions/remote-config)to allow on-demand changes to AI parameters (like model name) without an app update.**

## General

### Review the general launch checklist for apps that use Firebase

This[Firebase launch checklist](https://firebase.google.com/support/guides/launch-checklist)describes important best practices before launching any Firebase app to production.

### Make sure your Firebase projects follow best practices

For example, make sure that you use different Firebase projects for development, testing, and production. Review more best practices for[managing your projects](https://firebase.google.com/support/guides/launch-checklist#projects-follow-best-practices).

## Access and security

### Review the general security checklist for apps that use Firebase

This[security checklist](https://firebase.google.com/support/guides/security-checklist)describes important best practices for access and security for Firebase apps and services.

### Start*enforcing* Firebase App Check

[Firebase App Check](https://firebase.google.com/docs/ai-logic/app-check)helps protect the APIs that give you access to theGeminiandImagenmodels.App Checkverifies that requests are from your actual app and an authentic, untampered device. It supports attestation providers for Apple platforms (DeviceCheck or App Attest), Android (Play Integrity), and Web (reCAPTCHA Enterprise), and it supports all these providers for Flutter and Unity apps, as well.

Also, to[prepare for upcoming enhanced protection fromApp Check](https://firebase.google.com/docs/ai-logic/app-check#enhanced-protection)through*replay protection*, we recommend enabling the usage of limited-use tokens in your apps.

### Set up restrictions for your Firebase API keys

- Review each Firebase API key's["API restrictions"](https://cloud.google.com/docs/authentication/api-keys#adding_api_restrictions)allowlist:

  - Make sure that theFirebase AI LogicAPI is in the allowlist.

  - Make sure that the only other APIs in the key's allowlist are for Firebase services that you use in your app. See the[list of which APIs are required to be on the allowlist for each product](https://firebase.google.com/docs/projects/api-keys#faq-required-apis-for-restricted-firebase-api-key).

- Set["Application restrictions"](https://cloud.google.com/docs/authentication/api-keys#adding_application_restrictions)to help restrict usage of each Firebase API key to only requests from your app (for example, a matching bundle ID for the Apple app). Note that even if you restrict your key,Firebase App Checkis still strongly recommended.

Note that Firebase-related APIs use API keys only to*identify* the Firebase project or app,*not for authorization*to call the API.

## Billing, monitoring, and quota

### Avoid surprise bills

If your Firebase project is on the pay-as-you-go Blaze pricing plan, then[monitor your usage](https://firebase.google.com/docs/ai-logic/monitoring)and[set up budget alerts](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills#set-up-budget-alert-emails).

### Set up AI monitoring in theFirebaseconsole

[Set up AI monitoring](https://firebase.google.com/docs/ai-logic/monitoring#ai-monitoring-in-console)to gain visibility into key performance metrics, like requests, latency, errors, and token usage. AI monitoring also helps you inspect and debug yourFirebase AI Logicfeatures by surfacing individual traces.

### Review your quotas for the required underlying APIs

- Make sure that you[understand the quotas for each required API](https://firebase.google.com/docs/ai-logic/quotas#understand-quotas).

- [Set rate limits per user](https://firebase.google.com/docs/ai-logic/quotas#understand-quotas-vertexai-in-firebase)(the default is 100 RPM).

- [Edit quota or request a quota increase](https://firebase.google.com/docs/ai-logic/quotas#edit-quota-or-request-quota-increase), as needed.

## Management of configurations

### Use a stable model version in your production app

In your production app, only use[*stable*model versions](https://firebase.google.com/docs/ai-logic/models#versions)(like`gemini-2.0-flash-001`), not a*preview* or*experimental* version or an*auto-updated*alias.

Even though an*auto-updated* stable alias points to a stable version, the actual model version it points to will automatically change whenever a new stable version is released, which could mean unexpected behavior or responses. Also,*preview* and*experimental*versions are only recommended during prototyping.
| **Important:** We strongly recommend using[Firebase Remote Config](https://firebase.google.com/docs/ai-logic/change-model-name-remotely)to control and update the model name used in your app (see the next section).

### Set up and useFirebase Remote Config

WithRemote Config, you can control important configurations for your generative AI features*in the cloud*rather than hard-coding values in your code. This means that you can update your configuration without releasing a new version of your app.

- *(Strongly Recommended)* [Remotely change the model name used in your app](https://firebase.google.com/docs/ai-logic/change-model-name-remotely)as new models are released or others are retired.

- *(Optional)* [Dynamically and even conditionally control other parameters in your app](https://firebase.google.com/docs/ai-logic/solutions/remote-config), like model generation configuration (maximum tokens, temperature, etc.), safety settings, system instructions, and prompt data.

- *(Optional)* Set a`minimum_version`parameter inRemote Configto compare the app's current version with theRemote Config-defined latest version, to either show an upgrade notification to users or force users to upgrade.

### Set the location for accessing the model

<br />

|-------------------------------------------------------------------------|
| *Only available when using theVertex AIGemini APIas your API provider.* |

<br />

[Setting a location for accessing the model](https://firebase.google.com/docs/ai-logic/locations)can help with costs as well as help prevent latency for your users.

If you don't specify a location, the default is`us-central1`. You can set this location during initialization, or you can optionally[useFirebase Remote Configto dynamically change the location based on each user's location](https://firebase.google.com/docs/ai-logic/solutions/remote-config).