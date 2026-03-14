# Source: https://www.skeleton.dev/docs/svelte/framework-components/pagination.md

# Source: https://www.skeleton.dev/docs/react/framework-components/pagination.md

# Pagination

Client and server-side pagination controls.

```tsx
import { users } from './data';
import { Pagination } from '@skeletonlabs/skeleton-react';
import { ArrowRightIcon, ArrowLeftIcon } from 'lucide-react';
import { useState } from 'react';

const PAGE_SIZE = 5;

export default function Default() {
	const [page, setPage] = useState(1);

	const start = (page - 1) * PAGE_SIZE;
	const end = start + PAGE_SIZE;
	const paginatedUsers = users.slice(start, end);

	return (
		<div className="grid gap-4 w-full place-items-center">
			<table className="table table-auto">
				<thead>
					<tr>
						<th>ID</th>
						<th>Name</th>
						<th>Email</th>
						<th>Country</th>
					</tr>
				</thead>
				<tbody>
					{paginatedUsers.map((user) => (
						<tr key={user.id}>
							<td>{user.id}</td>
							<td>{user.name}</td>
							<td>{user.email}</td>
							<td>{user.country}</td>
						</tr>
					))}
				</tbody>
			</table>
			<Pagination count={users.length} pageSize={PAGE_SIZE} page={page} onPageChange={(event) => setPage(event.page)}>
				<Pagination.PrevTrigger>
					<ArrowLeftIcon className="size-4" />
				</Pagination.PrevTrigger>
				<Pagination.Context>
					{(pagination) =>
						pagination.pages.map((page, index) =>
							page.type === 'page' ? (
								<Pagination.Item key={index} {...page}>
									{page.value}
								</Pagination.Item>
							) : (
								<Pagination.Ellipsis key={index} index={index}>
									&#8230;
								</Pagination.Ellipsis>
							),
						)
					}
				</Pagination.Context>
				<Pagination.NextTrigger>
					<ArrowRightIcon className="size-4" />
				</Pagination.NextTrigger>
			</Pagination>
		</div>
	);
}

```

```ts
import { faker } from '@faker-js/faker';

faker.seed(0);

export const users = Array.from({ length: 500 }, (_, i) => ({
	id: i + 1,
	name: faker.person.fullName(),
	email: faker.internet.email(),
	country: faker.location.country(),
}));

```

## Page Size

Implement a custom page `pageSize` amount using a select element.

```tsx
import { users } from './data';
import { Pagination } from '@skeletonlabs/skeleton-react';
import { ArrowRightIcon, ArrowLeftIcon } from 'lucide-react';
import { useState } from 'react';

export default function Default() {
	const [page, setPage] = useState(1);
	const [pageSize, setPageSize] = useState(5);

	const start = (page - 1) * pageSize;
	const end = start + pageSize;
	const paginatedUsers = users.slice(start, end);

	return (
		<div className="grid gap-4 w-full place-items-center">
			<table className="table table-auto">
				<thead>
					<tr>
						<th>ID</th>
						<th>Name</th>
						<th>Email</th>
						<th>Country</th>
					</tr>
				</thead>
				<tbody>
					{paginatedUsers.map((user) => (
						<tr key={user.id}>
							<td>{user.id}</td>
							<td>{user.name}</td>
							<td>{user.email}</td>
							<td>{user.country}</td>
						</tr>
					))}
				</tbody>
			</table>
			<div className="flex justify-between items-center gap-4 w-full">
				<label className="label">
					<span className="sr-only">Page Size</span>
					<select className="select w-fit" value={String(pageSize)} onChange={(e) => setPageSize(Number(e.currentTarget.value))}>
						<option value="5">5</option>
						<option value="10">10</option>
						<option value="20">20</option>
					</select>
				</label>

				<Pagination count={users.length} pageSize={pageSize} page={page} onPageChange={(event) => setPage(event.page)}>
					<Pagination.PrevTrigger>
						<ArrowLeftIcon className="size-4" />
					</Pagination.PrevTrigger>
					<Pagination.Context>
						{(pagination) =>
							pagination.pages.map((page, index) =>
								page.type === 'page' ? (
									<Pagination.Item key={index} {...page}>
										{page.value}
									</Pagination.Item>
								) : (
									<Pagination.Ellipsis key={index} index={index}>
										&#8230;
									</Pagination.Ellipsis>
								),
							)
						}
					</Pagination.Context>
					<Pagination.NextTrigger>
						<ArrowRightIcon className="size-4" />
					</Pagination.NextTrigger>
				</Pagination>
			</div>
		</div>
	);
}

```

```ts
import { faker } from '@faker-js/faker';

faker.seed(0);

export const users = Array.from({ length: 500 }, (_, i) => ({
	id: i + 1,
	name: faker.person.fullName(),
	email: faker.internet.email(),
	country: faker.location.country(),
}));

```

## Direction

Set the text direction (`ltr` or `rtl`) using the `dir` prop.

```tsx
import { users } from './data';
import { Pagination } from '@skeletonlabs/skeleton-react';
import { ArrowRightIcon, ArrowLeftIcon } from 'lucide-react';
import { useState } from 'react';

const PAGE_SIZE = 5;

export default function Dir() {
	const [page, setPage] = useState(1);

	const start = (page - 1) * PAGE_SIZE;
	const end = start + PAGE_SIZE;
	const paginatedUsers = users.slice(start, end);

	return (
		<div className="grid gap-4 w-full place-items-center">
			<table className="table table-auto">
				<thead>
					<tr>
						<th>ID</th>
						<th>Name</th>
						<th>Email</th>
						<th>Country</th>
					</tr>
				</thead>
				<tbody>
					{paginatedUsers.map((user) => (
						<tr key={user.id}>
							<td>{user.id}</td>
							<td>{user.name}</td>
							<td>{user.email}</td>
							<td>{user.country}</td>
						</tr>
					))}
				</tbody>
			</table>
			<Pagination count={users.length} pageSize={PAGE_SIZE} page={page} onPageChange={(event) => setPage(event.page)} dir="rtl">
				<Pagination.PrevTrigger>
					<ArrowRightIcon className="size-4" />
				</Pagination.PrevTrigger>
				<Pagination.Context>
					{(pagination) =>
						pagination.pages.map((page, index) =>
							page.type === 'page' ? (
								<Pagination.Item key={index} {...page}>
									{page.value}
								</Pagination.Item>
							) : (
								<Pagination.Ellipsis key={index} index={index}>
									&#8230;
								</Pagination.Ellipsis>
							),
						)
					}
				</Pagination.Context>
				<Pagination.NextTrigger>
					<ArrowLeftIcon className="size-4" />
				</Pagination.NextTrigger>
			</Pagination>
		</div>
	);
}

```

```ts
import { faker } from '@faker-js/faker';

faker.seed(0);

export const users = Array.from({ length: 500 }, (_, i) => ({
	id: i + 1,
	name: faker.person.fullName(),
	email: faker.internet.email(),
	country: faker.location.country(),
}));

```

## Total Count

For server-side pagination, your data source may be truncated. Make sure to specify the total records using `count`.

```ts
const res = {
	"results": [...],
	"pagination": {
		"page": 1,
		"limit": 10,
		"count": 500,
	}
}
```

{/* prettier-ignore */}

```html
<Pagination
	page={res.pagination.page}
	count={res.pagination.count}
	pageSize={res.pagination.limit}
>
	<!-- ... -->
</Pagination>
```

## Anatomy

Here's an overview of how the Pagination component is structured in code:

```tsx
import { Pagination } from '@skeletonlabs/skeleton-react';

export default function Anatomy() {
	return (
		<Pagination>
			<Pagination.FirstTrigger />
			<Pagination.PrevTrigger />
			<Pagination.Item />
			<Pagination.Ellipsis />
			<Pagination.NextTrigger />
			<Pagination.LastTrigger />
		</Pagination>
	);
}
```

## API Reference

### Root

| Prop             | Description                                                                                                                      | Type                                                                                                                                                                                                | Default  |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| ids              | The ids of the elements in the accordion. Useful for composition.                                                                | Partial\<\{ root: string; ellipsis: (index: number) => string; firstTrigger: string; prevTrigger: string; nextTrigger: string; lastTrigger: string; item: (page: number) => string; }> \| undefined | -        |
| translations     | Specifies the localized strings that identifies the accessibility elements and their states                                      | IntlTranslations \| undefined                                                                                                                                                                       | -        |
| count            | Total number of data items                                                                                                       | number \| undefined                                                                                                                                                                                 | -        |
| pageSize         | The controlled number of data items per page                                                                                     | number \| undefined                                                                                                                                                                                 | -        |
| defaultPageSize  | The initial number of data items per page when rendered.&#xA;Use when you don't need to control the page size of the pagination. | number \| undefined                                                                                                                                                                                 | 10       |
| siblingCount     | Number of pages to show beside active page                                                                                       | number \| undefined                                                                                                                                                                                 | 1        |
| boundaryCount    | Number of pages to show at the beginning and end                                                                                 | number \| undefined                                                                                                                                                                                 | 1        |
| page             | The controlled active page                                                                                                       | number \| undefined                                                                                                                                                                                 | -        |
| defaultPage      | The initial active page when rendered.&#xA;Use when you don't need to control the active page of the pagination.                 | number \| undefined                                                                                                                                                                                 | 1        |
| onPageChange     | Called when the page number is changed                                                                                           | ((details: PageChangeDetails) => void) \| undefined                                                                                                                                                 | -        |
| onPageSizeChange | Called when the page size is changed                                                                                             | ((details: PageSizeChangeDetails) => void) \| undefined                                                                                                                                             | -        |
| type             | The type of the trigger element                                                                                                  | "button" \| "link" \| undefined                                                                                                                                                                     | "button" |
| getPageUrl       | Function to generate href attributes for pagination links.&#xA;Only used when \`type\` is set to "link".                         | ((details: PageUrlDetails) => string) \| undefined                                                                                                                                                  | -        |
| dir              | The document's text/writing direction.                                                                                           | "ltr" \| "rtl" \| undefined                                                                                                                                                                         | "ltr"    |
| getRootNode      | A root node to correctly resolve document in custom environments. E.x.: Iframes, Electron.                                       | (() => ShadowRoot \| Node \| Document) \| undefined                                                                                                                                                 | -        |
| element          | Render the element yourself                                                                                                      | ((attributes: HTMLAttributes\<"nav">) => Element) \| undefined                                                                                                                                      | -        |

### Provider

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| value   | -                           | PaginationApi\<PropTypes>                                      | -       |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"nav">) => Element) \| undefined | -       |

### Context

| Prop     | Description | Type                                                 | Default |
| -------- | ----------- | ---------------------------------------------------- | ------- |
| children | -           | (pagination: PaginationApi\<PropTypes>) => ReactNode | -       |

### FirstTrigger

| Prop    | Description                 | Type                                                              | Default |
| ------- | --------------------------- | ----------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"button">) => Element) \| undefined | -       |

### PrevTrigger

| Prop    | Description                 | Type                                                              | Default |
| ------- | --------------------------- | ----------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"button">) => Element) \| undefined | -       |

### Item

| Prop    | Description                 | Type                                                         | Default |
| ------- | --------------------------- | ------------------------------------------------------------ | ------- |
| type    | -                           | "page"                                                       | -       |
| value   | -                           | number                                                       | -       |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"a">) => Element) \| undefined | -       |

### Ellipsis

| Prop    | Description                 | Type                                                            | Default |
| ------- | --------------------------- | --------------------------------------------------------------- | ------- |
| index   | -                           | number                                                          | -       |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"span">) => Element) \| undefined | -       |

### NextTrigger

| Prop    | Description                 | Type                                                              | Default |
| ------- | --------------------------- | ----------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"button">) => Element) \| undefined | -       |

### LastTrigger

| Prop    | Description                 | Type                                                              | Default |
| ------- | --------------------------- | ----------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"button">) => Element) \| undefined | -       |
