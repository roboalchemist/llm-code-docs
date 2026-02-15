# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmeetingtitle/index.md

---

title: RtkMeetingTitle · Cloudflare Realtime docs
description: API reference for RtkMeetingTitle component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmeetingtitle/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmeetingtitle/index.md
---

Displays the title of the meeting.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkMeetingTitle } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkMeetingTitle />;
}
```

### With Properties

```tsx
import { RtkMeetingTitle } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkMeetingTitle
      meeting={meeting}
    />
  );
}
```
