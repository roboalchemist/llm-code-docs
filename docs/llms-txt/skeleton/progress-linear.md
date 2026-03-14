# Source: https://www.skeleton.dev/docs/svelte/framework-components/progress-linear.md

# Source: https://www.skeleton.dev/docs/react/framework-components/progress-linear.md

# Progress - Linear

An indicator showing the progress or completion of a task.

```tsx
import { Progress, Slider } from '@skeletonlabs/skeleton-react';
import { useState } from 'react';

export default function Default() {
	const [value, setValue] = useState(50);

	return (
		<div className="w-full space-y-8">
			{/* Progress */}
			<Progress value={value} className="grid grid-cols-[auto_1fr] items-center gap-4">
				<Progress.Label className="text-sm">{value}%</Progress.Label>
				<Progress.Track>
					<Progress.Range />
				</Progress.Track>
			</Progress>

			{/* Control */}
			<Slider className="w-32 mx-auto" value={[value]} onValueChange={(e) => setValue(e.value[0])} step={10}>
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

## Color

Change the track and range color using utility classes or custom CSS variables to match your design system.

```tsx
import { Progress } from '@skeletonlabs/skeleton-react';

export default function Color() {
	return (
		<div className="flex w-full flex-col gap-8">
			<Progress>
				<Progress.Track className="bg-primary-50-950">
					<Progress.Range className="bg-primary-500" />
				</Progress.Track>
			</Progress>
			<Progress>
				<Progress.Track className="bg-secondary-50-950">
					<Progress.Range className="bg-secondary-500" />
				</Progress.Track>
			</Progress>
			<Progress>
				<Progress.Track className="bg-tertiary-50-950">
					<Progress.Range className="bg-tertiary-500" />
				</Progress.Track>
			</Progress>
		</div>
	);
}

```

## Height

Create variations using different heights.

```tsx
import { Progress } from '@skeletonlabs/skeleton-react';

export default function Height() {
	return (
		<div className="flex w-full flex-col gap-8">
			<Progress>
				<Progress.Track className="h-1">
					<Progress.Range />
				</Progress.Track>
			</Progress>
			<Progress>
				<Progress.Track className="h-4">
					<Progress.Range />
				</Progress.Track>
			</Progress>
			<Progress>
				<Progress.Track className="h-6">
					<Progress.Range />
				</Progress.Track>
			</Progress>
		</div>
	);
}

```

## Orientation

Using the `orientation` prop to control the layout.

```tsx
import { Progress } from '@skeletonlabs/skeleton-react';

export default function Orientation() {
	return (
		<Progress orientation="vertical">
			<Progress.Track>
				<Progress.Range />
			</Progress.Track>
		</Progress>
	);
}

```

## Indeterminate

Set a `null` value to enable indeterminate mode.

```tsx
import { Progress } from '@skeletonlabs/skeleton-react';

export default function Indeterminate() {
	return (
		<Progress value={null}>
			<Progress.Track>
				<Progress.Range />
			</Progress.Track>
		</Progress>
	);
}

```

Use CSS to enable custom animations.

```tsx
import { Progress } from '@skeletonlabs/skeleton-react';

export default function CustomAnimation() {
	return (
		<>
			<Progress value={null}>
				<Progress.Track>
					<Progress.Range className="animate-[custom-animation_2s_ease-in-out_infinite]" />
				</Progress.Track>
			</Progress>
			<style>{`
                @keyframes custom-animation {
                    from {
                        scale: 0.5 1;
                        transform: translateX(-200%);
                    }
                    25% {
                        transform: translateX(50%);
                    }
                    50% {
                        transform: translateX(-50%);
                    }
                    75% {
                        transform: translateX(150%);
                    }
                    to {
                        scale: 0.5 1;
                        transform: translateX(200%);
                    }
                }
            `}</style>
		</>
	);
}

```

## Direction

Set the text direction (`ltr` or `rtl`) using the `dir` prop.

```tsx
import { Progress } from '@skeletonlabs/skeleton-react';

export default function Dir() {
	return (
		<Progress dir="rtl">
			<Progress.Label>Label</Progress.Label>
			<Progress.Track>
				<Progress.Range />
			</Progress.Track>
		</Progress>
	);
}

```

## Native Alternative

Skeleton also provides styles for the native [Progress](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress) element.

```tsx
export default function Native() {
	return <progress className="progress" value="50" max="100" />;
}

```

## Anatomy

Here's an overview of how the Progress (Linear) component is structured in code:

```tsx
import { Progress } from '@skeletonlabs/skeleton-react';

export default function Anatomy() {
	return (
		<Progress>
			<Progress.Label />
			<Progress.Track>
				<Progress.Range />
			</Progress.Track>
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
