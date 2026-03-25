# Source: https://radix-ui.com/primitives

Title: Radix Primitives

URL Source: https://radix-ui.com/primitives

Published Time: Mon, 09 Mar 2026 15:34:17 GMT

Markdown Content:
Core building blocks for your design system
-------------------------------------------

Unstyled, accessible, open source React primitives for high-quality web apps and design systems.

[Get started](https://www.radix-ui.com/primitives/docs)

Case in point

So, you think you can build a dropdown?
---------------------------------------

We agonise over API design, performance, and accessibility so you don't need to.

![Image 1: A dropdown menu example with a checked item and a submenu](https://www.radix-ui.com/marketing/dropdown-menu.svg)

Supports assistive technology

Accessibility out of the box
----------------------------

Screen reader

Show Minimap,

ticked, menu item

Radix component

Navigation

Show Minimap

Go to Symbol

Go to Definition

Go to References

### WAI-ARIA compliant

Radix Primitives follow the WAI-ARIA guidelines, implementing correct semantics and behaviors for our components.

### Keyboard navigation

Primitives provide full keyboard support for components where users expect to use a keyboard or other input devices.

### Focus management

Out of the box, Primitives provide sensible focus management defaults, which can be further customized in your code.

### Screen reader tested

We test Primitives with common assistive technologies, looking out for practical issues that people may experience.

Developer experience to love

Develop with an open, thought‑out API
-------------------------------------

One of our main goals is to provide the best possible developer experience. Radix Primitives provides a fully-typed API. All components share a similar API, creating a consistent and predictable experience.

MyComponent.jsx

```
// Add styles with your preferred CSS technology
const TooltipContent = styled(Tooltip.Content, {
backgroundColor: "black",
borderRadius: "3px",
padding: "5px"
});
const PopoverContent = styled(Popover.Content, {
backgroundColor: "white",
boxShadow: "0 2px 10px -3px rgb(0 0 0 / 20%)",
borderRadius: "3px",
});
const DialogContent = styled(Dialog.Content, {
backgroundColor: "white",
boxShadow: "0 3px 15px -4px rgb(0 0 0 / 30%)",
borderRadius: "5px",
});	
// Compose a custom Tooltip component
export const StatusTooltip = ({ state, label }) => {
return (
<Tooltip.Root>
			<Tooltip.Trigger asChild>
				<Text>
					<Status variant={state} />
				</Text>
			</Tooltip.Trigger>
			<Tooltip.Portal>
				<TooltipContent>
					<Tooltip.Arrow />
					{label}
				</TooltipContent>
			</Tooltip.Portal>
		</Tooltip.Root>
);
};	// Compose a Popover with custom focus and positioning
export const StatusPopover = ({ children }) => {
const popoverCloseButton = React.useRef(null);
return (
<Popover.Root>
			<Popover.Trigger>View status</Popover.Trigger>
			<Popover.Portal>
				<PopoverContent
					align="start"
					collisionPadding={10}
					onOpenAutoFocus={(event) => {
						// Focus the close button when popover opens
						popoverCloseButton.current?.focus();
						event.preventDefault();
					}}
				>
					{children}
					<Popover.Close ref={popoverCloseButton}>
						Close
					</Popover.Close>
				</PopoverContent>
			</Popover.Portal>
		</Popover.Root>
);
};	// Compose a Dialog with custom focus management
export const InfoDialog = ({ children }) => {
const dialogCloseButton = React.useRef(null);
return (
<Dialog.Root>
			<Dialog.Trigger>View details</Dialog.Trigger>
			<Dialog.Overlay />
			<Dialog.Portal>
				<DialogContent
					onOpenAutoFocus={(event) => {
						// Focus the close button when dialog opens
						dialogCloseButton.current?.focus();
						event.preventDefault();
					}}
				>
					{children}
					<Dialog.Close ref={dialogCloseButton}>
						Close
					</Dialog.Close>
				</DialogContent>
			</Dialog.Portal>
		</Dialog.Root>
);
};
```

Transition to Radix Primitives

Adoption made easy
------------------

[Go to docs](https://www.radix-ui.com/primitives/docs)

### Incremental adoption

Each component is its own independently versioned package, so new components can be added alongside your existing code. No need to disrupt feature work with a huge rewrite⁠—you can start small and add more components one by one.

### Detailed docs and TypeScript support

Radix documentation contains real-world examples, extensive API references, accessibility details, and full TypeScript support. All components share a similar API, creating a consistent developer experience. You will love working with Radix Primitives.

An active and friendly community

👋

Join our fast-growing community
-------------------------------
