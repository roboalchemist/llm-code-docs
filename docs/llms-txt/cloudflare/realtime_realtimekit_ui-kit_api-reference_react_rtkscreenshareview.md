# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkscreenshareview/index.md

---

title: RtkScreenshareView · Cloudflare Realtime docs
description: API reference for RtkScreenshareView component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkscreenshareview/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkscreenshareview/index.md
---

A component which plays a participant's screenshared video. It also allows for placement of other components similar to `rtk-participant-tile`. This component will not render anything if the participant hasn't start screensharing.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `hideFullScreenButton` | `boolean` | ✅ | - | Hide full screen button |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `nameTagPosition` | `\| 'bottom-left' \| 'bottom-right' \| 'bottom-center' \| 'top-left' \| 'top-right' \| 'top-center'` | ✅ | - | Position of name tag |
| `participant` | `Peer` | ✅ | - | Participant object |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `'solid' \| 'gradient'` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkScreenshareView } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkScreenshareView />;
}
```

### With Properties

```tsx
import { RtkScreenshareView } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkScreenshareView
      hideFullScreenButton={true}
      meeting={meeting}
      nameTagPosition={| 'bottom-left'
    | 'bottom-right'
    | 'bottom-center'
    | 'top-left'
    | 'top-right'
    | 'top-center'}
    />
  );
}
```
