# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtknotifications/index.md

---

title: RtkNotifications · Cloudflare Realtime docs
description: API reference for RtkNotifications component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtknotifications/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtknotifications/index.md
---

A component which handles notifications. You can configure which notifications you want to see and which ones you want to hear. There are also certain limits which you can set as well.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config object |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkNotifications } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkNotifications />;
}
```

### With Properties

```tsx
import { RtkNotifications } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkNotifications
      meeting={meeting}
      size="md"
    />
  );
}
```
