# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/policy-fix.md

# policyFix

Represents configuration and details for a policy-based fix.

### Examples

```graphql
type PolicyFix {
  settingType: String
  tooltip: String
  description: String
  warning: String
  confirmation: String
  inputs: [FixInput]
}
```

### Fields

| Field                                                                                                              | Description                                        | Supported fields                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| settingType `String`                                                                                               | Type of setting controlled by the policy fix       |                                                                                                                                                                                                                                                                         |
| tooltip `String`                                                                                                   | Tooltip text to describe the policy fix in the UI  |                                                                                                                                                                                                                                                                         |
| description `String`                                                                                               | Detailed description of the policy fix             |                                                                                                                                                                                                                                                                         |
| warning `String`                                                                                                   | Warning message related to applying the fix        |                                                                                                                                                                                                                                                                         |
| confirmation `String`                                                                                              | Confirmation message shown before applying the fix |                                                                                                                                                                                                                                                                         |
| inputs [`[FixInput]`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/fix-input) | List of inputs required to configure the fix       | <p>type <code>String</code><br>name <code>String</code><br>options <a href="fix-input-option"><code>\[FixInputOption]</code></a><br>multiSelect <code>Boolean</code><br>maxSelect <code>Int</code><br>minSelect <code>Int</code><br>displayName <code>String</code></p> |

### References

#### Fields with this object

* [{} Issue.fixes](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
