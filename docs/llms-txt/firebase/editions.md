# Source: https://firebase.google.com/docs/firestore/editions.md.txt

This page describesCloud Firestoreeditions and its key features.Cloud Firestoreis available in the following editions:

- **Standard edition**: provides a comprehensive suite of capabilities as a document database including fluent SDKs for a large number of programming languages, real-time and offline support, high availability in single and multi-region configurations, and a convenient serverless operation model with seamless autoscaling.
- **Enterprise edition**: provides MongoDB compatibility and a new query engine that supports a larger number of features and increased limits.

## Editions features

The following table summarizes the features available for each edition:

|                                                                         |                            **Standard**                            |                           **Enterprise**                           |
|-------------------------------------------------------------------------|--------------------------------------------------------------------|--------------------------------------------------------------------|
| Query Engine                                                            | Standard                                                           | Advanced                                                           |
| SupportsCloud Firestorein Native mode server-side, web, and mobile SDKs | Yes                                                                | event                                                              |
| Supports real-time and offline capabilities                             | Yes                                                                | event                                                              |
| SupportsCloud Firestorewith MongoDB compatibility                       | No                                                                 | Yes                                                                |
| Observability                                                           | - Key Visualizer - Query Explain - Query Insights                  | - Query Explain - Query Insights                                   |
| Data protection                                                         | - Scheduled backups - Point-in-time recovery                       | - Scheduled backups - Point-in-time recovery                       |
| Encryption                                                              | - Google-managed encryption key - Customer-managed encryption keys | - Google-managed encryption key - Customer-managed encryption keys |
| Storage                                                                 | Hybrid storage (SSD \& HDD)                                        | SSD                                                                |
| Committed Use Discounts                                                 | 20% for 1 year; 40% for 3 years                                    | 20% for 1 year; 40% for 3 years                                    |
| Document Size Limits                                                    | 1 MiB                                                              | 4 MiB                                                              |

## What you need to do

If you haven't selected an edition for yourCloud Firestoredatabase, it's automatically upgraded to Standard edition with no changes required on your part. If you want to create a newCloud FirestoreEnterprise edition database, follow the steps outlined in[Create aCloud Firestorewith MongoDB compatibility database](https://firebase.google.com/docs/firestore/enterprise/create-databases#create_a_database).

## Pricing

For information aboutCloud Firestoreeditions pricing, see pricing pages for[Enterprise edition](https://cloud.google.com/firestore/enterprise/pricing)and[Standard edition](https://cloud.google.com/firestore/pricing).