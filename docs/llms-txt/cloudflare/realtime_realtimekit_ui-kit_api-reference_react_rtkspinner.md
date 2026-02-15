# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkspinner/index.md

---

title: RtkSpinner · Cloudflare Realtime docs
description: API reference for RtkSpinner component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkspinner/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkspinner/index.md
---

A component which shows an animating spinner.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `size` | `Size1` | ✅ | - | Size |

## Usage Examples

### Basic Usage

```tsx
import { RtkSpinner } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkSpinner />;
}
```

### With Properties

```tsx
import { RtkSpinner } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkSpinner
      size="md"
    />
  );
}
```
