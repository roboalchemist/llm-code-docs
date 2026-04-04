# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtklivestreamplayer/index.md

---

title: RtkLivestreamPlayer · Cloudflare Realtime docs
description: API reference for RtkLivestreamPlayer component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtklivestreamplayer/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtklivestreamplayer/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size1` | ✅ | - | Size |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkLivestreamPlayer } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkLivestreamPlayer />;
}
```

### With Properties

```tsx
import { RtkLivestreamPlayer } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkLivestreamPlayer
      meeting={meeting}
      size="md"
    />
  );
}
```
