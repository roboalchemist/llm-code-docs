# Source: https://firebase.google.com/docs/app-hosting.md.txt

# Firebase App Hosting

plat_web  

Firebase App Hostingstreamlines the development and deployment of dynamic web apps, offering GitHub integration and integration with other Firebase products likeAuthentication,Cloud Firestore, andFirebase AI Logic.App Hostinghas built-in, preconfigured support for Next.js and Angular as well as broader support for various popular web frameworks.

[Get started](https://firebase.google.com/docs/app-hosting/get-started)

<br />

## Key capabilities

|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GitHub integration                | A git commit is all that's needed to roll out a new version of your app.App Hostingcan automatically deploy every time you push to a specific branch.                                                                                                   |
| Backed byGoogle Cloud             | App HostingusesGoogle CloudTerms of Service, and deploys your app toGoogle Cloudproducts you trust. Apps are built withCloud Build, served onCloud Run, and cached in Cloud CDN. Integrated services like Cloud Secret Manager keep your API keys safe. |
| Ship AI-powered features at scale | Start with AI samples that use Gemini. Protect your API endpoint's API key with Cloud Secret Manager and leverage App Hosting's streaming support to maintain fast initial load times as you add generative AI features into your app.                  |
| Firebaseconsole integration       | Monitor your builds and rollouts in theFirebaseconsole so you always know what's going on. Access logs and metrics, add a custom domain, and manually trigger rollouts from theFirebaseconsole.                                                         |

## How does it work?

1. Using theFirebaseconsole orFirebaseCLI, authorize and install the Firebase GitHub app on your repository.
2. Still in theFirebaseconsole orFirebaseCLI, create aFirebase App Hostingbackend, with a repository and live branch for continuous deployment.App Hostingcreates a default rollout policy for your backend to roll out to 100% of traffic immediately when a change is pushed to the target branch.
3. When a commit is pushed to your live branch, Google Cloud Developer Connect sends an event toFirebase App Hosting.
4. Responding to this event,Firebase App Hostingcreates a new build for the backend connected to the repository.
   1. First,Firebase App Hostingcreates a newCloud Buildbuild for your commit. In this job,[Google Cloud buildpacks](https://cloud.google.com/docs/buildpacks/overview)determine which framework is being used in your application to create a container and configuration (including environment variables, secrets, minimum or maximum instances, concurrency memory, CPU, and VPC configuration) that suits your application. See[theApp Hostingbuild process](https://firebase.google.com/docs/app-hosting/build)For more information.
   2. When theCloud Buildjob is complete, your container is stored in anArtifact Registryrepository dedicated toFirebase App Hosting.Firebase App Hostingthen adds a newCloud RunRevision to aCloud Runservice using your image and configuration.
5. Once yourCloud RunRevision is complete and verified healthy,Firebase App Hostingmodifies its traffic configuration to point all new requests to your newCloud RunRevision. At this point, the rollout is complete.
6. When a request is sent to a website hosted onFirebase App Hosting, the request is served by Google Cloud Load Balancer with Cloud CDN enabled. Uncached requests are sent to yourCloud Runservice.

## Implementation path

|---|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | Set up Firebase             | If you don't already have one, create a Firebase project and make sure it has the Blaze pricing plan enabled.                                                                                                                                                                                  |
|   | Set upApp Hosting           | With theFirebaseconsole or theFirebaseCLI, create anApp Hostingbackend. This is the collection of managed resources for your app, including the connection to the GitHub repository for your app.                                                                                              |
|   | Manage and monitor your app | When you finish creating anApp Hostingbackend, your app is available on its free subdomain, and you can view details about the rollout in theFirebaseconsole. You can use the[Google Cloudconsole](https://console.cloud.google.com/logs/query?project=_)to view and search through your logs. |
|   | Develop your app            | App Hostingautomatically starts a new rollout every time a commit is pushed to your live branch.                                                                                                                                                                                               |

## Next steps

- [Get started](https://firebase.google.com/docs/app-hosting/get-started)deploying apps.
- Try anApp Hostingcodelab that integrates a hosted app with Firebase Authentication and Google AI features:[Next.js](https://firebase.google.com/codelabs/firebase-nextjs)\|[Angular](https://firebase.google.com/codelabs/firebase-web).}
- Learn more about the various[community-supported frameworks](https://firebaseopensource.com/platform/app_hosting)supported byApp Hosting.