# Source: https://docs.port.io/workflows/examples.md

# Source: https://docs.port.io/search-and-query/examples.md

# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/terraform-cloud/examples.md

# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/project-management/jira/examples.md

# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/project-management/jira-server/examples.md

# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/incident-management/statuspage/examples.md

# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/incident-management/pagerduty/examples.md

# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/incident-management/opsgenie/examples.md

# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/git/gitlab/examples.md

# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/git/gitlab-v2/examples.md

# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/git/github/examples.md

# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/git/github-ocean/examples.md

# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/git/bitbucket/bitbucket-cloud/examples.md

# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/git/bitbucket/bitbucket-app/examples.md

# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/git/azure-devops/examples.md

# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/code-quality-security/wiz/examples.md

# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/code-quality-security/sonarqube/examples.md

# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/code-quality-security/checkmarx/examples.md

# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/cloud-providers/gcp/examples.md

# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws/examples.md

# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws/aws-exporter/examples.md

# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/apm-alerting/datadog/examples.md

# Source: https://docs.port.io/build-your-software-catalog/set-catalog-rbac/examples.md

# Source: https://docs.port.io/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/calculation-property/examples.md

# Source: https://docs.port.io/build-your-software-catalog/custom-integration/webhook/examples.md

# Source: https://docs.port.io/build-your-software-catalog/custom-integration/api/ci-cd/jenkins-deployment/examples.md

# Source: https://docs.port.io/build-your-software-catalog/custom-integration/api/ci-cd/gitlab-pipelines/examples.md

# Source: https://docs.port.io/build-your-software-catalog/custom-integration/api/ci-cd/github-workflow/examples.md

# Source: https://docs.port.io/build-your-software-catalog/custom-integration/api/ci-cd/codefresh-workflow-template/examples.md

# Source: https://docs.port.io/build-your-software-catalog/custom-integration/api/ci-cd/circleci-workflow/examples.md

# Source: https://docs.port.io/build-your-software-catalog/custom-integration/api/ci-cd/azure-pipelines/examples.md

# Source: https://docs.port.io/actions-and-automations/define-automations/examples.md

# Source: https://docs.port.io/actions-and-automations/create-self-service-experiences/set-self-service-actions-rbac/dynamic-permissions/examples.md

# Examples

The following examples demonstrate common patterns for dynamic permissions.

## Forbid execution if entity exists[â](#forbid-execution-if-entity-exists "Direct link to Forbid execution if entity exists")

Let's take a look at the following scenario: Say we have an action that scaffolds a new microservice, and as a result creates an entity in our software catalog representing that service. Now say we want to ensure that execution of this action will be blocked if the provided service name already exists in our catalog.

Here is an example of a permissions JSON that achieves this:

**Full permissions JSON (click to expand)**

```
{
  "execute": {
    // the next three keys allow users to specify roles, specific users, and specific teams that may execute this action
    "roles": ["Member", "Admin"],
    "users": [],
    "teams": [],
    "ownedByTeam": false, // declares ownership of the action by a team, if desired
    "policy": {
      "queries": {
        "search_entity": {
          "rules": [
            // fetch all entities created from the "service" blueprint
            {
              "value": "service",
              "operator": "=",
              "property": "$blueprint"
            },
            // fetch all entities whose identifier is equal to the name provided as an input in the action execution
            {
              "value": "{{ .inputs.name }}",
              "operator": "=",
              "property": "$identifier"
            }
          ],
          "combinator": "and"
        }
      },
      // if our rule results produced no entities, that means that a service with our desired name does not exist, so we can execute the action
      "conditions": [
        ".results.search_entity.entities | length == 0"
      ]
    }
  },
  "approve": {
    "roles": [
      "Admin"
    ],
    "users": [],
    "teams": []
  }
}
```

**Explanation**

The two rules that we defined fetch all `service` entities whose name is the same as the one provided to the action during execution. These rules will return an array of entities that comply with them. If no entities comply with the rules, the array will be empty. The `conditions` query checks if the resulting array is empty or not, and returns `true` or `false`, respectively. If the array is empty, that means that an entity with the provided name does not exist in our software catalog, so we can return `true` and allow the action execution.

***

## Team leader approval[â](#team-leader-approval "Direct link to Team leader approval")

In this example we create rules that state that execution of an action can be **approved** only by the team leader of the user that asked to execute the action.

**Note** that this example assumes that the relevant team leader has the `Moderator` role, as you can see in the `approvingUsers` section of the permissions JSON below.

The example contains two queries:

1. `executingUser` - fetches the user who executed the action.
2. `approvingUsers` - fetches the users who are allowed to approve the action.

The `condition` checks if the approver is the executer's team leader, via the relation between `user` and `team`.

**Full permissions JSON (click to expand)**

```
{
  "execute": {
    // the next three keys allow users to specify roles, specific users, and specific teams that may execute this action
    "roles": ["Member", "Admin"],
    "users": [],
    "teams": [],
    "ownedByTeam": false // declares ownership of the action by a team, if desired
    // a policy key may be added here, with queries and conditions within it
  },
  "approve": {
    "roles": [],
    "users": [],
    "teams": [],
    "policy": {
      "queries": {
        // executingUser is a custom query that returns an array of entities
        "executingUser": {
          "rules": [
            // fetches all users from user blueprint
            {
              "value": "_user",
              "operator": "=",
              "property": "$blueprint"
            },
            // filters all users from immediately previous query
            // to find only the user who executed the action
            {
              "value": "{{.trigger.user.email}}",
              "operator": "=",
              "property": "$identifier"
            }
          ],
          "combinator": "and" // both of the conditions above must be true
        },
        // approvingUsers is a custom query that returns an array of entities
        "approvingUsers": {
          "rules": [
            // fetches all users from user blueprint
            {
              "value": "_user",
              "operator": "=",
              "property": "$blueprint"
            },
            // fetches all users with the `Moderator` role
            {
              "value": "Moderator",
              "operator": "=",
              "property": "port_role"
            }
          ],
          "combinator": "and" // both of the conditions above must be true
        }
      },
      // see next section for description of what occurs in the jq query below
      "conditions": [
        "(.results.executingUser.entities | first | .relations.team) as $executerTeam | [.results.approvingUsers.entities[] | select(.relations.team == $executerTeam) | .identifier]"
      ]
    }
  }
}
```

**Explanation**

The `conditions` query uses the two arrays produced as a result of the `executingUser` and `approvingUsers` queries and returns an array of users who may approve the self-service action.

The query below filters the array produced by the `executingUser` query down to only the first element in the array, then further filters this array to show only the contents of the `.relations.team` key. This newly filtered array is saved as a variable (`$`) called `executerTeam`.

```
"(.results.executingUser.entities | first | .relations.team) as $executerTeam"
```

The next query (`.results.approvingUsers.entities[]`) takes the *entire* array from the `approvingUsers` query, then applies a filter to include *only* the approving users from that array who are on the same team as the executing user (`select(.relations.team == $executerTeam)`). Finally, the array is filtered to yield only an array of the `.identifier` property of all approvers, which Port then uses to *dynamically* evaluate who may approve this self-service action.

***

## Prevent self-approval[â](#prevent-self-approval "Direct link to Prevent self-approval")

In this example, we will implement a security best practice known as "segregation of duties" by ensuring that the user who executes an action cannot also approve it. This is particularly important for sensitive operations like production deployments, infrastructure changes, or permission modifications.

**Full permissions JSON (click to expand)**

```
{
  "execute": {
    "roles": ["Member", "Admin"],
    "users": [],
    "teams": [],
    "ownedByTeam": false
  },
  "approve": {
    "roles": [],
    "users": [],
    "teams": [],
    "policy": {
      "queries": {
        "approvingUsers": {
          "rules": [
            {
              "value": "_user",
              "operator": "=",
              "property": "$blueprint"
            },
            {
              "value": "Moderator",
              "operator": "=",
              "property": "port_role"
            }
          ],
          "combinator": "and"
        }
      },
      "conditions": [
        ".trigger.user.email as $executor | [.results.approvingUsers.entities[] | select(.identifier != $executor) | .identifier]"
      ]
    }
  }
}
```

**Explanation**

This configuration implements a "four-eyes principle", which requires that sensitive actions be verified by a second person before being executed.

Here's what's happening in each part:

1. **Execute Permissions**: Any user with either the `Member` or `Admin` role can execute this action.

2. **Approve Permissions**: The approval process is governed by a policy that:

   * Queries all users from the `_user` blueprint who have the `Moderator` role.
   * Uses a JQ condition to filter out the specific user who executed the action.

3. **The Key Condition**:

   ```
   ".trigger.user.email as $executor | [.results.approvingUsers.entities[] | select(.identifier != $executor) | .identifier]"
   ```

   This JQ expression:

   * Takes all moderator users from our query results.
   * Filters out any user whose identifier matches the email of the person who triggered the action.
   * Returns only the identifiers of the remaining users.

The result is a dynamic list of all users who are authorized to approve the action, excluding the original executor. This ensures that no single person can both initiate and approve a sensitive change, reducing the risk of unauthorized or accidental changes.

***

## Manager approval for team-owned entities[â](#manager-approval-for-team-owned-entities "Direct link to Manager approval for team-owned entities")

In this example, we ensure that actions on team-owned entities require approval from the manager of the owning team. This is useful when you want to enforce hierarchical approval for changes to resources owned by specific teams, such as infrastructure, services, or projects.

**Note** that this example assumes:

* Your software catalog has a `_team` blueprint with a `manager` relation pointing to user entities.
* Your entities have a `team` property or relation indicating ownership.
* **Important:** Replace `yourBlueprint` in the example below with your actual blueprint identifier (e.g., `service`, `environment`, `deployment`, etc.).

**Full permissions JSON (click to expand)**

```
{
  "execute": {
    "roles": ["Member", "Admin"],
    "users": [],
    "teams": [],
    "ownedByTeam": false
  },
  "approve": {
    "roles": [],
    "users": [],
    "teams": [],
    "policy": {
      "queries": {
        "allTeams": {
          "rules": [
            {
              "value": "_team",
              "operator": "=",
              "property": "$blueprint"
            }
          ],
          "combinator": "and"
        },
        "selectedEntity": {
          "rules": [
            {
              "value": "yourBlueprint",
              "operator": "=",
              "property": "$blueprint"
            },
            {
              "value": "{{ .entity.identifier }}",
              "operator": "=",
              "property": "$identifier"
            }
          ],
          "combinator": "and"
        }
      },
      "conditions": [
        "(.results.selectedEntity.entities | first | .team) as $entityTeams | [.results.allTeams.entities[] | select(.identifier as $teamId | $entityTeams | index($teamId)) | .relations.manager.identifier] | unique"
      ]
    }
  }
}
```

**Explanation**

This configuration requires that actions on team-owned entities be approved by the manager of the team that owns the entity.

Here's how it works:

1. **Execute Permissions**: Any user with the `Member` or `Admin` role can execute this action.

2. **Queries**:

   * `allTeams`: Fetches all team entities from the `_team` blueprint.
   * `selectedEntity`: Fetches the specific entity that the action is being performed on, using `{{ .entity.identifier }}` to reference the entity being acted upon. **Remember to replace `yourBlueprint` with your actual blueprint identifier.**

3. **The Condition**:

   ```
   "(.results.selectedEntity.entities | first | .team) as $entityTeams | [.results.allTeams.entities[] | select(.identifier as $teamId | $entityTeams | index($teamId)) | .relations.manager.identifier] | unique"
   ```

   This JQ expression:

   * Extracts the `team` property from the selected entity and stores it in the `$entityTeams` variable.
   * Iterates through all teams and filters to find those whose identifier matches the entity's team.
   * For each matching team, extracts the manager's identifier from the `manager` relation.
   * Returns a unique list of manager identifiers who can approve the action.

The result is that only the manager(s) of the team that owns the entity can approve actions performed on it, ensuring proper hierarchical oversight.

***

## Restrict execution to owning team members[â](#restrict-execution-to-owning-team-members "Direct link to Restrict execution to owning team members")

In this example, we restrict action execution to users who are members of the team that owns the service (for day-2 actions).

**Full permissions JSON (click to expand)**

```
{
  "execute": {
    "roles": ["Member", "Admin"],
    "users": [],
    "teams": [],
    "policy": {
      "queries": {
        "owningTeamMembers": {
          "rules": [
            {
              "property": "$blueprint",
              "operator": "=",
              "value": "_user"
            },
            {
              "property": "teams",
              "operator": "contains",
              "value": "{{ .entity.relations.owning_team }}"
            }
          ],
          "combinator": "and"
        }
      },
      "conditions": [
        ".trigger.user.email as $user | [.results.owningTeamMembers.entities[].identifier] | any(. == $user)"
      ]
    }
  },
  "approve": {
    "roles": ["Admin"],
    "users": [],
    "teams": []
  }
}
```

**Explanation**

This configuration ensures only team members who own the service can perform day-2 actions on it.

1. **Query**: Fetches all users from the `_user` blueprint whose `teams` property contains the owning team of the entity (accessed via `.entity.relations.owning_team`).

2. **Condition**: Checks if the executing user's email exists in the list of team member identifiers:

   * `.trigger.user.email as $user` - stores the executor's email.
   * `.results.owningTeamMembers.entities[].identifier` - gets all user emails from the query.
   * `any(. == $user)` - returns `true` if the executor is in the list.

Using entity data in queries

For day-2 actions, you can access the entity's properties and relations using `{{ .entity.properties.X }}` and `{{ .entity.relations.X }}` in your query rules. This allows you to create ownership-based permissions.
