# Source: https://help.aikido.dev/code-scanning/scanning-practices/sast-autotriage.md

# Denoise via SAST AutoTriage

AutoTriage reduces noise from static analysis so engineers can focus on issues that are actual security threats. It does this by first trying to rule out exploitability, and then, only when needed, ranking the remaining findings by (1) exploitability, and (2) severity if exploited. In Aikido, AutoTriage primarily operates on SAST findings and plugs into familiar development workflows like your local IDE, PR checks, and scheduled nightly scans.

{% hint style="info" %}
AutoTriage primarily targets SAST. A small number of cloud and container checks are also supported where context allows similar upgrade/downgrade decisions.
{% endhint %}

### What AutoTriage is (and isn’t)

AutoTriage isn't itself a scanner. It sits downstream of your scans and makes determinations about ***exploitability*** and ***severity*** based on the code and its context.&#x20;

For the majority of SAST issues, Aikido performs triage based on Aikido-defined rules. For some more complex cases, Aikido uses reasoning models to interpret more nuanced control and data flows. This will include constructing a relevant code snippet by calculating the call tree and incorporating any called functions that reference variables passed to the vulnerability sink.

In Aikido's internal evaluations this approach detects roughly twice as many false positives on those complex cases compared to non‑reasoning approaches.

### How AutoTriage works

#### False positive filtering before triage

**Before AutoTriage uses an LLM to look at your code**, Aikido’s [reachability](https://help.aikido.dev/getting-started/reachability-analysis/reachability-engine-to-remove-false-positives) engine filters out false positives by checking whether vulnerable code paths are even reachable in your application. That may include:

* Verifying you actually call the affected function
* Tracing whether a vulnerable dependency is only used in tools versus in production&#x20;
* Checking for any sanitization between source and sink
* Pruning stale or unused code paths

These steps alone suppress a significant portion of alerts compared with most traditional scanners.

> You'll likely notice that many prospective issues are automatically marked as ignored because reachability analysis determined there’s no path from untrusted input to a dangerous sink, or the usage sits outside a production flow.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FGX2AELTpYyZHoexWVIWj%2FScreenshot%202025-10-23%20at%205.19.02%E2%80%AFPM.png?alt=media&#x26;token=62760212-e9d9-42e0-89ef-bcce78fc8841" alt=""><figcaption></figcaption></figure>

If exploitability cannot be ruled out, then AutoTriage proceeds to prioritization.

#### Priority scoring

When an issue remains possibly exploitable, AutoTriage sets the priority by assessing likelihood and impact. It starts from Aikido’s severity score (0–100) and adjusts it up or down using the code context gathered in the earlier steps.&#x20;

> **Examples:**
>
> * &#x20;An SQL injection report might be safely ***downgraded*** if the input variable originates from a trusted source such as a database that’s already validated upstream
> * &#x20;A login endpoint with a NoSQL injection risk can be ***upgraded*** to “very high priority to fix” because the attack is trivial and directly impacts authentication, as shown below

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FBhJgU2TY8Lye4kZxMTCZ%2Fimage.png?alt=media&#x26;token=a2683700-595f-4bdd-94c9-885a0279744e" alt=""><figcaption></figcaption></figure>

#### If true positive, then AutoFix

For triaged true positives, Aikido can generate a recommended patch through [AutoFix](https://help.aikido.dev/aikido-autofix/overview-aikido-autofix) and open a pull request for review. AutoFix focuses on the reported vulnerability only and is available in PR checks in GitHub, GitLab, Bitbucket, Azure DevOps, as well as in your local IDE.

### Signals AutoTriage considers

AutoTriage is **context‑hungry** by design. In practice, it considers things like:

* Reachability of user input into sensitive sinks, as well as presence and effectiveness of sanitization/validation
* Whether input originates from trusted stores, and whether vulnerable code is used at build or test time versus in production
* Business impact signals, like data sensitivity&#x20;
* For complex rules reasoning models evaluate edge cases such, for example OS‑specific separators, and path resolution semantics
