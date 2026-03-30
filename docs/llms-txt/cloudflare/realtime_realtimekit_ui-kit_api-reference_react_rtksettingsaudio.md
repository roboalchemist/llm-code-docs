# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksettingsaudio/index.md

---

title: RtkSettingsAudio · Cloudflare Realtime docs
description: API reference for RtkSettingsAudio component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksettingsaudio/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksettingsaudio/index.md
---

A component which lets to manage your audio devices and audio preferences. Emits `rtkStateUpdate` event with data for muting notification sounds:

```ts
{
 prefs: {
   muteNotificationSounds: boolean
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
import { RtkSettingsAudio } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkSettingsAudio />;
}
```

### With Properties

```tsx
import { RtkSettingsAudio } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkSettingsAudio
      meeting={meeting}
      size="md"
    />
  );
}
```
