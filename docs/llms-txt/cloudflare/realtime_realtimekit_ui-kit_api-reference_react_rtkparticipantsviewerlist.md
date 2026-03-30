# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantsviewerlist/index.md

---

title: RtkParticipantsViewerList · Cloudflare Realtime docs
description: API reference for RtkParticipantsViewerList component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantsviewerlist/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantsviewerlist/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `config` | `UIConfig1` | ❌ | `createDefaultConfig()` | Config |
| `hideHeader` | `boolean` | ✅ | - | Hide Viewer Count Header |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `search` | `string` | ✅ | - | Search |
| `size` | `Size1` | ✅ | - | Size |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |
| `view` | `ParticipantsViewMode` | ✅ | - | View mode for participants list |

## Usage Examples

### Basic Usage

```tsx
import { RtkParticipantsViewerList } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkParticipantsViewerList />;
}
```

### With Properties

```tsx
import { RtkParticipantsViewerList } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkParticipantsViewerList
      hideHeader={true}
      meeting={meeting}
      search="example"
    />
  );
}
```
