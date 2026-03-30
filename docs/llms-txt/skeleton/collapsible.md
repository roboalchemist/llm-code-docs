# Source: https://www.skeleton.dev/docs/svelte/framework-components/collapsible.md

# Source: https://www.skeleton.dev/docs/react/framework-components/collapsible.md

# Collapsible

A container that can be expanded or collapsed to show or hide content.

```tsx
import { Collapsible } from '@skeletonlabs/skeleton-react';
import { ArrowUpDownIcon } from 'lucide-react';

export default function Default() {
	return (
		<Collapsible className="items-start card preset-filled-surface-100-900 p-4 w-56 mx-auto">
			<div className="w-full flex justify-between items-center">
				<p className="font-bold">Design System</p>
				<Collapsible.Trigger className="btn-icon hover:preset-tonal">
					<ArrowUpDownIcon className="size-4" />
				</Collapsible.Trigger>
			</div>
			<Collapsible.Content className="flex flex-col gap-2">
				<nav className="contents">
					<a className="anchor" href="/docs/design/themes">
						Themes
					</a>
					<a className="anchor" href="/docs/design/colors">
						Colors
					</a>
					<a className="anchor" href="/docs/design/presets">
						Presets
					</a>
					<a className="anchor" href="/docs/design/typography">
						Typography
					</a>
					<a className="anchor" href="/docs/design/spacing">
						Spacing
					</a>
					<a className="anchor" href="/docs/design/iconography">
						Iconography
					</a>
				</nav>
			</Collapsible.Content>
		</Collapsible>
	);
}

```

## Controlled

Control the active state of the component.

```tsx
import { Collapsible } from '@skeletonlabs/skeleton-react';
import { useState } from 'react';

export default function Controlled() {
	const [open, setOpen] = useState(false);

	return (
		<Collapsible open={open} onOpenChange={(details) => setOpen(details.open)}>
			<Collapsible.Content>
				The world dies over and over again, but the skeleton always gets up and walks. Every heart has its own skeletons. The bones of the
				skeleton which support the body can become the bars of the cage which imprison the spirit.
			</Collapsible.Content>
			<Collapsible.Trigger className="btn preset-filled">Show {open ? 'Less' : 'More'}</Collapsible.Trigger>
		</Collapsible>
	);
}

```

## Indicator

Add a visual indicator to the toggle button.

```tsx
import { Collapsible } from '@skeletonlabs/skeleton-react';
import { MinusIcon, PlusIcon } from 'lucide-react';

export default function Default() {
	return (
		<Collapsible>
			<Collapsible.Content>
				The world dies over and over again, but the skeleton always gets up and walks. Every heart has its own skeletons. The bones of the
				skeleton which support the body can become the bars of the cage which imprison the spirit.
			</Collapsible.Content>
			<Collapsible.Trigger className="btn preset-filled">
				<span>Toggle</span>
				<Collapsible.Indicator className="group">
					<MinusIcon className="size-4 group-data-[state=open]:block hidden" />
					<PlusIcon className="size-4 group-data-[state=open]:hidden block" />
				</Collapsible.Indicator>
			</Collapsible.Trigger>
		</Collapsible>
	);
}

```

## Disabled

Set the disabled state for the component.

```tsx
import { Collapsible } from '@skeletonlabs/skeleton-react';

export default function Disabled() {
	return (
		<Collapsible disabled>
			<Collapsible.Content>Hidden!</Collapsible.Content>
			<Collapsible.Trigger className="btn preset-filled">Toggle</Collapsible.Trigger>
		</Collapsible>
	);
}

```

## Alignment

Control the position and alignment of the trigger and content using flexbox `items-*`.

```tsx
import { Collapsible } from '@skeletonlabs/skeleton-react';

export default function Alignment() {
	return (
		<Collapsible className="items-start">
			<Collapsible.Content>
				The world dies over and over again, but the skeleton always gets up and walks. Every heart has its own skeletons. The bones of the
				skeleton which support the body can become the bars of the cage which imprison the spirit.
			</Collapsible.Content>
			<Collapsible.Trigger className="btn preset-filled">Toggle</Collapsible.Trigger>
		</Collapsible>
	);
}

```

## Direction

Set the text direction (`ltr` or `rtl`) using the `dir` prop.

```tsx
import { Collapsible } from '@skeletonlabs/skeleton-react';

export default function Dir() {
	return (
		<Collapsible dir="rtl">
			<Collapsible.Content>
				The world dies over and over again, but the skeleton always gets up and walks. Every heart has its own skeletons. The bones of the
				skeleton which support the body can become the bars of the cage which imprison the spirit.
			</Collapsible.Content>
			<Collapsible.Trigger className="btn preset-filled">Toggle</Collapsible.Trigger>
		</Collapsible>
	);
}

```

## Anatomy

Here's an overview of how the Collapsible component is structured in code:

```tsx
import { Collapsible } from '@skeletonlabs/skeleton-react';

export default function Anatomy() {
	return (
		<Collapsible>
			<Collapsible.Trigger />
			<Collapsible.Content />
		</Collapsible>
	);
}
```

## API Reference

### Root

| Prop            | Description                                                                                                                        | Type                                                                        | Default |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | ------- |
| ids             | The ids of the elements in the collapsible. Useful for composition.                                                                | Partial\<\{ root: string; content: string; trigger: string; }> \| undefined | -       |
| open            | The controlled open state of the collapsible.                                                                                      | boolean \| undefined                                                        | -       |
| defaultOpen     | The initial open state of the collapsible when rendered.&#xA;Use when you don't need to control the open state of the collapsible. | boolean \| undefined                                                        | -       |
| onOpenChange    | The callback invoked when the open state changes.                                                                                  | ((details: OpenChangeDetails) => void) \| undefined                         | -       |
| onExitComplete  | The callback invoked when the exit animation completes.                                                                            | VoidFunction \| undefined                                                   | -       |
| disabled        | Whether the collapsible is disabled.                                                                                               | boolean \| undefined                                                        | -       |
| collapsedHeight | The height of the content when collapsed.                                                                                          | string \| number \| undefined                                               | -       |
| collapsedWidth  | The width of the content when collapsed.                                                                                           | string \| number \| undefined                                               | -       |
| getRootNode     | A root node to correctly resolve document in custom environments. E.x.: Iframes, Electron.                                         | (() => ShadowRoot \| Node \| Document) \| undefined                         | -       |
| dir             | The document's text/writing direction.                                                                                             | "ltr" \| "rtl" \| undefined                                                 | "ltr"   |
| element         | Render the element yourself                                                                                                        | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined              | -       |

### Provider

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| value   | -                           | CollapsibleApi\<PropTypes>                                     | -       |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Context

| Prop     | Description | Type                                                   | Default |
| -------- | ----------- | ------------------------------------------------------ | ------- |
| children | -           | (collapsible: CollapsibleApi\<PropTypes>) => ReactNode | -       |

### Trigger

| Prop    | Description                 | Type                                                              | Default |
| ------- | --------------------------- | ----------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"button">) => Element) \| undefined | -       |

### Indicator

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Content

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |
