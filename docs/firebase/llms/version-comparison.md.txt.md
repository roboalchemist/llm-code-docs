# Source: https://firebase.google.com/docs/functions/version-comparison.md.txt

There are two versions of Cloud Functions for Firebase:

- **Cloud Functions (2nd gen)** , which deploys your functions as services on Cloud Run, allowing you to trigger them using Eventarc and Pub/Sub.
- **Cloud Functions (1st gen)**, the original version of functions with limited event triggers and configurability.

We recommend that you choose Cloud Functions (2nd gen) for new functions
wherever possible. However, we plan to continue supporting Cloud Functions
(1st gen).

This page describes features introduced in Cloud Functions and
provides a comparison between the two product versions.

## Cloud Functions (2nd gen)

Cloud Functions is Firebase's next-generation
Functions-as-a-Service offering. Built on Cloud Run and
Eventarc, Cloud Functions (2nd gen) brings enhanced
infrastructure and broader event coverage to Cloud Functions, including:

- **Built on Cloud Run** : Functions are built with Cloud Build and deployed as Cloud Run services using the default [Cloud Run execution environment](https://cloud.google.com/run/docs/about-execution-environments). This gives you the ability to customize your function as you would a Cloud Run service. Refer to Cloud Run documentation to explore options for configuring your service, such as [memory
  limits](https://cloud.google.com/run/docs/configuring/services/memory-limits), [environment variables](https://cloud.google.com/run/docs/configuring/services/environment-variables), and so forth.
- **Longer request processing times** : Run longer-request workloads such as processing large streams of data from Cloud Storage or BigQuery.
- **Larger instance sizes**: Run larger in-memory, compute-intensive, and parallel workloads.
- **Improved concurrency**: Handle multiple concurrent requests with a single function instance to minimize cold starts and improve latency.
- **Traffic management**: Split traffic between different function revisions or roll a function back to a prior version.
- **Eventarc integration** : Native support for Eventarc triggers, bringing all 90+ event sources supported by Eventarc to Cloud Functions.
- **Broader CloudEvents support** : Support for industry-standard [CloudEvents](https://cloudevents.io/) in all language runtimes, providing a consistent developer experience.

See the [comparison table](https://firebase.google.com/docs/functions/version-comparison#comparison-table) for details.

Because Cloud Functions deploys functions as services on Cloud Run,
Cloud Functions shares resource quotas and limits with
Cloud Run. See [Quotas](https://firebase.google.com/docs/functions/quotas).

## Comparison table

| Feature | Cloud Functions (1st gen) | Cloud Functions |
|---|---|---|
| Image registry | Container Registry or Artifact Registry | Artifact Registry only |
| Request timeout | Up to 9 minutes | - Up to 60 minutes for HTTP-triggered functions - Up to 9 minutes for event-triggered functions |
| Service account\* | Google App Engine service account (<var translate="no">PROJECT_ID</var>@appspot.gserviceaccount.com) | Google Cloud default compute service account (<var translate="no">PROJECT_NUMBER</var>-compute@developer.gserviceaccount.com) |
| Instance size | Up to 8GB RAM with 2 vCPU | Up to 16GiB RAM with 4 vCPU |
| Concurrency | 1 concurrent request per function instance | Up to 1000 concurrent requests per function instance |

\* This is the default service account used to access Firebase or Cloud APIs
from a running function. It is used by the Firebase Admin SDK when you
[initialize without arguments](https://firebase.google.com/docs/admin/setup#initialize-sdk).

## Pricing

For pricing information, see [Firebase pricing plans](https://firebase.google.com/pricing#cloud-functions).

You can view your costs associated with Cloud Functions as follows:

1. Go to the [Cloud Billing Reports page](https://console.cloud.google.com/billing/reports) in the Google Cloud console.
2. If prompted, select the billing account associated with your Google Cloud project.
3. In the **Filters** panel, under **Labels** , [add a label filter](https://cloud.google.com//billing/docs/how-to/reports#filters) with the key `goog-managed-by` and the value `cloudfunctions`.

> [!NOTE]
> **Note:** If you are using Cloud Functions for Firebase (1st gen) and are interested in Cloud Functions, see [Upgrade 1st gen Node.js functions to 2nd gen](https://firebase.google.com/docs/functions/2nd-gen-upgrade).

## Limitations

Cloud Functions for Firebase (2nd gen) does not provide support for Analytics
events.

Though Cloud Functions for Firebase (2nd gen) supports authentication blocking
events, it does not support the same set of basic Authentication events as
1st gen.

However, because 1st gen and 2nd gen
functions can coexist side-by-side in the same source file, you can still
develop and deploy Analytics and basic Authentication triggers in 1st gen
together with 2nd gen functions.