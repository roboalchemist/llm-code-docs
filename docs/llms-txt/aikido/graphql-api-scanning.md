# Source: https://help.aikido.dev/dast-surface-monitoring/api-scanning/graphql-api-scanning.md

# GraphQL API Scanning

Aikido can scan your GraphQL API endpoints to uncover endpoint vulnerabilities specifically related to GraphQL. One of the methods we use is API fuzzing, which essentially includes spamming dangerous payloads to each field in your API.

> NEVER do this setup on a production environment, but always on staging to avoid potential downtime or interference.

### Main Use Cases <a href="#main-use-cases" id="main-use-cases"></a>

You can see all checks in the [Aikido app here](https://app.aikido.dev/domains/checks?scanner=graphql).

### Setting up GraphQL API Scanning <a href="#setting-up-graphql-api-scanning" id="setting-up-graphql-api-scanning"></a>

**Step 1:** Click **Add Domain** in the [Domain Overview ](https://app.aikido.dev/domains)and select **GraphQL** scanning

![Application type selection screen for security testing of web and API applications.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-4f0766de37209ca13525fd0562d6563e2b089060%2Fgraphql-api-scanning_e3b66d94-162f-414b-bd36-87a4641556de.png?alt=media)

**Step 2.** Enter the domain name of your **staging environment**. Ensure this is the base URL for your GraphQL APIs (e.g., `https://example.io/graphql`)

![Input field for entering a GraphQL endpoint domain name.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-69a562d073722c8409347cb77ab936d4da516880%2Fgraphql-api-scanning_7d9ed9dd-97d3-4063-8a12-d15534fa4430.png?alt=media)

**Step 3:** Click save, Aikido will now scan your GraphQL API.

**Step 4. Authorization:** Note that you can also add authorization information if this is required to talk to your API. You can do this by clicking the triple dots action menu on the domain, and then '**Authenticate Domain**'

![Domain action menu offering scan, configuration, authentication, and delete options.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-3f9ee407d58f08ed07d482a471b34990e0e663bd%2Fgraphql-api-scanning_93e28303-bdd8-43f4-ad11-ed62a73d5cc7.png?alt=media)

This will trigger the modal where you can fill in the authentication details.

![Domain authentication setup form for enabling form-based login credentials.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-62e066c94ef2f94ad560ac511f85dda13743ed97%2Fgraphql-api-scanning_fd6fe4c4-64a7-4f4d-a031-118eafd83dc0.png?alt=media)

### Identifying Aikido traffic

All requests coming from Aikido REST and GraphQL scans will have:

* the `User-Agent` set to `aikido-scan-agent/1.0`&#x20;
* the following header `aikido-api-test` set to value `1` in the request &#x20;
* [will come from the IP's documented here](https://help.aikido.dev/dast-surface-monitoring/allowing-ip-addresses-for-dast-surface-monitoring)
