# Source: https://redocly.com/docs/cli/rules/arazzo/step-onsuccess-unique.md

# Source: https://redocly.com/docs/cli/v1/rules/arazzo/step-onsuccess-unique.md

# step-onSuccess-unique

Requires the `onSuccess` actions of the `step` object to be unique.

| Arazzo | Compatibility |
|  --- | --- |
| 1.x | â |


## Design principles

Each `onSuccess` action must be unique to avoid confusion or unexpected outcomes.
A duplicate could indicate a mistake, or cause unwanted side effects if not detected by this rule.

## Configuration

| Option | Type | Description |
|  --- | --- | --- |
| severity | string | Possible values: `off`, `warn`, `error`. Default `off`. |


An example configuration:


```yaml
rules:
  step-onSuccess-unique: error
```

## Examples

Given the following configuration:


```yaml
rules:
  step-onSuccess-unique: error
```

Example of a **correct** `onSuccess` list:


```yaml
workflows:
- workflowId: get-museum-hours
  description: This workflow demonstrates how to get the museum opening hours and buy tickets.
  steps:
    - stepId: get-museum-hours
      operationId: museum-api.getMuseumHours
      successCriteria:
        - condition: $statusCode == 200
      onSuccess:
        - name: call-crud-events
          workflowId: events-crud
          type: goto
        - name: second-call-crud-events
          workflowId: events-crud
          type: goto
        - reference: $components.successActions.notify
        - reference: $components.successActions.report
```

## Related rules

- [step-onFailure-unique](/docs/cli/v1/rules/arazzo/step-onfailure-unique)


## Resources

- [Rule source](https://github.com/Redocly/redocly-cli/blob/main/packages/core/src/rules/arazzo/step-onSuccess-unique.ts)