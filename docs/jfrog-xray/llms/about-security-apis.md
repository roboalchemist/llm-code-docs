# Source: https://docs.jfrog.com/security/reference/about-security-apis.md

# About Security APIs

## JFrog Security API Reference

Welcome to the new JFrog Security API help center. We’ve redesigned this experience to be more developer-centric, providing a more intuitive way to integrate security into your automated workflows.

You can use the **Search** bar at the top of the page to find specific endpoints by name, method, or functionality.

### Documentation Structure

Our APIs are organized to mirror your security lifecycle, covering **JFrog Xray**, **Advanced Security**, and **Curation**:

* **Vulnerability & License Scanning:** Programmatically trigger scans, retrieve security reports, and export SBOMs (Software Bill of Materials).
* **Policies & Watches:** Automate the enforcement of security gates and notification rules across your repositories and builds.
* **Advanced Security (JAS):** Access endpoints for Secrets Detection, Contextual Analysis, and Infrastructure-as-Code (IaC) scanning.
* **Curation:** Manage the "OSS Firewall" to programmatically block or allow packages based on organizational risk profiles.
* **System & Configuration:** Handle administrative tasks like indexing, component metadata, and system health checks.

### Key Features

* **Try It Out:** Use the interactive API explorer on each page to send requests directly from your browser (requires a valid JFrog URL and credentials).
* **Code Samples:** Copy-paste ready-to-use snippets in various languages (cURL, Python, Node.js, etc.) located in the right-hand panel of each endpoint.
* **Detailed Schemas:** Expand response objects to view data types, constraints, and descriptions for every field.

### Authentication

Most Security APIs require an **Access Token** or **Identity Token** for authentication.