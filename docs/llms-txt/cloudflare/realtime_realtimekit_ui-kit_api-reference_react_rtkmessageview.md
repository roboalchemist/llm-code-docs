# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmessageview/index.md

---

title: RtkMessageView · Cloudflare Realtime docs
description: API reference for RtkMessageView component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmessageview/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmessageview/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `actions` | `MessageAction[]` | ✅ | - | List of actions to show in menu |
| `authorName` | `string` | ✅ | - | Author display label |
| `avatarUrl` | `string` | ✅ | - | Avatar image url |
| `hideAuthorName` | `boolean` | ✅ | - | Hides author display label |
| `hideAvatar` | `boolean` | ✅ | - | Hides avatar |
| `hideMetadata` | `boolean` | ✅ | - | Hides metadata (time) |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `isEdited` | `boolean` | ✅ | - | Has the message been edited |
| `isSelf` | `boolean` | ✅ | - | Is the message sent by the current user |
| `messageType` | `Message['type']` | ✅ | - | Type of message |
| `pinned` | `boolean` | ✅ | - | Is message pinned |
| `time` | `Date` | ✅ | - | Time when message was sent |
| `variant` | `'plain' \| 'bubble'` | ✅ | - | Appearance |
| `viewType` | `'incoming' \| 'outgoing'` | ✅ | - | Render |

## Usage Examples

### Basic Usage

```tsx
import { RtkMessageView } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkMessageView />;
}
```

### With Properties

```tsx
import { RtkMessageView } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkMessageView
      actions={[]}
      authorName="example"
      avatarUrl="example"
    />
  );
}
```
