# Source: https://docs.qodo.ai/qodo-documentation/code-review/tutorials/shape-the-review-experience-lean-vs-verbose.md

# Shape the Review Experience: Lean vs Verbose

The review experience is shaped by how multiple configuration settings work together. By tuning severity thresholds, display mode, limits on findings, display preferences, verbosity, and ignore rules, you can make reviews feel more **lean** or more **verbose**.

#### Lean review experience

A lean review experience focuses on surfacing only the most critical issues and minimizing noise.

It is typically achieved by combining:

* Higher severity thresholds for inline comments
* Fewer findings shown by default
* More collapsed findings in the review view
* Summary-focused feedback
* More aggressive ignore rules (for PRs, files, tickets, or authors)

**Example configuration:**

```toml
# Only show the most critical issues inline
inline_comments_severity_threshold = 3

# Show feedback primarily in the summary
comments_location_policy = "summary"

# Ignore low-signal PRs and generated code
[config]
ignore_pr_labels = ["chore", "skip-review"]
ignore_language_framework = ["protobuf"]

# Display a minimal set of findings and keep most sections collapsed
[review_agent_ux]
finding_overflow_count = 1
resolved_overflow_count = 1
expand_description = true
expand_code = false
expand_evidence = false
expand_prompt = false
```

This setup highlights only issues that must be addressed before merging and keeps the review output compact.

#### Verbose review experience

A verbose review experience provides broader coverage and richer context.

It is typically achieved by combining:

* Lower severity thresholds for inline comments
* More findings shown by default
* Expanded sections that provide richer context
* Feedback shown both inline and in summary
* No ignore rules

**Example configuration:**

```toml
# Show multiple severity levels inline
inline_comments_severity_threshold = 1

# Show feedback both inline and in summary
comments_location_policy = "both"

# Display more findings and expand contextual sections
[review_agent_ux]
finding_overflow_count = 5
resolved_overflow_count = 5
expand_description = true
expand_code = true
expand_evidence = true
expand_prompt = true
```

This setup is useful during onboarding, when working with new codebases, or when teams want deeper insight and guidance.
