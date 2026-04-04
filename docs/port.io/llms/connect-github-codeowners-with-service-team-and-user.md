# Source: https://docs.port.io/guides/all/connect-github-codeowners-with-service-team-and-user.md

# Connect GitHub CODEOWNERS with Repository, Team & User

This guide demostrates how to map CODEOWNERS file in GitHub to their respective GitHub repositories, GitHub teams and GitHub user blueprints in Port.

Available Github Integrations

This guide includes one or more steps that require integration with GitHub.<br /><!-- -->Port supports two GitHub integrations:

* **GitHub (Legacy)** - uses a GitHub app, which is soon to be deprecated.
* **GitHub (Ocean)** - uses the [Ocean framework](/build-your-software-catalog/sync-data-to-catalog/git/github-ocean/installation/.md), recommended for new integrations.

Both integration options are present in this guide via tabs, choose the one that fits your needs.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

* A Port account.

- GitHub (Legacy)
- GitHub (Ocean)

* Install [Port's GitHub app](/build-your-software-catalog/sync-data-to-catalog/git/github/.md#setup) in your organization or in repositories you are interested in.

Default Github Blueprints

Once you install Port's GitHub app, the following blueprints will be automatically created in your data model: `Repository`, `Pull Request`, `Github User`, `Github Team`.

* Install [GitHub ocean](/build-your-software-catalog/sync-data-to-catalog/git/github-ocean/installation/.md).

Default Github Blueprints

Once you install GitHub ocean, the following blueprints will be automatically created in your data model: `Repository`, `Pull Request`, `Github User`, `Github Team`.

## Set up data model[â](#set-up-data-model "Direct link to Set up data model")

First, let's create the necessary [blueprint]() to store the Codeowners data, then we will set up the mapping configuration.

### Create the Codeowners blueprint[â](#create-the-codeowners-blueprint "Direct link to Create the Codeowners blueprint")

To add the CODEOWNERS blueprint:

1. Navigate to your [data model](https://app.getport.io/settings/data-model) page of your portal.

2. Click on the `+ Blueprint` button.

3. Click on the `Edit JSON` button.

4. Copy the following definition and paste it in the editor, then click `Save`:

   **CODEOWNERS blueprint (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "githubCodeowners",
     "description": "This blueprint represents a CODEOWNERS file in a service",
     "title": "Github Codeowners",
     "icon": "Github",
     "schema": {
       "properties": {
         "location": {
           "type": "string",
           "title": "File location",
           "description": "File path to CODEOWNERS file"
         },
         "scope": {
           "icon": "DefaultProperty",
           "type": "string",
           "title": "Scope",
           "description": "The scope which the user/team owns."
         }
       },
       "required": []
     },
     "mirrorProperties": {},
     "calculationProperties": {},
     "aggregationProperties": {},
     "relations": {
       "users": {
         "title": "Users",
         "target": "githubUser",
         "required": false,
         "many": true
       },
       "teams": {
         "title": "Teams",
         "target": "githubTeam",
         "required": false,
         "many": true
       },
       "repository": {
         "title": "Repository",
         "description": "The repository which the CODEOWNERS file resides in",
         "target": "githubRepository",
         "required": true,
         "many": false
       }
     }
   }
   ```

### Set up mapping configuration[â](#set-up-mapping-configuration "Direct link to Set up mapping configuration")

* GitHub (Legacy)
* GitHub (Ocean)

1. Go to the [data sources](https://app.getport.io/settings/data-sources) page of your portal.

2. Under `Exporters`, click on your desired GitHub organization.

3. A window will open containing the default YAML configuration of your GitHub integration.

4. In the bottom-left corner you can modify the configuration to suit your needs, by adding/removing entries.

5. Copy the following configuration and paste it in the editor, then click `Save & Resync`:

   **CODEOWNERS mapping configuration (Click to expand)**

   ```
   resources:
     - kind: file
       selector:
         query: .repo.archived == false
         files:
           - path: '**/.github/CODEOWNERS'
       port:
         itemsToParse: >-
           (. as $root | .file.content | split("\n") | map(trim) |
           map(select((test("^[[:space:]]*#") | not) and (length > 0))) | map(
               (split(" ") | map(select(length > 0))) as $tokens
               | {
                   scope: ($tokens[0]), 
                   # Replacing ** and * characters since the identifier can't contain special characters
                   identifier: ($tokens[0] 
                             | gsub("\\*\\*"; "doublestar")
                             | gsub("\\*"; "star")),
                   # Extracting users and teams to their respective arrays
                   users: (
                       $tokens[1:]
                       | map(select(contains("/") | not)
                               | gsub("@" ; "")
                             )
                     ),
                   teams: (
                       $tokens[1:]
                       | map(select(test("^@[^ ]+/[^ ]+$"))
                             | split("/")
                             | .[-1]
                 ))
               }
               )
             )
         entity:
           mappings:
             identifier: .repo.full_name + "_" +.item.identifier + "_codeowners"
             title: .item.scope + " codeowners"
             blueprint: '"githubCodeowners"'
             properties:
               scope: .item.scope
               location: .file.path
             relations:
               repository: .repo.full_name
               teams: 
                 combinator: '''and'''
                 rules:
                   - property: '"$title"'
                     value: .item.teams
                     operator: '"in"'
               users: .item.users
   ```

1) Go to the [data sources](https://app.getport.io/settings/data-sources) page of your portal.

2) Under `Exporters`, click on your installed GitHub ocean integration.

3) A window will open containing the default YAML configuration of your GitHub ocean integration.

4) In the bottom-left corner you can modify the configuration to suit your needs, by adding/removing entries.

5) Copy the following configuration and paste it in the editor, then click `Save & Resync`:

   **CODEOWNERS mapping configuration (Click to expand)**

   ```
   resources:
     - kind: file
       selector:
         query: .repository.archived == false
         files:
           - path: '**/.github/CODEOWNERS'
       port:
         itemsToParse: >-
           (. as $root | .content | split("\n") | map(trim) |
           map(select((test("^[[:space:]]*#") | not) and (length > 0))) | map(
               (split(" ") | map(select(length > 0))) as $tokens
               | {
                   scope: ($tokens[0]), 
                   # Replacing ** and * characters since the identifier can't contain special characters
                   identifier: ($tokens[0] 
                             | gsub("\\*\\*"; "doublestar")
                             | gsub("\\*"; "star")),
                   # Extracting users and teams to their respective arrays
                   users: (
                       $tokens[1:]
                       | map(select(contains("/") | not)
                               | gsub("@" ; "")
                             )
                     ),
                   teams: (
                       $tokens[1:]
                       | map(select(test("^@[^ ]+/[^ ]+$"))
                             | split("/")
                             | .[-1]
                 ))
               }
               )
             )
         entity:
           mappings:
             identifier: .repository.full_name + "_" +.item.identifier + "_codeowners"
             title: .item.scope + " codeowners"
             blueprint: '"githubCodeowners"'
             properties:
               scope: .item.scope
               location: .path
             relations:
               repository: .repository.name
               teams: 
                 combinator: '''and'''
                 rules:
                   - property: '"$title"'
                     value: .item.teams
                     operator: '"in"'
               users: .item.users
   ```

## Example[â](#example "Direct link to Example")

For the following `CODEOWNERS` file example:

**CODEOWNERS file example (Click to expand)**

```
# Default owner for all files in the repo
*                @sivanelk97 @sivan27

# Backend ownership
/backend/         @sivanelk97 @sivan-org/backend-team @sivan-org/docs-team

# Frontend ownership (multiple owners)
/frontend/        @sivanelk97

# Specific file
/README.md        @sivanelk97

# JavaScript files in any folder
**/*.js           @sivanelk97

# Terraform files anywhere
**/*.tf          @sivanelk97

# CI/CD workflows
.github/workflows/  @sivanelk97

# Config files named 'config.yaml' in any folder
**/config.yaml    @sivanelk97

# Markdown documentation files
*.md              @sivanelk97 @sivan27 @sivan-org/docs-team
```

The [software catalog](https://app.getport.io/organization/catalog) **Codeowners page** should display the corresponding Codeowners entities:

![](/img/build-your-software-catalog/custom-integration/api/ci-cd/github-workflow/guides/gitHubCodeownersAfterIngestionIntoPort.png)

<br />
