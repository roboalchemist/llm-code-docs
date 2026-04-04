# Source: https://firebase.google.com/docs/app-hosting/costs.md.txt

<br />

App Hostingrequires a project with the Firebase Blaze pricing plan enabled. This plan has the following no-cost limits for Google Cloud products invoked byApp Hosting:

|                                 Product                                 |        Feature         |                                                 No-cost                                                 |               Billed (for usage past the no-cost limits)               |
|-------------------------------------------------------------------------|------------------------|---------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| [App Hosting](https://firebase.google.com/pricing)                      | Outgoing bandwidth     | 10 GiB / month                                                                                          | $0.15 / cached GiB $0.20 / uncached GiB                                |
| [Artifact Registry](https://cloud.google.com/artifact-registry/pricing) | Storage                | 0.5 GB / month                                                                                          | $0.10 / GB / month for over 0.5 GB                                     |
| [Artifact Registry](https://cloud.google.com/artifact-registry/pricing) | Egress                 | No Cost                                                                                                 | See Artifact Registry pricing for a full list of egress prices         |
| [Cloud Run](https://cloud.google.com/run/pricing)                       | CPU                    | 180k vCPU-seconds                                                                                       | $0.00002400 / vCPU-second                                              |
| [Cloud Run](https://cloud.google.com/run/pricing)                       | Memory                 | 360k GiB-seconds                                                                                        | $0.00000250 / GiB-second                                               |
| [Cloud Run](https://cloud.google.com/run/pricing)                       | Requests               | 2M requests                                                                                             | $0.40 / million requests                                               |
| [Cloud Build](https://cloud.google.com/build/pricing)                   | Build-minutes          | 2500 build-minutes                                                                                      | $0.006 / build-minute                                                  |
| [Cloud Logging](https://cloud.google.com/logging#pricing)               | Logging Storage        | 50 GiB / project / month                                                                                | $0.50/GiB                                                              |
| [Cloud Logging](https://cloud.google.com/logging#pricing)               | Logging Retention      | No cost for 30 days                                                                                     | $0.01 / GiB / month for logs retained more than 30 days                |
| [Secret Manager](https://cloud.google.com/secret-manager/pricing)       | Active Secret Versions | 6 versions / month                                                                                      | $0.06 per version per location                                         |
| [Secret Manager](https://cloud.google.com/secret-manager/pricing)       | Access Operations      | 10,000 operations / month                                                                               | $0.03 per 10,000 operations                                            |
| [Secret Manager](https://cloud.google.com/secret-manager/pricing)       | Rotation Notifications | 3 rotations / month                                                                                     | $0.05 per rotation                                                     |
| [Cloud Storage](https://cloud.google.com/storage/pricing)^1^            | Standard storage^2^    | 5 GB-months                                                                                             | $0.020 per GB per month                                                |
| [Cloud Storage](https://cloud.google.com/storage/pricing)^1^            | Class A Operations^2^  | 5,000                                                                                                   | $0.0050 per 1,000 operations                                           |
| [Cloud Storage](https://cloud.google.com/storage/pricing)^1^            | Class B Operations^2^  | 50,000                                                                                                  | $0.0004 per 1,000 operations                                           |
| [Cloud Storage](https://cloud.google.com/storage/pricing)^1^            | Data transfer^2^       | 100 GB from North America to each Google Cloud Data transfer destination (Australia and China excluded) | $0.02 / GB for North America $0.02 / GB for Europe $0.08 / GB for Asia |

^1^Cloud Storageis only used when deploying from local source with theFirebaseCLI.

^2^Cloud StorageAlways Free quotas apply toApp Hostingbackends in US-CENTRAL1 only.

No-cost usage is aggregated across projects by billing account and resets every month; you are billed only for usage past the limits.
| When your project is on the Blaze pricing plan,[**set up budget alerts**](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills#set-up-budget-alert-emails)using the console.
|
| Be aware that**budget alerts do*not*cap your usage or charges** --- they are*alerts* about your costs so that you can take action, if needed. For example, you might consider[using budget notifications to programmatically disableCloud Billingon a project](https://cloud.google.com/billing/docs/how-to/disable-billing-with-notifications).

## Calculate costs

Starting August 1, 2025, you begin incurring costs for yourFirebase App Hostingproject once you exceed the pay-as-you-go Blaze pricing plan allowances. You will be charged for the followingFirebase App Hostingline items:

- **Uncached Outgoing Bandwidth** refers to the data transferred directly from the origin servers of theFirebase App Hostingservice to fulfill user requests. Origin servers are located between anApp Hostingbackend'sCloud Runservice and Cloud CDN. This occurs when the requested content is not already stored in the Cloud CDN cache (that is, it's uncached). Consequently, the origin server must fetch the data and send it to the user.

  This process incurs costs for two primary reasons:
  1. **Populating Cloud CDN caches:**When a user requests uncached content, it triggers a process to fetch that data from the origin server and store a copy in the Cloud CDN cache for future requests. This initial transfer of data from the origin to the CDN contributes to the overall cost.
  2. **Transferring data to the end user:**Once the content is available (either directly from the origin or from the CDN after the initial cache population), it must be transmitted to the end user's device at the requested destination. This data transfer also contributes to the cost.
- **Cached Outgoing Bandwidth**refers to the data transferred in gibibytes from Cloud CDN's caches to the end user's device at the requested destination.

See[Cache app content](https://firebase.google.com/docs/app-hosting/optimize-cache)for guidance on how to optimize performance with Cloud CDN.

You will also be charged for the usage of the underlyingGoogle Cloudproducts that your backend uses:

- Cloud Run
- Cloud Build
- Artifact Registry
- Secret Manager
- Cloud Logging

The exact price points for these line items can be viewed on our[pricing page](https://firebase.google.com/pricing).
| **Note:** The[log-based metrics](https://cloud.google.com/stackdriver/pricing#log-based-metrics)feature of[Cloud Logging](https://cloud.google.com/logging)is required for route-based monitoring metrics. Most projects won't see an increase in cost, but it's important to note that opting into our route based monitoring may result in increasedCloud Loggingusage. For more information onCloud Loggingpricing and to estimate your costs, see[Cloud Loggingpricing](https://cloud.google.com/logging).

## Billing examples

The cost of running a dynamic web app onApp Hostingcan vary widely depending on factors like traffic, runtime settings, and response size. Costs in our example are based on certain assumptions about these factors.
| **Note:** The examples in this section are provided as a general guide, but your actual costs may differ.

### Traffic and response size

Once your app has reached its monthly free quota, each visit to your site will incur costs. These costs aren't fixed; they depend on factors like the number of background requests triggered by each visit, the compute power needed to create the response, and the response size. Some requests are simply more expensive than others. For instance, it'll likely cost more to serve a page rich with images or complex data than a simple HTML file. Similarly, generating a page dynamically on the server is typically pricier than serving a cached version from a CDN.

To effectively estimate your app's costs, you'll want to consider a few key metrics:

- Requests per visit: How many individual requests does a typical user visit trigger? (Remember, one "page load" usually involves many underlying requests for assets like images, CSS, and JavaScript.)
- Average response size: What's the typical size of the data sent back for each request?
- Average response latency: How long does it take for your app to respond to a request, on average?

You can estimate these values by inspecting your app's request logs within the Google Cloud console. Our example cost calculations assume the following:

|      Traffic characteristics       |      |
|------------------------------------|------|
| \~Billed Requests per single visit | 10   |
| Average response size (KiB)        | 400  |
| Average response latency (ms)      | 1000 |
| Cache-hit rate                     | 50%  |

### Runtime settings

|  Cloud Runsettings^1^  |     |
|------------------------|-----|
| CPU limit (vCPU)       | 1   |
| Memory limit (MiB)     | 512 |
| Concurrency (requests) | 80  |
| minInstances           | 0   |
| maxInstances           | 100 |

^1^These are the default values provided byApp Hosting. You can check your Cloud Run configuration for each rollout by viewing theCloud Runrevision details. From the**Rollouts** tab in the Firebase console, hover over a rollout and select the three dot menu, then select "ViewCloud Runrevision."

### Other assumptions

|           Project usage           |               |
|-----------------------------------|---------------|
| Deployment method                 | GitHub        |
| Builds per month                  | 20            |
| Minutes per build                 | 8             |
| Log Retention                     | \< 30 days    |
| Secret versions                   | \< 6 versions |
| Artifact registry image size (MB) | 380           |

### Sample bill

With these assumptions, we can extrapolate the following costs for this example scenario. At a level of 10k visits there are virtually no costs, with costs of any significance beginning to accrue at the 1M visit level, where a visit is a request to your app initiated by a user.

|                  **SKU**                  | **Price** |    **Unit**    | **No-cost Tier** | **10K visits usage** | **10K visits cost** | **1M visits usage** | **1M visits cost** |
|-------------------------------------------|-----------|----------------|------------------|----------------------|---------------------|---------------------|--------------------|
| Cloud Run - CPU                           | $0.00     | vCPU second    | 180,000.00       | 1250                 | $0.00               | 125000              | $0.00              |
| Cloud Run - memory                        | $0.00     | GiB second     | 360,000.00       | 625                  | $0.00               | 62500               | $0.00              |
| Cloud Run - requests                      | $0.40     | M SSR requests | 2.00             | 0.05                 | $0.00               | 5                   | $1.20              |
| Cloud Build - build minutes               | $0.01     | build-minute   | 2,500.00         | 160                  | $0.00               | 160                 | $0.00              |
| Artifact Registry - storage               | $0.10     | GiB (stored)   | 0.50             | 0.6                  | $0.01               | 0.6                 | $0.01              |
| App Hosting - Uncached outgoing bandwidth | $0.20     | GiB            | 10               | 2                    | $0.00               | 200                 | $39.00             |
| App Hosting - Cached outgoing bandwidth   | $0.15     | GiB            | 10               | 2                    | $0.00               | 200                 | $29.25             |
| Secrets Manager - Active Secret Versions  | $0.06     | versions       | 6.00             | 6.00                 | $0.00               | 6.00                | $0.00              |
| Secrets Manager - Access Operations       | $0.03     | 10K operations | 1.0              | 0.10                 | $0.00               | 5.00                | $0.12              |
| Secrets Manager - Rotation Notifications  | $0.05     | rotations      | 3.00             | 0.00                 | $0.00               | 0.00                | $0.00              |
| Cloud Logging - Logging Storage           | $0.50     | GiB            | 50.00            | 0.50                 | $0.00               | 50.00               | $0.00              |
| Cloud Logging - Logging Retention         | $0.01     | GiB / month    | 30 days          |                      | $0.00               |                     | $0.00              |
| **Total**                                 |           |                |                  |                      | **$0.01**           |                     | **$69.58**         |

### Calculations

|               SKU                |      Unit      |                                                             How to calculate usage                                                              |
|----------------------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Cloud Run - CPU                  | vCPU second    | vCPU seconds = vCPU per instance \* average response latency per request \* # of visits \* billed requests per visit / # of concurrent requests |
| Cloud Run - memory               | GiB second     | GiB seconds = GiB per instance \* average response latency per request \* # of visits \* billed requests per visit / # of concurrent requests   |
| Cloud Run - requests             | M SSR requests | M SSR requests = (# of visits \* billed requests per visit / 1M) \* (1 - cache-hit rate)                                                        |
| Cloud Build - build minutes      | build-minute   | build-minutes = # of builds \* minutes per build                                                                                                |
| Artifact Registry - storage^1^   | GiB (stored)   | GiB (stored) = 2 \* image size                                                                                                                  |
| App Hosting - Uncached Bandwidth | GiB            | Uncached GiB= (1 - cache-hit rate) \* (# of visits \* billed requests per visit \* outgoing bandwidth per request)                              |
| App Hosting - Cached Bandwidth   | GiB            | Cached GiB = cache-hit rate \* (# of visits \* billed requests per visit \* outgoing bandwidth per request)                                     |

^1^Your app will typically have only one image in Artifact Registry, as App Hosting automatically cleans up unused versions. You may see two images briefly only during a new rollout.