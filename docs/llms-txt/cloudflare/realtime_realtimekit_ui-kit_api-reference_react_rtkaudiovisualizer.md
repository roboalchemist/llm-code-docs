# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaudiovisualizer/index.md

---

title: RtkAudioVisualizer · Cloudflare Realtime docs
description: API reference for RtkAudioVisualizer component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaudiovisualizer/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaudiovisualizer/index.md
---

An audio visualizer component which visualizes a participants audio. Commonly used inside `rtk-name-tag`.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `hideMuted` | `boolean` | ✅ | - | Hide the visualizer if audio is muted |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `isScreenShare` | `boolean` | ✅ | - | Audio visualizer for screensharing, it will use screenShareTracks.audio instead of audioTrack |
| `participant` | `Peer` | ✅ | - | Participant object |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `AudioVisualizerVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkAudioVisualizer } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkAudioVisualizer />;
}
```

### With Properties

```tsx
import { RtkAudioVisualizer } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkAudioVisualizer
      hideMuted={true}
      isScreenShare={true}
      participant={participant}
    />
  );
}
```
