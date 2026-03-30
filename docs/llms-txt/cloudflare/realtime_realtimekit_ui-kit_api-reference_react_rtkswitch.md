# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkswitch/index.md

---

title: RtkSwitch · Cloudflare Realtime docs
description: API reference for RtkSwitch component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkswitch/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkswitch/index.md
---

A switch component which follows RTK Design System.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `checked` | `boolean` | ✅ | - | Whether the switch is enabled/checked |
| `disabled` | `boolean` | ✅ | - | Whether switch is readonly |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `readonly` | `boolean` | ✅ | - | Whether switch is readonly |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkSwitch } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkSwitch />;
}
```

### With Properties

```tsx
import { RtkSwitch } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkSwitch
      checked={true}
      disabled={true}
      readonly={true}
    />
  );
}
```
