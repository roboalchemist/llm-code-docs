# Source: https://code.kx.com/kdbai/latest/reference/authentication.html

Title: Authentication and Authorization in KDB.AI

URL Source: https://code.kx.com/kdbai/latest/reference/authentication.html

Markdown Content:
Authentication and Authorization in KDB.AI - KDB.AI Documentation
===============
- [x] - [x] 

[Skip to content](https://code.kx.com/kdbai/latest/reference/authentication.html#authentication-and-authorization-in-kdbai)

[](https://code.kx.com/kdbai/latest/index.html "KDB.AI Homepage")

 KDB.AI Documentation 

1.9.0
*   [1.9.0](https://code.kx.com/kdbai/1.9.0/)
*   [1.8.0](https://code.kx.com/kdbai/1.8.0/)
*   [1.7.0](https://code.kx.com/kdbai/1.7.0/)
*   [1.6.0](https://code.kx.com/kdbai/1.6.0/)
*   [1.5.0](https://code.kx.com/kdbai/1.5.0/)
*   [1.4.0](https://code.kx.com/kdbai/1.4.0/)
*   [1.3.0](https://code.kx.com/kdbai/1.3.0/)
*   [1.2.0](https://code.kx.com/kdbai/1.2.0/)
*   [1.1.0](https://code.kx.com/kdbai/1.1.0/)
*   [1.0.0](https://code.kx.com/kdbai/1.0.0/)

 Authentication and Authorization in KDB.AI 

Type to start searching

*   [Home](https://code.kx.com/kdbai/latest/index.html)
*   [Learn](https://code.kx.com/kdbai/latest/reference/authentication.html)
*   [How To](https://code.kx.com/kdbai/latest/use/database.html)
*   [API Reference](https://code.kx.com/kdbai/latest/reference/python-client.html)
*   [Integrations](https://code.kx.com/kdbai/latest/integrations/allintegrations.html)
*   [Examples](https://github.com/KxSystems/kdbai-samples/)
*   [Releases](https://code.kx.com/kdbai/latest/releaseNotes/release-notes-latest.html)
*   [Help and Support](https://code.kx.com/kdbai/latest/support/known-issues.html)

[](https://code.kx.com/kdbai/latest/ "KDB.AI Documentation") KDB.AI Documentation  
*   - [x]  Home   Home  
    *   [About KDB.AI](https://code.kx.com/kdbai/latest/index.html)
    *   - [x]  Get Started   Get Started  
        *   [Prerequisites](https://code.kx.com/kdbai/latest/gettingStarted/pre-requisites.html)
        *   [KDB.AI Server Setup](https://code.kx.com/kdbai/latest/gettingStarted/kdb-ai-server-setup.html)
        *   [Quick Start](https://code.kx.com/kdbai/latest/gettingStarted/quickstart.html)
        *   [Versioning and Upgrade](https://code.kx.com/kdbai/latest/versioning.html)

*   - [x]  Learn   Learn  
    *   - [x]  Authentication and Authorization (New)  [Authentication and Authorization (New)](https://code.kx.com/kdbai/latest/reference/authentication.html) On this page  
        *   [Static authentication](https://code.kx.com/kdbai/latest/reference/authentication.html#static-authentication)
            *   [Architecture](https://code.kx.com/kdbai/latest/reference/authentication.html#architecture)
            *   [Benefits](https://code.kx.com/kdbai/latest/reference/authentication.html#benefits)
            *   [When to use](https://code.kx.com/kdbai/latest/reference/authentication.html#when-to-use)

        *   [OAuth 2.0 authentication and authorization](https://code.kx.com/kdbai/latest/reference/authentication.html#oauth-20-authentication-and-authorization)
            *   [Architecture](https://code.kx.com/kdbai/latest/reference/authentication.html#architecture_1)
            *   [Benefits](https://code.kx.com/kdbai/latest/reference/authentication.html#benefits_1)
            *   [When to use](https://code.kx.com/kdbai/latest/reference/authentication.html#when-to-use_1)

        *   [Comparison](https://code.kx.com/kdbai/latest/reference/authentication.html#comparison)
        *   [Summary](https://code.kx.com/kdbai/latest/reference/authentication.html#summary)
        *   [Next steps](https://code.kx.com/kdbai/latest/reference/authentication.html#next-steps)

    *   [Database](https://code.kx.com/kdbai/latest/reference/database.html)
    *   [Table](https://code.kx.com/kdbai/latest/reference/table.html)
    *   [Data Types](https://code.kx.com/kdbai/latest/reference/supported-types.html)
    *   [Index](https://code.kx.com/kdbai/latest/reference/index.html)
    *   [Similarity Metrics](https://code.kx.com/kdbai/latest/reference/metrics.html)
    *   [Hybrid Search](https://code.kx.com/kdbai/latest/reference/hybrid.html)
    *   [Transformed TSS](https://code.kx.com/kdbai/latest/reference/transformed-tss.html)
    *   [Non-Transformed TSS](https://code.kx.com/kdbai/latest/reference/non-transformed-tss.html)
    *   [Dynamic Time Warping](https://code.kx.com/kdbai/latest/reference/dynamic-time-warping.html)
    *   [Filters](https://code.kx.com/kdbai/latest/reference/filters.html)
    *   [Partitioning](https://code.kx.com/kdbai/latest/reference/partition.html)
    *   [Reranking](https://code.kx.com/kdbai/latest/reference/reranking.html)
    *   [Parallel Processing](https://code.kx.com/kdbai/latest/reference/multithreading.html)
    *   [Learning Hub](https://kdb.ai/learning-hub)

*   - [x]  How To   How To  
    *   [Use Databases](https://code.kx.com/kdbai/latest/use/database.html)
    *   [Manage Tables](https://code.kx.com/kdbai/latest/use/manage-tables.html)
    *   [Ingest Data](https://code.kx.com/kdbai/latest/use/ingestion.html)
    *   [Query Data](https://code.kx.com/kdbai/latest/use/query.html)
    *   [Delete Data](https://code.kx.com/kdbai/latest/use/delete-data.html)
    *   [Use Indexes](https://code.kx.com/kdbai/latest/use/supported-indexes.html)
    *   - [x]  Search   Search  
        *   [Similarity Search](https://code.kx.com/kdbai/latest/use/search.html)
        *   [Hybrid Search](https://code.kx.com/kdbai/latest/use/hybrid-search.html)
        *   [Transformed TSS](https://code.kx.com/kdbai/latest/use/transformed-tss.html)
        *   [Non-Transformed TSS](https://code.kx.com/kdbai/latest/use/non-transformed-tss.html)
        *   [Dynamic Time Warping (DTW)](https://code.kx.com/kdbai/latest/use/dynamic-time-warping-dtw.html)

    *   [Customize Filters](https://code.kx.com/kdbai/latest/use/filter.html)
    *   [Partition](https://code.kx.com/kdbai/latest/use/partitioning.html)
    *   [Rerank](https://code.kx.com/kdbai/latest/use/rerank.html)
    *   - [x]  Set Up Authentication   Set Up Authentication  
        *   [Static Authentication](https://code.kx.com/kdbai/latest/use/set-up-static-authentication.html)
        *   [OAuth 2.0](https://code.kx.com/kdbai/latest/use/set-up-oauth2-authentication.html)

    *   [Get System Usage Info](https://code.kx.com/kdbai/latest/use/get-system-usage-info.html)

*   - [x]  API Reference   API Reference  
    *   [Python API](https://code.kx.com/kdbai/latest/reference/python-client.html)
    *   [q API](https://code.kx.com/kdbai/latest/reference/qAPI.html)
    *   [REST API](https://code.kx.com/kdbai/latest/reference/rest-api.html)
    *   [Naming and Reserved Words](https://code.kx.com/kdbai/latest/reference/naming-convention-reserved-words.html)
    *   [Glossary](https://code.kx.com/kdbai/latest/reference/glossary.html)

*   - [x]  Integrations   Integrations  
    *   [All integrations](https://code.kx.com/kdbai/latest/integrations/allintegrations.html)
    *   [kdb+](https://code.kx.com/kdbai/latest/integrations/kdb.html)
    *   [OpenAI](https://code.kx.com/kdbai/latest/integrations/openai.html)
    *   [LangChain](https://code.kx.com/kdbai/latest/integrations/langchain.html)
    *   [LlamaIndex](https://code.kx.com/kdbai/latest/integrations/llamaindex.html)
    *   [Vector IO](https://code.kx.com/kdbai/latest/integrations/vector-io.html)
    *   [Azure AI](https://code.kx.com/kdbai/latest/integrations/azureml.html)
    *   [Hugging Face](https://code.kx.com/kdbai/latest/integrations/hugging-face.html)
    *   [Unstructured](https://code.kx.com/kdbai/latest/integrations/unstructured-io.html)
    *   [Cohere](https://code.kx.com/kdbai/latest/use/rerank.html)
    *   [Jina AI](https://code.kx.com/kdbai/latest/use/rerank.html)
    *   [Voyage AI](https://code.kx.com/kdbai/latest/use/rerank.html)
    *   [Model Context Protocol (MCP) Server](https://code.kx.com/kdbai/latest/integrations/mcp-server.html)

*   - [x]  Examples   Examples  
    *   [GitHub Samples](https://github.com/KxSystems/kdbai-samples/)

*   - [x]  Releases   Releases  
    *   [Latest](https://code.kx.com/kdbai/latest/releaseNotes/release-notes-latest.html)
    *   [Previous](https://code.kx.com/kdbai/latest/releaseNotes/release-notes-previous.html)

*   - [x]  Help and Support   Help and Support  
    *   [Known Issues](https://code.kx.com/kdbai/latest/support/known-issues.html)
    *   [FAQs and Troubleshooting](https://code.kx.com/kdbai/latest/support/FAQ-troubleshooting.html)
    *   [Slack Community](http://kx.com/slack)

 On this page  
*   [Static authentication](https://code.kx.com/kdbai/latest/reference/authentication.html#static-authentication)
    *   [Architecture](https://code.kx.com/kdbai/latest/reference/authentication.html#architecture)
    *   [Benefits](https://code.kx.com/kdbai/latest/reference/authentication.html#benefits)
    *   [When to use](https://code.kx.com/kdbai/latest/reference/authentication.html#when-to-use)

*   [OAuth 2.0 authentication and authorization](https://code.kx.com/kdbai/latest/reference/authentication.html#oauth-20-authentication-and-authorization)
    *   [Architecture](https://code.kx.com/kdbai/latest/reference/authentication.html#architecture_1)
    *   [Benefits](https://code.kx.com/kdbai/latest/reference/authentication.html#benefits_1)
    *   [When to use](https://code.kx.com/kdbai/latest/reference/authentication.html#when-to-use_1)

*   [Comparison](https://code.kx.com/kdbai/latest/reference/authentication.html#comparison)
*   [Summary](https://code.kx.com/kdbai/latest/reference/authentication.html#summary)
*   [Next steps](https://code.kx.com/kdbai/latest/reference/authentication.html#next-steps)

Authentication and Authorization in KDB.AI
==========================================

_This page explains how authentication works in KDB.AI and introduces the two supported mechanisms: static authentication and OAuth 2.0._

If you're already familiar with this topic, you can skip ahead to the [Set Up Static Authentication](https://code.kx.com/kdbai/latest/use/set-up-static-authentication.html) and [OAuth 2.0 Authentication and Authorization](https://code.kx.com/kdbai/latest/use/set-up-oauth2-authentication.html) how-to guides.

Authentication is the first layer of security in a KDB.AI deployment. It determines who is allowed to connect to the system and ensures that only trusted clients can issue queries, ingest data, or administer the platform.

When you enable authentication, every incoming request must include valid credentials. KDB.AI verifies those credentials before allowing the request to proceed. It also supports authorization through internal ACL management.

Different deployments have different security requirements. KDB.AI therefore offers two authentication models, each suited to specific environments:

*   [**Static authentication**](https://code.kx.com/kdbai/latest/reference/authentication.html#static-authentication)
*   [**OAuth 2.0 authentication and authorization**](https://code.kx.com/kdbai/latest/reference/authentication.html#oauth-20-authentication-and-authorization)

The sections below provide an overview of both mechanisms and the scenarios in which each is appropriate.

Static authentication
---------------------

### Architecture

Static authentication uses a single shared password configured on the server. When a client connects, KDB.AI compares the provided password with the configured secret. If the password matches, the request proceeds. KDB.AI does not integrate with an identity provider in this mode and does not evaluate tenants, groups, or ACL grants.

### Benefits

Static authentication keeps the access model straightforward and centralized within the server configuration:

*   **No external dependencies:** does not require an identity provider or network access to external services.
*   **Works for both connection types:** supports TCP/QIPC and HTTP authentication when enabled.
*   **Predictable behavior:** all authenticated clients receive the same level of access.
*   **Low operational overhead:** you configure one secret on the server. There are no JWT claims, issuers, or ACL grants to maintain.

### When to use

Static authentication keeps configuration minimal and centralizes access control in the server itself. We recommend it when:

*   You need a single shared password to control access.
*   All authenticated clients should have the same access level.
*   You do not require tenant separation.
*   You do not require group-based permissions.
*   You do not use an external identity provider.

For setup details, go to the [Set Up Static Authentication in KDB.AI](https://code.kx.com/kdbai/latest/use/set-up-static-authentication.html) how-to guide.

OAuth 2.0 authentication and authorization
------------------------------------------

### Architecture

OAuth 2.0 enables KDB.AI to authenticate users through an external identity provider while enforcing fine-grained authorization through internal ACL grants.

KDB.AI validates the token’s signature and issuer, then extracts the configured tenant and group claims (with claim field names defined by the user) to evaluate ACL grants.

### Benefits

OAuth 2.0 separates authentication (handled by the IdP) from authorization (handled by ACL grants in KDB.AI), allowing structured access control:

*   **Group-based access control:** uses group membership from the JWT to determine permissions.
*   **Fine-grained authorization:** uses ACL grants to control access at the database or table level.
*   **Defined system administrator role:** supports a system administrator role based on configured tenant and group values.

### When to use

OAuth 2.0 allows KDB.AI to rely on the identity provider for user and group management while enforcing authorization through ACL grants. We recommend it when:

*   You need to separate access by namespace such as tenant, org, or team.
*   You need to control permissions by group.
*   You want to grant different levels of access to different teams.
*   You need database-level or table-level access control.
*   You require a defined system administrator role.
*   You already use an identity provider (for example, Keycloak, Entra ID, or Okta).

For configuration and examples, go to the [OAuth 2.0 Authentication and Authorization](https://code.kx.com/kdbai/latest/use/set-up-oauth2-authentication.html) how-to guide.

Comparison
----------

Each authentication method offers different levels of control and operational complexity. The table below summarizes the main differences so you can select the approach that best fits your deployment.

| **Feature** | **Static authentication** | **OAuth 2.0 authentication and authorization** |
| --- | --- | --- |
| External identity provider | No | Yes |
| Credential type | Shared password | JWT access token |
| Identity source | Configured on server | Managed by identity provider |
| Tenant support | No | Yes |
| Group-based access control | No | Yes |
| Fine-grained permissions | No | Yes (through ACL grants) |
| Authorization model | Same access for all authenticated clients | Access based on tenant and group claims |
| System administrator role | No | Yes |
| Operational complexity | Low | Higher (IdP and ACL configuration) |

Summary
-------

Static authentication provides a single shared access boundary: all authenticated clients operate with the same permissions.

OAuth 2.0 authentication separates identity management – handled by the identity provider – from authorization, which is defined through ACL grants in KDB.AI. Access depends on the tenant and group claims present in the token.

Use static authentication when you only need simple access restriction. Choose OAuth 2.0 authentication and authorization when you require structured access control, group‑based permissions, or tenant separation.

Next steps
----------

*   If you prefer a simple, single‑password model, continue to the how-to guide on [Setting up Static Authentication](https://code.kx.com/kdbai/latest/use/set-up-static-authentication.html).
*   If you need tenant separation or fine‑grained permissions, move on to the how-to guide on [OAuth 2.0 Authentication and Authorization](https://code.kx.com/kdbai/latest/use/set-up-oauth2-authentication.html).

[Previous Versioning and Upgrade](https://code.kx.com/kdbai/latest/versioning.html)[Next Database](https://code.kx.com/kdbai/latest/reference/database.html)

 © 2026 KX Systems, Inc. KX, KDB-X, and kdb+ are registered trademarks of KX Systems, Inc., a subsidiary of KX Software Limited. 

 Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

![Image 1](https://id.rlcdn.com/464526.gif)

By clicking “Accept All Cookies”, you agree to the storing of cookies on your device to enhance site navigation, analyze site usage, and assist in our marketing efforts.[Cookies Policy.](https://kx.com/cookie-policy/)

Cookies Settings Reject All Accept All

![Image 2: KX Logo](https://cdn-ukwest.onetrust.com/logos/2e246b76-a09f-455a-b12d-cb0cc60b7d47/36d73287-3cef-4657-ad68-1de87d20bcfb/e5b10d3a-3252-4f3a-8f47-e55d701ecfdf/KX-Logo-Black-500x500.png)

Privacy Preference Center
-------------------------

*   ### Your Privacy 
*   ### Strictly Necessary Cookies 
*   ### Performance Cookies 
*   ### Functional Cookies 
*   ### Targeting Cookies 

#### Your Privacy

When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. 

[More information](https://cookiepedia.co.uk/giving-consent-to-cookies)

#### Strictly Necessary Cookies

Always Active

These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.

#### Performance Cookies

- [x] Performance Cookies 

These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance.

#### Functional Cookies

- [x] Functional Cookies 

These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.

#### Targeting Cookies

- [x] Targeting Cookies 

These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.

### Cookie List

Consent Leg.Interest

- [x] checkbox label label

- [x] checkbox label label

- [x] checkbox label label

Clear

- [x] checkbox label label

Apply Cancel

Confirm My Choices

Allow All

[![Image 3: Powered by Onetrust](https://cdn-ukwest.onetrust.com/logos/static/powered_by_logo.svg)](https://www.onetrust.com/products/cookie-consent/)
