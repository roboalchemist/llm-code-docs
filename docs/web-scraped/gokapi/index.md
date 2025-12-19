# Source: https://gokapi.readthedocs.io/en/stable/index.html

[]

# Gokapi[](#gokapi "Link to this heading")

Gokapi is a lightweight server to share files, which expire after a set amount of downloads or days. It is similar to the discontinued Firefox Send, with the difference that only the admin is allowed to upload files.

This enables companies or individuals to share their files very easily and having them removed afterwards, therefore saving disk space and having control over who downloads the file from the server.

Identical files will be deduplicated. An API is available to interact with Gokapi. AWS S3 compatible storage can be used instead of local storage. Customization is very easy with HTML/CSS knowledge.

## Contents[](#contents "Link to this heading")

-   [Setup](setup.html)
    -   [Installation](setup.html#installation)
    -   [First Start](setup.html#first-start)
    -   [Changing Configuration](setup.html#changing-configuration)
    -   [Reverse Proxy](setup.html#reverse-proxy)
    -   [Installing a systemd service](setup.html#installing-a-systemd-service)
-   [Usage](usage.html)
    -   [Admin Menu](usage.html#admin-menu)
    -   [API Menu](usage.html#api-menu)
-   [Updating Gokapi](update.html)
    -   [Docker](update.html#docker)
    -   [Native deployment](update.html#native-deployment)
-   [Advanced usage](advanced.html)
    -   [Environment variables](advanced.html#environment-variables)
    -   [Databases](advanced.html#databases)
    -   [CLI Tool](advanced.html#cli-tool)
    -   [API](advanced.html#api)
    -   [Chunk Sizes / Considerations for servers with limited or high amount of RAM](advanced.html#chunk-sizes-considerations-for-servers-with-limited-or-high-amount-of-ram)
    -   [Automatic Deployment](advanced.html#automatic-deployment)
    -   [Customising](advanced.html#customising)
-   [Examples](examples.html)
    -   [Nginx Configuration](examples.html#nginx-configuration)
    -   [OpenID Connect Configuration](examples.html#openid-connect-configuration)
-   [Contributions](contributions.html)
-   [Changelog](changelog.html)
    -   [Overview of all changes](changelog.html#overview-of-all-changes)