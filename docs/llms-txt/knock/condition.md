# Source: https://docs.knock.app/mapi-reference/workflows/schemas/condition.md

# Source: https://docs.knock.app/api-reference/$shared/schemas/condition.md

### Condition

A condition to be evaluated.

#### Attributes

- **argument** (string) *required* - The argument value to compare against in the condition.
- **operator** (string) *required* - The operator to use in the condition evaluation.
- **variable** (string) *required* - The variable to be evaluated in the condition.

#### Example

```json
{
  "argument": "frog_genome",
  "operator": "contains",
  "variable": "specimen.dna_sequence"
}
```

