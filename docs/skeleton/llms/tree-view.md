# Source: https://www.skeleton.dev/docs/svelte/framework-components/tree-view.md

# Source: https://www.skeleton.dev/docs/react/framework-components/tree-view.md

# Tree View

Used to display hierarchical data.

```tsx
import { TreeView, createTreeViewCollection } from '@skeletonlabs/skeleton-react';
import { FileIcon, FolderIcon } from 'lucide-react';

interface Node {
	id: string;
	name: string;
	children?: Node[];
}

function TreeNode(props: { node: Node; indexPath: number[] }) {
	return (
		<TreeView.NodeProvider value={props}>
			{props.node.children ? (
				<TreeView.Branch>
					<TreeView.BranchControl>
						<TreeView.BranchIndicator />
						<TreeView.BranchText>
							<FolderIcon className="size-4" />
							{props.node.name}
						</TreeView.BranchText>
					</TreeView.BranchControl>
					<TreeView.BranchContent>
						<TreeView.BranchIndentGuide />
						{props.node.children.map((childNode, childIndex) => (
							<TreeNode key={childNode.id} node={childNode} indexPath={[...props.indexPath, childIndex]} />
						))}
					</TreeView.BranchContent>
				</TreeView.Branch>
			) : (
				<TreeView.Item>
					<FileIcon className="size-4" />
					{props.node.name}
				</TreeView.Item>
			)}
		</TreeView.NodeProvider>
	);
}

export default function Default() {
	const collection = createTreeViewCollection<Node>({
		nodeToValue: (node) => node.id,
		nodeToString: (node) => node.name,
		rootNode: {
			id: 'root',
			name: '',
			children: [
				{
					id: 'node_modules',
					name: 'node_modules',
					children: [
						{
							id: 'node_modules/@skeletonlabs',
							name: '@skeletonlabs',
							children: [
								{
									id: 'node_modules/@skeletonlabs/skeleton',
									name: 'skeleton',
								},
							],
						},
					],
				},
				{
					id: 'package.json',
					name: 'package.json',
				},
			],
		},
	});
	return (
		<TreeView collection={collection}>
			<TreeView.Label>File System</TreeView.Label>
			<TreeView.Tree>
				{collection.rootNode.children?.map((node, index) => (
					<TreeNode node={node} indexPath={[index]} key={node.id} />
				))}
			</TreeView.Tree>
		</TreeView>
	);
}

```

## Controlled

Reactively set and control the state values.

```tsx
import { TreeView, createTreeViewCollection } from '@skeletonlabs/skeleton-react';
import { FileIcon, FolderIcon } from 'lucide-react';

interface Node {
	id: string;
	name: string;
	children?: Node[];
}

function TreeNode(props: { node: Node; indexPath: number[] }) {
	return (
		<TreeView.NodeProvider value={props}>
			{props.node.children ? (
				<TreeView.Branch>
					<TreeView.BranchControl>
						<TreeView.BranchIndicator />
						<TreeView.BranchText>
							<FolderIcon className="size-4" />
							{props.node.name}
						</TreeView.BranchText>
					</TreeView.BranchControl>
					<TreeView.BranchContent>
						<TreeView.BranchIndentGuide />
						{props.node.children.map((childNode, childIndex) => (
							<TreeNode key={childNode.id} node={childNode} indexPath={[...props.indexPath, childIndex]} />
						))}
					</TreeView.BranchContent>
				</TreeView.Branch>
			) : (
				<TreeView.Item>
					<FileIcon className="size-4" />
					{props.node.name}
				</TreeView.Item>
			)}
		</TreeView.NodeProvider>
	);
}

export default function Default() {
	const collection = createTreeViewCollection<Node>({
		nodeToValue: (node) => node.id,
		nodeToString: (node) => node.name,
		rootNode: {
			id: 'root',
			name: '',
			children: [
				{
					id: 'node_modules',
					name: 'node_modules',
					children: [
						{
							id: 'node_modules/@skeletonlabs',
							name: '@skeletonlabs',
							children: [
								{
									id: 'node_modules/@skeletonlabs/skeleton',
									name: 'skeleton',
								},
							],
						},
					],
				},
				{
					id: 'package.json',
					name: 'package.json',
				},
			],
		},
	});
	return (
		<TreeView collection={collection}>
			<TreeView.Label>File System</TreeView.Label>
			<TreeView.Tree>
				{collection.rootNode.children?.map((node, index) => (
					<TreeNode node={node} indexPath={[index]} key={node.id} />
				))}
			</TreeView.Tree>
		</TreeView>
	);
}

```

## Multiple Selection

* Windows: Hold <kbd class="kbd">Ctrl</kbd> + left click with mouse.
* MacOS: Hold <kbd class="kbd">⌘</kbd> + left click with mouse.

```tsx
import { TreeView, createTreeViewCollection } from '@skeletonlabs/skeleton-react';
import { FileIcon, FolderIcon } from 'lucide-react';

interface Node {
	id: string;
	name: string;
	children?: Node[];
}

function TreeNode(props: { node: Node; indexPath: number[] }) {
	return (
		<TreeView.NodeProvider value={props}>
			{props.node.children ? (
				<TreeView.Branch>
					<TreeView.BranchControl>
						<TreeView.BranchIndicator />
						<TreeView.BranchText>
							<FolderIcon className="size-4" />
							{props.node.name}
						</TreeView.BranchText>
					</TreeView.BranchControl>
					<TreeView.BranchContent>
						<TreeView.BranchIndentGuide />
						{props.node.children.map((childNode, childIndex) => (
							<TreeNode key={childNode.id} node={childNode} indexPath={[...props.indexPath, childIndex]} />
						))}
					</TreeView.BranchContent>
				</TreeView.Branch>
			) : (
				<TreeView.Item>
					<FileIcon className="size-4" />
					{props.node.name}
				</TreeView.Item>
			)}
		</TreeView.NodeProvider>
	);
}

export default function MultipleSelection() {
	const collection = createTreeViewCollection<Node>({
		nodeToValue: (node) => node.id,
		nodeToString: (node) => node.name,
		rootNode: {
			id: 'root',
			name: '',
			children: [
				{
					id: 'node_modules',
					name: 'node_modules',
					children: [
						{
							id: 'node_modules/@skeletonlabs',
							name: '@skeletonlabs',
							children: [
								{
									id: 'node_modules/@skeletonlabs/skeleton',
									name: 'skeleton',
								},
							],
						},
					],
				},
				{
					id: 'package.json',
					name: 'package.json',
				},
			],
		},
	});
	return (
		<TreeView collection={collection} selectionMode="multiple">
			<TreeView.Label>File System</TreeView.Label>
			<TreeView.Tree>
				{collection.rootNode.children?.map((node, index) => (
					<TreeNode node={node} indexPath={[index]} key={node.id} />
				))}
			</TreeView.Tree>
		</TreeView>
	);
}

```

## Provider Pattern

Use the [Provider Pattern](/docs/\[framework]/get-started/fundamentals#provider-pattern) to gain access to the `collapse` and `expand` methods on the `TreeView` instance.

```tsx
import { TreeView, createTreeViewCollection, useTreeView } from '@skeletonlabs/skeleton-react';
import { FileIcon, FolderIcon } from 'lucide-react';

interface Node {
	id: string;
	name: string;
	children?: Node[];
}

function TreeNode(props: { node: Node; indexPath: number[] }) {
	return (
		<TreeView.NodeProvider value={props}>
			{props.node.children ? (
				<TreeView.Branch>
					<TreeView.BranchControl>
						<TreeView.BranchIndicator />
						<TreeView.BranchText>
							<FolderIcon className="size-4" />
							{props.node.name}
						</TreeView.BranchText>
					</TreeView.BranchControl>
					<TreeView.BranchContent>
						<TreeView.BranchIndentGuide />
						{props.node.children.map((childNode, childIndex) => (
							<TreeNode key={childNode.id} node={childNode} indexPath={[...props.indexPath, childIndex]} />
						))}
					</TreeView.BranchContent>
				</TreeView.Branch>
			) : (
				<TreeView.Item>
					<FileIcon className="size-4" />
					{props.node.name}
				</TreeView.Item>
			)}
		</TreeView.NodeProvider>
	);
}

export default function CollapseExpand() {
	const collection = createTreeViewCollection<Node>({
		nodeToValue: (node) => node.id,
		nodeToString: (node) => node.name,
		rootNode: {
			id: 'root',
			name: '',
			children: [
				{
					id: 'node_modules',
					name: 'node_modules',
					children: [
						{
							id: 'node_modules/@skeletonlabs',
							name: '@skeletonlabs',
							children: [
								{
									id: 'node_modules/@skeletonlabs/skeleton',
									name: 'skeleton',
								},
							],
						},
					],
				},
				{
					id: 'package.json',
					name: 'package.json',
				},
			],
		},
	});

	const treeView = useTreeView({
		collection: collection,
	});

	return (
		<div className="w-full flex flex-col items-center gap-4">
			<TreeView.Provider value={treeView}>
				<TreeView.Label>File System</TreeView.Label>
				<TreeView.Tree>
					{collection.rootNode.children?.map((node, index) => (
						<TreeNode node={node} indexPath={[index]} key={node.id} />
					))}
				</TreeView.Tree>
			</TreeView.Provider>

			<div className="flex gap-2">
				<button className="btn preset-filled" onClick={() => treeView.collapse()}>
					Collapse
				</button>
				<button className="btn preset-filled" onClick={() => treeView.expand()}>
					Expand
				</button>
			</div>
		</div>
	);
}

```

## Lazy Loading

Utilize promises to asynchronously load large node lists.

```tsx
import { TreeView, createTreeViewCollection, type TreeViewRootProps } from '@skeletonlabs/skeleton-react';
import { FileIcon, FolderIcon, LoaderIcon } from 'lucide-react';
import { useState } from 'react';

interface Node {
	id: string;
	name: string;
	children?: Node[];
	childrenCount?: number;
}

const response: Record<string, Node[]> = {
	node_modules: [
		{
			id: 'node_modules/@skeletonlabs',
			name: '@skeletonlabs',
			childrenCount: 3,
		},
	],
	'node_modules/@skeletonlabs': [
		{
			id: 'node_modules/@skeletonlabs/skeleton',
			name: 'skeleton',
		},
		{
			id: 'node_modules/@skeletonlabs/skeleton-react',
			name: 'skeleton-react',
		},
		{
			id: 'node_modules/@skeletonlabs/skeleton-svelte',
			name: 'skeleton-svelte',
		},
	],
};

function TreeNode(props: { node: Node; indexPath: number[] }) {
	return (
		<TreeView.NodeProvider value={props}>
			{props.node.children || props.node.childrenCount ? (
				<TreeView.Branch>
					<TreeView.BranchControl>
						<TreeView.BranchIndicator className="data-loading:hidden" />
						<TreeView.BranchIndicator className="hidden data-loading:inline animate-spin">
							<LoaderIcon className="size-4" />
						</TreeView.BranchIndicator>
						<TreeView.BranchText>
							<FolderIcon className="size-4" />
							{props.node.name}
						</TreeView.BranchText>
					</TreeView.BranchControl>
					<TreeView.BranchContent>
						<TreeView.BranchIndentGuide />
						{props.node.children?.map((childNode, childIndex) => (
							<TreeNode key={childNode.id} node={childNode} indexPath={[...props.indexPath, childIndex]} />
						))}
					</TreeView.BranchContent>
				</TreeView.Branch>
			) : (
				<TreeView.Item>
					<FileIcon className="size-4" />
					{props.node.name}
				</TreeView.Item>
			)}
		</TreeView.NodeProvider>
	);
}

export default function LazyLoading() {
	const [collection, setCollection] = useState(
		createTreeViewCollection<Node>({
			nodeToValue: (node) => node.id,
			nodeToString: (node) => node.name,
			rootNode: {
				id: 'root',
				name: '',
				children: [
					{
						id: 'node_modules',
						name: 'node_modules',
						childrenCount: 1,
					},
					{
						id: 'package.json',
						name: 'package.json',
					},
				],
			},
		}),
	);

	const loadChildren: TreeViewRootProps['loadChildren'] = async (details) => {
		await new Promise((resolve) => setTimeout(resolve, 1000));
		return response[details.node.id] || [];
	};

	const onLoadChildrenComplete: TreeViewRootProps['onLoadChildrenComplete'] = (details) => {
		setCollection(details.collection);
	};

	return (
		<TreeView collection={collection} loadChildren={loadChildren} onLoadChildrenComplete={onLoadChildrenComplete}>
			<TreeView.Label>File System</TreeView.Label>
			<TreeView.Tree>
				{collection.rootNode.children?.map((node, index) => (
					<TreeNode node={node} indexPath={[index]} key={node.id} />
				))}
			</TreeView.Tree>
		</TreeView>
	);
}

```

## Anatomy

Here's an overview of how the TreeView component is structured in code:

```tsx
import { TreeView } from '@skeletonlabs/skeleton-react';

export default function Anatomy() {
	return (
		<TreeView>
			<TreeView.Label />
			<TreeView.Tree>
				<TreeView.Branch>
					<TreeView.BranchControl>
						<TreeView.BranchTrigger />
						<TreeView.BranchIndicator />
						<TreeView.BranchText />
					</TreeView.BranchControl>
					<TreeView.BranchContent>
						<TreeView.Item>
							<TreeView.ItemText />
						</TreeView.Item>
					</TreeView.BranchContent>
				</TreeView.Branch>
			</TreeView.Tree>
		</TreeView>
	);
}
```

## API Reference

### Root

| Prop                   | Description                                                                                                                                 | Type                                                                                                    | Default  |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | -------- |
| collection             | The tree collection data                                                                                                                    | TreeCollection\<T> \| undefined                                                                         | -        |
| ids                    | The ids of the tree elements. Useful for composition.                                                                                       | Partial\<\{ root: string; tree: string; label: string; node: (value: string) => string; }> \| undefined | -        |
| expandedValue          | The controlled expanded node ids                                                                                                            | string\[] \| undefined                                                                                  | -        |
| defaultExpandedValue   | The initial expanded node ids when rendered.&#xA;Use when you don't need to control the expanded node value.                                | string\[] \| undefined                                                                                  | -        |
| selectedValue          | The controlled selected node value                                                                                                          | string\[] \| undefined                                                                                  | -        |
| defaultSelectedValue   | The initial selected node value when rendered.&#xA;Use when you don't need to control the selected node value.                              | string\[] \| undefined                                                                                  | -        |
| defaultCheckedValue    | The initial checked node value when rendered.&#xA;Use when you don't need to control the checked node value.                                | string\[] \| undefined                                                                                  | -        |
| checkedValue           | The controlled checked node value                                                                                                           | string\[] \| undefined                                                                                  | -        |
| defaultFocusedValue    | The initial focused node value when rendered.&#xA;Use when you don't need to control the focused node value.                                | string \| null \| undefined                                                                             | -        |
| focusedValue           | The value of the focused node                                                                                                               | string \| null \| undefined                                                                             | -        |
| selectionMode          | Whether the tree supports multiple selection&#xA;- "single": only one node can be selected&#xA;- "multiple": multiple nodes can be selected | "single" \| "multiple" \| undefined                                                                     | "single" |
| onExpandedChange       | Called when the tree is opened or closed                                                                                                    | ((details: ExpandedChangeDetails\<T>) => void) \| undefined                                             | -        |
| onSelectionChange      | Called when the selection changes                                                                                                           | ((details: SelectionChangeDetails\<T>) => void) \| undefined                                            | -        |
| onFocusChange          | Called when the focused node changes                                                                                                        | ((details: FocusChangeDetails\<T>) => void) \| undefined                                                | -        |
| onCheckedChange        | Called when the checked value changes                                                                                                       | ((details: CheckedChangeDetails) => void) \| undefined                                                  | -        |
| canRename              | Function to determine if a node can be renamed                                                                                              | ((node: T, indexPath: IndexPath) => boolean) \| undefined                                               | -        |
| onRenameStart          | Called when a node starts being renamed                                                                                                     | ((details: RenameStartDetails\<T>) => void) \| undefined                                                | -        |
| onBeforeRename         | Called before a rename is completed. Return false to prevent the rename.                                                                    | ((details: RenameCompleteDetails) => boolean) \| undefined                                              | -        |
| onRenameComplete       | Called when a node label rename is completed                                                                                                | ((details: RenameCompleteDetails) => void) \| undefined                                                 | -        |
| onLoadChildrenComplete | Called when a node finishes loading children                                                                                                | ((details: LoadChildrenCompleteDetails\<T>) => void) \| undefined                                       | -        |
| onLoadChildrenError    | Called when loading children fails for one or more nodes                                                                                    | ((details: LoadChildrenErrorDetails\<T>) => void) \| undefined                                          | -        |
| expandOnClick          | Whether clicking on a branch should open it or not                                                                                          | boolean \| undefined                                                                                    | true     |
| typeahead              | Whether the tree supports typeahead search                                                                                                  | boolean \| undefined                                                                                    | true     |
| loadChildren           | Function to load children for a node asynchronously.&#xA;When provided, branches will wait for this promise to resolve before expanding.    | ((details: LoadChildrenDetails\<T>) => Promise\<T\[]>) \| undefined                                     | -        |
| scrollToIndexFn        | Function to scroll to a specific index.&#xA;Useful for virtualized tree views.                                                              | ((details: ScrollToIndexDetails\<T>) => void) \| undefined                                              | -        |
| dir                    | The document's text/writing direction.                                                                                                      | "ltr" \| "rtl" \| undefined                                                                             | "ltr"    |
| getRootNode            | A root node to correctly resolve document in custom environments. E.x.: Iframes, Electron.                                                  | (() => ShadowRoot \| Node \| Document) \| undefined                                                     | -        |
| element                | Render the element yourself                                                                                                                 | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined                                          | -        |

### Provider

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| value   | -                           | TreeViewApi\<PropTypes, any>                                   | -       |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Context

| Prop     | Description | Type                                                  | Default |
| -------- | ----------- | ----------------------------------------------------- | ------- |
| children | -           | (treeView: TreeViewApi\<PropTypes, any>) => ReactNode | -       |

### Tree

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Label

| Prop    | Description                 | Type                                                          | Default |
| ------- | --------------------------- | ------------------------------------------------------------- | ------- |
| level   | The level of the heading.   | 1 \| 2 \| 3 \| 4 \| 5 \| 6 \| undefined                       | -       |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"h3">) => Element) \| undefined | -       |

### NodeProvider

| Prop     | Description | Type      | Default |
| -------- | ----------- | --------- | ------- |
| value    | -           | NodeProps | -       |
| children | -           | ReactNode | -       |

### NodeContext

| Prop     | Description | Type                               | Default |
| -------- | ----------- | ---------------------------------- | ------- |
| children | -           | (treeView: NodeProps) => ReactNode | -       |

### Branch

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### BranchControl

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### BranchText

| Prop    | Description                 | Type                                                            | Default |
| ------- | --------------------------- | --------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"span">) => Element) \| undefined | -       |

### BranchIndicator

| Prop    | Description                 | Type                                                            | Default |
| ------- | --------------------------- | --------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"span">) => Element) \| undefined | -       |

### BranchContent

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### BranchIndentGuide

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Item

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |
