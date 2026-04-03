# Source: https://firebase.google.com/docs/ai-logic/faq-and-troubleshooting.md.txt

<br />

This page provides answers to frequently asked questions (FAQs) and troubleshooting information about theGemini APIand theFirebase AI LogicSDKs.

## Status dashboards

- [Firebase AI Logic](https://status.firebase.google.com/)

- [Gemini Developer API](https://aistudio.google.com/status)

- [Vertex AIGemini API](https://status.cloud.google.com/#:%7E:text=Vertex%20Gemini%20API)(`Vertex Gemini API`and`Vertex Imagen API`)

## General FAQ

<br />

#### Why did the name change from "Vertex AI in Firebase" to "Firebase AI Logic"?

<br />

Back in 2024, we launched a set of Firebase client SDKs that could use theVertex AIGemini APIas well as a Firebase proxy gateway to protect that API from abuse and to enable integrations with other Firebase products. We called our product "Vertex AI in Firebase", and this product name accurately described our product's available use cases at that time.

Since then, though, we've expanded the capabilities of our product. For example, as of May 2025, we now offer support for theGemini Developer API, including the ability to protect theGemini Developer APIfrom abuse using our integration withFirebase App Check.

As a result, the name "Vertex AI in Firebase" no longer accurately represents the expanded scope of our product. Thus,**a new name ---Firebase AI Logic--- better reflects our evolving feature set and allows us to continue to expand our offerings in the future!**

Check out the[migration guide](https://firebase.google.com/docs/ai-logic/migrate-to-latest-sdk)to make sure you get all the latest features fromFirebase AI Logic(and optionally start using theGemini Developer API).

<br />

<br />

<br />

#### What are the differences between using theGemini Developer APIand theVertex AIGemini API?

<br />

The following table lists important differences between the two "Gemini API" providers***in general regardless of how you access them***:

|                                                                                                            |                                     Gemini Developer API                                     |                                                       Vertex AIGemini API                                                       |
|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| [**Pricing**](https://firebase.google.com/docs/ai-logic/pricing)                                           | Available on both the no-cost Spark pricing plan and the pay-as-you-go Blaze pricing plan^1^ | Always requires the pay-as-you-go Blaze pricing plan^1^(when used withFirebase AI Logic)                                        |
| **[Rate limits (quota)](https://firebase.google.com/docs/ai-logic/quotas)**                                | Explicit rate limits                                                                         | Uses dynamic shared quota (DSQ) that everyone using that model in that region shares. Provisioned throughput (PT) is available. |
| [**Specifying the location for accessing the model**](https://firebase.google.com/docs/ai-logic/locations) | not supported by the API                                                                     | supported by the API                                                                                                            |
| **Support for[Cloud StorageURLs](https://firebase.google.com/docs/ai-logic/solutions/cloud-storage)**      | not supported by the API^2^                                                                  | Public files and files protected byFirebase Security Rules                                                                      |
| **Support for YouTube URLs and Browser URLs**                                                              | YouTube URLs only                                                                            | YouTube URLs and Browser URLs                                                                                                   |

^1^*The two API providers have different pay-as-you-go pricing (learn more in their respective documentation).*

^2^*The[Files API](https://ai.google.dev/api/files)for theGemini Developer APIis not supported through theFirebase AI LogicSDKs.*

<br />

The following table lists the availability of commonly asked about features for the two "Gemini API" providers. This table applies***specifically when using theFirebase AI Logicclient SDKs***.

|                                                             Feature                                                             | Gemini Developer API | Vertex AIGemini API |
|---------------------------------------------------------------------------------------------------------------------------------|----------------------|---------------------|
| **Support for[Geminimodels](https://firebase.google.com/docs/ai-logic/models)**                                                 | supported            | supported           |
| **Support for[Imagenmodels](https://firebase.google.com/docs/ai-logic/models)**                                                 | supported            | supported           |
| **Support for Veo models**                                                                                                      | not supported yet    | not supported yet   |
| **Support for the[Gemini Live API](https://firebase.google.com/docs/ai-logic/live-api)**                                        | supported            | supported           |
| **Integration with[Firebase App Check](https://firebase.google.com/docs/ai-logic/app-check)**                                   | supported            | supported           |
| **Compatible with[Firebase Remote Config](https://firebase.google.com/docs/ai-logic/solutions/remote-config)**                  | supported            | supported           |
| **Support for[AI monitoring inFirebaseconsole](https://firebase.google.com/docs/ai-logic/monitoring#ai-monitoring-in-console)** | supported            | supported           |

| **Note:** *When usingFirebase AI Logic* , the following capabilities are**not** yet supported: context caching, fine tuning a model, embeddings generation, semantic retrieval, native audio for theLive API, and some[advanced features ofImagen](https://firebase.google.com/docs/ai-logic/generate-images-imagen#supported-features-requirements)models.

<br />

<br />

<br />

#### Can I use both theGemini Developer APIand theVertex AIGemini API?

<br />

Yes, you can have both "Gemini API" providers enabled in your Firebase project, and you can use both APIs in your app itself.

To switch between API providers in your code, just make sure that you've[set the backend service appropriately in your code](https://firebase.google.com/docs/ai-logic/get-started#initialize-service-and-model).
| **Important:** If your project is on the pay-as-you-go Blaze pricing plan (which is required to use theVertex AIGemini APIand several other products in the Firebase andGoogle Cloudecosystem), be aware that*all calls* to theGemini Developer APIare pay-as-you-go.

<br />

<br />

<br />

#### What are the required APIs? And how do I enable them?

<br />

|--------------------------------------------------------------------------------------------------------------|
| *Select your Gemini API provider to view provider-specific content* Gemini Developer APIVertex AI Gemini API |

To use theFirebase AI LogicSDKs with theGemini Developer API, your project must have the following two APIs enabled:

- [Gemini Developer API](https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com?project=_)(`generativelanguage.googleapis.com`)
- [Firebase AI LogicAPI](https://console.cloud.google.com/apis/library/firebasevertexai.googleapis.com?project=_)(`firebasevertexai.googleapis.com`)

You should enable these two APIs using theFirebaseconsole:

1. In theFirebaseconsole, go to the[**Firebase AI Logic**page](https://console.firebase.google.com/project/_/ailogic).

2. Click**Get started**.

3. Select to get started with theGemini Developer API.

   This launches a guided workflow that enables the two APIs for you. The console will also generate aGeminiAPI key, as well as add theFirebase AI LogicAPI to the allowlist for your Firebase API key.

<br />

<br />

<br />

#### How do I disable APIs in my Firebase project?

<br />

ForFirebase AI Logic, we try to make setup of your Firebase project to use your chosenGemini APIprovider as easy as possible. This includes enabling the[required APIs](https://firebase.google.com/docs/ai-logic/faq-and-troubleshooting#required-apis)in your Firebase project during specific journeys, like the guided workflow in theFirebaseconsole.

However, if you decide to not useFirebase AI Logicor one of theGemini APIproviders, you can disable the associated APIs in your Firebase project.
| **Warning** :**Before you disable an API, be aware of the following:**
|
| - If you disable a required API and you have a feature in your app that relies on that API, then that feature will break across all versions of your app when you disable the API.
| - If you disable theGemini Developer APIor theVertex AIAPI in your Firebase project, then you're disabling its usage for*all use cases* of that API, not just forFirebase AI Logic. Confirm that you're not using the API for other reasons (like withGenkit, the GenAI server-side SDKs, ADK, etc.).
|
| You can check the level of usage for an API in its respective API page in theGoogle Cloudconsole before you disable it (find links to each API page in the instructions below).

<br />

#### Disable APIs associated with usingGemini Developer API

<br />

To use theFirebase AI LogicSDKs with theGemini Developer API, your project must have the following two APIs enabled:

- [Gemini Developer API](https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com?project=_)(`generativelanguage.googleapis.com`)
- [Firebase AI LogicAPI](https://console.cloud.google.com/apis/library/firebasevertexai.googleapis.com?project=_)(`firebasevertexai.googleapis.com`)

**If you want to stop usingFirebase AI Logiccompletely:**

1. Click each API link above to go to the respective API pages in theGoogle Cloudconsole, then click**Manage**.

2. View the**Metrics**tab to verify that there's no usage of the API.

3. If you still want to disable the API, click**Disable API**at the top of the page.

4. Remove theFirebase AI LogicAPI from the list of selected APIs that can be called using your Firebase API keys. Review[this FAQ about the allowlist for Firebase API keys](https://firebase.google.com/docs/projects/api-keys#faq-required-apis-for-restricted-firebase-api-key)to learn about modifying this list.

**If you want to continue usingFirebase AI Logic, but with theVertex AIGemini APIinstead:**

1. Go to the[Gemini Developer API](https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com?project=_)page in theGoogle Cloudconsole, then click**Manage**.

2. View the**Metrics**tab to verify that there's no usage of the API.

3. If you still want to disable the API, click**Disable API**at the top of the page.

4. Make sure that your project has the[required APIs enabled](https://firebase.google.com/docs/ai-logic/faq-and-troubleshooting?api=vertex#required-apis)for theVertex AIGemini API.

<br />

<br />

<br />

#### Disable APIs associated with usingVertex AIGemini API

<br />

To use theFirebase AI LogicSDKs with theVertex AIGemini API, your project must have the following two APIs enabled:

- [Vertex AIAPI](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?project=_)(`aiplatform.googleapis.com`)
- [Firebase AI LogicAPI](https://console.cloud.google.com/apis/library/firebasevertexai.googleapis.com?project=_)(`firebasevertexai.googleapis.com`)

**If you want to stop usingFirebase AI Logiccompletely:**

1. Click each API link above to go to the respective API pages in theGoogle Cloudconsole, then click**Manage**.

2. View the**Metrics**tab to verify that there's no usage of the API.

3. If you still want to disable the API, click**Disable API**at the top of the page.

4. Remove theFirebase AI LogicAPI from the list of selected APIs that can be called using your Firebase API keys. Review[this FAQ about the allowlist for Firebase API keys](https://firebase.google.com/docs/projects/api-keys#faq-required-apis-for-restricted-firebase-api-key)to learn about modifying this list.

**If you want to continue usingFirebase AI Logic, but with theGemini Developer APIinstead:**

1. Go to the[Vertex AIAPI](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?project=_)page in theGoogle Cloudconsole, then click**Manage**.

2. View the**Metrics**tab to verify that there's no usage of the API.

3. If you still want to disable the API, click**Disable API**at the top of the page.

4. Make sure that your project has the[required APIs enabled](https://firebase.google.com/docs/ai-logic/faq-and-troubleshooting?api=dev#required-apis)for theGemini Developer API.

<br />

<br />

<br />

<br />

<br />

#### Which models can be used with theFirebase AI LogicSDKs?

<br />

See[lists of supported models](https://firebase.google.com/docs/ai-logic/models#available-model-names). We frequently add new capabilities to the SDKs, so check back on this FAQ for updates (as well as in release notes, blogs, and social posts).

- **Gemini Developer API**

  - BothGeminiandImagenfoundation models.

    Note that theGemini Developer API(regardless of how it's accessed) only supports[specific stableImagenmodels](https://firebase.google.com/docs/ai-logic/generate-images-imagen?api=dev#models-that-support-capability).
- **Vertex AIGemini API**

  - BothGeminiandImagenfoundation models.
- **Regardless of your chosenGemini APIprovider**

  - Firebase AI Logicdoes***not***support the following:

    - Non-foundationGeminimodels (like PaLM models, tuned models, or Gemma-based models).

    - OlderImagenmodels or`imagen-3.0-capability-001`.

<br />

<br />

<br />

#### What to do when models are retired?

<br />

When we release a stable model version, we strive to ensure that it's available for*at minimum*one year before retiring the model.
| **Note:** When a stable version is released for a given model, all experimental and preview versions of that model will usually be retired within a few days or weeks. Also, model versions that have been announced for retirement will often be restricted to existing projects or to projects that have previously used that model.

#### Where to find the retirement date of a model?

Here are some ways you can find the retirement date of a model:

- **At the time of release** : We list each model's expected retirement date several places in theGemini APIprovider documentation as well as in the Firebase documentation (see the[supported models page](https://firebase.google.com/docs/ai-logic/models#available-model-names)).

- **As the retirement date approaches** : We send emails to appropriate project members, and we post reminders in the release notes and other channels about any upcoming retirements (for example,[reminder of retirement dates](https://firebase.google.com/support/releases#gemini-api-gemini-1.5-and-1.0-models-deprecated)for the Gemini 1.5 and 1.0 stable models).

#### What to do if the model you're using is about to retire?

1. Find a suitable[currently supported model](https://firebase.google.com/docs/ai-logic/models)and its[model name](https://firebase.google.com/docs/ai-logic/models#available-model-names).

2. Update the model name used by your app*before the retirement date*; otherwise, any requests to that model will fail with a 404 error.

   - You set the model name during initialization when you[create a`GenerativeModel`,`LiveModel`, or`ImagenModel`instance](https://firebase.google.com/docs/ai-logic/get-started#initialize-service-and-model). Make sure to review the critical recommendation below about usingFirebase Remote Config.

   - When usingFirebase AI Logic, you*usually*don't need to modify any of the code which actually calls the model.

3. Test your app to ensure that responses are still as expected.

| Because requests to retired models fail,**we strongly recommend that you do*not* hard-code the model and model version into your app's codebase. Instead,[set up and useFirebase Remote Config](https://firebase.google.com/docs/ai-logic/change-model-name-remotely)to control the model and model version used in your app.**
|
| WithRemote Config, you can dynamically and*remotely* change the model and model version used by your app without releasing a new version of your app. Any already released versions of your app (that are configured to useRemote Config) will immediately start using the new model and model name.

#### Retirement dates for the Gemini 1.5 and 1.0 stable models

- Gemini 1.5 Promodels:

  - `gemini-1.5-pro-002`(and`gemini-1.5-pro`): September 24, 2025
  - `gemini-1.5-pro-001`: May 24, 2025
- Gemini 1.5 Flashmodels:

  - `gemini-1.5-flash-002`(and`gemini-1.5-flash`): September 24, 2025
  - `gemini-1.5-flash-001`: May 24, 2025
- Gemini 1.0 Pro Visionmodels: April 21, 2025*(previously scheduled for April 09, 2025)*

- Gemini 1.0 Promodels: April 21, 2025*(previously scheduled for April 09, 2025)*

<br />

<br />

<br />

#### How do I set a per-user rate limit?

<br />

By default,Firebase AI Logicsets the request limit per user at 100 requests per minute (RPM).

If you want to adjust your per-user rate limit, you need to adjust the quota settings for theFirebase AI LogicAPI.

Learn more about the[Firebase AI LogicAPI quota](https://firebase.google.com/docs/ai-logic/quotas). On that page, you can also learn how to view and edit your quota.

<br />

<br />

<br />

#### Which permissions may be needed to use theFirebase AI LogicSDKs?

<br />

<br />

|                      **Action**                       |                                                     **Required IAM permissions**                                                     |                                                                                     **IAM role(s) that include required permissions by default**                                                                                     |
|-------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Upgrade billing to pay-as-you-go (Blaze) pricing plan | `firebase.billingPlans.update` `resourcemanager.projects.createBillingAssignment` `resourcemanager.projects.deleteBillingAssignment` | [Owner](https://firebase.google.com/docs/projects/iam/roles-basic)                                                                                                                                                                   |
| Enable APIs in project                                | `serviceusage.services.enable`                                                                                                       | [Editor](https://firebase.google.com/docs/projects/iam/roles-basic) [Owner](https://firebase.google.com/docs/projects/iam/roles-basic)                                                                                               |
| Create Firebase app                                   | `firebase.clients.create`                                                                                                            | [Firebase Admin](https://firebase.google.com/docs/projects/iam/roles-predefined-all-products) [Editor](https://firebase.google.com/docs/projects/iam/roles-basic) [Owner](https://firebase.google.com/docs/projects/iam/roles-basic) |

<br />

<br />

<br />

<br />

#### DoesFirebase AI Logicuse my data to train models?

<br />

See[Data governance \& Responsible AI](https://firebase.google.com/docs/ai-logic/data-governance).

<br />

<br />

<br />

#### Is MIME type required in my multimodal requests? (like for images, PDFs, video, and audio input)

<br />

Yes, in each multimodal request, you must always provide the following:

- The file's`mimeType`.*See an exception below.*

- The file. You can either provide the file as inline data or provide the file using its URL.

Learn about supported input file types, how to specify MIME type, and the two options for providing the file in[Supported input files and requirements](https://firebase.google.com/docs/ai-logic/input-file-requirements).

#### Exception to including MIME type in your request

An exception to providing the MIME type is inline image inputs for requests from native Android and Apple platform apps.

TheFirebase AI LogicSDKs for Android and Apple platforms provide a simplified and platform-friendly way to handle images in requests --- all images (no matter their format) are converted client-side to JPEG at 80% quality before being sent to the server. This means that**when you provide*images as inline data*using the Android and Apple platforms SDKs, you don't need to specify the MIME type in the request**.

This simplified handling is shown in theFirebase AI Logicdocumentation in the examples for sending base64-encoded images in requests.

Here's some additional platform-specific information about this feature:

- **For Android**:

  - You can take advantage of the simplified way to handle platform-native image types (`Bitmap`) in multimodal prompts that contain images as inline data (see[example](https://firebase.google.com/docs/ai-logic/analyze-images#base64)).

  - For more control over image formats and conversions, you may provide the images as an`InlineDataPart`and supply the specific MIME type. For example:

    `content { inlineData(/* PNG as byte array */, "image/png") }`
- **For Apple platforms**:

  - You can take advantage of the simplified way to handle platform-native image types (`UIImage`,`NSImage`,`CIImage`, and`CGImage`) in multimodal prompts that contain images as inline data (see[example](https://firebase.google.com/docs/ai-logic/analyze-images#base64)).

  - For more control over image formats and conversions, you may provide the images as an`InlineDataPart`and supply the specific MIME type. For example:

    `InlineDataPart(data: Data(/* PNG Data */), mimeType: "image/png")`

<br />

<br />

<br />

#### Are these features available when usingFirebase AI Logic? Context caching, fine tuning a model, embeddings generation, semantic retrieval, and native audio?

<br />

The following features are supported by various models and the API providers, but***they are not available when usingFirebase AI Logic***:

- Context caching
- Fine tuning a model
- Embeddings generation
- Semantic retrieval
- Native audio for theLive API

If you would like to add these as feature requests or vote on an existing feature request, visit[Firebase UserVoice](https://firebase.uservoice.com/forums/948424-general?category_id=501080).

<br />

<br />

<br />

#### For Swift apps on Apple platforms - What to do about the module name change from`FirebaseAI`to`FirebaseAILogic`?

<br />

For Apple platform apps, starting with Firebase SDK v12.5.0,Firebase AI Logicis now distributed under the`FirebaseAILogic`module. We've made this change non-breaking and backwards-compatible.
| **Note:** This FAQ applies if you're currently using the`FirebaseAI`module and you upgrade to v12.5.0+ of the Firebase SDK. If you're using the legacy`FirebaseVertexAI`module, then visit our[migration guide](https://firebase.google.com/docs/ai-logic/migrate-to-latest-sdk).

#### Why did we make this change?

We formerly distributed this service under the`FirebaseAI`module. However, we needed to rename it to`FirebaseAILogic`for the following reasons:

- Avoid a name collision between module and class that causes issues in binary distributions.

- Enable us to use Swift macros for future feature development.

#### What to do if you're upgrading to v12.5.0+?

The module name change to`FirebaseAILogic`is non-breaking and backwards-compatible. However, eventually, we may remove the old module alongside a future major Firebase SDK breaking change release*(time frame currently undetermined)*.

There are***no required changes*** for this module name change, but we***recommend***that you do the following:

1. When choosing Swift PM dependencies, choose`FirebaseAILogic`(instead of`FirebaseAI`).

2. Change import statements to`FirebaseAILogic`(instead of`FirebaseAI`).

<br />

<br />

## GeminiAPI key FAQ

**These FAQ are only applicable if you're using theGemini Developer API.**

<br />

#### What's aGeminiAPI key?

<br />

TheGemini Developer APIuses a "GeminiAPI key" to authorize the caller. So, if you're using theGemini Developer APIthrough theFirebase AI LogicSDKs, then you need a validGeminiAPI key in your Firebase project to make calls to that API.

A "GeminiAPI key" just means an API key that has the[Gemini Developer API](https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com?project=_)in its API allowlist.
| **Note:** TheGemini Developer APIis sometimes called the "Generative Language API" in theGoogle Cloudconsole.

When you go through the[Firebase AI Logicsetup workflow](https://console.firebase.google.com/project/_/ailogic)in theFirebaseconsole, we create aGeminiAPI key that's restricted to only theGemini Developer API, and we set up theFirebase AI Logicproxy service to use this API key. This Firebase-generatedGeminiAPI key is named*Gemini Developer API key (auto created by Firebase)* in the credentials page of theGoogle Cloudconsole.

Learn more about[API restrictions for API keys](https://cloud.google.com/docs/authentication/api-keys#adding-api-restrictions).

You do***not*** add yourGeminiAPI key to your app's codebase when using theFirebase AI LogicSDKs. Learn more about how to[keep yourGeminiAPI key secure](https://firebase.google.com/docs/ai-logic/faq-and-troubleshooting#keep-gemini-api-key-secure).

<br />

<br />

<br />

#### Should I add myGeminiAPI key into my mobile or web app's codebase?

<br />

When using theFirebase AI LogicSDKs, do***not*** add yourGeminiAPI key into your app's codebase.

In fact, while developing with theFirebase AI LogicSDKs, you don't directly interact with yourGeminiAPI key. Instead, ourFirebase AI Logicproxy service will internally include theGeminiAPI key in each request to theGemini Developer API--- completely in the backend.
| As soon as you start seriously developing your app,**it's critical that you[integrate withFirebase App Check](https://firebase.google.com/docs/ai-logic/app-check)**so that only requests from your actual app and verified devices are passed through to the backend.

<br />

<br />

<br />

#### How can I change theGeminiAPI key used to call theGemini Developer API?

<br />

When using theFirebase AI LogicSDKs, it's unlikely that you'll need to change yourGeminiAPI key. However, here are two cases where you might need to:

- If you accidentally leaked the key and want to replace it with a new secure key.

- If you accidentally deleted the key. Note that you can[undelete the key](https://cloud.google.com/docs/authentication/api-keys#undelete)within 30 days of deletion.

**Here's how you change theGeminiAPI key that's used by theFirebase AI LogicSDKs:**

1. If your Firebase-generatedGeminiAPI key still exists, delete it.

   You can delete this API key in the[*APIs \& Services* \>*Credentials*panel](https://console.cloud.google.com/apis/credentials?project=_)of theGoogle Cloudconsole. It's named:  
   *Gemini Developer API key (auto created by Firebase)*.
2. In that same page of theGoogle Cloudconsole,[create a new API key.](https://cloud.google.com/docs/authentication/api-keys#create)We suggest naming it something like:  
   *Gemini Developer API key for Firebase*.

3. To this new API key,[add API restrictions](https://cloud.google.com/docs/authentication/api-keys#adding-api-restrictions)and only select**Generative Language API** .  
   "Generative Language API" is what theGemini Developer APIis sometimes called in theGoogle Cloudconsole.

   Do***not*** add any[app restrictions](https://cloud.google.com/docs/authentication/api-keys#adding-application-restrictions); otherwise theFirebase AI Logicproxy service won't work as expected.
4. Run the following command to set this new key as theGeminiAPI key that theFirebase AI Logicproxy service should use.

       PROJECT_ID="<var translate="no">PROJECT_ID</var>"
       GENERATIVE_LANGUAGE_API_KEY="<var translate="no">DEVELOPER_CREATED_GEMINI_API_KEY</var>"
       curl \
         -X PATCH \
         -H "x-goog-user-project: ${PROJECT_ID}" \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://firebasevertexai.googleapis.com/v1beta/projects/${PROJECT_ID}/locations/global/config" \
         -d "{\"generativeLanguageConfig\": {\"apiKey\": \"${GENERATIVE_LANGUAGE_API_KEY}\"}}"

   Learn about the[gcloud CLI](https://cloud.google.com/sdk/docs/install).

Make sure to***not*** add this newGeminiAPI key to your app's codebase. Learn more about how to[keep yourGeminiAPI key secure](https://firebase.google.com/docs/ai-logic/faq-and-troubleshooting#keep-gemini-api-key-secure).
| **Note:** You can always[reach out to Firebase Support](https://firebase.google.com/support/troubleshooter/contact)for questions and guidance when working with API keys.

<br />

<br />

<br />

#### Can I use my "Firebase API key" as myGeminiAPI key?

<br />

No --- you should***not*** use your "Firebase API key" as yourGeminiAPI key. We strongly recommend that you do***not*** add theGemini Developer APIto the allowlist for your Firebase API key.

Your Firebase API key is the API key that's listed in your Firebase configuration file or object that you add into your app's codebase to connect your app to Firebase.**It's OK to include your Firebase API key in your code*when you use the key only with Firebase-related APIs (likeFirebase AI Logic)*.** [Learn important information about Firebase API keys](https://firebase.google.com/docs/projects/api-keys).

In the[*APIs \& Services* \>*Credentials*panel](https://console.cloud.google.com/apis/credentials?project=_)of theGoogle Cloudconsole, this is what Firebase API keys look like:

![API keys automatically created by Firebase for your Firebase Apps](https://firebase.google.com/static/docs/projects/images/api-keys-from-firebase-cloud-console.png)

Because you need to add your Firebase API key into your app's codebase for Firebase-related APIs to work, and because theGemini Developer APIis*authorized* via API key,**we strongly recommend that you do NOT add theGemini Developer API(called the "Generative Language API" in theGoogle Cloudconsole) to the API allowlist for your Firebase API key** . If you do, then you're exposing theGemini Developer APIto potential abuse.

<br />

<br />

<br />

#### How do I keep myGeminiAPI key secure?

<br />

This FAQ describes some recommended best practices to keep yourGeminiAPI key secure.

**If you're calling theGemini Developer APIdirectly from your mobile or web app:**

- Use theFirebase AI Logicclient SDKs.
- Do***not*** add yourGeminiAPI key into your app's codebase.

Firebase AI Logicprovides a proxy service that internally includes yourGeminiAPI key in each request to theGemini Developer API--- completely in the backend.

**Additionally, we strongly recommend the following:**

- As soon as you start seriously developing your app,[integrate withFirebase App Check](https://firebase.google.com/docs/ai-logic/app-check)to help protect your backend resources as well as the APIs used to access generative models.

- Do***not*** reuse the Firebase-generatedGeminiAPI key outside ofFirebase AI Logic. If you need aGeminiAPI key for another use case, create a separate key.

- In general, you should NOT modify the Firebase-generatedGeminiAPI key. This key is named*Gemini Developer API key (auto created by Firebase)* in theGoogle Cloudconsole.

  - Do***not*** add any additional APIs to the API allowlist for your Firebase-generatedGeminiAPI key. In its API allowlist, yourGeminiAPI key should***only*** have theGemini Developer API(called the "Generative Language API" in theGoogle Cloudconsole).

  - Do***not*** add any[app restrictions](https://cloud.google.com/docs/authentication/api-keys#adding-application-restrictions); otherwise theFirebase AI Logicproxy service won't work as expected.

<br />

<br />

<br />

#### MyGeminiAPI key was compromised. What do I need to do?

<br />

If yourGeminiAPI key has been compromised, follow the instructions to[change theGeminiAPI key](https://firebase.google.com/docs/ai-logic/faq-and-troubleshooting#change-gemini-api-key)that's used to call theGemini Developer API.

Also, review the recommended best practices to[keep yourGeminiAPI key secure](https://firebase.google.com/docs/ai-logic/faq-and-troubleshooting#keep-gemini-api-key-secure).

<br />

<br />

## Troubleshoot errors

<br />

#### How do I fix this 404 error?`Firebase AI Logic genai config not found`

<br />

If you're attempting to use theGemini Developer APIand you receive a 404 error that says`Firebase AI Logic genai config not found`, it usually means that your Firebase project doesn't have a validGeminiAPI key for use with theFirebase AI Logicclient SDKs.

Here are the most likely causes of this error:

- You haven't yet set up your Firebase project for theGemini Developer API.

  What to do:  
  In theFirebaseconsole, go to the[**Firebase AI Logic**page](https://console.firebase.google.com/project/_/ailogic). Click**Get started** , and then select the**Gemini Developer API** . Enable the API, and the console will set up your project for theGemini Developer API. After completing the workflow, try your request again.
- If you very recently went through theFirebase AI Logicsetup workflow in theFirebaseconsole, then yourGeminiAPI key might not yet be available to all required backend services in all regions.

  What to do:  
  Wait a few minutes, and then try your request again.
- YourGeminiAPI key might have been deleted from your Firebase project.

  What to do:  
  Learn how to[change theGeminiAPI key used byFirebase AI Logic](https://firebase.google.com/docs/ai-logic/faq-and-troubleshooting#change-gemini-api-key).

<br />

<br />

<br />

#### How do I fix this 400 error?`Service agents are being provisioned ... Service agents are needed to read the Cloud Storage file provided.`

<br />

If you're trying to send a multimodal request with aCloud Storage for FirebaseURL, you might encounter the following 400 error:  
`Service agents are being provisioned ... Service agents are needed to read the Cloud Storage file provided.`

This error is caused by a project that didn't have the required service agents correctly auto-provisioned when theVertex AIAPI was enabled in the project. This is a known issue with some projects, and we're working on a global fix.

Here's the workaround to fix your project and correctly provision these service agents so that you can start includingCloud Storage for FirebaseURLs in your multimodal requests. You must be an[Owner](https://firebase.google.com/docs/projects/iam/roles-basic)on the project, and you only need to complete this set of tasks once for your project.

1. Access and authenticate with thegcloud CLI.  
   The easiest way to do this is fromCloud Shell. Learn more in the[Google Clouddocumentation](https://cloud.google.com/shell/docs/launching-cloud-shell).

2. If prompted, follow the instructions displayed in the terminal to make thegcloud CLIrun against your Firebase project.

   You'll need your Firebase project ID, which you can find at the top of thesettings[*Project settings*](https://console.firebase.google.com/project/_/settings/general/)in theFirebaseconsole.
3. Provision the required service agents in your project by running the following command:

   ```
   curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"  https://us-central1-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/endpoints -d ''
   ```
4. Wait a few minutes to ensure that the service agents are provisioned, and then retry sending your multimodal request that includes theCloud Storage for FirebaseURL.

If you're still getting this error after waiting several minutes, reach out to[Firebase Support](https://firebase.google.com/support/troubleshooter/contact).

<br />

<br />

<br />

#### How do I fix this 400 error?`API key not valid. Please pass a valid API key.`

<br />

If you receive a 400 error that says`API key not valid. Please pass a valid API key.`, it usually means that the API key in your Firebase configuration file/object doesn't exist or isn't setup to be used with your app and/or Firebase project.

Check that the API key listed in your Firebase configuration file/object matches the API key for your app. You can view all your API keys in the[*APIs \& Services* \>*Credentials*](https://console.cloud.google.com/apis/credentials?project=_)panel in theGoogle Cloudconsole.

If you discover that they don't match, then[obtain a fresh Firebase configuration file/object](https://support.google.com/firebase/answer/7015592), and then*replace*the one that's in your app. The fresh config file/object should contain a valid API key for your app and Firebase project.

<br />

<br />

<br />

#### How do I fix this 403 error?`Requests to this API firebasevertexai.googleapis.com ... are blocked.`

<br />

If you receive a 403 error that says`Requests to this API firebasevertexai.googleapis.com ... are blocked.`, it usually means that the API key in your Firebase configuration in your app has restrictions that prevent it from calling the required API.

To fix this, you need to update your API key's restrictions in theGoogle Cloudconsole to include the required API. ForFirebase AI Logic, you must ensure the*Firebase AI LogicAPI* (`firebasevertexai.googleapis.com`) is included in the list of selected APIs that can be called using the API key.

Follow these steps:

1. In theGoogle Cloudconsole, open the[*APIs \& Services* \>*Credentials*](https://console.cloud.google.com/apis/credentials?project=_)panel.

2. Select the API key that your application is configured to use (for example, the "iOS key" for an iOS app).

3. On the*Edit API key* page, find the*API restrictions*section.

4. Ensure the**Restrict key**option is selected. If it isn't, your key is unrestricted, and this is likely not the source of the error.

   | **Note:** If you have an unrestricted API key, we strongly recommend that you apply["API restrictions"](https://firebase.google.com/docs/projects/api-keys#faq-required-apis-for-restricted-firebase-api-key)to your Firebase API key.
5. In the*Selected APIs* drop-down menu, search for and select the*Firebase AI LogicAPI*to add it to the list of selected APIs that can be called using the API key.

6. Click**Save**.

   It may take up to five minutes for the changes to take effect.

| **Note:** Firebase-related APIs use API keys only to*identify* the Firebase project or app,*not for authorization* to call the API (like some other APIs allow). Authorization for Firebase-related APIs is handled separately from the API key, either throughGoogle CloudIAM permissions,Firebase Security Rules, orFirebase App Check. Learn more about[Firebase API keys](https://firebase.google.com/docs/projects/api-keys).

<br />

<br />

<br />

#### How do I fix this 403 error?`PERMISSION_DENIED: The caller does not have permission.`

<br />

If you receive a 403 error that says`PERMISSION_DENIED: The caller does not have permission.`, it usually means that the API key in your Firebase configuration file/object belongs to a different Firebase project.

Check that the API key listed in your Firebase configuration file/object matches the API key for your app. You can view all your API keys in the[*APIs \& Services* \>*Credentials*](https://console.cloud.google.com/apis/credentials?project=_)panel in theGoogle Cloudconsole.

If you discover that they don't match, then[obtain a fresh Firebase configuration file/object](https://support.google.com/firebase/answer/7015592), and then*replace*the one that's in your app. The fresh config file/object should contain a valid API key for your app and Firebase project.

<br />

<br />

<br />

#### How do I fix the 404 error that says a model "`was not found or your project does not have access to it`"?

<br />

<br />

For example: "`Publisher Model projects/PROJECT-ID/locations/us-central1/publishers/google/models/gemini-3-pro-image-preview was not found or your project does not have access to it. Please ensure you are using a valid model version.`"

<br />

There are a couple different reasons why you could get an error like this.

- **Invalid model name**

  - **Cause**: The model name you've provided isn't a valid model name.

  - **Fix** : Check your model name and model version against the list of all[supported and available models](https://firebase.google.com/docs/ai-logic/models#available-model-names). Be sure to check the segments and their order in the model name. For example:

    - TheGemini 3 Propreview model name is`gemini-3-pro-preview`.
    - The "nano banana pro" preview model name is`gemini-3-pro-image-preview`.
    - The "nano banana" model name is`gemini-2.5-flash-image`.
- **Invalid location** *(only applicable if using theVertex AIGemini APIprovider and a**preview** or**experimental**model)*

  - **Cause** : You're using a*preview* or*experimental* version of a model (for example,`gemini-3-pro-preview`and`gemini-3-pro-image-preview`), and you didn't specify the`global`location.

    If you use theVertex AIGemini API, all*preview* and*experimental* Geminimodels (except Gemini Live models) are only available in the`global`location. However, sinceFirebase AI Logicdefaults to the`us-central1`location, you need to explicitly specify the`global`location when initializing theVertex AIGemini APIbackend service in your code when using these*preview* and*experimental* Geminimodels.
  - **Fix** : When you initialize theVertex AIGemini APIservice, specify the location`global`. Learn more about how to[specify the location for accessing the model](https://firebase.google.com/docs/ai-logic/locations?api=vertex)(including code snippets).

- **Invalid location** *(only applicable if using theVertex AIGemini APIprovider)*

  - **Cause**: You're using a model that's not supported in the location where you're trying to access it.

    If you use theVertex AIGemini API,[some models are only available in specific locations](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/locations#google_model_endpoint_locations). For example (but not exhaustive):
    - Imagenmodels are*not* supported in the`global`location.
    - Gemini Live APImodels (like`gemini-2.0-flash-live-preview-04-09`) are*only* supported in the`us-central1`location.
    - Gemini 2.5 models (like`gemini-2.5-pro`) are*only* available in the`global`location, the US locations, and some European locations (and sometimes in other locations if your project has special options).
  - **Fix** : When you initialize theVertex AIGemini APIservice, make sure that you specify a supported location for the model that you're using. Learn more about how to[specify the location for accessing the model](https://firebase.google.com/docs/ai-logic/locations?api=vertex)(including code snippets) and the[supported locations for models](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/locations#google_model_endpoint_locations).

    Note thatFirebase AI Logicdefaults to the`us-central1`location.

<br />

<br />

<br />

#### How do I fix this 429 error?`"You exceeded your current quota, please check your plan and billing details"`?

<br />

429 errors indicate that you're going over your quota. The action to take depends on whether you're using theGemini Developer APIorVertex AIGemini API. For more information about quotas and how to request additional quota, see[Rate limits and quotas](https://firebase.google.com/docs/ai-logic/quotas).
| **Important:** Starting on December 7, 2025, theGemini Developer APIquota for both the Free Tier and Paid Tier 1 were adjusted. These changes may lead to unexpected 429 quota-exceeded errors.

<br />

<br />

<br />

[Give feedback about your experience withFirebase AI Logic](https://firebase.google.com/docs/ai-logic/feedback)

<br />