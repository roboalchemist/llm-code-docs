# Source: https://firebase.google.com/docs/functions/locations.md.txt

<br />

Cloud Functions is
[*regional*](https://cloud.google.com/docs/geography-and-regions),
which means the infrastructure that runs your function is located in specific
regions and is managed by Google to be redundantly available across all the
zones within those regions.

When selecting what regions to run your functions in, your primary
considerations should be latency and availability. You can
generally select regions close to your users, but you
should also consider the location of the
[other products and services](https://cloud.google.com/about/locations/#locations)
that your app uses. Using services across multiple regions can affect
your app's latency, as well as [pricing](https://firebase.google.com/pricing/).

By default, functions run in the `us-central1` region. Note that this may be
different from the region of an event source, such as a Cloud Storage bucket.
Learn how to
[specify the region where a function runs](https://firebase.google.com/docs/functions/locations#best_practices_for_specifying_a_region)
later in this page.

## Supported regions

In the lists in this section, the energy_savings_leaf icon indicates that the electricity for this region is produced with
low carbon emissions. For more information, see
[Carbon free energy for Google Cloud regions](https://cloud.google.com/sustainability/region-carbon).

### Tier 1 pricing

Cloud Functions is available in the following regions with
[Tier 1 pricing](https://cloud.google.com/functions/pricing):

| Region | Location | Supported product versions | CO~2~ emissions |
|---|---|---|---|
| `africa-south1` | Johannesburg | 2nd gen only |   |
| `asia-east1` | Taiwan | 1st gen, 2nd gen |   |
| `asia-east2` | Hong Kong | 1st gen only |   |
| `asia-northeast1` | Tokyo | 1st gen, 2nd gen |   |
| `asia-northeast2` | Osaka | 1st gen, 2nd gen |   |
| `europe-north1` | Finland | 2nd gen only | energy_savings_leaf |
| `europe-southwest1` | Madrid | 2nd gen only |   |
| `europe-west1` | Belgium | 1st gen, 2nd gen | energy_savings_leaf |
| `europe-west4` | Netherlands | 2nd gen only |   |
| `europe-west8` | Milan | 2nd gen only |   |
| `europe-west9` | Paris | 2nd gen only | energy_savings_leaf |
| `me-west1` | Tel Aviv | 2nd gen only |   |
| `europe-west2` | London | 1st gen only |   |
| `us-central1` | Iowa | 1st gen, 2nd gen | energy_savings_leaf |
| `us-east1` | South Carolina | 1st gen, 2nd gen |   |
| `us-east4` | Northern Virginia | 1st gen, 2nd gen |   |
| `us-east5` | Columbus | 2nd gen only |   |
| `us-south1` | Dallas | 2nd gen only |   |
| `us-west1` | Oregon | 1st gen, 2nd gen | energy_savings_leaf |

### Tier 2 pricing

Cloud Functions is available in the following regions with
[Tier 2 pricing](https://firebase.google.com/functions/pricing):

| Region | Location | Supported product versions | CO~2~ emissions |
|---|---|---|---|
| `asia-east2` | Hong Kong | 2nd gen only |   |
| `asia-northeast3` | Seoul | 1st gen, 2nd gen |   |
| `asia-southeast1` | Singapore | 1st gen, 2nd gen |   |
| `asia-southeast2` | Jakarta | 1st gen, 2nd gen |   |
| `asia-south1` | Mumbai | 2nd gen only |   |
| `asia-south2` | Delhi, India | 2nd gen only |   |
| `australia-southeast1` | Sydney | 1st gen, 2nd gen |   |
| `australia-southeast2` | Melbourne | 2nd gen only |   |
| `europe-central2` | Warsaw | 1st gen, 2nd gen |   |
| `europe-west2` | London | 2nd gen only |   |
| `europe-west3` | Frankfurt | 1st gen, 2nd gen | energy_savings_leaf |
| `europe-west6` | Zurich | 1st gen, 2nd gen | energy_savings_leaf |
| `europe-west10` | Berlin | 2nd gen only |   |
| `europe-west12` | Turin | 2nd gen only |   |
| `me-central1` | Doha | 2nd gen only |   |
| `me-central2` | Dammam | 2nd gen only |   |
| `northamerica-northeast1` | Montreal | 1st gen, 2nd gen | energy_savings_leaf |
| `northamerica-northeast2` | Toronto | 2nd gen only | energy_savings_leaf |
| `southamerica-east1` | Sao Paulo | 1st gen, 2nd gen | energy_savings_leaf |
| `southamerica-west1` | Santiago, Chile | 2nd gen only |   |
| `us-west2` | Los Angeles | 1st gen, 2nd gen |   |
| `us-west3` | Salt Lake City | 1st gen, 2nd gen |   |
| `us-west4` | Las Vegas | 1st gen, 2nd gen |   |

Functions in a given region in a given project must have unique (case
insensitive) names, but functions across regions or across projects may share
the same name.

## Best practices for specifying a region

By default, functions run in the `us-central1` region. Note that this may be
different from the region of an event source, such as a Cloud Storage bucket. If
you need to specify the region where a function runs, follow the
recommendations in this section for each function trigger type.

To set the region where a function runs, set the `region` parameter in the
function definition as shown:

### Node.js

    exports.firestoreAsia = onDocumentCreated(
      {
        document: "my-collection/{docId}",
        region: "asia-northeast1",
      },
      (event) => {},
    );

### Python

    # Before
    @firestore_fn.on_document_created("my-collection/{docId}")
    def firestore_trigger(event):
        pass

    # After
    @firestore_fn.on_document_created("my-collection/{docId}",
                                      region="asia-northeast1")
    def firestore_trigger_asia(event):
        pass

You can specify multiple regions by passing multiple comma-separated region
strings in `region`. Also note that, when specifying a region for many
background trigger types, you'll need to specify the correct event filter
along with the region. In the example above, this is the Cloud Firestore `document`
that emits the event. For a Cloud Storage trigger the event filter
could be `bucket`; for a Pub/Sub trigger it would be `topic`, and so on.

See
[change a function's region](https://firebase.google.com/docs/functions/manage-functions#modify-region)
for more information on changing the region for a function that's handling
production traffic.

### HTTP and client-callable functions

For HTTP and callable functions, we recommend that you first set your function to the
destination region, or closest to where most expected customers are located, and
then alter your original function to redirect its HTTP request to the new
function (they can have the same name). If clients of your HTTP function support
redirects, you can simply change your original function to return an HTTP
redirect status (301) along with the URL of your new function. If your clients
do not handle redirects well, you can *proxy* the request from the original
function to the new function by initiating a new request from the original
function to the new function. The final step is to ensure that all clients are
calling the new function.

#### Client-side location selection for callable functions

Regarding the callable function, client callable setups should follow the same
guidelines as HTTP functions. The client can also specify a region, and
*must* do so if the function runs in any region other than `us-central1`.

To set
regions on the client, specify the desired region at initialization:

### Swift

    lazy var functions = Functions.functions(region:"europe-west1")

### Objective-C

    @property(strong, nonatomic) FIRFunctions *functions;
    // ...
    self.functions = [FIRFunctions functionsWithRegion:@"europe-west1"];

### Web


    var functions = firebase.app().functions('europe-west1');

### Android

    private FirebaseFunctions mFunctions;
    // ...
    mFunctions = FirebaseFunctions.getInstance("europe-west1");

### C++

    firebase::functions::Functions* functions;
    // ...
    functions = firebase::functions::Functions::GetInstance("europe-west1");

### Unity

    firebase.Functions.FirebaseFunctions functions;

    functions = Firebase.Functions.FirebaseFunctions.GetInstance("europe-west1");

### Background functions

Background functions adopt an at-least-once event delivery semantic, which means
that under some circumstances they may receive duplicate events. So, you should
implement functions to be
[idempotent](https://firebase.google.com/docs/functions/tips#write_idempotent_functions). If your function
is already idempotent, then you can redeploy the function in the new region with
the same event trigger and remove the old function after you verify that the
new function is correctly receiving traffic. During this transition, both
functions will receive events. See
[change a function's region](https://firebase.google.com/docs/functions/manage-functions#modify-region)
for the recommended sequence of commands to change regions for functions.

If your function is not currently idempotent, or its idempotency does not
extend beyond the region, then we recommend that you first implement
idempotency before moving the function.

Optimal region recommendations differ by event trigger type:

| Trigger Type | Region Recommendation |
|---|---|
| Cloud Firestore | Closest region to the Cloud Firestore instance location (see next section) |
| Realtime Database | Same region as the Realtime Database instance |
| Cloud Storage | Closest region to the Cloud Storage bucket location (see next section) |
| Others | If you are interacting with a Realtime Database instance, a Cloud Firestore instance, or a Cloud Storage bucket inside of the function, then the recommended region is the same as if you had a function triggered by one of those resources. Otherwise, use the default region of `us-central1`. Functions connected to Firebase Hosting can be in any region, but see [the hosting serverless overview](https://firebase.google.com/docs/hosting/serverless-overview#choosing_a_serverless_option) for recommendations. |

### Selecting regions based on Cloud Firestore and Cloud Storage locations

The available regions for functions do not always match precisely with the
regions available for your Cloud Firestore database and your Cloud Storage
buckets.

Note that if your function and your resource (database instance or Cloud Storage
bucket) are in different locations, then you could potentially experience
increased latency and
[billing costs](https://cloud.google.com/functions/pricing#networking).

Here's a mapping of the closest functions-supported regions for Cloud Firestore
and Cloud Storage, for cases where the same region is *not* supported:

| Region/Multi-region for Cloud Firestore and Cloud Storage | Nearest region for functions |
|---|---|
| `nam5` or `us-central` (multi-region) | `us-central1` |
| `eur3` or `europe-west` (multi-region) | `europe-west1` |
| `europe-west4` (Netherlands) | `europe-west1` |
| `asia-south1` (Mumbai) | `asia-east2` |
| `asia-south2` (Delhi) | `asia-east2` |
| `australia-southeast2` (Melbourne) | `australia-southeast1` |