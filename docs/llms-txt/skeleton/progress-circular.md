# Source: https://www.skeleton.dev/docs/svelte/framework-components/progress-circular.md

# Source: https://www.skeleton.dev/docs/react/framework-components/progress-circular.md

# Progress - Circular

Circular progress indicators for showing task progress.

```tsx
import { Progress, Slider } from '@skeletonlabs/skeleton-react';
import { useState } from 'react';

export default function Default() {
	const [value, setValue] = useState(50);

	return (
		<div className="flex flex-col gap-8 items-center">
			{/* Progress */}
			<Progress value={value} className="items-center w-fit">
				<Progress.Label>Progress</Progress.Label>
				<Progress.Circle>
					<Progress.CircleTrack />
					<Progress.CircleRange />
				</Progress.Circle>
				<Progress.ValueText />
			</Progress>

			{/* Control */}
			<Slider className="w-full" value={[value]} onValueChange={(e) => setValue(e.value[0])} step={10}>
				<Slider.Control>
					<Slider.Track>
						<Slider.Range className="bg-transparent" />
					</Slider.Track>
					<Slider.Thumb index={0}>
						<Slider.HiddenInput />
					</Slider.Thumb>
				</Slider.Control>
			</Slider>
		</div>
	);
}

```

## Size

Use different sizes for context-appropriate indicators.

```tsx
import { Progress } from '@skeletonlabs/skeleton-react';

export default function Size() {
	return (
		<div className="flex gap-4 justify-evenly items-center w-full">
			<Progress value={75} className="w-fit">
				<Progress.Circle className="[--size:--spacing(16)]">
					<Progress.CircleTrack />
					<Progress.CircleRange />
				</Progress.Circle>
			</Progress>
			<Progress value={75}>
				<Progress.Circle>
					<Progress.CircleTrack />
					<Progress.CircleRange />
				</Progress.Circle>
			</Progress>
			<Progress value={75} className="w-fit">
				<Progress.Circle className="[--size:--spacing(32)]">
					<Progress.CircleTrack />
					<Progress.CircleRange />
				</Progress.Circle>
			</Progress>
		</div>
	);
}

```

## Color

Change the track and indicator color using utility classes or custom CSS variables to match your design system.

```tsx
import { Progress } from '@skeletonlabs/skeleton-react';

export default function Color() {
	return (
		<div className="flex gap-4 justify-evenly items-center w-full">
			<Progress value={40} className="w-fit">
				<Progress.Circle>
					<Progress.CircleTrack className="stroke-primary-50-950" />
					<Progress.CircleRange className="stroke-primary-500" />
				</Progress.Circle>
			</Progress>
			<Progress value={40} className="w-fit">
				<Progress.Circle>
					<Progress.CircleTrack className="stroke-secondary-50-950" />
					<Progress.CircleRange className="stroke-secondary-500" />
				</Progress.Circle>
			</Progress>
			<Progress value={40} className="w-fit">
				<Progress.Circle>
					<Progress.CircleTrack className="stroke-tertiary-50-950" />
					<Progress.CircleRange className="stroke-tertiary-500" />
				</Progress.Circle>
			</Progress>
		</div>
	);
}

```

## Centered Content

Place content in the center of the circular progress if needed (for example, a numeric value).

```tsx
import { Progress } from '@skeletonlabs/skeleton-react';

export default function CenteredContent() {
	return (
		<Progress className="w-fit relative">
			<div className="absolute inset-0 flex items-center justify-center">
				<Progress.ValueText />
			</div>
			<Progress.Circle>
				<Progress.CircleTrack />
				<Progress.CircleRange />
			</Progress.Circle>
		</Progress>
	);
}

```

## Indeterminate

Set a `null` value to enable indeterminate mode.

```tsx
import { Progress } from '@skeletonlabs/skeleton-react';

export default function Default() {
	return (
		<Progress className="items-center w-fit" value={null}>
			<Progress.Circle>
				<Progress.CircleTrack />
				<Progress.CircleRange />
			</Progress.Circle>
			<Progress.ValueText />
		</Progress>
	);
}

```

## Format

Use the `format` prop to customize the output of the `ValueText` component. Options include:

* `percentage` (default)
* `decimal` (0.0 - 1.0)
* Custom - via the [Intl API](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl).

```tsx
import { Progress } from '@skeletonlabs/skeleton-react';

export default function Format() {
	return (
		<div className="flex gap-4 justify-evenly items-center w-full">
			<Progress className="items-center w-fit" formatOptions={{ style: 'percent' }}>
				<Progress.Circle>
					<Progress.CircleTrack />
					<Progress.CircleRange />
				</Progress.Circle>
				<Progress.ValueText />
			</Progress>
			<Progress className="items-center w-fit" formatOptions={{ style: 'decimal' }}>
				<Progress.Circle>
					<Progress.CircleTrack />
					<Progress.CircleRange />
				</Progress.Circle>
				<Progress.ValueText />
			</Progress>
			<Progress className="items-center w-fit" formatOptions={{ style: 'currency', currency: 'EUR' }}>
				<Progress.Circle>
					<Progress.CircleTrack />
					<Progress.CircleRange />
				</Progress.Circle>
				<Progress.ValueText />
			</Progress>
		</div>
	);
}

```

## Custom Value Text

Provide a custom renderer for the `ValueText` if you need to show a different layout or label.

```tsx
import { Progress } from '@skeletonlabs/skeleton-react';

export default function CustomValueText() {
	return (
		<Progress className="items-center w-fit">
			<Progress.Circle>
				<Progress.CircleTrack />
				<Progress.CircleRange />
			</Progress.Circle>
			<Progress.ValueText>
				<Progress.Context>{(progress) => `${progress.value} of ${progress.max}`}</Progress.Context>
			</Progress.ValueText>
		</Progress>
	);
}

```

## Anatomy

Here's an overview of how the Progress (Circular) component is structured in code:

```tsx
import { Progress } from '@skeletonlabs/skeleton-react';

export default function Anatomy() {
	return (
		<Progress>
			<Progress.Label />
			<Progress.Circle>
				<Progress.CircleTrack />
				<Progress.CircleRange />
			</Progress.Circle>
			<Progress.ValueText />
		</Progress>
	);
}
```

## API Reference

### Root

| Prop          | Description                                                                                                                | Type                                                                                    | Default               |
| ------------- | -------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------- |
| ids           | The ids of the elements in the progress bar. Useful for composition.                                                       | Partial\<\{ root: string; track: string; label: string; circle: string; }> \| undefined | -                     |
| value         | The controlled value of the progress bar.                                                                                  | number \| null \| undefined                                                             | -                     |
| defaultValue  | The initial value of the progress bar when rendered.&#xA;Use when you don't need to control the value of the progress bar. | number \| null \| undefined                                                             | 50                    |
| min           | The minimum allowed value of the progress bar.                                                                             | number \| undefined                                                                     | 0                     |
| max           | The maximum allowed value of the progress bar.                                                                             | number \| undefined                                                                     | 100                   |
| translations  | The localized messages to use.                                                                                             | IntlTranslations \| undefined                                                           | -                     |
| onValueChange | Callback fired when the value changes.                                                                                     | ((details: ValueChangeDetails) => void) \| undefined                                    | -                     |
| formatOptions | The options to use for formatting the value.                                                                               | NumberFormatOptions \| undefined                                                        | \{ style: "percent" } |
| locale        | The locale to use for formatting the value.                                                                                | string \| undefined                                                                     | "en-US"               |
| dir           | The document's text/writing direction.                                                                                     | "ltr" \| "rtl" \| undefined                                                             | "ltr"                 |
| getRootNode   | A root node to correctly resolve document in custom environments. E.x.: Iframes, Electron.                                 | (() => ShadowRoot \| Node \| Document) \| undefined                                     | -                     |
| orientation   | The orientation of the element.                                                                                            | "horizontal" \| "vertical" \| undefined                                                 | "horizontal"          |
| element       | Render the element yourself                                                                                                | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined                          | -                     |

### Provider

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| value   | -                           | ProgressApi\<PropTypes>                                        | -       |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Context

| Prop     | Description | Type                                             | Default |
| -------- | ----------- | ------------------------------------------------ | ------- |
| children | -           | (progress: ProgressApi\<PropTypes>) => ReactNode | -       |

### Label

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### ValueText

| Prop    | Description                 | Type                                                            | Default |
| ------- | --------------------------- | --------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"span">) => Element) \| undefined | -       |

### Track

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Range

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Circle

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"svg">) => Element) \| undefined | -       |

### CircleTrack

| Prop    | Description                 | Type                                                              | Default |
| ------- | --------------------------- | ----------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"circle">) => Element) \| undefined | -       |

### CircleRange

| Prop    | Description                 | Type                                                              | Default |
| ------- | --------------------------- | ----------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"circle">) => Element) \| undefined | -       |
