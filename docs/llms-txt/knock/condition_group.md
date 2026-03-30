# Source: https://docs.knock.app/mapi-reference/workflows/schemas/condition_group.md

### ConditionGroup

A group of conditions to be evaluated.

#### Attributes

#### Example

```json
{
  "all": [
    {
      "argument": "some_property",
      "operator": "equal_to",
      "variable": "recipient.property"
    }
  ]
}
```

