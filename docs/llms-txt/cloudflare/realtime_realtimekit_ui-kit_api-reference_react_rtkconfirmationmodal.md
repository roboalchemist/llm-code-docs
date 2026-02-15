# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkconfirmationmodal/index.md

---

title: RtkConfirmationModal · Cloudflare Realtime docs
description: API reference for RtkConfirmationModal component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkconfirmationmodal/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkconfirmationmodal/index.md
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
import { RtkConfirmationModal } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkConfirmationModal />;
}
```

### With Properties

```tsx
import { RtkConfirmationModal } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkConfirmationModal
      meeting={meeting}
    />
  );
}
```
