# Source: https://northflank.com/docs/v1/api/project/pipelines/update-release-flow.md

# Update release flow

Updates a release flow

Required permission: Project > Pipelines > General > Update

**Path parameters:**

{object}
- `projectId`: (string) (required) ID of the project
- `pipelineId`: (string) (required) ID of the pipeline
- `stage`: (string) (required) Stage of the pipeline

**Request body:**

{object}
- `arguments`: {object}
- `triggers`: [array of] {object}
   - `ref`: (string) A reference that can be used to access the output of this trigger in the template.
   - `vcsService`: (string) (required) The VCS provider to use. (enum: bitbucket, gitlab, github, self-hosted, azure)
   - `selfHostedVcsId`: (string) If vcsService is self-hosted, the ID of the self-hosted vcs to use. (pattern: ^([A-Za-z0-9-]+)|([0-9a-f]{24})$)
   - `accountLogin`: (string) By default, if you have multiple version control accounts of the same provider linked, Northflank will pick a linked account that has access to the repository. If `accountLogin` is provided, Northflank will instead use your linked account with that login name.
   - `vcsLinkId`: (string)
   - `repoUrl`: (string) (required) URL of the Git repo that will trigger the template. (pattern: ^(https:\/\/)?((www(\.[a-zA-Z0-9\-]{2,})+\.)?[a-zA-Z0-9\-]{2,})(\.([a-zA-Z0-9\-]{2,}))+(\/([a-zA-Z0-9\-._]{2,}))+?$)
   - `branchRestrictions`: [array of] (string) (pattern: ^[a-zA-Z/*0-9%\-.#_!'();,&=+]*$)
   - `prRestrictions`: [array of] (string) (pattern: ^[a-zA-Z/*0-9%\-.#_!'();,&=+]*$)
   - `pathIgnoreRules`: [array of] (string) A path ignore rule, following `.gitignore` syntax. For example, `*.md` will ignore all files ending with `.md`. (max length: 260)
   - `ciIgnoreFlags`: [array of] (string) A commit ignore flag. (max length: 72)
   - `ciIgnoreFlagsEnabled`: (boolean)
   - `isAllowList`: (boolean)
   - `ignoreDrafts`: (boolean) If `true`, draft pull requests from this repo will not trigger the template.
- `options`: {object}
  - `concurrencyPolicy`: (string) Defines the concurrency behaviour of the template with respect to parallel runs. (enum: allow, queue, forbid)
  - `paused`: (boolean) If `true`, the template will not run when triggered by git.
- `gitops`: {object}
  - `vcsService`: (string) (required) The VCS provider to use. (enum: bitbucket, gitlab, github, self-hosted, azure)
  - `selfHostedVcsId`: (string) If projectType is self-hosted, the ID of the self-hosted vcs to use. (pattern: ^([A-Za-z0-9-]+)|([0-9a-f]{24})$)
  - `accountLogin`: (string) By default, if you have multiple version control accounts of the same provider linked, Northflank will pick a linked account that has access to the repository. If `accountLogin` is provided, Northflank will instead use your linked account with that login name.
  - `vcsLinkId`: (string) Legacy key. Please used accountLogin instead.
  - `repoUrl`: (string) (required) URL of the Git repo to sync the file with. (pattern: ^(https:\/\/)?((www(\.[a-zA-Z0-9\-]{2,})+\.)?[a-zA-Z0-9\-]{2,})(\.([a-zA-Z0-9\-]{2,}))+(\/([a-zA-Z0-9\-._]{2,}))+?$)
  - `branch`: (string) (required) The name of the branch to use.
  - `filePath`: (string) (required) The file path in the repository. If using an existing file, it should be in JSON format. (pattern: ^\/([a-zA-Z0-9-._]+\/)*[a-zA-Z0-9-._]+$)
- `$schema`: (string)
- `richInputs`: [array of] (multiple options) {object}
    - `kind`: (string) (required) The kind of input. (enum: BranchCommitSelector)
    - `spec`: {object}
      - `title`: (string) (required) The title displayed for the input.
      - `description`: (string) The description displayed for the input.
      - `required`: (boolean) If true, an error will be displayed if this input is not provided a value.
      - `inputs`: {object}
        - `source`: (string) (required) The ID of the build service to use for this input.
      - `outputs`: {object}
        - `branch`: (string)
        - `buildSha`: (string) | {object}
    - `kind`: (string) (required) The kind of input. (enum: BuildSelector)
    - `spec`: {object}
      - `title`: (string) (required) The title displayed for the input.
      - `description`: (string) The description displayed for the input.
      - `required`: (boolean) If true, an error will be displayed if this input is not provided a value.
      - `inputs`: {object}
        - `source`: (string) (required) The ID of the build service to use for this input.
      - `outputs`: {object}
        - `branch`: (string)
        - `buildId`: (string)
        - `buildSha`: (string)
- `apiVersion`: (string) (required)
- `project`: {object}
- `spec`: {object}

## API reference

POST /v1/projects/{projectId}/pipelines/{pipelineId}/release-flows/{stage}

POST /v1/teams/{teamId}/projects/{projectId}/pipelines/{pipelineId}/release-flows/{stage}

### Example request

Request body

```curl
curl --header "Content-Type: application/json" \
  --header "Authorization: Bearer NORTHFLANK_API_TOKEN" \
  --request POST \
  --data '{"triggers":[{"vcsService":"github","accountLogin":"github-user","repoUrl":"https://github.com/northflank-examples/remix-postgres-redis-demo","pathIgnoreRules":["README.md"],"ciIgnoreFlags":["[skip ci]"]}],"options":{"concurrencyPolicy":"allow","paused":false},"gitops":{"vcsService":"github","accountLogin":"github-user","repoUrl":"https://github.com/northflank-examples/remix-postgres-redis-demo","branch":"main","filePath":"/Dockerfile"},"richInputs":[{"kind":"BranchCommitSelector","spec":{"required":false,"inputs":{"source":"build-service"},"outputs":{"branch":"TARGET_BRANCH","buildSha":"TARGET_COMMIT"}}}]}' \
  https://api.northflank.com/v1/projects/{projectId}/pipelines/{pipelineId}/release-flows/{stage}
```

```javascript
const payload = {
  "triggers": [
    {
      "vcsService": "github",
      "accountLogin": "github-user",
      "repoUrl": "https://github.com/northflank-examples/remix-postgres-redis-demo",
      "pathIgnoreRules": [
        "README.md"
      ],
      "ciIgnoreFlags": [
        "[skip ci]"
      ]
    }
  ],
  "options": {
    "concurrencyPolicy": "allow",
    "paused": false
  },
  "gitops": {
    "vcsService": "github",
    "accountLogin": "github-user",
    "repoUrl": "https://github.com/northflank-examples/remix-postgres-redis-demo",
    "branch": "main",
    "filePath": "/Dockerfile"
  },
  "richInputs": [
    {
      "kind": "BranchCommitSelector",
      "spec": {
        "required": false,
        "inputs": {
          "source": "build-service"
        },
        "outputs": {
          "branch": "TARGET_BRANCH",
          "buildSha": "TARGET_COMMIT"
        }
      }
    }
  ]
}

const response = await fetch('https://api.northflank.com/v1/projects/{projectId}/pipelines/{pipelineId}/release-flows/{stage}', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${NORTHFLANK_API_TOKEN}`
  },
  body: JSON.stringify(payload)
})

const json = await response.json()
console.log(json)
```

```python
import requests

url = "https://api.northflank.com/v1/projects/{projectId}/pipelines/{pipelineId}/release-flows/{stage}"

payload = {"triggers":[{"vcsService":"github","accountLogin":"github-user","repoUrl":"https://github.com/northflank-examples/remix-postgres-redis-demo","pathIgnoreRules":["README.md"],"ciIgnoreFlags":["[skip ci]"]}],"options":{"concurrencyPolicy":"allow","paused":false},"gitops":{"vcsService":"github","accountLogin":"github-user","repoUrl":"https://github.com/northflank-examples/remix-postgres-redis-demo","branch":"main","filePath":"/Dockerfile"},"richInputs":[{"kind":"BranchCommitSelector","spec":{"required":false,"inputs":{"source":"build-service"},"outputs":{"branch":"TARGET_BRANCH","buildSha":"TARGET_COMMIT"}}}]}
headers = {"Content-Type": "application/json", "Authorization": "Bearer NORTHFLANK_API_TOKEN"}

response = requests.request("POST", url, headers = headers, json = payload)

print(response.json())
```

```go
package main

import (
  "bytes"
  "fmt"
  "io/ioutil"
  "net/http"
)

func main() {
  url := "https://api.northflank.com/v1/projects/{projectId}/pipelines/{pipelineId}/release-flows/{stage}"

  var jsonStr = []byte(`{"triggers":[{"vcsService":"github","accountLogin":"github-user","repoUrl":"https://github.com/northflank-examples/remix-postgres-redis-demo","pathIgnoreRules":["README.md"],"ciIgnoreFlags":["[skip ci]"]}],"options":{"concurrencyPolicy":"allow","paused":false},"gitops":{"vcsService":"github","accountLogin":"github-user","repoUrl":"https://github.com/northflank-examples/remix-postgres-redis-demo","branch":"main","filePath":"/Dockerfile"},"richInputs":[{"kind":"BranchCommitSelector","spec":{"required":false,"inputs":{"source":"build-service"},"outputs":{"branch":"TARGET_BRANCH","buildSha":"TARGET_COMMIT"}}}]}`)
  req, err := http.NewRequest("POST", url, bytes.NewBuffer(jsonStr))
  req.Header.Set("Content-Type", "application/json")
  req.Header.Set("Authorization", "Bearer NORTHFLANK_API_TOKEN")

  client := &http.Client{}
  resp, err := client.Do(req)
  if err != nil {
    panic(err)
  }
  defer resp.Body.Close()

  fmt.Println("Response status:", resp.Status)
  fmt.Println("Response headers:", resp.Header)
  body, _ := ioutil.ReadAll(resp.Body)
  fmt.Println("Response body:", string(body))
}
```

### Example Response

200 OK: success

## CLI reference

$ northflank update release-flow

Options:

- `--projectId <projectId>`: ID of the project

- `--pipelineId <pipelineId>`: ID of the pipeline

- `--stage <stage>`: Stage of the pipeline

- `-f --file <file>`: Path to a JSON/YAML resource definition file

- `-i --input <definition>`: JSON/YAML resource definition string (takes precedence over --file)

- `--verbose `: Verbose output

- `--quiet `: No console output

- `-o --output <format>`: Output formatting 

```json
{
  "triggers": [
    {
      "vcsService": "github",
      "accountLogin": "github-user",
      "repoUrl": "https://github.com/northflank-examples/remix-postgres-redis-demo",
      "pathIgnoreRules": [
        "README.md"
      ],
      "ciIgnoreFlags": [
        "[skip ci]"
      ]
    }
  ],
  "options": {
    "concurrencyPolicy": "allow",
    "paused": false
  },
  "gitops": {
    "vcsService": "github",
    "accountLogin": "github-user",
    "repoUrl": "https://github.com/northflank-examples/remix-postgres-redis-demo",
    "branch": "main",
    "filePath": "/Dockerfile"
  },
  "richInputs": [
    {
      "kind": "BranchCommitSelector",
      "spec": {
        "required": false,
        "inputs": {
          "source": "build-service"
        },
        "outputs": {
          "branch": "TARGET_BRANCH",
          "buildSha": "TARGET_COMMIT"
        }
      }
    }
  ]
}
```

## JavaScript client reference

### Example request

Request body

```javascript
await apiClient.update.releaseFlow({
  parameters: {
    "projectId": "default-project",
    "pipelineId": "example-pipeline",
    "stage": "development"
  },
  data: {
    "triggers": [
      {
        "vcsService": "github",
        "accountLogin": "github-user",
        "repoUrl": "https://github.com/northflank-examples/remix-postgres-redis-demo",
        "pathIgnoreRules": [
          "README.md"
        ],
        "ciIgnoreFlags": [
          "[skip ci]"
        ]
      }
    ],
    "options": {
      "concurrencyPolicy": "allow",
      "paused": false
    },
    "gitops": {
      "vcsService": "github",
      "accountLogin": "github-user",
      "repoUrl": "https://github.com/northflank-examples/remix-postgres-redis-demo",
      "branch": "main",
      "filePath": "/Dockerfile"
    },
    "richInputs": [
      {
        "kind": "BranchCommitSelector",
        "spec": {
          "required": false,
          "inputs": {
            "source": "build-service"
          },
          "outputs": {
            "branch": "TARGET_BRANCH",
            "buildSha": "TARGET_COMMIT"
          }
        }
      }
    ]
  }    
});
```

Previous: [Get release flow](/docs/v1/api//project/pipelines/get-release-flow)

Next: [Run release flow](/docs/v1/api//project/pipelines/run-release-flow)