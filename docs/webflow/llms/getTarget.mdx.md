# Source: https://developers.webflow.com/designer/reference/link-element/getTarget.mdx

***

title: Get Link Target
slug: designer/reference/link-element/getTarget
description: Get the target value of the link block element.
hidden: false
'og:title': 'Webflow Designer API: Link Element - getTarget()'
'og:description': Get the target value of the link block element.
-----------------------------------------------------------------

## `element.getTarget()`

Get the target value of the link block element. Links can target URLs emails, and phone numbers, as well as pages within a site, elements on a page, and attachments.

## Syntax

```typescript
element.getTarget(): Promise<null | string | Page | AnyElement | Asset>;
```

## Returns

**Promise\<*null | string | Page | AnyElement | Asset*>**

A Promise that resolves to the target value of the link. The target value can be a string, Page, Element, or an Asset object.

## Example

```typescript
const elements = await webflow.getAllElements(); // Get All Elements
const links = elements.filter((element) => element.type === "Link"); // Filter for Link elements

// Print target value of each link element
for (const link of links) {
  const targetValue = await link.getTarget();
  console.log(`ID: ${link.id.element}, Target Value: ${targetValue}`);
}
```

## Designer Ability

Checks for authorization only

| Designer Ability    | Locale | Branch | Workflow | Sitemode |
| :------------------ | :----- | :----- | :------- | :------- |
| **canAccessCanvas** | any    | any    | any      | any      |

```
```
