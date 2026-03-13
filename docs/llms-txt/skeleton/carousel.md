# Source: https://www.skeleton.dev/docs/svelte/framework-components/carousel.md

# Source: https://www.skeleton.dev/docs/react/framework-components/carousel.md

# Carousel

Navigate through a collection of slides with controls and indicators.

```tsx
import { Carousel } from '@skeletonlabs/skeleton-react';

const slides = [
	{ title: 'Slide 1' },
	{ title: 'Slide 2' },
	{ title: 'Slide 3' },
	{ title: 'Slide 4' },
	{ title: 'Slide 5' },
	{ title: 'Slide 6' },
	{ title: 'Slide 7' },
	{ title: 'Slide 8' },
	{ title: 'Slide 9' },
	{ title: 'Slide 10' },
];

export default function Default() {
	return (
		<Carousel slideCount={slides.length} slidesPerPage={3} spacing="16px" loop>
			<Carousel.Control className="flex justify-between mb-4">
				<Carousel.PrevTrigger className="btn preset-filled">
					<span>&larr;</span>
					<span>Back</span>
				</Carousel.PrevTrigger>
				<Carousel.AutoplayTrigger className="btn preset-tonal">Toggle Autoplay</Carousel.AutoplayTrigger>
				<Carousel.NextTrigger className="btn preset-filled">
					<span>Next</span>
					<span>&rarr;</span>
				</Carousel.NextTrigger>
			</Carousel.Control>
			<Carousel.ItemGroup>
				{slides.map((slide, i) => (
					<Carousel.Item index={i} key={i} className="card bg-surface-100-900 h-50 p-4 flex justify-center items-center">
						{slide.title}
					</Carousel.Item>
				))}
			</Carousel.ItemGroup>
			<Carousel.IndicatorGroup>
				<Carousel.Context>{(carousel) => carousel.pageSnapPoints.map((_, i) => <Carousel.Indicator key={i} index={i} />)}</Carousel.Context>
			</Carousel.IndicatorGroup>
		</Carousel>
	);
}

```

Breaking convention in Skeleton, some portions of this component are provided “headless”. Meaning no default styles are applied out of the box. This ensures you retain full control of styling for maximum flexibility.

## Overlapping Controls

Introduce supporting elements and styles to implement this variation.

```tsx
import { Carousel } from '@skeletonlabs/skeleton-react';

const slides = [
	{ title: 'Slide 1' },
	{ title: 'Slide 2' },
	{ title: 'Slide 3' },
	{ title: 'Slide 4' },
	{ title: 'Slide 5' },
	{ title: 'Slide 6' },
	{ title: 'Slide 7' },
	{ title: 'Slide 8' },
	{ title: 'Slide 9' },
	{ title: 'Slide 10' },
];

export default function Overlap() {
	return (
		<Carousel slideCount={slides.length} slidesPerPage={4} spacing="16px" padding="48px" autoSize loop>
			<div className="relative">
				<Carousel.Control>
					<Carousel.PrevTrigger className="btn-icon preset-filled rounded-full absolute top-[50%] left-0 translate-y-[-50%]">
						<span>&larr;</span>
					</Carousel.PrevTrigger>
					<Carousel.NextTrigger className="btn-icon preset-filled rounded-full absolute top-[50%] right-0 translate-y-[-50%]">
						<span>&rarr;</span>
					</Carousel.NextTrigger>
				</Carousel.Control>
				<Carousel.ItemGroup>
					{slides.map((slide, i) => (
						<Carousel.Item index={i} key={i} className="card bg-surface-100-900 h-50 aspect-square p-4 flex justify-center items-center">
							{slide.title}
						</Carousel.Item>
					))}
				</Carousel.ItemGroup>
			</div>
			<Carousel.IndicatorGroup>
				<Carousel.Context>{(carousel) => carousel.pageSnapPoints.map((_, i) => <Carousel.Indicator key={i} index={i} />)}</Carousel.Context>
			</Carousel.IndicatorGroup>
		</Carousel>
	);
}

```

## Orientation

Apply `orientation="vertical"` on the root, and apply a set height on the `<Carousel.ItemGroup>`.

```tsx
import { Carousel } from '@skeletonlabs/skeleton-react';

const slides = [
	{ title: 'Slide 1' },
	{ title: 'Slide 2' },
	{ title: 'Slide 3' },
	{ title: 'Slide 4' },
	{ title: 'Slide 5' },
	{ title: 'Slide 6' },
	{ title: 'Slide 7' },
	{ title: 'Slide 8' },
	{ title: 'Slide 9' },
	{ title: 'Slide 10' },
];

export default function Orientation() {
	return (
		<Carousel slideCount={slides.length} slidesPerPage={3} spacing="16px" loop orientation="vertical" autoSize>
			<Carousel.Control className="flex justify-between mb-4">
				<Carousel.PrevTrigger className="btn preset-filled">
					<span>&larr;</span>
					<span>Back</span>
				</Carousel.PrevTrigger>
				<Carousel.AutoplayTrigger className="btn preset-tonal">Toggle Autoplay</Carousel.AutoplayTrigger>
				<Carousel.NextTrigger className="btn preset-filled">
					<span>Next</span>
					<span>&rarr;</span>
				</Carousel.NextTrigger>
			</Carousel.Control>
			<Carousel.ItemGroup className="h-80">
				{slides.map((slide, i) => (
					<Carousel.Item index={i} key={i} className="card bg-surface-100-900 h-32 p-4 flex justify-center items-center">
						{slide.title}
					</Carousel.Item>
				))}
			</Carousel.ItemGroup>
			<Carousel.IndicatorGroup>
				<Carousel.Context>{(carousel) => carousel.pageSnapPoints.map((_, i) => <Carousel.Indicator key={i} index={i} />)}</Carousel.Context>
			</Carousel.IndicatorGroup>
		</Carousel>
	);
}

```

## Text

Display a text display of the carousel state.

```tsx
import { Carousel } from '@skeletonlabs/skeleton-react';

const slides = [
	{ title: 'Slide 1' },
	{ title: 'Slide 2' },
	{ title: 'Slide 3' },
	{ title: 'Slide 4' },
	{ title: 'Slide 5' },
	{ title: 'Slide 6' },
	{ title: 'Slide 7' },
	{ title: 'Slide 8' },
	{ title: 'Slide 9' },
	{ title: 'Slide 10' },
];

export default function Text() {
	return (
		<Carousel slideCount={slides.length} slidesPerPage={3} spacing="16px" loop>
			<Carousel.Control className="flex justify-between mb-4">
				<Carousel.PrevTrigger className="btn preset-filled">
					<span>&larr;</span>
					<span>Back</span>
				</Carousel.PrevTrigger>
				<Carousel.AutoplayTrigger className="btn preset-filled">Toggle Autoplay</Carousel.AutoplayTrigger>
				<Carousel.NextTrigger className="btn preset-filled">
					<span>Next</span>
					<span>&rarr;</span>
				</Carousel.NextTrigger>
			</Carousel.Control>
			<Carousel.ItemGroup>
				{slides.map((slide, i) => (
					<Carousel.Item index={i} key={i} className="card bg-surface-100-900 h-50 p-4 flex justify-center items-center">
						{slide.title}
					</Carousel.Item>
				))}
			</Carousel.ItemGroup>
			<Carousel.IndicatorGroup>
				<Carousel.Context>
					{(carousel) => (
						<p>
							Showing {carousel.page + 1} of {carousel.pageSnapPoints.length}
						</p>
					)}
				</Carousel.Context>
			</Carousel.IndicatorGroup>
		</Carousel>
	);
}

```

## Anatomy

Here's an overview of how the Carousel component is structured in code:

```tsx
import { Carousel } from '@skeletonlabs/skeleton-react';

export default function Anatomy() {
	return (
		<Carousel>
			<Carousel.Control>
				<Carousel.PrevTrigger />
				<Carousel.AutoplayTrigger />
				<Carousel.NextTrigger />
			</Carousel.Control>
			<Carousel.ItemGroup>
				<Carousel.Item />
			</Carousel.ItemGroup>
			<Carousel.IndicatorGroup>
				<Carousel.Indicator />
			</Carousel.IndicatorGroup>
			<Carousel.ProgressText />
		</Carousel>
	);
}
```

## API Reference

### Root

| Prop                   | Description                                                                                                                                                  | Type                                                                                                                                                                                                  | Default      |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| ids                    | The ids of the elements in the carousel. Useful for composition.                                                                                             | Partial\<\{ root: string; item: (index: number) => string; itemGroup: string; nextTrigger: string; prevTrigger: string; indicatorGroup: string; indicator: (index: number) => string; }> \| undefined | -            |
| translations           | The localized messages to use.                                                                                                                               | IntlTranslations \| undefined                                                                                                                                                                         | -            |
| slidesPerPage          | The number of slides to show at a time.                                                                                                                      | number \| undefined                                                                                                                                                                                   | 1            |
| autoSize               | Whether to enable variable width slides.                                                                                                                     | boolean \| undefined                                                                                                                                                                                  | false        |
| slidesPerMove          | The number of slides to scroll at a time.&#xA;&#xA;When set to \`auto\`, the number of slides to scroll is determined by the&#xA;\`slidesPerPage\` property. | number \| "auto" \| undefined                                                                                                                                                                         | "auto"       |
| autoplay               | Whether to scroll automatically. The default delay is 4000ms.                                                                                                | boolean \| \{ delay: number; } \| undefined                                                                                                                                                           | false        |
| allowMouseDrag         | Whether to allow scrolling via dragging with mouse                                                                                                           | boolean \| undefined                                                                                                                                                                                  | false        |
| loop                   | Whether the carousel should loop around.                                                                                                                     | boolean \| undefined                                                                                                                                                                                  | false        |
| page                   | The controlled page of the carousel.                                                                                                                         | number \| undefined                                                                                                                                                                                   | -            |
| defaultPage            | The initial page to scroll to when rendered.&#xA;Use when you don't need to control the page of the carousel.                                                | number \| undefined                                                                                                                                                                                   | 0            |
| spacing                | The amount of space between items.                                                                                                                           | string \| undefined                                                                                                                                                                                   | "0px"        |
| padding                | Defines the extra space added around the scrollable area,&#xA;enabling nearby items to remain partially in view.                                             | string \| undefined                                                                                                                                                                                   | -            |
| onPageChange           | Function called when the page changes.                                                                                                                       | ((details: PageChangeDetails) => void) \| undefined                                                                                                                                                   | -            |
| inViewThreshold        | The threshold for determining if an item is in view.                                                                                                         | number \| number\[] \| undefined                                                                                                                                                                      | 0.6          |
| snapType               | The snap type of the item.                                                                                                                                   | "proximity" \| "mandatory" \| undefined                                                                                                                                                               | "mandatory"  |
| slideCount             | The total number of slides.&#xA;Useful for SSR to render the initial ating the snap points.                                                                  | number                                                                                                                                                                                                | -            |
| onDragStatusChange     | Function called when the drag status changes.                                                                                                                | ((details: DragStatusDetails) => void) \| undefined                                                                                                                                                   | -            |
| onAutoplayStatusChange | Function called when the autoplay status changes.                                                                                                            | ((details: AutoplayStatusDetails) => void) \| undefined                                                                                                                                               | -            |
| dir                    | The document's text/writing direction.                                                                                                                       | "ltr" \| "rtl" \| undefined                                                                                                                                                                           | "ltr"        |
| getRootNode            | A root node to correctly resolve document in custom environments. E.x.: Iframes, Electron.                                                                   | (() => ShadowRoot \| Node \| Document) \| undefined                                                                                                                                                   | -            |
| orientation            | The orientation of the element.                                                                                                                              | "horizontal" \| "vertical" \| undefined                                                                                                                                                               | "horizontal" |
| element                | Render the element yourself                                                                                                                                  | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined                                                                                                                                        | -            |

### Provider

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| value   | -                           | CarouselApi\<PropTypes>                                        | -       |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Context

| Prop     | Description | Type                                             | Default |
| -------- | ----------- | ------------------------------------------------ | ------- |
| children | -           | (carousel: CarouselApi\<PropTypes>) => ReactNode | -       |

### Control

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### ItemGroup

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Item

| Prop      | Description                     | Type                                                           | Default |
| --------- | ------------------------------- | -------------------------------------------------------------- | ------- |
| index     | The index of the item.          | number                                                         | -       |
| snapAlign | The snap alignment of the item. | "start" \| "end" \| "center" \| undefined                      | "start" |
| element   | Render the element yourself     | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### PrevTrigger

| Prop    | Description                 | Type                                                              | Default |
| ------- | --------------------------- | ----------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"button">) => Element) \| undefined | -       |

### NextTrigger

| Prop    | Description                 | Type                                                              | Default |
| ------- | --------------------------- | ----------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"button">) => Element) \| undefined | -       |

### AutoplayTrigger

| Prop    | Description                 | Type                                                              | Default |
| ------- | --------------------------- | ----------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"button">) => Element) \| undefined | -       |

### IndicatorGroup

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Indicator

| Prop     | Description                         | Type                                                              | Default |
| -------- | ----------------------------------- | ----------------------------------------------------------------- | ------- |
| index    | The index of the indicator.         | number                                                            | -       |
| readOnly | Whether the indicator is read only. | boolean \| undefined                                              | false   |
| element  | Render the element yourself         | ((attributes: HTMLAttributes\<"button">) => Element) \| undefined | -       |

### ProgressText

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |
