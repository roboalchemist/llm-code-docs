# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbreakoutroomparticipants/index.md

---

title: RtkBreakoutRoomParticipants · Cloudflare Realtime docs
description: API reference for RtkBreakoutRoomParticipants component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbreakoutroomparticipants/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbreakoutroomparticipants/index.md
---

A component which lists all participants, with ability to run privileged actions on each participant according to your permissions.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `participantIds` | `string[]` | ✅ | - | Participant ids |
| `selectedParticipantIds` | `string[]` | ✅ | - | selected participants |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkBreakoutRoomParticipants } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkBreakoutRoomParticipants />;
}
```

### With Properties

```tsx
import { RtkBreakoutRoomParticipants } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkBreakoutRoomParticipants
      meeting={meeting}
      participantIds="example"
      selectedParticipantIds="example"
    />
  );
}
```
