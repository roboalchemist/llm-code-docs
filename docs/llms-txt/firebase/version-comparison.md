# Source: https://firebase.google.com/docs/functions/version-comparison.md.txt

<br />

There are two versions ofCloud Functions for Firebase:

- **Cloud Functions(2nd gen)** , which deploys your functions as services onCloud Run, allowing you to trigger them usingEventarcandPub/Sub.
- **Cloud Functions(1st gen)**, the original version of functions with limited event triggers and configurability.

We recommend that you chooseCloud Functions(2nd gen) for new functions wherever possible. However, we plan to continue supportingCloud Functions(1st gen).

This page describes features introduced inCloud Functionsand provides a comparison between the two product versions.

## Cloud Functions(2nd gen)

Cloud Functionsis Firebase's next-generation Functions-as-a-Service offering. Built onCloud RunandEventarc,Cloud Functions(2nd gen) brings enhanced infrastructure and broader event coverage toCloud Functions, including:

- **Built onCloud Run** : Functions are built withCloud Buildand deployed asCloud Runservices using the default[Cloud Runexecution environment](https://cloud.google.com/run/docs/about-execution-environments). This gives you the ability to customize your function as you would aCloud Runservice. Refer toCloud Rundocumentation to explore options for configuring your service, such as[memory limits](https://cloud.google.com/run/docs/configuring/services/memory-limits),[environment variables](https://cloud.google.com/run/docs/configuring/services/environment-variables), and so forth.
- **Longer request processing times** : Run longer-request workloads such as processing large streams of data fromCloud StorageorBigQuery.
- **Larger instance sizes**: Run larger in-memory, compute-intensive, and parallel workloads.
- **Improved concurrency**: Handle multiple concurrent requests with a single function instance to minimize cold starts and improve latency.
- **Traffic management**: Split traffic between different function revisions or roll a function back to a prior version.
- **Eventarcintegration** : Native support forEventarctriggers, bringing all 90+ event sources supported byEventarctoCloud Functions.
- **Broader CloudEvents support** : Support for industry-standard[CloudEvents](https://cloudevents.io/)in all language runtimes, providing a consistent developer experience.

See the[comparison table](https://firebase.google.com/docs/functions/version-comparison#comparison-table)for details.

BecauseCloud Functionsdeploys functions as services onCloud Run,Cloud Functionsshares resource quotas and limits withCloud Run. See[Quotas](https://firebase.google.com/docs/functions/quotas).

## Comparison table

|      Feature      |                                       Cloud Functions(1st gen)                                       |                                                        Cloud Functions                                                        |
|-------------------|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Image registry    | Container RegistryorArtifact Registry                                                                | Artifact Registryonly                                                                                                         |
| Request timeout   | Up to 9 minutes                                                                                      | - Up to 60 minutes for HTTP-triggered functions - Up to 9 minutes for event-triggered functions                               |
| Service account\* | Google App Engine service account (<var translate="no">PROJECT_ID</var>@appspot.gserviceaccount.com) | Google Cloud default compute service account (<var translate="no">PROJECT_NUMBER</var>-compute@developer.gserviceaccount.com) |
| Instance size     | Up to 8GB RAM with 2 vCPU                                                                            | Up to 16GiB RAM with 4 vCPU                                                                                                   |
| Concurrency       | 1 concurrent request per function instance                                                           | Up to 1000 concurrent requests per function instance                                                                          |

\* This is the default service account used to access Firebase or Cloud APIs from a running function. It is used by the Firebase Admin SDK when you[initialize without arguments](https://firebase.google.com/docs/admin/setup#initialize-sdk).

## Pricing

For pricing information, see[Firebase pricing plans](https://firebase.google.com/pricing#cloud-functions).

You can view your costs associated withCloud Functionsas follows:

1. Go to the[Cloud BillingReports page](https://console.cloud.google.com/billing/reports)in the Google Cloud console.
2. If prompted, select the billing account associated with your Google Cloud project.
3. In the**Filters** panel, under**Labels** ,[add a label filter](https://cloud.google.com//billing/docs/how-to/reports#filters)with the key`goog-managed-by`and the value`cloudfunctions`.

| **Note:** If you are usingCloud Functions for Firebase(1st gen) and are interested inCloud Functions, see[Upgrade 1st gen Node.js functions to 2nd gen](https://firebase.google.com/docs/functions/2nd-gen-upgrade).

## Limitations

Cloud Functions for Firebase(2nd gen) does not provide support forAnalyticsevents.

ThoughCloud Functions for Firebase(2nd gen) supports authentication blocking events, it does not support the same set of basicAuthenticationevents as 1st gen.

However, because 1st gen and 2nd gen functions can coexist side-by-side in the same source file, you can still develop and deployAnalyticsand basicAuthenticationtriggers in 1st gen together with 2nd gen functions.