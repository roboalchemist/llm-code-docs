# Source: https://docs.qodo.ai/qodo-documentation/code-review/get-started/use-qodo-in-prs/code-review/findings-visibility.md

# Control Findings Visibility and Expansion in PRs

{% hint style="success" %}
These configurations can also be set organization-wide in the [Qodo portal.](https://docs.qodo.ai/qodo-documentation/code-review/get-started/configuration-overview/portal-configuration)
{% endhint %}

You can control how many findings are surfaced in a review to avoid overwhelming developers on large pull requests.

This helps keep feedback focused and actionable, while still preserving full visibility.

* Only a subset of findings are shown by default
* Additional findings are not discarded
* Hidden findings can be viewed by expanding the section in the review summary

In addition to controlling the number of findings surfaced, you can also configure how findings are displayed and expanded in the review output.

### Number of findings shown before collapse

Control how many findings are shown before the rest collapse behind **“View all”**.

Example:

```
[review_agent_ux]
finding_overflow_count = 3
```

Supported values:

* `none` – all findings collapsed
* `1`, `3`, `5` – number of findings shown before “View all”
* `all` – all findings expanded

### Number of resolved findings shown before collapse

Control how many **resolved findings** are shown before the rest collapse behind **“View all”**.

Example:

```
[review_agent_ux]
resolved_overflow_count = 3
```

Supported values:

* `none`
* `1`, `3`, `5`
* `all`

### Default expanded sections in a finding

Control which sections of a finding are expanded by default when it is opened.

Example:

```
[review_agent_ux]
expand_description = true
expand_code = true
expand_evidence = false
expand_prompt = false
```

Values:

* `true` – section expanded by default
* `false` – section collapsed by default

Settings:

* `expand_description` – Description section
* `expand_code` – Code section
* `expand_evidence` – Evidence section
* `expand_prompt` – Agent prompt section
