# Source: https://firebase.google.com/docs/firestore/enterprise/query-realtime-pricing-examples.md.txt

<br />

\`

<br />

> [!WARNING]
> **Preview:** **Firestore in Native mode (with Pipeline operations) for Enterprise
> edition** is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific
> Terms](https://cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage
> descriptions](https://cloud.google.com/products#product-launch-stages).

Here are some examples that'll help you understand pricing of Firestore
Enterprise edition in various scenarios.

## Query pricing example

**Scenario:** A query filters on a field `username` with the value
`ilovefirebase` in a collection containing 100 documents, where each document is
2KiB in size. Let's assume there is only one `username` with the value
`ilovefirebase`. The same query is ran 1 million times.

|---|---|---|---|
| **Activity** | **Standard edition (Auto-Indexed query)** | **Enterprise edition (Indexed query)** | **Enterprise edition (Unindexed Collection Scan)** |
| **Indexing Status** | **Uses automatically created index** for the username lookup. | After **manual index creation** on the username field. | **Does not use an index**; scans the entire 200KiB user collection. |
| **Read Units Per Query** | Cost accrues **1 read**. | Cost accrues **2 read units** (1 for index scan and 1 for document read). | Cost accrues **50 read units** (100 documents at 2KiB = 200KiB total scan. 200KiB / 4KiB per unit = 50 units). |
| **Total Cost (per 1 Million Queries)** | **$0.30 per million queries** (1 read @ $0.30/million read units). | **$0.10 per million queries** (2 read unit @ $0.05/million read units). | **$2.50 per million queries** (50 read units @ $0.05/million). |


**Cost difference summary**

- **Indexed query:** The same query on Enterprise edition costs $0.10 per million with a manually created index on the username field.
- **Unindexed collection scan query:** An unindexed collection scan query in Enterprise edition costs **$2.50 per million**, which is significantly higher than the $0.30 charged for the equivalent auto-indexed read in Standard edition. This illustrates that querying without indexes can lead to non-performant and costly execution.
- **Cost advantage:** **$0.10 per million read units** is three times cheaper than the Standard edition indexed read cost. This demonstrates the low base price of the Enterprise edition read unit when queries are optimized.

## Real-time pricing example

For more information about pricing, see [real-time pricing](https://firebase.google.com/docs/firestore/pipelines/pricing#real-time-listen-queries-pricing).


**Scenario 1:**One million clients query for the 10 most recent posts in a collection (indexed on a timestamp). Each post is 6KiB in size. Two of these posts are subsequently updated, resulting in real-time updates being pushed to the clients.

<br />

|---|---|---|---|
| **Activity** | **Standard edition** | **Enterprise edition** | **Pricing Highlights** |
| **Pricing Model** | Initial query and real-time updates are both charged per document read. | Initial query is charged using read unit (4KiB tranche). Real-time updates use a separate Real-time updates SKU. | Enterprise edition leverages read unit pricing for cheaper initial reads |
| **First Read (Initial sync of 10 posts with 6KiB documents each)** | **10 reads** are incurred per client (document size doesn't matter). | **21 read units** are incurred per client (1 read unit for the index scan of 10 posts) (20 read units: 2 read units per 6KiB document \* 10 documents) | Enterprise edition consumes more units (21 versus 10) but at a much lower unit price. |
| **First Read Cost (per 1 million )** | 10 reads \* 1 million clients at $0.30/million: $**3.00**. | 21 read units \* 1 million clients at 0.05/million: $**1.05**. | Initial read is 4 times cheaper in the Enterprise edition. |
| **Real-time updates (2 updates to 6 KiB documents)** | **2 reads** are incurred (2 updated documents). | **4 real-time update units** are incurred (2 real-time update units per 6KiB documents \* 2 real-time updates). | Enterprise edition separates real-time updates into a dedicated SKU. |
| **Real-time cost (per 1 million clients)** | 2 reads \* 1 million clients at $0.30/million: $**0.60.** | 4 real-time units \* 1 million clients at $0.30/million: $**1.20**. | Real-time cost is higher in the Enterprise edition for this specific update scenario. |
| **Total cost** | **$3.60** ($3.00 +$ $0.60). | **$2.25** ($1.05 + $1.20). | **Enterprise edition is cheaper ($2.25 vs $3.60)** in this scenario involving large documents (6KiB) and high volume. |

## Additional Real-time Listen queries pricing examples for Enterprise edition


For illustration, the costs in the following scenarios are calculated using the
*us-central1* rate of $0.05 per million read units and $0.30 per million
real-time update units.

|---|---|---|---|---|---|---|
| **Scenario (Clients, Document Size)** | **Phase 1: Initial Query (Sync) Details** | **Phase 1: Initial Query Consumption** | **Illustrative cost** | **Phase 2: Real-time Updates Details** | **Phase 2: Real-time Updates Consumption** | **Illustrative cost** |
| **1 client, 2KiB docs** | Query runs an unindexed collection scan of 10,000 sequential documents of 2KiB each. | **5,000 Read Units** | $0.00025 (calculated based on $0.05/million) | Client receives 1,000 total documents using real-time updates, with a size of 2KiB per document. | **1,000 Real-time Update Units** | $0.003 (Calculated based on $0.30/million) |
| **1,000 clients, 2KiB docs** | 1,000 clients each run a query that does an unindexed collection scan of 10,000 sequential documents of 2KiB each. | **5 million Read Units** | $0.25 (calculated based on $0.05/million) | 1,000 clients each receive 1,000 total documents using real-time updates, with a size of 2KiB per document. | **1 million Real-time Update Units** | $0.30 (calculated based on $0.30/million) |
| **1,000 clients, 6KiB docs** | 1,000 clients each run a query that does an unindexed collection scan of 10,000 sequential documents of 6KiB each. | **15 million Read Units** | $0.75 (calculated based on $0.05/million) | 1,000 clients each receive 1,000 total documents using real-time updates, with a size of 6KiB each. | **2 million Real-time Update Units** | $0.60 (Calculated based on $0.30/million) |