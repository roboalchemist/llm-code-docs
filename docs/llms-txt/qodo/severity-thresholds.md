# Source: https://docs.qodo.ai/qodo-documentation/code-review/get-started/use-qodo-in-prs/code-review/severity-thresholds.md

# Configure Severity Levels and Inline Comment Thresholds in PRs

{% hint style="success" %}
**Platforms supported:** GitHub, GitLab
{% endhint %}

Findings are categorized by severity. Severity is used both for prioritization and for controlling which findings appear inline in the pull request.

You can configure a severity threshold to limit which findings are shown as inline comments.\
\
Example:

```toml
inline_comments_severity_threshold = 3
```

<table><thead><tr><th data-type="number">Threshold Value</th><th>Inline Issues Shown</th><th>Description</th></tr></thead><tbody><tr><td>3</td><td>Action Required</td><td>Blocking or critical issues</td></tr><tr><td>2</td><td>Action Required, Remediation Recommended</td><td>Important but non-blocking issues, plus critical ones</td></tr><tr><td>1</td><td>Action Required, Remediation Recommended, Other</td><td>All findings, including informational</td></tr></tbody></table>

* The severity threshold applies only to inline comments
* The summary view always shows all findings, regardless of severity This enables teams to keep inline feedback focused while preserving full visibility in the summary.
