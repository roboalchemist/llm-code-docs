# Source: https://www.skeleton.dev/docs/svelte/framework-components/portal.md

# Source: https://www.skeleton.dev/docs/react/framework-components/portal.md

# Portal

Renders children into a DOM node that exists outside the DOM hierarchy.

```tsx
import { Portal } from '@skeletonlabs/skeleton-react';
import { SkullIcon } from 'lucide-react';
import { useState, useRef } from 'react';

export default function Default() {
	const [disabled, setDisabled] = useState(true);
	const ref = useRef<HTMLDivElement | null>(null);

	const cardClasses = 'card preset-outlined-surface-300-700 size-24 grid place-items-center p-4';
	const buttonClasses = 'col-span-2 btn preset-filled';

	return (
		<div className="grid grid-cols-2 gap-4">
			{/* Source */}
			<div className={cardClasses}>
				<Portal disabled={disabled} target={ref.current ?? undefined}>
					<SkullIcon className="size-8" />
				</Portal>
			</div>

			{/* Target */}
			<div className={cardClasses} ref={ref}>
				{/* (the content will appear here) */}
			</div>

			{/* Trigger */}
			<button className={buttonClasses} onClick={() => setDisabled(!disabled)}>
				{disabled ? 'Enable' : 'Disable'}
			</button>
		</div>
	);
}

```

## How It Works

When enabled, the content will move from the source to the target element.

## Anatomy

Here's an overview of how the Portal component is structured in code:

```tsx
import { Portal } from '@skeletonlabs/skeleton-react';

export default function Anatomy() {
	return <Portal>{/* Content */}</Portal>;
}
```

## API Reference

### Root

| Prop     | Description                                                                       | Type                                                                                                                                                                   | Default       |
| -------- | --------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| disabled | If true, the portal functionality is disabled and children are rendered in place. | boolean \| undefined                                                                                                                                                   | false         |
| target   | The HTML element to which the portal content will be appended.                    | HTMLElement \| undefined                                                                                                                                               | document.body |
| children | -                                                                                 | string \| number \| bigint \| boolean \| ReactElement\<unknown, string \| JSXElementConstructor\<any>> \| Iterable\<ReactNode> \| ReactPortal \| Promise\<...> \| null | -             |
