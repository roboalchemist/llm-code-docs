# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmessagelistview/index.md

---

title: RtkMessageListView · Cloudflare Realtime docs
description: API reference for RtkMessageListView component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmessagelistview/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmessagelistview/index.md
---

A component which renders list of messages.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `estimateItemSize` | `number` | ✅ | - | Estimated height of an item |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `loadMore` | `(lastMessage: Message)` | ✅ | - | Function to load more messages. Messages returned from this will be preprended |
| `messages` | `Message[]` | ✅ | - | Messages to render |
| `renderer` | `(message: Message, index: number)` | ✅ | - | Render function of the message |
| `visibleItemsCount` | `number` | ✅ | - | Maximum visible messages |

## Usage Examples

### Basic Usage

```tsx
import { RtkMessageListView } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkMessageListView />;
}
```

### With Properties

```tsx
import { RtkMessageListView } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkMessageListView
      estimateItemSize={42}
      loadMore={(lastmessage: message)}
      messages={[]}
    />
  );
}
```
