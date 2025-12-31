# Source: https://docs.augmentcode.com/codereview/review-guidelines.md

# Adding Review Guidelines

> Configure custom guidelines to help Augment Code Review focus on specific areas and domain knowledge.

## Tell Augment Code Review to check specific areas with guidelines

Some domain knowledge cannot be inferred from code alone. Tell Augment Code Review exactly what to check by adding custom guidelines. Guidelines are most relevant for repositories that contain multiple distinct domains and should be captured as custom review guidelines. Tell Augment Code Review to check specific areas like security vulnerabilities or inside particular directories when relevant. Augment Code Review allows you to outline these special guidelines per repository. Describe any areas of focus using a yaml file entitled code\_review\_guidelines.yaml inside the .augment folder at the repository root:

`<repo-root>/.augment/code_review_guidelines.yaml`

Scope guidelines to the appropriate sub-directories and focus on objective issues that can cause bugs, expose vulnerabilities, etc. and less on stylistic or subjective things. Augment Code Review uses a unique yaml file instead of relying on markdown guideline files like Agents.md, etc. because it allows the agent to cite a guideline if it was used for a particular comment, and compute per-guideline analytics.

### Example Augment Code Review Guidelines

```yaml  theme={null}
# Guidelines exclusive to augmentcode/auggie

areas:
  databases:
    description: "Data and Database related rules"
    globs:
      - "**"
    rules:
      - id: "no_pii_in_bigquery"
        description: "Never store PII data in BigQuery tables."
        severity: "high"
      - id: "no_guid_keys"
        description: "GUID foreign keys can slow lookups"
        severity: "medium"

  memory_safety:
    description: "Ensure Memory Safety"
    globs:
      - "kernel/**"
    rules:
      - id: "avoid_unsafe_rust"
        description: "Avoid unsafe Rust operations."
        severity: "high"
```

<Note>
  Common **globs** or pattern matching syntax:

  * `**` - Matches any number of directories (recursive wildcard)
    * Example: `**/test.py` matches `test.py`, `src/test.py`, `src/utils/test.py`, etc.
  * `*` - Matches any sequence of characters within a single directory level
    * Example: `*.py` matches `file.py`, `main.py` but not `src/main.py`
  * `?` - Matches exactly one character
    * Example: `test?.py` matches `test1.py`, `testA.py` but not `test10.py`
</Note>

* **Rules:** Areas can contain more than one rule. Each rule contains:
  * **ID**: Double quoted unique identifier
  * **Description**: Double quoted message summarizing intent of the rule
  * **Severity**: Expects double quoted "high", "medium" or "low". Sets the priority of review by Augment Code Review


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.augmentcode.com/llms.txt