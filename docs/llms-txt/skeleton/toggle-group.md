# Source: https://www.skeleton.dev/docs/svelte/framework-components/toggle-group.md

# Source: https://www.skeleton.dev/docs/react/framework-components/toggle-group.md

# Toggle Group

Grouped buttons for toggling option states.

```tsx
import { ToggleGroup } from '@skeletonlabs/skeleton-react';
import { BoldIcon, ItalicIcon, UnderlineIcon } from 'lucide-react';

export default function Default() {
	return (
		<ToggleGroup defaultValue={['bold']} multiple>
			<ToggleGroup.Item value="bold">
				<BoldIcon className="size-4" />
			</ToggleGroup.Item>
			<ToggleGroup.Item value="italic">
				<ItalicIcon className="size-4" />
			</ToggleGroup.Item>
			<ToggleGroup.Item value="underline">
				<UnderlineIcon className="size-4" />
			</ToggleGroup.Item>
		</ToggleGroup>
	);
}

```

## Controlled

Use the `value` and `onValueChange` props to control state programmatically.

```tsx
import { ToggleGroup } from '@skeletonlabs/skeleton-react';
import { BoldIcon, ItalicIcon, UnderlineIcon } from 'lucide-react';
import { useState } from 'react';

export default function Controlled() {
	const [value, setValue] = useState(['bold']);

	return (
		<div className="flex flex-col items-center gap-4">
			<ToggleGroup value={value} onValueChange={(details) => setValue(details.value)} multiple>
				<ToggleGroup.Item value="bold">
					<BoldIcon className="size-4" />
				</ToggleGroup.Item>
				<ToggleGroup.Item value="italic">
					<ItalicIcon className="size-4" />
				</ToggleGroup.Item>
				<ToggleGroup.Item value="underline">
					<UnderlineIcon className="size-4" />
				</ToggleGroup.Item>
			</ToggleGroup>

			{/* Message */}
			<p>
				<span className="opacity-60">You selected</span> <code className="code">{value.length > 0 ? value.join(', ') : 'none'}</code>
			</p>
		</div>
	);
}

```

## Orientation

Using the `orientation` prop to control the layout.

```tsx
import { ToggleGroup } from '@skeletonlabs/skeleton-react';
import { BoldIcon, ItalicIcon, UnderlineIcon } from 'lucide-react';

export default function Orientation() {
	return (
		<div className="flex flex-col items-center gap-4">
			<p>Horizontal</p>
			<ToggleGroup defaultValue={['bold']} multiple orientation="horizontal">
				<ToggleGroup.Item value="bold">
					<BoldIcon className="size-4" />
				</ToggleGroup.Item>
				<ToggleGroup.Item value="italic">
					<ItalicIcon className="size-4" />
				</ToggleGroup.Item>
				<ToggleGroup.Item value="underline">
					<UnderlineIcon className="size-4" />
				</ToggleGroup.Item>
			</ToggleGroup>

			<p>Vertical</p>
			<ToggleGroup defaultValue={['bold']} multiple orientation="vertical" className="flex-col">
				<ToggleGroup.Item value="bold">
					<BoldIcon className="size-4" />
				</ToggleGroup.Item>
				<ToggleGroup.Item value="italic">
					<ItalicIcon className="size-4" />
				</ToggleGroup.Item>
				<ToggleGroup.Item value="underline">
					<UnderlineIcon className="size-4" />
				</ToggleGroup.Item>
			</ToggleGroup>
		</div>
	);
}

```

## Direction

Set the text direction (`ltr` or `rtl`) using the `dir` prop.

```tsx
import { ToggleGroup } from '@skeletonlabs/skeleton-react';
import { BoldIcon, ItalicIcon, UnderlineIcon } from 'lucide-react';

export default function Dir() {
	return (
		<ToggleGroup defaultValue={['bold']} multiple dir="rtl">
			<ToggleGroup.Item value="bold">
				<BoldIcon className="size-4" />
			</ToggleGroup.Item>
			<ToggleGroup.Item value="italic">
				<ItalicIcon className="size-4" />
			</ToggleGroup.Item>
			<ToggleGroup.Item value="underline">
				<UnderlineIcon className="size-4" />
			</ToggleGroup.Item>
		</ToggleGroup>
	);
}

```

## Anatomy

Here's an overview of how the ToggleGroup component is structured in code:

```tsx
import { ToggleGroup } from '@skeletonlabs/skeleton-react';

export default function Anatomy() {
	return (
		<ToggleGroup>
			<ToggleGroup.Item />
		</ToggleGroup>
	);
}
```

## API Reference

### Root

| Prop          | Description                                                                                                                                  | Type                                                                       | Default      |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ------------ |
| ids           | The ids of the elements in the toggle. Useful for composition.                                                                               | Partial\<\{ root: string; item: (value: string) => string; }> \| undefined | -            |
| disabled      | Whether the toggle is disabled.                                                                                                              | boolean \| undefined                                                       | -            |
| value         | The controlled selected value of the toggle group.                                                                                           | string\[] \| undefined                                                     | -            |
| defaultValue  | The initial selected value of the toggle group when rendered.&#xA;Use when you don't need to control the selected value of the toggle group. | string\[] \| undefined                                                     | -            |
| onValueChange | Function to call when the toggle is clicked.                                                                                                 | ((details: ValueChangeDetails) => void) \| undefined                       | -            |
| loopFocus     | Whether to loop focus inside the toggle group.                                                                                               | boolean \| undefined                                                       | true         |
| rovingFocus   | Whether to use roving tab index to manage focus.                                                                                             | boolean \| undefined                                                       | true         |
| orientation   | The orientation of the toggle group.                                                                                                         | Orientation \| undefined                                                   | "horizontal" |
| multiple      | Whether to allow multiple toggles to be selected.                                                                                            | boolean \| undefined                                                       | -            |
| deselectable  | Whether the toggle group allows empty selection.&#xA;\*\*Note:\*\* This is ignored if \`multiple\` is \`true\`.                              | boolean \| undefined                                                       | true         |
| dir           | The document's text/writing direction.                                                                                                       | "ltr" \| "rtl" \| undefined                                                | "ltr"        |
| getRootNode   | A root node to correctly resolve document in custom environments. E.x.: Iframes, Electron.                                                   | (() => ShadowRoot \| Node \| Document) \| undefined                        | -            |
| element       | Render the element yourself                                                                                                                  | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined             | -            |

### Provider

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| value   | -                           | ToggleGroupApi\<PropTypes>                                     | -       |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Context

| Prop     | Description | Type                                                   | Default |
| -------- | ----------- | ------------------------------------------------------ | ------- |
| children | -           | (togglegroup: ToggleGroupApi\<PropTypes>) => ReactNode | -       |

### Item

| Prop     | Description                 | Type                                                              | Default |
| -------- | --------------------------- | ----------------------------------------------------------------- | ------- |
| value    | -                           | string                                                            | -       |
| disabled | -                           | boolean \| undefined                                              | -       |
| element  | Render the element yourself | ((attributes: HTMLAttributes\<"button">) => Element) \| undefined | -       |
