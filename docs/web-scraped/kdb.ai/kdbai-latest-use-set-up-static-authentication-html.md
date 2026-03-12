# Source: https://code.kx.com/kdbai/latest/use/set-up-static-authentication.html

Title: Static Authentication in KDB.AI - KDB.AI Documentation

URL Source: https://code.kx.com/kdbai/latest/use/set-up-static-authentication.html

Markdown Content:
Static Authentication in KDB.AI - KDB.AI Documentation
===============
- [x] - [x] 

[Skip to content](https://code.kx.com/kdbai/latest/use/set-up-static-authentication.html#static-authentication-in-kdbai)

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

 Static Authentication in KDB.AI 

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
    *   [Authentication and Authorization (New)](https://code.kx.com/kdbai/latest/reference/authentication.html)
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
        *   - [x]  Static Authentication  [Static Authentication](https://code.kx.com/kdbai/latest/use/set-up-static-authentication.html) On this page  
            *   [Static Authentication in KDB.AI](https://code.kx.com/kdbai/latest/use/set-up-static-authentication.html#static-authentication-in-kdbai)
            *   [Static authentication with environment variable](https://code.kx.com/kdbai/latest/use/set-up-static-authentication.html#static-authentication-with-environment-variable)
            *   [Static authentication with password file](https://code.kx.com/kdbai/latest/use/set-up-static-authentication.html#static-authentication-with-password-file)
            *   [Python Client version](https://code.kx.com/kdbai/latest/use/set-up-static-authentication.html#python-client-version)
            *   [Docker examples](https://code.kx.com/kdbai/latest/use/set-up-static-authentication.html#docker-examples)
                *   [Authentication from environment variable](https://code.kx.com/kdbai/latest/use/set-up-static-authentication.html#authentication-from-environment-variable)
                *   [Authentication from file](https://code.kx.com/kdbai/latest/use/set-up-static-authentication.html#authentication-from-file)
                *   [No authentication specified](https://code.kx.com/kdbai/latest/use/set-up-static-authentication.html#no-authentication-specified)

            *   [Examples](https://code.kx.com/kdbai/latest/use/set-up-static-authentication.html#examples)
                *   [HTTP authentication using curl](https://code.kx.com/kdbai/latest/use/set-up-static-authentication.html#http-authentication-using-curl)
                *   [Authentication using Python Client](https://code.kx.com/kdbai/latest/use/set-up-static-authentication.html#authentication-using-python-client)

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
*   [Static Authentication in KDB.AI](https://code.kx.com/kdbai/latest/use/set-up-static-authentication.html#static-authentication-in-kdbai)
*   [Static authentication with environment variable](https://code.kx.com/kdbai/latest/use/set-up-static-authentication.html#static-authentication-with-environment-variable)
*   [Static authentication with password file](https://code.kx.com/kdbai/latest/use/set-up-static-authentication.html#static-authentication-with-password-file)
*   [Python Client version](https://code.kx.com/kdbai/latest/use/set-up-static-authentication.html#python-client-version)
*   [Docker examples](https://code.kx.com/kdbai/latest/use/set-up-static-authentication.html#docker-examples)
    *   [Authentication from environment variable](https://code.kx.com/kdbai/latest/use/set-up-static-authentication.html#authentication-from-environment-variable)
    *   [Authentication from file](https://code.kx.com/kdbai/latest/use/set-up-static-authentication.html#authentication-from-file)
    *   [No authentication specified](https://code.kx.com/kdbai/latest/use/set-up-static-authentication.html#no-authentication-specified)

*   [Examples](https://code.kx.com/kdbai/latest/use/set-up-static-authentication.html#examples)
    *   [HTTP authentication using curl](https://code.kx.com/kdbai/latest/use/set-up-static-authentication.html#http-authentication-using-curl)
    *   [Authentication using Python Client](https://code.kx.com/kdbai/latest/use/set-up-static-authentication.html#authentication-using-python-client)

Static Authentication
=====================

Static Authentication in KDB.AI
-------------------------------

_This page explains how to set up and use static authentication in KDB.AI. It includes details on environment variables, Docker examples, and Python client usage._

If you're new to this topic, start with [Learn: Authentication](https://code.kx.com/kdbai/latest/reference/authentication.html).

KDB.AI supports static authentication, allowing access management for different users.

With static authentication, the server verifies the client password with a static key provided to the server. You can supply the static key as an environment variable or as a mounted file path (for example, using a Kubernetes secret). The following variables enable static authentication:

| **Variable** | **Purpose** | **Supported values** | **Mandatory** | **Default** |
| --- | --- | --- | --- | --- |
| `AUTH_TYPE` | Authentication type | static | Yes | None |
| `AUTH_PASSWORD` | Authentication password | any string | No (password file can be mounted instead) | None |

Static authentication with environment variable
-----------------------------------------------

To configure static authentication, add the following environment variables to your Docker/Kubernetes configuration:

```bash
AUTH_TYPE=static
AUTH_PASSWORD="secret" # if static API key is passed using env var else no need to define this variable
```

Static authentication with password file
----------------------------------------

To use a mounted secret file, mount it at the path `/opt/kx/secret/auth_pwd`. A mounted secret file always takes precedence over the `AUTH_PASSWORD` environment variable.

Python Client version
---------------------

To maintain compatibility with the server, use `kdbai-client>=1.6.0`:

*   `kdbai-client==1.6.0` supports `TCP/QIPC` connection with authentication.

*   `kdbai-client>=1.7.0` supports `TCP/QIPC` and `HTTP` connections with authentication.

*   `kdbai-client<1.6.0` is not compatible.

Docker examples
---------------

### Authentication from environment variable

Use the `AUTH_PASSWORD` variable:

```bash
docker run -it --rm -p 8081:8081 -p 8082:8082 \
        -e KDB_LICENSE_B64="$KDB_LICENSE_B64" \
        -e AUTH_TYPE=STATIC \
        -e AUTH_PASSWORD="secret" \
        -v "$PWD/vdbdata":/tmp/kx/data \
         portal.dl.kx.com/kdbai-db:1.7.0
```

### Authentication from file

Create a password file and mount it into the container:

```bash
echo "secret" > /tmp/auth_pwd
docker run -it --rm -p 8081:8081 -p 8082:8082 \
        -e KDB_LICENSE_B64="$KDB_LICENSE_B64" \
        -e AUTH_TYPE=STATIC \
        -v /tmp/auth_pwd:/opt/kx/secret/auth_pwd \
        -v "$PWD/vdbdata":/tmp/kx/data \
         portal.dl.kx.com/kdbai-db:1.7.0
```

### No authentication specified

Run as normal without specifying any authentication variables:

```bash
docker run -it --rm -p 8081:8081 -p 8082:8082 \
        -e KDB_LICENSE_B64="$KDB_LICENSE_B64" \
        -v "$PWD/vdbdata":/tmp/kx/data \
         portal.dl.kx.com/kdbai-db:1.7.0
```

Examples
--------

### HTTP authentication using curl

```bash
curl http://localhost:8081/api/v2/version
{"message":"You are not authorized to access this resource."}

curl -u user:password-file http://localhost:8081/api/v2/version
{"serverVersion":"1.7.0","clientMinVersion":"1.7.0","clientMaxVersion":"latest"}
```

### Authentication using Python Client

```bash
import kdbai_client as kdbai
import os
PASSWORD = os.environ.get("auth_pwd")
try:
    session = kdbai.Session(endpoint="http://localhost:8082", options={"username":"user","password":"pass"})
    print(f"Success, connected to server with qipc")
except kdbai.KDBAIException as e:
    print(f"Failed to connect with password={PASSWORD} --> {e}")
EOF
```

[Previous Rerank](https://code.kx.com/kdbai/latest/use/rerank.html)[Next OAuth 2.0](https://code.kx.com/kdbai/latest/use/set-up-oauth2-authentication.html)

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
