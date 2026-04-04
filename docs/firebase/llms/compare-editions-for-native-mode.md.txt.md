# Source: https://firebase.google.com/docs/firestore/compare-editions-for-native-mode.md.txt

<br />

With the introduction of Firestore in Native mode support in the
Enterprise edition, both Firestore Core and Pipeline operations are
available. The Core operations function differently than in the
Standard edition, because of new
indexing rules and a different pricing model.

|---|---|---|
| **Feature** | **Standard edition** | **Enterprise edition** |
| **Supported querying operations** | Limited to Firestore Core operations. | Supports Firestore Core and Pipeline operations, and Firestore MongoDB compatibility operations. |
| **Indexing Requirement** | All queries require indexes. | Indexes are not required for queries. |
| **Index creation** | **Automatic indexes** are created for single fields. You can manually create composite indexes. | **No automatic indexes** are created. Indexes need to be [manually managed](https://firebase.google.com/docs/firestore/enterprise/index-overview-native). |
| **Query Performance and Cost** | Queries are generally **performant** due to index requirements. | Query **costs and performance can be better than the Standard edition with indexes** . You can identify missing indexes using Query Explain and Query Insights. Queries **without indexes may risk being non-performant and costly** as the dataset grows, requiring monitoring and tuning. |
| **Indexing Overhead Cost** | No charge for index entry writes, as indexes are automatic. However, **required indexes incur storage costs.** | Writing index entries **consume write units** when an associated document is written (1 write unit per 1 KiB of index entry size). You save on storage costs by not creating index entries for every field. |
| **Billing Model (Reads/Writes/Deletes)** | Charged per **document read, write, and delete**. | Charged for **reads and writes in byte tranches** . Reads are charged in **Read Units** (4 KiB tranches). Writes and deletes are merged into **Write Units** (1 KiB tranches). |
| **Base Pricing (per million)** Prices shown are for the *us-central1* region. | Reads: **$0.03 per 100,000 documents** (or $0.30 per million). Writes: **$0.09 per 100,000 documents** (or $0.90 per million). Deletes: **$0.01 per 100,000 documents** (or $0.10 per million) | Read Units: **$0.05 per 1 million** read units. Write Units: **$0.26 per 1 million** write units. Prices are generally **lower if documents are under 4KiB** compared to the Standard Read cost. |
| **Real-time Updates** Prices shown are for the *us-central1* region | Real-time updates are **included billed as Reads at $0.03 per 100,000 documents**. | Real-time updates have a **separate SKU** (Real-time update units), charged per 4 KiB tranche. Real-time updates cost **$0.30 per million read units**. |