# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaudiotile/index.md

---

title: RtkAudioTile · Cloudflare Realtime docs
description: API reference for RtkAudioTile component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaudiotile/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaudiotile/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `config` | `UIConfig` | ✅ | - | Config |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting |
| `participant` | `Peer` | ✅ | - | Participant object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States1` | ✅ | - | States |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkAudioTile } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkAudioTile />;
}
```

### With Properties

```tsx
import { RtkAudioTile } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkAudioTile
      config={defaultUiConfig}
      meeting={meeting}
      participant={participant}
    />
  );
}
```
