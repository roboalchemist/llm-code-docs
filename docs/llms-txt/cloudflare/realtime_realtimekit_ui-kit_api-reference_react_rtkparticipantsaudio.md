# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantsaudio/index.md

---

title: RtkParticipantsAudio · Cloudflare Realtime docs
description: API reference for RtkParticipantsAudio component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantsaudio/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantsaudio/index.md
---

A component which plays all the audio from participants and screenshares.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `preloadedAudioElem` | `HTMLAudioElement` | ✅ | - | Pass existing audio element |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkParticipantsAudio } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkParticipantsAudio />;
}
```

### With Properties

```tsx
import { RtkParticipantsAudio } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkParticipantsAudio
      meeting={meeting}
      preloadedAudioElem={htmlaudioelement}
    />
  );
}
```
