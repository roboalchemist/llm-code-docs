# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfilemessageview/index.md

---

title: RtkFileMessageView · Cloudflare Realtime docs
description: API reference for RtkFileMessageView component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfilemessageview/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfilemessageview/index.md
---

A component which renders a file message.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `name` | `string` | ✅ | - | Name of the file |
| `size` | `number` | ✅ | - | Size of the file |
| `url` | `string` | ✅ | - | Url of the file |

## Usage Examples

### Basic Usage

```tsx
import { RtkFileMessageView } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkFileMessageView />;
}
```

### With Properties

```tsx
import { RtkFileMessageView } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkFileMessageView
      name="example"
      size={42}
      url="example"
    />
  );
}
```
