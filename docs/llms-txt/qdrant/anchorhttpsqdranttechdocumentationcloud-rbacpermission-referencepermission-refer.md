# [Anchor](https://qdrant.tech/documentation/cloud-rbac/permission-reference/\#permission-reference)**Permission Reference**

This document outlines the permissions available in Qdrant Cloud.

* * *

> 💡 When enabling `write:*` permissions in the UI, the corresponding `read:*` permission will also be enabled and non-actionable. This guarantees access to resources after creating and/or updating them.

## [Anchor](https://qdrant.tech/documentation/cloud-rbac/permission-reference/\#identity-and-access-management)**Identity and Access Management**

Permissions for users, user roles, management keys, and invitations.

| Permission | Description |
| --- | --- |
| `read:roles` | View roles in the Access Management page. |
| `write:roles` | Create and modify roles in the Access Management page. |
| `delete:roles` | Remove roles in the Access Management page. |
| `read:management_keys` | View Cloud Management Keys in the Access Management page. |
| `write:management_keys` | Create and manage Cloud Management Keys. |
| `delete:management_keys` | Remove Cloud Management Keys in the Access Management page. |
| `write:invites` | Invite new users to an account and revoke invitations. |
| `read:invites` | View pending invites in an account. |
| `delete:invites` | Remove an invitation. |
| `read:users` | View user details in the profile page.<br>\- Also applicable in User Management and Role details (User tab). |
| `delete:users` | Remove users from an account.<br>\- Applicable in User Management and Role details (User tab). |

* * *

## [Anchor](https://qdrant.tech/documentation/cloud-rbac/permission-reference/\#cluster)**Cluster**

Permissions for API Keys, backups, clusters, and backup schedules.

### [Anchor](https://qdrant.tech/documentation/cloud-rbac/permission-reference/\#api-keys)**API Keys**

| Permission | Description |
| --- | --- |
| `read:api_keys` | View Database API Keys for Managed Cloud clusters. |
| `write:api_keys` | Create new Database API Keys for Managed Cloud clusters. |
| `delete:api_keys` | Remove Database API Keys for Managed Cloud clusters. |

### [Anchor](https://qdrant.tech/documentation/cloud-rbac/permission-reference/\#backups)**Backups**

| Permission | Description |
| --- | --- |
| `read:backups` | View backups in the **Backups page** and **Cluster details > Backups tab**. |
| `write:backups` | Create backups from the **Backups page** and **Cluster details > Backups tab**. |
| `delete:backups` | Remove backups from the **Backups page** and **Cluster details > Backups tab**. |

### [Anchor](https://qdrant.tech/documentation/cloud-rbac/permission-reference/\#clusters)**Clusters**

| Permission | Description |
| --- | --- |
| `read:clusters` | View cluster details. |
| `write:clusters` | Modify cluster settings. |
| `delete:clusters` | Delete clusters. |

### [Anchor](https://qdrant.tech/documentation/cloud-rbac/permission-reference/\#backup-schedules)**Backup Schedules**

| Permission | Description |
| --- | --- |
| `read:backup_schedules` | View backup schedules in the **Backups page** and **Cluster details > Backups tab**. |
| `write:backup_schedules` | Create backup schedules from the **Backups page** and **Cluster details > Backups tab**. |
| `delete:backup_schedules` | Remove backup schedules from the **Backups page** and **Cluster details > Backups tab**. |

* * *

## [Anchor](https://qdrant.tech/documentation/cloud-rbac/permission-reference/\#hybrid-cloud)**Hybrid Cloud**

Permissions for Hybrid Cloud environments.

| Permission | Description |
| --- | --- |
| `read:hybrid_cloud_environments` | View Hybrid Cloud environment details. |
| `write:hybrid_cloud_environments` | Modify Hybrid Cloud environment settings. |
| `delete:hybrid_cloud_environments` | Delete Hybrid Cloud environments. |

* * *

## [Anchor](https://qdrant.tech/documentation/cloud-rbac/permission-reference/\#payment--billing)**Payment & Billing**

Permissions for payment methods and billing information.

| Permission | Description |
| --- | --- |
| `read:payment_information` | View payment methods and billing details. |
| `write:payment_information` | Modify or remove payment methods and billing details. |

* * *

## [Anchor](https://qdrant.tech/documentation/cloud-rbac/permission-reference/\#account-management)**Account Management**

Permissions for managing user accounts.

| Permission | Description |
| --- | --- |
| `read:account` | View account details that the user is a part of. |
| `write:account` | Modify account details such as:<br>\- Editing the account name<br>\- Setting an account as default<br>\- Leaving an account<br>**(Only available to Owners)** |
| `delete:account` | Remove an account from:<br>\- The **Profile page** (list of user accounts).<br>\- The **active account** (if the user is an owner/admin). |

* * *

## [Anchor](https://qdrant.tech/documentation/cloud-rbac/permission-reference/\#profile)**Profile**

Permissions for accessing personal profile information.

| Permission | Description |
| --- | --- |
| `read:profile` | View the user’s own profile information.<br>**(Assigned to all users by default)** |

* * *

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud-rbac/permission-reference.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud-rbac/permission-reference.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-69-lllmstxt|>
## vector-search-manuals
- [Articles](https://qdrant.tech/articles/)
- Vector Search Manuals

#### Vector Search Manuals

Take full control of your vector data with Qdrant. Learn how to easily store, organize, and optimize vectors for high-performance similarity search.

[![Preview](https://qdrant.tech/articles_data/vector-search-production/preview/preview.jpg)\\
**Vector Search in Production** \\
We gathered our most recommended tips and tricks to make your production deployment run smoothly.\\
\\
David Myriel\\
\\
April 30, 2025](https://qdrant.tech/articles/vector-search-production/)[![Preview](https://qdrant.tech/articles_data/indexing-optimization/preview/preview.jpg)\\
**Optimizing Memory for Bulk Uploads** \\
Efficient memory management is key when handling large-scale vector data. Learn how to optimize memory consumption during bulk uploads in Qdrant and keep your deployments performant under heavy load.\\
\\
Sabrina Aquino\\
\\
February 13, 2025](https://qdrant.tech/articles/indexing-optimization/)[![Preview](https://qdrant.tech/articles_data/vector-search-resource-optimization/preview/preview.jpg)\\
**Vector Search Resource Optimization Guide** \\
Learn how to get the most from Qdrant's optimization features. Discover key tricks and best practices to boost vector search performance and reduce Qdrant's resource usage.\\
\\
David Myriel\\
\\
February 09, 2025](https://qdrant.tech/articles/vector-search-resource-optimization/)[![Preview](https://qdrant.tech/articles_data/what-is-a-vector-database/preview/preview.jpg)\\
**What is a Vector Database?** \\
Discover what a vector database is, its core functionalities, and real-world applications.\\
\\
Sabrina Aquino\\
\\
October 09, 2024](https://qdrant.tech/articles/what-is-a-vector-database/)[![Preview](https://qdrant.tech/articles_data/what-is-vector-quantization/preview/preview.jpg)\\
**What is Vector Quantization?** \\
In this article, we'll teach you about compression methods like Scalar, Product, and Binary Quantization. Learn how to choose the best method for your specific application.\\
\\
Sabrina Aquino\\
\\
September 25, 2024](https://qdrant.tech/articles/what-is-vector-quantization/)[![Preview](https://qdrant.tech/articles_data/vector-search-filtering/preview/preview.jpg)\\
**A Complete Guide to Filtering in Vector Search** \\
Learn everything about filtering in Qdrant. Discover key tricks and best practices to boost semantic search performance and reduce Qdrant's resource usage.\\
\\
Sabrina Aquino, David Myriel\\
\\
September 10, 2024](https://qdrant.tech/articles/vector-search-filtering/)[![Preview](https://qdrant.tech/articles_data/hybrid-search/preview/preview.jpg)\\
**Hybrid Search Revamped - Building with Qdrant's Query API** \\
Our new Query API allows you to build a hybrid search system that uses different search methods to improve search quality & experience. Learn more here.\\
\\
Kacper Łukawski\\
\\
July 25, 2024](https://qdrant.tech/articles/hybrid-search/)[![Preview](https://qdrant.tech/articles_data/data-privacy/preview/preview.jpg)\\
**Data Privacy with Qdrant: Implementing Role-Based Access Control (RBAC)** \\
Discover how Qdrant's Role-Based Access Control (RBAC) ensures data privacy and compliance for your AI applications. Build secure and scalable systems with ease. Read more now!\\
\\
Qdrant Team\\
\\
June 18, 2024](https://qdrant.tech/articles/data-privacy/)[![Preview](https://qdrant.tech/articles_data/what-are-embeddings/preview/preview.jpg)\\
**What are Vector Embeddings? - Revolutionize Your Search Experience** \\
Discover the power of vector embeddings. Learn how to harness the potential of numerical machine learning representations to create a personalized Neural Search Service with FastEmbed.\\
\\
Sabrina Aquino\\
\\
February 06, 2024](https://qdrant.tech/articles/what-are-embeddings/)[![Preview](https://qdrant.tech/articles_data/multitenancy/preview/preview.jpg)\\
**How to Implement Multitenancy and Custom Sharding in Qdrant** \\
Discover how multitenancy and custom sharding in Qdrant can streamline your machine-learning operations. Learn how to scale efficiently and manage data securely.\\
\\
David Myriel\\
\\
February 06, 2024](https://qdrant.tech/articles/multitenancy/)[![Preview](https://qdrant.tech/articles_data/sparse-vectors/preview/preview.jpg)\\
**What is a Sparse Vector? How to Achieve Vector-based Hybrid Search** \\
Learn what sparse vectors are, how they work, and their importance in modern data processing. Explore methods like SPLADE for creating and leveraging sparse vectors efficiently.\\
\\
Nirant Kasliwal\\
\\
December 09, 2023](https://qdrant.tech/articles/sparse-vectors/)[![Preview](https://qdrant.tech/articles_data/storing-multiple-vectors-per-object-in-qdrant/preview/preview.jpg)\\
**Optimizing Semantic Search by Managing Multiple Vectors** \\
Discover the power of vector storage optimization and learn how to efficiently manage multiple vectors per object for enhanced semantic search capabilities.\\
\\
Kacper Łukawski\\
\\
October 05, 2022](https://qdrant.tech/articles/storing-multiple-vectors-per-object-in-qdrant/)[![Preview](https://qdrant.tech/articles_data/batch-vector-search-with-qdrant/preview/preview.jpg)\\
**Mastering Batch Search for Vector Optimization** \\
Discover how to optimize your vector search capabilities with efficient batch search. Learn optimization strategies for faster, more accurate results.\\
\\
Kacper Łukawski\\
\\
September 26, 2022](https://qdrant.tech/articles/batch-vector-search-with-qdrant/)[![Preview](https://qdrant.tech/articles_data/neural-search-tutorial/preview/preview.jpg)\\
**Neural Search 101: A Complete Guide and Step-by-Step Tutorial** \\
Discover the power of neural search. Learn what neural search is and follow our tutorial to build a neural search service using BERT, Qdrant, and FastAPI.\\
\\
Andrey Vasnetsov\\
\\
June 10, 2021](https://qdrant.tech/articles/neural-search-tutorial/)

×

[Powered by](https://qdrant.tech/)

<|page-70-lllmstxt|>
## snapshots
- [Documentation](https://qdrant.tech/documentation/)
- [Concepts](https://qdrant.tech/documentation/concepts/)
- Snapshots