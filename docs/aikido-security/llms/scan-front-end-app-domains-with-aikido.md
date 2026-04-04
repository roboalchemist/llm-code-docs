# Source: https://help.aikido.dev/dast-surface-monitoring/front-end-scanning/scan-front-end-app-domains-with-aikido.md

# Scan Front-End App Domains with Aikido

Aikido's surface monitoring watches your app's public attack surface by probing your domain names for weaknesses.

### What is Surface Monitoring Scanning? <a href="#what-is-surface-monitoring-scanning" id="what-is-surface-monitoring-scanning"></a>

Surface monitoring, sometimes better known as Dynamic Application Security Testing (DAST) inspects all the externally-facing components of your software, including the application programming interfaces (APIs), web pages, data transfer protocols, libraries and external resources used and other user-facing features.

### Overview of checks performed <a href="#overview-of-checks-performed" id="overview-of-checks-performed"></a>

To see the checks performed by the Surface Monitoring Scanner, visit our [checks overview page](https://app.aikido.dev/domains/checks). Here, you'll find a detailed list of all the checks performed during the scan. Aikido will only perform safe, non-destructive automated test (eg no automated SQL injection attempts,..).

### Overview of libraries detected <a href="#overview-of-libraries-detected" id="overview-of-libraries-detected"></a>

To see a list of all libraries detected by Surface Monitoring Scanner visit the **Resources** tab for a specific domain. You will find the library, version, date and time of detection and url for each detected resource. When CVE's are found for actively used resources, they will be added to your feed like other vulnerabilities.

### Add a domain to be scanned with Aikido <a href="#add-a-domain-to-be-scanned-with-aikido" id="add-a-domain-to-be-scanned-with-aikido"></a>

**Step 1:** Navigate to the [Domains Overview Page](https://app.aikido.dev/domains) or [Domains Settings](https://app.aikido.dev/settings/domains) and select **Front-End App**

![Application type selection screen for security testing of various app types and APIs.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FvN5HoHKHQGJG4Vp9kd4r%2FScreenshot%202025-10-28%20at%2018.16.48.png?alt=media\&token=b81f26a5-f483-4519-bcc6-96d9d06beaed)

**Step 2:** Fill in the service URL for the repositories which have public-facing domains by filling out the configuration form. You can specify full paths.

**Step 3: Optional**: link your domain to a repository or container

**Step 4: Optional:** set the sensitivity of the data

![Form to add domain details, link assets, and classify data sensitivity for issue scoring.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FVMDWK7WrdXUSuFRUl8X0%2FScreenshot%202025-10-28%20at%2018.17.30.png?alt=media\&token=e7af0626-7673-411c-b34b-eb7c227542ac)
