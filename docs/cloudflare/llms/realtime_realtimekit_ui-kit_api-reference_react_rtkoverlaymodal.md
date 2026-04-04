# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkoverlaymodal/index.md

---

title: RtkOverlayModal · Cloudflare Realtime docs
description: API reference for RtkOverlayModal component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkoverlaymodal/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkoverlaymodal/index.md
---

A confirmation modal.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkOverlayModal } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkOverlayModal />;
}
```

### With Properties

```tsx
import { RtkOverlayModal } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkOverlayModal
      meeting={meeting}
    />
  );
}
```
