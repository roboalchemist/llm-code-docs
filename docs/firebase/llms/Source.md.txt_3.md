# Source: https://firebase.google.com/docs/reference/data-connect/rest/v1beta/Source.md.txt

# Source

Used to represent a set of source files.

| JSON representation |
|---|
| ``` { "files": [ { object (`https://firebase.google.com/docs/reference/data-connect/rest/v1beta/Source#File`) } ] } ``` |

| Fields ||
|---|---|
| `files[]` | ``object (`https://firebase.google.com/docs/reference/data-connect/rest/v1beta/Source#File`)`` Required. The files that comprise the source set. |

## File

Individual files.

| JSON representation |
|---|
| ``` { "path": string, "content": string } ``` |

| Fields ||
|---|---|
| `path` | `string` Required. The file name including folder path, if applicable. The path should be relative to a local workspace (e.g. dataconnect/(schema\|connector)/\*.gql) and not an absolute path (e.g. /absolute/path/(schema\|connector)/\*.gql). |
| `content` | `string` Required. The file's textual content. |