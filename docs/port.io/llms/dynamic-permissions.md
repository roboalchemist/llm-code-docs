# Source: https://docs.port.io/actions-and-automations/create-self-service-experiences/set-self-service-actions-rbac/dynamic-permissions.md

# Dynamic permissions

Dynamic permissions allow you to control who can execute or approve self-service actions based on data in your software catalog. Unlike static permissions, where you explicitly list roles, users, or teams, dynamic permissions let you define logic that evaluates at runtime.

This enables access control patterns such as requiring manager approval, restricting actions based on entity ownership, or enforcing separation of duties.

## Common use cases[â](#common-use-cases "Direct link to Common use cases")

* Ensure that action executions requested by a team member can only be approved by his/her direct manager.
* Perform validations/manipulations on inputs that depend on data from related entities.
* Ensure that only those who are on-call can perform rollbacks of a service with issues.
* Allow service owners to modify their own infrastructure freely, but also enforce approval when they seek to make changes to infrastructure shared by multiple services.

## How it works[â](#how-it-works "Direct link to How it works")

Dynamic permissions are configured using a `policy` object in the action's permissions JSON. The policy requires two keys:

* `queries` - Fetch entities from your software catalog based on rules you define.
* `conditions` - JQ expressions that evaluate the query results.

Both keys must be present in the policy object.

**When a `policy` is defined:**

* The `roles`, `users`, and `teams` keys control who can **see** the action.
* The `policy` exclusively controls who can **execute** or **approve** the action.

**When no `policy` is defined:**

* The `roles`, `users`, and `teams` keys control both visibility and execution/approval.

### Evaluation order[â](#evaluation-order "Direct link to Evaluation order")

Dynamic permissions are evaluated **after** [blueprint permissions](/sso-rbac/rbac-overview/.md). This means:

1. Port first checks if the user has the required permissions on the underlying blueprint.
2. Only if the blueprint permissions allow access, the dynamic permission policy is evaluated.

Dynamic permissions can only **further restrict** who can execute or approve an action, or **dynamically determine approvers**. They cannot bypass blueprint-level restrictions.

## Configuration[â](#configuration "Direct link to Configuration")

Dynamic permissions are defined in the action's permissions JSON. This section covers how to access and structure the configuration.

### Accessing the permissions JSON[â](#accessing-the-permissions-json "Direct link to Accessing the permissions JSON")

To define dynamic permissions for an action:

1. Go to the [Self-service](https://app.getport.io/self-serve) page of your portal.
2. Hover over the desired action, click on the `...` icon in its top-right corner, and choose `Edit`.
3. Click on the `Edit JSON` button in the top-right corner of the configuration modal, then choose the `Permissions` tab.

### The policy object structure[â](#the-policy-object-structure "Direct link to The policy object structure")

The permissions JSON contains two top-level keys:

* `"execute"` - defines who can **run** the action.
* `"approve"` - defines who can **approve** the action (only relevant if [manual approval](/actions-and-automations/create-self-service-experiences/set-self-service-actions-rbac/.md#configure-manual-approval-for-actions) is enabled).

Under each of these keys, you can define:

* `roles` - which roles can execute/approve the action.

* `users` - which specific users can execute/approve the action.

* `teams` - which teams can execute/approve the action.

* `policy` - dynamic logic containing:

  <!-- -->

  * [`queries`](/search-and-query/structure-and-syntax.md) - [rules](/search-and-query/structure-and-syntax.md#rules) to fetch entities from your catalog.
  * `conditions` - JQ expressions that determine access. Multiple conditions are evaluated with an implicit "OR".

**Note** that to remove an existing policy, set `"policy": null` in the JSON configuration. Simply deleting the policy content will not remove it.

The following example shows the complete structure of a policy object:

**Complete policy structure example (click to expand)**

```
{
  "execute": {
    "policy": {
      "queries": {
        "query_name": {
          "rules": [
              // Your rule/s logic here
            ],
            "combinator": "and"
        }
      },
      "conditions": [
        // A jq query resulting in a boolean value (allowed/not-allowed to execute)
      ]
    }
  },
  "approve": {
    "roles": [
      "Admin"
    ],
    "users": [],
    "teams": [],
    "policy": {
      "queries": {
        "query_name": {
          "rules": [
              // Your rule/s logic here
            ],
            "combinator": "and"
        }
      },
      "conditions": [
        // A jq query resulting in an array of strings (a list of users who can approve the action)
      ]
    }
  }
}
```

### How policy affects visibility vs execution[â](#how-policy-affects-visibility-vs-execution "Direct link to How policy affects visibility vs execution")

When no `policy` is defined, `roles`, `users`, and `teams` control both visibility **and** execution/approval permissions. When a `policy` is defined, `roles`, `users`, and `teams` control only **visibility**, while the `policy` exclusively controls **execution** or **approval**.

**Example without policy:**

The action is visible and executable by users with the `admin` role or members of the `engineering` team:

```
"execute": {
  "roles": ["admin"],
  "users": [],
  "teams": ["engineering"]
}
```

**Example with policy:**

Using the same configuration, but this time with a `policy` object defined, these `roles` and `teams` only determine who can view the action, while the `policy` exclusively controls who can **execute** or **approve** it.

In the following example, the action will be visible to `admin` and `engineering` team members, but its execution permissions depend only on whether the `policy` conditions evaluate to `true`:

```
"execute": {
  "roles": ["admin"],
  "users": [],
  "teams": ["engineering"],
  "policy": {
    "queries": {
      "example_query": {
        "rules": [
          // Your rule logic here
        ],
        "combinator": "and"
      }
    },
    "conditions": [
      // A jq query returning a boolean (allowed/not-allowed to execute)
    ]
  }
}
```

### Condition return types[â](#condition-return-types "Direct link to Condition return types")

The `conditions` array in a policy behaves differently depending on whether it's used for **execute** or **approve** permissions: execute conditions return a **boolean**, while approve conditions return an **array of email addresses**.

* Execute conditions
* Approve conditions

Execute conditions must return a **boolean** value (`true` or `false`).

* `true` â the user **can** execute the action.
* `false` â the user **cannot** execute the action.

**Example condition:**

```
"conditions": [
  ".results.search_entity.entities | length == 0"
]
```

This condition checks if the query returned zero entities. Execution is allowed only in that case.

Approve conditions must return an **array of strings** containing the **email addresses** of users who can approve the action.

* The array must contain **email addresses**, not user IDs. Fields like `createdBy` or `updatedBy` return user IDs, which will silently fail to match any approvers.
* An empty array means no one can approve.

**Example condition:**

```
"conditions": [
  "[.results.approvingUsers.entities[] | select(.relations.team == $executerTeam) | .identifier]"
]
```

This condition returns an array of user emails who are on the same team as the executor.

### Query-condition evaluation flow[â](#query-condition-evaluation-flow "Direct link to Query-condition evaluation flow")

The `policy` object uses two keys that work together:

**`queries`** - Fetch data from your software catalog using [Port's search syntax](/search-and-query/structure-and-syntax.md). Each query:

* Has a name (e.g., `executingUser`, `serviceOwners`) that you choose.
* Contains `rules` that filter entities (similar to catalog search).
* Supports `{{ .inputs.fieldName }}` and `{{ .trigger.user.email }}` templating.
* Results are stored in `.results.<query_name>.entities` for use in conditions.

**`conditions`** - Evaluate the fetched data using JQ expressions to make the final decision. Each condition:

* Has access to query results via `.results.<query_name>.entities`.
* Has access to metadata like `.trigger.user`, `.inputs`, `.entity`, etc.
* Must return a boolean (for execute) or array of email strings (for approve).
* Multiple conditions have an implicit OR between them.

**How they work together:**

1. QUERIES run first

   * Fetch entities from catalog based on rules
   * Results stored in `.results.<query_name>.entities`

2. CONDITIONS evaluate the results

   * JQ expressions process .results + metadata
   * Return boolean (execute) or email array (approve)

**Example breakdown:**

```
"policy": {
  "queries": {
    "serviceOwners": {                    // Query name (you choose this)
      "rules": [
        {
          "property": "$blueprint",
          "operator": "=",
          "value": "_user"                // Fetch from _user blueprint
        },
        {
          "property": "teams",
          "operator": "contains",
          "value": "{{ .entity.relations.owning_team }}"  // Template: team from entity
        }
      ],
      "combinator": "and"
    }
  },
  "conditions": [                         // JQ expressions using query results
    ".trigger.user.email as $user | .results.serviceOwners.entities | map(.identifier) | any(. == $user)"
  ]
}
```

This example:

1. **Query** fetches all users who belong to the entity's owning team.
2. **Condition** checks if the executing user's email is in that list (returns `true`/`false`).

### Available context variables[â](#available-context-variables "Direct link to Available context variables")

When writing JQ conditions, you have access to the action's [trigger data](/actions-and-automations/create-self-service-experiences/setup-the-backend/.md#trigger-data) - the same context available when defining backend payloads.

**Commonly used in conditions:**

| Variable                         | Description                                         |
| -------------------------------- | --------------------------------------------------- |
| `.trigger.user.email`            | Email of the user who triggered the action          |
| `.inputs.<field_name>`           | Values provided by the user for action inputs       |
| `.entity`                        | The entity being acted on (DAY-2/DELETE operations) |
| `.results.<query_name>.entities` | Array of entities returned by your queries          |

Query results

Access query results using `.results.<query_name>.entities`. Each entity contains `.identifier`, `.title`, `.properties.*`, and `.relations.*`.

## Troubleshooting[â](#troubleshooting "Direct link to Troubleshooting")

Dynamic permissions can be challenging to debug because there's limited visibility into what's happening at runtime. Here are strategies to diagnose common issues.

### Common issues[â](#common-issues "Direct link to Common issues")

**Policy not working at all (click to expand)**

**Check blueprint permissions first.** Dynamic permissions are evaluated *after* blueprint permissions. If the user doesn't have the required blueprint permissions, the policy won't even be evaluated.

To verify:

1. Temporarily remove the `policy` object from the permissions JSON.
2. Test if the user can execute the action with just `roles`/`users`/`teams`.
3. If they still can't, the issue is with blueprint permissions, not your policy.

**No approvers appear for approval policy (click to expand)**

This usually means your condition is returning user **IDs** instead of **email addresses**. Approve conditions must return an array of email addresses.

Common culprits:

* Using `.createdBy` or `.updatedBy` (these return user IDs, not emails)
* Using `.identifier` on a user entity when the identifier is an ID rather than an email

**Fix:** If your user entities use email as the identifier, use `.identifier`. If not, you need to access the email from a property, e.g., `.properties.email`.

**JQ condition syntax errors (click to expand)**

JQ syntax errors cause conditions to fail silently. Test your JQ expressions locally before adding them to Port.

**Test JQ locally:**

1. Create a file with sample context data (e.g., `test-data.json`)
2. Run your expression: `jq '<your_expression>' test-data.json`

**Common JQ mistakes:**

* Missing quotes around strings
* Using `=` instead of `==` for comparison
* Forgetting to handle empty arrays (use `// []` for defaults)

### Testing queries with the search API[â](#testing-queries-with-the-search-api "Direct link to Testing queries with the search API")

You can test your query rules using Port's [search API](/api-reference/search-entities.md) before adding them to a policy. This helps verify that your rules return the expected entities.

The query structure in dynamic permissions is identical to the search API request body:

```
// In your policy:
"queries": {
  "my_query": {
    "rules": [...],
    "combinator": "and"
  }
}

// Equivalent Search API request body:
{
  "rules": [...],
  "combinator": "and"
}
```

Template variables

When testing, remember that template variables like `{{ .inputs.name }}` won't work in the API - you will need to replace them with actual values.

## Limitations[â](#limitations "Direct link to Limitations")

* Each query can return up to **1000 entities**. Make your queries as precise as possible to stay within this limit.
* Any query that fails to evaluate will be **silently ignored**.
* Dynamically resolved approvers are only notified via the Port UI. Email notifications are **not** sent to them. To send email notifications, define approvers statically using the `users`, `roles`, or `teams` keys.
* There is no limit to the number of queries you can define per policy.

## Examples[â](#examples "Direct link to Examples")

See the [examples](/actions-and-automations/create-self-service-experiences/set-self-service-actions-rbac/dynamic-permissions/examples.md) page for practical implementations of dynamic permissions patterns.
