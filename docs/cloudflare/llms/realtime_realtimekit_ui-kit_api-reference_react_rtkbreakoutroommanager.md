# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbreakoutroommanager/index.md

---

title: RtkBreakoutRoomManager · Cloudflare Realtime docs
description: API reference for RtkBreakoutRoomManager component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbreakoutroommanager/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbreakoutroommanager/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `allowDelete` | `boolean` | ✅ | - | allow room delete |
| `assigningParticipants` | `boolean` | ✅ | - | Enable updating participants |
| `defaultExpanded` | `boolean` | ✅ | - | display expanded card by default |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `isDragMode` | `boolean` | ✅ | - | Drag mode |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `mode` | `'edit' \| 'create'` | ✅ | - | Mode in which selector is used |
| `room` | `DraftMeeting` | ✅ | - | Connected Room Config Object |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkBreakoutRoomManager } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkBreakoutRoomManager />;
}
```

### With Properties

```tsx
import { RtkBreakoutRoomManager } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkBreakoutRoomManager
      allowDelete={true}
      assigningParticipants={true}
      defaultExpanded={true}
    />
  );
}
```
