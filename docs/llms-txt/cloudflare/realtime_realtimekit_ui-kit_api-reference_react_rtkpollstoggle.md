# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpollstoggle/index.md

---

title: RtkPollsToggle · Cloudflare Realtime docs
description: API reference for RtkPollsToggle component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpollstoggle/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpollstoggle/index.md
---

A button which toggles visibility of polls. You need to pass the `meeting` object to it to see the unread polls count badge. When clicked it emits a `rtkStateUpdate` event with the data:

```ts
{ activeSidebar: boolean; sidebar: 'polls' }
```

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkPollsToggle } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkPollsToggle />;
}
```

### With Properties

```tsx
import { RtkPollsToggle } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkPollsToggle
      meeting={meeting}
      size="md"
      variant="button"
    />
  );
}
```
