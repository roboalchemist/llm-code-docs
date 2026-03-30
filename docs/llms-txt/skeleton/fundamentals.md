# Source: https://www.skeleton.dev/docs/svelte/get-started/fundamentals.md

# Source: https://www.skeleton.dev/docs/react/get-started/fundamentals.md

# Fundamentals

An introduction to the core concepts of Skeleton.

Skeleton is comprised of three pillars - the design system, our extensions to Tailwind, and an optional suite of framework-specific components. Together these form a comprehensive solution for designing and implementing complex web interfaces at scale.

***

## Design System

Explore each pillar of the Skeleton design system. Provided via the Skeleton core.

<NavigationGrid filter={(doc) => doc.id.includes('design/')} class="md:grid-cols-2" />

***

## Tailwind Components

Tailwind components that act as primitives for creating complex interfaces. Provided via the Skeleton core.

<NavigationGrid filter={(doc) => doc.id.includes('tailwind-components/')} class="md:grid-cols-2" />

***

## Framework Components

Skeleton also offers optional component packages for select component frameworks. Each component automatically adapts to Skeleton's design system. While still allowing a high level of customization.

### Supported Frameworks

\| Framework | NPM Package                     | Description                     |
\| --------- | ------------------------------- | ------------------------------- |
\| React     | `@skeletonlabs/skeleton-react`  | Contains all React components.  |
\| Svelte    | `@skeletonlabs/skeleton-svelte` | Contains all Svelte components. |

### Powered by Zag.js

Skeleton's components are built on **Zag.js**, which provides a collection of framework-agnostic UI component patterns to manage logic and state. Zag is actively maintained by industry veterans, such as [Segun Adebayo](https://github.com/segunadebayo) - the creator and core maintainer for [Chakra UI](https://www.chakra-ui.com/), [Ark UI](https://ark-ui.com/), and [PandaCSS](https://panda-css.com/).

<iframe class="aspect-video" src="https://www.youtube-nocookie.com/embed/SLPBmP588Hk?si=NJLvt4aMrevTnQbY" title="Skeleton + Zag.js: Building Cross-Framework Components" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

<figure class="linker bg-noise">
  <a class="btn preset-filled" href="https://zagjs.com/" target="_blank">
    View Zag.js
  </a>
</figure>

### Importing Components

You may import components per each Skeleton framework as follows.

```ts
import { Avatar } from '@skeletonlabs/skeleton-react';
```

This also includes access to the component prop types.

```ts
import type { AvatarRootProps, ... } from '@skeletonlabs/skeleton-react';
```

### Composed Pattern

Skeleton components are granular. This offers direct access to all children within the tree, similar to working with raw HTML. This allows passing in arbitrary props and attributes directly to the template within. Including: `required`, `data-*`, `style`, `className`, and more.

```tsx
export default function Avatar() {
	return (
		<Avatar>
			<Avatar.Image src="https://i.pravatar.cc/150?img=48" />
			<Avatar.Fallback>SK</Avatar.Fallback>
		</Avatar>
	);
}
```

### Styling Components

Skeleton components implement a universal convention for accepting CSS utility classes via the `className` attribute. Use this to pass any CSS utility class.

```tsx
export default function Avatar() {
	return (
		<Avatar className="rounded-2xl">
			<Avatar.Image src="https://i.pravatar.cc/150?img=48" className="grayscale" />
			<Avatar.Fallback>SK</Avatar.Fallback>
		</Avatar>
	);
}
```

### Extensible Markup

Skeleton components provide a mechanism for overwriting the internal HTML with custom markup. Use the `element` prop to provide a custom element, this prop accepts a function which the `attributes` are passed into. Then spread the `attributes` to your custom elements. Note that this is an optional and advanced feature aimed at power users, and should not be needed for normal usage.

```tsx
export default function () {
	return (
		<Accordion>
			<Accordion.Item value="item-1">
				<h3>
					<Accordion.ItemTrigger element={(attributes) => <button {...attributes}>My Own Button</button>} />
				</h3>
				<Accordion.ItemContent>Content for Item 1</Accordion.ItemContent>
			</Accordion.Item>
		</Accordion>
	);
}
```

### Custom Animations

Using the extensible markup pattern, you may implement custom animations. We showcase this below with [Motion](https://motion.dev/), but you could also use framework agnostic solutions such as [Anime.js](https://animejs.com/) or [Animate.css](https://animate.style/).

```tsx
import { Accordion } from '@skeletonlabs/skeleton-react';
import { motion, AnimatePresence } from 'motion/react';

export default function CustomAnimation() {
	return (
		<Accordion>
			{['1', '2', '3'].map((item) => (
				<Accordion.Item key={item} value={item}>
					<h3>
						<Accordion.ItemTrigger>Item {item}</Accordion.ItemTrigger>
					</h3>
					<Accordion.ItemContent
						element={(attributes) => (
							<AnimatePresence initial={false}>
								{!attributes.hidden && (
									<motion.div
										className="overflow-hidden"
										initial={{ height: 0, opacity: 0 }}
										animate={{ height: 'auto', opacity: 1 }}
										exit={{ height: 0, opacity: 0 }}
									>
										<div {...attributes}>Content for item {item}</div>
									</motion.div>
								)}
							</AnimatePresence>
						)}
					/>
				</Accordion.Item>
			))}
		</Accordion>
	);
}
```

1. Implement the `element` snippet to gain access to the `attributes`.
2. Spread the `attributes` to the custom element, a `<div>` in this example.
3. Wrap the custom element in Motion's `<AnimatePresence>`.
4. Then implement conditional rendering that triggers animations when `attributes.hidden` is toggled.

### Data Model Pattern

Skeleton components maintain a uniform pattern for handling data flow in and out. We lean into the Zag convention for this, which handles this explictly with a prop for data in and event handler for data out. As opposed to two-way binding (such as `bind:` in Svelte). You can see this in practice below for the Switch component.

```tsx
import { Switch } from '@skeletonlabs/skeleton-react';
import { useState } from 'react';

export default function Default() {
	const [checked, setChecked] = useState(false);

    return (
    	<Switch checked={checked} onCheckedChange={(e) => setChecked(e.checked)}>
    		<Switch.Control>
    			<Switch.Thumb />
    		</Switch.Control>
    		<Switch.Label>Label</Switch.Label>
    		<Switch.HiddenInput />
    	</Switch>
    );

}

```

In this example the Switch component uses `checked` to pass state in, and `onCheckedChange` to listen and update then the state is modified internally. Please note the prop, event prop, and key within the event payload may vary from component to component. For example:

* `<Accordion>` - handled via `open` / `onOpenChange` / `e.change`
* `<Slider>` - handled via `value` / `onValueChange` / `e.value`
* `<Stepper>` - handled via `step` / `onStepChange` / `e.step`

This pattern is utilized for all relevant components, and is documented via the [API Reference](/docs/framework-components/switch#api-reference) table per component.

### Provider Pattern

Most Skeleton components also support the Provider Pattern. This utilizes a provider component that replaces the root and provides access to the underlying component APIs. In practice, this allows direct access to Zag.js API features, such as programmatic control for overlay components, the ability to clear input components, and more.

```tsx
import { Portal, Tooltip, useTooltip } from '@skeletonlabs/skeleton-react';

export default function TooltipExample() {
	const tooltip = useTooltip();

	return (
		<>
			<button type="button" onClick={() => tooltip.setOpen(!tooltip.open)}>
				Trigger
			</button>

			<Tooltip.Provider value={tooltip}>
				<Tooltip.Trigger>Anchor</Tooltip.Trigger>
				<Portal>
					<Tooltip.Positioner>
						<Tooltip.Content>Content</Tooltip.Content>
					</Tooltip.Positioner>
				</Portal>
			</Tooltip.Provider>
		</>
	);
}
```

### Learn More

For a comprehensive guide to how Skeleton implements components, refer to our [contribution guidelines](/docs/\[framework]/resources/contribute/components).

```
```
