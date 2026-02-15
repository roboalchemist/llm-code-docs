# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmuteallconfirmation/index.md

---

title: RtkMuteAllConfirmation · Cloudflare Realtime docs
description: API reference for RtkMuteAllConfirmation component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmuteallconfirmation/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmuteallconfirmation/index.md
---

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
import { RtkMuteAllConfirmation } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkMuteAllConfirmation />;
}
```

### With Properties

```tsx
import { RtkMuteAllConfirmation } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkMuteAllConfirmation
      meeting={meeting}
    />
  );
}
```
