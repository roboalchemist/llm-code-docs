# Source: https://firebase.google.com/docs/hosting/use-cases.md.txt

## What is Firebase Hosting?

Firebase Hosting is a fully-managed hosting service for static and dynamic
content as well as microservices. The service is backed by SSD storage and a
global CDN (content delivery network). Zero-configuration SSL is built into
Firebase Hosting, so content is always delivered securely.

## What can you host?

**Host your single-page web apps, marketing websites, and static and dynamic
assets**

Benefit from Firebase Hosting's unique optimization for serving single-page
web apps and static websites. Delivery of static assets (HTML, CSS, JavaScript,
fonts, etc.) is powered by our SSD backend storage and a global CDN with edge
locations across all major locations in the world. You can even
[cache your dynamic content](https://firebase.google.com/docs/hosting/manage-cache) on the global CDN. All
sites hosted by Firebase also get an SSL certificate at no cost, so your
content is always delivered securely.

**Build then host your microservices, API, and forms**

Pair Firebase Hosting with [Cloud Functions](https://firebase.google.com/docs/functions) to build microservices
using the Express.js framework. This pairing allows you to host your
microservices and APIs on Firebase. In addition, you can use a deep integration
with [Cloud Firestore](https://firebase.google.com/docs/firestore) to build very powerful forms and web apps which can
update data in real time.

> [!NOTE]
> You can also use our new serverless offering, [Cloud Run](https://firebase.google.com/docs/hosting/cloud-run), with Firebase Hosting to generate and host your dynamic content or build then host your microservices, APIs, and forms.

## Add a custom domain (or a subdomain)

With Firebase Hosting, you're automatically given a Firebase sub-domain, but
you can choose to serve your content on a
[custom domain](https://firebase.google.com/docs/hosting/custom-domain) (like
`example.com` or `myrealtimeapp.example.com`). Firebase Hosting
provisions an SSL certificate for each of your domains and serves your content
over a global CDN.

## Set up production workflows

Before deploying to your live site, you'll want to view and test your changes.
Firebase Hosting enables you to view and test changes locally and interact
with emulated backend project resources. If you need your teammates to view and
test your changes, Hosting can create sharable, temporary preview URLs for
your site. We even support a
[GitHub integration](https://firebase.google.com/docs/hosting/github-integration) to deploy from a pull
request.

[Learn more](https://firebase.google.com/docs/hosting/test-preview-deploy) about testing locally,
previewing changes, and deploying.

## Keep all your sites in one place

Firebase Hosting supports
[multiple sites in a single Firebase project](https://firebase.google.com/docs/hosting/multisites). Each
site hosts its own collection of content, has its own hosting configuration, and
can have one or more associated domains. Since the sites are all in the same
Firebase project, all the sites can access the other Firebase resources of the
project.

You can use multiple sites in a Firebase project to keep related sites together
(for example your single-page app, blog, and marketing website).

## View, search, and filter your site's web request logs

You can link your Firebase project to Cloud Logging to view, search, and
filter your web request logs for each of your Hosting sites. These logs are
from the CDN that's automatically provided by Firebase, so every request to your
site and the associated request data are logged.

Here are some things you do with Cloud Logging logs:

- **Better understand your site** --- Learn from where and when you have visits to
  your site, your site's response statuses, the latency of end user requests,
  and more.

- **Filter your logs with queries** --- Leverage automatically collected data to
  filter and plot data associated with each request or your site.

- **Use logs-based metrics** --- Create Cloud Monitoring charts and alerting
  policies from predefined system metrics or user-defined metrics.

- **Export logs to other Google Cloud tools** --- Use logs data in other tools
  (like BigQuery and Looker Studio) for more powerful analysis
  and correlation.

Learn more in the
[Cloud Logging and Hosting integration page](https://firebase.google.com/docs/hosting/web-request-logs-and-metrics).

## Automate continuous deployment with Cloud Build

[Video](https://www.youtube.com/watch?v=iyGHW4UQ_Ts)

Firebase Hosting partnered with
[Cloud Build](https://cloud.google.com/cloud-build/) offers a
DevOps-ready solution for automating a continuous deployment workflow for your
static and dynamic content as well as for your microservices.

After you configure these tools, you can deploy your web app to
Firebase Hosting by simply checking in your code to your git repository.

If you're interested in continuous deployment for full-stack Web apps
developed in Next.js or Angular Universal, check out the
[Firebase App Hosting](https://firebase.google.com/docs/app-hosting) preview. App Hosting
provides automatic rollouts from a GitHub repository using Cloud Build
and Cloud Run, without requiring any manual configuration.

## Customize everything!

- [Error pages](https://firebase.google.com/docs/hosting/full-config#404) --- Return a neatly fully
  customized 404 page from your web app.

- [Rewrites](https://firebase.google.com/docs/hosting/full-config#rewrites) --- Customize which endpoints
  serve what traffic, and even display the same content from multiple URLs.

- [Localized content](https://firebase.google.com/docs/hosting/i18n-rewrites) --- Serve content that's
  customized for a user's language preference and/or country.

- [Headers](https://firebase.google.com/docs/hosting/full-config#headers) --- Want to access cookies?
  Use custom headers!

- [Caching and CDN behavior](https://firebase.google.com/docs/hosting/full-config#headers) --- Control
  how your web app is cached across the CDN through custom headers.

## Restrict access and counter a DDoS attack for your web apps

Using the power of Express.js middleware, you can build custom logic into
serving your microservices, APIs, and other HTTPS endpoints. For example, with
just a few lines of code, you can integrate popular Node.js middleware offerings
to build additional security layers, like access management by IP or protection
from denial-of-service (DDoS) attacks.

## Deploy to Firebase from various web-based IDEs

Firebase Hosting is integrated with various web-based IDEs so that you can
deploy to Firebase Hosting directly from within
[StackBlitz](https://stackblitz.com/) and [Glitch](https://glitch.com/),
two web-based IDEs.
![Deploy using Stackblitz](https://firebase.google.com/static/docs/hosting/images/hosting-deploy-stackblitz.gif) Deploy to Firebase Hosting using [Stackblitz](https://stackblitz.com/) ![Deploy using Glitch](https://firebase.google.com/static/docs/hosting/images/hosting-deploy-glitch.gif) Deploy to Firebase Hosting using [Glitch](https://glitch.com/)


These IDEs automatically detect when you're creating a
Firebase app and allow you to deploy to Firebase Hosting with the click of
a button, without ever leaving the IDE!

## Build deep integrations with other Firebase services

![FriendlyChat web codelab](https://firebase.google.com/static/docs/hosting/images/friendlychat-web-codelab.png)

Firebase Hosting works out-of-the-box with Firebase services, including
[Cloud Functions](https://firebase.google.com/docs/functions),
[Authentication](https://firebase.google.com/docs/auth),
[Realtime Database](https://firebase.google.com/docs/database),
[Cloud Firestore](https://firebase.google.com/docs/firestore), and
[Cloud Messaging](https://firebase.google.com/docs/cloud-messaging).
You can build powerful microservices and web apps using these complementary
Firebase services.

Try out our
[FriendlyChat web codelab](https://codelabs.developers.google.com/codelabs/firebase-web/#0)
to learn how Hosting pairs with these Firebase services.

## Create a custom deployment workflow using REST API and our Node.js modules

Firebase Hosting supports a [REST API](https://firebase.google.com/docs/reference/hosting/rest) for
advanced developers to build custom workflows, like deploying through a
JavaScript app.

We also have a [Node.js module](https://github.com/firebase/firebase-tools)
which you can import into your Node.js apps to build advanced functionality.