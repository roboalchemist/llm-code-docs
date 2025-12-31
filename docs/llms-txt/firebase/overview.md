# Source: https://firebase.google.com/docs/genkit/overview.md.txt

# Source: https://firebase.google.com/docs/firestore/security/overview.md.txt

# Source: https://firebase.google.com/docs/projects/iam/overview.md.txt

# Source: https://firebase.google.com/docs/ai-logic/solutions/overview.md.txt

<br />

As you develop your app withFirebase AI Logic, you might want to go beyond the basics discussed in the main guides. The solutions outlined in this section offer guidance on more advanced use cases.

## Protect your app from unauthorized clients

For mobile and web apps, you need to protect theGemini APIand your project resources from abuse by unauthorized clients. You can useFirebase App Checkto verify that all API calls are from your actual app.

[See theFirebase App Checkguide](https://firebase.google.com/docs/ai-logic/app-check)
| **Important:** We strongly recommend[implementingApp Checkinto your app](https://firebase.google.com/docs/ai-logic/app-check)as early as possible, even during development, so that every version of your app is protected from API abuse.

## Update values in your app without releasing a new version of your app

If you need to dynamically change values in your app without releasing a new version of your app, you can useFirebase Remote Config. Examples include changing the model name, system instructions, prompts, safety settings, or input for a request.

[See theRemote Configsolution](https://firebase.google.com/docs/ai-logic/solutions/remote-config)
| **Important:** We strongly recommend implementingRemote Configfor[remotely changing the model name in your app](https://firebase.google.com/docs/ai-logic/change-model-name-remotely)as new models are released or others retired.

## Dynamically and conditionally set runtime configurations

If you want to set configurations based on runtime conditions, you can use[Firebase Remote Config](https://firebase.google.com/docs/remote-config). One example is changing the location where you run theVertex AIservice and generative model based on an end-user's location.

[See theRemote Configsolution](https://firebase.google.com/docs/ai-logic/solutions/remote-config)

## Manage files and include large files in multimodal requests

By usingCloud Storage for Firebase, you can take advantage of a fast, secure, and scalable infrastructure for file storage and management. Plus, you can include larger files in your multimodal requests using aCloud Storage for FirebaseURL.

[See theCloud Storage for Firebasesolution](https://firebase.google.com/docs/ai-logic/solutions/cloud-storage)

<br />

We're actively working on other solutions and guides, so check back soon!