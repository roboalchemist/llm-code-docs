# Source: https://crawlee.dev/js/api/basic-crawler/class/Element.md

# externalElement<!-- -->

An element within the DOM.

### Hierarchy

* NodeWithChildren
  * *Element*

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**attribs](#attribs)
* [**children](#children)
* [**endIndex](#endIndex)
* [**name](#name)
* [**namespace](#namespace)
* [**next](#next)
* [**parent](#parent)
* [**prev](#prev)
* [**sourceCodeLocation](#sourceCodeLocation)
* [**startIndex](#startIndex)
* [**type](#type)
* [**x-attribsNamespace](#x-attribsNamespace)
* [**x-attribsPrefix](#x-attribsPrefix)

### Accessors

* [**attributes](#attributes)
* [**childNodes](#childNodes)
* [**firstChild](#firstChild)
* [**lastChild](#lastChild)
* [**nextSibling](#nextSibling)
* [**nodeType](#nodeType)
* [**parentNode](#parentNode)
* [**previousSibling](#previousSibling)
* [**tagName](#tagName)

### Methods

* [**cloneNode](#cloneNode)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/domhandler/src/node.d.ts#L178)externalconstructor

* ****new Element**(name, attribs, children, type): [Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)

- Overrides NodeWithChildren.constructor

  #### Parameters

  * ##### externalname: string

    Name of the tag, eg. `div`, `span`.

  * ##### externalattribs: <!-- -->{}

    Object mapping attribute names to attribute values.

  *

    ##### externaloptionalchildren: ChildNode\[]

    Children of the node.

  * ##### externaloptionaltype: Script | Style | Tag

  #### Returns [Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)

## Properties<!-- -->[**](#Properties)

### [**](#attribs)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/domhandler/src/node.d.ts#L169)externalattribs

**attribs:

<!-- -->

{}

#### Type declaration



### [**](#children)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/domhandler/src/node.d.ts#L126)externalinheritedchildren

**children: ChildNode\[]

Inherited from NodeWithChildren.children

### [**](#endIndex)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/domhandler/src/node.d.ts#L39)externalinheritedendIndex

**endIndex: null | number

Inherited from NodeWithChildren.endIndex

The end index of the node. Requires `withEndIndices` on the handler to be \`true.

### [**](#name)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/domhandler/src/node.d.ts#L168)externalname

**name: string

### [**](#namespace)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/domhandler/src/node.d.ts#L196)externaloptionalnamespace

**namespace?

<!-- -->

: string

Element namespace (parse5 only).

### [**](#next)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/domhandler/src/node.d.ts#L35)externalinheritednext

**next: null | ChildNode

Inherited from NodeWithChildren.next

Next sibling

### [**](#parent)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/domhandler/src/node.d.ts#L31)externalinheritedparent

**parent: null | ParentNode

Inherited from NodeWithChildren.parent

Parent of the node

### [**](#prev)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/domhandler/src/node.d.ts#L33)externalinheritedprev

**prev: null | ChildNode

Inherited from NodeWithChildren.prev

Previous sibling

### [**](#sourceCodeLocation)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/domhandler/src/node.d.ts#L187)externaloptionalsourceCodeLocation

**sourceCodeLocation?

<!-- -->

: null | TagSourceCodeLocation

Overrides NodeWithChildren.sourceCodeLocation

`parse5` source code location info, with start & end tags.

Available if parsing with parse5 and location info is enabled.

### [**](#startIndex)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/domhandler/src/node.d.ts#L37)externalinheritedstartIndex

**startIndex: null | number

Inherited from NodeWithChildren.startIndex

The start index of the node. Requires `withStartIndices` on the handler to be \`true.

### [**](#type)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/domhandler/src/node.d.ts#L172)externaltype

**type: Script | Style | Tag

Overrides NodeWithChildren.type

The type of the node.

### [**](#x-attribsNamespace)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/domhandler/src/node.d.ts#L198)externaloptionalx-attribsNamespace

**x-attribsNamespace?

<!-- -->

: Record\<string, string>

Element attribute namespaces (parse5 only).

### [**](#x-attribsPrefix)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/domhandler/src/node.d.ts#L200)externaloptionalx-attribsPrefix

**x-attribsPrefix?

<!-- -->

: Record\<string, string>

Element attribute namespace-related prefixes (parse5 only).

## Accessors<!-- -->[**](#Accessors)

### [**](#attributes)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/domhandler/src/node.d.ts#L194)externalattributes

* **get attributes(): Attribute\[]

- #### Returns Attribute\[]

### [**](#childNodes)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/domhandler/src/node.d.ts#L139)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/domhandler/src/node.d.ts#L140)externalinheritedchildNodes

* **get childNodes(): ChildNode\[]
* **set childNodes(children): void

- Inherited from NodeWithChildren.childNodes

  Same as children. [DOM spec](https://dom.spec.whatwg.org)-compatible alias.

  ***

  #### Returns ChildNode\[]

- Inherited from NodeWithChildren.childNodes

  #### Parameters

  * ##### externalchildren: ChildNode\[]

  #### Returns void

### [**](#firstChild)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/domhandler/src/node.d.ts#L132)externalinheritedfirstChild

* **get firstChild(): null | ChildNode

- Inherited from NodeWithChildren.firstChild

  First child of the node.

  ***

  #### Returns null | ChildNode

### [**](#lastChild)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/domhandler/src/node.d.ts#L134)externalinheritedlastChild

* **get lastChild(): null | ChildNode

- Inherited from NodeWithChildren.lastChild

  Last child of the node.

  ***

  #### Returns null | ChildNode

### [**](#nextSibling)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/domhandler/src/node.d.ts#L67)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/domhandler/src/node.d.ts#L68)externalinheritednextSibling

* **get nextSibling(): null | ChildNode
* **set nextSibling(next): void

- Inherited from NodeWithChildren.nextSibling

  Same as next. [DOM spec](https://dom.spec.whatwg.org)-compatible alias.

  ***

  #### Returns null | ChildNode

- Inherited from NodeWithChildren.nextSibling

  #### Parameters

  * ##### externalnext: null | ChildNode

  #### Returns void

### [**](#nodeType)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/domhandler/src/node.d.ts#L181)externalnodeType

* **get nodeType(): 1

- Overrides NodeWithChildren.nodeType

  [DOM spec](https://dom.spec.whatwg.org/#dom-node-nodetype)-compatible node type.

  ***

  #### Returns 1

### [**](#parentNode)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/domhandler/src/node.d.ts#L55)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/domhandler/src/node.d.ts#L56)externalinheritedparentNode

* **get parentNode(): null | ParentNode
* **set parentNode(parent): void

- Inherited from NodeWithChildren.parentNode

  Same as parent. [DOM spec](https://dom.spec.whatwg.org)-compatible alias.

  ***

  #### Returns null | ParentNode

- Inherited from NodeWithChildren.parentNode

  #### Parameters

  * ##### externalparent: null | ParentNode

  #### Returns void

### [**](#previousSibling)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/domhandler/src/node.d.ts#L61)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/domhandler/src/node.d.ts#L62)externalinheritedpreviousSibling

* **get previousSibling(): null | ChildNode
* **set previousSibling(prev): void

- Inherited from NodeWithChildren.previousSibling

  Same as prev. [DOM spec](https://dom.spec.whatwg.org)-compatible alias.

  ***

  #### Returns null | ChildNode

- Inherited from NodeWithChildren.previousSibling

  #### Parameters

  * ##### externalprev: null | ChildNode

  #### Returns void

### [**](#tagName)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/domhandler/src/node.d.ts#L192)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/domhandler/src/node.d.ts#L193)externaltagName

* **get tagName(): string
* **set tagName(name): void

- Same as name. [DOM spec](https://dom.spec.whatwg.org)-compatible alias.

  ***

  #### Returns string

- #### Parameters

  * ##### externalname: string

  #### Returns void

## Methods<!-- -->[**](#Methods)

### [**](#cloneNode)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/domhandler/src/node.d.ts#L75)externalinheritedcloneNode

* ****cloneNode**\<T>(this, recursive): T

- Inherited from NodeWithChildren.cloneNode

  Clone this node, and optionally its children.

  ***

  #### Parameters

  * ##### externalthis: T

  * ##### externaloptionalrecursive: boolean

    Clone child nodes as well.

  #### Returns T

  A clone of the node.
