# Source: https://www.skeleton.dev/docs/svelte/framework-components/rating-group.md

# Source: https://www.skeleton.dev/docs/react/framework-components/rating-group.md

# Rating Group

Rating Group allows users to rate something

```tsx
import { RatingGroup } from '@skeletonlabs/skeleton-react';

export default function Default() {
	return (
		<RatingGroup count={5} defaultValue={3}>
			<RatingGroup.Control>
				<RatingGroup.Context>
					{(ratingGroup) => ratingGroup.items.map((index) => <RatingGroup.Item key={index} index={index} />)}
				</RatingGroup.Context>
			</RatingGroup.Control>
			<RatingGroup.HiddenInput />
		</RatingGroup>
	);
}

```

## Half Step

Set the `allowHalf` prop to enable half steps.

```tsx
import { RatingGroup } from '@skeletonlabs/skeleton-react';

export default function Half() {
	return (
		<RatingGroup count={5} allowHalf>
			<RatingGroup.Control>
				<RatingGroup.Context>
					{(ratingGroup) => ratingGroup.items.map((index) => <RatingGroup.Item key={index} index={index} />)}
				</RatingGroup.Context>
			</RatingGroup.Control>
			<RatingGroup.HiddenInput />
		</RatingGroup>
	);
}

```

## Custom Icons

Insert your own custom images or icons for the `empty` and `full` states.

```tsx
import { RatingGroup } from '@skeletonlabs/skeleton-react';
import { BoneIcon, SkullIcon } from 'lucide-react';

export default function CustomIcons() {
	return (
		<RatingGroup count={3}>
			<RatingGroup.Control>
				<RatingGroup.Context>
					{(ratingGroup) =>
						ratingGroup.items.map((index) => <RatingGroup.Item key={index} index={index} empty={<BoneIcon />} full={<SkullIcon />} />)
					}
				</RatingGroup.Context>
			</RatingGroup.Control>
			<RatingGroup.HiddenInput />
		</RatingGroup>
	);
}

```

## Label

Use the `Label` component to describe the intended usage.

```tsx
import { RatingGroup } from '@skeletonlabs/skeleton-react';

export default function Label() {
	return (
		<RatingGroup count={5}>
			<RatingGroup.Label>Rate us:</RatingGroup.Label>
			<RatingGroup.Control>
				<RatingGroup.Context>
					{(ratingGroup) => ratingGroup.items.map((index) => <RatingGroup.Item key={index} index={index} />)}
				</RatingGroup.Context>
			</RatingGroup.Control>
			<RatingGroup.HiddenInput />
		</RatingGroup>
	);
}

```

## Disabled

Set the `disabled` prop to enable the disabled state.

```tsx
import { RatingGroup } from '@skeletonlabs/skeleton-react';

export default function Page() {
	return (
		<RatingGroup count={5} disabled>
			<RatingGroup.Control>
				<RatingGroup.Context>
					{(ratingGroup) => ratingGroup.items.map((index) => <RatingGroup.Item key={index} index={index} />)}
				</RatingGroup.Context>
			</RatingGroup.Control>
			<RatingGroup.HiddenInput />
		</RatingGroup>
	);
}

```

## Direction

Set the text direction (`ltr` or `rtl`) using the `dir` prop.

```tsx
import { RatingGroup } from '@skeletonlabs/skeleton-react';

export default function Dir() {
	return (
		<RatingGroup count={5} dir="rtl">
			<RatingGroup.Label>Label</RatingGroup.Label>
			<RatingGroup.Control>
				<RatingGroup.Context>
					{(ratingGroup) => ratingGroup.items.map((index) => <RatingGroup.Item key={index} index={index} />)}
				</RatingGroup.Context>
			</RatingGroup.Control>
			<RatingGroup.HiddenInput />
		</RatingGroup>
	);
}

```

## Anatomy

Here's an overview of how the RatingGroup component is structured in code:

```tsx
import { RatingGroup } from '@skeletonlabs/skeleton-react';

export default function Anatomy() {
	return (
		<RatingGroup>
			<RatingGroup.Label />
			<RatingGroup.Control>
				<RatingGroup.Item />
			</RatingGroup.Control>
			<RatingGroup.HiddenInput />
		</RatingGroup>
	);
}
```

## API Reference

### Root

| Prop          | Description                                                                                                    | Type                                                                                                                         | Default |
| ------------- | -------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------- |
| ids           | The ids of the elements in the rating. Useful for composition.                                                 | Partial\<\{ root: string; label: string; hiddenInput: string; control: string; item: (id: string) => string; }> \| undefined | -       |
| translations  | Specifies the localized strings that identifies the accessibility elements and their states                    | IntlTranslations \| undefined                                                                                                | -       |
| count         | The total number of ratings.                                                                                   | number \| undefined                                                                                                          | 5       |
| name          | The name attribute of the rating element (used in forms).                                                      | string \| undefined                                                                                                          | -       |
| form          | The associate form of the underlying input element.                                                            | string \| undefined                                                                                                          | -       |
| value         | The controlled value of the rating                                                                             | number \| undefined                                                                                                          | -       |
| defaultValue  | The initial value of the rating when rendered.&#xA;Use when you don't need to control the value of the rating. | number \| undefined                                                                                                          | -       |
| readOnly      | Whether the rating is readonly.                                                                                | boolean \| undefined                                                                                                         | -       |
| disabled      | Whether the rating is disabled.                                                                                | boolean \| undefined                                                                                                         | -       |
| required      | Whether the rating is required.                                                                                | boolean \| undefined                                                                                                         | -       |
| allowHalf     | Whether to allow half stars.                                                                                   | boolean \| undefined                                                                                                         | -       |
| autoFocus     | Whether to autofocus the rating.                                                                               | boolean \| undefined                                                                                                         | -       |
| onValueChange | Function to be called when the rating value changes.                                                           | ((details: ValueChangeDetails) => void) \| undefined                                                                         | -       |
| onHoverChange | Function to be called when the rating value is hovered.                                                        | ((details: HoverChangeDetails) => void) \| undefined                                                                         | -       |
| dir           | The document's text/writing direction.                                                                         | "ltr" \| "rtl" \| undefined                                                                                                  | "ltr"   |
| getRootNode   | A root node to correctly resolve document in custom environments. E.x.: Iframes, Electron.                     | (() => ShadowRoot \| Node \| Document) \| undefined                                                                          | -       |
| element       | Render the element yourself                                                                                    | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined                                                               | -       |

### Provider

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| value   | -                           | RatingGroupApi\<PropTypes>                                     | -       |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Context

| Prop     | Description | Type                                                   | Default |
| -------- | ----------- | ------------------------------------------------------ | ------- |
| children | -           | (ratingGroup: RatingGroupApi\<PropTypes>) => ReactNode | -       |

### Label

| Prop    | Description                 | Type                                                             | Default |
| ------- | --------------------------- | ---------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"label">) => Element) \| undefined | -       |

### Control

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Item

| Prop    | Description                                                | Type                                                            | Default         |
| ------- | ---------------------------------------------------------- | --------------------------------------------------------------- | --------------- |
| empty   | The content to render when the item is in the empty state. | ReactNode                                                       | StarEmpty (SVG) |
| half    | The content to render when the item is in the half state.  | ReactNode                                                       | StarHalf (SVG)  |
| full    | The content to render when the item is in the full state.  | ReactNode                                                       | StarFull (SVG)  |
| index   | -                                                          | number                                                          | -               |
| element | Render the element yourself                                | ((attributes: HTMLAttributes\<"span">) => Element) \| undefined | -               |

### HiddenInput

| Prop    | Description                 | Type                                                             | Default |
| ------- | --------------------------- | ---------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"input">) => Element) \| undefined | -       |
