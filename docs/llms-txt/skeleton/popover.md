# Source: https://www.skeleton.dev/docs/svelte/framework-components/popover.md

# Source: https://www.skeleton.dev/docs/react/framework-components/popover.md

# Popover

Small overlay panels positioned relative to a trigger.

```tsx
import { Avatar, Popover, Portal } from '@skeletonlabs/skeleton-react';
import { XIcon } from 'lucide-react';

export default function Default() {
	return (
		<Popover>
			<Popover.Trigger className="btn preset-filled">Trigger</Popover.Trigger>
			<Portal>
				<Popover.Positioner>
					<Popover.Content className="card w-96 p-4 bg-surface-100-900 shadow-xl">
						<div className="space-y-4">
							<header className="grid grid-cols-[auto_1fr_auto] gap-4 items-center">
								<Avatar>
									<Avatar.Image
										src="https://cdn.bsky.app/img/avatar/plain/did:plc:whtgi5zx7ylmdw2i76vq7vq4/bafkreibgoxuqahwcpiah22yfovqszh33x2u4sysmqoyuk5j54aoakt7364@jpeg"
										alt="Skeleton Labs"
									/>
								</Avatar>
								<div>
									<Popover.Title className="text-lg font-bold">Skeleton Labs</Popover.Title>
									<a href="https://bsky.app/profile/skeleton.dev" target="_blank" rel="noopener noreferrer" className="anchor">
										@skeletonlabs.dev
									</a>
								</div>
								<Popover.CloseTrigger className="btn-icon hover:preset-tonal self-start">
									<XIcon className="size-4" />
								</Popover.CloseTrigger>
							</header>
							<Popover.Description>Your friendly neighborhood open source maintainers. Creators of Skeleton.</Popover.Description>
							<div className="flex gap-4">
								<p className="text-sm">
									800 <span className="opacity-60">Followers</span>
								</p>
								<p className="text-sm">
									120 <span className="opacity-60">Following</span>
								</p>
								<p className="text-sm">
									100 <span className="opacity-60">Posts</span>
								</p>
							</div>
						</div>
						<Popover.Arrow className="[--arrow-size:--spacing(2)] [--arrow-background:var(--color-surface-100-900)]">
							<Popover.ArrowTip />
						</Popover.Arrow>
					</Popover.Content>
				</Popover.Positioner>
			</Portal>
		</Popover>
	);
}

```

Breaking convention in Skeleton, this component is provided "headless". Meaning no default styles are applied out of the box. This ensures you retain full control of all styling for maximum flexibility.

## Anchor

Use the `Anchor` component to position the popover contents relative to an element other than the trigger.

```tsx
import { Avatar, Popover, Portal } from '@skeletonlabs/skeleton-react';
import { XIcon } from 'lucide-react';

export default function Anchor() {
	return (
		<Popover>
			<div className="flex items-center gap-4">
				<Popover.Anchor>
					<Avatar>
						<Avatar.Image
							src="https://cdn.bsky.app/img/avatar/plain/did:plc:whtgi5zx7ylmdw2i76vq7vq4/bafkreibgoxuqahwcpiah22yfovqszh33x2u4sysmqoyuk5j54aoakt7364@jpeg"
							alt="Skeleton Labs"
						/>
					</Avatar>
				</Popover.Anchor>
				<Popover.Trigger className="btn preset-filled">Show Profile</Popover.Trigger>
			</div>
			<Portal>
				<Popover.Positioner>
					<Popover.Content className="card w-96 p-4 bg-surface-100-900 shadow-xl">
						<div className="space-y-4">
							<header className="grid grid-cols-[auto_1fr_auto] gap-4 items-center">
								<Avatar>
									<Avatar.Image
										src="https://cdn.bsky.app/img/avatar/plain/did:plc:whtgi5zx7ylmdw2i76vq7vq4/bafkreibgoxuqahwcpiah22yfovqszh33x2u4sysmqoyuk5j54aoakt7364@jpeg"
										alt="Skeleton Labs"
									/>
								</Avatar>
								<div>
									<Popover.Title className="text-lg font-bold">Skeleton Labs</Popover.Title>
									<a href="https://bsky.app/profile/skeleton.dev" target="_blank" rel="noopener noreferrer" className="anchor">
										@skeletonlabs.dev
									</a>
								</div>
								<Popover.CloseTrigger className="btn-icon hover:preset-tonal self-start">
									<XIcon className="size-4" />
								</Popover.CloseTrigger>
							</header>
							<Popover.Description>Your friendly neighborhood open source maintainers. Creators of Skeleton.</Popover.Description>
							<div className="flex gap-4">
								<p className="text-sm">
									800 <span className="opacity-60">Followers</span>
								</p>
								<p className="text-sm">
									120 <span className="opacity-60">Following</span>
								</p>
								<p className="text-sm">
									100 <span className="opacity-60">Posts</span>
								</p>
							</div>
						</div>
						<Popover.Arrow className="[--arrow-size:--spacing(2)] [--arrow-background:var(--color-surface-100-900)]">
							<Popover.ArrowTip />
						</Popover.Arrow>
					</Popover.Content>
				</Popover.Positioner>
			</Portal>
		</Popover>
	);
}

```

## Arrow

Visually connects the popover content to the trigger element. Will automatically align based on the selected side.

```tsx
import { Popover, Portal } from '@skeletonlabs/skeleton-react';

export default function Arrow() {
	return (
		<Popover>
			<Popover.Trigger className="btn preset-filled">Trigger</Popover.Trigger>
			<Portal>
				<Popover.Positioner>
					<Popover.Content className="card max-w-md p-4 bg-surface-100-900 shadow-xl">
						<Popover.Description>This example will have a small arrow.</Popover.Description>
						<Popover.Arrow className="[--arrow-size:--spacing(2)] [--arrow-background:var(--color-surface-100-900)]">
							<Popover.ArrowTip />
						</Popover.Arrow>
					</Popover.Content>
				</Popover.Positioner>
			</Portal>
		</Popover>
	);
}

```

## Z-Index

By default Skeleton does not take an opinionated stance regarding z-index stacking. The result is the component can sometimes be occluded beneath other elements with a higher index. The Z-Index can controlled by applying a utility class to the `Positioner` component.

```tsx
import { Popover, Portal } from '@skeletonlabs/skeleton-react';

export default function ZIndex() {
	return (
		<div className="grid grid-cols-2 gap-4">
			<Popover>
				<Popover.Trigger className="btn preset-filled">Default (auto)</Popover.Trigger>
				<Portal>
					<Popover.Positioner>
						<Popover.Content className="card max-w-md p-4 bg-surface-100-900 space-y-2">
							<Popover.Description>This example will be below the sibling.</Popover.Description>
						</Popover.Content>
					</Popover.Positioner>
				</Portal>
			</Popover>

			<Popover>
				<Popover.Trigger className="btn preset-filled">Above (20)</Popover.Trigger>
				<Portal>
					<Popover.Positioner className="z-20!">
						<Popover.Content className="card max-w-md p-4 bg-surface-100-900 shadow-xl space-y-2">
							<Popover.Description>This example will be above the sibling.</Popover.Description>
						</Popover.Content>
					</Popover.Positioner>
				</Portal>
			</Popover>

			<div className="col-span-2 h-[100px] relative">
				<div className="rounded bg-primary-200-800/75 w-full h-full z-10 flex justify-center items-center absolute">Sibling (10)</div>
			</div>
		</div>
	);
}

```

## Provider Pattern

Use the [Provider Pattern](/docs/\[framework]/get-started/fundamentals#provider-pattern) to gain access to the inner component APIs.

```tsx
import { Popover, Portal, usePopover } from '@skeletonlabs/skeleton-react';

export default function Default() {
	const popover = usePopover({
		closeOnInteractOutside: false,
	});

	function showAndHide() {
		popover.setOpen(true);
		setTimeout(() => {
			popover.setOpen(false);
		}, 3000);
	}
	return (
		<div className="flex flex-col gap-4">
			<button className="btn preset-filled" onClick={showAndHide}>
				Show for 3 seconds
			</button>

			<Popover.Provider value={popover}>
				<Popover.Trigger className="btn preset-tonal">Anchor</Popover.Trigger>
				<Portal>
					<Popover.Positioner>
						<Popover.Content className="card max-w-sm p-4 bg-surface-100-900 shadow-xl space-y-2">
							<Popover.Description>This popover will appear, stay open for three seconds, then close on it's own.</Popover.Description>
						</Popover.Content>
					</Popover.Positioner>
				</Portal>
			</Popover.Provider>
		</div>
	);
}

```

## Direction

Set the text direction (`ltr` or `rtl`) using the `dir` prop.

```tsx
import { Popover, Portal } from '@skeletonlabs/skeleton-react';

export default function Dir() {
	return (
		<Popover dir="rtl">
			<Popover.Trigger className="btn preset-filled">Trigger</Popover.Trigger>
			<Portal>
				<Popover.Positioner>
					<Popover.Content className="card max-w-md p-4 bg-surface-100-900 shadow-xl space-y-2">
						<Popover.Title className="font-bold">Title</Popover.Title>
						<Popover.Description>
							Lorem ipsum dolor, sit amet consectetur adipisicing elit. Sapiente magni distinctio explicabo quisquam. Rerum impedit culpa
							nesciunt enim.
						</Popover.Description>
						<Popover.CloseTrigger className="btn preset-tonal">Close</Popover.CloseTrigger>
					</Popover.Content>
				</Popover.Positioner>
			</Portal>
		</Popover>
	);
}

```

## Anatomy

Here's an overview of how the Popover component is structured in code:

```tsx
import { Popover, Portal } from '@skeletonlabs/skeleton-react';

export default function Anatomy() {
	return (
		<Popover>
			<Popover.Anchor />
			<Popover.Trigger />
			<Portal>
				<Popover.Positioner>
					<Popover.Content>
						<Popover.Title />
						<Popover.Description />
						<Popover.CloseTrigger />
						<Popover.Arrow>
							<Popover.ArrowTip />
						</Popover.Arrow>
					</Popover.Content>
				</Popover.Positioner>
			</Portal>
		</Popover>
	);
}
```

## API Reference

### Root

| Prop                   | Description                                                                                                                                                                                                                                           | Type                                                                                                                                                                       | Default |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| children               | -                                                                                                                                                                                                                                                     | ReactNode                                                                                                                                                                  | -       |
| ids                    | The ids of the elements in the popover. Useful for composition.                                                                                                                                                                                       | Partial\<\{ anchor: string; trigger: string; content: string; title: string; description: string; closeTrigger: string; positioner: string; arrow: string; }> \| undefined | -       |
| modal                  | Whether the popover should be modal. When set to \`true\`:&#xA;- interaction with outside elements will be disabled&#xA;- only popover content will be visible to screen readers&#xA;- scrolling is blocked&#xA;- focus is trapped within the popover | boolean \| undefined                                                                                                                                                       | false   |
| portalled              | Whether the popover is portalled. This will proxy the tabbing behavior regardless of the DOM position&#xA;of the popover content.                                                                                                                     | boolean \| undefined                                                                                                                                                       | true    |
| autoFocus              | Whether to automatically set focus on the first focusable&#xA;content within the popover when opened.                                                                                                                                                 | boolean \| undefined                                                                                                                                                       | true    |
| initialFocusEl         | The element to focus on when the popover is opened.                                                                                                                                                                                                   | (() => HTMLElement \| null) \| undefined                                                                                                                                   | -       |
| closeOnInteractOutside | Whether to close the popover when the user clicks outside of the popover.                                                                                                                                                                             | boolean \| undefined                                                                                                                                                       | true    |
| closeOnEscape          | Whether to close the popover when the escape key is pressed.                                                                                                                                                                                          | boolean \| undefined                                                                                                                                                       | true    |
| onOpenChange           | Function invoked when the popover opens or closes                                                                                                                                                                                                     | ((details: OpenChangeDetails) => void) \| undefined                                                                                                                        | -       |
| positioning            | The user provided options used to position the popover content                                                                                                                                                                                        | PositioningOptions \| undefined                                                                                                                                            | -       |
| open                   | The controlled open state of the popover                                                                                                                                                                                                              | boolean \| undefined                                                                                                                                                       | -       |
| defaultOpen            | The initial open state of the popover when rendered.&#xA;Use when you don't need to control the open state of the popover.                                                                                                                            | boolean \| undefined                                                                                                                                                       | -       |
| getRootNode            | A root node to correctly resolve document in custom environments. E.x.: Iframes, Electron.                                                                                                                                                            | (() => Node \| ShadowRoot \| Document) \| undefined                                                                                                                        | -       |
| dir                    | The document's text/writing direction.                                                                                                                                                                                                                | "ltr" \| "rtl" \| undefined                                                                                                                                                | "ltr"   |
| onEscapeKeyDown        | Function called when the escape key is pressed                                                                                                                                                                                                        | ((event: KeyboardEvent) => void) \| undefined                                                                                                                              | -       |
| onRequestDismiss       | Function called when this layer is closed due to a parent layer being closed                                                                                                                                                                          | ((event: LayerDismissEvent) => void) \| undefined                                                                                                                          | -       |
| onPointerDownOutside   | Function called when the pointer is pressed down outside the component                                                                                                                                                                                | ((event: PointerDownOutsideEvent) => void) \| undefined                                                                                                                    | -       |
| onFocusOutside         | Function called when the focus is moved outside the component                                                                                                                                                                                         | ((event: FocusOutsideEvent) => void) \| undefined                                                                                                                          | -       |
| onInteractOutside      | Function called when an interaction happens outside the component                                                                                                                                                                                     | ((event: InteractOutsideEvent) => void) \| undefined                                                                                                                       | -       |
| persistentElements     | Returns the persistent elements that:&#xA;- should not have pointer-events disabled&#xA;- should not trigger the dismiss event                                                                                                                        | (() => Element \| null)\[] \| undefined                                                                                                                                    | -       |

### Provider

| Prop     | Description | Type                   | Default |
| -------- | ----------- | ---------------------- | ------- |
| value    | -           | PopoverApi\<PropTypes> | -       |
| children | -           | ReactNode              | -       |

### Context

| Prop     | Description | Type                                           | Default |
| -------- | ----------- | ---------------------------------------------- | ------- |
| children | -           | (popover: PopoverApi\<PropTypes>) => ReactNode | -       |

### Anchor

| Prop     | Description                 | Type                                                           | Default |
| -------- | --------------------------- | -------------------------------------------------------------- | ------- |
| children | -                           | ReactNode                                                      | -       |
| element  | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Trigger

| Prop     | Description                 | Type                                                              | Default |
| -------- | --------------------------- | ----------------------------------------------------------------- | ------- |
| children | -                           | ReactNode                                                         | -       |
| element  | Render the element yourself | ((attributes: HTMLAttributes\<"button">) => Element) \| undefined | -       |

### Positioner

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Content

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Arrow

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### ArrowTip

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Title

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Description

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### CloseTrigger

| Prop    | Description                 | Type                                                              | Default |
| ------- | --------------------------- | ----------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"button">) => Element) \| undefined | -       |
