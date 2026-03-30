# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtklogo/index.md

---

title: RtkLogo · Cloudflare Realtime docs
description: API reference for RtkLogo component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtklogo/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtklogo/index.md
---

A component which loads the logo from your config, or via the `logo-url` attribute.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config object |
| `logoUrl` | `string` | ✅ | - | Logo URL |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkLogo } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkLogo />;
}
```

### With Properties

```tsx
import { RtkLogo } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkLogo
      logoUrl="example"
      meeting={meeting}
    />
  );
}
```
