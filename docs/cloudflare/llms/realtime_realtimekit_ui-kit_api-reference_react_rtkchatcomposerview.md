# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatcomposerview/index.md

---

title: RtkChatComposerView · Cloudflare Realtime docs
description: API reference for RtkChatComposerView component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatcomposerview/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatcomposerview/index.md
---

A component which renders a chat composer

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `canSendFiles` | `boolean` | ✅ | - | Whether user can send file messages |
| `canSendTextMessage` | `boolean` | ✅ | - | Whether user can send text messages |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `inputTextPlaceholder` | `string` | ✅ | - | Placeholder for text input |
| `isEditing` | `boolean` | ✅ | - | Sets composer to edit mode |
| `maxLength` | `number` | ✅ | - | Max length for text input |
| `message` | `string` | ✅ | - | Message to be pre-populated |
| `quotedMessage` | `string` | ✅ | - | Quote message to be displayed |
| `rateLimits` | `{ period: number; maxInvocations: number; }` | ✅ | - | Rate limits |
| `storageKey` | `string` | ✅ | - | Key for storing message in localStorage |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkChatComposerView } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkChatComposerView />;
}
```

### With Properties

```tsx
import { RtkChatComposerView } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkChatComposerView
      canSendFiles={true}
      canSendTextMessage={true}
      inputTextPlaceholder="example"
    />
  );
}
```
