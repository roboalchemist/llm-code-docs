# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatselectorui/index.md

---

title: RtkChatSelectorUi · Cloudflare Realtime docs
description: API reference for RtkChatSelectorUi component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatselectorui/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatselectorui/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `groups` | `ChatGroup[]` | ✅ | - | Participants |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `selectedGroupId` | `string` | ✅ | - | Selected participant |
| `selfUserId` | `string` | ✅ | - | Self User ID |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `unreadCounts` | `Record<string, number>` | ✅ | - | Unread counts |

## Usage Examples

### Basic Usage

```tsx
import { RtkChatSelectorUi } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkChatSelectorUi />;
}
```

### With Properties

```tsx
import { RtkChatSelectorUi } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkChatSelectorUi
      groups={[]}
      selectedGroupId="example"
      selfUserId="example"
    />
  );
}
```
