# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkimagemessage/index.md

---

title: RtkImageMessage · Cloudflare Realtime docs
description: API reference for RtkImageMessage component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkimagemessage/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkimagemessage/index.md
---

@deprecated `rtk-image-message` is deprecated and will be removed soon. Use `rtk-image-message-view` instead. A component which renders an image message from chat.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `isContinued` | `boolean` | ✅ | - | Whether the message is continued by same user |
| `message` | `ImageMessage` | ✅ | - | Text message object |
| `now` | `Date` | ✅ | - | Date object of now, to calculate distance between dates |
| `showBubble` | `boolean` | ✅ | - | show message in bubble |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkImageMessage } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkImageMessage />;
}
```

### With Properties

```tsx
import { RtkImageMessage } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkImageMessage
      isContinued={true}
      message={imagemessage}
      now={date}
    />
  );
}
```
