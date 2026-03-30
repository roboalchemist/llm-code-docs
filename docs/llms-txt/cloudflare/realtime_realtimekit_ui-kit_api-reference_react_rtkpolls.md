# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpolls/index.md

---

title: RtkPolls · Cloudflare Realtime docs
description: API reference for RtkPolls component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpolls/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpolls/index.md
---

A component which lists all available plugins a user can access with the ability to enable or disable them as per their permissions.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkPolls } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkPolls />;
}
```

### With Properties

```tsx
import { RtkPolls } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkPolls
      meeting={meeting}
      size="md"
    />
  );
}
```
