# Source: https://docs.ox.security/ox-integrations/3rd-party-integrations/dynamic-app-security.md

# Dynamic App Security

Dynamic application security testing (DAST) scanners probe running web apps and APIs to find runtime risks, such as SQL injection or cross-site scripting.

OX connects to third-party DAST tools to import their findings, enrich them with OX context, and present everything in one place alongside SAST, SCA, cloud, and infrastructure data.

OX does not run scans in your DAST tool. Each connector reads findings through the vendor’s API, then maps them to your applications and workflows in OX so you can triage, prioritize, and report consistently.

Where you will see DAST data in OX:

* **Active issues:** Filter by **Source tool** to focus on a specific vendor.
* **Issue details:** Tabs include Summary, URL, Request, Response, Compliance, and CWE, and OX context, such as attack path.
* **Applications:** Imported applications appear in the Applications list and dashboards.

The following DAST connectors are supported:

* [Invicti](https://docs.ox.security/ox-integrations/3rd-party-integrations/dynamic-app-security/invicti)
* [Bright Security](https://docs.ox.security/ox-integrations/3rd-party-integrations/dynamic-app-security/bright)
* [CyCognito](https://docs.ox.security/ox-integrations/3rd-party-integrations/dynamic-app-security/cycognito)
* [Bitsight](https://docs.ox.security/ox-integrations/3rd-party-integrations/dynamic-app-security/bitsight)
* [Applause](https://docs.ox.security/ox-integrations/3rd-party-integrations/dynamic-app-security/applause)

## How data from DAST connectors is used by OX

When a DAST connector is active, issues from connectors appear in the Active Issues page, under the DAST Source Tool.

Severity factors in these issues are displayed only for issues that include CVEs. This means that if an issue pulled from the connector has an associated CVE, OX will show its severity level. However, not all DAST issues include CVEs, so severity scoring will only be available for those that do.

This distinction helps users quickly assess which issues are tied to known vulnerabilities and prioritize accordingly, but it also means that some issues may appear without severity factors if they lack a CVE reference.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-6a5abb7abf8b5458ab31837f745358d46b052e32%2FDAST%20issues.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

Each issue includes the following info received from a DAST connector:

* The attacked URL, or a group of URLs; all URLs that triggered this issue appear under the same issue.
* The HTTP request that triggered the issue.
* The HTTP response returned by the application.
* Issue severity as reported by the connector.
* CWE identifiers, if provided.
* Compliance-related tags, if provided.
* Other metadata specific to the connector.
