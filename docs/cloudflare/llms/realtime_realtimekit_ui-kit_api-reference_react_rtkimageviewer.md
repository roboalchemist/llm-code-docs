# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkimageviewer/index.md

---

title: RtkImageViewer · Cloudflare Realtime docs
description: API reference for RtkImageViewer component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkimageviewer/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkimageviewer/index.md
---

A component which shows an image sent via chat.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `image` | `ImageMessage` | ✅ | - | Image message |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkImageViewer } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkImageViewer />;
}
```

### With Properties

```tsx
import { RtkImageViewer } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkImageViewer
      image={imagemessage}
      size="md"
    />
  );
}
```
