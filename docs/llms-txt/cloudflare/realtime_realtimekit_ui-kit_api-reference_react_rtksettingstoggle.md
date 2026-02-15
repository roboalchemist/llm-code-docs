# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksettingstoggle/index.md

---

title: RtkSettingsToggle · Cloudflare Realtime docs
description: API reference for RtkSettingsToggle component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksettingstoggle/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksettingstoggle/index.md
---

A button which toggles visibility of settings module. When clicked it emits a `rtkStateUpdate` event with the data:

```ts
{ activeSettings: boolean; }
```

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkSettingsToggle } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkSettingsToggle />;
}
```

### With Properties

```tsx
import { RtkSettingsToggle } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkSettingsToggle
      size="md"
      variant="button"
    />
  );
}
```
