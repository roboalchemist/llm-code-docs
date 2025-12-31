# Source: https://react-spectrum.adobe.com/AvatarGroup.md

# AvatarGroup

An avatar group is a grouping of avatars that are related to each other.

```tsx
import {AvatarGroup, Avatar} from '@react-spectrum/s2';

<AvatarGroup>
  <Avatar
    alt="Abraham Baker"
    src="https://www.untitledui.com/images/avatars/abraham-baker" />
  <Avatar
    alt="Adriana Sullivan"
    src="https://www.untitledui.com/images/avatars/adriana-sullivan" />
  <Avatar
    alt="Jonathan Kelly"
    src="https://www.untitledui.com/images/avatars/jonathan-kelly" />
  <Avatar
    alt="Zara Bush"
    src="https://www.untitledui.com/images/avatars/zara-bush" />
</AvatarGroup>
```

## API

```tsx
<AvatarGroup>
  <Avatar />
</AvatarGroup>
```

### AvatarGroup

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `aria-describedby` | `string | undefined` | â | Identifies the element (or elements) that describes the object. |
| `aria-details` | `string | undefined` | â | Identifies the element (or elements) that provide a detailed, extended description for the object. |
| `aria-label` | `string | undefined` | â | Defines a string value that labels the current element. |
| `aria-labelledby` | `string | undefined` | â | Identifies the element (or elements) that labels the current element. |
| `children` | `ReactNode` | â | Avatar children of the avatar group. |
| `id` | `string | undefined` | â | The element's unique identifier. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id). |
| `label` | `string | undefined` | â | The label for the avatar group. |
| `size` | `28 | 16 | 20 | 24 | 32 | 36 | 40 | undefined` | 24 | The size of the avatar group. |
| `slot` | `string | null | undefined` | â | A slot name for the component. Slots allow the component to receive props from a parent component. An explicit `null` value indicates that the local props completely override all props received from a parent. |
| `styles` | `StylesPropWithoutWidth | undefined` | â | Spectrum-defined styles, returned by the `style()` macro. |
| `UNSAFE_className` | `UnsafeClassName | undefined` | â | Sets the CSS [className](https://developer.mozilla.org/en-US/docs/Web/API/Element/className) for the element. Only use as a **last resort**. Use the `style` macro via the `styles` prop instead. |
| `UNSAFE_style` | `CSSProperties | undefined` | â | Sets inline [style](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style) for the element. Only use as a **last resort**. Use the `style` macro via the `styles` prop instead. |
