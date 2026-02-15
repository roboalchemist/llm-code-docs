# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksidebar/index.md

---

title: RtkSidebar · Cloudflare Realtime docs
description: API reference for RtkSidebar component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksidebar/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksidebar/index.md
---

A component which handles the sidebar and you can customize which sections you want, and which section you want as the default.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config |
| `defaultSection` | `RtkSidebarSection` | ✅ | - | Default section |
| `enabledSections` | `RtkSidebarTab[]` | ✅ | - | Enabled sections in sidebar |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `view` | `RtkSidebarView` | ✅ | - | View type |

## Usage Examples

### Basic Usage

```tsx
import { RtkSidebar } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkSidebar />;
}
```

### With Properties

```tsx
import { RtkSidebar } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkSidebar
      defaultSection={rtksidebarsection}
      enabledSections={[]}
      meeting={meeting}
    />
  );
}
```
