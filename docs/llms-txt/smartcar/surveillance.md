# Source: https://smartcar.com/docs/api-reference/signals/surveillance.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Surveillance Signals & Attributes

## Signals

### Is Enabled

Signal code: `surveillance-isenabled`

Indicates if the surveillance system is enabled

<ParamField path="value" type="boolean" required={false}>
  Boolean indicating if surveillance is active
</ParamField>

```json Example theme={null}
{
  "value": true
}
```

## Attributes

### Brand

Signal code: `surveillance-brand`

Indicates the brand of surveillance available on the vehicle e.g. for Tesla this would be Sentry Mode

<ParamField path="value" type="string" required={false}>
  The brand name or type of surveillance system
</ParamField>

```json Example theme={null}
{
  "value": "Sentry Mode"
}
```
