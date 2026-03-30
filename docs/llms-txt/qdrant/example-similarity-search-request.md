# Example similarity search request
response = qdrant_client.search(
    collection_name="demo_collection",
    query_vector=search_vector,
    limit=5  # Number of results to retrieve
)

```

For convenience, we have added a JWT generation tool in the Qdrant Web UI, which is present under the 🔑 tab. For your local deployments, you will find it at [http://localhost:6333/dashboard#/jwt](http://localhost:6333/dashboard#/jwt).

### [Anchor](https://qdrant.tech/articles/data-privacy/\#payload-configuration) Payload Configuration

There are several different options (claims) you can use in the JWT payload that help control access and functionality. Let’s look at them one by one.

**exp**: This claim is the expiration time of the token, and is a unix timestamp in seconds. After the expiration time, the token will be invalid.

**value\_exists**: This claim validates the token against a specific key-value stored in a collection. By using this claim, you can revoke access by simply changing a value without having to invalidate the API key.

**access**: This claim defines the access level of the token. The access level can be global read (r) or manage (m). It can also be specific to a collection, or even a subset of a collection, using read (r) and read-write (rw).

Let’s look at a few example JWT payload configurations.

**Scenario 1: 1-hour expiry time, and read-only access to a collection**

```json
{
  "exp": 1690995200,  // Set to 1 hour from the current time (Unix timestamp)
  "access": [\
    {\
      "collection": "demo_collection",\
      "access": "r"  // Read-only access\
    }\
  ]
}

```

**Scenario 2: 1-hour expiry time, and access to user with a specific role**

Suppose you have a ‘users’ collection and have defined specific roles for each user, such as ‘developer’, ‘manager’, ‘admin’, ‘analyst’, and ‘revoked’. In such a scenario, you can use a combination of **exp** and **value\_exists**.

```json
{
  "exp":  1690995200,
  "value_exists": {
    "collection": "users",
    "matches": [\
      { "key": "username", "value": "john" },\
      { "key": "role", "value": "developer" }\
    ],
  },
}

```

Now, if you ever want to revoke access for a user, simply change the value of their role. All future requests will be invalid using a token payload of the above type.

**Scenario 3: 1-hour expiry time, and read-write access to a subset of a collection**

You can even specify access levels specific to subsets of a collection. This can be especially useful when you are leveraging [multitenancy](https://qdrant.tech/documentation/guides/multiple-partitions/), and want to segregate access.

```json
{
  "exp": 1690995200,
  "access": [\
    {\
      "collection": "demo_collection",\
      "access": "r",\
      "payload": {\
        "user_id": "user_123456"\
      }\
    }\
  ]
}

```

By combining the claims, you can fully customize the access level that a user or a role has within the vector store.

### [Anchor](https://qdrant.tech/articles/data-privacy/\#creating-role-based-access-control-rbac-using-jwt) Creating Role-Based Access Control (RBAC) Using JWT

As we saw above, JWT claims create powerful levers through which you can create granular access control on Qdrant. Let’s bring it all together and understand how it helps you create Role-Based Access Control (RBAC).

In a typical enterprise application, you will have a segregation of users based on their roles and permissions. These could be:

1. **Admin or Owner:** with full access, and can generate API keys.
2. **Editor:** with read-write access levels to specific collections.
3. **Viewer:** with read-only access to specific collections.
4. **Data Scientist or Analyst:** with read-only access to specific collections.
5. **Developer:** with read-write access to development- or testing-specific collections, but limited access to production data.
6. **Guest:** with limited read-only access to publicly available collections.

In addition, you can create access levels within sections of a collection. In a multi-tenant application, where you have used payload-based partitioning, you can create read-only access for specific user roles for a subset of the collection that belongs to that user.

Your application requirements will eventually help you decide the roles and access levels you should create. For example, in an application managing customer data, you could create additional roles such as:

**Customer Support Representative**: read-write access to customer service-related data but no access to billing information.

**Billing Department**: read-only access to billing data and read-write access to payment records.

**Marketing Analyst**: read-only access to anonymized customer data for analytics.

Each role can be assigned a JWT with claims that specify expiration times, read/write permissions for collections, and validating conditions.

In such an application, an example JWT payload for a customer support representative role could be:

```json
{
  "exp": 1690995200,
  "access": [\
    {\
      "collection": "customer_data",\
      "access": "rw",\
      "payload": {\
        "department": "support"\
      }\
    }\
  ],
  "value_exists": {
    "collection": "departments",
    "matches": [\
      { "key": "department", "value": "support" }\
    ]
  }
}

```

As you can see, by implementing RBAC, you can ensure proper segregation of roles and their privileges, and avoid privacy loopholes in your application.

## [Anchor](https://qdrant.tech/articles/data-privacy/\#qdrant-hybrid-cloud-and-data-sovereignty) Qdrant Hybrid Cloud and Data Sovereignty

Data governance varies by country, especially for global organizations dealing with different regulations on data privacy, security, and access. This often necessitates deploying infrastructure within specific geographical boundaries.

To address these needs, the vector database you choose should support deployment and scaling within your controlled infrastructure. [Qdrant Hybrid Cloud](https://qdrant.tech/documentation/hybrid-cloud/) offers this flexibility, along with features like sharding, replicas, JWT authentication, and monitoring.

Qdrant Hybrid Cloud integrates Kubernetes clusters from various environments—cloud, on-premises, or edge—into a unified managed service. This allows organizations to manage Qdrant databases through the Qdrant Cloud UI while keeping the databases within their infrastructure.

With JWT and RBAC, Qdrant Hybrid Cloud provides a secure, private, and sovereign vector store. Enterprises can scale their AI applications geographically, comply with local laws, and maintain strict data control.

## [Anchor](https://qdrant.tech/articles/data-privacy/\#conclusion) Conclusion

Vector similarity is increasingly becoming the backbone of AI applications that leverage unstructured data. By transforming data into vectors – their numerical representations – organizations can build powerful applications that harness semantic search, ranging from better recommendation systems to algorithms that help with personalization, or powerful customer support chatbots.

However, to fully leverage the power of AI in production, organizations need to choose a vector database that offers strong privacy and security features, while also helping them adhere to local laws and regulations.

Qdrant provides exceptional efficiency and performance, along with the capability to implement granular access control to data, Role-Based Access Control (RBAC), and the ability to build a fully data-sovereign architecture.

Interested in mastering vector search security and deployment strategies? [Join our Discord community](https://discord.gg/qdrant) to explore more advanced search strategies, connect with other developers and researchers in the industry, and stay updated on the latest innovations!

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/data-privacy.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/data-privacy.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-114-lllmstxt|>
## changelog
- [Documentation](https://qdrant.tech/documentation/)
- [Private cloud](https://qdrant.tech/documentation/private-cloud/)
- Changelog