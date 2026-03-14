# Source: https://www.skeleton.dev/docs/svelte/framework-components/steps.md

# Source: https://www.skeleton.dev/docs/react/framework-components/steps.md

# Steps

Use steps to guide users through a multi-step process.

```tsx
import { Steps } from '@skeletonlabs/skeleton-react';

const steps = [
	{ title: 'First', content: 'First do this.' },
	{ title: 'Then', content: 'Then do that.' },
	{ title: 'Finally', content: 'Almost done...' },
];

export default function Default() {
	return (
		<Steps count={steps.length} className="w-full">
			<Steps.List>
				{steps.map((item, index) => (
					<Steps.Item key={index} index={index}>
						<Steps.Trigger>
							<Steps.Indicator>{index + 1}</Steps.Indicator> {item.title}
						</Steps.Trigger>
						{index < steps.length - 1 && <Steps.Separator />}
					</Steps.Item>
				))}
			</Steps.List>
			{steps.map((item, index) => (
				<Steps.Content key={index} index={index}>
					{item.content}
				</Steps.Content>
			))}
			<Steps.Content index={steps.length}>All done!</Steps.Content>
			<div className="flex justify-between items-center gap-2">
				<Steps.PrevTrigger className="btn preset-filled">Back</Steps.PrevTrigger>
				<Steps.NextTrigger className="btn preset-filled">Next</Steps.NextTrigger>
			</div>
		</Steps>
	);
}

```

## Controlled

Use the `step` and `onStepChange` props to control state programmatically.

```tsx
import { Steps } from '@skeletonlabs/skeleton-react';
import { useState } from 'react';

const steps = [
	{ title: 'First', content: 'First do this.' },
	{ title: 'Then', content: 'Then do that.' },
	{ title: 'Finally', content: 'Almost done...' },
];

export default function Default() {
	const [step, setStep] = useState(0);
	return (
		<Steps step={step} onStepChange={(details) => setStep(details.step)} count={steps.length} className="w-full">
			<Steps.List>
				{steps.map((item, index) => (
					<Steps.Item key={index} index={index}>
						<Steps.Trigger>
							<Steps.Indicator>{index + 1}</Steps.Indicator> {item.title}
						</Steps.Trigger>
						{index < steps.length - 1 && <Steps.Separator />}
					</Steps.Item>
				))}
			</Steps.List>
			{steps.map((item, index) => (
				<Steps.Content key={index} index={index}>
					{item.content}
				</Steps.Content>
			))}
			<Steps.Content index={steps.length}>All done!</Steps.Content>
			<div className="flex justify-between items-center gap-2">
				<Steps.PrevTrigger className="btn preset-filled">Back</Steps.PrevTrigger>
				<Steps.NextTrigger className="btn preset-filled">Next</Steps.NextTrigger>
			</div>
		</Steps>
	);
}

```

## Orientation

Using the `orientation` prop to control the layout.

```tsx
import { Steps } from '@skeletonlabs/skeleton-react';

const steps = [
	{ title: 'First', content: 'First do this.' },
	{ title: 'Then', content: 'Then do that.' },
	{ title: 'Finally', content: 'Almost done...' },
];

export default function Default() {
	return (
		<Steps orientation="vertical" count={steps.length} className="w-full h-48">
			<Steps.List>
				{steps.map((item, index) => (
					<Steps.Item key={index} index={index}>
						<Steps.Trigger>
							<Steps.Indicator>{index + 1}</Steps.Indicator> {item.title}
						</Steps.Trigger>
						{index < steps.length - 1 && <Steps.Separator />}
					</Steps.Item>
				))}
			</Steps.List>
			<div className="flex flex-col grow">
				{steps.map((item, index) => (
					<Steps.Content key={index} index={index} className="grow">
						{item.content}
					</Steps.Content>
				))}
				<Steps.Content index={steps.length} className="grow">
					All done!
				</Steps.Content>
				<div className="flex justify-between items-center gap-2">
					<Steps.PrevTrigger className="btn preset-filled">Back</Steps.PrevTrigger>
					<Steps.NextTrigger className="btn preset-filled">Next</Steps.NextTrigger>
				</div>
			</div>
		</Steps>
	);
}

```

## Direction

Set the text direction (`ltr` or `rtl`) using the `dir` prop.

```tsx
import { Steps } from '@skeletonlabs/skeleton-react';

const steps = [
	{ title: 'First', content: 'First do this.' },
	{ title: 'Then', content: 'Then do that.' },
	{ title: 'Finally', content: 'Almost done...' },
];

export default function Default() {
	return (
		<Steps dir="rtl" count={steps.length} className="w-full">
			<Steps.List>
				{steps.map((item, index) => (
					<Steps.Item key={index} index={index}>
						<Steps.Trigger>
							<Steps.Indicator>{index + 1}</Steps.Indicator> {item.title}
						</Steps.Trigger>
						{index < steps.length - 1 && <Steps.Separator />}
					</Steps.Item>
				))}
			</Steps.List>
			{steps.map((item, index) => (
				<Steps.Content key={index} index={index}>
					{item.content}
				</Steps.Content>
			))}
			<Steps.Content index={steps.length}>All done!</Steps.Content>
			<div className="flex justify-between items-center gap-2">
				<Steps.PrevTrigger className="btn preset-filled">Back</Steps.PrevTrigger>
				<Steps.NextTrigger className="btn preset-filled">Next</Steps.NextTrigger>
			</div>
		</Steps>
	);
}

```

## Anatomy

Here's an overview of how the Steps component is structured in code:

```tsx
import { Steps } from '@skeletonlabs/skeleton-react';

export default function Anatomy() {
	return (
		<Steps>
			<Steps.List>
				<Steps.Item>
					<Steps.Trigger>
						<Steps.Indicator />
					</Steps.Trigger>
					<Steps.Separator />
				</Steps.Item>
			</Steps.List>
			<Steps.Content />
			<Steps.PrevTrigger />
			<Steps.NextTrigger />
		</Steps>
	);
}
```

## API Reference

### Root

| Prop            | Description                                                                                                      | Type                                                           | Default      |
| --------------- | ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | ------------ |
| ids             | The custom ids for the stepper elements                                                                          | ElementIds \| undefined                                        | -            |
| step            | The controlled value of the stepper                                                                              | number \| undefined                                            | -            |
| defaultStep     | The initial value of the stepper when rendered.&#xA;Use when you don't need to control the value of the stepper. | number \| undefined                                            | -            |
| onStepChange    | Callback to be called when the value changes                                                                     | ((details: StepChangeDetails) => void) \| undefined            | -            |
| onStepComplete  | Callback to be called when a step is completed                                                                   | VoidFunction \| undefined                                      | -            |
| linear          | If \`true\`, the stepper requires the user to complete the steps in order                                        | boolean \| undefined                                           | -            |
| orientation     | The orientation of the stepper                                                                                   | "horizontal" \| "vertical" \| undefined                        | "horizontal" |
| count           | The total number of steps                                                                                        | number \| undefined                                            | -            |
| isStepValid     | Whether a step is valid. Invalid steps block forward navigation in linear mode.                                  | ((index: number) => boolean) \| undefined                      | () => true   |
| isStepSkippable | Whether a step can be skipped during navigation.&#xA;Skippable steps are bypassed when using next/prev.          | ((index: number) => boolean) \| undefined                      | () => false  |
| onStepInvalid   | Called when navigation is blocked due to an invalid step.                                                        | ((details: StepInvalidDetails) => void) \| undefined           | -            |
| dir             | The document's text/writing direction.                                                                           | "ltr" \| "rtl" \| undefined                                    | "ltr"        |
| getRootNode     | A root node to correctly resolve document in custom environments. E.x.: Iframes, Electron.                       | (() => ShadowRoot \| Node \| Document) \| undefined            | -            |
| element         | Render the element yourself                                                                                      | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -            |

### Provider

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| value   | -                           | StepsApi\<PropTypes>                                           | -       |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Context

| Prop     | Description | Type                                       | Default |
| -------- | ----------- | ------------------------------------------ | ------- |
| children | -           | (steps: StepsApi\<PropTypes>) => ReactNode | -       |

### List

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Item

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| index   | -                           | number                                                         | -       |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Trigger

| Prop    | Description                 | Type                                                              | Default |
| ------- | --------------------------- | ----------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"button">) => Element) \| undefined | -       |

### Indicator

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Separator

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Content

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| index   | -                           | number                                                         | -       |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### PrevTrigger

| Prop    | Description                 | Type                                                              | Default |
| ------- | --------------------------- | ----------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"button">) => Element) \| undefined | -       |

### NextTrigger

| Prop    | Description                 | Type                                                              | Default |
| ------- | --------------------------- | ----------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"button">) => Element) \| undefined | -       |
