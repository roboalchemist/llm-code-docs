# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkleavebutton/index.md

---

title: RtkLeaveButton · Cloudflare Realtime docs
description: API reference for RtkLeaveButton component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkleavebutton/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkleavebutton/index.md
---

A button which toggles visilibility of the leave confirmation dialog.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkLeaveButton } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkLeaveButton />;
}
```

### With Properties

```tsx
import { RtkLeaveButton } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkLeaveButton
      size="md"
      variant="button"
    />
  );
}
```
