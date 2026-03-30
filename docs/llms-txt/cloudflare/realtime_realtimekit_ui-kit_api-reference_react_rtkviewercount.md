# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkviewercount/index.md

---

title: RtkViewerCount · Cloudflare Realtime docs
description: API reference for RtkViewerCount component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkviewercount/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkviewercount/index.md
---

A component which shows count of total joined participants in a meeting.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ViewerCountVariant` | ✅ | - | Viewer count variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkViewerCount } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkViewerCount />;
}
```

### With Properties

```tsx
import { RtkViewerCount } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkViewerCount
      meeting={meeting}
      variant="primary"
    />
  );
}
```
