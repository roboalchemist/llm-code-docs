# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatcomposerui/index.md

---

title: RtkChatComposerUi · Cloudflare Realtime docs
description: API reference for RtkChatComposerUi component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatcomposerui/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatcomposerui/index.md
---

@deprecated . This component is deprecated, please use rtk-chat-composer-view instead.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `canSendFiles` | `boolean` | ✅ | - | Whether user can send file messages |
| `canSendTextMessage` | `boolean` | ✅ | - | Whether user can send text messages |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `prefill` | `{ suggestedReplies?: string[]; editMessage?: TextMessage; replyMessage?: TextMessage; }` | ❌ | - | prefill the composer |
| `size` | `Size1` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkChatComposerUi } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkChatComposerUi />;
}
```

### With Properties

```tsx
import { RtkChatComposerUi } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkChatComposerUi
      canSendFiles={true}
      canSendTextMessage={true}
      size="md"
    />
  );
}
```
