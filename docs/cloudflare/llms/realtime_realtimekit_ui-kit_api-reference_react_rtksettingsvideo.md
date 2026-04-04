# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksettingsvideo/index.md

---

title: RtkSettingsVideo · Cloudflare Realtime docs
description: API reference for RtkSettingsVideo component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksettingsvideo/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksettingsvideo/index.md
---

A component which lets to manage your camera devices and your video preferences. Emits `rtkStateUpdate` event with data for toggling mirroring of self video:

```ts
{
 prefs: {
   mirrorVideo: boolean
 }
}
```

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
import { RtkSettingsVideo } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkSettingsVideo />;
}
```

### With Properties

```tsx
import { RtkSettingsVideo } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkSettingsVideo
      meeting={meeting}
      size="md"
    />
  );
}
```
