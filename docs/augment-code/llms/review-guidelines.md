# Source: https://docs.augmentcode.com/codereview/review-guidelines.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Review Guidelines

> Configure custom guidelines to help Augment Code Review focus on specific areas and domain knowledge. Learn which files are automatically skipped and how to customize file exclusions.

## Tell Augment Code Review to check specific areas with guidelines

Some domain knowledge cannot be inferred from code alone. Tell Augment Code Review exactly what to check by adding custom guidelines. Guidelines are most relevant for repositories that contain multiple distinct domains and should be captured as custom review guidelines. Tell Augment Code Review to check specific areas like security vulnerabilities or inside particular directories when relevant. Augment Code Review allows you to outline these special guidelines per repository. Describe any areas of focus using a yaml file entitled code\_review\_guidelines.yaml inside the .augment folder at the repository root:

`<repo-root>/.augment/code_review_guidelines.yaml`

Scope guidelines to the appropriate sub-directories and focus on objective issues that can cause bugs, expose vulnerabilities, etc. and less on stylistic or subjective things. Augment Code Review uses a unique yaml file instead of relying on markdown guideline files like Agents.md, etc. because it allows the agent to cite a guideline if it was used for a particular comment, and compute per-guideline analytics.

### Example Augment Code Review Guidelines

For a complete working example, see the [Code Review Best Practices](https://github.com/augmentcode/code-review-best-practices) repository.

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

### Referencing Existing Rules Files

You can add a custom rule that references an existing rules file (like `Agents.md`) to incorporate those guidelines into your code review process. This allows you to reuse existing documentation and standards without duplicating content.

However, it is recommended to use the YAML format to track guidelines, as this enables Augment Code Review to cite specific guidelines in comments and compute per-guideline analytics.

## Files Automatically Skipped During Review

Augment Code Review automatically skips certain file types that are not typically code files. This helps focus the review on meaningful code changes and avoids wasting time on binary files, generated content, and other non-reviewable assets.

<Accordion title="File Extensions Automatically Ignored">
  The following file extensions are automatically skipped during code review:

  **Archive files:**

  * `.bz2`, `.gz`, `.xz`, `.zip`, `.7z`, `.rar`, `.zst`, `.tar`, `.jar`, `.war`, `.nar`

  **Image files:**

  * `.ico`, `.svg`, `.jpeg`, `.jpg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.webm`

  **Font files:**

  * `.ttf`, `.otf`, `.woff`, `.woff2`, `.eot`

  **Document files:**

  * `.pdf`, `.doc`, `.docx`, `.xls`, `.xlsx`, `.ppt`, `.pptx`

  **Data files:**

  * `.csv`, `.tsv`, `.dat`, `.db`, `.parquet`

  **System files:**

  * `.DS_Store`, `.tags`

  **Cscope files:**

  * `.cscope.files`, `.cscope.out`, `.cscope.in.out`, `.cscope.po.out`

  **Log and output files:**

  * `.log`, `.map`, `.out`, `.sum`, `.work`, `.md5sum`

  **3D and graphics files:**

  * `.tga`, `.dds`, `.psd`, `.fbx`, `.obj`, `.blend`, `.dae`, `.gltf`

  **Shader files:**

  * `.hlsl`, `.glsl`

  **Game engine files:**

  * `.unity`, `.umap`, `.prefab`, `.mat`, `.shader`, `.shadergraph`, `.sav`, `.scene`, `.asset`

  **Python compiled files:**

  * `.pyc`, `.pyd`, `.pyo`, `.pkl`, `.pickle`

  **Protocol buffer files:**

  * `.pb.go`, `.pb.gw.go`

  **Terraform files:**

  * `.tfstate`, `.tfstate.backup`

  **Minified files:**

  * `.min.js`, `.min.js.map`, `.min.css`

  **Lock and dependency files:**

  * `.lock`, `.lockb`, `.lockfile`

  **Debug and trace files:**

  * `.trace`, `.dump`

  **Backup files:**

  * `.bak`, `.backup`

  **Database files:**

  * `.sql.gz`
</Accordion>

<Accordion title="File Patterns Automatically Ignored">
  In addition to specific extensions, the following file patterns are also skipped:

  * `*lock.json`, `*lock.yaml`, `*lock.yml` - Lock files with specific patterns
  * `go.sum` - Go module checksum files
  * `*.bundle.js`, `*.chunk.js` - JavaScript bundle files
  * `**/generated/**`, `**/*.generated.*` - Generated files
  * `*_snapshot.json` - Snapshot files
</Accordion>

## Customizing Files to Skip

You can add additional files or paths to skip during code review by specifying them in your custom guidelines file. This is useful for repository-specific generated files, large data files, or other content that shouldn't be reviewed.

### Adding Custom File Paths to Ignore

Use the `file_paths_to_ignore` section in your `code_review_guidelines.yaml` file. This field supports doublestar glob patterns for flexible matching.

```yaml  theme={null}
# File paths to ignore during code review (supports doublestar glob patterns)
file_paths_to_ignore:
  - "services/code_review/**/category_taxonomy.json"
  - "**/generated/**"
  - "**/*.generated.ts"
  - "dist/**"
  - "build/**"
```

<Accordion title="Complete Example with Custom Ignores">
  ```yaml  theme={null}
  # Guidelines for myproject

  # Custom files to skip during review
  file_paths_to_ignore:
    - "services/code_review/**/category_taxonomy.json"
    - "**/*.generated.graphql"
    - "public/assets/**"

  areas:
    databases:
      description: "Data and Database related rules"
      globs:
        - "**"
      rules:
        - id: "no_pii_in_bigquery"
          description: "Never store PII data in BigQuery tables."
          severity: "high"
  ```
</Accordion>
