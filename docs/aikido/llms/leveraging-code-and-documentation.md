# Source: https://help.aikido.dev/pentests/leveraging-code-and-documentation.md

# Leveraging Code and Documentation

## TL;DR

Black-box testing is blind. White-box testing is precise. Connect your repositories to give the system full visibility, then use the context box and file uploads to fill in the gaps.

## Repositories

{% hint style="warning" %}
**Unlock White-Box Testing**\
Without source code, the system scans blind. Connecting your repositories upgrades the test from external guessing to internal verification.
{% endhint %}

Connecting your repositories is the single most impactful step you can take. Instead of just poking at endpoints from the outside, the system analyzes the actual source code to understand how the application processes data.

* **Why it matters:** It finds deep-logic vulnerabilities that external scanning simply cannot see.
* **What to select:** Include all repos involved in the scope (Frontend, Backend, IaC).
  * You can connect a maximum of 4 repositories per pentest, this limit ensures the pentest is optimally configured for a single application. Overloading the scope with unrelated services can dilute the depth of the analysis.
  * **Need more?** If your application relies on more than 4 repositories, reach out to our support team and we can increase the limit for your specific use case.
* **The result:** The system maps your routes and logic directly from the source. It doesn't need to guess your API structure, it reads it.

## Upload Data

Files cover the structural elements that the code doesn't reveal.

* **OpenAPI Specs (JSON / YAML):** Gives the system a complete map of the API surface. This ensures it interacts with and attacks every endpoint, not just the ones it can crawl.
* **Documentation (README.md / Specs):** Provides the system with deep context on the target and its threat model, helping it distinguish between intended design and actual vulnerabilities.
* **User Role Definitions:** A list of supported roles (e.g., Admin vs. Viewer) and their specific constraints. The system uses this to strictly test what specific users *should not* be able to access.
* **Workflows & High-Level Structure:** Descriptions of complex flows (like "Checkout" or "Onboarding") and the general app structure.
* **Previous Pentest Reports (PDF):** Feeds the system historical data. It uses this to validate past fixes (regression testing) and hunt for variations of those specific bugs elsewhere in the code.

{% hint style="info" %}

#### Data persistance

We persist your data encrypted for two pragmatic reasons:

1\. Continuous Pentesting & Repeatability Security isn't a one-off. When you trigger a re-scan or a continuous test, we use these attack resources to ensure the test is consistent. You don't want to re-configure the scope every time a scan is triggered.

2\. Audit & Legal Defense For SOC2 or ISO 27001, you need to prove *how* you tested. We maintain this data to create a defensible audit trail. It allows you to justify exactly what was in scope, and prove that the test was done with full white-box visibility, not just a superficial scan.
{% endhint %}

## Additional Context

Code shows syntax, but it doesn't always show intent. Use this text box for anything valuable that isn't explicitly defined in the repo or the docs.

* **Business Logic:** Explain rules that might look like bugs but aren't (e.g., "Admins are allowed to see all user data").
* **Architecture Quirks:** "We use a custom implementation of OAuth" or "The database is read-only for this service."
* **Known Gaps:** "The API documentation in the repo is slightly outdated for the payment service."
