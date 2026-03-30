# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfilepickerbutton/index.md

---

title: RtkFilePickerButton · Cloudflare Realtime docs
description: API reference for RtkFilePickerButton component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfilepickerbutton/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfilepickerbutton/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `filter` | `string` | ✅ | - | File type filter to open file picker with |
| `icon` | `keyof IconPack1` | ✅ | - | Icon |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `label` | `string` | ✅ | - | Label for tooltip |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkFilePickerButton } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkFilePickerButton />;
}
```

### With Properties

```tsx
import { RtkFilePickerButton } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkFilePickerButton
      filter="example"
      icon={defaultIconPack}
      label="example"
    />
  );
}
```
