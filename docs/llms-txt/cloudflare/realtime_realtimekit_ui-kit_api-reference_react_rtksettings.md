# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksettings/index.md

---

title: RtkSettings · Cloudflare Realtime docs
description: API reference for RtkSettings component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksettings/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksettings/index.md
---

A settings component to see and change your audio/video devices as well as see your connection quality.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkSettings } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkSettings />;
}
```

### With Properties

```tsx
import { RtkSettings } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkSettings
      meeting={meeting}
      size="md"
    />
  );
}
```
