# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkimagemessageview/index.md

---

title: RtkImageMessageView · Cloudflare Realtime docs
description: API reference for RtkImageMessageView component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkimagemessageview/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkimagemessageview/index.md
---

A component which renders an image message.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |
| `url` | `string` | ✅ | - | Url of the image |

## Usage Examples

### Basic Usage

```tsx
import { RtkImageMessageView } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkImageMessageView />;
}
```

### With Properties

```tsx
import { RtkImageMessageView } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkImageMessageView
      url="example"
    />
  );
}
```
