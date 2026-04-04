# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatsearchresults/index.md

---

title: RtkChatSearchResults · Cloudflare Realtime docs
description: API reference for RtkChatSearchResults component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatsearchresults/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatsearchresults/index.md
---

@deprecated `rtk-chat-search-results` is deprecated and will be removed soon. Use `rtk-chat-messages-ui-paginated` instead. -

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `channelId` | `string` | ✅ | - | Channel id |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `query` | `string` | ✅ | - | Search query |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkChatSearchResults } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkChatSearchResults />;
}
```

### With Properties

```tsx
import { RtkChatSearchResults } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkChatSearchResults
      channelId="example"
      meeting={meeting}
      query="example"
    />
  );
}
```
