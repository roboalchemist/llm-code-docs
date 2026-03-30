# Source: https://docs.wandb.ai/models/ref/python/public-api/betareport.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# BetaReport

export const GitHubLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="github-source-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z" />
    </svg>
    GitHub source
  </a>;

<GitHubLink url="https://github.com/wandb/wandb/blob/main/wandb/apis/public/reports.py" />

## <kbd>class</kbd> `BetaReport`

BetaReport is a class associated with reports created in W\&B.

Provides access to report attributes (name, description, user, spec, timestamps) and methods for retrieving associated runs, sections, and for rendering the report as HTML.

**Attributes:**

* `id` (string):  Unique identifier of the report.
* `display_name` (string):  Human-readable display name of the report.
* `name` (string):  The name of the report. Use `display_name` for a more user-friendly name.
* `description` (string):  Description of the report.
* `user` (User):  Dictionary containing user info (username, email) who  created the report.
* `spec` (dict):  The spec of the report.
* `url` (string):  The URL of the report.
* `updated_at` (string):  Timestamp of last update.
* `created_at` (string):  Timestamp when the report was created.

### <kbd>method</kbd> `BetaReport.__init__`

```python  theme={null}
__init__(
    client: 'RetryingClient',
    attrs: 'dict',
    entity: 'str | None' = None,
    project: 'str | None' = None
)
```

***

### <kbd>property</kbd> BetaReport.created\_at

***

### <kbd>property</kbd> BetaReport.description

***

### <kbd>property</kbd> BetaReport.display\_name

***

### <kbd>property</kbd> BetaReport.id

***

### <kbd>property</kbd> BetaReport.name

***

### <kbd>property</kbd> BetaReport.sections

Get the panel sections (groups) from the report.

***

### <kbd>property</kbd> BetaReport.spec

***

### <kbd>property</kbd> BetaReport.updated\_at

***

### <kbd>property</kbd> BetaReport.url

***

### <kbd>property</kbd> BetaReport.user

***

### <kbd>method</kbd> `BetaReport.runs`

```python  theme={null}
runs(
    section: 'dict[str, Any]',
    per_page: 'int' = 50,
    only_selected: 'bool' = True
) → public.Runs
```

Get runs associated with a section of the report.

***

### <kbd>method</kbd> `BetaReport.to_html`

```python  theme={null}
to_html(height: 'int' = 1024, hidden: 'bool' = False) → str
```

Generate HTML containing an iframe displaying this report.
