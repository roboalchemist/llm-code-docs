# Source: https://help.aikido.dev/dast-surface-monitoring/api-scanning/rest-api-scanning.md

# REST API & Web App Scanning

Aikido can scan your REST API and Web App endpoints to uncover critical endpoint vulnerabilities, such as SQL injection or path traversal. Aikido uses API fuzzing, which essentially includes spamming dangerous payloads to each field in your API.

> NEVER do this setup on a production environment, always on staging to avoid potential downtime.

### Main Use Cases <a href="#main-use-cases" id="main-use-cases"></a>

**Critical Vulnerability Detection**:

* SQL injection
* NoSQL injection
* Path traversal
* Shell injection

You can see all checks in the [Aikido app here](https://app.aikido.dev/domains/checks?scanner=rest).

### Setting up REST API Scanning <a href="#setting-up-rest-api-scanning" id="setting-up-rest-api-scanning"></a>

**Step 1:** Click **Add Domain** in the [Domain Overview ](https://app.aikido.dev/domains)and **select REST API**

![Application type selection screen for security testing of different app architectures.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F7YE7dsmtmtWzilpZ4NTH%2FScreenshot%202025-07-02%20at%2016.31.48.png?alt=media\&token=8bf5c637-9c56-4218-8372-59c353164484)

**Step 2.** Enter the domain name of your **staging environment**. Ensure this is the base URL for your REST APIs (e.g., `https://example.io/api`)

![API domain name input field for application configuration.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-d51a43b4e1e15ece54efb4d0999371895723ad68%2Frest-api-scanning_ba74a958-2462-4a6c-88b5-40f2fe05d53d.png?alt=media)

**Step 3:** Add your OpenAPI specification using one of these options:

* [**Connect to Zen App (recommended)**](https://help.aikido.dev/zen-firewall): Integrate with Zen to automatically discover and update API endpoints for continuous scanning. More info about Zen [can be found here](https://help.aikido.dev/section/zen-by-aikido/sgIt4HRxlrFr). No manual work or maintenance needed!
* [**Generate via Aikido AI (in beta)**](https://help.aikido.dev/dast-surface-monitoring/api-scanning/autogenerate-openapi-via-aikido-ai-code2swagger)**:** Using your codebase Aikido will generate an OpenAPI spec. No manual work is needed. Regular rescans keep everything current.
* **Fetch from URL:** Provide a URL that has the latest version of your OpenAPI spec. Aikido will fetch the spec before each scan.
* **Manual Upload**: Upload a OpenAPI file to define your API endpoints. You will be required to manually update and upload your spec each time new API endpoints are added or changed.

![Add or upload an OpenAPI spec to scan for security risks; staging use only.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F1V7IUiOugY7x15JWKoW7%2FScreenshot%202025-07-02%20at%2016.22.50.png?alt=media\&token=f40c47fc-f58e-4d9a-82c7-cb9d8f47cc9a)

**Step 4:** Add authorization information to your API to make sure Aikido can access endpoints that require login. You can do this by clicking the triple dots action menu on the domain, and then '**Authenticate Domain**'

![Domain action menu with options: Start scan, Edit, Authenticate, and Delete domain.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-3f9ee407d58f08ed07d482a471b34990e0e663bd%2Frest-api-scanning_b352fba8-9a02-4c8d-84e7-60b6d94e5b9d.png?alt=media)

This will trigger the modal where you can fill in the authentication details. Multiple authentication types are available: **Login via Form** and **Custom Headers** support

![Domain authentication setup form with input fields for API URL, email, and password.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-62e066c94ef2f94ad560ac511f85dda13743ed97%2Frest-api-scanning_42a1f3d3-08d5-4a6b-a142-aeaaeda72705.png?alt=media)

### Identifying Aikido traffic

All requests coming from Aikido REST and GraphQL scans will have:

* the `User-Agent` set to `aikido-scan-agent/1.0`&#x20;
* the following header `aikido-api-test` set to value `1` in the request &#x20;
* [will come from the IP's documented here](https://help.aikido.dev/dast-surface-monitoring/allowing-ip-addresses-for-dast-surface-monitoring)
