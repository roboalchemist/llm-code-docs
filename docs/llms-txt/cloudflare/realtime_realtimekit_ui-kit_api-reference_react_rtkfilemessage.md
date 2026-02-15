# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfilemessage/index.md

---

title: RtkFileMessage · Cloudflare Realtime docs
description: API reference for RtkFileMessage component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfilemessage/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfilemessage/index.md
---

@deprecated `rtk-file-message` is deprecated and will be removed soon. Use `rtk-file-message-view` instead. A component which renders a file message from chat.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `isContinued` | `boolean` | ✅ | - | Whether the message is continued by same user |
| `message` | `FileMessage` | ✅ | - | Text message object |
| `now` | `Date` | ✅ | - | Date object of now, to calculate distance between dates |
| `showBubble` | `boolean` | ✅ | - | show message in bubble |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkFileMessage } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkFileMessage />;
}
```

### With Properties

```tsx
import { RtkFileMessage } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkFileMessage
      isContinued={true}
      message={filemessage}
      now={date}
    />
  );
}
```
