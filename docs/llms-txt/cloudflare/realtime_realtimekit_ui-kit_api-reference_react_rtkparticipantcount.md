# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantcount/index.md

---

title: RtkParticipantCount · Cloudflare Realtime docs
description: API reference for RtkParticipantCount component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantcount/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantcount/index.md
---

A component which shows count of total joined participants in a meeting.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkParticipantCount } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkParticipantCount />;
}
```

### With Properties

```tsx
import { RtkParticipantCount } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkParticipantCount
      meeting={meeting}
      size="md"
    />
  );
}
```
