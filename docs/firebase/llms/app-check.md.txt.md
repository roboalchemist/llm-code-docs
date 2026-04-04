# Source: https://firebase.google.com/docs/ai-logic/app-check.md.txt

When you call an API directly from a mobile or web app (for example, the APIs
that allow access to generative AI models), the API is vulnerable to abuse by
unauthorized clients. To help protect these APIs, you can use
[Firebase App Check](https://firebase.google.com/docs/app-check) to verify that all incoming API calls
are from your actual app.

Firebase AI Logic provides a proxy gateway that lets you integrate with
Firebase App Check and protect the generative AI model APIs called by your
mobile and web apps. Using App Check with the
Firebase AI Logic SDKs supports all our configurations:

- Protects both "Gemini API" providers: Gemini Developer API and
  Vertex AI Gemini API.

- Protects all supported models, both Gemini models and Imagen
  models.

> [!CAUTION]
> We **strongly recommend implementing
> Firebase App Check into your app as early as possible**, even during development, so that every version of your app is protected from API abuse.

## High-level summary of how App Check works

With App Check, devices running your app use an app or device attestation
provider that verifies one or both of the following:

- Requests originate from your authentic app
- Requests originate from an authentic, untampered device

This attestation is attached to every request your app makes using a
Firebase AI Logic SDK. When you enable App Check enforcement,
requests from clients without a valid attestation will be rejected, as will any
request originating from an app or platform you haven't authorized.

We recommend that when you set up App Check, make sure to
[prepare for upcoming enhanced protection](https://firebase.google.com/docs/ai-logic/app-check#enhanced-protection)
(known as *replay protection*).

You can find [detailed information about App Check](https://firebase.google.com/docs/app-check) in its
documentation, including its [quotas and limits](https://firebase.google.com/docs/app-check#quotas_limits).

## Available providers and implementation instructions

The App Check documentation provides descriptions of attestation providers
as well as implementation instructions.

1. Choose a default provider, and follow the implementation instructions at the
   following links:

   - **Apple platforms** : [DeviceCheck](https://firebase.google.com/docs/app-check/ios/devicecheck-provider) or [App Attest](https://firebase.google.com/docs/app-check/ios/app-attest-provider)
   - **Android** : [Play Integrity](https://firebase.google.com/docs/app-check/android/play-integrity-provider)
   - **Web** : [reCAPTCHA Enterprise](https://firebase.google.com/docs/app-check/web/recaptcha-enterprise-provider)
   - **Flutter** : Supports [all the default providers above](https://firebase.google.com/docs/app-check/flutter/default-providers)   
     Also, make sure to follow [special instantiation requirements](https://firebase.google.com/docs/ai-logic/app-check#instantiation-flutter) for Flutter and App Check.
   - **Unity** : Supports [all the default providers above](https://firebase.google.com/docs/app-check/unity/default-providers)

   Note that if none of the default providers are sufficient for your needs,
   then you can [implement a custom provider](https://firebase.google.com/docs/app-check/custom-provider)
   that uses either a third-party attestation provider or your own attestation
   techniques.
2. *(Recommended)*
   [Prepare for upcoming enhanced protection from App Check](https://firebase.google.com/docs/ai-logic/app-check#enhanced-protection)
   (known as *replay protection*).

3. *(Required)* Before you release your app to real users,
   [**enable enforcement of App Check**](https://firebase.google.com/docs/app-check/enable-enforcement).

### Special instantiation required for Flutter

|---|
| *Click your Gemini API provider to view provider-specific content and code on this page.* <button value="dev" default="">Gemini Developer API</button> <button value="vertex">Vertex AI Gemini API</button> |

When using App Check with Firebase AI Logic in Flutter apps, you need to
explicitly pass in App Check during instantiation, like so:

    // ...

    final ai = await FirebaseAI.googleAI(
      appCheck: FirebaseAppCheck.instance, // for Flutter, pass in App Check explicitly
    );

    // ...

## Prepare for upcoming enhanced protection

|---|
| ***Enabling the usage of limited-use tokens is supported for Apple platforms (v12.2.0+), Android (v17.2.0+, BoM v34.2.0+), Web (v12.3.0+), and Flutter (v3.2.0+, BoM v4.2.0+).** Support for Unity is coming soon.* |

By default, App Check uses *session tokens* which have a configurable
time to live (TTL) between 30 minutes and 7 days.
These session tokens are cached by the App Check SDK and sent along with
requests from your app.

In the future, App Check will add the option to enable *replay protection*
for Firebase AI Logic (similar to the support that App Check already
offers for some other resources). When replay protection is enabled, it
enhances protection in the following ways:

- App Check will only allow requests if they're accompanied by a special
  kind of token called a *limited-use token*.

- After the limited-use token is verified, the token is consumed so that it can
  be used only once, preventing replay attacks.

**To prepare for replay protection, we recommend that you
[enable the usage of limited-use tokens](https://firebase.google.com/docs/ai-logic/app-check#enable-limited-use-tokens)** as part
of setting up App Check. That way, when replay protection becomes available,
then you can enable it sooner because more of your users will be on versions
of your app that send limited-use tokens.

Note the following if you enable usage of limited-use tokens in your app now
(while replay protection is unavailable):

- App Check does *not* block the usage of *valid session tokens*.

- Just like session tokens, limited-use tokens are cached by the
  App Check SDK and sent along with requests. These limited-use tokens
  provide a *small* amount of additional protection than the default session
  tokens because limited-use tokens have a shorter TTL
  (only 5 minutes and not adjustable) compared to session tokens.

- Even though limited-use tokens are valid for 5 minutes, the SDK
  will still generate a new token for *each* request. This process can add some
  latency to your request.

However, when replay protection is available for Firebase AI Logic in the
future (and you enable it), the use of session tokens and the reuse of
limited-use tokens won't be possible. Note that the additional latency for
generating a new token for each request will still happen.

### Enable usage of limited-use tokens

|---|
| *Click your Gemini API provider to view provider-specific content and code on this page.* <button value="dev" default="">Gemini Developer API</button> <button value="vertex">Vertex AI Gemini API</button> |

> [!NOTE]
> **Note:** Consider setting up limited-use tokens to be a Firebase Remote Config parameter so that you can control its setting remotely rather than having it hard-coded in your app. Learn more about [using Remote Config](https://firebase.google.com/docs/ai-logic/solutions/remote-config).

Here's how to enable usage of limited-use tokens:

1. [Implement App Check](https://firebase.google.com/docs/ai-logic/app-check#available-providers), and make sure that you've
   [enabled App Check enforcement](https://firebase.google.com/docs/app-check/enable-enforcement)
   for your app.

2. In your app during instantiation, enable the usage of limited-use tokens by
   setting the `useLimitedUseAppCheckTokens` parameter to `true`:

   ### Swift


       // ...

       // During instantiation, enable usage of limited-use tokens
       let ai = FirebaseAI.firebaseAI(
         backend: .googleAI(),
         useLimitedUseAppCheckTokens: true
       )

       // ...

   ### Kotlin


       // ...

       // During instantiation, enable usage of limited-use tokens
       val ai = Firebase.ai(
         backend = GenerativeBackend.googleAI(),
         useLimitedUseAppCheckTokens = true
       )

       // ...

   ### Java


       // ...

       // During instantiation, enable usage of limited-use tokens
       FirebaseAI ai = FirebaseAI.getInstance(
         /* backend: */ GenerativeBackend.googleAI(),
         /* useLimitedUseAppCheckTokens: */ true
       );

       // ...

   ### Web


       // ...

       // During instantiation, enable usage of limited-use tokens
       const ai = getAI(firebaseApp, {
         backend: new GoogleAIBackend(),
         useLimitedUseAppCheckTokens: true
       });

       // ...

   ### Dart


       // ...

       // During instantiation, enable usage of limited-use tokens
       final ai = await FirebaseAI.googleAI(
         appCheck: FirebaseAppCheck.instance, // for Flutter, pass in App Check explicitly
         useLimitedUseAppCheckTokens: true,
       );

       // ...

   ### Unity

   Using limited-use tokens with Unity games will be supported in a
   future release. Check back soon!

## Understand how Firebase AI Logic integrates with App Check

To use the Firebase AI Logic SDKs, the
[Firebase AI Logic API (`firebasevertexai.googleapis.com`)](https://console.cloud.google.com/apis/library/firebasevertexai.googleapis.com?project=_)
must be enabled in your Firebase project. This is because requests made by the
Firebase AI Logic SDKs are first sent to the Firebase AI Logic
server, which acts as a proxy gateway where Firebase App Check verification
takes place *before* the request is allowed to proceed to your chosen
"Gemini API" provider's backend and the APIs to access the Gemini
and Imagen models.