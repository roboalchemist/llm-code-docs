# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmenulist/index.md

---

title: RtkMenuList · Cloudflare Realtime docs
description: API reference for RtkMenuList component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmenulist/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmenulist/index.md
---

A menu list component.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `menuVariant` | `'primary' \| 'secondary'` | ✅ | - | Variant |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkMenuList } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkMenuList />;
}
```

### With Properties

```tsx
import { RtkMenuList } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkMenuList
      menuVariant={'primary' | 'secondary'}
    />
  );
}
```
