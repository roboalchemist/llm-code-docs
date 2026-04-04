# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktabbar/index.md

---

title: RtkTabBar · Cloudflare Realtime docs
description: API reference for RtkTabBar component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktabbar/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktabbar/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `activeTab` | `Tab` | ✅ | - | Active tab |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | UI Config |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon Pack |
| `layout` | `GridLayout1` | ✅ | - | Grid Layout |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `tabs` | `Tab[]` | ✅ | - | Tabs |

## Usage Examples

### Basic Usage

```tsx
import { RtkTabBar } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkTabBar />;
}
```

### With Properties

```tsx
import { RtkTabBar } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkTabBar
      activeTab={tab}
      layout={gridlayout1}
      meeting={meeting}
    />
  );
}
```
