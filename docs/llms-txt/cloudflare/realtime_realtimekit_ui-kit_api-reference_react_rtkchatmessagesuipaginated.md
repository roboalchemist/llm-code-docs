# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatmessagesuipaginated/index.md

---

title: RtkChatMessagesUiPaginated · Cloudflare Realtime docs
description: API reference for RtkChatMessagesUiPaginated component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatmessagesuipaginated/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatmessagesuipaginated/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `privateChatRecipient` | `Participant \| null` | ✅ | - | Selected recipient for private chat; when unset, messages are loaded for public chat (Everyone). |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkChatMessagesUiPaginated } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkChatMessagesUiPaginated />;
}
```

### With Properties

```tsx
import { RtkChatMessagesUiPaginated } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkChatMessagesUiPaginated
      meeting={meeting}
      privateChatRecipient={participant | null}
      size="md"
    />
  );
}
```
