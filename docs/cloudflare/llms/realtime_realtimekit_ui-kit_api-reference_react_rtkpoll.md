# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpoll/index.md

---

title: RtkPoll · Cloudflare Realtime docs
description: API reference for RtkPoll component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpoll/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpoll/index.md
---

A poll component. Shows a poll where a user can vote.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `permissions` | `RTKPermissionsPreset` | ✅ | - | Permissions Object |
| `poll` | `Poll` | ✅ | - | Poll |
| `self` | `string` | ✅ | - | Self ID |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkPoll } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkPoll />;
}
```

### With Properties

```tsx
import { RtkPoll } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkPoll
      permissions={rtkpermissionspreset}
      poll={poll}
      self="example"
    />
  );
}
```
