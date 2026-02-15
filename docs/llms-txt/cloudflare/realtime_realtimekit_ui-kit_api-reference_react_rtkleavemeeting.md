# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkleavemeeting/index.md

---

title: RtkLeaveMeeting · Cloudflare Realtime docs
description: API reference for RtkLeaveMeeting component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkleavemeeting/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkleavemeeting/index.md
---

A component which allows you to leave a meeting or end meeting for all, if you have the permission.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkLeaveMeeting } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkLeaveMeeting />;
}
```

### With Properties

```tsx
import { RtkLeaveMeeting } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkLeaveMeeting
      meeting={meeting}
    />
  );
}
```
