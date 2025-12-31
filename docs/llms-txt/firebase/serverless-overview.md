# Source: https://firebase.google.com/docs/hosting/serverless-overview.md.txt

<br />

<br />

Firebase Hostingintegrates with serverless computing options, includingCloud Functions for FirebaseandCloud Run. UsingFirebase Hostingwith these options, you can host microservices by directing HTTPS requests to trigger your functions and containerized apps to run in a managed, secure environment.

[**Cloud Functions for Firebase**](https://firebase.google.com/docs/hosting/functions): You write and deploy a function, which is backend code that responds to a specific trigger. Then, usingFirebase Hosting, you can direct HTTPS requests to trigger your function to run.

[**Cloud Run**](https://firebase.google.com/docs/hosting/cloud-run): You write and deploy an application packaged in a container image. Then, usingFirebase Hosting, you can direct HTTPS requests to trigger your containerized app to run.
| **Note:** If you're using Angular or Next.js to develop a full-stack Web app with server-side rendering or AI features, try out the preview of[App Hosting](https://firebase.google.com/docs/app-hosting). App Hosting is a unified product for managing static and dynamic content together.

## Use cases

How can you use serverless computing options withFirebase Hosting?

- **Serve dynamic content** --- In addition to serving static content on yourHostingsite, you can serve dynamically generated responses from a function or containerized app that is performing server-side logic.

  For example, you can point a URL pattern (like`/blog/<blog-post-id>`) to a function that uses the URL's blog post ID parameter to retrieve content dynamically from your database.
- **Build REST APIs**--- You can create a microservice API using functions.

  For instance, functions can handle the sign-in functionality for your website. While your website is hosted at`/`, any request to`/api`is redirected to your microservice API. For an example, check out[this open-source sample](https://github.com/firebase/functions-samples/tree/Node-8/authenticated-json-api).
- **Cache dynamic content** --- You can[configure caching](https://firebase.google.com/docs/hosting/manage-cache)of your dynamic content on a global CDN.

  For example, if a function generates new content only periodically, you can speed up your app by caching the generated content for at least a short period of time. You can also potentially reduce execution costs because the content is served from the CDN rather than via a triggered function or containerized app.
- **Prerender your single-page apps** --- You can improve SEO and optimize sharing across various social networks by creating dynamic`meta`tags. To learn more, watch this[video](https://www.youtube.com/watch?v=82tZAPMHfT4)or check out[this open-source sample](https://github.com/firebase/functions-samples/tree/Node-8/isomorphic-react-app).

## Choosing a serverless option

While both[**Cloud Functions for Firebase**](https://firebase.google.com/docs/hosting/functions)and[**Cloud Run**](https://firebase.google.com/docs/hosting/cloud-run)integrate withFirebase Hostingand offer a fully managed, autoscaling, and secure serverless environment, the two options can be leveraged for different use cases and desired level of customized configuration.

When using either serverless option, it is best to co-locate it with the servers forFirebase Hostingby deploying in one of the following regions:

- `us-west1`
- `us-central1`
- `us-east1`
- `europe-west1`
- `asia-east1`

The following table describes some basic considerations for usingCloud Functions for FirebaseversusCloud Run. For a full listing of quotas, limits, and metrics, refer to each product's detailed documentation ([Cloud Functions for Firebase](https://firebase.google.com/docs/functions/quotas)or[Cloud Run](https://cloud.google.com/run/quotas)).

|          **Consideration**          |                                                                                                                       **Cloud Functions for Firebase**                                                                                                                       |                                                                                                                         **Cloud Run**                                                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Setup**                           | TheFirebaseCLI bundles multiple tasks into single commands, from initializing to building and deploying.                                                                                                                                                                     | Containers offer more customizable options, so setup, build, and deployment tasks involve discrete steps.                                                                                                                                                      |
| **Runtime environment**             | Requires Node.js, but you can specify[which version](https://firebase.google.com/docs/functions/manage-functions#set_runtime_options)of Node.js to use.                                                                                                                      | When[building your container](https://firebase.google.com/docs/hosting/cloud-run#containerize), you specify the runtime environment.                                                                                                                           |
| **Language and frameworks support** | JavaScript and TypeScript Web frameworks, like Express.js, are supported.                                                                                                                                                                                                    | Any language that Dockerfiles support, including[Go, Node.js, Python, Java, and others](https://cloud.google.com/run/docs/quickstarts/build-and-deploy#writing) Web frameworks for each language are supported.                                                |
| **Timeout forHostingrequest**       | 60 seconds (see Note below)                                                                                                                                                                                                                                                  | 60 seconds (see Note below)                                                                                                                                                                                                                                    |
| **Concurrency**                     | 1 request per function instance (no concurrency per instance)                                                                                                                                                                                                                | Up to 1,000 concurrent requests per container instance                                                                                                                                                                                                         |
| **Billing**                         | [Cloud Functionsusage](https://firebase.google.com/pricing) Free usage quota, but a[Cloud Billingaccount](https://cloud.google.com/billing/docs/how-to/manage-billing-account)is required. See the[Firebase FAQ](https://firebase.google.com/support/faq#functions-pricing). | [Cloud Runusage](https://cloud.google.com/run/pricing)+[Container Registrystorage](https://cloud.google.com/container-registry/) Free usage quota, but a[Cloud Billingaccount](https://cloud.google.com/billing/docs/how-to/manage-billing-account)is required |
| **Billing**                         | | If your Firebase project is on the Spark pricing plan, and you associate your Firebase project with aCloud Billingaccount, then your Firebase project is automatically upgraded to the Blaze pricing plan. Review the[Firebase pricing page](https://firebase.google.com/pricing)for a comparison of the Spark and Blaze plans.                                                                                                                                                                                                            ||

| **Note:** Even thoughCloud FunctionsandCloud Runhave longer request timeouts,Firebase Hostingis subject to a 60-second request timeout. If your app requires more than 60 seconds to run, you'll receive an HTTPS status code`504`(request timeout).