# Source: https://www.skeleton.dev/docs/svelte/framework-components/listbox.md

# Source: https://www.skeleton.dev/docs/react/framework-components/listbox.md

# Listbox

Accessible listbox for single and multi selection.

```tsx
import { Listbox, useListCollection } from '@skeletonlabs/skeleton-react';

const data = [
	{ label: 'Apple', value: 'apple' },
	{ label: 'Banana', value: 'banana' },
	{ label: 'Orange', value: 'orange' },
	{ label: 'Carrot', value: 'carrot' },
	{ label: 'Broccoli', value: 'broccoli' },
	{ label: 'Spinach', value: 'spinach' },
];

export default function Default() {
	const collection = useListCollection({
		items: data,
		itemToString: (item) => item.label,
		itemToValue: (item) => item.value,
	});

	return (
		<Listbox className="w-full max-w-md" collection={collection}>
			<Listbox.Label>Select a food</Listbox.Label>
			<Listbox.Content>
				{collection.items.map((item) => (
					<Listbox.Item key={item.value} item={item}>
						<Listbox.ItemText>{item.label}</Listbox.ItemText>
						<Listbox.ItemIndicator />
					</Listbox.Item>
				))}
			</Listbox.Content>
		</Listbox>
	);
}

```

## Groups

Organize items into categorized groups.

```tsx
import { Listbox, useListCollection } from '@skeletonlabs/skeleton-react';

const data = [
	{ label: 'Apple', value: 'apple', type: 'Fruits' },
	{ label: 'Banana', value: 'banana', type: 'Fruits' },
	{ label: 'Orange', value: 'orange', type: 'Fruits' },
	{ label: 'Carrot', value: 'carrot', type: 'Vegetables' },
	{ label: 'Broccoli', value: 'broccoli', type: 'Vegetables' },
	{ label: 'Spinach', value: 'spinach', type: 'Vegetables' },
];

export default function Group() {
	const collection = useListCollection({
		items: data,
		itemToString: (item) => item.label,
		itemToValue: (item) => item.value,
		groupBy: (item) => item.type,
	});

	return (
		<Listbox className="w-full max-w-md" collection={collection}>
			<Listbox.Content>
				{collection.group().map(([type, items]) => (
					<Listbox.ItemGroup key={type}>
						<Listbox.ItemGroupLabel>{type}</Listbox.ItemGroupLabel>
						{items.map((item) => (
							<Listbox.Item key={item.value} item={item}>
								<Listbox.ItemText>{item.label}</Listbox.ItemText>
								<Listbox.ItemIndicator />
							</Listbox.Item>
						))}
					</Listbox.ItemGroup>
				))}
			</Listbox.Content>
		</Listbox>
	);
}

```

## Multiple

Set the `multiple` proper to allow selecting more than one item.

```tsx
import { Listbox, useListCollection } from '@skeletonlabs/skeleton-react';

const data = [
	{ label: 'Apple', value: 'apple' },
	{ label: 'Banana', value: 'banana' },
	{ label: 'Orange', value: 'orange' },
	{ label: 'Carrot', value: 'carrot' },
	{ label: 'Broccoli', value: 'broccoli' },
	{ label: 'Spinach', value: 'spinach' },
];

export default function Multiple() {
	const collection = useListCollection({
		items: data,
		itemToString: (item) => item.label,
		itemToValue: (item) => item.value,
	});

	return (
		<Listbox className="w-full max-w-md" collection={collection} selectionMode="multiple">
			<Listbox.Content>
				{collection.items.map((item) => (
					<Listbox.Item key={item.value} item={item}>
						<Listbox.ItemText>{item.label}</Listbox.ItemText>
						<Listbox.ItemIndicator />
					</Listbox.Item>
				))}
			</Listbox.Content>
		</Listbox>
	);
}

```

## Disabled

Set the `disabled` prop to enable the disabled state.

```tsx
import { Listbox, useListCollection } from '@skeletonlabs/skeleton-react';

const data = [
	{ label: 'Apple', value: 'apple' },
	{ label: 'Banana', value: 'banana' },
	{ label: 'Orange', value: 'orange' },
	{ label: 'Carrot', value: 'carrot' },
	{ label: 'Broccoli', value: 'broccoli' },
	{ label: 'Spinach', value: 'spinach' },
];

export default function Disabled() {
	const collection = useListCollection({
		items: data,
		itemToString: (item) => item.label,
		itemToValue: (item) => item.value,
	});

	return (
		<Listbox className="w-full max-w-md" collection={collection} disabled={true}>
			<Listbox.Content>
				{collection.items.map((item) => (
					<Listbox.Item key={item.value} item={item}>
						<Listbox.ItemText>{item.label}</Listbox.ItemText>
						<Listbox.ItemIndicator />
					</Listbox.Item>
				))}
			</Listbox.Content>
		</Listbox>
	);
}

```

Which can also be enabled per item.

```tsx
import { Listbox, useListCollection } from '@skeletonlabs/skeleton-react';

const data = [
	{ label: 'Apple', value: 'apple' },
	{ label: 'Banana', value: 'banana' },
	{ label: 'Orange', value: 'orange' },
	{ label: 'Carrot', value: 'carrot' },
	{ label: 'Broccoli', value: 'broccoli' },
	{ label: 'Spinach', value: 'spinach' },
];

export default function DisabledItem() {
	const collection = useListCollection({
		items: data,
		itemToString: (item) => item.label,
		itemToValue: (item) => item.value,
		isItemDisabled: (item) => item.value === 'banana',
	});

	return (
		<Listbox className="w-full max-w-md" collection={collection}>
			<Listbox.Content>
				{collection.items.map((item) => (
					<Listbox.Item key={item.value} item={item}>
						<Listbox.ItemText>{item.label}</Listbox.ItemText>
						<Listbox.ItemIndicator />
					</Listbox.Item>
				))}
			</Listbox.Content>
		</Listbox>
	);
}

```

## Search

Utilize the `Input` component to implement simple search.

```tsx
import { Listbox, useListCollection } from '@skeletonlabs/skeleton-react';
import { useMemo, useState } from 'react';

const data = [
	{ label: 'Apple', value: 'apple' },
	{ label: 'Banana', value: 'banana' },
	{ label: 'Orange', value: 'orange' },
	{ label: 'Carrot', value: 'carrot' },
	{ label: 'Broccoli', value: 'broccoli' },
	{ label: 'Spinach', value: 'spinach' },
];

export default function Search() {
	const [query, setQuery] = useState('');

	const collection = useMemo(() => {
		const items = data.filter((item) => item.label.toLowerCase().includes(query.toLowerCase()));
		return useListCollection({ items });
	}, [query]);

	return (
		<Listbox className="w-full max-w-md" collection={collection}>
			<Listbox.Label>Search for Food</Listbox.Label>
			<Listbox.Input placeholder="Type to search..." value={query} onInput={(e) => setQuery(e.currentTarget.value)} />
			<Listbox.Content>
				{collection.items.map((item) => (
					<Listbox.Item key={item.value} item={item}>
						<Listbox.ItemText>{item.label}</Listbox.ItemText>
						<Listbox.ItemIndicator />
					</Listbox.Item>
				))}
			</Listbox.Content>
		</Listbox>
	);
}

```

## Direction

Set the text direction (`ltr` or `rtl`) using the `dir` prop.

```tsx
import { Listbox, useListCollection } from '@skeletonlabs/skeleton-react';

const data = [
	{ label: 'Apple', value: 'apple' },
	{ label: 'Banana', value: 'banana' },
	{ label: 'Orange', value: 'orange' },
	{ label: 'Carrot', value: 'carrot' },
	{ label: 'Broccoli', value: 'broccoli' },
	{ label: 'Spinach', value: 'spinach' },
];

export default function Dir() {
	const collection = useListCollection({
		items: data,
		itemToString: (item) => item.label,
		itemToValue: (item) => item.value,
	});

	return (
		<Listbox className="w-full max-w-md" collection={collection} dir="rtl">
			<Listbox.Label>Select a food</Listbox.Label>
			<Listbox.Content>
				{collection.items.map((item) => (
					<Listbox.Item key={item.value} item={item}>
						<Listbox.ItemText>{item.label}</Listbox.ItemText>
						<Listbox.ItemIndicator />
					</Listbox.Item>
				))}
			</Listbox.Content>
		</Listbox>
	);
}

```

## Anatomy

Here's an overview of how the Listbox component is structured in code:

```tsx
import { Listbox } from '@skeletonlabs/skeleton-react';

export default function Anatomy() {
	return (
		<Listbox>
			<Listbox.Label />
			<Listbox.Content>
				<Listbox.Item>
					<Listbox.ItemText />
					<Listbox.ItemIndicator />
				</Listbox.Item>
			</Listbox.Content>
		</Listbox>
	);
}
```

## API Reference

### Root

| Prop                    | Description                                                                                                                                                                                                                                                                       | Type                                                                                                                                                                                                             | Default    |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| orientation             | The orientation of the listbox.                                                                                                                                                                                                                                                   | "horizontal" \| "vertical" \| undefined                                                                                                                                                                          | "vertical" |
| collection              | The item collection                                                                                                                                                                                                                                                               | ListCollection\<any> \| GridCollection\<any>                                                                                                                                                                     | -          |
| ids                     | The ids of the elements in the listbox. Useful for composition.                                                                                                                                                                                                                   | Partial\<\{ root: string; content: string; label: string; item: (id: string \| number) => string; itemGroup: (id: string \| number) => string; itemGroupLabel: (id: string \| number) => string; }> \| undefined | -          |
| disabled                | Whether the listbox is disabled                                                                                                                                                                                                                                                   | boolean \| undefined                                                                                                                                                                                             | -          |
| disallowSelectAll       | Whether to disallow selecting all items when \`meta+a\` is pressed                                                                                                                                                                                                                | boolean \| undefined                                                                                                                                                                                             | -          |
| onHighlightChange       | The callback fired when the highlighted item changes.                                                                                                                                                                                                                             | ((details: HighlightChangeDetails\<any>) => void) \| undefined                                                                                                                                                   | -          |
| onValueChange           | The callback fired when the selected item changes.                                                                                                                                                                                                                                | ((details: ValueChangeDetails\<any>) => void) \| undefined                                                                                                                                                       | -          |
| value                   | The controlled keys of the selected items                                                                                                                                                                                                                                         | string\[] \| undefined                                                                                                                                                                                           | -          |
| defaultValue            | The initial default value of the listbox when rendered.&#xA;Use when you don't need to control the value of the listbox.                                                                                                                                                          | string\[] \| undefined                                                                                                                                                                                           | \[]        |
| highlightedValue        | The controlled key of the highlighted item                                                                                                                                                                                                                                        | string \| null \| undefined                                                                                                                                                                                      | -          |
| defaultHighlightedValue | The initial value of the highlighted item when opened.&#xA;Use when you don't need to control the highlighted value of the listbox.                                                                                                                                               | string \| null \| undefined                                                                                                                                                                                      | -          |
| loopFocus               | Whether to loop the keyboard navigation through the options                                                                                                                                                                                                                       | boolean \| undefined                                                                                                                                                                                             | false      |
| selectionMode           | How multiple selection should behave in the listbox.&#xA;&#xA;- \`single\`: The user can select a single item.&#xA;- \`multiple\`: The user can select multiple items without using modifier keys.&#xA;- \`extended\`: The user can select multiple items by using modifier keys. | SelectionMode \| undefined                                                                                                                                                                                       | "single"   |
| scrollToIndexFn         | Function to scroll to a specific index                                                                                                                                                                                                                                            | ((details: ScrollToIndexDetails) => void) \| undefined                                                                                                                                                           | -          |
| selectOnHighlight       | Whether to select the item when it is highlighted                                                                                                                                                                                                                                 | boolean \| undefined                                                                                                                                                                                             | -          |
| deselectable            | Whether to disallow empty selection                                                                                                                                                                                                                                               | boolean \| undefined                                                                                                                                                                                             | -          |
| typeahead               | Whether to enable typeahead on the listbox                                                                                                                                                                                                                                        | boolean \| undefined                                                                                                                                                                                             | -          |
| onSelect                | Function called when an item is selected                                                                                                                                                                                                                                          | ((details: SelectionDetails) => void) \| undefined                                                                                                                                                               | -          |
| dir                     | The document's text/writing direction.                                                                                                                                                                                                                                            | "ltr" \| "rtl" \| undefined                                                                                                                                                                                      | "ltr"      |
| getRootNode             | A root node to correctly resolve document in custom environments. E.x.: Iframes, Electron.                                                                                                                                                                                        | (() => ShadowRoot \| Node \| Document) \| undefined                                                                                                                                                              | -          |
| element                 | Render the element yourself                                                                                                                                                                                                                                                       | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined                                                                                                                                                   | -          |

### Provider

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| value   | -                           | ListboxApi\<PropTypes, any>                                    | -       |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Context

| Prop     | Description | Type                                                | Default |
| -------- | ----------- | --------------------------------------------------- | ------- |
| children | -           | (listbox: ListboxApi\<PropTypes, any>) => ReactNode | -       |

### Label

| Prop    | Description                 | Type                                                             | Default |
| ------- | --------------------------- | ---------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"label">) => Element) \| undefined | -       |

### Input

| Prop    | Description                 | Type                                                             | Default |
| ------- | --------------------------- | ---------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"input">) => Element) \| undefined | -       |

### Content

| Prop    | Description                 | Type                                                          | Default |
| ------- | --------------------------- | ------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"ul">) => Element) \| undefined | -       |

### ItemGroup

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### ItemGroupLabel

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Item

| Prop             | Description                            | Type                                                          | Default |
| ---------------- | -------------------------------------- | ------------------------------------------------------------- | ------- |
| item             | The item to render                     | any                                                           | -       |
| highlightOnHover | Whether to highlight the item on hover | boolean \| undefined                                          | -       |
| element          | Render the element yourself            | ((attributes: HTMLAttributes\<"li">) => Element) \| undefined | -       |

### ItemText

| Prop    | Description                 | Type                                                            | Default |
| ------- | --------------------------- | --------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"span">) => Element) \| undefined | -       |

### ItemIndicator

| Prop    | Description                 | Type                                                            | Default |
| ------- | --------------------------- | --------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"span">) => Element) \| undefined | -       |
