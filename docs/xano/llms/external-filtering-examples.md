# Source: https://docs.xano.com/the-function-stack/functions/database-requests/query-all-records/external-filtering-examples.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# External Filtering Examples

## **Basic Equals Operation**

Checking if a user ID equals 1:

```json  theme={null}
{
  "expression": [{
    "statement": {
      "left": {
        "tag": "col",
        "operand": "users.id"
      },
      "op": "=",
      "right": {
        "operand": "1"
      }
    }
  }]
}
```

## **Between Operation**

Finding transactions with amount between 100 and 1000:

```json  theme={null}
{
  "expression": [{
    "statement": {
      "left": {
        "tag": "col",
        "operand": "transactions.amount"
      },
      "op": "between",
      "right": {
        "operand": ["100", "1000"]
      }
    }
  }]
}
```

## **Contains Operation**

Finding users with email containing '@company.com':

```json  theme={null}
{
  "expression": [{
    "statement": {
      "left": {
        "tag": "col",
        "operand": "users.email"
      },
      "op": "contains",
      "right": {
        "operand": "@company.com"
      }
    }
  }]
}
```

## **Multiple Conditions Example**

Finding active premium users who have made at least 5 purchases:

```json  theme={null}
{
  "expression": [
    {
      "statement": {
        "left": {
          "tag": "col",
          "operand": "users.status"
        },
        "op": "=",
        "right": {
          "operand": "active"
        }
      }
    },
    {
      "statement": {
        "left": {
          "tag": "col",
          "operand": "users.account_type"
        },
        "op": "=",
        "right": {
          "operand": "premium"
        }
      }
    },
    {
      "statement": {
        "left": {
          "tag": "col",
          "operand": "users.purchase_count"
        },
        "op": ">=",
        "right": {
          "operand": "5"
        }
      }
    }
  ]
}
```

## **Case-Insensitive Pattern Matching (ilike)**

Finding products with names starting with 'phone', regardless of case:

```json  theme={null}
{
  "expression": [{
    "statement": {
      "left": {
        "tag": "col",
        "operand": "products.name"
      },
      "op": "ilike",
      "right": {
        "operand": "phone%"
      }
    }
  }]
}
```

## **Array Membership (in)**

Finding orders with specific status values:

```json  theme={null}
{
  "expression": [{
    "statement": {
      "left": {
        "tag": "col",
        "operand": "orders.status"
      },
      "op": "in",
      "right": {
        "operand": ["pending", "processing", "shipped"]
      }
    }
  }]
}
```

## **Complex Multiple Conditions**

Finding high-value transactions (>1000) made in the last 30 days by premium users:

```json  theme={null}
{
  "expression": [
    {
      "statement": {
        "left": {
          "tag": "col",
          "operand": "transactions.amount"
        },
        "op": ">",
        "right": {
          "operand": "1000"
        }
      }
    },
    {
      "statement": {
        "left": {
          "tag": "col",
          "operand": "transactions.date"
        },
        "op": ">=",
        "right": {
          "operand": "2024-12-29"
        }
      }
    },
    {
      "statement": {
        "left": {
          "tag": "col",
          "operand": "users.account_type"
        },
        "op": "=",
        "right": {
          "operand": "premium"
        }
      }
    }
  ]
}
```

## Using And/Or

<Info>
  By default, all statements will be considered an 'and' statement, and nothing needs to be specified. You'll only need to specify whether `or` is `true` when you want to use it.

  For readability purposes, however, you can specify `or` is `false` if you'd like.

  The two examples below demonstrate this and would return the same result.
</Info>

```json  theme={null}
{
  "expression": [
    {
      "statement": {
        "left": {
          "tag": "col",
          "operand": "users.id"
        },
        "op": "=",
        "right": {
          "operand": "1"
        }
      }
    }
  ]
}
```

```json  theme={null}
// Verbose specification of "or"

{
  "expression": [
    {
      "or": false,
      "statement": {
        "left": {
          "tag": "col",
          "operand": "users.id"
        },
        "op": "=",
        "right": {
          "operand": "1"
        }
      }
    }
  ]
}
```

### Two Conditions Combined with OR

This example filters for users whose status is 'inactive' OR whose account type is 'basic'.

```json  theme={null}
{
  "expression": [
    {
      "statement": {
        "left": {
          "tag": "col",
          "operand": "users.status"
        },
        "op": "=",
        "right": {
          "operand": "inactive"
        }
      }
    },
    {
      "or": true,
      "statement": {
        "left": {
          "tag": "col",
          "operand": "users.account_type"
        },
        "op": "=",
        "right": {
          "operand": "basic"
        }
      }
    }
  ]
}
```

### Three Conditions with AND and OR

This example filters for active users AND (whose purchase count is less than 10 OR whose last login is before a specific date).

```json  theme={null}
{
  "expression": [
    {
      "statement": {
        "left": {
          "tag": "col",
          "operand": "users.status"
        },
        "op": "=",
        "right": {
          "operand": "active"
        }
      }
    },
    {
      "statement": {
        "left": {
          "tag": "col",
          "operand": "users.purchase_count"
        },
        "op": "<",
        "right": {
          "operand": "10"
        }
      }
    },
    {
      "or": true,
      "statement": {
        "left": {
          "tag": "col",
          "operand": "users.last_login"
        },
        "op": "<",
        "right": {
          "operand": "2024-01-01"
        }
      }
    }
  ]
}
```

### Using And/Or Groups - (Condition A AND Condition B) OR (Condition C AND Condition D)

Here's how the logic `(a = 1 AND b = 2) OR (a = 4 AND b = 5)` would be represented:

```json  theme={null}
{
    "expression": [
      {
        "or": false,
        "type": "group",
        "group": {
          "expression": [
            {
              "or": false,
              "statement": {
                "left": { "operand": "your_table.a" },
                "op": "=",
                "right": { "operand": "1" }
              },
              "type": "statement"
            },
            {
              "or": false,
              "statement": {
                "left": { "operand": "your_table.b" },
                "op": "=",
                "right": { "operand": "2" }
              },
              "type": "statement"
            }
          ]
        }
      },
      {
        "or": true,
        "type": "group",
        "group": {
          "expression": [
            {
              "or": false,
              "statement": {
                "left": { "operand": "your_table.a" },
                "op": "=",
                "right": { "operand": "4" }
              },
              "type": "statement"
            },
            {
              "or": false,
              "statement": {
                "left": { "operand": "your_table.b" },
                "op": "=",
                "right": { "operand": "5" }
              },
              "type": "statement"
            }
          ]
        }
      }
    ]
  }
```


Built with [Mintlify](https://mintlify.com).