# Source: https://firebase.google.com/docs/app-hosting.md.txt

# Firebase App Hosting

[Video](https://www.youtube.com/watch?v=saQ7Ab8ETkY)

Firebase App Hosting streamlines the development and deployment of dynamic
web apps, offering GitHub integration and integration with other Firebase
products like Authentication, Cloud Firestore, and Firebase AI Logic.
App Hosting has built-in, preconfigured support for Next.js and Angular
as well as broader support for various popular web frameworks.

[Get started](https://firebase.google.com/docs/app-hosting/get-started)

## Key capabilities

|---|---|
| GitHub integration | A git commit is all that's needed to roll out a new version of your app. App Hosting can automatically deploy every time you push to a specific branch. |
| Backed by Google Cloud | App Hosting uses Google Cloud Terms of Service, and deploys your app to Google Cloud products you trust. Apps are built with Cloud Build, served on Cloud Run, and cached in Cloud CDN. Integrated services like Cloud Secret Manager keep your API keys safe. |
| Ship AI-powered features at scale | Start with AI samples that use Gemini. Protect your API endpoint's API key with Cloud Secret Manager and leverage App Hosting's streaming support to maintain fast initial load times as you add generative AI features into your app. |
| Firebase console integration | Monitor your builds and rollouts in the Firebase console so you always know what's going on. Access logs and metrics, add a custom domain, and manually trigger rollouts from the Firebase console. |

## How does it work?

1. Using the Firebase console or Firebase CLI, authorize and install the Firebase GitHub app on your repository.
2. Still in the Firebase console or Firebase CLI, create a Firebase App Hosting backend, with a repository and live branch for continuous deployment. App Hosting creates a default rollout policy for your backend to roll out to 100% of traffic immediately when a change is pushed to the target branch.
3. When a commit is pushed to your live branch, Google Cloud Developer Connect sends an event to Firebase App Hosting.
4. Responding to this event, Firebase App Hosting creates a new build for the backend connected to the repository.
   1. First, Firebase App Hosting creates a new Cloud Build build for your commit. In this job, [Google Cloud buildpacks](https://cloud.google.com/docs/buildpacks/overview) determine which framework is being used in your application to create a container and configuration (including environment variables, secrets, minimum or maximum instances, concurrency memory, CPU, and VPC configuration) that suits your application. See [the App Hosting build process](https://firebase.google.com/docs/app-hosting/build) For more information.
   2. When the Cloud Build job is complete, your container is stored in an Artifact Registry repository dedicated to Firebase App Hosting. Firebase App Hosting then adds a new Cloud Run Revision to a Cloud Run service using your image and configuration.
5. Once your Cloud Run Revision is complete and verified healthy, Firebase App Hosting modifies its traffic configuration to point all new requests to your new Cloud Run Revision. At this point, the rollout is complete.
6. When a request is sent to a website hosted on Firebase App Hosting, the request is served by Google Cloud Load Balancer with Cloud CDN enabled. Uncached requests are sent to your Cloud Run service.

## Implementation path

|---|---|---|
|   | Set up Firebase | If you don't already have one, create a Firebase project and make sure it has the Blaze pricing plan enabled. |
|   | Set up App Hosting | With the Firebase console or the Firebase CLI, create an App Hosting backend. This is the collection of managed resources for your app, including the connection to the GitHub repository for your app. |
|   | Manage and monitor your app | When you finish creating an App Hosting backend, your app is available on its free subdomain, and you can view details about the rollout in the Firebase console. You can use the [Google Cloud console](https://console.cloud.google.com/logs/query?project=_) to view and search through your logs. |
|   | Develop your app | App Hosting automatically starts a new rollout every time a commit is pushed to your live branch. |

## Next steps

- [Get started](https://firebase.google.com/docs/app-hosting/get-started) deploying apps.
- Try an App Hosting codelab that integrates a hosted app with Firebase Authentication and Google AI features: [Next.js](https://firebase.google.com/codelabs/firebase-nextjs) \| [Angular](https://firebase.google.com/codelabs/firebase-web).}
- Learn more about the various [community-supported frameworks](https://firebaseopensource.com/platform/app_hosting) supported by App Hosting.