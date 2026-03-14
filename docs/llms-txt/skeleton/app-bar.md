# Source: https://www.skeleton.dev/docs/svelte/framework-components/app-bar.md

# Source: https://www.skeleton.dev/docs/react/framework-components/app-bar.md

# App Bar

A header element for the top of your page layout.

```tsx
import { AppBar } from '@skeletonlabs/skeleton-react';
import { CalendarIcon } from 'lucide-react';
import { CircleUserIcon } from 'lucide-react';
import { MenuIcon } from 'lucide-react';
import { SearchIcon } from 'lucide-react';

export default function Default() {
	return (
		<AppBar>
			<AppBar.Toolbar className="grid-cols-[auto_1fr_auto]">
				<AppBar.Lead>
					<button type="button" className="btn-icon btn-icon-lg hover:preset-tonal">
						<MenuIcon />
					</button>
				</AppBar.Lead>
				<AppBar.Headline>
					<p className="text-2xl">Skeleton</p>
				</AppBar.Headline>
				<AppBar.Trail>
					<button type="button" className="btn-icon hover:preset-tonal">
						<SearchIcon className="size-6" />
					</button>
					<button type="button" className="btn-icon hover:preset-tonal">
						<CalendarIcon className="size-6" />
					</button>
					<button type="button" className="btn-icon hover:preset-tonal">
						<CircleUserIcon className="size-6" />
					</button>
				</AppBar.Trail>
			</AppBar.Toolbar>
		</AppBar>
	);
}

```

## Centered

Control the layout using a [grid-cols-\*](https://tailwindcss.com/docs/grid-column) utility class.

```tsx
import { AppBar } from '@skeletonlabs/skeleton-react';
import { CalendarIcon } from 'lucide-react';
import { CircleUserIcon } from 'lucide-react';
import { MenuIcon } from 'lucide-react';
import { SearchIcon } from 'lucide-react';

export default function Centered() {
	return (
		<AppBar>
			<AppBar.Toolbar className="grid-cols-[1fr_2fr_1fr]">
				<AppBar.Lead>
					<button type="button" className="btn-icon btn-icon-lg hover:preset-tonal">
						<MenuIcon />
					</button>
				</AppBar.Lead>
				<AppBar.Headline className="flex justify-center">
					<p>Headline</p>
				</AppBar.Headline>
				<AppBar.Trail className="justify-end">
					<button type="button" className="btn-icon hover:preset-tonal">
						<SearchIcon className="size-6" />
					</button>
					<button type="button" className="btn-icon hover:preset-tonal">
						<CalendarIcon className="size-6" />
					</button>
					<button type="button" className="btn-icon hover:preset-tonal">
						<CircleUserIcon className="size-6" />
					</button>
				</AppBar.Trail>
			</AppBar.Toolbar>
		</AppBar>
	);
}

```

## Extended

Move the `<AppBar.Headline>` to a new row within the root.

```tsx
import { AppBar } from '@skeletonlabs/skeleton-react';
import { CalendarIcon } from 'lucide-react';
import { CircleUserIcon } from 'lucide-react';
import { MenuIcon } from 'lucide-react';
import { SearchIcon } from 'lucide-react';

export default function Extended() {
	return (
		<AppBar>
			<AppBar.Toolbar className="grid-cols-[auto_auto]">
				<AppBar.Lead>
					<button type="button" className="btn-icon btn-icon-lg hover:preset-tonal">
						<MenuIcon />
					</button>
				</AppBar.Lead>
				<AppBar.Trail>
					<button type="button" className="btn-icon hover:preset-tonal">
						<SearchIcon className="size-6" />
					</button>
					<button type="button" className="btn-icon hover:preset-tonal">
						<CalendarIcon className="size-6" />
					</button>
					<button type="button" className="btn-icon hover:preset-tonal">
						<CircleUserIcon className="size-6" />
					</button>
				</AppBar.Trail>
			</AppBar.Toolbar>
			<AppBar.Headline>
				<h2 className="h2">Headline</h2>
			</AppBar.Headline>
		</AppBar>
	);
}

```

## Responsive

Modify the layout based on responsive breakpoints.

```tsx
import { AppBar } from '@skeletonlabs/skeleton-react';
import { CalendarIcon } from 'lucide-react';
import { CircleUserIcon } from 'lucide-react';
import { MenuIcon } from 'lucide-react';
import { SearchIcon } from 'lucide-react';

export default function Responsive() {
	return (
		<>
			<AppBar>
				{/* 1. Set dynamic layout columns */}
				<AppBar.Toolbar className="grid-cols-[auto_1fr_auto] md:grid-cols-[auto_auto]">
					<AppBar.Lead>
						<button type="button" className="btn-icon btn-icon-lg hover:preset-tonal">
							<MenuIcon />
						</button>
					</AppBar.Lead>

					{/* 2. Set Mobile display */}
					<AppBar.Headline className="md:hidden">
						<p className="text-2xl">Headline</p>
					</AppBar.Headline>

					<AppBar.Trail>
						<button type="button" className="btn-icon hover:preset-tonal">
							<SearchIcon className="size-6" />
						</button>
						<button type="button" className="btn-icon hover:preset-tonal">
							<CalendarIcon className="size-6" />
						</button>
						<button type="button" className="btn-icon hover:preset-tonal">
							<CircleUserIcon className="size-6" />
						</button>
					</AppBar.Trail>
				</AppBar.Toolbar>

				{/* 3 Set Desktop display */}
				<AppBar.Headline className="hidden md:block">
					<p className="text-2xl">Headline</p>
				</AppBar.Headline>
			</AppBar>
		</>
	);
}

```

## Anatomy

Here's an overview of how the AppBar component is structured in code:

```tsx
import { AppBar } from '@skeletonlabs/skeleton-react';

export default function Anatomy() {
	return (
		<AppBar>
			<AppBar.Toolbar>
				<AppBar.Lead />
				<AppBar.Headline />
				<AppBar.Trail />
			</AppBar.Toolbar>
		</AppBar>
	);
}
```

## API Reference

### Root

| Prop    | Description                 | Type                                                              | Default |
| ------- | --------------------------- | ----------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"header">) => Element) \| undefined | -       |

### Toolbar

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Lead

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"nav">) => Element) \| undefined | -       |

### Headline

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Trail

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"nav">) => Element) \| undefined | -       |
