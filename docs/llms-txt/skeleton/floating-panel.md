# Source: https://www.skeleton.dev/docs/svelte/framework-components/floating-panel.md

# Source: https://www.skeleton.dev/docs/react/framework-components/floating-panel.md

# Floating Panel

A draggable, resizable floating panel with minimize/maximize controls.

```tsx
import { FloatingPanel, Portal } from '@skeletonlabs/skeleton-react';
import { GripVerticalIcon, MinimizeIcon, XIcon, MinusIcon, MaximizeIcon } from 'lucide-react';

export default function Default() {
	return (
		<FloatingPanel>
			<FloatingPanel.Trigger className="btn preset-filled">Open Panel</FloatingPanel.Trigger>
			<Portal>
				<FloatingPanel.Positioner className="z-50">
					<FloatingPanel.Content>
						<FloatingPanel.DragTrigger>
							<FloatingPanel.Header>
								<FloatingPanel.Title>
									<GripVerticalIcon className="size-4" />
									Floating Panel
								</FloatingPanel.Title>
								<FloatingPanel.Control>
									<FloatingPanel.StageTrigger stage="minimized">
										<MinusIcon className="size-4" />
									</FloatingPanel.StageTrigger>
									<FloatingPanel.StageTrigger stage="maximized">
										<MaximizeIcon className="size-4" />
									</FloatingPanel.StageTrigger>
									<FloatingPanel.StageTrigger stage="default">
										<MinimizeIcon className="size-4" />
									</FloatingPanel.StageTrigger>
									<FloatingPanel.CloseTrigger>
										<XIcon className="size-4" />
									</FloatingPanel.CloseTrigger>
								</FloatingPanel.Control>
							</FloatingPanel.Header>
						</FloatingPanel.DragTrigger>
						<FloatingPanel.Body>
							<p>
								This is a floating panel that can be dragged, resized, minimized, and maximized. Try dragging from the header or resizing
								from the bottom-right corner.
							</p>
						</FloatingPanel.Body>
						<FloatingPanel.ResizeTrigger axis="se" />
					</FloatingPanel.Content>
				</FloatingPanel.Positioner>
			</Portal>
		</FloatingPanel>
	);
}

```

## Size Constraints

Use the `minSize` and `maxSize` props to set size constraints on the Floating Panel.

```tsx
import { FloatingPanel, Portal } from '@skeletonlabs/skeleton-react';
import { GripVerticalIcon, MinimizeIcon, XIcon, MinusIcon, MaximizeIcon } from 'lucide-react';

export default function SizeConstraints() {
	return (
		<FloatingPanel maxSize={{ width: 900, height: 600 }} minSize={{ width: 300, height: 200 }}>
			<FloatingPanel.Trigger className="btn preset-filled">Open Panel</FloatingPanel.Trigger>
			<Portal>
				<FloatingPanel.Positioner className="z-50">
					<FloatingPanel.Content>
						<FloatingPanel.DragTrigger>
							<FloatingPanel.Header>
								<FloatingPanel.Title>
									<GripVerticalIcon className="size-4" />
									Floating Panel
								</FloatingPanel.Title>
								<FloatingPanel.Control>
									<FloatingPanel.StageTrigger stage="minimized">
										<MinusIcon className="size-4" />
									</FloatingPanel.StageTrigger>
									<FloatingPanel.StageTrigger stage="maximized">
										<MaximizeIcon className="size-4" />
									</FloatingPanel.StageTrigger>
									<FloatingPanel.StageTrigger stage="default">
										<MinimizeIcon className="size-4" />
									</FloatingPanel.StageTrigger>
									<FloatingPanel.CloseTrigger>
										<XIcon className="size-4" />
									</FloatingPanel.CloseTrigger>
								</FloatingPanel.Control>
							</FloatingPanel.Header>
						</FloatingPanel.DragTrigger>
						<FloatingPanel.Body>
							<p>This panel has size constraints applied: minimum 300x200 pixels and maximum 900x600 pixels.</p>
							<p>Try resizing from the bottom-right corner - the panel will respect these boundaries.</p>
						</FloatingPanel.Body>
						<FloatingPanel.ResizeTrigger axis="se" />
					</FloatingPanel.Content>
				</FloatingPanel.Positioner>
			</Portal>
		</FloatingPanel>
	);
}

```

## Controlled

Control the open state and size of the Floating Panel with your own state.

```tsx
import { FloatingPanel, Portal } from '@skeletonlabs/skeleton-react';
import { GripVerticalIcon, XIcon, MinusIcon, MaximizeIcon, MinimizeIcon } from 'lucide-react';
import { useState } from 'react';

export default function Controlled() {
	const [open, setOpen] = useState(false);
	const [size, setSize] = useState({
		width: 400,
		height: 300,
	});

	return (
		<>
			<div className="flex flex-col gap-4">
				<label className="label flex items-center gap-2">
					<input type="checkbox" className="checkbox" checked={open} onChange={(e) => setOpen(e.currentTarget.checked)} />
					<span className="label-text">Open Panel</span>
				</label>
				<label className="label">
					<span className="label-text">Width:</span>
					<input type="number" className="input" value={size.width} onChange={(e) => setSize({ ...size, width: Number(e.target.value) })} />
				</label>
				<label className="label">
					<span className="label-text">Height:</span>
					<input
						type="number"
						className="input"
						value={size.height}
						onChange={(e) => setSize({ ...size, height: Number(e.target.value) })}
					/>
				</label>
			</div>

			<FloatingPanel
				open={open}
				onOpenChange={(details) => setOpen(details.open)}
				size={size}
				onSizeChange={(details) => setSize(details.size)}
			>
				<Portal>
					<FloatingPanel.Positioner className="z-50">
						<FloatingPanel.Content>
							<FloatingPanel.DragTrigger>
								<FloatingPanel.Header>
									<FloatingPanel.Title>
										<GripVerticalIcon className="size-4" />
										Controlled Panel
									</FloatingPanel.Title>
									<FloatingPanel.Control>
										<FloatingPanel.StageTrigger stage="minimized">
											<MinusIcon className="size-4" />
										</FloatingPanel.StageTrigger>
										<FloatingPanel.StageTrigger stage="maximized">
											<MaximizeIcon className="size-4" />
										</FloatingPanel.StageTrigger>
										<FloatingPanel.StageTrigger stage="default">
											<MinimizeIcon className="size-4" />
										</FloatingPanel.StageTrigger>
										<FloatingPanel.CloseTrigger>
											<XIcon className="size-4" />
										</FloatingPanel.CloseTrigger>
									</FloatingPanel.Control>
								</FloatingPanel.Header>
							</FloatingPanel.DragTrigger>
							<FloatingPanel.Body>
								<p>This panel's open state and size are controlled via the inputs above.</p>
								<p>Try changing the values or resizing/closing the panel to see the inputs update.</p>
							</FloatingPanel.Body>
							<FloatingPanel.ResizeTrigger axis="se" />
						</FloatingPanel.Content>
					</FloatingPanel.Positioner>
				</Portal>
			</FloatingPanel>
		</>
	);
}

```

## Anchor Position

Position the panel relative to another element using the `defaultPosition` prop.

```tsx
import { FloatingPanel, Portal } from '@skeletonlabs/skeleton-react';
import { GripVerticalIcon, XIcon, MinusIcon, MaximizeIcon, MinimizeIcon } from 'lucide-react';

export default function AnchorPosition() {
	return (
		<div className="space-y-4">
			<FloatingPanel
				getAnchorPosition={(ctx) => {
					if (!ctx.triggerRect) return { x: 0, y: 0 };
					return {
						x: ctx.triggerRect.x + ctx.triggerRect.width / 2,
						y: ctx.triggerRect.y + ctx.triggerRect.height / 2,
					};
				}}
			>
				<FloatingPanel.Trigger className="btn preset-filled">Open Panel</FloatingPanel.Trigger>
				<Portal>
					<FloatingPanel.Positioner className="z-50">
						<FloatingPanel.Content>
							<FloatingPanel.DragTrigger>
								<FloatingPanel.Header>
									<FloatingPanel.Title>
										<GripVerticalIcon className="size-4" />
										Anchored Panel
									</FloatingPanel.Title>
									<FloatingPanel.Control>
										<FloatingPanel.StageTrigger stage="minimized">
											<MinusIcon className="size-4" />
										</FloatingPanel.StageTrigger>
										<FloatingPanel.StageTrigger stage="maximized">
											<MaximizeIcon className="size-4" />
										</FloatingPanel.StageTrigger>
										<FloatingPanel.StageTrigger stage="default">
											<MinimizeIcon className="size-4" />
										</FloatingPanel.StageTrigger>
										<FloatingPanel.CloseTrigger>
											<XIcon className="size-4" />
										</FloatingPanel.CloseTrigger>
									</FloatingPanel.Control>
								</FloatingPanel.Header>
							</FloatingPanel.DragTrigger>
							<FloatingPanel.Body>
								<p>This panel is centered in the viewport using getAnchorPosition.</p>
								<p>The position is calculated based on the boundary rectangle.</p>
							</FloatingPanel.Body>
							<FloatingPanel.ResizeTrigger axis="se" />
						</FloatingPanel.Content>
					</FloatingPanel.Positioner>
				</Portal>
			</FloatingPanel>
		</div>
	);
}

```

## Resize Triggers

Add resize triggers on all sides and corners of the Floating Panel using the `axis` prop.

```tsx
import { FloatingPanel, Portal } from '@skeletonlabs/skeleton-react';
import { GripVerticalIcon, MinimizeIcon, XIcon, MinusIcon, MaximizeIcon } from 'lucide-react';

export default function Default() {
	return (
		<FloatingPanel>
			<FloatingPanel.Trigger className="btn preset-filled">Open Panel</FloatingPanel.Trigger>
			<Portal>
				<FloatingPanel.Positioner className="z-50">
					<FloatingPanel.Content>
						<FloatingPanel.DragTrigger>
							<FloatingPanel.Header>
								<FloatingPanel.Title>
									<GripVerticalIcon className="size-4" />
									Floating Panel
								</FloatingPanel.Title>
								<FloatingPanel.Control>
									<FloatingPanel.StageTrigger stage="minimized">
										<MinusIcon className="size-4" />
									</FloatingPanel.StageTrigger>
									<FloatingPanel.StageTrigger stage="maximized">
										<MaximizeIcon className="size-4" />
									</FloatingPanel.StageTrigger>
									<FloatingPanel.StageTrigger stage="default">
										<MinimizeIcon className="size-4" />
									</FloatingPanel.StageTrigger>
									<FloatingPanel.CloseTrigger>
										<XIcon className="size-4" />
									</FloatingPanel.CloseTrigger>
								</FloatingPanel.Control>
							</FloatingPanel.Header>
						</FloatingPanel.DragTrigger>
						<FloatingPanel.Body>
							<p>
								This is a floating panel that can be dragged, resized, minimized, and maximized. Try dragging from the header or resizing
								from the bottom-right corner.
							</p>
						</FloatingPanel.Body>
						<FloatingPanel.ResizeTrigger className="bg-primary-500/50" axis="n" />
						<FloatingPanel.ResizeTrigger className="bg-primary-500/50" axis="e" />
						<FloatingPanel.ResizeTrigger className="bg-primary-500/50" axis="w" />
						<FloatingPanel.ResizeTrigger className="bg-primary-500/50" axis="s" />
						<FloatingPanel.ResizeTrigger className="bg-primary-500/50" axis="ne" />
						<FloatingPanel.ResizeTrigger className="bg-primary-500/50" axis="se" />
						<FloatingPanel.ResizeTrigger className="bg-primary-500/50" axis="sw" />
						<FloatingPanel.ResizeTrigger className="bg-primary-500/50" axis="nw" />
					</FloatingPanel.Content>
				</FloatingPanel.Positioner>
			</Portal>
		</FloatingPanel>
	);
}

```

## Disable Dragging

Disable dragging by setting the `draggable` prop to `false`. The panel will remain in a fixed position but can still be resized.

```tsx
import { FloatingPanel, Portal } from '@skeletonlabs/skeleton-react';
import { GripVerticalIcon, XIcon, MinusIcon, MaximizeIcon, MinimizeIcon } from 'lucide-react';

export default function DisableDragging() {
	return (
		<FloatingPanel draggable={false}>
			<FloatingPanel.Trigger className="btn preset-filled">Open Panel</FloatingPanel.Trigger>
			<Portal>
				<FloatingPanel.Positioner className="z-50">
					<FloatingPanel.Content>
						<FloatingPanel.DragTrigger>
							<FloatingPanel.Header>
								<FloatingPanel.Title>
									<GripVerticalIcon className="size-4" />
									Fixed Position Panel
								</FloatingPanel.Title>
								<FloatingPanel.Control>
									<FloatingPanel.StageTrigger stage="minimized">
										<MinusIcon className="size-4" />
									</FloatingPanel.StageTrigger>
									<FloatingPanel.StageTrigger stage="maximized">
										<MaximizeIcon className="size-4" />
									</FloatingPanel.StageTrigger>
									<FloatingPanel.StageTrigger stage="default">
										<MinimizeIcon className="size-4" />
									</FloatingPanel.StageTrigger>
									<FloatingPanel.CloseTrigger>
										<XIcon className="size-4" />
									</FloatingPanel.CloseTrigger>
								</FloatingPanel.Control>
							</FloatingPanel.Header>
						</FloatingPanel.DragTrigger>
						<FloatingPanel.Body>
							<p>This panel cannot be dragged - the position is fixed.</p>
							<p>However, it can still be resized from the bottom-right corner.</p>
						</FloatingPanel.Body>
						<FloatingPanel.ResizeTrigger axis="se" />
					</FloatingPanel.Content>
				</FloatingPanel.Positioner>
			</Portal>
		</FloatingPanel>
	);
}

```

## Disable Resizing

Disable resizing by setting the `resizable` prop to `false`. The panel will have a fixed size but can still be dragged.

```tsx
import { FloatingPanel, Portal } from '@skeletonlabs/skeleton-react';
import { GripVerticalIcon, XIcon, MinusIcon, MaximizeIcon, MinimizeIcon } from 'lucide-react';

export default function DisableResizing() {
	return (
		<FloatingPanel resizable={false}>
			<FloatingPanel.Trigger className="btn preset-filled">Open Panel</FloatingPanel.Trigger>
			<Portal>
				<FloatingPanel.Positioner className="z-50">
					<FloatingPanel.Content>
						<FloatingPanel.DragTrigger>
							<FloatingPanel.Header>
								<FloatingPanel.Title>
									<GripVerticalIcon className="size-4" />
									Fixed Size Panel
								</FloatingPanel.Title>
								<FloatingPanel.Control>
									<FloatingPanel.StageTrigger stage="minimized">
										<MinusIcon className="size-4" />
									</FloatingPanel.StageTrigger>
									<FloatingPanel.StageTrigger stage="maximized">
										<MaximizeIcon className="size-4" />
									</FloatingPanel.StageTrigger>
									<FloatingPanel.StageTrigger stage="default">
										<MinimizeIcon className="size-4" />
									</FloatingPanel.StageTrigger>
									<FloatingPanel.CloseTrigger>
										<XIcon className="size-4" />
									</FloatingPanel.CloseTrigger>
								</FloatingPanel.Control>
							</FloatingPanel.Header>
						</FloatingPanel.DragTrigger>
						<FloatingPanel.Body>
							<p>This panel cannot be resized.</p>
							<p>Try dragging the edges - they won't respond.</p>
						</FloatingPanel.Body>
						<FloatingPanel.ResizeTrigger axis="se" />
					</FloatingPanel.Content>
				</FloatingPanel.Positioner>
			</Portal>
		</FloatingPanel>
	);
}

```

## Direction

Set the text direction (`ltr` or `rtl`) using the `dir` prop.

```tsx
import { FloatingPanel, Portal } from '@skeletonlabs/skeleton-react';
import { GripVerticalIcon, XIcon, MinusIcon, MaximizeIcon, MinimizeIcon } from 'lucide-react';

export default function Dir() {
	return (
		<FloatingPanel dir="rtl">
			<FloatingPanel.Trigger className="btn preset-filled">Open Panel</FloatingPanel.Trigger>
			<Portal>
				<FloatingPanel.Positioner className="z-50">
					<FloatingPanel.Content>
						<FloatingPanel.DragTrigger>
							<FloatingPanel.Header>
								<FloatingPanel.Title>
									<GripVerticalIcon className="size-4" />
									Floating Panel
								</FloatingPanel.Title>
								<FloatingPanel.Control>
									<FloatingPanel.StageTrigger stage="minimized">
										<MinusIcon className="size-4" />
									</FloatingPanel.StageTrigger>
									<FloatingPanel.StageTrigger stage="maximized">
										<MaximizeIcon className="size-4" />
									</FloatingPanel.StageTrigger>
									<FloatingPanel.StageTrigger stage="default">
										<MinimizeIcon className="size-4" />
									</FloatingPanel.StageTrigger>
									<FloatingPanel.CloseTrigger>
										<XIcon className="size-4" />
									</FloatingPanel.CloseTrigger>
								</FloatingPanel.Control>
							</FloatingPanel.Header>
						</FloatingPanel.DragTrigger>
						<FloatingPanel.Body>
							<p>This is a floating panel with right-to-left (RTL) direction.</p>
							<p>You can drag it from the header or resize it from the bottom-right corner.</p>
						</FloatingPanel.Body>
						<FloatingPanel.ResizeTrigger axis="se" />
					</FloatingPanel.Content>
				</FloatingPanel.Positioner>
			</Portal>
		</FloatingPanel>
	);
}

```

## Anatomy

Here's an overview of how the Floating Panel component is structured in code:

```tsx
import { FloatingPanel, Portal } from '@skeletonlabs/skeleton-react';

export default function Anatomy() {
	return (
		<FloatingPanel>
			<FloatingPanel.Trigger />
			<Portal>
				<FloatingPanel.Positioner>
					<FloatingPanel.Content>
						<FloatingPanel.DragTrigger>
							<FloatingPanel.Header>
								<FloatingPanel.Title />
								<FloatingPanel.Control>
									<FloatingPanel.StageTrigger />
									<FloatingPanel.CloseTrigger />
								</FloatingPanel.Control>
							</FloatingPanel.Header>
						</FloatingPanel.DragTrigger>
						<FloatingPanel.Body />
						<FloatingPanel.ResizeTrigger />
					</FloatingPanel.Content>
				</FloatingPanel.Positioner>
			</Portal>
		</FloatingPanel>
	);
}
```

## API Reference

### Root

| Prop                | Description                                                                                                                               | Type                                                                                                             | Default |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ------- |
| children            | -                                                                                                                                         | ReactNode                                                                                                        | -       |
| ids                 | The ids of the elements in the floating panel. Useful for composition.                                                                    | Partial\<\{ trigger: string; positioner: string; content: string; title: string; header: string; }> \| undefined | -       |
| translations        | The translations for the floating panel.                                                                                                  | IntlTranslations \| undefined                                                                                    | -       |
| strategy            | The strategy to use for positioning                                                                                                       | "absolute" \| "fixed" \| undefined                                                                               | "fixed" |
| allowOverflow       | Whether the panel should be strictly contained within the boundary when dragging                                                          | boolean \| undefined                                                                                             | true    |
| open                | The controlled open state of the panel                                                                                                    | boolean \| undefined                                                                                             | -       |
| defaultOpen         | The initial open state of the panel when rendered.&#xA;Use when you don't need to control the open state of the panel.                    | boolean \| undefined                                                                                             | false   |
| draggable           | Whether the panel is draggable                                                                                                            | boolean \| undefined                                                                                             | true    |
| resizable           | Whether the panel is resizable                                                                                                            | boolean \| undefined                                                                                             | true    |
| size                | The size of the panel                                                                                                                     | Size \| undefined                                                                                                | -       |
| defaultSize         | The default size of the panel                                                                                                             | Size \| undefined                                                                                                | -       |
| minSize             | The minimum size of the panel                                                                                                             | Size \| undefined                                                                                                | -       |
| maxSize             | The maximum size of the panel                                                                                                             | Size \| undefined                                                                                                | -       |
| position            | The controlled position of the panel                                                                                                      | Point \| undefined                                                                                               | -       |
| defaultPosition     | The initial position of the panel when rendered.&#xA;Use when you don't need to control the position of the panel.                        | Point \| undefined                                                                                               | -       |
| getAnchorPosition   | Function that returns the initial position of the panel when it is opened.&#xA;If provided, will be used instead of the default position. | ((details: AnchorPositionDetails) => Point) \| undefined                                                         | -       |
| lockAspectRatio     | Whether the panel is locked to its aspect ratio                                                                                           | boolean \| undefined                                                                                             | -       |
| closeOnEscape       | Whether the panel should close when the escape key is pressed                                                                             | boolean \| undefined                                                                                             | -       |
| getBoundaryEl       | The boundary of the panel. Useful for recalculating the boundary rect when&#xA;the it is resized.                                         | (() => HTMLElement \| null) \| undefined                                                                         | -       |
| disabled            | Whether the panel is disabled                                                                                                             | boolean \| undefined                                                                                             | -       |
| onPositionChange    | Function called when the position of the panel changes via dragging                                                                       | ((details: PositionChangeDetails) => void) \| undefined                                                          | -       |
| onPositionChangeEnd | Function called when the position of the panel changes via dragging ends                                                                  | ((details: PositionChangeDetails) => void) \| undefined                                                          | -       |
| onOpenChange        | Function called when the panel is opened or closed                                                                                        | ((details: OpenChangeDetails) => void) \| undefined                                                              | -       |
| onSizeChange        | Function called when the size of the panel changes via resizing                                                                           | ((details: SizeChangeDetails) => void) \| undefined                                                              | -       |
| onSizeChangeEnd     | Function called when the size of the panel changes via resizing ends                                                                      | ((details: SizeChangeDetails) => void) \| undefined                                                              | -       |
| persistRect         | Whether the panel size and position should be preserved when it is closed                                                                 | boolean \| undefined                                                                                             | -       |
| gridSize            | The snap grid for the panel                                                                                                               | number \| undefined                                                                                              | 1       |
| onStageChange       | Function called when the stage of the panel changes                                                                                       | ((details: StageChangeDetails) => void) \| undefined                                                             | -       |
| dir                 | The document's text/writing direction.                                                                                                    | "ltr" \| "rtl" \| undefined                                                                                      | "ltr"   |
| getRootNode         | A root node to correctly resolve document in custom environments. E.x.: Iframes, Electron.                                                | (() => Node \| ShadowRoot \| Document) \| undefined                                                              | -       |

### Provider

| Prop     | Description | Type                         | Default |
| -------- | ----------- | ---------------------------- | ------- |
| value    | -           | FloatingPanelApi\<PropTypes> | -       |
| children | -           | ReactNode                    | -       |

### Context

| Prop     | Description | Type                                                       | Default |
| -------- | ----------- | ---------------------------------------------------------- | ------- |
| children | -           | (floatingPanel: FloatingPanelApi\<PropTypes>) => ReactNode | -       |

### Trigger

| Prop    | Description                 | Type                                                              | Default |
| ------- | --------------------------- | ----------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"button">) => Element) \| undefined | -       |

### Positioner

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Content

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### DragTrigger

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Header

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Title

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Control

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### StageTrigger

| Prop    | Description                 | Type                                                              | Default |
| ------- | --------------------------- | ----------------------------------------------------------------- | ------- |
| stage   | The stage of the panel      | Stage                                                             | -       |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"button">) => Element) \| undefined | -       |

### CloseTrigger

| Prop    | Description                 | Type                                                              | Default |
| ------- | --------------------------- | ----------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"button">) => Element) \| undefined | -       |

### Body

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### ResizeTrigger

| Prop    | Description                   | Type                                                           | Default |
| ------- | ----------------------------- | -------------------------------------------------------------- | ------- |
| axis    | The axis of the resize handle | ResizeTriggerAxis                                              | -       |
| element | Render the element yourself   | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |
