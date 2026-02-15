# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkrecordingindicator/index.md

---

title: RtkRecordingIndicator · Cloudflare Realtime docs
description: API reference for RtkRecordingIndicator component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkrecordingindicator/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkrecordingindicator/index.md
---

A component which indicates the recording status of a meeting. It will not render anything if no recording is taking place.

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
import { RtkRecordingIndicator } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkRecordingIndicator />;
}
```

### With Properties

```tsx
import { RtkRecordingIndicator } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkRecordingIndicator
      meeting={meeting}
      size="md"
    />
  );
}
```
