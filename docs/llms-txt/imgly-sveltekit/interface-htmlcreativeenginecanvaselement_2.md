# Interface: HTMLCreativeEngineCanvasElement

A wrapper around a plain canvas

The idea is to shield the user from the weird semantics of changing width and height of a canvas by making this a opaque block element instead and managing the internal render resolution of the canvas dynamically

## Extends[#](#extends)

*   `HTMLElement`

## Methods[#](#methods)

### clear()[#](#clear)

```
clear(): void;
```

Clear the canvas

This is useful when mounting the canvas into a new position in the DOM. If the canvas is not cleared, it will appear in the new DOM position, with its contents stretched to the new size. It will re-render correctly during the next animation frame, but for a brief moment the canvas contents can flash distorted.

Call `clear()` before mounting into the DOM to avoid this. This will cause the canvas to be cleared until rendering the next frame.

#### Returns[#](#returns)

`void`

* * *

### animate()[#](#animate)

```
animate(keyframes, options?): Animation;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/animate)

#### Parameters[#](#parameters)

| Parameter | Type |
| --- | --- |
| `keyframes` | `Keyframe`\[\] |
| `options?` | `number` |

#### Returns[#](#returns-1)

`Animation`

#### Inherited from[#](#inherited-from)

```
HTMLElement.animate
```

* * *

### getAnimations()[#](#getanimations)

```
getAnimations(options?): Animation[];
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/getAnimations)

#### Parameters[#](#parameters-1)

| Parameter | Type |
| --- | --- |
| `options?` | `GetAnimationsOptions` |

#### Returns[#](#returns-2)

`Animation`\[\]

#### Inherited from[#](#inherited-from-1)

```
HTMLElement.getAnimations
```

* * *

### after()[#](#after)

```
after(...nodes): void;
```

Inserts nodes just after node, while replacing strings in nodes with equivalent Text nodes.

Throws a “HierarchyRequestError” DOMException if the constraints of the node tree are violated.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/CharacterData/after)

#### Parameters[#](#parameters-2)

| Parameter | Type |
| --- | --- |
| …`nodes` | (`string` |

#### Returns[#](#returns-3)

`void`

#### Inherited from[#](#inherited-from-2)

```
HTMLElement.after
```

* * *

### before()[#](#before)

```
before(...nodes): void;
```

Inserts nodes just before node, while replacing strings in nodes with equivalent Text nodes.

Throws a “HierarchyRequestError” DOMException if the constraints of the node tree are violated.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/CharacterData/before)

#### Parameters[#](#parameters-3)

| Parameter | Type |
| --- | --- |
| …`nodes` | (`string` |

#### Returns[#](#returns-4)

`void`

#### Inherited from[#](#inherited-from-3)

```
HTMLElement.before
```

* * *

### remove()[#](#remove)

```
remove(): void;
```

Removes node.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/CharacterData/remove)

#### Returns[#](#returns-5)

`void`

#### Inherited from[#](#inherited-from-4)

```
HTMLElement.remove
```

* * *

### replaceWith()[#](#replacewith)

```
replaceWith(...nodes): void;
```

Replaces node with nodes, while replacing strings in nodes with equivalent Text nodes.

Throws a “HierarchyRequestError” DOMException if the constraints of the node tree are violated.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/CharacterData/replaceWith)

#### Parameters[#](#parameters-4)

| Parameter | Type |
| --- | --- |
| …`nodes` | (`string` |

#### Returns[#](#returns-6)

`void`

#### Inherited from[#](#inherited-from-5)

```
HTMLElement.replaceWith
```

* * *

### attachShadow()[#](#attachshadow)

```
attachShadow(init): ShadowRoot;
```

Creates a shadow root for element and returns it.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/attachShadow)

#### Parameters[#](#parameters-5)

| Parameter | Type |
| --- | --- |
| `init` | `ShadowRootInit` |

#### Returns[#](#returns-7)

`ShadowRoot`

#### Inherited from[#](#inherited-from-6)

```
HTMLElement.attachShadow
```

* * *

### checkVisibility()[#](#checkvisibility)

```
checkVisibility(options?): boolean;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/checkVisibility)

#### Parameters[#](#parameters-6)

| Parameter | Type |
| --- | --- |
| `options?` | `CheckVisibilityOptions` |

#### Returns[#](#returns-8)

`boolean`

#### Inherited from[#](#inherited-from-7)

```
HTMLElement.checkVisibility
```

* * *

### closest()[#](#closest)

#### Call Signature[#](#call-signature)

```
closest<K>(selector): HTMLElementTagNameMap[K];
```

Returns the first (starting at element) inclusive ancestor that matches selectors, and null otherwise.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/closest)

##### Type Parameters[#](#type-parameters)

| Type Parameter |
| --- |
| `K` _extends_ keyof `HTMLElementTagNameMap` |

##### Parameters[#](#parameters-7)

| Parameter | Type |
| --- | --- |
| `selector` | `K` |

##### Returns[#](#returns-9)

`HTMLElementTagNameMap`\[`K`\]

##### Inherited from[#](#inherited-from-8)

```
HTMLElement.closest
```

#### Call Signature[#](#call-signature-1)

```
closest<K>(selector): SVGElementTagNameMap[K];
```

##### Type Parameters[#](#type-parameters-1)

| Type Parameter |
| --- |
| `K` _extends_ keyof `SVGElementTagNameMap` |

##### Parameters[#](#parameters-8)

| Parameter | Type |
| --- | --- |
| `selector` | `K` |

##### Returns[#](#returns-10)

`SVGElementTagNameMap`\[`K`\]

##### Inherited from[#](#inherited-from-9)

```
HTMLElement.closest
```

#### Call Signature[#](#call-signature-2)

```
closest<K>(selector): MathMLElementTagNameMap[K];
```

##### Type Parameters[#](#type-parameters-2)

| Type Parameter |
| --- |
| `K` _extends_ keyof `MathMLElementTagNameMap` |

##### Parameters[#](#parameters-9)

| Parameter | Type |
| --- | --- |
| `selector` | `K` |

##### Returns[#](#returns-11)

`MathMLElementTagNameMap`\[`K`\]

##### Inherited from[#](#inherited-from-10)

```
HTMLElement.closest
```

#### Call Signature[#](#call-signature-3)

```
closest<E>(selectors): E;
```

##### Type Parameters[#](#type-parameters-3)

| Type Parameter | Default type |
| --- | --- |
| `E` _extends_ `Element` | `Element` |

##### Parameters[#](#parameters-10)

| Parameter | Type |
| --- | --- |
| `selectors` | `string` |

##### Returns[#](#returns-12)

`E`

##### Inherited from[#](#inherited-from-11)

```
HTMLElement.closest
```

* * *

### computedStyleMap()[#](#computedstylemap)

```
computedStyleMap(): StylePropertyMapReadOnly;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/computedStyleMap)

#### Returns[#](#returns-13)

`StylePropertyMapReadOnly`

#### Inherited from[#](#inherited-from-12)

```
HTMLElement.computedStyleMap
```

* * *

### getAttribute()[#](#getattribute)

```
getAttribute(qualifiedName): string;
```

Returns element’s first attribute whose qualified name is qualifiedName, and null if there is no such attribute otherwise.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/getAttribute)

#### Parameters[#](#parameters-11)

| Parameter | Type |
| --- | --- |
| `qualifiedName` | `string` |

#### Returns[#](#returns-14)

`string`

#### Inherited from[#](#inherited-from-13)

```
HTMLElement.getAttribute
```

* * *

### getAttributeNS()[#](#getattributens)

```
getAttributeNS(namespace, localName): string;
```

Returns element’s attribute whose namespace is namespace and local name is localName, and null if there is no such attribute otherwise.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/getAttributeNS)

#### Parameters[#](#parameters-12)

| Parameter | Type |
| --- | --- |
| `namespace` | `string` |
| `localName` | `string` |

#### Returns[#](#returns-15)

`string`

#### Inherited from[#](#inherited-from-14)

```
HTMLElement.getAttributeNS
```

* * *

### getAttributeNames()[#](#getattributenames)

```
getAttributeNames(): string[];
```

Returns the qualified names of all element’s attributes. Can contain duplicates.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/getAttributeNames)

#### Returns[#](#returns-16)

`string`\[\]

#### Inherited from[#](#inherited-from-15)

```
HTMLElement.getAttributeNames
```

* * *

### getAttributeNode()[#](#getattributenode)

```
getAttributeNode(qualifiedName): Attr;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/getAttributeNode)

#### Parameters[#](#parameters-13)

| Parameter | Type |
| --- | --- |
| `qualifiedName` | `string` |

#### Returns[#](#returns-17)

`Attr`

#### Inherited from[#](#inherited-from-16)

```
HTMLElement.getAttributeNode
```

* * *

### getAttributeNodeNS()[#](#getattributenodens)

```
getAttributeNodeNS(namespace, localName): Attr;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/getAttributeNodeNS)

#### Parameters[#](#parameters-14)

| Parameter | Type |
| --- | --- |
| `namespace` | `string` |
| `localName` | `string` |

#### Returns[#](#returns-18)

`Attr`

#### Inherited from[#](#inherited-from-17)

```
HTMLElement.getAttributeNodeNS
```

* * *

### getBoundingClientRect()[#](#getboundingclientrect)

```
getBoundingClientRect(): DOMRect;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/getBoundingClientRect)

#### Returns[#](#returns-19)

`DOMRect`

#### Inherited from[#](#inherited-from-18)

```
HTMLElement.getBoundingClientRect
```

* * *

### getClientRects()[#](#getclientrects)

```
getClientRects(): DOMRectList;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/getClientRects)

#### Returns[#](#returns-20)

`DOMRectList`

#### Inherited from[#](#inherited-from-19)

```
HTMLElement.getClientRects
```

* * *

### getElementsByClassName()[#](#getelementsbyclassname)

```
getElementsByClassName(classNames): HTMLCollectionOf<Element>;
```

Returns a HTMLCollection of the elements in the object on which the method was invoked (a document or an element) that have all the classes given by classNames. The classNames argument is interpreted as a space-separated list of classes.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/getElementsByClassName)

#### Parameters[#](#parameters-15)

| Parameter | Type |
| --- | --- |
| `classNames` | `string` |

#### Returns[#](#returns-21)

`HTMLCollectionOf`<`Element`\>

#### Inherited from[#](#inherited-from-20)

```
HTMLElement.getElementsByClassName
```

* * *

### getElementsByTagName()[#](#getelementsbytagname)

#### Call Signature[#](#call-signature-4)

```
getElementsByTagName<K>(qualifiedName): HTMLCollectionOf<HTMLElementTagNameMap[K]>;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/getElementsByTagName)

##### Type Parameters[#](#type-parameters-4)

| Type Parameter |
| --- |
| `K` _extends_ keyof `HTMLElementTagNameMap` |

##### Parameters[#](#parameters-16)

| Parameter | Type |
| --- | --- |
| `qualifiedName` | `K` |

##### Returns[#](#returns-22)

`HTMLCollectionOf`<`HTMLElementTagNameMap`\[`K`\]>

##### Inherited from[#](#inherited-from-21)

```
HTMLElement.getElementsByTagName
```

#### Call Signature[#](#call-signature-5)

```
getElementsByTagName<K>(qualifiedName): HTMLCollectionOf<SVGElementTagNameMap[K]>;
```

##### Type Parameters[#](#type-parameters-5)

| Type Parameter |
| --- |
| `K` _extends_ keyof `SVGElementTagNameMap` |

##### Parameters[#](#parameters-17)

| Parameter | Type |
| --- | --- |
| `qualifiedName` | `K` |

##### Returns[#](#returns-23)

`HTMLCollectionOf`<`SVGElementTagNameMap`\[`K`\]>

##### Inherited from[#](#inherited-from-22)

```
HTMLElement.getElementsByTagName
```

#### Call Signature[#](#call-signature-6)

```
getElementsByTagName<K>(qualifiedName): HTMLCollectionOf<MathMLElementTagNameMap[K]>;
```

##### Type Parameters[#](#type-parameters-6)

| Type Parameter |
| --- |
| `K` _extends_ keyof `MathMLElementTagNameMap` |

##### Parameters[#](#parameters-18)

| Parameter | Type |
| --- | --- |
| `qualifiedName` | `K` |

##### Returns[#](#returns-24)

`HTMLCollectionOf`<`MathMLElementTagNameMap`\[`K`\]>

##### Inherited from[#](#inherited-from-23)

```
HTMLElement.getElementsByTagName
```

#### Call Signature[#](#call-signature-7)

```
getElementsByTagName<K>(qualifiedName): HTMLCollectionOf<HTMLElementDeprecatedTagNameMap[K]>;
```

##### Type Parameters[#](#type-parameters-7)

| Type Parameter |
| --- |
| `K` _extends_ keyof `HTMLElementDeprecatedTagNameMap` |

##### Parameters[#](#parameters-19)

| Parameter | Type |
| --- | --- |
| `qualifiedName` | `K` |

##### Returns[#](#returns-25)

`HTMLCollectionOf`<`HTMLElementDeprecatedTagNameMap`\[`K`\]>

##### Deprecated[#](#deprecated)

##### Inherited from[#](#inherited-from-24)

```
HTMLElement.getElementsByTagName
```

#### Call Signature[#](#call-signature-8)

```
getElementsByTagName(qualifiedName): HTMLCollectionOf<Element>;
```

##### Parameters[#](#parameters-20)

| Parameter | Type |
| --- | --- |
| `qualifiedName` | `string` |

##### Returns[#](#returns-26)

`HTMLCollectionOf`<`Element`\>

##### Inherited from[#](#inherited-from-25)

```
HTMLElement.getElementsByTagName
```

* * *

### getElementsByTagNameNS()[#](#getelementsbytagnamens)

#### Call Signature[#](#call-signature-9)

```
getElementsByTagNameNS(namespaceURI, localName): HTMLCollectionOf<HTMLElement>;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/getElementsByTagNameNS)

##### Parameters[#](#parameters-21)

| Parameter | Type |
| --- | --- |
| `namespaceURI` | `"http://www.w3.org/1999/xhtml"` |
| `localName` | `string` |

##### Returns[#](#returns-27)

`HTMLCollectionOf`<`HTMLElement`\>

##### Inherited from[#](#inherited-from-26)

```
HTMLElement.getElementsByTagNameNS
```

#### Call Signature[#](#call-signature-10)

```
getElementsByTagNameNS(namespaceURI, localName): HTMLCollectionOf<SVGElement>;
```

##### Parameters[#](#parameters-22)

| Parameter | Type |
| --- | --- |
| `namespaceURI` | `"http://www.w3.org/2000/svg"` |
| `localName` | `string` |

##### Returns[#](#returns-28)

`HTMLCollectionOf`<`SVGElement`\>

##### Inherited from[#](#inherited-from-27)

```
HTMLElement.getElementsByTagNameNS
```

#### Call Signature[#](#call-signature-11)

```
getElementsByTagNameNS(namespaceURI, localName): HTMLCollectionOf<MathMLElement>;
```

##### Parameters[#](#parameters-23)

| Parameter | Type |
| --- | --- |
| `namespaceURI` | `"http://www.w3.org/1998/Math/MathML"` |
| `localName` | `string` |

##### Returns[#](#returns-29)

`HTMLCollectionOf`<`MathMLElement`\>

##### Inherited from[#](#inherited-from-28)

```
HTMLElement.getElementsByTagNameNS
```

#### Call Signature[#](#call-signature-12)

```
getElementsByTagNameNS(namespace, localName): HTMLCollectionOf<Element>;
```

##### Parameters[#](#parameters-24)

| Parameter | Type |
| --- | --- |
| `namespace` | `string` |
| `localName` | `string` |

##### Returns[#](#returns-30)

`HTMLCollectionOf`<`Element`\>

##### Inherited from[#](#inherited-from-29)

```
HTMLElement.getElementsByTagNameNS
```

* * *

### getHTML()[#](#gethtml)

```
getHTML(options?): string;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/getHTML)

#### Parameters[#](#parameters-25)

| Parameter | Type |
| --- | --- |
| `options?` | `GetHTMLOptions` |

#### Returns[#](#returns-31)

`string`

#### Inherited from[#](#inherited-from-30)

```
HTMLElement.getHTML
```

* * *

### hasAttribute()[#](#hasattribute)

```
hasAttribute(qualifiedName): boolean;
```

Returns true if element has an attribute whose qualified name is qualifiedName, and false otherwise.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/hasAttribute)

#### Parameters[#](#parameters-26)

| Parameter | Type |
| --- | --- |
| `qualifiedName` | `string` |

#### Returns[#](#returns-32)

`boolean`

#### Inherited from[#](#inherited-from-31)

```
HTMLElement.hasAttribute
```

* * *

### hasAttributeNS()[#](#hasattributens)

```
hasAttributeNS(namespace, localName): boolean;
```

Returns true if element has an attribute whose namespace is namespace and local name is localName.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/hasAttributeNS)

#### Parameters[#](#parameters-27)

| Parameter | Type |
| --- | --- |
| `namespace` | `string` |
| `localName` | `string` |

#### Returns[#](#returns-33)

`boolean`

#### Inherited from[#](#inherited-from-32)

```
HTMLElement.hasAttributeNS
```

* * *

### hasAttributes()[#](#hasattributes)

```
hasAttributes(): boolean;
```

Returns true if element has attributes, and false otherwise.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/hasAttributes)

#### Returns[#](#returns-34)

`boolean`

#### Inherited from[#](#inherited-from-33)

```
HTMLElement.hasAttributes
```

* * *

### hasPointerCapture()[#](#haspointercapture)

```
hasPointerCapture(pointerId): boolean;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/hasPointerCapture)

#### Parameters[#](#parameters-28)

| Parameter | Type |
| --- | --- |
| `pointerId` | `number` |

#### Returns[#](#returns-35)

`boolean`

#### Inherited from[#](#inherited-from-34)

```
HTMLElement.hasPointerCapture
```

* * *

### insertAdjacentElement()[#](#insertadjacentelement)

```
insertAdjacentElement(where, element): Element;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/insertAdjacentElement)

#### Parameters[#](#parameters-29)

| Parameter | Type |
| --- | --- |
| `where` | `InsertPosition` |
| `element` | `Element` |

#### Returns[#](#returns-36)

`Element`

#### Inherited from[#](#inherited-from-35)

```
HTMLElement.insertAdjacentElement
```

* * *

### insertAdjacentHTML()[#](#insertadjacenthtml)

```
insertAdjacentHTML(position, string): void;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/insertAdjacentHTML)

#### Parameters[#](#parameters-30)

| Parameter | Type |
| --- | --- |
| `position` | `InsertPosition` |
| `string` | `string` |

#### Returns[#](#returns-37)

`void`

#### Inherited from[#](#inherited-from-36)

```
HTMLElement.insertAdjacentHTML
```

* * *

### insertAdjacentText()[#](#insertadjacenttext)

```
insertAdjacentText(where, data): void;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/insertAdjacentText)

#### Parameters[#](#parameters-31)

| Parameter | Type |
| --- | --- |
| `where` | `InsertPosition` |
| `data` | `string` |

#### Returns[#](#returns-38)

`void`

#### Inherited from[#](#inherited-from-37)

```
HTMLElement.insertAdjacentText
```

* * *

### matches()[#](#matches)

```
matches(selectors): boolean;
```

Returns true if matching selectors against element’s root yields element, and false otherwise.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/matches)

#### Parameters[#](#parameters-32)

| Parameter | Type |
| --- | --- |
| `selectors` | `string` |

#### Returns[#](#returns-39)

`boolean`

#### Inherited from[#](#inherited-from-38)

```
HTMLElement.matches
```

* * *

### releasePointerCapture()[#](#releasepointercapture)

```
releasePointerCapture(pointerId): void;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/releasePointerCapture)

#### Parameters[#](#parameters-33)

| Parameter | Type |
| --- | --- |
| `pointerId` | `number` |

#### Returns[#](#returns-40)

`void`

#### Inherited from[#](#inherited-from-39)

```
HTMLElement.releasePointerCapture
```

* * *

### removeAttribute()[#](#removeattribute)

```
removeAttribute(qualifiedName): void;
```

Removes element’s first attribute whose qualified name is qualifiedName.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/removeAttribute)

#### Parameters[#](#parameters-34)

| Parameter | Type |
| --- | --- |
| `qualifiedName` | `string` |

#### Returns[#](#returns-41)

`void`

#### Inherited from[#](#inherited-from-40)

```
HTMLElement.removeAttribute
```

* * *

### removeAttributeNS()[#](#removeattributens)

```
removeAttributeNS(namespace, localName): void;
```

Removes element’s attribute whose namespace is namespace and local name is localName.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/removeAttributeNS)

#### Parameters[#](#parameters-35)

| Parameter | Type |
| --- | --- |
| `namespace` | `string` |
| `localName` | `string` |

#### Returns[#](#returns-42)

`void`

#### Inherited from[#](#inherited-from-41)

```
HTMLElement.removeAttributeNS
```

* * *

### removeAttributeNode()[#](#removeattributenode)

```
removeAttributeNode(attr): Attr;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/removeAttributeNode)

#### Parameters[#](#parameters-36)

| Parameter | Type |
| --- | --- |
| `attr` | `Attr` |

#### Returns[#](#returns-43)

`Attr`

#### Inherited from[#](#inherited-from-42)

```
HTMLElement.removeAttributeNode
```

* * *

### requestFullscreen()[#](#requestfullscreen)

```
requestFullscreen(options?): Promise<void>;
```

Displays element fullscreen and resolves promise when done.

When supplied, options’s navigationUI member indicates whether showing navigation UI while in fullscreen is preferred or not. If set to “show”, navigation simplicity is preferred over screen space, and if set to “hide”, more screen space is preferred. User agents are always free to honor user preference over the application’s. The default value “auto” indicates no application preference.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/requestFullscreen)

#### Parameters[#](#parameters-37)

| Parameter | Type |
| --- | --- |
| `options?` | `FullscreenOptions` |

#### Returns[#](#returns-44)

`Promise`<`void`\>

#### Inherited from[#](#inherited-from-43)

```
HTMLElement.requestFullscreen
```

* * *

### requestPointerLock()[#](#requestpointerlock)

```
requestPointerLock(options?): Promise<void>;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/requestPointerLock)

#### Parameters[#](#parameters-38)

| Parameter | Type |
| --- | --- |
| `options?` | `PointerLockOptions` |

#### Returns[#](#returns-45)

`Promise`<`void`\>

#### Inherited from[#](#inherited-from-44)

```
HTMLElement.requestPointerLock
```

* * *

### scroll()[#](#scroll)

#### Call Signature[#](#call-signature-13)

```
scroll(options?): void;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/scroll)

##### Parameters[#](#parameters-39)

| Parameter | Type |
| --- | --- |
| `options?` | `ScrollToOptions` |

##### Returns[#](#returns-46)

`void`

##### Inherited from[#](#inherited-from-45)

```
HTMLElement.scroll
```

#### Call Signature[#](#call-signature-14)

```
scroll(x, y): void;
```

##### Parameters[#](#parameters-40)

| Parameter | Type |
| --- | --- |
| `x` | `number` |
| `y` | `number` |

##### Returns[#](#returns-47)

`void`

##### Inherited from[#](#inherited-from-46)

```
HTMLElement.scroll
```

* * *

### scrollBy()[#](#scrollby)

#### Call Signature[#](#call-signature-15)

```
scrollBy(options?): void;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/scrollBy)

##### Parameters[#](#parameters-41)

| Parameter | Type |
| --- | --- |
| `options?` | `ScrollToOptions` |

##### Returns[#](#returns-48)

`void`

##### Inherited from[#](#inherited-from-47)

```
HTMLElement.scrollBy
```

#### Call Signature[#](#call-signature-16)

```
scrollBy(x, y): void;
```

##### Parameters[#](#parameters-42)

| Parameter | Type |
| --- | --- |
| `x` | `number` |
| `y` | `number` |

##### Returns[#](#returns-49)

`void`

##### Inherited from[#](#inherited-from-48)

```
HTMLElement.scrollBy
```

* * *

### scrollIntoView()[#](#scrollintoview)

```
scrollIntoView(arg?): void;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/scrollIntoView)

#### Parameters[#](#parameters-43)

| Parameter | Type |
| --- | --- |
| `arg?` | `boolean` |

#### Returns[#](#returns-50)

`void`

#### Inherited from[#](#inherited-from-49)

```
HTMLElement.scrollIntoView
```

* * *

### scrollTo()[#](#scrollto)

#### Call Signature[#](#call-signature-17)

```
scrollTo(options?): void;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/scrollTo)

##### Parameters[#](#parameters-44)

| Parameter | Type |
| --- | --- |
| `options?` | `ScrollToOptions` |

##### Returns[#](#returns-51)

`void`

##### Inherited from[#](#inherited-from-50)

```
HTMLElement.scrollTo
```

#### Call Signature[#](#call-signature-18)

```
scrollTo(x, y): void;
```

##### Parameters[#](#parameters-45)

| Parameter | Type |
| --- | --- |
| `x` | `number` |
| `y` | `number` |

##### Returns[#](#returns-52)

`void`

##### Inherited from[#](#inherited-from-51)

```
HTMLElement.scrollTo
```

* * *

### setAttribute()[#](#setattribute)

```
setAttribute(qualifiedName, value): void;
```

Sets the value of element’s first attribute whose qualified name is qualifiedName to value.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/setAttribute)

#### Parameters[#](#parameters-46)

| Parameter | Type |
| --- | --- |
| `qualifiedName` | `string` |
| `value` | `string` |

#### Returns[#](#returns-53)

`void`

#### Inherited from[#](#inherited-from-52)

```
HTMLElement.setAttribute
```

* * *

### setAttributeNS()[#](#setattributens)

```
setAttributeNS(   namespace,   qualifiedName,   value): void;
```

Sets the value of element’s attribute whose namespace is namespace and local name is localName to value.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/setAttributeNS)

#### Parameters[#](#parameters-47)

| Parameter | Type |
| --- | --- |
| `namespace` | `string` |
| `qualifiedName` | `string` |
| `value` | `string` |

#### Returns[#](#returns-54)

`void`

#### Inherited from[#](#inherited-from-53)

```
HTMLElement.setAttributeNS
```

* * *

### setAttributeNode()[#](#setattributenode)

```
setAttributeNode(attr): Attr;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/setAttributeNode)

#### Parameters[#](#parameters-48)

| Parameter | Type |
| --- | --- |
| `attr` | `Attr` |

#### Returns[#](#returns-55)

`Attr`

#### Inherited from[#](#inherited-from-54)

```
HTMLElement.setAttributeNode
```

* * *

### setAttributeNodeNS()[#](#setattributenodens)

```
setAttributeNodeNS(attr): Attr;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/setAttributeNodeNS)

#### Parameters[#](#parameters-49)

| Parameter | Type |
| --- | --- |
| `attr` | `Attr` |

#### Returns[#](#returns-56)

`Attr`

#### Inherited from[#](#inherited-from-55)

```
HTMLElement.setAttributeNodeNS
```

* * *

### setHTMLUnsafe()[#](#sethtmlunsafe)

```
setHTMLUnsafe(html): void;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/setHTMLUnsafe)

#### Parameters[#](#parameters-50)

| Parameter | Type |
| --- | --- |
| `html` | `string` |

#### Returns[#](#returns-57)

`void`

#### Inherited from[#](#inherited-from-56)

```
HTMLElement.setHTMLUnsafe
```

* * *

### setPointerCapture()[#](#setpointercapture)

```
setPointerCapture(pointerId): void;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/setPointerCapture)

#### Parameters[#](#parameters-51)

| Parameter | Type |
| --- | --- |
| `pointerId` | `number` |

#### Returns[#](#returns-58)

`void`

#### Inherited from[#](#inherited-from-57)

```
HTMLElement.setPointerCapture
```

* * *

### toggleAttribute()[#](#toggleattribute)

```
toggleAttribute(qualifiedName, force?): boolean;
```

If force is not given, “toggles” qualifiedName, removing it if it is present and adding it if it is not present. If force is true, adds qualifiedName. If force is false, removes qualifiedName.

Returns true if qualifiedName is now present, and false otherwise.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/toggleAttribute)

#### Parameters[#](#parameters-52)

| Parameter | Type |
| --- | --- |
| `qualifiedName` | `string` |
| `force?` | `boolean` |

#### Returns[#](#returns-59)

`boolean`

#### Inherited from[#](#inherited-from-58)

```
HTMLElement.toggleAttribute
```

* * *

### ~webkitMatchesSelector()~[#](#webkitmatchesselector)

```
webkitMatchesSelector(selectors): boolean;
```

#### Parameters[#](#parameters-53)

| Parameter | Type |
| --- | --- |
| `selectors` | `string` |

#### Returns[#](#returns-60)

`boolean`

#### Deprecated[#](#deprecated-1)

This is a legacy alias of `matches`.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/matches)

#### Inherited from[#](#inherited-from-59)

```
HTMLElement.webkitMatchesSelector
```

* * *

### dispatchEvent()[#](#dispatchevent)

```
dispatchEvent(event): boolean;
```

Dispatches a synthetic event event to target and returns true if either event’s cancelable attribute value is false or its preventDefault() method was not invoked, and false otherwise.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/EventTarget/dispatchEvent)

#### Parameters[#](#parameters-54)

| Parameter | Type |
| --- | --- |
| `event` | `Event` |

#### Returns[#](#returns-61)

`boolean`

#### Inherited from[#](#inherited-from-60)

```
HTMLElement.dispatchEvent
```

* * *

### attachInternals()[#](#attachinternals)

```
attachInternals(): ElementInternals;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/attachInternals)

#### Returns[#](#returns-62)

`ElementInternals`

#### Inherited from[#](#inherited-from-61)

```
HTMLElement.attachInternals
```

* * *

### click()[#](#click)

```
click(): void;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/click)

#### Returns[#](#returns-63)

`void`

#### Inherited from[#](#inherited-from-62)

```
HTMLElement.click
```

* * *

### hidePopover()[#](#hidepopover)

```
hidePopover(): void;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/hidePopover)

#### Returns[#](#returns-64)

`void`

#### Inherited from[#](#inherited-from-63)

```
HTMLElement.hidePopover
```

* * *

### showPopover()[#](#showpopover)

```
showPopover(): void;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/showPopover)

#### Returns[#](#returns-65)

`void`

#### Inherited from[#](#inherited-from-64)

```
HTMLElement.showPopover
```

* * *

### togglePopover()[#](#togglepopover)

```
togglePopover(force?): boolean;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/togglePopover)

#### Parameters[#](#parameters-55)

| Parameter | Type |
| --- | --- |
| `force?` | `boolean` |

#### Returns[#](#returns-66)

`boolean`

#### Inherited from[#](#inherited-from-65)

```
HTMLElement.togglePopover
```

* * *

### addEventListener()[#](#addeventlistener)

#### Call Signature[#](#call-signature-19)

```
addEventListener<K>(   type,   listener,   options?): void;
```

##### Type Parameters[#](#type-parameters-8)

| Type Parameter |
| --- |
| `K` _extends_ keyof `HTMLElementEventMap` |

##### Parameters[#](#parameters-56)

| Parameter | Type |
| --- | --- |
| `type` | `K` |
| `listener` | (`this`, `ev`) => `any` |
| `options?` | `boolean` |

##### Returns[#](#returns-67)

`void`

##### Inherited from[#](#inherited-from-66)

```
HTMLElement.addEventListener
```

#### Call Signature[#](#call-signature-20)

```
addEventListener(   type,   listener,   options?): void;
```

##### Parameters[#](#parameters-57)

| Parameter | Type |
| --- | --- |
| `type` | `string` |
| `listener` | `EventListenerOrEventListenerObject` |
| `options?` | `boolean` |

##### Returns[#](#returns-68)

`void`

##### Inherited from[#](#inherited-from-67)

```
HTMLElement.addEventListener
```

* * *

### removeEventListener()[#](#removeeventlistener)

#### Call Signature[#](#call-signature-21)

```
removeEventListener<K>(   type,   listener,   options?): void;
```

##### Type Parameters[#](#type-parameters-9)

| Type Parameter |
| --- |
| `K` _extends_ keyof `HTMLElementEventMap` |

##### Parameters[#](#parameters-58)

| Parameter | Type |
| --- | --- |
| `type` | `K` |
| `listener` | (`this`, `ev`) => `any` |
| `options?` | `boolean` |

##### Returns[#](#returns-69)

`void`

##### Inherited from[#](#inherited-from-68)

```
HTMLElement.removeEventListener
```

#### Call Signature[#](#call-signature-22)

```
removeEventListener(   type,   listener,   options?): void;
```

##### Parameters[#](#parameters-59)

| Parameter | Type |
| --- | --- |
| `type` | `string` |
| `listener` | `EventListenerOrEventListenerObject` |
| `options?` | `boolean` |

##### Returns[#](#returns-70)

`void`

##### Inherited from[#](#inherited-from-69)

```
HTMLElement.removeEventListener
```

* * *

### blur()[#](#blur)

```
blur(): void;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/blur)

#### Returns[#](#returns-71)

`void`

#### Inherited from[#](#inherited-from-70)

```
HTMLElement.blur
```

* * *

### focus()[#](#focus)

```
focus(options?): void;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/focus)

#### Parameters[#](#parameters-60)

| Parameter | Type |
| --- | --- |
| `options?` | `FocusOptions` |

#### Returns[#](#returns-72)

`void`

#### Inherited from[#](#inherited-from-71)

```
HTMLElement.focus
```

* * *

### appendChild()[#](#appendchild)

```
appendChild<T>(node): T;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/appendChild)

#### Type Parameters[#](#type-parameters-10)

| Type Parameter |
| --- |
| `T` _extends_ `Node` |

#### Parameters[#](#parameters-61)

| Parameter | Type |
| --- | --- |
| `node` | `T` |

#### Returns[#](#returns-73)

`T`

#### Inherited from[#](#inherited-from-72)

```
HTMLElement.appendChild
```

* * *

### cloneNode()[#](#clonenode)

```
cloneNode(deep?): Node;
```

Returns a copy of node. If deep is true, the copy also includes the node’s descendants.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/cloneNode)

#### Parameters[#](#parameters-62)

| Parameter | Type |
| --- | --- |
| `deep?` | `boolean` |

#### Returns[#](#returns-74)

`Node`

#### Inherited from[#](#inherited-from-73)

```
HTMLElement.cloneNode
```

* * *

### compareDocumentPosition()[#](#comparedocumentposition)

```
compareDocumentPosition(other): number;
```

Returns a bitmask indicating the position of other relative to node.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/compareDocumentPosition)

#### Parameters[#](#parameters-63)

| Parameter | Type |
| --- | --- |
| `other` | `Node` |

#### Returns[#](#returns-75)

`number`

#### Inherited from[#](#inherited-from-74)

```
HTMLElement.compareDocumentPosition
```

* * *

### contains()[#](#contains)

```
contains(other): boolean;
```

Returns true if other is an inclusive descendant of node, and false otherwise.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/contains)

#### Parameters[#](#parameters-64)

| Parameter | Type |
| --- | --- |
| `other` | `Node` |

#### Returns[#](#returns-76)

`boolean`

#### Inherited from[#](#inherited-from-75)

```
HTMLElement.contains
```

* * *

### getRootNode()[#](#getrootnode)

```
getRootNode(options?): Node;
```

Returns node’s root.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/getRootNode)

#### Parameters[#](#parameters-65)

| Parameter | Type |
| --- | --- |
| `options?` | `GetRootNodeOptions` |

#### Returns[#](#returns-77)

`Node`

#### Inherited from[#](#inherited-from-76)

```
HTMLElement.getRootNode
```

* * *

### hasChildNodes()[#](#haschildnodes)

```
hasChildNodes(): boolean;
```

Returns whether node has children.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/hasChildNodes)

#### Returns[#](#returns-78)

`boolean`

#### Inherited from[#](#inherited-from-77)

```
HTMLElement.hasChildNodes
```

* * *

### insertBefore()[#](#insertbefore)

```
insertBefore<T>(node, child): T;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/insertBefore)

#### Type Parameters[#](#type-parameters-11)

| Type Parameter |
| --- |
| `T` _extends_ `Node` |

#### Parameters[#](#parameters-66)

| Parameter | Type |
| --- | --- |
| `node` | `T` |
| `child` | `Node` |

#### Returns[#](#returns-79)

`T`

#### Inherited from[#](#inherited-from-78)

```
HTMLElement.insertBefore
```

* * *

### isDefaultNamespace()[#](#isdefaultnamespace)

```
isDefaultNamespace(namespace): boolean;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/isDefaultNamespace)

#### Parameters[#](#parameters-67)

| Parameter | Type |
| --- | --- |
| `namespace` | `string` |

#### Returns[#](#returns-80)

`boolean`

#### Inherited from[#](#inherited-from-79)

```
HTMLElement.isDefaultNamespace
```

* * *

### isEqualNode()[#](#isequalnode)

```
isEqualNode(otherNode): boolean;
```

Returns whether node and otherNode have the same properties.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/isEqualNode)

#### Parameters[#](#parameters-68)

| Parameter | Type |
| --- | --- |
| `otherNode` | `Node` |

#### Returns[#](#returns-81)

`boolean`

#### Inherited from[#](#inherited-from-80)

```
HTMLElement.isEqualNode
```

* * *

### isSameNode()[#](#issamenode)

```
isSameNode(otherNode): boolean;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/isSameNode)

#### Parameters[#](#parameters-69)

| Parameter | Type |
| --- | --- |
| `otherNode` | `Node` |

#### Returns[#](#returns-82)

`boolean`

#### Inherited from[#](#inherited-from-81)

```
HTMLElement.isSameNode
```

* * *

### lookupNamespaceURI()[#](#lookupnamespaceuri)

```
lookupNamespaceURI(prefix): string;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/lookupNamespaceURI)

#### Parameters[#](#parameters-70)

| Parameter | Type |
| --- | --- |
| `prefix` | `string` |

#### Returns[#](#returns-83)

`string`

#### Inherited from[#](#inherited-from-82)

```
HTMLElement.lookupNamespaceURI
```

* * *

### lookupPrefix()[#](#lookupprefix)

```
lookupPrefix(namespace): string;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/lookupPrefix)

#### Parameters[#](#parameters-71)

| Parameter | Type |
| --- | --- |
| `namespace` | `string` |

#### Returns[#](#returns-84)

`string`

#### Inherited from[#](#inherited-from-83)

```
HTMLElement.lookupPrefix
```

* * *

### normalize()[#](#normalize)

```
normalize(): void;
```

Removes empty exclusive Text nodes and concatenates the data of remaining contiguous exclusive Text nodes into the first of their nodes.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/normalize)

#### Returns[#](#returns-85)

`void`

#### Inherited from[#](#inherited-from-84)

```
HTMLElement.normalize
```

* * *

### removeChild()[#](#removechild)

```
removeChild<T>(child): T;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/removeChild)

#### Type Parameters[#](#type-parameters-12)

| Type Parameter |
| --- |
| `T` _extends_ `Node` |

#### Parameters[#](#parameters-72)

| Parameter | Type |
| --- | --- |
| `child` | `T` |

#### Returns[#](#returns-86)

`T`

#### Inherited from[#](#inherited-from-85)

```
HTMLElement.removeChild
```

* * *

### replaceChild()[#](#replacechild)

```
replaceChild<T>(node, child): T;
```

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/replaceChild)

#### Type Parameters[#](#type-parameters-13)

| Type Parameter |
| --- |
| `T` _extends_ `Node` |

#### Parameters[#](#parameters-73)

| Parameter | Type |
| --- | --- |
| `node` | `Node` |
| `child` | `T` |

#### Returns[#](#returns-87)

`T`

#### Inherited from[#](#inherited-from-86)

```
HTMLElement.replaceChild
```

* * *

### append()[#](#append)

```
append(...nodes): void;
```

Inserts nodes after the last child of node, while replacing strings in nodes with equivalent Text nodes.

Throws a “HierarchyRequestError” DOMException if the constraints of the node tree are violated.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Document/append)

#### Parameters[#](#parameters-74)

| Parameter | Type |
| --- | --- |
| …`nodes` | (`string` |

#### Returns[#](#returns-88)

`void`

#### Inherited from[#](#inherited-from-87)

```
HTMLElement.append
```

* * *

### prepend()[#](#prepend)

```
prepend(...nodes): void;
```

Inserts nodes before the first child of node, while replacing strings in nodes with equivalent Text nodes.

Throws a “HierarchyRequestError” DOMException if the constraints of the node tree are violated.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Document/prepend)

#### Parameters[#](#parameters-75)

| Parameter | Type |
| --- | --- |
| …`nodes` | (`string` |

#### Returns[#](#returns-89)

`void`

#### Inherited from[#](#inherited-from-88)

```
HTMLElement.prepend
```

* * *

### querySelector()[#](#queryselector)

#### Call Signature[#](#call-signature-23)

```
querySelector<K>(selectors): HTMLElementTagNameMap[K];
```

Returns the first element that is a descendant of node that matches selectors.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Document/querySelector)

##### Type Parameters[#](#type-parameters-14)

| Type Parameter |
| --- |
| `K` _extends_ keyof `HTMLElementTagNameMap` |

##### Parameters[#](#parameters-76)

| Parameter | Type |
| --- | --- |
| `selectors` | `K` |

##### Returns[#](#returns-90)

`HTMLElementTagNameMap`\[`K`\]

##### Inherited from[#](#inherited-from-89)

```
HTMLElement.querySelector
```

#### Call Signature[#](#call-signature-24)

```
querySelector<K>(selectors): SVGElementTagNameMap[K];
```

##### Type Parameters[#](#type-parameters-15)

| Type Parameter |
| --- |
| `K` _extends_ keyof `SVGElementTagNameMap` |

##### Parameters[#](#parameters-77)

| Parameter | Type |
| --- | --- |
| `selectors` | `K` |

##### Returns[#](#returns-91)

`SVGElementTagNameMap`\[`K`\]

##### Inherited from[#](#inherited-from-90)

```
HTMLElement.querySelector
```

#### Call Signature[#](#call-signature-25)

```
querySelector<K>(selectors): MathMLElementTagNameMap[K];
```

##### Type Parameters[#](#type-parameters-16)

| Type Parameter |
| --- |
| `K` _extends_ keyof `MathMLElementTagNameMap` |

##### Parameters[#](#parameters-78)

| Parameter | Type |
| --- | --- |
| `selectors` | `K` |

##### Returns[#](#returns-92)

`MathMLElementTagNameMap`\[`K`\]

##### Inherited from[#](#inherited-from-91)

```
HTMLElement.querySelector
```

#### Call Signature[#](#call-signature-26)

```
querySelector<K>(selectors): HTMLElementDeprecatedTagNameMap[K];
```

##### Type Parameters[#](#type-parameters-17)

| Type Parameter |
| --- |
| `K` _extends_ keyof `HTMLElementDeprecatedTagNameMap` |

##### Parameters[#](#parameters-79)

| Parameter | Type |
| --- | --- |
| `selectors` | `K` |

##### Returns[#](#returns-93)

`HTMLElementDeprecatedTagNameMap`\[`K`\]

##### Deprecated[#](#deprecated-2)

##### Inherited from[#](#inherited-from-92)

```
HTMLElement.querySelector
```

#### Call Signature[#](#call-signature-27)

```
querySelector<E>(selectors): E;
```

##### Type Parameters[#](#type-parameters-18)

| Type Parameter | Default type |
| --- | --- |
| `E` _extends_ `Element` | `Element` |

##### Parameters[#](#parameters-80)

| Parameter | Type |
| --- | --- |
| `selectors` | `string` |

##### Returns[#](#returns-94)

`E`

##### Inherited from[#](#inherited-from-93)

```
HTMLElement.querySelector
```

* * *

### querySelectorAll()[#](#queryselectorall)

#### Call Signature[#](#call-signature-28)

```
querySelectorAll<K>(selectors): NodeListOf<HTMLElementTagNameMap[K]>;
```

Returns all element descendants of node that match selectors.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Document/querySelectorAll)

##### Type Parameters[#](#type-parameters-19)

| Type Parameter |
| --- |
| `K` _extends_ keyof `HTMLElementTagNameMap` |

##### Parameters[#](#parameters-81)

| Parameter | Type |
| --- | --- |
| `selectors` | `K` |

##### Returns[#](#returns-95)

`NodeListOf`<`HTMLElementTagNameMap`\[`K`\]>

##### Inherited from[#](#inherited-from-94)

```
HTMLElement.querySelectorAll
```

#### Call Signature[#](#call-signature-29)

```
querySelectorAll<K>(selectors): NodeListOf<SVGElementTagNameMap[K]>;
```

##### Type Parameters[#](#type-parameters-20)

| Type Parameter |
| --- |
| `K` _extends_ keyof `SVGElementTagNameMap` |

##### Parameters[#](#parameters-82)

| Parameter | Type |
| --- | --- |
| `selectors` | `K` |

##### Returns[#](#returns-96)

`NodeListOf`<`SVGElementTagNameMap`\[`K`\]>

##### Inherited from[#](#inherited-from-95)

```
HTMLElement.querySelectorAll
```

#### Call Signature[#](#call-signature-30)

```
querySelectorAll<K>(selectors): NodeListOf<MathMLElementTagNameMap[K]>;
```

##### Type Parameters[#](#type-parameters-21)

| Type Parameter |
| --- |
| `K` _extends_ keyof `MathMLElementTagNameMap` |

##### Parameters[#](#parameters-83)

| Parameter | Type |
| --- | --- |
| `selectors` | `K` |

##### Returns[#](#returns-97)

`NodeListOf`<`MathMLElementTagNameMap`\[`K`\]>

##### Inherited from[#](#inherited-from-96)

```
HTMLElement.querySelectorAll
```

#### Call Signature[#](#call-signature-31)

```
querySelectorAll<K>(selectors): NodeListOf<HTMLElementDeprecatedTagNameMap[K]>;
```

##### Type Parameters[#](#type-parameters-22)

| Type Parameter |
| --- |
| `K` _extends_ keyof `HTMLElementDeprecatedTagNameMap` |

##### Parameters[#](#parameters-84)

| Parameter | Type |
| --- | --- |
| `selectors` | `K` |

##### Returns[#](#returns-98)

`NodeListOf`<`HTMLElementDeprecatedTagNameMap`\[`K`\]>

##### Deprecated[#](#deprecated-3)

##### Inherited from[#](#inherited-from-97)

```
HTMLElement.querySelectorAll
```

#### Call Signature[#](#call-signature-32)

```
querySelectorAll<E>(selectors): NodeListOf<E>;
```

##### Type Parameters[#](#type-parameters-23)

| Type Parameter | Default type |
| --- | --- |
| `E` _extends_ `Element` | `Element` |

##### Parameters[#](#parameters-85)

| Parameter | Type |
| --- | --- |
| `selectors` | `string` |

##### Returns[#](#returns-99)

`NodeListOf`<`E`\>

##### Inherited from[#](#inherited-from-98)

```
HTMLElement.querySelectorAll
```

* * *

### replaceChildren()[#](#replacechildren)

```
replaceChildren(...nodes): void;
```

Replace all children of node with nodes, while replacing strings in nodes with equivalent Text nodes.

Throws a “HierarchyRequestError” DOMException if the constraints of the node tree are violated.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Document/replaceChildren)

#### Parameters[#](#parameters-86)

| Parameter | Type |
| --- | --- |
| …`nodes` | (`string` |

#### Returns[#](#returns-100)

`void`

#### Inherited from[#](#inherited-from-99)

```
HTMLElement.replaceChildren
```

## Properties[#](#properties)

| Property | Modifier | Type | Description | Inherited from |
| --- | --- | --- | --- | --- |
| `ariaAtomic` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaAtomic) | `HTMLElement.ariaAtomic` |
| `ariaAutoComplete` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaAutoComplete) | `HTMLElement.ariaAutoComplete` |
| `ariaBrailleLabel` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaBrailleLabel) | `HTMLElement.ariaBrailleLabel` |
| `ariaBrailleRoleDescription` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaBrailleRoleDescription) | `HTMLElement.ariaBrailleRoleDescription` |
| `ariaBusy` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaBusy) | `HTMLElement.ariaBusy` |
| `ariaChecked` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaChecked) | `HTMLElement.ariaChecked` |
| `ariaColCount` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaColCount) | `HTMLElement.ariaColCount` |
| `ariaColIndex` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaColIndex) | `HTMLElement.ariaColIndex` |
| `ariaColSpan` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaColSpan) | `HTMLElement.ariaColSpan` |
| `ariaCurrent` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaCurrent) | `HTMLElement.ariaCurrent` |
| `ariaDescription` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaDescription) | `HTMLElement.ariaDescription` |
| `ariaDisabled` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaDisabled) | `HTMLElement.ariaDisabled` |
| `ariaExpanded` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaExpanded) | `HTMLElement.ariaExpanded` |
| `ariaHasPopup` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaHasPopup) | `HTMLElement.ariaHasPopup` |
| `ariaHidden` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaHidden) | `HTMLElement.ariaHidden` |
| `ariaInvalid` | `public` | `string` | \- | `HTMLElement.ariaInvalid` |
| `ariaKeyShortcuts` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaKeyShortcuts) | `HTMLElement.ariaKeyShortcuts` |
| `ariaLabel` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaLabel) | `HTMLElement.ariaLabel` |
| `ariaLevel` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaLevel) | `HTMLElement.ariaLevel` |
| `ariaLive` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaLive) | `HTMLElement.ariaLive` |
| `ariaModal` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaModal) | `HTMLElement.ariaModal` |
| `ariaMultiLine` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaMultiLine) | `HTMLElement.ariaMultiLine` |
| `ariaMultiSelectable` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaMultiSelectable) | `HTMLElement.ariaMultiSelectable` |
| `ariaOrientation` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaOrientation) | `HTMLElement.ariaOrientation` |
| `ariaPlaceholder` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaPlaceholder) | `HTMLElement.ariaPlaceholder` |
| `ariaPosInSet` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaPosInSet) | `HTMLElement.ariaPosInSet` |
| `ariaPressed` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaPressed) | `HTMLElement.ariaPressed` |
| `ariaReadOnly` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaReadOnly) | `HTMLElement.ariaReadOnly` |
| `ariaRequired` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaRequired) | `HTMLElement.ariaRequired` |
| `ariaRoleDescription` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaRoleDescription) | `HTMLElement.ariaRoleDescription` |
| `ariaRowCount` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaRowCount) | `HTMLElement.ariaRowCount` |
| `ariaRowIndex` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaRowIndex) | `HTMLElement.ariaRowIndex` |
| `ariaRowSpan` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaRowSpan) | `HTMLElement.ariaRowSpan` |
| `ariaSelected` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaSelected) | `HTMLElement.ariaSelected` |
| `ariaSetSize` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaSetSize) | `HTMLElement.ariaSetSize` |
| `ariaSort` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaSort) | `HTMLElement.ariaSort` |
| `ariaValueMax` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaValueMax) | `HTMLElement.ariaValueMax` |
| `ariaValueMin` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaValueMin) | `HTMLElement.ariaValueMin` |
| `ariaValueNow` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaValueNow) | `HTMLElement.ariaValueNow` |
| `ariaValueText` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaValueText) | `HTMLElement.ariaValueText` |
| `role` | `public` | `string` | \- | `HTMLElement.role` |
| `attributes` | `readonly` | `NamedNodeMap` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/attributes) | `HTMLElement.attributes` |
| `classList` | `readonly` | `DOMTokenList` | Allows for manipulation of element’s class content attribute as a set of whitespace-separated tokens through a DOMTokenList object. [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/classList) | `HTMLElement.classList` |
| `className` | `public` | `string` | Returns the value of element’s class content attribute. Can be set to change it. [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/className) | `HTMLElement.className` |
| `clientHeight` | `readonly` | `number` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/clientHeight) | `HTMLElement.clientHeight` |
| `clientLeft` | `readonly` | `number` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/clientLeft) | `HTMLElement.clientLeft` |
| `clientTop` | `readonly` | `number` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/clientTop) | `HTMLElement.clientTop` |
| `clientWidth` | `readonly` | `number` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/clientWidth) | `HTMLElement.clientWidth` |
| `id` | `public` | `string` | Returns the value of element’s id content attribute. Can be set to change it. [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/id) | `HTMLElement.id` |
| `innerHTML` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/innerHTML) | `HTMLElement.innerHTML` |
| `localName` | `readonly` | `string` | Returns the local name. [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/localName) | `HTMLElement.localName` |
| `namespaceURI` | `readonly` | `string` | Returns the namespace. [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/namespaceURI) | `HTMLElement.namespaceURI` |
| `onfullscreenchange` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/fullscreenchange_event) | `HTMLElement.onfullscreenchange` |
| `onfullscreenerror` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/fullscreenerror_event) | `HTMLElement.onfullscreenerror` |
| `outerHTML` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/outerHTML) | `HTMLElement.outerHTML` |
| `ownerDocument` | `readonly` | `Document` | Returns the node document. Returns null for documents. [MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/ownerDocument) | `HTMLElement.ownerDocument` |
| `part` | `readonly` | `DOMTokenList` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/part) | `HTMLElement.part` |
| `prefix` | `readonly` | `string` | Returns the namespace prefix. [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/prefix) | `HTMLElement.prefix` |
| `scrollHeight` | `readonly` | `number` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/scrollHeight) | `HTMLElement.scrollHeight` |
| `scrollLeft` | `public` | `number` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/scrollLeft) | `HTMLElement.scrollLeft` |
| `scrollTop` | `public` | `number` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/scrollTop) | `HTMLElement.scrollTop` |
| `scrollWidth` | `readonly` | `number` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/scrollWidth) | `HTMLElement.scrollWidth` |
| `shadowRoot` | `readonly` | `ShadowRoot` | Returns element’s shadow root, if any, and if shadow root’s mode is “open”, and null otherwise. [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/shadowRoot) | `HTMLElement.shadowRoot` |
| `slot` | `public` | `string` | Returns the value of element’s slot content attribute. Can be set to change it. [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/slot) | `HTMLElement.slot` |
| `tagName` | `readonly` | `string` | Returns the HTML-uppercased qualified name. [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/tagName) | `HTMLElement.tagName` |
| `attributeStyleMap` | `readonly` | `StylePropertyMap` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/attributeStyleMap) | `HTMLElement.attributeStyleMap` |
| `style` | `readonly` | `CSSStyleDeclaration` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/style) | `HTMLElement.style` |
| `contentEditable` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/contentEditable) | `HTMLElement.contentEditable` |
| `enterKeyHint` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/enterKeyHint) | `HTMLElement.enterKeyHint` |
| `inputMode` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/inputMode) | `HTMLElement.inputMode` |
| `isContentEditable` | `readonly` | `boolean` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/isContentEditable) | `HTMLElement.isContentEditable` |
| `onabort` | `public` | (`this`, `ev`) => `any` | Fires when the user aborts the download. | `HTMLElement.onabort` |
| `onanimationcancel` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/animationcancel_event) | `HTMLElement.onanimationcancel` |
| `onanimationend` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/animationend_event) | `HTMLElement.onanimationend` |
| `onanimationiteration` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/animationiteration_event) | `HTMLElement.onanimationiteration` |
| `onanimationstart` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/animationstart_event) | `HTMLElement.onanimationstart` |
| `onauxclick` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/auxclick_event) | `HTMLElement.onauxclick` |
| `onbeforeinput` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/beforeinput_event) | `HTMLElement.onbeforeinput` |
| `onbeforetoggle` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/beforetoggle_event) | `HTMLElement.onbeforetoggle` |
| `onblur` | `public` | (`this`, `ev`) => `any` | Fires when the object loses the input focus. | `HTMLElement.onblur` |
| `oncancel` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/cancel_event) | `HTMLElement.oncancel` |
| `oncanplay` | `public` | (`this`, `ev`) => `any` | Occurs when playback is possible, but would require further buffering. | `HTMLElement.oncanplay` |
| `oncanplaythrough` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLMediaElement/canplaythrough_event) | `HTMLElement.oncanplaythrough` |
| `onchange` | `public` | (`this`, `ev`) => `any` | Fires when the contents of the object or selection have changed. | `HTMLElement.onchange` |
| `onclick` | `public` | (`this`, `ev`) => `any` | Fires when the user clicks the left mouse button on the object | `HTMLElement.onclick` |
| `onclose` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLDialogElement/close_event) | `HTMLElement.onclose` |
| `oncontextlost` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLCanvasElement/webglcontextlost_event) | `HTMLElement.oncontextlost` |
| `oncontextmenu` | `public` | (`this`, `ev`) => `any` | Fires when the user clicks the right mouse button in the client area, opening the context menu. | `HTMLElement.oncontextmenu` |
| `oncontextrestored` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLCanvasElement/contextrestored_event) | `HTMLElement.oncontextrestored` |
| `oncopy` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/copy_event) | `HTMLElement.oncopy` |
| `oncuechange` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLTrackElement/cuechange_event) | `HTMLElement.oncuechange` |
| `oncut` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/cut_event) | `HTMLElement.oncut` |
| `ondblclick` | `public` | (`this`, `ev`) => `any` | Fires when the user double-clicks the object. | `HTMLElement.ondblclick` |
| `ondrag` | `public` | (`this`, `ev`) => `any` | Fires on the source object continuously during a drag operation. | `HTMLElement.ondrag` |
| `ondragend` | `public` | (`this`, `ev`) => `any` | Fires on the source object when the user releases the mouse at the close of a drag operation. | `HTMLElement.ondragend` |
| `ondragenter` | `public` | (`this`, `ev`) => `any` | Fires on the target element when the user drags the object to a valid drop target. | `HTMLElement.ondragenter` |
| `ondragleave` | `public` | (`this`, `ev`) => `any` | Fires on the target object when the user moves the mouse out of a valid drop target during a drag operation. | `HTMLElement.ondragleave` |
| `ondragover` | `public` | (`this`, `ev`) => `any` | Fires on the target element continuously while the user drags the object over a valid drop target. | `HTMLElement.ondragover` |
| `ondragstart` | `public` | (`this`, `ev`) => `any` | Fires on the source object when the user starts to drag a text selection or selected object. | `HTMLElement.ondragstart` |
| `ondrop` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/drop_event) | `HTMLElement.ondrop` |
| `ondurationchange` | `public` | (`this`, `ev`) => `any` | Occurs when the duration attribute is updated. | `HTMLElement.ondurationchange` |
| `onemptied` | `public` | (`this`, `ev`) => `any` | Occurs when the media element is reset to its initial state. | `HTMLElement.onemptied` |
| `onended` | `public` | (`this`, `ev`) => `any` | Occurs when the end of playback is reached. | `HTMLElement.onended` |
| `onerror` | `public` | `OnErrorEventHandlerNonNull` | Fires when an error occurs during object loading. **Param** The event. [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/error_event) | `HTMLElement.onerror` |
| `onfocus` | `public` | (`this`, `ev`) => `any` | Fires when the object receives focus. | `HTMLElement.onfocus` |
| `onformdata` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLFormElement/formdata_event) | `HTMLElement.onformdata` |
| `ongotpointercapture` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/gotpointercapture_event) | `HTMLElement.ongotpointercapture` |
| `oninput` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/input_event) | `HTMLElement.oninput` |
| `oninvalid` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLInputElement/invalid_event) | `HTMLElement.oninvalid` |
| `onkeydown` | `public` | (`this`, `ev`) => `any` | Fires when the user presses a key. | `HTMLElement.onkeydown` |
| ~`onkeypress`~ | `public` | (`this`, `ev`) => `any` | Fires when the user presses an alphanumeric key. **Deprecated** [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/keypress_event) | `HTMLElement.onkeypress` |
| `onkeyup` | `public` | (`this`, `ev`) => `any` | Fires when the user releases a key. | `HTMLElement.onkeyup` |
| `onload` | `public` | (`this`, `ev`) => `any` | Fires immediately after the browser loads the object. | `HTMLElement.onload` |
| `onloadeddata` | `public` | (`this`, `ev`) => `any` | Occurs when media data is loaded at the current playback position. | `HTMLElement.onloadeddata` |
| `onloadedmetadata` | `public` | (`this`, `ev`) => `any` | Occurs when the duration and dimensions of the media have been determined. | `HTMLElement.onloadedmetadata` |
| `onloadstart` | `public` | (`this`, `ev`) => `any` | Occurs when Internet Explorer begins looking for media data. | `HTMLElement.onloadstart` |
| `onlostpointercapture` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/lostpointercapture_event) | `HTMLElement.onlostpointercapture` |
| `onmousedown` | `public` | (`this`, `ev`) => `any` | Fires when the user clicks the object with either mouse button. | `HTMLElement.onmousedown` |
| `onmouseenter` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/mouseenter_event) | `HTMLElement.onmouseenter` |
| `onmouseleave` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/mouseleave_event) | `HTMLElement.onmouseleave` |
| `onmousemove` | `public` | (`this`, `ev`) => `any` | Fires when the user moves the mouse over the object. | `HTMLElement.onmousemove` |
| `onmouseout` | `public` | (`this`, `ev`) => `any` | Fires when the user moves the mouse pointer outside the boundaries of the object. | `HTMLElement.onmouseout` |
| `onmouseover` | `public` | (`this`, `ev`) => `any` | Fires when the user moves the mouse pointer into the object. | `HTMLElement.onmouseover` |
| `onmouseup` | `public` | (`this`, `ev`) => `any` | Fires when the user releases a mouse button while the mouse is over the object. | `HTMLElement.onmouseup` |
| `onpaste` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/paste_event) | `HTMLElement.onpaste` |
| `onpause` | `public` | (`this`, `ev`) => `any` | Occurs when playback is paused. | `HTMLElement.onpause` |
| `onplay` | `public` | (`this`, `ev`) => `any` | Occurs when the play method is requested. | `HTMLElement.onplay` |
| `onplaying` | `public` | (`this`, `ev`) => `any` | Occurs when the audio or video has started playing. | `HTMLElement.onplaying` |
| `onpointercancel` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/pointercancel_event) | `HTMLElement.onpointercancel` |
| `onpointerdown` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/pointerdown_event) | `HTMLElement.onpointerdown` |
| `onpointerenter` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/pointerenter_event) | `HTMLElement.onpointerenter` |
| `onpointerleave` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/pointerleave_event) | `HTMLElement.onpointerleave` |
| `onpointermove` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/pointermove_event) | `HTMLElement.onpointermove` |
| `onpointerout` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/pointerout_event) | `HTMLElement.onpointerout` |
| `onpointerover` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/pointerover_event) | `HTMLElement.onpointerover` |
| `onpointerup` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/pointerup_event) | `HTMLElement.onpointerup` |
| `onprogress` | `public` | (`this`, `ev`) => `any` | Occurs to indicate progress while downloading media data. | `HTMLElement.onprogress` |
| `onratechange` | `public` | (`this`, `ev`) => `any` | Occurs when the playback rate is increased or decreased. | `HTMLElement.onratechange` |
| `onreset` | `public` | (`this`, `ev`) => `any` | Fires when the user resets a form. | `HTMLElement.onreset` |
| `onresize` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLVideoElement/resize_event) | `HTMLElement.onresize` |
| `onscroll` | `public` | (`this`, `ev`) => `any` | Fires when the user repositions the scroll box in the scroll bar on the object. | `HTMLElement.onscroll` |
| `onscrollend` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Document/scrollend_event) | `HTMLElement.onscrollend` |
| `onsecuritypolicyviolation` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Document/securitypolicyviolation_event) | `HTMLElement.onsecuritypolicyviolation` |
| `onseeked` | `public` | (`this`, `ev`) => `any` | Occurs when the seek operation ends. | `HTMLElement.onseeked` |
| `onseeking` | `public` | (`this`, `ev`) => `any` | Occurs when the current playback position is moved. | `HTMLElement.onseeking` |
| `onselect` | `public` | (`this`, `ev`) => `any` | Fires when the current selection changes. | `HTMLElement.onselect` |
| `onselectionchange` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Document/selectionchange_event) | `HTMLElement.onselectionchange` |
| `onselectstart` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/selectstart_event) | `HTMLElement.onselectstart` |
| `onslotchange` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLSlotElement/slotchange_event) | `HTMLElement.onslotchange` |
| `onstalled` | `public` | (`this`, `ev`) => `any` | Occurs when the download has stopped. | `HTMLElement.onstalled` |
| `onsubmit` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLFormElement/submit_event) | `HTMLElement.onsubmit` |
| `onsuspend` | `public` | (`this`, `ev`) => `any` | Occurs if the load operation has been intentionally halted. | `HTMLElement.onsuspend` |
| `ontimeupdate` | `public` | (`this`, `ev`) => `any` | Occurs to indicate the current playback position. | `HTMLElement.ontimeupdate` |
| `ontoggle` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLDetailsElement/toggle_event) | `HTMLElement.ontoggle` |
| `ontouchcancel?` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/touchcancel_event) | `HTMLElement.ontouchcancel` |
| `ontouchend?` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/touchend_event) | `HTMLElement.ontouchend` |
| `ontouchmove?` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/touchmove_event) | `HTMLElement.ontouchmove` |
| `ontouchstart?` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/touchstart_event) | `HTMLElement.ontouchstart` |
| `ontransitioncancel` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/transitioncancel_event) | `HTMLElement.ontransitioncancel` |
| `ontransitionend` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/transitionend_event) | `HTMLElement.ontransitionend` |
| `ontransitionrun` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/transitionrun_event) | `HTMLElement.ontransitionrun` |
| `ontransitionstart` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/transitionstart_event) | `HTMLElement.ontransitionstart` |
| `onvolumechange` | `public` | (`this`, `ev`) => `any` | Occurs when the volume is changed, or playback is muted or unmuted. | `HTMLElement.onvolumechange` |
| `onwaiting` | `public` | (`this`, `ev`) => `any` | Occurs when playback stops because the next frame of a video resource is not available. | `HTMLElement.onwaiting` |
| ~`onwebkitanimationend`~ | `public` | (`this`, `ev`) => `any` | **Deprecated** This is a legacy alias of `onanimationend`. [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/animationend_event) | `HTMLElement.onwebkitanimationend` |
| ~`onwebkitanimationiteration`~ | `public` | (`this`, `ev`) => `any` | **Deprecated** This is a legacy alias of `onanimationiteration`. [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/animationiteration_event) | `HTMLElement.onwebkitanimationiteration` |
| ~`onwebkitanimationstart`~ | `public` | (`this`, `ev`) => `any` | **Deprecated** This is a legacy alias of `onanimationstart`. [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/animationstart_event) | `HTMLElement.onwebkitanimationstart` |
| ~`onwebkittransitionend`~ | `public` | (`this`, `ev`) => `any` | **Deprecated** This is a legacy alias of `ontransitionend`. [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/transitionend_event) | `HTMLElement.onwebkittransitionend` |
| `onwheel` | `public` | (`this`, `ev`) => `any` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/wheel_event) | `HTMLElement.onwheel` |
| `accessKey` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/accessKey) | `HTMLElement.accessKey` |
| `accessKeyLabel` | `readonly` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/accessKeyLabel) | `HTMLElement.accessKeyLabel` |
| `autocapitalize` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/autocapitalize) | `HTMLElement.autocapitalize` |
| `dir` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/dir) | `HTMLElement.dir` |
| `draggable` | `public` | `boolean` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/draggable) | `HTMLElement.draggable` |
| `hidden` | `public` | `boolean` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/hidden) | `HTMLElement.hidden` |
| `inert` | `public` | `boolean` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/inert) | `HTMLElement.inert` |
| `innerText` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/innerText) | `HTMLElement.innerText` |
| `lang` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/lang) | `HTMLElement.lang` |
| `offsetHeight` | `readonly` | `number` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/offsetHeight) | `HTMLElement.offsetHeight` |
| `offsetLeft` | `readonly` | `number` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/offsetLeft) | `HTMLElement.offsetLeft` |
| `offsetParent` | `readonly` | `Element` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/offsetParent) | `HTMLElement.offsetParent` |
| `offsetTop` | `readonly` | `number` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/offsetTop) | `HTMLElement.offsetTop` |
| `offsetWidth` | `readonly` | `number` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/offsetWidth) | `HTMLElement.offsetWidth` |
| `outerText` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/outerText) | `HTMLElement.outerText` |
| `popover` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/popover) | `HTMLElement.popover` |
| `spellcheck` | `public` | `boolean` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/spellcheck) | `HTMLElement.spellcheck` |
| `title` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/title) | `HTMLElement.title` |
| `translate` | `public` | `boolean` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/translate) | `HTMLElement.translate` |
| `autofocus` | `public` | `boolean` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/autofocus) | `HTMLElement.autofocus` |
| `dataset` | `readonly` | `DOMStringMap` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/dataset) | `HTMLElement.dataset` |
| `nonce?` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/nonce) | `HTMLElement.nonce` |
| `tabIndex` | `public` | `number` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/tabIndex) | `HTMLElement.tabIndex` |
| `baseURI` | `readonly` | `string` | Returns node’s node document’s document base URL. [MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/baseURI) | `HTMLElement.baseURI` |
| `childNodes` | `readonly` | `NodeListOf`<`ChildNode`\> | Returns the children. [MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/childNodes) | `HTMLElement.childNodes` |
| `firstChild` | `readonly` | `ChildNode` | Returns the first child. [MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/firstChild) | `HTMLElement.firstChild` |
| `isConnected` | `readonly` | `boolean` | Returns true if node is connected and false otherwise. [MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/isConnected) | `HTMLElement.isConnected` |
| `lastChild` | `readonly` | `ChildNode` | Returns the last child. [MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/lastChild) | `HTMLElement.lastChild` |
| `nextSibling` | `readonly` | `ChildNode` | Returns the next sibling. [MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/nextSibling) | `HTMLElement.nextSibling` |
| `nodeName` | `readonly` | `string` | Returns a string appropriate for the type of node. [MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/nodeName) | `HTMLElement.nodeName` |
| `nodeType` | `readonly` | `number` | Returns the type of node. [MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/nodeType) | `HTMLElement.nodeType` |
| `nodeValue` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/nodeValue) | `HTMLElement.nodeValue` |
| `parentElement` | `readonly` | `HTMLElement` | Returns the parent element. [MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/parentElement) | `HTMLElement.parentElement` |
| `parentNode` | `readonly` | `ParentNode` | Returns the parent. [MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/parentNode) | `HTMLElement.parentNode` |
| `previousSibling` | `readonly` | `ChildNode` | Returns the previous sibling. [MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/previousSibling) | `HTMLElement.previousSibling` |
| `textContent` | `public` | `string` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/textContent) | `HTMLElement.textContent` |
| `ELEMENT_NODE` | `readonly` | `1` | node is an element. | `HTMLElement.ELEMENT_NODE` |
| `ATTRIBUTE_NODE` | `readonly` | `2` | \- | `HTMLElement.ATTRIBUTE_NODE` |
| `TEXT_NODE` | `readonly` | `3` | node is a Text node. | `HTMLElement.TEXT_NODE` |
| `CDATA_SECTION_NODE` | `readonly` | `4` | node is a CDATASection node. | `HTMLElement.CDATA_SECTION_NODE` |
| `ENTITY_REFERENCE_NODE` | `readonly` | `5` | \- | `HTMLElement.ENTITY_REFERENCE_NODE` |
| `ENTITY_NODE` | `readonly` | `6` | \- | `HTMLElement.ENTITY_NODE` |
| `PROCESSING_INSTRUCTION_NODE` | `readonly` | `7` | node is a ProcessingInstruction node. | `HTMLElement.PROCESSING_INSTRUCTION_NODE` |
| `COMMENT_NODE` | `readonly` | `8` | node is a Comment node. | `HTMLElement.COMMENT_NODE` |
| `DOCUMENT_NODE` | `readonly` | `9` | node is a document. | `HTMLElement.DOCUMENT_NODE` |
| `DOCUMENT_TYPE_NODE` | `readonly` | `10` | node is a doctype. | `HTMLElement.DOCUMENT_TYPE_NODE` |
| `DOCUMENT_FRAGMENT_NODE` | `readonly` | `11` | node is a DocumentFragment node. | `HTMLElement.DOCUMENT_FRAGMENT_NODE` |
| `NOTATION_NODE` | `readonly` | `12` | \- | `HTMLElement.NOTATION_NODE` |
| `DOCUMENT_POSITION_DISCONNECTED` | `readonly` | `1` | Set when node and other are not in the same tree. | `HTMLElement.DOCUMENT_POSITION_DISCONNECTED` |
| `DOCUMENT_POSITION_PRECEDING` | `readonly` | `2` | Set when other is preceding node. | `HTMLElement.DOCUMENT_POSITION_PRECEDING` |
| `DOCUMENT_POSITION_FOLLOWING` | `readonly` | `4` | Set when other is following node. | `HTMLElement.DOCUMENT_POSITION_FOLLOWING` |
| `DOCUMENT_POSITION_CONTAINS` | `readonly` | `8` | Set when other is an ancestor of node. | `HTMLElement.DOCUMENT_POSITION_CONTAINS` |
| `DOCUMENT_POSITION_CONTAINED_BY` | `readonly` | `16` | Set when other is a descendant of node. | `HTMLElement.DOCUMENT_POSITION_CONTAINED_BY` |
| `DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC` | `readonly` | `32` | \- | `HTMLElement.DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC` |
| `nextElementSibling` | `readonly` | `Element` | Returns the first following sibling that is an element, and null otherwise. [MDN Reference](https://developer.mozilla.org/docs/Web/API/CharacterData/nextElementSibling) | `HTMLElement.nextElementSibling` |
| `previousElementSibling` | `readonly` | `Element` | Returns the first preceding sibling that is an element, and null otherwise. [MDN Reference](https://developer.mozilla.org/docs/Web/API/CharacterData/previousElementSibling) | `HTMLElement.previousElementSibling` |
| `childElementCount` | `readonly` | `number` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Document/childElementCount) | `HTMLElement.childElementCount` |
| `children` | `readonly` | `HTMLCollection` | Returns the child elements. [MDN Reference](https://developer.mozilla.org/docs/Web/API/Document/children) | `HTMLElement.children` |
| `firstElementChild` | `readonly` | `Element` | Returns the first child that is an element, and null otherwise. [MDN Reference](https://developer.mozilla.org/docs/Web/API/Document/firstElementChild) | `HTMLElement.firstElementChild` |
| `lastElementChild` | `readonly` | `Element` | Returns the last child that is an element, and null otherwise. [MDN Reference](https://developer.mozilla.org/docs/Web/API/Document/lastElementChild) | `HTMLElement.lastElementChild` |
| `assignedSlot` | `readonly` | `HTMLSlotElement` | [MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/assignedSlot) | `HTMLElement.assignedSlot` |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/engine/interfaces/gradientcolorstop)