# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfiledropzone/index.md

---

title: RtkFileDropzone · Cloudflare Realtime docs
description: API reference for RtkFileDropzone component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfiledropzone/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfiledropzone/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `hostEl` | `HTMLElement` | ✅ | - | Host element on which drop events to attach |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkFileDropzone } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkFileDropzone />;
}
```

### With Properties

```tsx
import { RtkFileDropzone } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkFileDropzone
      hostEl={htmlelement}
    />
  );
}
```
