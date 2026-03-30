# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmoretoggle/index.md

---

title: RtkMoreToggle · Cloudflare Realtime docs
description: API reference for RtkMoreToggle component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmoretoggle/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmoretoggle/index.md
---

A button which toggles visibility of a more menu. When clicked it emits a `rtkStateUpdate` event with the data:

```ts
{ activeMoreMenu: boolean; }
```

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkMoreToggle } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkMoreToggle />;
}
```

### With Properties

```tsx
import { RtkMoreToggle } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkMoreToggle
      size="md"
    />
  );
}
```
