# Source: https://redocly.com/docs/realm/config/openapi/events.md

# `events`

Use event hooks to get notified about various user events in your API reference documentation.
This feature provides access to in-page analytics.

The events  is not available in Redoc Community Edition.

Each event provides information about a specific event as well as some basic information:


```typescript
    eventType: string;
    resource: string;
    action: string;
    operationId?: string;
    operationPath: string;
    operationHttpVerb: string;
    operationSummary?: string;
```

## Options

| Option | Type | Description |
|  --- | --- | --- |
| codeSamplesLanguageSwitch | string | A function called when the user switches to a different language tab in the code samples section.
Provides information about the selected language (lang) and an optional example ID (exampleId). |
| tryItOpen | string | A function that triggers when the user opens the âTry itâ panel.
Captures actions like opening the panel or navigating using the override links. |
| targetServerSwitch | string | A function invoked when the user changes the target server selection.
Provides the updated server URL (serverUrl). |
| tryItSent | string | A function called when the user clicks the âSendâ button in the âTry itâ panel.
Captures whether the request was successfully sent (Sent) or if there was a validation failure (ValidationFailed). |
| panelToggle | string | A function that records when a user expands or collapses any panel in the Reference docs UI (for example, request, responses, request samples, or response samples).
Includes details about the panel type (panelType) and its state (expanded or collapsed). |
| codeSamplesCopy | string | A function that triggers when a user copies request or response samples within the Reference docs UI.
Captures details such as the sample type (request or responses), example ID (if applicable), code sample language (`lang`), and label (`label`). |


## Examples

The following example show the usage of the `events` configuration:


```yaml redocly.yaml
openapi:
  events:
    codeSamplesLanguageSwitch: '({ lang, label, exampleId}) => {
      console.log(`Switched to language: ${lang}`);
    }'
    tryItOpen: '() => {
      console.log(`Try it panel opened`);
    }'
    targetServerSwitch: '({ serverUrl }) => {
      console.log(`Switched to server: ${serverUrl}`);
    }'
```

## Resources

- **[OpenAPI configuration](/docs/realm/config/openapi)** - Complete guide to OpenAPI configuration options for customizing API reference documentation
- **[OpenAPI Specification](https://spec.openapis.org/oas/latest.html)** - Official OpenAPI Specification documentation for understanding API description standards
- **[OpenAPI visual reference](https://redocly.com/learn/openapi/openapi-visual-reference)** - Visual guide to OpenAPI specification structure and event configuration principles
- **[Configuration options](/docs/realm/config)** - Explore other project configuration options for comprehensive documentation customization