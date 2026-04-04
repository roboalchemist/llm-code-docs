# Semgrep Secrets overview

Source: https://semgrep.dev/docs/semgrep-secrets/conceptual-overview

- [](/docs/)- [Scan](/docs/getting-started/quickstart)- Scan and triage- Secrets- Overview**On this page- [Semgrep Secrets](/docs/tags/semgrep-secrets)Semgrep Secrets overview
**Semgrep Secrets** scans code to detect exposed API keys, passwords, and other
credentials. When exposed, these can be used by malicious actors to leak data
or gain access to sensitive systems. Semgrep Secrets allows you to determine:

- What secrets have been committed to your repository.
- The validation status of the secret; for example, **valid** secrets are those that have been tested against a web service and
confirmed to successfully grant resources or authentication. They are actively
in use.
- For GitHub repositories: if there are credentials in public or private repositories.

Semgrep saves security engineers time and effort by prioritizing valid leaked secrets and informs developers of valid secrets in their PRs and MRs by posting comments directly.

## How Semgrep Secrets works[​](#how-semgrep-secrets-works)
To ensure that findings are high-signal, comprehensive, and easy for users to
prioritize, a Semgrep Secrets scan performs the following:

- Search using regex
- Semantic analysis
- Validation
- Entropy analysis

The following sections explain how each step works.

### Detect secrets through regex[​](#detect-secrets-through-regex)
Semgrep Secrets uses a regex language detector to find secrets in various file types. This is done by detecting a commonly defined prefix and then searching for the secret using its expected length and format.

To reduce the number of false positives this process raises, Semgrep uses and combines as many of the following processes with its search using regex when possible:

- Removal of results that are likely to be false positives
- Validation
- Entropy analysis

### Detect secrets through semantic analysis[​](#detect-secrets-through-semantic-analysis)
Semantic analysis refers to Semgrep Secrets&#x27; ability to understand how data is
used within your code. This differentiates Semgrep Secrets from regex-based
detectors that simply define a pattern to match a piece of code.

Semgrep Secrets uses several mechanisms to perform semantic analysis. It uses
[** dataflow
analysis](/docs/writing-rules/data-flow/data-flow-overview) and [** constant
propagation](/docs/writing-rules/data-flow/constant-propagation) which means that it
is able to track data, such as variables, and the flow of that data across files
and functions in your codebase.

Performing semantic analysis is encapsulated in [** rules](/docs/running-rules). By running these rules, Semgrep
Secrets is able to detect if a variable is renamed,
reassigned, or used in a function in such a way that a secret is exposed.

See the following rule and JavaScript test code for an example.

*

### Validate secrets[​](#validate-secrets)
After scanning your codebase, Semgrep Secrets uses a proprietary
**validator** to determine if a secret is actively being used or some other state if there is a validator defined in the rule used.

infoAll validations, such as API calls, are done **locally** in your environment. No tokens are sent to Semgrep servers.

- The validator detects the service, such as Slack or AWS, that the secret
is used for.
- If the validator doesn&#x27;t support the service that the secret is used
for, Semgrep notes that there is **No validator** finding for the secret.
- Semgrep Secrets performs an API
call if the validator supports the service. The following outcomes can occur:

**Confirmed valid:** Semgrep made an HTTP request using the secret, and it returned an HTTP status code of 200 or similar **and** some indication of valid access. For example, a service can include a `&quot;message&quot;: &quot;ok&quot;` in the response body.
- **Confirmed invalid:** Semgrep made an HTTP request using the secret and it returned an HTTP status code of 401 or similar.
- **Validation error:** Semgrep made an HTTP request using the secret, but either the network request could not be made, a timeout occurred, or the HTTP status code returned a different HTTP status code. In this case, the Semgrep Team recommends manually reviewing the finding.
- **No Validator:** The rule does not have a validator. The Semgrep Team recommends manually reviewing the finding.

By performing this validation check, you can prioritize and triage the most
high-priority, active findings.

note
- For a list of all supported detectors that Semgrep offers, see the [Policies](/docs/semgrep-secrets/policies) page in your deployment.
- See [Validators](/docs/semgrep-secrets/validators) for syntax and examples.

### Fine-tune findings through entropy analysis[​](#fine-tune-findings-through-entropy-analysis)
Entropy is the measure of a **string&#x27;s randomness**. It&#x27;s used to measure how
likely a string is random. If a string is highly entropic, it&#x27;s highly
random. For certain types of secrets, such as API keys, randomness indicates
that a string could be a secret. By performing entropy analysis, Semgrep Secrets
can reduce false positives and produce more true positives.

Examples of high-entropy (random) strings:

`EXAMPLE_HIGH_ENTROPY_STRING_REDACTED`
Examples of low-entropy strings:

`XXXXXXtxtPassword1`
## Next steps[​](#next-steps)
See [* Scan for secrets](/docs/semgrep-secrets/getting-started) to learn how to:

- Enable secrets scanning for your repositories
- Manage the rules in your [policy](/docs/semgrep-secrets/policies) to control how your scan runs.
- View and triage secrets-related findings
- Receive notifications and post tickets whenever Semgrep Secrets identifies issues
- Write [custom rules](/docs/semgrep-secrets/rules) with [validators](/docs/semgrep-secrets/validators) to find bespoke secrets
Not finding what you need in this doc? Ask questions in our [Community Slack group](https://go.semgrep.dev/slack), or see [Support](/docs/support/) for other ways to get help.

Tags:**- [Semgrep Secrets](/docs/tags/semgrep-secrets)[Edit this page](https://github.com/semgrep/semgrep-docs/edit/main/docs/semgrep-secrets/conceptual-overview.md)Last updated on **Oct 15, 2025**