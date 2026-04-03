# Source: https://firebase.google.com/docs/hosting.md.txt

# Firebase Hosting

plat_web  
Firebase Hostingprovides fast and secure hosting for your web app.  

Firebase Hostingis production-grade web content hosting for developers. With a single command, you can quickly deploy web apps to a global CDN (content delivery network).

ThoughFirebase Hostingis optimized for static and single-page web apps, you can also[pairFirebase HostingwithCloud FunctionsorCloud Run](https://firebase.google.com/docs/hosting/serverless-overview)to build and host dynamic content and microservices on Firebase.

[Get started](https://firebase.google.com/docs/hosting/quickstart)

## Key capabilities

|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Serve content over a secure connection                | Zero-configuration SSL is built intoFirebase Hosting, so content is always delivered securely.                                                                                                                                                                                                                 |
| Deliver content fast                                  | Each file that you upload is cached on SSDs at CDN edges around the world and served as gzip or Brotli. We auto-select the best compression method for your content. No matter where your users are, the content is delivered fast.                                                                            |
| Emulate and even share your changes before going live | View and test your changes on a locally hosted URL and interact with an emulated backend. Share your changes with teammates using temporary preview URLs.Hostingalso provides a[GitHub integration](https://firebase.google.com/docs/hosting/github-integration)for easy iterations of your previewed content. |
| Deploy new versions with one command                  | Using theFirebaseCLI, you can get your app up and running in seconds. Command line tools let you add deployment targets into your build process. And if you need to undo the deploy,Hostingprovides one-click rollbacks.                                                                                       |

## How does it work?

Whether you are deploying a simple app landing page or a complex Progressive Web App (PWA),Hostinggives you the infrastructure, features, and tooling tailored to deploying and managing websites and apps.

Using the[FirebaseCLI](https://firebase.google.com/docs/cli), you deploy files from local directories on your computer to ourHostingservers. Beyond serving static content, you can useCloud Functions for FirebaseorCloud Runto[serve dynamic content and host microservices](https://firebase.google.com/docs/hosting/serverless-overview)on your sites. All content is served over an SSL connection from the closest edge server on our global CDN.

You can also[view and test your changes before going live](https://firebase.google.com/docs/hosting/test-preview-deploy). Using theFirebase Local Emulator Suite, you can emulate your app and backend resources at a locally hosted URL. You can also share your changes at a temporary preview URL and set up a[GitHub integration](https://firebase.google.com/docs/hosting/github-integration)for easy iterations during development.

Firebase Hostinghas lightweight[hosting configuration options](https://firebase.google.com/docs/hosting/full-config)for you to build sophisticated PWAs. You can easily rewrite URLs for client-side routing, set up custom headers, and even serve localized content.

For serving your content, Firebase offers several domain and subdomain options:

- By default, every Firebase project has subdomains at no cost on the`web.app`and`firebaseapp.com`domains. These two sites serve the same deployed content and configuration.

- You can[create multiple sites](https://firebase.google.com/docs/hosting/multisites)if you have related sites and apps that serve different content but still share the same Firebase project resources (for example if you have a blog, admin panel, and public app).

- You can[connect your own domain name](https://firebase.google.com/docs/hosting/custom-domain)to a Firebase-hosted site.

Firebase automatically provisions SSL certificates for all your domains so that all your content is served securely.

## Implementation path

|---|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | Install theFirebaseCLI                                           | The[FirebaseCLI](https://firebase.google.com/docs/cli)makes it easy to set up a newHostingproject, run a local development server, and deploy content.                                                                                                                                                                                                                                                          |
|   | Set up a project directory                                       | Add your static assets to a local project directory, then runfirebase initto connect the directory to a Firebase project. In your local project directory, you can also set upCloud FunctionsorCloud Runfor your[dynamic content and microservices](https://firebase.google.com/docs/hosting/serverless-overview).                                                                                              |
|   | View, test, and share your changes before going live*(optional)* | Runfirebase emulators:startto emulateHostingand your backend project resources at a locally hosted URL. To view and share your changes at a temporary preview URL, runfirebase hosting:channel:deployto create and deploy to a preview channel. Set up the[GitHub integration](https://firebase.google.com/docs/hosting/github-integration)for easy iterations of your previewed content.                       |
|   | Deploy your site                                                 | When things are looking good, runfirebase deployto upload the latest snapshot to our servers. If you need to undo the deploy, you can roll back with just one click in theFirebaseconsole.                                                                                                                                                                                                                      |
|   | Link to a Firebase Web App*(optional)*                           | By linking your site to a[Firebase Web App](https://firebase.google.com/docs/web/setup), you can use[Google Analytics](https://firebase.google.com/docs/analytics/get-started?platform=web)to collect usage and behavior data for your app and use[Firebase Performance Monitoring](https://firebase.google.com/docs/perf-mon/get-started-web)to gain insight into the performance characteristics of your app. |

## Next steps

- [Get started](https://firebase.google.com/docs/hosting/quickstart)withFirebase Hosting.

- Continue to improve your site. Test locally, share changes at a temporary preview URL, then deploy to your live site. Follow this[step-by-step guide](https://firebase.google.com/docs/hosting/test-preview-deploy).

- [Build and host microservices](https://firebase.google.com/docs/hosting/serverless-overview)on Firebase.