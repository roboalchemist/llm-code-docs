# Source: https://firebase.google.com/docs/firestore/solutions.md.txt

<br />

As you develop your app withCloud Firestore, you might want to go beyond the basics discussed in the manage and query data sections. The solutions outlined in this section offer guidance on more advanced use cases.

## Integrate with BigQuery

**Summary:** UseFirebase Extensionsto integrate data inCloud FirestorewithBigQuery

**Use case:** If you need to analyze large amounts of data, you can useBigQuery.

[See the solution forBigQueryextensions](https://firebase.google.com/docs/firestore/solutions/bigquery)

## Implement an AI-driven chatbot

**Summary:** UseFirebase Extensionsto add an AI-driven chatbot to your app.

**Use case:**You can use chatbots to improve customer service, market a new feature or service, provide sales quotes, or any number of use cases. Get started by using these extensions.

[See the solution for AI chatbot extensions](https://firebase.google.com/docs/firestore/solutions/ai-chatbot)

## Enrich handling of text

**Summary:** UseFirebase Extensionsto mine and analyze text data.

**Use case:**If you need to summarize text, detect toxic speech, translate text, or transcribe audio, use these extensions.

[See the solution for text handling extensions](https://firebase.google.com/docs/firestore/solutions/enriched-text)

## Enrich value of media

**Summary:** UseFirebase Extensionsto mine and analyze media streams.

**Use case:**If you need to classify images, convert speech to text, or perform optical character recognition (OCR), use these extensions.

[See the solution for media processing extensions](https://firebase.google.com/docs/firestore/solutions/enriched-media)

## Firestore Lite, the streamlined REST-only Firestore Web SDK

**Summary:**Build smaller Web apps with faster load times when offline cache isn't important and you only need online access to your database.

**Use case:** If your app doesn't need to manage offline users, import`@firebase\firestore-lite`. Then, code features that make use of the Firestore backend.

[See the solution for Firestore Lite](https://firebase.google.com/docs/firestore/solutions/firestore-lite)

## Aggregation queries

**Summary:** Build an aggregate of your data inCloud Firestoreusing transactions andCloud Functions.

**Use case:**To query your data across collections, build an aggregate, then run the query. For example, in a recommendations app, you might want to retrieve all the information for a particular restaurant from different collections.

[See the solution for aggregation queries](https://firebase.google.com/docs/firestore/solutions/aggregation)

## Distributed counters

**Summary:** Distribute updates across "counter" subcollections to update a document more frequently thanCloud Firestorecurrently supports.

**Use case:** Use this solution to add "counters" to your app (for example, to represent upvotes), and update the corresponding document at a high frequency.Cloud Firestoresupports 2 writes/second on each document.

[See the solution for distributed counters](https://firebase.google.com/docs/firestore/solutions/counters)

## Full-text search

**Summary:** Search for text contained in yourCloud Firestoredocuments.

**Use case:**Users might want to search your app content, including text contained in individual fields across your documents and collections. Use this solution to enable full-text search.

[See the solution for full-text search](https://firebase.google.com/docs/firestore/solutions/search)

## Build presence

**Summary:**Add a presence system that identifies whether or not a user is actively connected.

**Use case:**Use this solution to identify users that are actively connected to your app. For example, in a chat app, you might use a presence system to populate a list of users that are online.

[See the solution for building presence](https://firebase.google.com/docs/firestore/solutions/presence)

## Secure data access for users and groups

**Summary:**Write security rules to control access to individual documents based on user roles.

**Use case:**Use this solution to build collaborative apps while minimizing the risk of improper data access.

[See the solution for secure data access](https://firebase.google.com/docs/firestore/solutions/role-based-access)

## Schedule data exports

**Summary:** Use theApp EngineCron Service to schedule exports of your data.

**Use case:**Use this solution to run export operations on a schedule.

[See the solution for scheduling exports](https://firebase.google.com/docs/firestore/solutions/schedule-export)