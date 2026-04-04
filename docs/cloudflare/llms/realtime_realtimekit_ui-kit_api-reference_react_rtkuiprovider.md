# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkuiprovider/index.md

---

title: RtkUiProvider · Cloudflare Realtime docs
description: API reference for RtkUiProvider component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkuiprovider/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkuiprovider/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `config` | `UIConfig1` | ✅ | - | Config |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting \| null` | ❌ | `null` | Meeting |
| `mode` | `MeetingMode1` | ✅ | - | Fill type |
| `overrides` | `Overrides1` | ❌ | `defaultOverrides` | UI Kit Overrides |
| `showSetupScreen` | `boolean` | ✅ | - | Whether to show setup screen or not |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language utility |

## Usage Examples

### Basic Usage

```tsx
import { RtkUiProvider } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkUiProvider />;
}
```

### With Properties

```tsx
import { RtkUiProvider } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkUiProvider
      config={defaultUiConfig}
      mode={meeting}
      showSetupScreen={true}
    />
  );
}
```
