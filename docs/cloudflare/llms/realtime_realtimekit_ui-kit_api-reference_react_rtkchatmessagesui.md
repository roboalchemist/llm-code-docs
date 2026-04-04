# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatmessagesui/index.md

---

title: RtkChatMessagesUi · Cloudflare Realtime docs
description: API reference for RtkChatMessagesUi component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatmessagesui/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatmessagesui/index.md
---

@deprecated Use `rtk-chat-messages-ui-paginated` instead.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `canPinMessages` | `boolean` | ✅ | - | Can current user pin/unpin messages |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `messages` | `Chat[]` | ✅ | - | Chat Messages |
| `selectedGroup` | `string` | ✅ | - | Selected group key |
| `selfUserId` | `string` | ✅ | - | User ID of self user |
| `size` | `Size1` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkChatMessagesUi } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkChatMessagesUi />;
}
```

### With Properties

```tsx
import { RtkChatMessagesUi } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkChatMessagesUi
      canPinMessages={true}
      messages={[]}
      selectedGroup="example"
    />
  );
}
```
