# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkrecordingtoggle/index.md

---

title: RtkRecordingToggle · Cloudflare Realtime docs
description: API reference for RtkRecordingToggle component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkrecordingtoggle/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkrecordingtoggle/index.md
---

A button which toggles recording state of a meeting. Only a privileged user can perform this action, thus the button will not be visible for participants who don't have the permission to record a meeting.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `disabled` | `boolean` | ✅ | - | Disable the button |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkRecordingToggle } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkRecordingToggle />;
}
```

### With Properties

```tsx
import { RtkRecordingToggle } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkRecordingToggle
      disabled={true}
      meeting={meeting}
      size="md"
    />
  );
}
```
