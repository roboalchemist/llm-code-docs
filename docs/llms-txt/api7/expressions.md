# Source: https://docs.api7.ai/enterprise/3.2.16.7/reference/expressions.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/reference/expressions.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/reference/expressions.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/reference/expressions.md

# Source: https://docs.api7.ai/enterprise/reference/expressions.md

# Source: https://docs.api7.ai/enterprise/3.8.x/reference/expressions.md

# Source: https://docs.api7.ai/enterprise/3.7.x/reference/expressions.md

# Source: https://docs.api7.ai/enterprise/3.6.x/reference/expressions.md

# Source: https://docs.api7.ai/enterprise/3.5.x/reference/expressions.md

# Source: https://docs.api7.ai/enterprise/3.4.x/reference/expressions.md

# Source: https://docs.api7.ai/enterprise/3.3.x/reference/expressions.md

# API7 Expressions

*API7 Expressions* are combinations of variables, operators, and values that can be evaluated to a result, such as a Boolean value, `true` or `false`. Expressions can be used in configurations for route matching, request filtering, selective plugin applications, log enrichment, and more.

API7 Enterprise supports the evaluation of comparison operators and logical operators, as well as [regular expressions (RegEx)](https://www.pcre.org).

## Comparison Operators[â](#comparison-operators "Direct link to Comparison Operators")

API7 Enterprise supports the following comparison operators to be used with [built-in variables](https://docs.api7.ai/enterprise/3.3.x/reference/built-in-variables.md) in expressions:

| **Operator** | **Description**                     | **Example**                                                        |
| ------------ | ----------------------------------- | ------------------------------------------------------------------ |
| `==`         | equal                               | `["arg_version", "==", "v2"]`                                      |
| `~=`         | not equal                           | `["arg_version", "~=", "v2"]`                                      |
| `>`          | greater than                        | `["arg_ttl", ">", 3600]`                                           |
| `>=`         | greater than or equal to            | `["arg_ttl", ">=", 3600]`                                          |
| `<`          | less than                           | `["arg_ttl", "<", 3600]`                                           |
| `<=`         | less than or equal to               | `["arg_ttl", "<=", 3600]`                                          |
| `~~`         | match RegEx                         | `["arg_env", "~~", "[Dd]ev"]`                                      |
| `~*`         | match RegEx (case-insensitive)      | `["arg_env", "~*", "dev"]`                                         |
| `in`         | exist in the right-hand side        | `["arg_version", "in", ["v1","v2"]]`                               |
| `has`        | contain item in the right-hand side | `["graphql_root_fields", "has", "owner"]`                          |
| `!`          | reverse the adjacent operator       | `["arg_env", "!", "~~", "[Dd]ev"]`                                 |
| `ipmatch`    | match IP address                    | `["remote_addr", "ipmatch", ["192.168.102.40", "192.168.3.0/24"]]` |

## Logical Operators[â](#logical-operators "Direct link to Logical Operators")

API7 Enterprise supports the following logical operators:

| **Operator** | **Explanation**                                    |
| ------------ | -------------------------------------------------- |
| `AND`        | `AND(A,B)` is true if both A and B are true.       |
| `OR`         | `OR(A,B)` is true if either A or B is true.        |
| `!AND`       | `!AND(A,B)` is true if either A or B is false.     |
| `!OR`        | `!OR(A,B)` is true only if both A and B are false. |

You can use logical operators to combine multiple expressions for evaluation, such as the following:

```
[
    "AND",
    ["arg_version", "==", "v2"],
    [
        "OR",
        ["arg_action", "==", "signup"],
        ["arg_action", "==", "subscribe"]
    ]
]
```
