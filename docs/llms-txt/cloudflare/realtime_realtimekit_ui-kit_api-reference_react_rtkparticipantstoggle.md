# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantstoggle/index.md

---

title: RtkParticipantsToggle · Cloudflare Realtime docs
description: API reference for RtkParticipantsToggle component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantstoggle/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantstoggle/index.md
---

A button which toggles visibility of participants. When clicked it emits a `rtkStateUpdate` event with the data:

```ts
{ activeSidebar: boolean; sidebar: 'participants' }
```

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkParticipantsToggle } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkParticipantsToggle />;
}
```

### With Properties

```tsx
import { RtkParticipantsToggle } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkParticipantsToggle
      meeting={meeting}
      size="md"
      variant="button"
    />
  );
}
```
