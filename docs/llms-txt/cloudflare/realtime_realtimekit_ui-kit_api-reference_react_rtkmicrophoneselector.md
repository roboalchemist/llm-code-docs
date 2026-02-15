# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmicrophoneselector/index.md

---

title: RtkMicrophoneSelector · Cloudflare Realtime docs
description: API reference for RtkMicrophoneSelector component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmicrophoneselector/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmicrophoneselector/index.md
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
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `'full' \| 'inline'` | ✅ | - | variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkMicrophoneSelector } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkMicrophoneSelector />;
}
```

### With Properties

```tsx
import { RtkMicrophoneSelector } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkMicrophoneSelector
      meeting={meeting}
      size="md"
      variant={'full' | 'inline'}
    />
  );
}
```
