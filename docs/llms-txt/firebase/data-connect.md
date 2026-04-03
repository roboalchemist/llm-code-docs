# Source: https://firebase.google.com/docs/reference/data-connect.md.txt

# Source: https://firebase.google.com/docs/data-connect.md.txt

# Firebase Data Connect

plat_iosplat_androidplat_webplat_flutter  
Firebase's first relational database solution for developers who want to create secure and scalable apps with Cloud SQL for PostgreSQL and type-safe mobile and web SDKs.[Learn more](https://firebase.google.com/products/data-connect).

Firebase Data Connectis a relational database service for mobile and web apps that lets you build and scale using a fully-managed PostgreSQL database powered by Cloud SQL. It provides secure schema, query and mutation management using GraphQL technology that integrates well withFirebase Authentication. You can quickly integrate this product into your mobile and web apps with SDK support in Kotlin Android, iOS, Flutter, and web.

Data Connectlets you declare your application's data model and the exact queries needed by your application. Using your data model we automatically create a PostgreSQL database schema to fit your data model, secure server endpoints that talk to the database, and type-safe SDKs for your client application that talk to the server endpoints. It's like a "self-driving app server" made-to-order for your specific application.

## Key capabilities

|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Backed by Cloud SQL for PostgreSQL   | Rely on a fully-managed database service that helps you set up, maintain, manage, and administer your PostgreSQL relational databases on Google Cloud.                                                                                                                       |
| Vector search                        | Data Connectsupports vector search for developers to build AI-powered applications.                                                                                                                                                                                          |
| Multiple platform SDKs               | Firebase Data Connectoffers multi-platform SDKs, for Kotlin Android, iOS, Flutter, and web.                                                                                                                                                                                  |
| User-based authentication            | Data Connectsupports end-user authentication, ensuring that only authorized users can access the data.                                                                                                                                                                       |
| Visual Studio Code extension         | Offers easy schema development, and query and mutation management, directly from your Visual Studio Code editor using GraphQL.                                                                                                                                               |
| Emulator                             | Firebase Data Connectincludes an emulator that lets you test your app with a local database without having to deploy to production.                                                                                                                                          |
| AI assistance from Gemini inFirebase | Use Gemini inFirebaseto generate queries and mutations on-demand using natural language and test them directly in theFirebaseconsole. Learn more at[UseAI assistance forData Connectfor queries and mutations](https://firebase.google.com/docs/data-connect/ai-assistance). |

## How does it work?

The top-level resource forFirebase Data Connectis a*service* , which represents a managed GraphQL API that can be defined by developers and called by end users. Your*schema* is the app data model for a service, represented primarily as a collection of GraphQL source files, as well as specific configuration for attached datasources (such as Cloud SQL instances). There can be only one schema per service. Finally, your*connectors*are collections of queries and mutations that have been defined to operate against a service's schema. There can be many connectors per service (for instance if you have a "rider" app and a "driver" app for your rideshare company).

YourData Connectschema maps explicitly to a specific underlying PostgreSQL database schema.Data Connectincludes tooling to automatically generate the SQL DDL needed to perform schema migrations based on changes to the app schema. Based on your app schema,Data Connectautomatically generates additional GraphQL schema to query and manipulate the data model.

Once your app schema is defined, you can write predefined queries and mutations that are executed to read and write data in the application.Data Connectqueries and mutations are not submitted by client code and executed on the server. Instead, when deployed, theseData Connectoperations are stored on the server, like Cloud Functions. This simplifies code management, and development of your client code. In privileged environments, like theFirebaseconsole and using our Data Connect VS Code extension, you can execute ad hoc operations with appropriate Google IAM credentials for administrative operations.

For client code, each supported platform has a*core SDK* that handles connecting to the backend, issuing requests, and processing responses. These SDKs are not schema-aware and must be supplied with operation names and variables as unstructured data. Each supported platform also has a*generated SDK*. As you define your data model and operations, tooling on your machine will automatically generate strongly-typed SDKs specific to the application. These SDKs will "wrap" the core SDKs for type safety, ergonomics, and other features such as data validation and more down the road.

## Implementation path

|---|------------------------------|-----------------------------------------------------------------------------------------------------------------------|
|   | Prototype your schema        | Prototype your database schema, including designs using vector types, starting in a local environment with tooling    |
|   | Prototype your operations    | Build predefined query and mutation operations for client apps based on automatically-generated queries and mutations |
|   | Generate type-safe SDKs      | Generate and test type-safe SDKs from your schema and operations, then implement client-side code                     |
|   | Deploy schema and operations | Deploy the schema and operations for yourFirebase Data Connectservice                                                 |
|   | Deploy clients               | Deploy your client code                                                                                               |

## Next steps

- Try outData Connectright now: explore a quickstart app repository and build a fully-featuredData Connectapp by following our[codelab for web](https://firebase.google.com/codelabs/firebase-dataconnect-web),[codelab for iOS](https://firebase.google.com/codelabs/firebase-dataconnect-ios), or[codelab for Android](https://firebase.google.com/codelabs/firebase-dataconnect-android).
- If you'd like to see theFirebase Data Connectdevelopment flow in action, read through the[Get started guide](https://firebase.google.com/docs/data-connect/quickstart).
- Learn aboutData Connect[pricing and billing](https://firebase.google.com/docs/data-connect/pricing).