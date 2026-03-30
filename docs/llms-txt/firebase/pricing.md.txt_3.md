# Source: https://firebase.google.com/docs/firestore/enterprise/pricing.md.txt

<br />

> [!WARNING]
> **Preview:** **Firestore in Native mode (with Pipeline operations) for Enterprise
> edition** is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific
> Terms](https://cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage
> descriptions](https://cloud.google.com/products#product-launch-stages).

The Firestore Enterprise edition introduces a [pricing
model](https://cloud.google.com/firestore/enterprise/pricing) that shifts
billing from a "per document" basis to a "per unit" (or tranche) basis, and
separating the cost of real-time updates.

> [!NOTE]
> **Note:** The Enterprise edition is applicable only to a few regions. For more information on supported regions, see [Locations](https://firebase.google.com/docs/firestore/pipelines/locations).

The following table details the cost per unit for both editions. The price shown
is for us-central1.

|---|---|---|
| **Unit** | **Standard edition** | **Enterprise edition** |
| **Reads** | **$0.03 per 100k reads** or**$0.30 per million reads** charged per document | **$0.05 per million read units**Read units are data processed (documents or indexes) when you read data from your database, calculated in 4 KiB tranches. |
| **Writes** | **$0.09 per 100k writes** or**$0.90 per million writes** charged per document | **$0.26 per million write units** Writes are measured in 1 KiB units. Index writes now cost write units. Note that indexing fields consume separate write units, so indexing a field with a 2KiB String incurs 2 write units. |
| **Deletes** | **$0.01 per 100k deletes** or **$0.10 per million deletes** | Utilizes Write units |
| **Real-time updates** | **$0.03 per 100k reads** or**$0.30 per million reads** charged per document | **$0.30 per million read units** Real-time updates have a new, separate SKU. |
| **Stored Data** | $0.00020 per GiB hour | $0.00032 per GiB hour |
| **Backup data** | $0.00004 per GiB hour | $0.00004 per GiB hour |
| **Restore operation** | $0.20 per GiB | $0.20 per GiB |
| **PITR Data** | $0.00020 per GiB hour | $0.00020 per GiB hour |
| **Clone operation** | $0.20 per GiB | $0.20 per GiB |

## Free Tier

The following table shows details for the free tier:

|---|---|---|
| **Unit** | **Standard edition (free tier per day)** | **Enterprise edition (free tier per day)** |
| Reads | 50,000 | 50,000 |
| Writes | 20,000 | 40,000 |
| Deletes | 20,000 | Included in Writes |
| Real-time updates | Included in Reads SKU | 50,000 |
| Stored data | 1GB Storage | 1GB Storage |

## Pricing Summary with Pipeline Operations

### Read and Write Units: Based on Document Size

One of the differences in pricing between editions lies in how reads and writes
are measured. In the Standard edition, costs are generally charged
per document. In the Enterprise edition, costs are charged per unit
based on document size: **reads are in units of 4KiB** , and **writes are in
units of 1KiB**.

|---|---|---|---|
| **Scenario (Reading documents)** | **Standard edition (Charged per document)** | **Enterprise edition (Charged per unit)** | **Pricing highlights** |
| **Reading a large 8KiB document** | Cost accrues **1 read**. | Cost accrues **2 read units** (8KiB /4KiB units, rounded up to 2 units). | Enterprise edition is cheaper. While Enterprise edition consumes more read units than Standard edition, the starting price for Enterprise edition read units is $0.05 per million read units v.s. $0.30 per million reads in Standard edition. |
| **Scanning a collection with 20 documents at 1KiB each** | Cost accrues **20 reads** | Collection scan: Cost accrues **5 read units** (20 documents \* 1KiB = 20KiB total; 20KiB / 4KiB units = 5 units) Indexed scan: Cost accrues **21 read units** (20 document each at 1KiB looked up, 1 index read) | Enterprise edition is significantly cheaper when documents are small (1--2KiB average document size). |

### Indexing Cost: Index Writes Consume Units

In the Enterprise edition, indexes are not free; they consume write
units when a document is written. An **additional write unit** is accrued for
each index-related field a document has.

|---|---|---|---|
| **Scenario (Writing a document)** | **Standard edition (No index write cost)** | **Enterprise edition (Index writes charged per 1KiB unit)** | **Pricing highlights** |
| **Writing a 5KiB document with 5 single-field indexes** | Cost accrues **1 write**. | The document itself accrues **5 write units** (5KiB / 1KiB per unit) with **5 additional write** units for the 5 indexes, totaling to **10 write units**. | Indexing overhead makes large writes with multiple indexes incur more write units on Enterprise edition. While Enterprise edition consumes more write units than Standard edition, the starting price for Enterprise edition write units is $0.26 per million write units v.s. $0.90 per million writes in Standard edition. |

### Real-time Listen Queries Pricing

Real-time queries are divided into two distinct steps with separate pricing
structure:

- **Initial query to sync results:**Retrieves the initial set of data and is charged using Read Units.
- **Real-time updates:** Subsequent updates that reflect document changes after the initial query and are charged using real-time update units.


For each updated document, you pay one real-time update unit per 4KiB of data.


You are also charged one real-time update unit when a document is removed from the result set. In contrast, when a document is deleted, you are not charged for a read.


Billing of listeners in the mobile and web SDKS also depends on whether offline persistence is enabled or not:

- If offline persistence is enabled and the listener is disconnected for more than 30 minutes (for example, if the user goes offline), you will be charged as if you had issued a brand-new query and real-time updates thereafter.
- If offline persistence is disabled, you will be charged for documents and index entries read as if you had issued a brand-new query whenever the listener disconnects and reconnects and real-time updates thereafter.

#### Free tier usage for Real-time updates

The free tier applies to only one Firestore database per project. The first
database that is created in a project without a free tier database will get the
free tier. The free tier for real-time update queries is 50,000 units per day.

After Free quota is consumed, the following pricing is applicable for Real-time
Read Units.

|---|---|---|---|
| **Regions** | **Default\* (USD)** | **Cloud Firestore CUD - 1 Year\* (USD)** | **Cloud Firestore CUD - 3 Year\* (USD)** |
| North America 5 (nam5) | $0.6 / 1,000,000 count | $0.48 / 1,000,000 count | 0.36 / 1,000,000 count |
| Northern Virginia (us-east4) | $0.3 / 1,000,000 count | $0.24 / 1,000,000 count | 0.18 / 1,000,000 count |
| Netherlands (europe-west4) | $0.315 / 1,000,000 count | $0.252 / 1,000,000 count | 0.189 / 1,000,000 count |
| Taiwan (asia-east1) | $0.347 / 1,000,000 count | $0.277 / 1,000,000 count | 0.208/ 1,000,000 count |
| Mumbai (asia-south1) | $0.312 / 1,000,000 count | $0.249 / 1,000,000 count | 0.187/ 1,000,000 count |
| Sao Paulo (southamerica-east1) | $0.476 / 1,000,000 count | $0.381 / 1,000,000 count | 0.285 / 1,000,000 count |

Customers are also eligible for a broader free-tier for
Firestore Enterprise edition. Details available on [Firestore Enterprise edition
pricing](https://cloud.google.com/firestore/enterprise/pricing). This includes a
free tier for read units of 50,000 per units per day. For more information on
how these pricing models work, see [Pricing
examples](https://firebase.google.com/firestore/pipelines/pricing-examples).