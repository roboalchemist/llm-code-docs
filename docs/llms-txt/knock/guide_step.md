# Source: https://docs.knock.app/mapi-reference/guides/schemas/guide_step.md

### GuideStep

A step in a guide that corresponds to a piece of UI and its content.

#### Attributes

- **name** (string) - A name for the step.
- **ref** (string) *required* - The unique reference string for the step. Must be at minimum 3 characters and at maximum 255 characters in length. Must be in the format of ^[a-z0-9_-]+$.
- **schema_key** (string) *required* - The key of the template schema to use for this step.
- **schema_semver** (string) *required* - The semantic version of the template schema to use.
- **schema_variant_key** (string) *required* - The key of the template schema variant to use.
- **values** (object) - A map of values that make up the step's content. Each value must conform to its respective template schema field settings.

#### Example

```json
{
  "name": "Welcome to the App",
  "ref": "welcome-step",
  "schema_key": "tooltip",
  "schema_semver": "1.0.0",
  "schema_variant_key": "default",
  "values": {
    "text_field": "value"
  }
}
```

