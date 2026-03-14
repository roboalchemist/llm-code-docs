# Source: https://www.skeleton.dev/docs/svelte/framework-components/dialog.md

# Source: https://www.skeleton.dev/docs/react/framework-components/dialog.md

# Dialog

A modal dialog for displaying content and actions.

```tsx
import { Dialog, Portal } from '@skeletonlabs/skeleton-react';
import { XIcon } from 'lucide-react';

export default function Default() {
	// The following animation is optional.
	// This may also be included inline.
	const animation =
		'transition transition-discrete opacity-0 translate-y-[100px] starting:data-[state=open]:opacity-0 starting:data-[state=open]:translate-y-[100px] data-[state=open]:opacity-100 data-[state=open]:translate-y-0';

	return (
		<Dialog>
			<Dialog.Trigger className="btn preset-filled">Trigger</Dialog.Trigger>
			<Portal>
				<Dialog.Backdrop className="fixed inset-0 z-50 bg-surface-50-950/50" />
				<Dialog.Positioner className="fixed inset-0 z-50 flex justify-center items-center p-4">
					<Dialog.Content className={`card bg-surface-100-900 w-full max-w-xl p-4 space-y-4 shadow-xl ${animation}`}>
						<header className="flex justify-between items-center">
							<Dialog.Title className="text-lg font-bold">Hello Skeleton</Dialog.Title>
							<Dialog.CloseTrigger className="btn-icon hover:preset-tonal">
								<XIcon className="size-4" />
							</Dialog.CloseTrigger>
						</header>
						<Dialog.Description>
							Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
						</Dialog.Description>
						<footer className="flex justify-end gap-2">
							<Dialog.CloseTrigger className="btn preset-tonal">Cancel</Dialog.CloseTrigger>
							<button type="button" className="btn preset-filled">
								Save
							</button>
						</footer>
					</Dialog.Content>
				</Dialog.Positioner>
			</Portal>
		</Dialog>
	);
}

```

Breaking convention in Skeleton, this component is provided "headless". Meaning no default styles are applied out of the box. This ensures you retain full control of all styling for maximum flexibility.

## Alert Dialog

The [alertdialog](https://w3c.github.io/aria/#alertdialog) role enables assistive technologies and browsers to distinguish alert dialogs from other dialogs so they have the option of giving alert dialogs special treatment, such as playing a system alert sound.

```tsx
import { Dialog, Portal } from '@skeletonlabs/skeleton-react';

export default function AlertDialog() {
	return (
		<Dialog role="alertdialog">
			<Dialog.Trigger className="btn preset-filled">Trigger</Dialog.Trigger>
			<Portal>
				<Dialog.Backdrop className="fixed inset-0 z-50 bg-error-50-950/50" />
				<Dialog.Positioner className="fixed inset-0 z-50 flex justify-center items-center">
					<Dialog.Content className="card preset-filled-error-500 w-md p-4 space-y-2 shadow-xl">
						<Dialog.Title className="text-2xl font-bold">Alert</Dialog.Title>
						<Dialog.Description>Something important has happened!</Dialog.Description>
						<Dialog.CloseTrigger className="btn preset-tonal-error">Close</Dialog.CloseTrigger>
					</Dialog.Content>
				</Dialog.Positioner>
			</Portal>
		</Dialog>
	);
}

```

## Interaction

If desired, you can disable click to close interactions for the backdrop.

> TIP: use this sparingly, as this can trap users in this experience without a dedicated close action.

```tsx
import { Dialog, Portal } from '@skeletonlabs/skeleton-react';

export default function Interaction() {
	return (
		<Dialog closeOnInteractOutside={false}>
			<Dialog.Trigger className="btn preset-filled">Trigger</Dialog.Trigger>
			<Portal>
				<Dialog.Backdrop className="fixed inset-0 z-50 bg-surface-50-950/50" />
				<Dialog.Positioner className="fixed inset-0 z-50 flex justify-center items-center">
					<Dialog.Content className="card bg-surface-100-900 w-md p-4 space-y-2 shadow-xl">
						<Dialog.Title className="text-2xl font-bold">Dialog Title</Dialog.Title>
						<Dialog.Description>This dialog will only close with the Close button or via programmatic controls.</Dialog.Description>
						<Dialog.CloseTrigger className="btn preset-tonal">Close</Dialog.CloseTrigger>
					</Dialog.Content>
				</Dialog.Positioner>
			</Portal>
		</Dialog>
	);
}

```

## Drawer

This example repurposes the Dialog for use as a side-panel Drawer. This pairs well with the [Navigation Sidebar](/docs/svelte/framework-components/navigation#sidebar).

```tsx
import { Dialog, Portal } from '@skeletonlabs/skeleton-react';
import { XIcon } from 'lucide-react';

export default function Drawer() {
	// The following animations are optional.
	// These may also be included inline.
	const animBackdrop = 'transition transition-discrete opacity-0 starting:data-[state=open]:opacity-0 data-[state=open]:opacity-100';
	const animModal =
		'transition transition-discrete opacity-0 -translate-x-full starting:data-[state=open]:opacity-0 starting:data-[state=open]:-translate-x-full data-[state=open]:opacity-100 data-[state=open]:translate-x-0';

	return (
		<Dialog>
			<Dialog.Trigger className="btn preset-filled">Trigger</Dialog.Trigger>
			<Portal>
				<Dialog.Backdrop className={`fixed inset-0 z-50 bg-surface-50-950/50 ${animBackdrop}`} />
				<Dialog.Positioner className="fixed inset-0 z-50 flex justify-start">
					<Dialog.Content className={`h-screen card bg-surface-100-900 w-sm p-4 space-y-4 shadow-xl ${animModal}`}>
						<header className="flex justify-between items-center">
							<Dialog.Title className="text-2xl font-bold">Drawer</Dialog.Title>
							<Dialog.CloseTrigger className="btn-icon preset-tonal">
								<XIcon />
							</Dialog.CloseTrigger>
						</header>
						<p>A slide out drawer panel.</p>
					</Dialog.Content>
				</Dialog.Positioner>
			</Portal>
		</Dialog>
	);
}

```

## Z-Index

By default Skeleton does not take an opinionated stance regarding z-index stacking. The result is the component can sometimes be occluded beneath other elements with a higher index. The Z-Index can controlled by applying a utility class to the `Positioner` component.

```tsx
import { Dialog, Portal } from '@skeletonlabs/skeleton-react';

export default function ZIndex() {
	return (
		<Dialog>
			<Dialog.Trigger className="btn preset-filled">Trigger</Dialog.Trigger>
			<Portal>
				<Dialog.Backdrop className="fixed inset-0 z-50 bg-surface-50-950/50" />
				<Dialog.Positioner className="fixed inset-0 z-50 flex justify-center items-center">
					<Dialog.Content className="card bg-surface-100-900 w-md p-4 space-y-2 shadow-xl">
						<Dialog.Title className="text-2xl font-bold">Setting Z-Index</Dialog.Title>
						<Dialog.Description>This dialog will have a z-index value of 50.</Dialog.Description>
						<Dialog.CloseTrigger className="btn preset-tonal">Close</Dialog.CloseTrigger>
					</Dialog.Content>
				</Dialog.Positioner>
			</Portal>
		</Dialog>
	);
}

```

## Direction

Set the text direction (`ltr` or `rtl`) using the `dir` prop.

```tsx
import { Dialog, Portal } from '@skeletonlabs/skeleton-react';

export default function Dir() {
	return (
		<Dialog dir="rtl">
			<Dialog.Trigger className="btn preset-filled">Trigger</Dialog.Trigger>
			<Portal>
				<Dialog.Backdrop className="fixed inset-0 z-50 bg-surface-50-950/50" />
				<Dialog.Positioner className="fixed inset-0 z-50 flex justify-center items-center">
					<Dialog.Content className="card bg-surface-100-900 w-md p-4 space-y-2 shadow-xl">
						<Dialog.Title className="text-2xl font-bold">Hello World</Dialog.Title>
						<Dialog.Description>This is an example of a basic dialog.</Dialog.Description>
						<Dialog.CloseTrigger className="btn preset-tonal">Close</Dialog.CloseTrigger>
					</Dialog.Content>
				</Dialog.Positioner>
			</Portal>
		</Dialog>
	);
}

```

## Anatomy

Here's an overview of how the Dialog component is structured in code:

```tsx
import { Dialog, Portal } from '@skeletonlabs/skeleton-react';

export default function Anatomy() {
	return (
		<Dialog>
			<Dialog.Trigger />
			<Portal>
				<Dialog.Backdrop />
				<Dialog.Positioner>
					<Dialog.Content>
						<Dialog.Title />
						<Dialog.Description />
						<Dialog.CloseTrigger />
					</Dialog.Content>
				</Dialog.Positioner>
			</Portal>
		</Dialog>
	);
}
```

## API Reference

### Root

| Prop                   | Description                                                                                                                    | Type                                                                                                                                                          | Default  |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| children               | -                                                                                                                              | ReactNode                                                                                                                                                     | -        |
| ids                    | The ids of the elements in the dialog. Useful for composition.                                                                 | Partial\<\{ trigger: string; positioner: string; backdrop: string; content: string; closeTrigger: string; title: string; description: string; }> \| undefined | -        |
| trapFocus              | Whether to trap focus inside the dialog when it's opened                                                                       | boolean \| undefined                                                                                                                                          | true     |
| preventScroll          | Whether to prevent scrolling behind the dialog when it's opened                                                                | boolean \| undefined                                                                                                                                          | true     |
| modal                  | Whether to prevent pointer interaction outside the element and hide all content below it                                       | boolean \| undefined                                                                                                                                          | true     |
| initialFocusEl         | Element to receive focus when the dialog is opened                                                                             | (() => MaybeElement) \| undefined                                                                                                                             | -        |
| finalFocusEl           | Element to receive focus when the dialog is closed                                                                             | (() => MaybeElement) \| undefined                                                                                                                             | -        |
| restoreFocus           | Whether to restore focus to the element that had focus before the dialog was opened                                            | boolean \| undefined                                                                                                                                          | -        |
| closeOnInteractOutside | Whether to close the dialog when the outside is clicked                                                                        | boolean \| undefined                                                                                                                                          | true     |
| closeOnEscape          | Whether to close the dialog when the escape key is pressed                                                                     | boolean \| undefined                                                                                                                                          | true     |
| aria-label             | Human readable label for the dialog, in event the dialog title is not rendered                                                 | string \| undefined                                                                                                                                           | -        |
| role                   | The dialog's role                                                                                                              | "dialog" \| "alertdialog" \| undefined                                                                                                                        | "dialog" |
| open                   | The controlled open state of the dialog                                                                                        | boolean \| undefined                                                                                                                                          | -        |
| defaultOpen            | The initial open state of the dialog when rendered.&#xA;Use when you don't need to control the open state of the dialog.       | boolean \| undefined                                                                                                                                          | false    |
| onOpenChange           | Function to call when the dialog's open state changes                                                                          | ((details: OpenChangeDetails) => void) \| undefined                                                                                                           | -        |
| dir                    | The document's text/writing direction.                                                                                         | "ltr" \| "rtl" \| undefined                                                                                                                                   | "ltr"    |
| getRootNode            | A root node to correctly resolve document in custom environments. E.x.: Iframes, Electron.                                     | (() => Node \| ShadowRoot \| Document) \| undefined                                                                                                           | -        |
| onEscapeKeyDown        | Function called when the escape key is pressed                                                                                 | ((event: KeyboardEvent) => void) \| undefined                                                                                                                 | -        |
| onRequestDismiss       | Function called when this layer is closed due to a parent layer being closed                                                   | ((event: LayerDismissEvent) => void) \| undefined                                                                                                             | -        |
| onPointerDownOutside   | Function called when the pointer is pressed down outside the component                                                         | ((event: PointerDownOutsideEvent) => void) \| undefined                                                                                                       | -        |
| onFocusOutside         | Function called when the focus is moved outside the component                                                                  | ((event: FocusOutsideEvent) => void) \| undefined                                                                                                             | -        |
| onInteractOutside      | Function called when an interaction happens outside the component                                                              | ((event: InteractOutsideEvent) => void) \| undefined                                                                                                          | -        |
| persistentElements     | Returns the persistent elements that:&#xA;- should not have pointer-events disabled&#xA;- should not trigger the dismiss event | (() => Element \| null)\[] \| undefined                                                                                                                       | -        |

### Provider

| Prop     | Description | Type                  | Default |
| -------- | ----------- | --------------------- | ------- |
| value    | -           | DialogApi\<PropTypes> | -       |
| children | -           | ReactNode             | -       |

### Context

| Prop     | Description | Type                                         | Default |
| -------- | ----------- | -------------------------------------------- | ------- |
| children | -           | (dialog: DialogApi\<PropTypes>) => ReactNode | -       |

### Trigger

| Prop    | Description                 | Type                                                              | Default |
| ------- | --------------------------- | ----------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"button">) => Element) \| undefined | -       |

### Backdrop

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Positioner

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Content

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
