# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfullscreentoggle/index.md

---

title: RtkFullscreenToggle · Cloudflare Realtime docs
description: API reference for RtkFullscreenToggle component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfullscreentoggle/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfullscreentoggle/index.md
---

A button which toggles full screen mode for any existing `rtk-meeting` component in the DOM.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `targetElement` | `HTMLElement` | ✅ | - | Target Element to fullscreen |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkFullscreenToggle } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkFullscreenToggle />;
}
```

### With Properties

```tsx
import { RtkFullscreenToggle } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkFullscreenToggle
      size="md"
      targetElement={htmlelement}
      variant="button"
    />
  );
}
```
