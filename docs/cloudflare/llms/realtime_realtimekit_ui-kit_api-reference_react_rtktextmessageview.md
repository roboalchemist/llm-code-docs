# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktextmessageview/index.md

---

title: RtkTextMessageView · Cloudflare Realtime docs
description: API reference for RtkTextMessageView component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktextmessageview/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktextmessageview/index.md
---

A component which renders a text message from chat.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `isMarkdown` | `boolean` | ✅ | - | Renders text as markdown (default = true) |
| `text` | `string` | ✅ | - | Text message |

## Usage Examples

### Basic Usage

```tsx
import { RtkTextMessageView } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkTextMessageView />;
}
```

### With Properties

```tsx
import { RtkTextMessageView } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkTextMessageView
      isMarkdown={true}
      text="example"
    />
  );
}
```
