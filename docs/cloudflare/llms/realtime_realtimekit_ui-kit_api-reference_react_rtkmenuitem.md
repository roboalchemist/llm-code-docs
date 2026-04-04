# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmenuitem/index.md

---

title: RtkMenuItem · Cloudflare Realtime docs
description: API reference for RtkMenuItem component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmenuitem/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmenuitem/index.md
---

A menu item component.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `menuVariant` | `'primary' \| 'secondary'` | ✅ | - | Variant |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkMenuItem } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkMenuItem />;
}
```

### With Properties

```tsx
import { RtkMenuItem } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkMenuItem
      menuVariant={'primary' | 'secondary'}
      size="md"
    />
  );
}
```
