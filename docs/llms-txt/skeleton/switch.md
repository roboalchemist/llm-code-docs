# Source: https://www.skeleton.dev/docs/svelte/framework-components/switch.md

# Source: https://www.skeleton.dev/docs/react/framework-components/switch.md

# Switch

Toggle between two states, such as on/off.

```tsx
import { Switch } from '@skeletonlabs/skeleton-react';
import { useState } from 'react';

export default function Default() {
	const [checked, setChecked] = useState(false);

	return (
		<div className="flex flex-col items-center gap-4">
			<Switch checked={checked} onCheckedChange={(details) => setChecked(details.checked)}>
				<Switch.Control>
					<Switch.Thumb />
				</Switch.Control>
				<Switch.Label>Label</Switch.Label>
				<Switch.HiddenInput />
			</Switch>
			<p>
				<span className="opacity-60">Checked: </span>
				<code className="code">{checked.toString()}</code>
			</p>
		</div>
	);
}

```

## Color

Use the [Tailwind data attribute syntax](https://tailwindcss.com/docs/hover-focus-and-other-states#data-attributes) to target the state using `data-[state=checked]`

```tsx
import { Switch } from '@skeletonlabs/skeleton-react';

export default function Colors() {
	return (
		<Switch>
			<Switch.Control className="preset-filled-secondary-50-950 data-[state=checked]:preset-filled-secondary-500">
				<Switch.Thumb />
			</Switch.Control>
			<Switch.Label>Label</Switch.Label>
			<Switch.HiddenInput />
		</Switch>
	);
}

```

## List

Use the `Label` component to create a list layout.

```tsx
import { Switch } from '@skeletonlabs/skeleton-react';

export default function List() {
	return (
		<div className="grid gap-2 w-full">
			{['Option 1', 'Option 2', 'Option 3'].map((label, i) => (
				<div key={label}>
					<Switch className="flex justify-between p-2">
						<Switch.Label>{label}</Switch.Label>
						<Switch.Control>
							<Switch.Thumb />
						</Switch.Control>
						<Switch.HiddenInput />
					</Switch>
					{i < 2 && <hr className="hr" />}
				</div>
			))}
		</div>
	);
}

```

## Icons

Add icons to act as state indicators.

```tsx
import { Switch } from '@skeletonlabs/skeleton-react';
import { MoonIcon, SunIcon } from 'lucide-react';

export default function ThumbIcons() {
	return (
		<Switch>
			<Switch.HiddenInput />
			<Switch.Control>
				<Switch.Thumb>
					<Switch.Context>
						{(switch_) => (switch_.checked ? <SunIcon className="size-3" /> : <MoonIcon className="size-3" />)}
					</Switch.Context>
				</Switch.Thumb>
			</Switch.Control>
			<Switch.Label>Label</Switch.Label>
		</Switch>
	);
}

```

## Direction

Set the text direction (`ltr` or `rtl`) using the `dir` prop.

```tsx
import { Switch } from '@skeletonlabs/skeleton-react';

export default function Dir() {
	return (
		<Switch dir="rtl">
			<Switch.Control>
				<Switch.Thumb />
			</Switch.Control>
			<Switch.Label>Label</Switch.Label>
			<Switch.HiddenInput />
		</Switch>
	);
}

```

## Anatomy

Here's an overview of how the Switch component is structured in code:

```tsx
import { Switch } from '@skeletonlabs/skeleton-react';

export default function Anatomy() {
	return (
		<Switch>
			<Switch.Control>
				<Switch.Thumb />
			</Switch.Control>
			<Switch.Label />
			<Switch.HiddenInput />
		</Switch>
	);
}
```

## API Reference

### Root

| Prop            | Description                                                                                                                    | Type                                                                                                          | Default |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------- | ------- |
| ids             | The ids of the elements in the switch. Useful for composition.                                                                 | Partial\<\{ root: string; hiddenInput: string; control: string; label: string; thumb: string; }> \| undefined | -       |
| label           | Specifies the localized strings that identifies the accessibility elements and their states                                    | string \| undefined                                                                                           | -       |
| disabled        | Whether the switch is disabled.                                                                                                | boolean \| undefined                                                                                          | -       |
| invalid         | If \`true\`, the switch is marked as invalid.                                                                                  | boolean \| undefined                                                                                          | -       |
| required        | If \`true\`, the switch input is marked as required,                                                                           | boolean \| undefined                                                                                          | -       |
| readOnly        | Whether the switch is read-only                                                                                                | boolean \| undefined                                                                                          | -       |
| onCheckedChange | Function to call when the switch is clicked.                                                                                   | ((details: CheckedChangeDetails) => void) \| undefined                                                        | -       |
| checked         | The controlled checked state of the switch                                                                                     | boolean \| undefined                                                                                          | -       |
| defaultChecked  | The initial checked state of the switch when rendered.&#xA;Use when you don't need to control the checked state of the switch. | boolean \| undefined                                                                                          | -       |
| name            | The name of the input field in a switch&#xA;(Useful for form submission).                                                      | string \| undefined                                                                                           | -       |
| form            | The id of the form that the switch belongs to                                                                                  | string \| undefined                                                                                           | -       |
| value           | The value of switch input. Useful for form submission.                                                                         | string \| number \| undefined                                                                                 | "on"    |
| dir             | The document's text/writing direction.                                                                                         | "ltr" \| "rtl" \| undefined                                                                                   | "ltr"   |
| getRootNode     | A root node to correctly resolve document in custom environments. E.x.: Iframes, Electron.                                     | (() => ShadowRoot \| Node \| Document) \| undefined                                                           | -       |
| element         | Render the element yourself                                                                                                    | ((attributes: HTMLAttributes\<"label">) => Element) \| undefined                                              | -       |

### Provider

| Prop    | Description                 | Type                                                             | Default |
| ------- | --------------------------- | ---------------------------------------------------------------- | ------- |
| value   | -                           | SwitchApi\<PropTypes>                                            | -       |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"label">) => Element) \| undefined | -       |

### Context

| Prop     | Description | Type                                           | Default |
| -------- | ----------- | ---------------------------------------------- | ------- |
| children | -           | (switch\_: SwitchApi\<PropTypes>) => ReactNode | -       |

### Control

| Prop    | Description                 | Type                                                            | Default |
| ------- | --------------------------- | --------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"span">) => Element) \| undefined | -       |

### Thumb

| Prop    | Description                 | Type                                                            | Default |
| ------- | --------------------------- | --------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"span">) => Element) \| undefined | -       |

### Label

| Prop    | Description                 | Type                                                            | Default |
| ------- | --------------------------- | --------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"span">) => Element) \| undefined | -       |

### HiddenInput

| Prop    | Description                 | Type                                                             | Default |
| ------- | --------------------------- | ---------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"input">) => Element) \| undefined | -       |
