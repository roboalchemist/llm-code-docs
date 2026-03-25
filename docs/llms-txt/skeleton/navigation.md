# Source: https://www.skeleton.dev/docs/svelte/framework-components/navigation.md

# Source: https://www.skeleton.dev/docs/react/framework-components/navigation.md

# Navigation

Navigation patterns for apps (bar, rail, sidebar, toggle).

## Bar

```tsx
import { Navigation } from '@skeletonlabs/skeleton-react';
import { BookIcon } from 'lucide-react';
import { HouseIcon } from 'lucide-react';
import { PopcornIcon } from 'lucide-react';
import { TvIcon } from 'lucide-react';

export default function Default() {
	const links = [
		{ label: 'Home', href: '/#', icon: HouseIcon },
		{ label: 'Books', href: '/#', icon: BookIcon },
		{ label: 'Movies', href: '/#', icon: PopcornIcon },
		{ label: 'Television', href: '/#', icon: TvIcon },
	];

	return (
		<div className="w-[375px] h-[667px] grid grid-rows-[1fr_auto] border border-surface-200-800">
			<div className="flex justify-center items-center">
				<p>Contents</p>
			</div>
			<Navigation layout="bar">
				<Navigation.Menu className="grid grid-cols-4 gap-2">
					{links.map((link) => {
						const Icon = link.icon;
						return (
							<Navigation.TriggerAnchor key={link.label} href={link.href}>
								<Icon className="size-5" />
								<Navigation.TriggerText>{link.label}</Navigation.TriggerText>
							</Navigation.TriggerAnchor>
						);
					})}
				</Navigation.Menu>
			</Navigation>
		</div>
	);
}

```

* Recommended for small sized screens (ex: mobile).
* Ideal for vertical screen layouts.
* Should be fixed to the bottom of the viewport.
* Supports 3-5 tiles based on contents and viewport width.
* Consider progressive enhancement with the [Virtual Keyboard API](https://developer.mozilla.org/en-US/docs/Web/API/VirtualKeyboard_API).

## Rail

```tsx
import { Navigation } from '@skeletonlabs/skeleton-react';
import { BookIcon } from 'lucide-react';
import { HouseIcon } from 'lucide-react';
import { PopcornIcon } from 'lucide-react';
import { SkullIcon } from 'lucide-react';
import { SettingsIcon } from 'lucide-react';
import { TvIcon } from 'lucide-react';

export default function Default() {
	const links = [
		{ label: 'Home', href: '/#', icon: HouseIcon },
		{ label: 'Books', href: '/#', icon: BookIcon },
		{ label: 'Movies', href: '/#', icon: PopcornIcon },
		{ label: 'Television', href: '/#', icon: TvIcon },
	];

	return (
		<div className="w-full h-[728px] grid grid-cols-[auto_1fr] border border-surface-200-800">
			<Navigation layout="rail">
				<Navigation.Header>
					<Navigation.TriggerAnchor href="/" title="View Homepage" aria-label="View Homepage">
						<SkullIcon className="size-8" />
					</Navigation.TriggerAnchor>
				</Navigation.Header>
				<Navigation.Content>
					<Navigation.Menu>
						{links.map((link) => {
							const Icon = link.icon;
							return (
								<Navigation.TriggerAnchor key={link.label} href={link.href}>
									<Icon className="size-5" />
									<Navigation.TriggerText>{link.label}</Navigation.TriggerText>
								</Navigation.TriggerAnchor>
							);
						})}
					</Navigation.Menu>
				</Navigation.Content>
				<Navigation.Footer>
					<Navigation.TriggerAnchor href="#" title="Settings" aria-label="Settings">
						<SettingsIcon className="size-5" />
					</Navigation.TriggerAnchor>
				</Navigation.Footer>
			</Navigation>
			<div className="flex justify-center items-center">
				<p className="opacity-50">Contents</p>
			</div>
		</div>
	);
}

```

* Recommended for medium sized screens (ex: tablet).
* Ideal for horizontal screen layouts.
* Should be fixed to the left or right of the viewport.
* Supports 3-7 tiles based on contents and viewport height.

## Sidebar

```tsx
import { Navigation } from '@skeletonlabs/skeleton-react';
import { BikeIcon } from 'lucide-react';
import { BookIcon } from 'lucide-react';
import { HouseIcon } from 'lucide-react';
import { MountainIcon } from 'lucide-react';
import { PopcornIcon } from 'lucide-react';
import { SailboatIcon } from 'lucide-react';
import { SettingsIcon } from 'lucide-react';
import { SkullIcon } from 'lucide-react';
import { TvIcon } from 'lucide-react';
import { WavesIcon } from 'lucide-react';

export default function Default() {
	const linksSidebar = {
		entertainment: [
			{ label: 'Books', href: '/#', icon: BookIcon },
			{ label: 'Movies', href: '/#', icon: PopcornIcon },
			{ label: 'Television', href: '/#', icon: TvIcon },
		],
		recreation: [
			{ label: 'Biking', href: '/#', icon: BikeIcon },
			{ label: 'Sailing', href: '/#', icon: SailboatIcon },
			{ label: 'Hiking', href: '/#', icon: MountainIcon },
			{ label: 'Swimming', href: '/#', icon: WavesIcon },
		],
	};

	return (
		<div className="w-full h-[728px] grid grid-cols-[auto_1fr] items-stretch border border-surface-200-800">
			<Navigation layout="sidebar" className="grid grid-rows-[auto_1fr_auto] gap-4">
				<Navigation.Header>
					<Navigation.TriggerAnchor href="https://www.skeleton.dev">
						<SkullIcon className="size-6" />
					</Navigation.TriggerAnchor>
				</Navigation.Header>
				<Navigation.Content>
					<Navigation.Group>
						<Navigation.Menu>
							<Navigation.TriggerAnchor href="/">
								<HouseIcon className="size-4" />
								<Navigation.TriggerText>Home</Navigation.TriggerText>
							</Navigation.TriggerAnchor>
						</Navigation.Menu>
					</Navigation.Group>
					{Object.entries(linksSidebar).map(([category, links]) => (
						<Navigation.Group key={category}>
							<Navigation.Label className="capitalize pl-2">{category}</Navigation.Label>
							<Navigation.Menu>
								{links.map((link) => {
									const Icon = link.icon;
									return (
										<Navigation.TriggerAnchor key={link.label} title={link.label} aria-label={link.label}>
											<Icon className="size-4" />
											<Navigation.TriggerText>{link.label}</Navigation.TriggerText>
										</Navigation.TriggerAnchor>
									);
								})}
							</Navigation.Menu>
						</Navigation.Group>
					))}
				</Navigation.Content>
				<Navigation.Footer>
					<Navigation.TriggerAnchor href="/" title="Settings" aria-label="Settings">
						<SettingsIcon className="size-4" />
						<Navigation.TriggerText>Settings</Navigation.TriggerText>
					</Navigation.TriggerAnchor>
				</Navigation.Footer>
			</Navigation>
			<div className="flex justify-center items-center">
				<p className="opacity-50">Contents</p>
			</div>
		</div>
	);
}

```

* Recommended for large sized screens (ex: desktop).
* Ideal for horizontal screen layouts.
* Should be fixed to the left or right of the viewport.
* Supports multiple groups of links for deep navigation.
* Supports a label field per each group.
* Can scroll vertically if contents extend beyond the viewport height.

## Toggle Layout

Using reactive state we can dynamically switch between multiple layouts. Tap the double arrow icon to toggle.

```tsx
import { Navigation } from '@skeletonlabs/skeleton-react';
import { BookIcon } from 'lucide-react';
import { HouseIcon } from 'lucide-react';
import { PopcornIcon } from 'lucide-react';
import { TvIcon } from 'lucide-react';
import { ArrowLeftRightIcon } from 'lucide-react';
import { useState } from 'react';

export default function Default() {
	const links = [
		{ label: 'Home', href: '/#', icon: HouseIcon },
		{ label: 'Books', href: '/#', icon: BookIcon },
		{ label: 'Movies', href: '/#', icon: PopcornIcon },
		{ label: 'Television', href: '/#', icon: TvIcon },
	];

	let [layoutRail, setLayoutRail] = useState(true);

	function toggleLayout() {
		setLayoutRail(!layoutRail);
	}

	return (
		<div className="w-full h-[728px] grid grid-cols-[auto_1fr] items-stretch border border-surface-200-800">
			<Navigation layout={layoutRail ? 'rail' : 'sidebar'} className={layoutRail ? '' : 'grid grid-rows-[1fr_auto] gap-4'}>
				<Navigation.Content>
					<Navigation.Header>
						<Navigation.Trigger onClick={toggleLayout}>
							<ArrowLeftRightIcon className={layoutRail ? 'size-5' : 'size-4'} />
							{!layoutRail ? <span>Resize</span> : ''}
						</Navigation.Trigger>
					</Navigation.Header>
					<Navigation.Menu>
						{links.map((link) => {
							const Icon = link.icon;
							return (
								<Navigation.TriggerAnchor key={link.label}>
									<Icon className={layoutRail ? 'size-5' : 'size-4'} />
									<Navigation.TriggerText>{link.label}</Navigation.TriggerText>
								</Navigation.TriggerAnchor>
							);
						})}
					</Navigation.Menu>
				</Navigation.Content>
			</Navigation>
			<div className="flex justify-center items-center">
				<p className="opacity-50">Contents</p>
			</div>
		</div>
	);
}

```

## Anatomy

Here's an overview of how the Navigation component is structured in code:

```tsx
import { Navigation } from '@skeletonlabs/skeleton-react';

export default function Anatomy() {
	return (
		<Navigation>
			<Navigation.Header />
			<Navigation.Content>
				<Navigation.Group>
					<Navigation.Label />
					<Navigation.Menu>
						<Navigation.Trigger>
							<Navigation.TriggerText />
						</Navigation.Trigger>
						<Navigation.TriggerAnchor>
							<Navigation.TriggerText />
						</Navigation.TriggerAnchor>
					</Navigation.Menu>
				</Navigation.Group>
			</Navigation.Content>
			<Navigation.Footer />
		</Navigation>
	);
}
```

## API Reference

### Root

| Prop    | Description                                                                                  | Type                                                           | Default |
| ------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | ------- |
| layout  | Sets the data-layout attribute, which modifies the visual presentation of the component set. | "bar" \| "rail" \| "sidebar" \| undefined                      | bar     |
| element | Render the element yourself                                                                  | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Header

| Prop    | Description                 | Type                                                              | Default |
| ------- | --------------------------- | ----------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"header">) => Element) \| undefined | -       |

### Content

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Group

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Label

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Menu

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Trigger

| Prop    | Description                 | Type                                                              | Default |
| ------- | --------------------------- | ----------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"button">) => Element) \| undefined | -       |

### TriggerAnchor

| Prop    | Description                 | Type                                                         | Default |
| ------- | --------------------------- | ------------------------------------------------------------ | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"a">) => Element) \| undefined | -       |

### TriggerText

| Prop    | Description                 | Type                                                            | Default |
| ------- | --------------------------- | --------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"span">) => Element) \| undefined | -       |

### Footer

| Prop    | Description                 | Type                                                              | Default |
| ------- | --------------------------- | ----------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"footer">) => Element) \| undefined | -       |
