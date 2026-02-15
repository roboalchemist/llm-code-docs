# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkicon/index.md

---

title: RtkIcon · Cloudflare Realtime docs
description: API reference for RtkIcon component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkicon/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkicon/index.md
---

An icon component which accepts an svg string and renders it.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `icon` | `string` | ✅ | - | Icon |
| `size` | `Size1` | ✅ | - | Size |
| `variant` | `IconVariant` | ✅ | - | Icon variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkIcon } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkIcon />;
}
```

### With Properties

```tsx
import { RtkIcon } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkIcon
      icon="example"
      size="md"
      variant="primary"
    />
  );
}
```
