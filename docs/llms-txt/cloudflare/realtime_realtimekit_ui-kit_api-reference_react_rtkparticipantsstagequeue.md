# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantsstagequeue/index.md

---

title: RtkParticipantsStageQueue · Cloudflare Realtime docs
description: API reference for RtkParticipantsStageQueue component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantsstagequeue/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantsstagequeue/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `config` | `UIConfig1` | ❌ | `createDefaultConfig()` | Config |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size1` | ✅ | - | Size |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |
| `view` | `ParticipantsViewMode` | ✅ | - | View mode for participants list |

## Usage Examples

### Basic Usage

```tsx
import { RtkParticipantsStageQueue } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkParticipantsStageQueue />;
}
```

### With Properties

```tsx
import { RtkParticipantsStageQueue } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkParticipantsStageQueue
      meeting={meeting}
      size="md"
      view={participantsviewmode}
    />
  );
}
```
