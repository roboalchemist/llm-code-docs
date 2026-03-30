# Data Privacy with Qdrant: Implementing Role-Based Access Control (RBAC)

Qdrant Team

·

June 18, 2024

![ Data Privacy with Qdrant: Implementing Role-Based Access Control (RBAC)](https://qdrant.tech/articles_data/data-privacy/preview/title.jpg)

Data stored in vector databases is often proprietary to the enterprise and may include sensitive information like customer records, legal contracts, electronic health records (EHR), financial data, and intellectual property. Moreover, strong security measures become critical to safeguarding this data. If the data stored in a vector database is not secured, it may open a vulnerability known as “ [embedding inversion attack](https://arxiv.org/abs/2004.00053),” where malicious actors could potentially [reconstruct the original data from the embeddings](https://arxiv.org/pdf/2305.03010) themselves.

Strict compliance regulations govern data stored in vector databases across various industries. For instance, healthcare must comply with HIPAA, which dictates how protected health information (PHI) is stored, transmitted, and secured. Similarly, the financial services industry follows PCI DSS to safeguard sensitive financial data. These regulations require developers to ensure data storage and transmission comply with industry-specific legal frameworks across different regions. **As a result, features that enable data privacy, security and sovereignty are deciding factors when choosing the right vector database.**

This article explores various strategies to ensure the security of your critical data while leveraging the benefits of vector search. Implementing some of these security approaches can help you build privacy-enhanced similarity search algorithms and integrate them into your AI applications.
Additionally, you will learn how to build a fully data-sovereign architecture, allowing you to retain control over your data and comply with relevant data laws and regulations.

> To skip right to the code implementation, [click here](https://qdrant.tech/articles/data-privacy/#jwt-on-qdrant).

## [Anchor](https://qdrant.tech/articles/data-privacy/\#vector-database-security-an-overview) Vector Database Security: An Overview

Vector databases are often unsecured by default to facilitate rapid prototyping and experimentation. This approach allows developers to quickly ingest data, build vector representations, and test similarity search algorithms without initial security concerns. However, in production environments, unsecured databases pose significant data breach risks.

For production use, robust security systems are essential. Authentication, particularly using static API keys, is a common approach to control access and prevent unauthorized modifications. Yet, simple API authentication is insufficient for enterprise data, which requires granular control.

The primary challenge with static API keys is their all-or-nothing access, inadequate for role-based data segregation in enterprise applications. Additionally, a compromised key could grant attackers full access to manipulate or steal data. To strengthen the security of the vector database, developers typically need the following:

1. **Encryption**: This ensures that sensitive data is scrambled as it travels between the application and the vector database. This safeguards against Man-in-the-Middle ( [MitM](https://en.wikipedia.org/wiki/Man-in-the-middle_attack)) attacks, where malicious actors can attempt to intercept and steal data during transmission.
2. **Role-Based Access Control**: As mentioned before, traditional static API keys grant all-or-nothing access, which is a significant security risk in enterprise environments. RBAC offers a more granular approach by defining user roles and assigning specific data access permissions based on those roles. For example, an analyst might have read-only access to specific datasets, while an administrator might have full CRUD (Create, Read, Update, Delete) permissions across the database.
3. **Deployment Flexibility**: Data residency regulations like GDPR (General Data Protection Regulation) and industry-specific compliance requirements dictate where data can be stored, processed, and accessed. Developers would need to choose a database solution which offers deployment options that comply with these regulations. This might include on-premise deployments within a company’s private cloud or geographically distributed cloud deployments that adhere to data residency laws.

## [Anchor](https://qdrant.tech/articles/data-privacy/\#how-qdrant-handles-data-privacy-and-security) How Qdrant Handles Data Privacy and Security

One of the cornerstones of our design choices at Qdrant has been the focus on security features. We have built in a range of features keeping the enterprise user in mind, which allow building of granular access control on a fully data sovereign architecture.

A Qdrant instance is unsecured by default. However, when you are ready to deploy in production, Qdrant offers a range of security features that allow you to control access to your data, protect it from breaches, and adhere to regulatory requirements. Using Qdrant, you can build granular access control, segregate roles and privileges, and create a fully data sovereign architecture.

### [Anchor](https://qdrant.tech/articles/data-privacy/\#api-keys-and-tls-encryption) API Keys and TLS Encryption

For simpler use cases, Qdrant offers API key-based authentication. This includes both regular API keys and read-only API keys. Regular API keys grant full access to read, write, and delete operations, while read-only keys restrict access to data retrieval operations only, preventing write actions.

On Qdrant Cloud, you can create API keys using the [Cloud Dashboard](https://qdrant.to/cloud). This allows you to generate API keys that give you access to a single node or cluster, or multiple clusters. You can read the steps to do so [here](https://qdrant.tech/documentation/cloud/authentication/).

![web-ui](https://qdrant.tech/articles_data/data-privacy/web-ui.png)

For on-premise or local deployments, you’ll need to configure API key authentication. This involves specifying a key in either the Qdrant configuration file or as an environment variable. This ensures that all requests to the server must include a valid API key sent in the header.

When using the simple API key-based authentication, you should also turn on TLS encryption. Otherwise, you are exposing the connection to sniffing and MitM attacks. To secure your connection using TLS, you would need to create a certificate and private key, and then [enable TLS](https://qdrant.tech/documentation/guides/security/#tls) in the configuration.

API authentication, coupled with TLS encryption, offers a first layer of security for your Qdrant instance. However, to enable more granular access control, the recommended approach is to leverage JSON Web Tokens (JWTs).

### [Anchor](https://qdrant.tech/articles/data-privacy/\#jwt-on-qdrant) JWT on Qdrant

JSON Web Tokens (JWTs) are a compact, URL-safe, and stateless means of representing _claims_ to be transferred between two parties. These claims are encoded as a JSON object and are cryptographically signed.

JWT is composed of three parts: a header, a payload, and a signature, which are concatenated with dots (.) to form a single string. The header contains the type of token and algorithm being used. The payload contains the claims (explained in detail later). The signature is a cryptographic hash and ensures the token’s integrity.

In Qdrant, JWT forms the foundation through which powerful access controls can be built. Let’s understand how.

JWT is enabled on the Qdrant instance by specifying the API key and turning on the **jwt\_rbac** feature in the configuration (alternatively, they can be set as environment variables). For any subsequent request, the API key is used to encode or decode the token.

The way JWT works is that just the API key is enough to generate the token, and doesn’t require any communication with the Qdrant instance or server. There are several libraries that help generate tokens by encoding a payload, such as [PyJWT](https://pyjwt.readthedocs.io/en/stable/) (for Python), [jsonwebtoken](https://www.npmjs.com/package/jsonwebtoken) (for JavaScript), and [jsonwebtoken](https://crates.io/crates/jsonwebtoken) (for Rust). Qdrant uses the HS256 algorithm to encode or decode the tokens.

We will look at the payload structure shortly, but here’s how you can generate a token using PyJWT.

```python
import jwt
import datetime