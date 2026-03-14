# Source: https://www.skeleton.dev/docs/svelte/framework-components/accordion.md

# Source: https://www.skeleton.dev/docs/react/framework-components/accordion.md

# Accordion

Divide content into collapsible sections.

```tsx
import { Accordion } from '@skeletonlabs/skeleton-react';
import { ChevronDownIcon } from 'lucide-react';
import { Fragment } from 'react';

export default function Default() {
	/**
	 * Attribution
	 * @see https://www.healthline.com/health/fun-facts-about-the-skeletal-system#8-More-than-half-your-bones-are-in-your-hands-and-feet
	 */
	const items = [
		{
			id: '1',
			title: 'Your skeleton is made of more than 200 bones',
			description:
				'Inside your body are 206 bones. Each bone plays a very important role in making all the mechanics of your body function properly. If a bone is broken, all the bones around it can’t perform their duty properly.',
		},
		{
			id: '2',
			title: 'The smallest bone in the body is in your ear',
			description:
				'The stapes, a bone in your inner ear, is the smallest of all your bones. This bone is also sometimes called the stirrup because of its Y shape. Together with the anvil and hammer bones, the stapes helps translate sounds you hear into waves your brain can understand.',
		},
		{
			id: '3',
			title: 'One bone isn’t connected to any other bones',
			description:
				'The hyoid bone, which is in your throat, is the only bone that doesn’t connect to a joint. The hyoid is responsible for holding your tongue in place.',
		},
	];
	return (
		<Accordion>
			{items.map((item, i) => (
				<Fragment key={item.id}>
					{i !== 0 && <hr className="hr" />}
					<Accordion.Item value={item.id}>
						<h3>
							<Accordion.ItemTrigger className="font-bold flex items-center justify-between gap-2">
								{item.title}
								<Accordion.ItemIndicator className="group">
									<ChevronDownIcon className="h-5 w-5 transition group-data-[state=open]:rotate-180" />
								</Accordion.ItemIndicator>
							</Accordion.ItemTrigger>
						</h3>
						<Accordion.ItemContent>{item.description}</Accordion.ItemContent>
					</Accordion.Item>
				</Fragment>
			))}
		</Accordion>
	);
}

```

## Controlled

Use the `open` and `onOpenChange` props to control the state.

```tsx
import { Accordion } from '@skeletonlabs/skeleton-react';
import { useState } from 'react';

export default function Controlled() {
	const [value, setValue] = useState(['1']);

	return (
		<Accordion value={value} onValueChange={(details) => setValue(details.value)}>
			{['1', '2', '3'].map((item) => (
				<Accordion.Item key={item} value={item}>
					<h3>
						<Accordion.ItemTrigger>Item {item}</Accordion.ItemTrigger>
					</h3>
					<Accordion.ItemContent>Content for item {item}</Accordion.ItemContent>
				</Accordion.Item>
			))}
		</Accordion>
	);
}

```

## Multiple

Allow multiple accordion items to stay open at once using the `multiple` prop.

```tsx
import { Accordion } from '@skeletonlabs/skeleton-react';

// [!code highlight]

export default function Multiple() {
	return (
		<Accordion multiple>
			{['1', '2', '3'].map((item) => (
				<Accordion.Item key={item} value={item}>
					<h3>
						<Accordion.ItemTrigger>Item {item}</Accordion.ItemTrigger>
					</h3>
					<Accordion.ItemContent>Content for item {item}</Accordion.ItemContent>
				</Accordion.Item>
			))}
		</Accordion>
	);
}

```

## Collapsible

Allow closing all items when one is open using the `collapsible` prop.

```tsx
import { Accordion } from '@skeletonlabs/skeleton-react';

export default function Collapsible() {
	return (
		<Accordion collapsible>
			{['1', '2', '3'].map((item) => (
				<Accordion.Item key={item} value={item}>
					<h3>
						<Accordion.ItemTrigger>Item {item}</Accordion.ItemTrigger>
					</h3>
					<Accordion.ItemContent>Content for item {item}</Accordion.ItemContent>
				</Accordion.Item>
			))}
		</Accordion>
	);
}

```

## Indicator

Add a custom indicator to accordion triggers.

```tsx
import { Accordion } from '@skeletonlabs/skeleton-react';
import { MinusIcon, PlusIcon } from 'lucide-react';

export default function Indicator() {
	return (
		<Accordion>
			{['1', '2', '3'].map((item) => (
				<Accordion.Item key={item} value={item}>
					<h3>
						<Accordion.ItemTrigger className="flex justify-between items-center">
							Item {item}
							<Accordion.ItemIndicator className="group">
								<MinusIcon className="size-4 group-data-[state=open]:block hidden" />
								<PlusIcon className="size-4 group-data-[state=open]:hidden block" />
							</Accordion.ItemIndicator>
						</Accordion.ItemTrigger>
					</h3>
					<Accordion.ItemContent>Content for item {item}</Accordion.ItemContent>
				</Accordion.Item>
			))}
		</Accordion>
	);
}

```

## Orientation

Render the accordion vertically or horizontally using the `orientation` prop.

```tsx
import { Accordion } from '@skeletonlabs/skeleton-react';

export default function Orientation() {
	return (
		<Accordion orientation="horizontal">
			{['1', '2', '3'].map((item) => (
				<Accordion.Item key={item} value={item} className="data-[state=open]:flex-1">
					<h3>
						<Accordion.ItemTrigger>Item {item}</Accordion.ItemTrigger>
					</h3>
					<Accordion.ItemContent>Content for item {item}</Accordion.ItemContent>
				</Accordion.Item>
			))}
		</Accordion>
	);
}

```

## Dir

Set the text direction (`ltr` or `rtl`) using the `dir` prop.

```tsx
import { Accordion } from '@skeletonlabs/skeleton-react';

export default function Dir() {
	return (
		<Accordion dir="rtl">
			{['1', '2', '3'].map((item) => (
				<Accordion.Item key={item} value={item}>
					<h3>
						<Accordion.ItemTrigger>Item {item}</Accordion.ItemTrigger>
					</h3>
					<Accordion.ItemContent>Content for item {item}</Accordion.ItemContent>
				</Accordion.Item>
			))}
		</Accordion>
	);
}

```

## Anatomy

Here's an overview of how the Accordion component is structured in code:

```tsx
import { Accordion } from '@skeletonlabs/skeleton-react';

export default function Anatomy() {
	return (
		<Accordion>
			<Accordion.Item>
				<Accordion.ItemTrigger />
				<Accordion.ItemIndicator />
				<Accordion.ItemContent />
			</Accordion.Item>
		</Accordion>
	);
}
```

## API Reference

### Root

| Prop          | Description                                                                                                           | Type                                                                                                                                                       | Default    |
| ------------- | --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| ids           | The ids of the elements in the accordion. Useful for composition.                                                     | Partial\<\{ root: string; item: (value: string) => string; itemContent: (value: string) => string; itemTrigger: (value: string) => string; }> \| undefined | -          |
| multiple      | Whether multiple accordion items can be expanded at the same time.                                                    | boolean \| undefined                                                                                                                                       | false      |
| collapsible   | Whether an accordion item can be closed after it has been expanded.                                                   | boolean \| undefined                                                                                                                                       | false      |
| value         | The controlled value of the expanded accordion items.                                                                 | string\[] \| undefined                                                                                                                                     | -          |
| defaultValue  | The initial value of the expanded accordion items.&#xA;Use when you don't need to control the value of the accordion. | string\[] \| undefined                                                                                                                                     | -          |
| disabled      | Whether the accordion items are disabled                                                                              | boolean \| undefined                                                                                                                                       | -          |
| onValueChange | The callback fired when the state of expanded/collapsed accordion items changes.                                      | ((details: ValueChangeDetails) => void) \| undefined                                                                                                       | -          |
| onFocusChange | The callback fired when the focused accordion item changes.                                                           | ((details: FocusChangeDetails) => void) \| undefined                                                                                                       | -          |
| orientation   | The orientation of the accordion items.                                                                               | "horizontal" \| "vertical" \| undefined                                                                                                                    | "vertical" |
| dir           | The document's text/writing direction.                                                                                | "ltr" \| "rtl" \| undefined                                                                                                                                | "ltr"      |
| getRootNode   | A root node to correctly resolve document in custom environments. E.x.: Iframes, Electron.                            | (() => ShadowRoot \| Node \| Document) \| undefined                                                                                                        | -          |
| element       | Render the element yourself                                                                                           | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined                                                                                             | -          |

### Provider

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| value   | -                           | AccordionApi\<PropTypes>                                       | -       |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Context

| Prop     | Description | Type                                               | Default |
| -------- | ----------- | -------------------------------------------------- | ------- |
| children | -           | (accordion: AccordionApi\<PropTypes>) => ReactNode | -       |

### Item

| Prop     | Description                             | Type                                                           | Default |
| -------- | --------------------------------------- | -------------------------------------------------------------- | ------- |
| value    | The value of the accordion item.        | string                                                         | -       |
| disabled | Whether the accordion item is disabled. | boolean \| undefined                                           | -       |
| children | -                                       | ReactNode                                                      | -       |
| element  | Render the element yourself             | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### ItemTrigger

| Prop     | Description                 | Type                                                              | Default |
| -------- | --------------------------- | ----------------------------------------------------------------- | ------- |
| children | -                           | ReactNode                                                         | -       |
| element  | Render the element yourself | ((attributes: HTMLAttributes\<"button">) => Element) \| undefined | -       |

### ItemIndicator

| Prop     | Description                 | Type                                                           | Default |
| -------- | --------------------------- | -------------------------------------------------------------- | ------- |
| children | -                           | ReactNode                                                      | -       |
| element  | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### ItemContent

| Prop     | Description                 | Type                                                           | Default |
| -------- | --------------------------- | -------------------------------------------------------------- | ------- |
| children | -                           | ReactNode                                                      | -       |
| element  | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |
