# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktextmessage/index.md

---

title: RtkTextMessage · Cloudflare Realtime docs
description: API reference for RtkTextMessage component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktextmessage/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktextmessage/index.md
---

@deprecated `rtk-text-message` is deprecated and will be removed soon. Use `rtk-text-message-view` instead. A component which renders a text message from chat.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `isContinued` | `boolean` | ✅ | - | Whether the message is continued by same user |
| `message` | `TextMessage` | ✅ | - | Text message object |
| `now` | `Date` | ✅ | - | Date object of now, to calculate distance between dates |
| `showBubble` | `boolean` | ✅ | - | show message in bubble |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkTextMessage } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkTextMessage />;
}
```

### With Properties

```tsx
import { RtkTextMessage } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkTextMessage
      isContinued={true}
      message={textmessage}
      now={date}
    />
  );
}
```
