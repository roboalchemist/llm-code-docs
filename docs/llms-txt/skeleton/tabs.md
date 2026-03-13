# Source: https://www.skeleton.dev/docs/svelte/framework-components/tabs.md

# Source: https://www.skeleton.dev/docs/react/framework-components/tabs.md

# Tabs

Use tabs to quickly switch between different views and pages.

```tsx
import { Tabs } from '@skeletonlabs/skeleton-react';

export default function Default() {
	return (
		<Tabs defaultValue="overview">
			<Tabs.List>
				<Tabs.Trigger value="overview">Overview</Tabs.Trigger>
				<Tabs.Trigger value="features">Key features</Tabs.Trigger>
				<Tabs.Trigger value="activity">Activity</Tabs.Trigger>
				<Tabs.Indicator />
			</Tabs.List>
			<Tabs.Content value="overview">
				A concise overview of the project: usage, goals, and recent highlights. Use this area to orient readers with key metrics and links
				to deeper docs.
			</Tabs.Content>
			<Tabs.Content value="features">
				List the most important features here with short, pragmatic descriptions so readers can scan for what matters (accessibility,
				theming, integrations).
			</Tabs.Content>
			<Tabs.Content value="activity">
				Show recent activity or sample data: new releases, PRs merged, or notable user events. This helps examples feel realistic and
				actionable.
			</Tabs.Content>
		</Tabs>
	);
}

```

## Controlled

Use the `value` and `onValueChange` props to control state programmatically.

```tsx
import { Tabs } from '@skeletonlabs/skeleton-react';
import { useState } from 'react';

export default function Controlled() {
	const [value, setValue] = useState('overview');

	return (
		<Tabs value={value} onValueChange={(details) => setValue(details.value)}>
			<Tabs.List>
				<Tabs.Trigger value="overview">Overview</Tabs.Trigger>
				<Tabs.Trigger value="features">Key features</Tabs.Trigger>
				<Tabs.Trigger value="activity">Activity</Tabs.Trigger>
				<Tabs.Indicator />
			</Tabs.List>
			<Tabs.Content value="overview">
				A concise overview of the project: usage, goals, and recent highlights. Use this area to orient readers with key metrics and links
				to deeper docs.
			</Tabs.Content>
			<Tabs.Content value="features">
				List the most important features here with short, pragmatic descriptions so readers can scan for what matters (accessibility,
				theming, integrations).
			</Tabs.Content>
			<Tabs.Content value="activity">
				Show recent activity or sample data: new releases, PRs merged, or notable user events. This helps examples feel realistic and
				actionable.
			</Tabs.Content>
		</Tabs>
	);
}

```

## Navigation

Use the `element` slot to override the default `button` with an `a` tag for navigation tabs.

```tsx
/**
 * Because demonstrating navigation inside a code snippet is not feasible, this example uses local state to simulate URL path changes.
 *
 * In a real application, you would:
 * - Replace the `url` variable with the `url` of the current page.
 * - Replace `onValueChange={(details) => setUrl(details.value)}` with `navigate((details) => navigate(details.value))` using your framework's navigation method.
 */

import { Tabs } from '@skeletonlabs/skeleton-react';
import { useState, type ComponentProps } from 'react';

export default function Navigation() {
	const [url, setUrl] = useState('#overview');

	return (
		<Tabs value={url} onValueChange={(details) => setUrl(details.value)}>
			<Tabs.List>
				<Tabs.Trigger
					value="#overview"
					element={(attributes) => (
						<a {...(attributes as ComponentProps<'a'>)} href="#overview">
							Overview
						</a>
					)}
				/>
				<Tabs.Trigger
					value="#key-features"
					element={(attributes) => (
						<a {...(attributes as ComponentProps<'a'>)} href="#key-features">
							Key Features
						</a>
					)}
				/>
				<Tabs.Trigger
					value="#activity"
					element={(attributes) => (
						<a {...(attributes as ComponentProps<'a'>)} href="#activity">
							Activity
						</a>
					)}
				/>
				<Tabs.Indicator />
			</Tabs.List>
			<Tabs.Content value="#overview">
				A concise overview of the project: usage, goals, and recent highlights. Use this area to orient readers with key metrics and links
				to deeper docs.
			</Tabs.Content>
			<Tabs.Content value="#key-features">
				List the most important features here with short, pragmatic descriptions so readers can scan for what matters (accessibility,
				theming, integrations).
			</Tabs.Content>
			<Tabs.Content value="#activity">
				Show recent activity or sample data: new releases, PRs merged, or notable user events. This helps examples feel realistic and
				actionable.
			</Tabs.Content>
		</Tabs>
	);
}

```

## Fluid Width

Use `flex` utility classes to make the tabs stretch to fill the width of their container.

```tsx
import { Tabs } from '@skeletonlabs/skeleton-react';

export default function Fluid() {
	return (
		<Tabs defaultValue="overview">
			<Tabs.List>
				<Tabs.Trigger className="flex-1" value="overview">
					Overview
				</Tabs.Trigger>
				<Tabs.Trigger className="flex-1" value="features">
					Key features
				</Tabs.Trigger>
				<Tabs.Trigger className="flex-1" value="activity">
					Activity
				</Tabs.Trigger>
				<Tabs.Indicator />
			</Tabs.List>
			<Tabs.Content value="overview">
				A concise overview of the project: usage, goals, and recent highlights. Use this area to orient readers with key metrics and links
				to deeper docs.
			</Tabs.Content>
			<Tabs.Content value="features">
				List the most important features here with short, pragmatic descriptions so readers can scan for what matters (accessibility,
				theming, integrations).
			</Tabs.Content>
			<Tabs.Content value="activity">
				Show recent activity or sample data: new releases, PRs merged, or notable user events. This helps examples feel realistic and
				actionable.
			</Tabs.Content>
		</Tabs>
	);
}

```

## Orientation

Using the `orientation` prop to control the layout.

```tsx
import { Tabs } from '@skeletonlabs/skeleton-react';

export default function Vertical() {
	return (
		<Tabs defaultValue="overview" orientation="vertical">
			<Tabs.List>
				<Tabs.Trigger value="overview" className="justify-start">
					Overview
				</Tabs.Trigger>
				<Tabs.Trigger value="features" className="justify-start">
					Key features
				</Tabs.Trigger>
				<Tabs.Trigger value="activity" className="justify-start">
					Activity
				</Tabs.Trigger>
				<Tabs.Indicator />
			</Tabs.List>
			<Tabs.Content value="overview">
				A concise overview of the project: usage, goals, and recent highlights. Use this area to orient readers with key metrics and links
				to deeper docs.
			</Tabs.Content>
			<Tabs.Content value="features">
				List the most important features here with short, pragmatic descriptions so readers can scan for what matters (accessibility,
				theming, integrations).
			</Tabs.Content>
			<Tabs.Content value="activity">
				Show recent activity or sample data: new releases, PRs merged, or notable user events. This helps examples feel realistic and
				actionable.
			</Tabs.Content>
		</Tabs>
	);
}

```

## Direction

Set the text direction (`ltr` or `rtl`) using the `dir` prop.

```tsx
import { Tabs } from '@skeletonlabs/skeleton-react';

export default function Dir() {
	return (
		<Tabs defaultValue="overview" dir="rtl">
			<Tabs.List>
				<Tabs.Trigger value="overview">Overview</Tabs.Trigger>
				<Tabs.Trigger value="features">Key features</Tabs.Trigger>
				<Tabs.Trigger value="activity">Activity</Tabs.Trigger>
				<Tabs.Indicator />
			</Tabs.List>
			<Tabs.Content value="overview">
				A concise overview of the project: usage, goals, and recent highlights. Use this area to orient readers with key metrics and links
				to deeper docs.
			</Tabs.Content>
			<Tabs.Content value="features">
				List the most important features here with short, pragmatic descriptions so readers can scan for what matters (accessibility,
				theming, integrations).
			</Tabs.Content>
			<Tabs.Content value="activity">
				Show recent activity or sample data: new releases, PRs merged, or notable user events. This helps examples feel realistic and
				actionable.
			</Tabs.Content>
		</Tabs>
	);
}

```

## Anatomy

Here's an overview of how the Tabs component is structured in code:

```tsx
import { Tabs } from '@skeletonlabs/skeleton-react';

export default function Anatomy() {
	return (
		<Tabs>
			<Tabs.List>
				<Tabs.Trigger />
				<Tabs.Indicator />
			</Tabs.List>
			<Tabs.Content />
		</Tabs>
	);
}
```

## API Reference

### Root

| Prop           | Description                                                                                                                                                                                                       | Type                                                                                                                                               | Default      |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| ids            | The ids of the elements in the tabs. Useful for composition.                                                                                                                                                      | Partial\<\{ root: string; trigger: (value: string) => string; list: string; content: (value: string) => string; indicator: string; }> \| undefined | -            |
| translations   | Specifies the localized strings that identifies the accessibility elements and their states                                                                                                                       | IntlTranslations \| undefined                                                                                                                      | -            |
| loopFocus      | Whether the keyboard navigation will loop from last tab to first, and vice versa.                                                                                                                                 | boolean \| undefined                                                                                                                               | true         |
| value          | The controlled selected tab value                                                                                                                                                                                 | string \| null \| undefined                                                                                                                        | -            |
| defaultValue   | The initial selected tab value when rendered.&#xA;Use when you don't need to control the selected tab value.                                                                                                      | string \| null \| undefined                                                                                                                        | -            |
| orientation    | The orientation of the tabs. Can be \`horizontal\` or \`vertical\`&#xA;- \`horizontal\`: only left and right arrow key navigation will work.&#xA;- \`vertical\`: only up and down arrow key navigation will work. | "horizontal" \| "vertical" \| undefined                                                                                                            | "horizontal" |
| activationMode | The activation mode of the tabs. Can be \`manual\` or \`automatic\`&#xA;- \`manual\`: Tabs are activated when clicked or press \`enter\` key.&#xA;- \`automatic\`: Tabs are activated when receiving focus        | "manual" \| "automatic" \| undefined                                                                                                               | "automatic"  |
| onValueChange  | Callback to be called when the selected/active tab changes                                                                                                                                                        | ((details: ValueChangeDetails) => void) \| undefined                                                                                               | -            |
| onFocusChange  | Callback to be called when the focused tab changes                                                                                                                                                                | ((details: FocusChangeDetails) => void) \| undefined                                                                                               | -            |
| composite      | Whether the tab is composite                                                                                                                                                                                      | boolean \| undefined                                                                                                                               | -            |
| deselectable   | Whether the active tab can be deselected when clicking on it.                                                                                                                                                     | boolean \| undefined                                                                                                                               | -            |
| navigate       | Function to navigate to the selected tab when clicking on it.&#xA;Useful if tab triggers are anchor elements.                                                                                                     | ((details: NavigateDetails) => void) \| null \| undefined                                                                                          | -            |
| dir            | The document's text/writing direction.                                                                                                                                                                            | "ltr" \| "rtl" \| undefined                                                                                                                        | "ltr"        |
| getRootNode    | A root node to correctly resolve document in custom environments. E.x.: Iframes, Electron.                                                                                                                        | (() => ShadowRoot \| Node \| Document) \| undefined                                                                                                | -            |
| element        | Render the element yourself                                                                                                                                                                                       | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined                                                                                     | -            |

### Provider

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| value   | -                           | TabsApi\<PropTypes>                                            | -       |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Context

| Prop     | Description | Type                                     | Default |
| -------- | ----------- | ---------------------------------------- | ------- |
| children | -           | (tabs: TabsApi\<PropTypes>) => ReactNode | -       |

### List

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Trigger

| Prop     | Description                 | Type                                                              | Default |
| -------- | --------------------------- | ----------------------------------------------------------------- | ------- |
| value    | The value of the tab        | string                                                            | -       |
| disabled | Whether the tab is disabled | boolean \| undefined                                              | -       |
| element  | Render the element yourself | ((attributes: HTMLAttributes\<"button">) => Element) \| undefined | -       |

### Indicator

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Content

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| value   | The value of the tab        | string                                                         | -       |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |
