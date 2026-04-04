# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtknotification/index.md

---

title: RtkNotification · Cloudflare Realtime docs
description: API reference for RtkNotification component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtknotification/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtknotification/index.md
---

A component which shows a notification. You need to remove the element after you receive the `rtkNotificationDismiss` event.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `notification` | `Notification` | ✅ | - | Message |
| `paused` | `boolean` | ✅ | - | Stops timeout when true |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkNotification } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkNotification />;
}
```

### With Properties

```tsx
import { RtkNotification } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkNotification
      notification={notification}
      paused={true}
      size="md"
    />
  );
}
```
