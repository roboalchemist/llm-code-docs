# Source: https://www.skeleton.dev/docs/svelte/framework-components/toast.md

# Source: https://www.skeleton.dev/docs/react/framework-components/toast.md

# Toast

Display brief messages to users.

```tsx
import { Toast, createToaster } from '@skeletonlabs/skeleton-react';

export default function Default() {
	const toaster = createToaster();

	return (
		<>
			<button
				className="btn preset-filled"
				onClick={() =>
					toaster.info({
						title: 'Title',
						description: 'This is a description.',
					})
				}
			>
				Toast
			</button>
			<Toast.Group toaster={toaster}>
				{(toast) => (
					<Toast toast={toast} key={toast.id}>
						<Toast.Message>
							<Toast.Title>{toast.title}</Toast.Title>
							<Toast.Description>{toast.description}</Toast.Description>
						</Toast.Message>
						<Toast.CloseTrigger />
					</Toast>
				)}
			</Toast.Group>
		</>
	);
}

```

## Usage

This component acts as a Singleton. Implement a single instance of `<Toast.Group>` in the root scope your application.

```tsx
import { toaster } from '/some/path/toaster.ts';
import { Toast } from '@skeletonlabs/skeleton-react';
import type { PropsWithChildren } from 'react';

export default function Layout(props: PropsWithChildren) {
	return (
		<>
			{props.children}
			<Toast.Group toaster={toaster}>
				{(toast) => (
					<Toast toast={toast} key={toast.id}>
						<Toast.Message>
						<Toast.Title>{toast.title}</Toast.Title>
						<Toast.Description>{toast.description}</Toast.Description>
						</Toast.Message>
						<Toast.CloseTrigger />
					</Toast>
				)}
			</Toast.Group>
		</>
	);
}
```

Create a shared reference to the `createToaster()` instance. We'll call it `toaster` here.

```ts
<script lang="ts">
	import { createToaster } from '@skeletonlabs/skeleton-react';

	export const toaster = createToaster();
</script>
```

Use this shared reference to trigger messages on demand throughout your application.

```tsx
import { toaster } from '/some/path/toaster.ts';

export default function Page() {
	function onClickHandler() {
		toaster.info({ title: 'Example', description: 'This is a toast message.' });
	}
	return ();
}
```

```tsx
import { toaster } from '/some/path/toaster.ts';

export default function Page() {
	function onClickHandler() {
		toaster.info({ title: 'Example', description: 'This is a toast message.' });
	}
	return ();
}
```

## Triggers

Shorthand methods are available for toast triggers, including: `info()`, `success()`, `warning()`, and `error()`.

```tsx
import { Toast, createToaster } from '@skeletonlabs/skeleton-react';

export default function Type() {
	const toaster = createToaster();

	return (
		<>
			<div className="grid grid-cols-2 gap-2">
				<button
					className="btn preset-filled"
					onClick={() =>
						toaster.info({
							title: 'Info',
							description: 'This is an info toast.',
						})
					}
				>
					Info
				</button>
				<button
					className="btn preset-filled-success-500"
					onClick={() =>
						toaster.success({
							title: 'Success',
							description: 'This is a success toast.',
						})
					}
				>
					Success
				</button>
				<button
					className="btn preset-filled-warning-500"
					onClick={() =>
						toaster.warning({
							title: 'Warning',
							description: 'This is a warning toast.',
						})
					}
				>
					Warning
				</button>
				<button
					className="btn preset-filled-error-500"
					onClick={() =>
						toaster.error({
							title: 'Error',
							description: 'This is an error toast.',
						})
					}
				>
					Error
				</button>
			</div>
			<Toast.Group toaster={toaster}>
				{(toast) => (
					<Toast toast={toast} key={toast.id}>
						<Toast.Message>
							<Toast.Title>{toast.title}</Toast.Title>
							<Toast.Description>{toast.description}</Toast.Description>
						</Toast.Message>
						<Toast.CloseTrigger />
					</Toast>
				)}
			</Toast.Group>
		</>
	);
}

```

Or use the generic `create()` method to trigger toasts of any type: `info|success|warning|error`.

```ts
toaster.create({
	type: 'info',
	title: 'This is a toast',
	description: 'This is a toast description.',
	duration: 4000, // Duration in milliseconds (default: 4000), use Infinity to prevent auto-close
	action: {
		label: 'Action',
		onClick: () => {
			// Handle action click
		},
	},
});
```

## Placement

Set the `placement` value in your `createToaster` instance to define the global screen position.

```tsx
import { Toast, createToaster } from '@skeletonlabs/skeleton-react';

export default function Placement() {
	const toaster = createToaster({
		placement: 'bottom-end',
	});

	return (
		<>
			<button
				className="btn preset-filled"
				onClick={() =>
					toaster.info({
						title: 'Title',
						description: 'This is a description.',
					})
				}
			>
				Toast
			</button>
			<Toast.Group toaster={toaster}>
				{(toast) => (
					<Toast toast={toast} key={toast.id}>
						<Toast.Message>
							<Toast.Title>{toast.title}</Toast.Title>
							<Toast.Description>{toast.description}</Toast.Description>
						</Toast.Message>
						<Toast.CloseTrigger />
					</Toast>
				)}
			</Toast.Group>
		</>
	);
}

```

## Overlap

Use the `overlap` option in your `createToaster` instance to enable overlapping toasts.

```tsx
import { Toast, createToaster } from '@skeletonlabs/skeleton-react';

export default function Default() {
	const toaster = createToaster({
		overlap: true,
	});

	return (
		<>
			<button
				className="btn preset-filled"
				onClick={() =>
					toaster.info({
						title: 'Title',
						description: 'This is a description.',
					})
				}
			>
				Toast
			</button>
			<Toast.Group toaster={toaster}>
				{(toast) => (
					<Toast toast={toast} key={toast.id}>
						<Toast.Message>
							<Toast.Title>{toast.title}</Toast.Title>
							<Toast.Description>{toast.description}</Toast.Description>
						</Toast.Message>
						<Toast.CloseTrigger />
					</Toast>
				)}
			</Toast.Group>
		</>
	);
}

```

> Note: Hovering over the toast group will expand all the toasts.

## Closable

Use the `closable` prop to toggle display of the close button.

```tsx
import { Toast, createToaster } from '@skeletonlabs/skeleton-react';

export default function Closable() {
	const toaster = createToaster();

	return (
		<>
			<button
				className="btn preset-filled"
				onClick={() =>
					toaster.info({
						title: 'Title',
						description: 'This is a description.',
						closable: false,
					})
				}
			>
				Toast
			</button>
			<Toast.Group toaster={toaster}>
				{(toast) => (
					<Toast toast={toast} key={toast.id}>
						<Toast.Message>
							<Toast.Title>{toast.title}</Toast.Title>
							<Toast.Description>{toast.description}</Toast.Description>
						</Toast.Message>
						{toast.closable && <Toast.CloseTrigger />}
					</Toast>
				)}
			</Toast.Group>
		</>
	);
}

```

## Action

Use the `action` key to add an interactive button to your toast. This is useful for actions like "Undo", "Retry", or other contextual operations.

```tsx
import { Toast, createToaster } from '@skeletonlabs/skeleton-react';

export default function Action() {
	const toaster = createToaster();

	return (
		<>
			<button
				className="btn preset-filled"
				onClick={() =>
					toaster.info({
						title: 'Toast',
						description: 'This is a toast message.',
						duration: Infinity,
						action: {
							label: 'Undo',
							onClick: () => {
								toaster.success({
									title: 'Task undone',
									description: 'The task has been undone.',
								});
							},
						},
					})
				}
			>
				Toast
			</button>

			<Toast.Group toaster={toaster}>
				{(toast) => (
					<Toast toast={toast} key={toast.id}>
						<Toast.Message>
							<Toast.Title>{toast.title}</Toast.Title>
							<Toast.Description>{toast.description}</Toast.Description>
						</Toast.Message>
						{toast.action && <Toast.ActionTrigger>{toast.action.label}</Toast.ActionTrigger>}
						<Toast.CloseTrigger />
					</Toast>
				)}
			</Toast.Group>
		</>
	);
}

```

## Meta

Use the `meta` key to pass arbitrary data along with the toast instance. This can be used to display an icon for example.

```tsx
import { Toast, createToaster } from '@skeletonlabs/skeleton-react';
import { SkullIcon } from 'lucide-react';

export default function Meta() {
	const toaster = createToaster();

	return (
		<>
			<button
				className="btn preset-filled"
				onClick={() =>
					toaster.info({
						title: 'Title',
						description: 'This is a description.',
						meta: {
							icon: <SkullIcon className="size-8" />,
						},
					})
				}
			>
				Toast
			</button>
			<Toast.Group toaster={toaster}>
				{(toast) => (
					<Toast toast={toast} key={toast.id}>
						{toast.meta!.icon}
						<Toast.Message>
							<Toast.Title className="flex gap-2 items-center">{toast.title}</Toast.Title>
							<Toast.Description>{toast.description}</Toast.Description>
						</Toast.Message>
						<Toast.CloseTrigger />
					</Toast>
				)}
			</Toast.Group>
		</>
	);
}

```

## Promise

Toasts support asynchronous updates using promises.

```tsx
import { Toast, createToaster } from '@skeletonlabs/skeleton-react';

export default function Promise_() {
	const toaster = createToaster();

	function generatePositiveNumber() {
		return new Promise<number>((resolve, reject) => {
			setTimeout(() => {
				const number = Math.random() - 0.5;
				if (number > 0) {
					resolve(number);
				} else {
					reject(number);
				}
			}, 2000);
		});
	}

	return (
		<>
			<button
				className="btn preset-filled"
				onClick={() =>
					toaster.promise(generatePositiveNumber(), {
						loading: {
							title: 'Loading...',
							description: 'Please wait while generating your number',
						},
						success: (number) => ({
							title: 'Success',
							description: `Your number is ${number.toFixed(2)}`,
						}),
						error: (number) => ({
							title: 'Error',
							description: `Your number is ${(number as number).toFixed(2)}`,
						}),
					})
				}
			>
				Toast
			</button>

			<Toast.Group toaster={toaster}>
				{(toast) => (
					<Toast toast={toast} key={toast.id}>
						<Toast.Message>
							<Toast.Title>{toast.title}</Toast.Title>
							<Toast.Description>{toast.description}</Toast.Description>
						</Toast.Message>
						<Toast.CloseTrigger />
					</Toast>
				)}
			</Toast.Group>
		</>
	);
}

```

## Anatomy

Here's an overview of how the Toast component is structured in code:

```tsx
import { Toast, createToaster } from '@skeletonlabs/skeleton-react';

export default function Anatomy() {
	return (
		<Toast.Group>
			<Toast>
				<Toast.Message>
					<Toast.Title />
					<Toast.Description />
				</Toast.Message>
				<Toast.CloseTrigger />
			</Toast>
		</Toast.Group>
	);
}
```

## API Reference

### Root

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| toast   | -                           | Omit\<ToastOptions\<any>, "id" \| "parent">                    | -       |
| index   | -                           | number \| undefined                                            | -       |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Context

| Prop     | Description | Type                                            | Default |
| -------- | ----------- | ----------------------------------------------- | ------- |
| children | -           | (toast: ToastApi\<PropTypes, any>) => ReactNode | -       |

### Group

| Prop     | Description                 | Type                                                           | Default |
| -------- | --------------------------- | -------------------------------------------------------------- | ------- |
| toaster  | -                           | ToastStore\<any>                                               | -       |
| children | -                           | ((toast: ToastProps\<any>) => Element \| null) \| undefined    | -       |
| element  | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Message

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

### ActionTrigger

| Prop    | Description                 | Type                                                              | Default |
| ------- | --------------------------- | ----------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"button">) => Element) \| undefined | -       |

### CloseTrigger

| Prop    | Description                 | Type                                                              | Default |
| ------- | --------------------------- | ----------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"button">) => Element) \| undefined | -       |
