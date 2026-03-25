# Source: https://crawlee.dev/js/api/basic-crawler/interface/CheerioAPI.md

# externalCheerioAPI<!-- -->

A querying function, bound to a document created from the provided markup.

Also provides several helper methods for dealing with the document as a whole.

### Hierarchy

* StaticType
  * *CheerioAPI*

### Callable

* ****CheerioAPI**\<T, S>(selector, context, root, options): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<S extends SelectorType ? [Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md) : T>

***

* This selector method is the starting point for traversing and manipulating the document. Like jQuery, it's the primary method for selecting elements in the document.

  `selector` searches within the `context` scope which searches within the `root` scope.

  * **@example**

    ```
    $('.apple', '#fruits').text();
    //=> Apple

    $('ul .pear').attr('class');
    //=> pear

    $('li[class=orange]').html();
    //=> Orange
    ```

  ***

  #### Parameters

  * ##### externaloptionalselector: S | BasicAcceptedElems\<T>

    Either a selector to look for within the document, or the contents of a new Cheerio instance.

  * ##### externaloptionalcontext: null | BasicAcceptedElems\<AnyNode>

    Either a selector to look for within the root, or the contents of the document to query.

  * ##### externaloptionalroot: BasicAcceptedElems\<Document>

    Optional HTML document string.

  * ##### externaloptionaloptions: CheerioOptions

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<S extends SelectorType ? [Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md) : T>

## Index[**](#Index)

### Properties

* [**fn](#fn)
* [**load](#load)

### Methods

* [**contains](#contains)
* [**html](#html)
* [**merge](#merge)
* [**parseHTML](#parseHTML)
* [**root](#root)
* [**text](#text)
* [**xml](#xml)

## Properties<!-- -->[**](#Properties)

### [**](#fn)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/load.d.ts#L55)externalfn

**fn: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<any>

Mimic jQuery's prototype alias for plugin authors.

### [**](#load)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/load.d.ts#L56)externalload

**load: (content, options, isDocument) => [CheerioAPI](https://crawlee.dev/js/api/basic-crawler/interface/CheerioAPI.md)

#### Type declaration

* * **(content, options, isDocument): [CheerioAPI](https://crawlee.dev/js/api/basic-crawler/interface/CheerioAPI.md)

  - #### Parameters

    * ##### externalcontent: string | Buffer\<ArrayBufferLike> | AnyNode | AnyNode\[]
    * ##### externaloptionaloptions: null | CheerioOptions
    * ##### externaloptionalisDocument: boolean

    #### Returns [CheerioAPI](https://crawlee.dev/js/api/basic-crawler/interface/CheerioAPI.md)

## Methods<!-- -->[**](#Methods)

### [**](#contains)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/static.d.ts#L77)externalinheritedcontains

* ****contains**(container, contained): boolean

- Inherited from StaticType.contains

  Checks to see if the `contained` DOM element is a descendant of the `container` DOM element.

  * **@alias**

    Cheerio.contains

  * **@see**

    <https://api.jquery.com/jQuery.contains/>

  ***

  #### Parameters

  * ##### externalcontainer: AnyNode

    Potential parent node.

  * ##### externalcontained: AnyNode

    Potential child node.

  #### Returns boolean

  Indicates if the nodes contain one another.

### [**](#html)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/static.d.ts#L11)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/static.d.ts#L19)externalinheritedhtml

* ****html**(this, options): string
* ****html**(this, dom, options): string

- Inherited from StaticType.html

  Renders the document.

  ***

  #### Parameters

  * ##### externalthis: [CheerioAPI](https://crawlee.dev/js/api/basic-crawler/interface/CheerioAPI.md)

  * ##### externaloptionaloptions: CheerioOptions

    Options for the renderer.

  #### Returns string

  The rendered document.

### [**](#merge)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/static.d.ts#L91)externalinheritedmerge

* ****merge**\<T>(arr1, arr2): ArrayLike\<T> | undefined

- Inherited from StaticType.merge

  $.merge().

  * **@alias**

    Cheerio.merge

  * **@see**

    <https://api.jquery.com/jQuery.merge/>

  ***

  #### Parameters

  * ##### externalarr1: WritableArrayLike\<T>

    First array.

  * ##### externalarr2: ArrayLike\<T>

    Second array.

  #### Returns ArrayLike\<T> | undefined

  `arr1`, with elements of `arr2` inserted.

### [**](#parseHTML)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/static.d.ts#L50)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/static.d.ts#L51)externalinheritedparseHTML

* ****parseHTML**(this, data, context, keepScripts): AnyNode\[]
* ****parseHTML**(this, data): null

- Inherited from StaticType.parseHTML

  Parses a string into an array of DOM nodes. The `context` argument has no meaning for Cheerio, but it is maintained for API compatibility with jQuery.

  * **@alias**

    Cheerio.parseHTML

  * **@see**

    <https://api.jquery.com/jQuery.parseHTML/>

  ***

  #### Parameters

  * ##### externalthis: [CheerioAPI](https://crawlee.dev/js/api/basic-crawler/interface/CheerioAPI.md)

  * ##### externaldata: string

    Markup that will be parsed.

  * ##### externaloptionalcontext: unknown

    Will be ignored. If it is a boolean it will be used as the value of `keepScripts`.

  * ##### externaloptionalkeepScripts: boolean

    If false all scripts will be removed.

  #### Returns AnyNode\[]

  The parsed DOM.

### [**](#root)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/static.d.ts#L66)externalinheritedroot

* ****root**(this): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<Document>

- Inherited from StaticType.root

  Sometimes you need to work with the top-level root element. To query it, you can use `$.root()`.

  * **@example**

    ```
    $.root().append('<ul id="vegetables"></ul>').html();
    //=> <ul id="fruits">...</ul><ul id="vegetables"></ul>
    ```

  * **@alias**

    Cheerio.root

  ***

  #### Parameters

  * ##### externalthis: [CheerioAPI](https://crawlee.dev/js/api/basic-crawler/interface/CheerioAPI.md)

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<Document>

  Cheerio instance wrapping the root node.

### [**](#text)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/static.d.ts#L37)externalinheritedtext

* ****text**(this, elements): string

- Inherited from StaticType.text

  Render the document as text.

  This returns the `textContent` of the passed elements. The result will include the contents of `script` and `stype` elements. To avoid this, use `.prop('innerText')` instead.

  ***

  #### Parameters

  * ##### externalthis: void | [CheerioAPI](https://crawlee.dev/js/api/basic-crawler/interface/CheerioAPI.md)

  * ##### externaloptionalelements: ArrayLike\<AnyNode>

    Elements to render.

  #### Returns string

  The rendered document.

### [**](#xml)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/static.d.ts#L26)externalinheritedxml

* ****xml**(this, dom): string

- Inherited from StaticType.xml

  Render the document as XML.

  ***

  #### Parameters

  * ##### externalthis: [CheerioAPI](https://crawlee.dev/js/api/basic-crawler/interface/CheerioAPI.md)

  * ##### externaloptionaldom: BasicAcceptedElems\<AnyNode>

    Element to render.

  #### Returns string

  THe rendered document.
