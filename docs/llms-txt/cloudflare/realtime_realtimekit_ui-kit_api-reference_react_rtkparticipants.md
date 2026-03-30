# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipants/index.md

---

title: RtkParticipants · Cloudflare Realtime docs
description: API reference for RtkParticipants component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipants/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipants/index.md
---

A component which lists all participants, with ability to run privileged actions on each participant according to your permissions.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config |
| `defaultParticipantsTabId` | `ParticipantsTabId` | ✅ | - | Default section |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkParticipants } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkParticipants />;
}
```

### With Properties

```tsx
import { RtkParticipants } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkParticipants
      defaultParticipantsTabId={participantstabid}
      meeting={meeting}
      size="md"
    />
  );
}
```
