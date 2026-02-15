# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbutton/index.md

---

title: RtkButton · Cloudflare Realtime docs
description: API reference for RtkButton component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbutton/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbutton/index.md
---

A button that follows RTK Design System.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `disabled` | `boolean` | ✅ | - | Where the button is disabled or not |
| `kind` | `ButtonKind` | ✅ | - | Button type |
| `reverse` | `boolean` | ✅ | - | Whether to reverse order of children |
| `size` | `Size` | ✅ | - | Size |
| `type` | `HTMLButtonElement['type']` | ✅ | - | Button type |
| `variant` | `ButtonVariant` | ✅ | - | Button variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkButton } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkButton />;
}
```

### With Properties

```tsx
import { RtkButton } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkButton
      disabled={true}
      kind={buttonkind}
      reverse={true}
    />
  );
}
```
