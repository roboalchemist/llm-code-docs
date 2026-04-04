# Source: https://docs.datadoghq.com/security/code_security/iast.md

---
title: Runtime Code Analysis (IAST)
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > Code Security > Runtime Code Analysis (IAST)
---

# Runtime Code Analysis (IAST)

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

Datadog Runtime Code Analysis (IAST) identifies code-level vulnerabilities in your services, using an Interactive Application Security Testing (IAST) approach to find vulnerabilities within your application code based on your Datadog application instrumentation.

IAST enables Datadog to identify vulnerabilities using legitimate application traffic instead of relying on external tests that could require extra configuration or periodic scheduling. It also monitors your code's interactions with other components of your stack, such as libraries and infrastructure, providing an up-to-date view of your attack surface area.

For a list of supported services, see the [Library Compatibility Requirements](https://docs.datadoghq.com/security/code_security/iast/setup/#using-datadog-tracing-libraries). IAST detection rules support the following languages:

| Severity | Detection Rule                        | Code                        | Java  | .NET  | Node.js | Python |
| -------- | ------------------------------------- | --------------------------- | ----- | ----- | ------- | ------ |
| Critical | NoSQL Injection                       | NOSQL_MONGODB_INJECTION     | FALSE | TRUE  | TRUE    | FALSE  |
| Critical | SQL Injection                         | SQL_INJECTION               | TRUE  | TRUE  | TRUE    | TRUE   |
| Critical | Server-Side Request Forgery (SSRF)    | SSRF                        | TRUE  | TRUE  | TRUE    | TRUE   |
| Critical | Code Injection                        | CODE_INJECTION              | FALSE | FALSE | TRUE    | FALSE  |
| Critical | Command Injection                     | COMMAND_INJECTION           | TRUE  | TRUE  | TRUE    | TRUE   |
| High     | LDAP Injection                        | LDAP_INJECTION              | TRUE  | TRUE  | TRUE    | FALSE  |
| High     | Email HTML Injection                  | EMAIL_HTML_INJECTION        | TRUE  | TRUE  | TRUE    | FALSE  |
| High     | Hardcoded Secrets                     | HARDCODED_SECRET            | TRUE  | TRUE  | TRUE    | FALSE  |
| High     | Hardcoded Passwords                   | HARDCODED_PASSWORD          | FALSE | FALSE | TRUE    | FALSE  |
| High     | Path Traversal                        | PATH_TRAVERSAL              | TRUE  | TRUE  | TRUE    | TRUE   |
| High     | Trust Boundary Violation              | TRUST_BOUNDARY_VIOLATION    | TRUE  | TRUE  | FALSE   | FALSE  |
| High     | Cross-Site Scripting (XSS)            | XSS                         | TRUE  | TRUE  | FALSE   | FALSE  |
| High     | Untrusted Deserialization             | UNTRUSTED_DESERIALIZATION   | TRUE  | FALSE | FALSE   | FALSE  |
| High     | Unvalidated Redirect                  | UNVALIDATED_REDIRECT        | TRUE  | TRUE  | TRUE    | FALSE  |
| High     | XPath Injection                       | XPATH_INJECTION             | TRUE  | TRUE  | FALSE   | FALSE  |
| High     | Header Injection                      | HEADER_INJECTION            | TRUE  | TRUE  | TRUE    | TRUE   |
| High     | Directory Listing Leak                | DIRECTORY_LISTING_LEAK      | TRUE  | FALSE | FALSE   | FALSE  |
| High     | Default HTML Escape Invalid           | DEFAULT_HTML_ESCAPE_INVALID | TRUE  | FALSE | FALSE   | FALSE  |
| High     | Verb Tampering                        | VERB_TAMPERING              | TRUE  | FALSE | FALSE   | FALSE  |
| Medium   | No SameSite Cookie                    | NO_SAMESITE_COOKIE          | TRUE  | TRUE  | TRUE    | TRUE   |
| Medium   | Insecure Cookie                       | INSECURE_COOKIE             | TRUE  | TRUE  | TRUE    | TRUE   |
| Medium   | No HttpOnly Cookie                    | NO_HTTPONLY_COOKIE          | TRUE  | TRUE  | TRUE    | TRUE   |
| Medium   | Weak Hashing                          | WEAK_HASH                   | TRUE  | TRUE  | TRUE    | TRUE   |
| Medium   | Weak Cipher                           | WEAK_CIPHER                 | TRUE  | TRUE  | TRUE    | TRUE   |
| Medium   | Stacktrace Leak                       | STACKTRACE_LEAK             | TRUE  | TRUE  | FALSE   | FALSE  |
| Medium   | Reflection Injection                  | REFLECTION_INJECTION        | TRUE  | TRUE  | FALSE   | FALSE  |
| Medium   | Insecure Authentication Protocol      | INSECURE_AUTH_PROTOCOL      | TRUE  | TRUE  | FALSE   | FALSE  |
| Medium   | Hardcoded Key                         | HARDCODED_KEY               | FALSE | TRUE  | FALSE   | FALSE  |
| Medium   | Insecure JSP Layout                   | INSECURE_JSP_LAYOUT         | TRUE  | FALSE | FALSE   | FALSE  |
| Low      | HSTS Header Missing                   | HSTS_HEADER_MISSING         | TRUE  | TRUE  | TRUE    | FALSE  |
| Low      | X-Content-Type-Options Header Missing | XCONTENTTYPE_HEADER_MISSING | TRUE  | TRUE  | TRUE    | FALSE  |
| Low      | Weak Randomness                       | WEAK_RANDOMNESS             | TRUE  | TRUE  | TRUE    | TRUE   |
| Low      | Admin Console Active                  | ADMIN_CONSOLE_ACTIVE        | TRUE  | FALSE | FALSE   | FALSE  |
| Low      | Session Timeout                       | SESSION_TIMEOUT             | TRUE  | FALSE | FALSE   | FALSE  |
| Low      | Session Rewriting                     | SESSION_REWRITING           | TRUE  | FALSE | FALSE   | FALSE  |

## How IAST detects vulnerabilities{% #how-iast-detects-vulnerabilities %}

Datadog Runtime Code Analysis (IAST) utilizes the same tracing libraries as Datadog APM, enabling it to monitor live application traffic and detect code-level vulnerabilities in real time. It follows this process:

- **Tracking data sources:**: IAST observes data entering your application from external sources such as request URLs, bodies, or headers. These inputs are tagged and monitored throughout their lifecycle.
- **Analyzing data flow**: The Datadog tracing library tracks how the input data moves through the applicationâeven if it's transformed, split, or combined. This allows IAST to understand if and how the original input reaches sensitive parts of the code.
- **Identifying vulnerable points**: IAST detects code locations where user-controlled inputs are used in potentially insecure waysâfor example, in SQL queries, dynamic code execution, or HTML rendering.
- **Confirming the vulnerability**: A vulnerability is only reported when IAST can confirm that tainted input reaches a vulnerable point in the code. This approach minimizes false positives and ensures that findings are actionable.

## Explore and manage code vulnerabilities{% #explore-and-manage-code-vulnerabilities %}

The [Vulnerability Explorer](https://app.datadoghq.com/security/appsec/vm/code) uses real-time threat data to help you understand vulnerabilities endangering your system. Vulnerabilities are ordered by severity.

{% image
   source="https://datadog-docs.imgix.net/images/code_security/vulnerability_explorer_code_vulnerabilities.e38bdfc735fef115116f9f82906c1295.png?auto=format"
   alt="Code Security in the Vulnerability Explorer" /%}

To triage vulnerabilities, each vulnerability contains a brief description of the issue, including:

- Impacted services.
- Vulnerability type.
- First detection.
- The exact file and line number where the vulnerability was found.

{% image
   source="https://datadog-docs.imgix.net/images/code_security/vulnerability-details.0192458122573d19e31e07eea730805b.png?auto=format"
   alt="Code Security vulnerability details" /%}

Each vulnerability detail includes a risk score (see screenshot below) and a severity rating: critical, high, medium, or low.

The risk score is tailored to the specific runtime context, including factors such as where the vulnerability is deployed and whether the service is targeted by active attacks.

{% image
   source="https://datadog-docs.imgix.net/images/code_security/vulnerability_prioritization.3975bf449665263ca1c37447c8d10a55.png?auto=format"
   alt="Code Security vulnerability prioritization" /%}

## Remediate a code vulnerability{% #remediate-a-code-vulnerability %}

Datadog Code Security automatically provides the information teams need to identify where a vulnerability is in an application, from the affected filename down to the exact method and line number.

{% image
   source="https://datadog-docs.imgix.net/images/code_security/code_security_remediation.b379a98e5b03934dcc2691650fa69efc.png?auto=format"
   alt="Code Security vulnerability remediation" /%}

When the [GitHub integration](https://docs.datadoghq.com/integrations/github/) is enabled, Code Security shows the first impacted version of a service, the commit that introduced the vulnerability, and a snippet of the vulnerable code. This information gives teams insight into where and when a vulnerability occurred and helps to prioritize their work.

{% image
   source="https://datadog-docs.imgix.net/images/code_security/vulnerability_code_snippet.1950c985733bd0b83ea313ed3c7d834b.png?auto=format"
   alt="Code vulnerability snippet" /%}

Detailed remediation steps are provided for each detected vulnerability.

{% image
   source="https://datadog-docs.imgix.net/images/code_security/remediation_recommendations.d00b0cac08e6b7601f54b384e0fb6df5.png?auto=format"
   alt="Remediation recommendations" /%}

Recommendations enable you to change the status of a vulnerability, assign it to a team member for review, and create a Jira issue for tracking.

{% image
   source="https://datadog-docs.imgix.net/images/code_security/vulnerability_jira_ticket.ea276726e4f348e72b5187395297c74b.png?auto=format"
   alt="creating a Jira ticket from a vulnerability" /%}

**Note:** To create Jira issues for vulnerabilities, you must configure the Jira integration, and have the `manage_integrations` permission. For detailed instructions, see the [Jira integration](https://docs.datadoghq.com/integrations/jira/) documentation, as well as the [Role Based Access Control](https://docs.datadoghq.com/account_management/rbac/permissions/#integrations) documentation.

## Vulnerability lifecycle{% #vulnerability-lifecycle %}

Datadog automatically manages the lifecycle of vulnerabilities detected by IAST to ensure findings remain accurate and relevant over time.

- **Automatic closure:** Vulnerabilities detected by IAST are automatically closed by Datadog when they haven't been observed for **14 days** since their last detection.

- **Service version updates:** If a new version of the service is deployed in the environment where the vulnerability was originally detected, the vulnerability is automatically closed **24 hours** after it is no longer seen in that new version.

- **Reopening logic:** If a vulnerability that was previously closed is detected again within the following **15 months**, Datadog automatically reopens it.

## Enable Runtime Code Analysis (IAST){% #enable-runtime-code-analysis-iast %}

To enable IAST, configure the [Datadog Tracing Library](https://docs.datadoghq.com/security/code_security/iast/setup/). Detailed instructions for both methods can be found in the [**Security > Code Security > Settings**](https://app.datadoghq.com/security/configuration/code-security/setup) section.

If you need additional help, contact [Datadog support](https://www.datadoghq.com/support/).

## Disable Code Security{% #disable-code-security %}

For information on disabling IAST, see [Disabling Code Security](https://docs.datadoghq.com/security/code_security/troubleshooting).

## Further reading{% #further-reading %}

- [Protect the life cycle of your application code and libraries with Datadog Code Security](https://www.datadoghq.com/blog/datadog-code-security/)
- [Detect and block exposed credentials with Datadog Secret Scanning](https://www.datadoghq.com/blog/code-security-secret-scanning)
