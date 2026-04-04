# Source: https://firebase.google.com/docs/app-hosting/product-comparison.md.txt

<br />

Serverless products likeFirebase App Hostinglet you deploy applications fast, without managing the infrastructure yourself. Among Google solutions,App Hostingis the best choice for web developers creating modern web apps on popular frameworks because it manages the full stack, from the CDN to server-side rendering.

However,App Hostingis only one of several Google serverless products. Depending on the nature of your app or your scalability needs, you might chooseApp Hostingor one of these other products:

- **[Cloud Run](https://cloud.google.com/run/docs):**Best for running backend services in containers with maximum configurability.
- **[Cloud Functions](https://cloud.google.com/functions/docs):**Best for quickly creating single-purpose, event-driven functions.
- **[Cloud Functions for Firebase](https://firebase.google.com/docs/functions)** : Like Cloud Functions, but with a simplified model for easier integration with other Firebase features likeRealtime DatabaseorCloud Firestore.
- **Firebase App Hosting:**Ideal for hosting modern frameworks-based web apps with server-side rendering (SSR) or generative AI features.
- **[Firebase Hosting](https://firebase.google.com/docs/hosting):**Excellent for hosting static assets like websites and images.

Regarding cost, Cloud Run, Cloud Functions, andFirebase App Hostingrequire a billing account to get started, include a no-cost tier for small deployments, and are priced based on usage.Firebase Hostingoffers a no-cost tier with no billing account required for small deployments, with flexibility to expand as your app scales up.

## App HostingandFirebase Hosting

App Hostingis not a drop-in replacement forFirebase Hosting-- it fills a specific gap. If you are developing a dynamic, server-rendered web app with SSR,App Hostingis definitely for you. If you want hosting for a static website or single-page app, it may make sense to use the originalHostingto optimize for cost and performance.

SinceApp HostingandFirebase Hostinghave a degree of overlap in the features they support, a more detailed look may be helpful.

|                     Feature                      |                                       Hosting                                        |               App Hosting               |
|--------------------------------------------------|--------------------------------------------------------------------------------------|-----------------------------------------|
| Automatic deployment of server-rendered web apps | Experimental                                                                         | Yes                                     |
| Request timeout                                  | 1m                                                                                   | 5m                                      |
| Cache timeout                                    | 1hr                                                                                  | 1hr                                     |
| Stale-While-Revalidate cache control             | No                                                                                   | Yes                                     |
| Terms of Service                                 | [Firebase](https://firebase.google.com/terms)                                        | [Cloud](https://cloud.google.com/terms) |
| Static content origin replicas                   | 3                                                                                    | N/A                                     |
| Dynamic content regions                          | 3                                                                                    | 3                                       |
| Continuous deployment                            | [Limited](https://firebase.google.com/docs/hosting/github-integration)               | Built-in                                |
| Build process                                    | Local environment                                                                    | Reproducible environment                |
| Preview content                                  | [Yes](https://firebase.google.com/docs/hosting/test-preview-deploy#preview-channels) | No                                      |
| Fault tolerance                                  | Global outage                                                                        | Regional outage                         |
| Emulator                                         | Yes                                                                                  | Yes                                     |

### Development lifecycle features ofApp HostingandHosting

Firebase App Hostingis deeply integrated with GitHub and offers efficient rollouts to production for your app. When you push a change to your live branch,App Hostingbuilds the branch in a reproducible Cloud Build environment. Then, in theApp Hostingdashboard UI, you can track each version of your web app to the exact commit it was built with, so that you know which changes were live at a certain time.

Firebase Hostingalso provides a degree of[integration using GitHub actions](https://firebase.google.com/docs/hosting/github-integration)to create preview channels and deploy to live channel in response to actions in a repository.

### Apps deployed using the frameworks experiment in the Firebase CLI

For modern web apps deployed toFirebase Hostingusing the frameworks experiment in the Firebase CLI, we recommend "graduating" toApp Hosting. WithApp Hosting, you'll have a unified solution to manage everything from CDN to server-side rendering, along with improved GitHub integration.