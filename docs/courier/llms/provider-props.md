# Source: https://www.courier.com/docs/platform/create/provider-props.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Editor Properties

> Explore configuration options for Courier Create Template and Brand Editors. Learn how to customize behavior, appearance, and functionality using detailed component properties.

Courier Create provides a set of properties for customizing the Template, Brand Editor and Template Provider. These properties give developers fine-grained control over editor behavior, visual styling, and data flow, making it easy to tailor the integration to any product or tenant-specific requirement.

## Template Provider Properties

The `TemplateProvider` wraps the Template editor component and manages the template's state, authentication, and data flow. It provides essential context and functionality needed for the editor to operate.

| Property     | Type   | Required | Description                                                 |
| ------------ | ------ | -------- | ----------------------------------------------------------- |
| `templateId` | string | Yes      | Unique ID for the template. Creates it if it doesn't exist. |
| `tenantId`   | string | Yes      | ID of the tenant the template belongs to.                   |
| `token`      | string | Yes      | JWT or Client Key used for authenticating API requests.     |

## Template Editor Properties

The `TemplateEditor` component is the core element that provides the template editing interface. If you are using the Template Editor with the Template provider, required properties will be provided.

| Property           | Type                                                | Default | Description                                                                               |
| ------------------ | --------------------------------------------------- | ------- | ----------------------------------------------------------------------------------------- |
| `autoSave`         | boolean                                             | true    | Enables automatic saving of changes.                                                      |
| `autoSaveDebounce` | number                                              | 200ms   | Time in milliseconds before auto-saving after changes.                                    |
| `brandEditor`      | boolean                                             | false   | Displays brand editor alongside the template editor.                                      |
| `brandProps`       | BrandEditorProps                                    | —       | Configuration options for the brand editor when enabled.                                  |
| `hidePublish`      | boolean                                             | false   | Hides the default "Publish Changes" button.                                               |
| `onChange`         | (value: ElementalContent) => void                   | —       | Callback triggered when the editor content changes.                                       |
| `routing`          | `{ method: "single" \| "all", channels: string[] }` | —       | Restricts which channels are visible in the editor. Channels not in the array are hidden. |
| `theme`            | ThemeObj / cssClass                                 | —       | Customize editor appearance via theme object or CSS class name.                           |
| `value`            | ElementalContent                                    | —       | Initial content loaded into the editor.                                                   |
| `variables`        | `Record<string, any>`                               | —       | Template personalization variables available in the editor.                               |

## Brand Provider Properties

The Brand Provider component is responsible for managing brand-related state and context in your application. It wraps the Brand Editor component and handles data flow, authentication, and state management for brand customization.

| Property   | Type   | Required | Description                                                          |
| ---------- | ------ | -------- | -------------------------------------------------------------------- |
| `tenantId` | string | Yes      | The tenant identifier for which brand settings are being customized. |
| `token`    | string | Yes      | JWT or Client Key used to authorize brand-related API access.        |

The Brand Editor component accepts properties that allow you to customize its behavior and appearance. These properties provide control over the editing interface and functionality specific to brand management.

| Property           | Type                           | Default | Description                                                      |
| ------------------ | ------------------------------ | ------- | ---------------------------------------------------------------- |
| `autoSave`         | boolean                        | true    | Enables automatic saving of brand changes.                       |
| `autoSaveDebounce` | number                         | 200ms   | Delay in milliseconds before triggering auto-save.               |
| `hidePublish`      | boolean                        | false   | Hides the "Publish Changes" button.                              |
| `onChange`         | (value: BrandSettings) => void | —       | Callback fired on brand settings updates.                        |
| `theme`            | ThemeObj / cssClass            | —       | Apply custom theme or class name for editor styling.             |
| `value`            | BrandSettings                  | —       | Initial brand configuration values.                              |
| `variables`        | `Record<string, any>`          | —       | Variables available for use in brand footer and related content. |
