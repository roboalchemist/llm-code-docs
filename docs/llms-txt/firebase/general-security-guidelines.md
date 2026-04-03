# Source: https://firebase.google.com/docs/projects/dev-workflows/general-security-guidelines.md.txt

This page describes the most important best practices for security across environments, but review the[*Security checklist*](https://firebase.google.com/support/guides/security-checklist)for more detailed and thorough guidance about security and Firebase.

## Security for pre-production environments

One benefit of separating environments in different Firebase projects is that a malicious actor who is able to access your pre-prod environments won't be able access real user data. Here are the most important security precautions to take for pre-production environments:

- Limit access to pre-prod environments. For mobile apps, use[App Distribution](https://firebase.google.com/docs/app-distribution)(or something similar) to distribute an app to a specific set of people. Web applications are harder to restrict; consider setting up a[blocking function](https://cloud.google.com/identity-platform/docs/blocking-functions)for the pre-prod environments that restricts access to users with email addresses that are specific to your domain. Or, if you're usingFirebase Hosting, set up your pre-prod workflows to use[temporary preview URLs](https://firebase.google.com/docs/hosting/test-preview-deploy).

- When an environment doesn't need to be persisted and is only being used by one person (or in the case of tests, by one machine) use the[Firebase Local Emulator Suite](https://firebase.google.com/docs/emulator-suite). These emulators are safer and faster because they can work entirely on localhost instead of using cloud resources.

- Make sure that you have[Firebase Security Rules](https://firebase.google.com/docs/rules)set up in pre-production environments, just as you do in prod. In general, theRulesshould be the same across environments, with the caveat that since rules change with code, there may be rules earlier in the pipeline that don't yet exist in production.

## Security for production environments

Production data is always a target, even if the app is obscure. Following these guidelines doesn't make it impossible for a malicious actor to get your data, but it makes it more difficult:

- Enable and enforce[App Check](https://firebase.google.com/docs/app-check)for all the products you're using that support it.App Checkmakes sure that requests to your backend services are coming from your genuine apps. In order to use it, you need to register each version of your app withApp Check. It's easier to set up before you have users, so set it up as soon as possible.

- Write robust[Firebase Security Rules](https://firebase.google.com/docs/rules).Realtime Database,Cloud Firestore, andCloud Storageall rely on developer-configuredRulesto enforce who should and shouldn't be able to access data. It's essential to your security that you write goodRules. If you're not sure how, start with this[codelab](https://firebase.google.com/codelabs/firebase-rules).

- Review the[*Security checklist*](https://firebase.google.com/support/guides/security-checklist)for more recommendations about security for production environments.

## Next steps

- Review the[Firebase launch checklist](https://firebase.google.com/support/guides/launch-checklist).