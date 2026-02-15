# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpermissionsmessage/index.md

---

title: RtkPermissionsMessage · Cloudflare Realtime docs
description: API reference for RtkPermissionsMessage component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpermissionsmessage/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpermissionsmessage/index.md
---

A component which shows permission related troubleshooting information.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon Pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkPermissionsMessage } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkPermissionsMessage />;
}
```

### With Properties

```tsx
import { RtkPermissionsMessage } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkPermissionsMessage
      meeting={meeting}
    />
  );
}
```
