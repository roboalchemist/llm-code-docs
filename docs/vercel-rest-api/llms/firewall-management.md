# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/examples/firewall-management.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Vercel WAF Management

> Learn how to use the Vercel SDK through real-life examples.

## Add custom rules

In this example, you create a new custom rule to protect your application against SQL injection threats.

```ts run.ts theme={"system"}
import { Vercel } from '@vercel/sdk';

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function insertCustomRule() {
  await vercel.security.updateFirewallConfig({
    projectId: "your-project-id",
    teamId: "your-team-id", //Not required but sometimes needed if the endpoint requires that you authenticate as a specific team - your token should also have access to this scope
    requestBody: {
      action: "rules.insert",
      id: null, // null for new rules
      value: {
        active: true,
        name: "Block SQL Injection Attempts",
        description: "Block requests with SQL injection patterns in query parameters",
        conditionGroup: [
          {
            conditions: [
              {
                op: "inc", // Contains
                type: "query",
                value: "SELECT",
              },
            ],
          },
        ],
        action: {
          mitigate: {
            action: "deny",
            rateLimit: null,
            redirect: null,
            actionDuration: null,
          },
        },
      },
    },
  });
}

insertCustomRule()
```

## Modify existing rules

In this example, you update an existing custom rule's configuration. This is useful When you need to programmatically adjust conditions, actions, or status of an existing rule.

```ts run.ts theme={"system"}
import { Vercel } from "@vercel/sdk";

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function updateExistingRule() {
  await vercel.security.updateFirewallConfig({
    projectId: "your-project-id",
    teamId: "your-team-id", //Not required but sometimes needed if the endpoint requires that you authenticate as a specific team - your token should also have access to this scope
    requestBody: {
      action: "rules.update",
      id: "existing-rule-id", //You can find the id by using the rules array of the Read Firewall Configuration endpoint
      value: {
        active: true,
        name: "Updated Rule Name",
        description: "Updated rule description",
        conditionGroup: [
          {
            conditions: [
              {
                op: "pre",
                type: "path",
                value: "/admin",
              },
            ],
          },
        ],
        action: {
          mitigate: {
            action: "challenge", // Changed from previous setting
            rateLimit: null,
            redirect: null,
            actionDuration: null,
          },
        },
      },
    },
  });
}

updateExistingRule()
```

## Delete custom rules

In this example, you delete an existing custom rule.

```ts run.ts theme={"system"}
import { Vercel } from "@vercel/sdk";

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function deleteRule() {
  await vercel.security.updateFirewallConfig({
    projectId: "your-project-id",
    teamId: "your-team-id", //Not required but sometimes needed if the endpoint requires that you authenticate as a specific team - your token should also have access to this scope
    requestBody: {
      action: "rules.remove",
      id: "rule-to-delete-id", //You can find the id by using the rules array of the Read Firewall Configuration endpoint
      value: null, // No value needed for deletion
    },
  });
}

deleteRule()
```

## Change rule priority

This parameter applies when you have more than one custom rule in your project. By default, the priority is determined based on the order in which the rules are added. You can change this in the Vercel dashboard by re-ordering the rules in the [Firewall Configure](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules#custom-rule-configuration) project page **or** by using the endpoint below.

```ts run.ts theme={"system"}
import { Vercel } from "@vercel/sdk";

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function reorderRules() {
  await vercel.security.updateFirewallConfig({
    projectId: "your-project-id",
    teamId: "your-team-id", //Not required but sometimes needed if the endpoint requires that you authenticate as a specific team - your token should also have access to this scope
    requestBody: {
      action: "rules.priority",
      id: "rule-to-update-priority-id", //You can find the id by using the rules array of the Read Firewall Configuration endpoint
      value: 1, //Use the rules array of the Read Firewall Configuration endpoint to determine what array position you would like this rule to move to. The minimum is 0 and the maximum is the length of the array
    },
  });
}

reorderRules()

```

## Custom system bypass rule

The [WAF system bypass rules](https://vercel.com/docs/vercel-firewall/vercel-waf/system-bypass-rules) allow you to have specific IP addresses or CIDRs bypass the system-level mitigations such as [DDoS Mitigation](https://vercel.com/docs/vercel-firewall/ddos-mitigation). For more complex filters, you can use REST API directly.

For example, to allow mobile applications to bypass the system-level mitigations, use the following code to create a [Custom Rule](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules) in your project. This condition will match mobile devices as well as other clients that emit mobile `user_agent` values.

<Note>
  Bypassing system-level mitigations with the API is currently in beta. Contact [support](https://vercel.com/help) if you would like to use it.
</Note>

```ts run.ts theme={"system"}
import { Vercel } from "@vercel/sdk";

const vercel = new Vercel({
  bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
});

async function run() {
  const result = await vercel.security.updateFirewallConfig({
    projectId: "<your_project_id>",
    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
    requestBody: {
      action: "rules.insert",
      id: null,
      value: {
        name: "Mobile App Bypass Security Rule",
        description: "Custom system bypass rule targeting mobile applications",
        active: true,
        conditionGroup: [
          {
            conditions: [
              {
                type: "user_agent",
                op: "re",
                neg: false,
                value: "Mobile|Android|iPhone|iPad"
              }
            ]
          }
        ],
        action: {
          mitigate: {
            action: "bypass",
            bypassSystem: true
          }
        }
      }
    },
  });

  // Handle the result
  console.log(result);
}

run();
```

## Update an OWASP rule

In this example, you update a specific rule from the [OWASP ruleset](https://vercel.com/docs/vercel-firewall/vercel-waf/managed-rulesets#configure-owasp-core-ruleset) in your project using `crs.update`. You specify the rule to update by using its name in the `id` field.

```ts run.ts theme={"system"}
import { Vercel } from "@vercel/sdk";

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function updateOwaspRule() {
  await vercel.security.updateFirewallConfig({
    projectId: "your-project-id",
    teamId: "your-team-id", // Not required in all cases
    requestBody: {
      action: "crs.update",
      id: "xss", // eg. "sd", "max", "lfi", "rfi", "rce", "php", "gen", "xss", "sqli", "sf", "java"
      value: {
        active: true, // Enable the rule
        action: "log", // e.g. "deny" | "log" 
      },
    },
  });
}

updateOwaspRule()
```

## Disable all OWASP rules

This example disables all [OWASP rules](https://vercel.com/docs/vercel-firewall/vercel-waf/managed-rulesets#configure-owasp-core-ruleset) for the project. It is a shortcut equivalent to setting every OWASP rule to `active = false`.

```ts run.ts theme={"system"}
import { Vercel } from "@vercel/sdk";

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function disableOWASPRules() {
  await vercel.security.updateFirewallConfig({
    projectId: "your-project-id",
    teamId: "your-team-id", // Not required in all cases
    requestBody: {
      action: "crs.disable",
      id: null,
      value: null,
    },
  });
}

disableOWASPRules()
```

## Update a managed ruleset

Use `managedRules.update`  with the ruleset name as `id` to enable/disable the ruleset and update the firewall action for that [managed ruleset](https://vercel.com/docs/vercel-firewall/vercel-waf/managed-rulesets) for the project.

```ts run.ts theme={"system"}
import { Vercel } from "@vercel/sdk";

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function updateManagedRuleset() {
  await vercel.security.updateFirewallConfig({
    projectId: "your-project-id",
    teamId: "your-team-id", // Not required in all cases
    requestBody: {
      action: "managedRules.update",
      id: "bot_protection", // eg. "owasp", "bot_protection", "ai_bots", "bot_filter"
      value: {
        active: true, // Enable the ruleset
        action: "log", // e.g. "deny" | "log" | "challenge"
      },
    },
  });
}

updateManagedRuleset()
```
