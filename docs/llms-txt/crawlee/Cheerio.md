# Source: https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md

# externalabstractCheerio<!-- --> \<T>

### Hierarchy

* AttributesType
* TraversingType
* ManipulationType
* CssType
* FormsType
* Iterable\<T>
  * *Cheerio*

### Implements

* ArrayLike\<T>

## Index[**](#Index)

### Attributes

* [**addClass](#addClass)
* [**attr](#attr)
* [**data](#data)
* [**hasClass](#hasClass)
* [**is](#is)
* [**prop](#prop)
* [**removeAttr](#removeAttr)
* [**removeClass](#removeClass)
* [**toggleClass](#toggleClass)
* [**val](#val)

### CSS

* [**css](#css)

### Forms

* [**serialize](#serialize)
* [**serializeArray](#serializeArray)

### Manipulation

* [**after](#after)
* [**append](#append)
* [**appendTo](#appendTo)
* [**before](#before)
* [**clone](#clone)
* [**empty](#empty)
* [**html](#html)
* [**insertAfter](#insertAfter)
* [**insertBefore](#insertBefore)
* [**prepend](#prepend)
* [**prependTo](#prependTo)
* [**remove](#remove)
* [**replaceWith](#replaceWith)
* [**text](#text)
* [**toString](#toString)
* [**unwrap](#unwrap)
* [**wrap](#wrap)
* [**wrapAll](#wrapAll)
* [**wrapInner](#wrapInner)

### Traversing

* [**add](#add)
* [**addBack](#addBack)
* [**children](#children)
* [**closest](#closest)
* [**contents](#contents)
* [**each](#each)
* [**end](#end)
* [**eq](#eq)
* [**filter](#filter)
* [**find](#find)
* [**first](#first)
* [**get](#get)
* [**has](#has)
* [**index](#index)
* [**last](#last)
* [**map](#map)
* [**next](#next)
* [**nextAll](#nextAll)
* [**nextUntil](#nextUntil)
* [**not](#not)
* [**parent](#parent)
* [**parents](#parents)
* [**parentsUntil](#parentsUntil)
* [**prev](#prev)
* [**prevAll](#prevAll)
* [**prevUntil](#prevUntil)
* [**siblings](#siblings)
* [**slice](#slice)

### Other

* [**cheerio](#cheerio)
* [**length](#length)
* [**options](#options)
* [**prevObject](#prevObject)
* [**splice](#splice)
* [**\[iterator\]](#\[iterator])
* [**filterArray](#filterArray)
* [**toArray](#toArray)

## Attributes<!-- -->[**](#Attributes)

### [**](#addClass)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/attributes.d.ts#L289)externaladdClass

* ****addClass**\<T, R>(this, value): R

- Adds class(es) to all of the matched elements. Also accepts a `function`.

  * **@example**

    ```
    $('.pear').addClass('fruit').html();
    //=> <li class="pear fruit">Pear</li>

    $('.apple').addClass('fruit red').html();
    //=> <li class="apple fruit red">Apple</li>
    ```

  * **@see**

    <https://api.jquery.com/addClass/>

  ***

  #### Parameters

  * ##### externalthis: R

  * ##### externaloptionalvalue: string | (this, i, className) => undefined | string

    Name of new class.



  #### Returns R

  The instance itself.

### [**](#attr)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/attributes.d.ts#L24)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/attributes.d.ts#L40)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/attributes.d.ts#L59)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/attributes.d.ts#L77)externalattr

* ****attr**\<T>(this, name): string | undefined
* ****attr**\<T>(this): Record\<string, string> | undefined
* ****attr**\<T>(this, name, value): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>
* ****attr**\<T>(this, values): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

- Method for getting attributes. Gets the attribute value for only the first element in the matched set.

  * **@example**

    ```
    $('ul').attr('id');
    //=> fruits
    ```

  * **@see**

    <https://api.jquery.com/attr/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externalname: string

    Name of the attribute.

  #### Returns string | undefined

  The attribute's value.

### [**](#data)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/attributes.d.ts#L141)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/attributes.d.ts#L157)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/attributes.d.ts#L176)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/attributes.d.ts#L195)externaldata

* ****data**\<T>(this, name): unknown | undefined
* ****data**\<T>(this): Record\<string, unknown>
* ****data**\<T>(this, name, value): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>
* ****data**\<T>(this, values): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

- Method for getting data attributes, for only the first element in the matched set.

  * **@example**

    ```
    $('<div data-apple-color="red"></div>').data('apple-color');
    //=> 'red'
    ```

  * **@see**

    <https://api.jquery.com/data/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externalname: string

    Name of the data attribute.

  #### Returns unknown | undefined

  The data attribute's value, or `undefined` if the attribute does not exist.

### [**](#hasClass)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/attributes.d.ts#L270)externalhasClass

* ****hasClass**\<T>(this, className): boolean

- Check to see if *any* of the matched elements have the given `className`.

  * **@example**

    ```
    $('.pear').hasClass('pear');
    //=> true

    $('apple').hasClass('fruit');
    //=> false

    $('li').hasClass('pear');
    //=> true
    ```

  * **@see**

    <https://api.jquery.com/hasClass/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externalclassName: string

    Name of the class.

  #### Returns boolean

  Indicates if an element has the given `className`.

### [**](#is)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/traversing.d.ts#L398)externalis

* ****is**\<T>(this, selector): boolean

- Checks the current list of elements and returns `true` if *any* of the elements match the selector. If using an element or Cheerio selection, returns `true` if *any* of the elements match. If using a predicate function, the function is executed in the context of the selected element, so `this` refers to the current element.

  * **@see**

    <https://api.jquery.com/is/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externaloptionalselector: AcceptedFilters\<T>

    Selector for the selection.

  #### Returns boolean

  Whether or not the selector matches an element of the instance.

### [**](#prop)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/attributes.d.ts#L103)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/attributes.d.ts#L104)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/attributes.d.ts#L106)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/attributes.d.ts#L118)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/attributes.d.ts#L120)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/attributes.d.ts#L122)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/attributes.d.ts#L123)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/attributes.d.ts#L124)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/attributes.d.ts#L125)externalprop

* ****prop**\<T>(this, name): T extends [Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md) ? string : undefined
* ****prop**\<T>(this, name): string | null
* ****prop**\<T>(this, name): StyleProp | undefined
* ****prop**\<T>(this, name): string | undefined
* ****prop**\<T, K>(this, name): [Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)\[K]
* ****prop**\<T, K>(this, name, value): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>
* ****prop**\<T>(this, name): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>
* ****prop**\<T>(this, name, value): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>
* ****prop**\<T>(this, name): string

- Method for getting and setting properties. Gets the property value for only the first element in the matched set.

  * **@example**

    ```
    $('input[type="checkbox"]').prop('checked');
    //=> false

    $('input[type="checkbox"]').prop('checked', true).val();
    //=> ok
    ```

  * **@see**

    <https://api.jquery.com/prop/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externalname: tagName | nodeName

    Name of the property.

  #### Returns T extends [Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md) ? string : undefined

  If `value` is specified the instance itself, otherwise the prop's value.

### [**](#removeAttr)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/attributes.d.ts#L248)externalremoveAttr

* ****removeAttr**\<T>(this, name): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

- Method for removing attributes by `name`.

  * **@example**

    ```
    $('.pear').removeAttr('class').html();
    //=> <li>Pear</li>

    $('.apple').attr('id', 'favorite');
    $('.apple').removeAttr('id class').html();
    //=> <li>Apple</li>
    ```

  * **@see**

    <https://api.jquery.com/removeAttr/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externalname: string

    Name of the attribute.

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  The instance itself.

### [**](#removeClass)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/attributes.d.ts#L309)externalremoveClass

* ****removeClass**\<T, R>(this, name): R

- Removes one or more space-separated classes from the selected elements. If no `className` is defined, all classes will be removed. Also accepts a `function`.

  * **@example**

    ```
    $('.pear').removeClass('pear').html();
    //=> <li class="">Pear</li>

    $('.apple').addClass('red').removeClass().html();
    //=> <li class="">Apple</li>
    ```

  * **@see**

    <https://api.jquery.com/removeClass/>

  ***

  #### Parameters

  * ##### externalthis: R

  * ##### externaloptionalname: string | (this, i, className) => undefined | string

    Name of the class. If not specified, removes all elements.



  #### Returns R

  The instance itself.

### [**](#toggleClass)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/attributes.d.ts#L330)externaltoggleClass

* ****toggleClass**\<T, R>(this, value, stateVal): R

- Add or remove class(es) from the matched elements, depending on either the class's presence or the value of the switch argument. Also accepts a `function`.

  * **@example**

    ```
    $('.apple.green').toggleClass('fruit green red').html();
    //=> <li class="apple fruit red">Apple</li>

    $('.apple.green').toggleClass('fruit green red', true).html();
    //=> <li class="apple green fruit red">Apple</li>
    ```

  * **@see**

    <https://api.jquery.com/toggleClass/>

  ***

  #### Parameters

  * ##### externalthis: R

  * ##### externaloptionalvalue: string | (this, i, className, stateVal) => string

    Name of the class. Can also be a function.

  *

    ##### externaloptionalstateVal: boolean

    If specified the state of the class.

  #### Returns R

  The instance itself.

### [**](#val)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/attributes.d.ts#L211)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/attributes.d.ts#L228)externalval

* ****val**\<T>(this): string | undefined | string\[]
* ****val**\<T>(this, value): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

- Method for getting the value of input, select, and textarea. Note: Support for `map`, and `function` has not been added yet.

  * **@example**

    ```
    $('input[type="text"]').val();
    //=> input_text
    ```

  * **@see**

    <https://api.jquery.com/val/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  #### Returns string | undefined | string\[]

  The value.

## CSS<!-- -->[**](#CSS)

### [**](#css)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/css.d.ts#L11)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/css.d.ts#L20)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/css.d.ts#L30)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/css.d.ts#L39)externalcss

* ****css**\<T>(this, names): Record\<string, string> | undefined
* ****css**\<T>(this, name): string | undefined
* ****css**\<T>(this, prop, val): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>
* ****css**\<T>(this, map): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

- Get the value of a style property for the first element in the set of matched elements.

  * **@see**

    <https://api.jquery.com/css/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externaloptionalnames: string\[]

    Optionally the names of the properties of interest.

  #### Returns Record\<string, string> | undefined

  A map of all of the style properties.

## Forms<!-- -->[**](#Forms)

### [**](#serialize)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/forms.d.ts#L17)externalserialize

* ****serialize**\<T>(this): string

- Encode a set of form elements as a string for submission.

  * **@example**

    ```
    $('<form><input name="foo" value="bar" /></form>').serialize();
    //=> 'foo=bar'
    ```

  * **@see**

    <https://api.jquery.com/serialize/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  #### Returns string

  The serialized form.

### [**](#serializeArray)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/forms.d.ts#L36)externalserializeArray

* ****serializeArray**\<T>(this): SerializedField\[]

- Encode a set of form elements as an array of names and values.

  * **@example**

    ```
    $('<form><input name="foo" value="bar" /></form>').serializeArray();
    //=> [ { name: 'foo', value: 'bar' } ]
    ```

  * **@see**

    <https://api.jquery.com/serializeArray/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  #### Returns SerializedField\[]

  The serialized form.

## Manipulation<!-- -->[**](#Manipulation)

### [**](#after)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/manipulation.d.ts#L303)externalafter

* ****after**\<T>(this, ...elems): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

- Insert content next to each element in the set of matched elements.

  * **@example**

    ```
    $('.apple').after('<li class="plum">Plum</li>');
    $.html();
    //=>  <ul id="fruits">
    //      <li class="apple">Apple</li>
    //      <li class="plum">Plum</li>
    //      <li class="orange">Orange</li>
    //      <li class="pear">Pear</li>
    //    </ul>
    ```

  * **@see**

    <https://api.jquery.com/after/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>
  * ##### externalrest...elems: \[(this, i, html) => BasicAcceptedElems\<AnyNode>] | BasicAcceptedElems\<AnyNode>\[]

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  The instance itself.

### [**](#append)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/manipulation.d.ts#L82)externalappend

* ****append**\<T>(this, ...elems): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

- Inserts content as the *last* child of each of the selected elements.

  * **@example**

    ```
    $('ul').append('<li class="plum">Plum</li>');
    $.html();
    //=>  <ul id="fruits">
    //      <li class="apple">Apple</li>
    //      <li class="orange">Orange</li>
    //      <li class="pear">Pear</li>
    //      <li class="plum">Plum</li>
    //    </ul>
    ```

  * **@see**

    <https://api.jquery.com/append/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>
  * ##### externalrest...elems: BasicAcceptedElems\<AnyNode>\[] | \[(this, i, html) => BasicAcceptedElems\<AnyNode>]

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

### [**](#appendTo)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/manipulation.d.ts#L40)externalappendTo

* ****appendTo**\<T>(this, target): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

- Insert every element in the set of matched elements to the end of the target.

  * **@example**

    ```
    $('<li class="plum">Plum</li>').appendTo('#fruits');
    $.html();
    //=>  <ul id="fruits">
    //      <li class="apple">Apple</li>
    //      <li class="orange">Orange</li>
    //      <li class="pear">Pear</li>
    //      <li class="plum">Plum</li>
    //    </ul>
    ```

  * **@see**

    <https://api.jquery.com/appendTo/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externaltarget: BasicAcceptedElems\<AnyNode>

    Element to append elements to.

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  The instance itself.

### [**](#before)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/manipulation.d.ts#L348)externalbefore

* ****before**\<T>(this, ...elems): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

- Insert content previous to each element in the set of matched elements.

  * **@example**

    ```
    $('.apple').before('<li class="plum">Plum</li>');
    $.html();
    //=>  <ul id="fruits">
    //      <li class="plum">Plum</li>
    //      <li class="apple">Apple</li>
    //      <li class="orange">Orange</li>
    //      <li class="pear">Pear</li>
    //    </ul>
    ```

  * **@see**

    <https://api.jquery.com/before/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>
  * ##### externalrest...elems: BasicAcceptedElems\<AnyNode>\[] | \[(this, i, html) => BasicAcceptedElems\<AnyNode>]

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  The instance itself.

### [**](#clone)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/manipulation.d.ts#L521)externalclone

* ****clone**\<T>(this): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

- Clone the cheerio object.

  * **@example**

    ```
    const moreFruit = $('#fruits').clone();
    ```

  * **@see**

    <https://api.jquery.com/clone/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  The cloned object.

### [**](#empty)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/manipulation.d.ts#L429)externalempty

* ****empty**\<T>(this): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

- Empties an element, removing all its children.

  * **@example**

    ```
    $('ul').empty();
    $.html();
    //=>  <ul id="fruits"></ul>
    ```

  * **@see**

    <https://api.jquery.com/empty/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  The instance itself.

### [**](#html)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/manipulation.d.ts#L447)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/manipulation.d.ts#L463)externalhtml

* ****html**\<T>(this): string | null
* ****html**\<T>(this, str): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

- Gets an HTML content string from the first selected element.

  * **@example**

    ```
    $('.orange').html();
    //=> Orange

    $('#fruits').html('<li class="mango">Mango</li>').html();
    //=> <li class="mango">Mango</li>
    ```

  * **@see**

    <https://api.jquery.com/html/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  #### Returns string | null

  The HTML content string.

### [**](#insertAfter)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/manipulation.d.ts#L325)externalinsertAfter

* ****insertAfter**\<T>(this, target): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

- Insert every element in the set of matched elements after the target.

  * **@example**

    ```
    $('<li class="plum">Plum</li>').insertAfter('.apple');
    $.html();
    //=>  <ul id="fruits">
    //      <li class="apple">Apple</li>
    //      <li class="plum">Plum</li>
    //      <li class="orange">Orange</li>
    //      <li class="pear">Pear</li>
    //    </ul>
    ```

  * **@see**

    <https://api.jquery.com/insertAfter/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externaltarget: BasicAcceptedElems\<AnyNode>

    Element to insert elements after.

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  The set of newly inserted elements.

### [**](#insertBefore)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/manipulation.d.ts#L370)externalinsertBefore

* ****insertBefore**\<T>(this, target): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

- Insert every element in the set of matched elements before the target.

  * **@example**

    ```
    $('<li class="plum">Plum</li>').insertBefore('.apple');
    $.html();
    //=>  <ul id="fruits">
    //      <li class="plum">Plum</li>
    //      <li class="apple">Apple</li>
    //      <li class="orange">Orange</li>
    //      <li class="pear">Pear</li>
    //    </ul>
    ```

  * **@see**

    <https://api.jquery.com/insertBefore/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externaltarget: BasicAcceptedElems\<AnyNode>

    Element to insert elements before.

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  The set of newly inserted elements.

### [**](#prepend)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/manipulation.d.ts#L102)externalprepend

* ****prepend**\<T>(this, ...elems): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

- Inserts content as the *first* child of each of the selected elements.

  * **@example**

    ```
    $('ul').prepend('<li class="plum">Plum</li>');
    $.html();
    //=>  <ul id="fruits">
    //      <li class="plum">Plum</li>
    //      <li class="apple">Apple</li>
    //      <li class="orange">Orange</li>
    //      <li class="pear">Pear</li>
    //    </ul>
    ```

  * **@see**

    <https://api.jquery.com/prepend/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>
  * ##### externalrest...elems: BasicAcceptedElems\<AnyNode>\[] | \[(this, i, html) => BasicAcceptedElems\<AnyNode>]

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

### [**](#prependTo)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/manipulation.d.ts#L62)externalprependTo

* ****prependTo**\<T>(this, target): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

- Insert every element in the set of matched elements to the beginning of the target.

  * **@example**

    ```
    $('<li class="plum">Plum</li>').prependTo('#fruits');
    $.html();
    //=>  <ul id="fruits">
    //      <li class="plum">Plum</li>
    //      <li class="apple">Apple</li>
    //      <li class="orange">Orange</li>
    //      <li class="pear">Pear</li>
    //    </ul>
    ```

  * **@see**

    <https://api.jquery.com/prependTo/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externaltarget: BasicAcceptedElems\<AnyNode>

    Element to prepend elements to.

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  The instance itself.

### [**](#remove)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/manipulation.d.ts#L391)externalremove

* ****remove**\<T>(this, selector): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

- Removes the set of matched elements from the DOM and all their children. `selector` filters the set of matched elements to be removed.

  * **@example**

    ```
    $('.pear').remove();
    $.html();
    //=>  <ul id="fruits">
    //      <li class="apple">Apple</li>
    //      <li class="orange">Orange</li>
    //    </ul>
    ```

  * **@see**

    <https://api.jquery.com/remove/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externaloptionalselector: string

    Optional selector for elements to remove.

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  The instance itself.

### [**](#replaceWith)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/manipulation.d.ts#L413)externalreplaceWith

* ****replaceWith**\<T>(this, content): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

- Replaces matched elements with `content`.

  * **@example**

    ```
    const plum = $('<li class="plum">Plum</li>');
    $('.pear').replaceWith(plum);
    $.html();
    //=> <ul id="fruits">
    //     <li class="apple">Apple</li>
    //     <li class="orange">Orange</li>
    //     <li class="plum">Plum</li>
    //   </ul>
    ```

  * **@see**

    <https://api.jquery.com/replaceWith/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externalcontent: AcceptedElems\<AnyNode>

    Replacement for matched elements.

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  The instance itself.

### [**](#text)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/manipulation.d.ts#L491)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/manipulation.d.ts#L507)externaltext

* ****text**\<T>(this): string
* ****text**\<T>(this, str): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

- Get the combined text contents of each element in the set of matched elements, including their descendants.

  * **@example**

    ```
    $('.orange').text();
    //=> Orange

    $('ul').text();
    //=>  Apple
    //    Orange
    //    Pear
    ```

  * **@see**

    <https://api.jquery.com/text/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  #### Returns string

  The text contents of the collection.

### [**](#toString)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/manipulation.d.ts#L470)externaltoString

* ****toString**\<T>(this): string

- Turns the collection to a string. Alias for `.html()`.

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  #### Returns string

  The rendered document.

### [**](#unwrap)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/manipulation.d.ts#L228)externalunwrap

* ****unwrap**\<T>(this, selector): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

- The .unwrap() function, removes the parents of the set of matched elements from the DOM, leaving the matched elements in their place.

  * **@example**

    ```
    const $ = cheerio.load(
      '<div id=test>\n  <div><p>Hello</p></div>\n  <div><p>World</p></div>\n</div>'
    );
    $('#test p').unwrap();

    //=> <div id=test>
    //     <p>Hello</p>
    //     <p>World</p>
    //   </div>
    ```

  * **@example**

    ```
    const $ = cheerio.load(
      '<div id=test>\n  <p>Hello</p>\n  <b><p>World</p></b>\n</div>'
    );
    $('#test p').unwrap('b');

    //=> <div id=test>
    //     <p>Hello</p>
    //     <p>World</p>
    //   </div>
    ```

  * **@see**

    <https://api.jquery.com/unwrap/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externaloptionalselector: string

    A selector to check the parent element against. If an element's parent does not match the selector, the element won't be unwrapped.

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  The instance itself, for chaining.

### [**](#wrap)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/manipulation.d.ts#L145)externalwrap

* ****wrap**\<T>(this, wrapper): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

- The .wrap() function can take any string or object that could be passed to the $() factory function to specify a DOM structure. This structure may be nested several levels deep, but should contain only one inmost element. A copy of this structure will be wrapped around each of the elements in the set of matched elements. This method returns the original set of elements for chaining purposes.

  * **@example**

    ```
    const redFruit = $('<div class="red-fruit"></div>');
    $('.apple').wrap(redFruit);

    //=> <ul id="fruits">
    //     <div class="red-fruit">
    //      <li class="apple">Apple</li>
    //     </div>
    //     <li class="orange">Orange</li>
    //     <li class="plum">Plum</li>
    //   </ul>

    const healthy = $('<div class="healthy"></div>');
    $('li').wrap(healthy);

    //=> <ul id="fruits">
    //     <div class="healthy">
    //       <li class="apple">Apple</li>
    //     </div>
    //     <div class="healthy">
    //       <li class="orange">Orange</li>
    //     </div>
    //     <div class="healthy">
    //        <li class="plum">Plum</li>
    //     </div>
    //   </ul>
    ```

  * **@see**

    <https://api.jquery.com/wrap/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externalwrapper: AcceptedElems\<AnyNode>

    The DOM structure to wrap around each element in the selection.

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

### [**](#wrapAll)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/manipulation.d.ts#L280)externalwrapAll

* ****wrapAll**\<T>(this, wrapper): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

- The .wrapAll() function can take any string or object that could be passed to the $() function to specify a DOM structure. This structure may be nested several levels deep, but should contain only one inmost element. The structure will be wrapped around all of the elements in the set of matched elements, as a single group.

  * **@example**

    ```
    const $ = cheerio.load(
      '<div class="container"><div class="inner">First</div><div class="inner">Second</div></div>'
    );
    $('.inner').wrapAll("<div class='new'></div>");

    //=> <div class="container">
    //     <div class='new'>
    //       <div class="inner">First</div>
    //       <div class="inner">Second</div>
    //     </div>
    //   </div>
    ```

  * **@example**

    ```
    const $ = cheerio.load(
      '<span>Span 1</span><strong>Strong</strong><span>Span 2</span>'
    );
    const wrap = $('<div><p><em><b></b></em></p></div>');
    $('span').wrapAll(wrap);

    //=> <div>
    //     <p>
    //       <em>
    //         <b>
    //           <span>Span 1</span>
    //           <span>Span 2</span>
    //         </b>
    //       </em>
    //     </p>
    //   </div>
    //   <strong>Strong</strong>
    ```

  * **@see**

    <https://api.jquery.com/wrapAll/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externalwrapper: AcceptedElems\<T>

    The DOM structure to wrap around all matched elements in the selection.

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  The instance itself.

### [**](#wrapInner)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/manipulation.d.ts#L189)externalwrapInner

* ****wrapInner**\<T>(this, wrapper): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

- The .wrapInner() function can take any string or object that could be passed to the $() factory function to specify a DOM structure. This structure may be nested several levels deep, but should contain only one inmost element. The structure will be wrapped around the content of each of the elements in the set of matched elements.

  * **@example**

    ```
    const redFruit = $('<div class="red-fruit"></div>');
    $('.apple').wrapInner(redFruit);

    //=> <ul id="fruits">
    //     <li class="apple">
    //       <div class="red-fruit">Apple</div>
    //     </li>
    //     <li class="orange">Orange</li>
    //     <li class="pear">Pear</li>
    //   </ul>

    const healthy = $('<div class="healthy"></div>');
    $('li').wrapInner(healthy);

    //=> <ul id="fruits">
    //     <li class="apple">
    //       <div class="healthy">Apple</div>
    //     </li>
    //     <li class="orange">
    //       <div class="healthy">Orange</div>
    //     </li>
    //     <li class="pear">
    //       <div class="healthy">Pear</div>
    //     </li>
    //   </ul>
    ```

  * **@see**

    <https://api.jquery.com/wrapInner/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externalwrapper: AcceptedElems\<AnyNode>

    The DOM structure to wrap around the content of each element in the selection.

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  The instance itself, for chaining.

## Traversing<!-- -->[**](#Traversing)

### [**](#add)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/traversing.d.ts#L626)externaladd

* ****add**\<S, T>(this, other, context): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<S | T>

- Add elements to the set of matched elements.

  * **@example**

    ```
    $('.apple').add('.orange').length;
    //=> 2
    ```

  * **@see**

    <https://api.jquery.com/add/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externalother: string | S | [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<S> | S\[]

    Elements to add.

  * ##### externaloptionalcontext: string | [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<S>

    Optionally the context of the new selection.

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<S | T>

  The combined set.

### [**](#addBack)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/traversing.d.ts#L643)externaladdBack

* ****addBack**\<T>(this, selector): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<AnyNode>

- Add the previous set of elements on the stack to the current set, optionally filtered by a selector.

  * **@example**

    ```
    $('li').eq(0).addBack('.orange').length;
    //=> 2
    ```

  * **@see**

    <https://api.jquery.com/addBack/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externaloptionalselector: string

    Selector for the elements to add.

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<AnyNode>

  The combined set.

### [**](#children)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/traversing.d.ts#L254)externalchildren

* ****children**\<T>(this, selector): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

- Gets the element children of each element in the set of matched elements.

  * **@example**

    ```
    $('#fruits').children().length;
    //=> 3

    $('#fruits').children('.pear').text();
    //=> Pear
    ```

  * **@see**

    <https://api.jquery.com/children/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externaloptionalselector: AcceptedFilters<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

    If specified filter for children.

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

  The children.

### [**](#closest)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/traversing.d.ts#L107)externalclosest

* ****closest**\<T>(this, selector): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<AnyNode>

- For each element in the set, get the first element that matches the selector by testing the element itself and traversing up through its ancestors in the DOM tree.

  * **@example**

    ```
    $('.orange').closest();
    //=> []

    $('.orange').closest('.apple');
    // => []

    $('.orange').closest('li');
    //=> [<li class="orange">Orange</li>]

    $('.orange').closest('#fruits');
    //=> [<ul id="fruits"> ... </ul>]
    ```

  * **@see**

    <https://api.jquery.com/closest/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externaloptionalselector: AcceptedFilters<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

    Selector for the element to find.

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<AnyNode>

  The closest nodes.

### [**](#contents)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/traversing.d.ts#L270)externalcontents

* ****contents**\<T>(this): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<AnyNode>

- Gets the children of each element in the set of matched elements, including text and comment nodes.

  * **@example**

    ```
    $('#fruits').contents().length;
    //=> 3
    ```

  * **@see**

    <https://api.jquery.com/contents/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<AnyNode>

  The children.

### [**](#each)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/traversing.d.ts#L296)externaleach

* ****each**\<T>(this, fn): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

- Iterates over a cheerio object, executing a function for each matched element. When the callback is fired, the function is fired in the context of the DOM element, so `this` refers to the current element, which is equivalent to the function parameter `element`. To break out of the `each` loop early, return with `false`.

  * **@example**

    ```
    const fruits = [];

    $('li').each(function (i, elem) {
      fruits[i] = $(this).text();
    });

    fruits.join(', ');
    //=> Apple, Orange, Pear
    ```

  * **@see**

    <https://api.jquery.com/each/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externalfn: (this, i, el) => boolean | void

    Function to execute.



  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  The instance itself, useful for chaining.

### [**](#end)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/traversing.d.ts#L609)externalend

* ****end**\<T>(this): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<AnyNode>

- End the most recent filtering operation in the current chain and return the set of matched elements to its previous state.

  * **@example**

    ```
    $('li').eq(0).end().length;
    //=> 3
    ```

  * **@see**

    <https://api.jquery.com/end/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<AnyNode>

  The previous state of the set of matched elements.

### [**](#eq)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/traversing.d.ts#L507)externaleq

* ****eq**\<T>(this, i): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

- Reduce the set of matched elements to the one at the specified index. Use `.eq(-i)` to count backwards from the last selected element.

  * **@example**

    ```
    $('li').eq(0).text();
    //=> Apple

    $('li').eq(-1).text();
    //=> Pear
    ```

  * **@see**

    <https://api.jquery.com/eq/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externali: number

    Index of the element to select.

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  The element at the `i`th position.

### [**](#filter)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/traversing.d.ts#L348)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/traversing.d.ts#L384)externalfilter

* ****filter**\<T, S>(this, match): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<S>
* ****filter**\<T, S>(this, match): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<S extends string ? [Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md) : T>

- Iterates over a cheerio object, reducing the set of selector elements to those that match the selector or pass the function's test.

  This is the definition for using type guards; have a look below for other ways to invoke this method. The function is executed in the context of the selected element, so `this` refers to the current element.

  * **@example**

    ```
    $('li')
      .filter(function (i, el) {
        // this === el
        return $(this).attr('class') === 'orange';
      })
      .attr('class'); //=> orange
    ```

  * **@see**

    <https://api.jquery.com/filter/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externalmatch: (this, index, value) => value is S

    Value to look for, following the rules above.



  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<S>

  The filtered collection.

### [**](#find)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/traversing.d.ts#L27)externalfind

* ****find**\<T>(this, selectorOrHaystack): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

- Get the descendants of each element in the current set of matched elements, filtered by a selector, jQuery object, or element.

  * **@example**

    ```
    $('#fruits').find('li').length;
    //=> 3
    $('#fruits').find($('.apple')).length;
    //=> 1
    ```

  * **@see**

    <https://api.jquery.com/find/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externaloptionalselectorOrHaystack: string | [Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md) | [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

    Element to look for.

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

  The found elements.

### [**](#first)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/traversing.d.ts#L472)externalfirst

* ****first**\<T>(this): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

- Will select the first element of a cheerio object.

  * **@example**

    ```
    $('#fruits').children().first().text();
    //=> Apple
    ```

  * **@see**

    <https://api.jquery.com/first/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  The first element.

### [**](#get)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/traversing.d.ts#L523)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/traversing.d.ts#L538)externalget

* ****get**\<T>(this, i): T | undefined
* ****get**\<T>(this): T\[]

- Retrieve one of the elements matched by the Cheerio object, at the `i`th position.

  * **@example**

    ```
    $('li').get(0).tagName;
    //=> li
    ```

  * **@see**

    <https://api.jquery.com/get/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externali: number

    Element to retrieve.

  #### Returns T | undefined

  The element at the `i`th position.

### [**](#has)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/traversing.d.ts#L457)externalhas

* ****has**(this, selectorOrHaystack): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<AnyNode | [Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

- Filters the set of matched elements to only those which have the given DOM element as a descendant or which have a descendant that matches the given selector. Equivalent to `.filter(':has(selector)')`.

  * **@example**

    ```
    $('ul').has('.pear').attr('id');
    //=> fruits
    ```

  * **@example**

    ```
    $('ul').has($('.pear')[0]).attr('id');
    //=> fruits
    ```

  * **@see**

    <https://api.jquery.com/has/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<AnyNode>

  * ##### externalselectorOrHaystack: string | [Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md) | [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

    Element to look for.

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<AnyNode | [Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

  The filtered collection.

### [**](#index)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/traversing.d.ts#L570)externalindex

* ****index**\<T>(this, selectorOrNeedle): number

- Search for a given element from among the matched elements.

  * **@example**

    ```
    $('.pear').index();
    //=> 2 $('.orange').index('li');
    //=> 1
    $('.apple').index($('#fruit, li'));
    //=> 1
    ```

  * **@see**

    <https://api.jquery.com/index/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externaloptionalselectorOrNeedle: string | AnyNode | [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<AnyNode>

    Element to look for.

  #### Returns number

  The index of the element.

### [**](#last)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/traversing.d.ts#L487)externallast

* ****last**\<T>(this): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

- Will select the last element of a cheerio object.

  * **@example**

    ```
    $('#fruits').children().last().text();
    //=> Pear
    ```

  * **@see**

    <https://api.jquery.com/last/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  The last element.

### [**](#map)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/traversing.d.ts#L323)externalmap

* ****map**\<T, M>(this, fn): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<M>

- Pass each element in the current matched set through a function, producing a new Cheerio object containing the return values. The function can return an individual data item or an array of data items to be inserted into the resulting set. If an array is returned, the elements inside the array are inserted into the set. If the function returns null or undefined, no element will be inserted.

  * **@example**

    ```
    $('li')
      .map(function (i, el) {
        // this === el
        return $(this).text();
      })
      .toArray()
      .join(' ');
    //=> "apple orange pear"
    ```

  * **@see**

    <https://api.jquery.com/map/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externalfn: (this, i, el) => undefined | null | M | M\[]

    Function to execute.



  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<M>

  The mapped elements, wrapped in a Cheerio collection.

### [**](#next)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/traversing.d.ts#L123)externalnext

* ****next**\<T>(this, selector): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

- Gets the next sibling of the first selected element, optionally filtered by a selector.

  * **@example**

    ```
    $('.apple').next().hasClass('orange');
    //=> true
    ```

  * **@see**

    <https://api.jquery.com/next/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externaloptionalselector: AcceptedFilters<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

    If specified filter for sibling.

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

  The next nodes.

### [**](#nextAll)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/traversing.d.ts#L142)externalnextAll

* ****nextAll**\<T>(this, selector): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

- Gets all the following siblings of the first selected element, optionally filtered by a selector.

  * **@example**

    ```
    $('.apple').nextAll();
    //=> [<li class="orange">Orange</li>, <li class="pear">Pear</li>]
    $('.apple').nextAll('.orange');
    //=> [<li class="orange">Orange</li>]
    ```

  * **@see**

    <https://api.jquery.com/nextAll/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externaloptionalselector: AcceptedFilters<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

    If specified filter for siblings.

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

  The next nodes.

### [**](#nextUntil)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/traversing.d.ts#L160)externalnextUntil

* ****nextUntil**\<T>(this, selector, filterSelector): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

- Gets all the following siblings up to but not including the element matched by the selector, optionally filtered by another selector.

  * **@example**

    ```
    $('.apple').nextUntil('.pear');
    //=> [<li class="orange">Orange</li>]
    ```

  * **@see**

    <https://api.jquery.com/nextUntil/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externaloptionalselector: null | AcceptedFilters<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

    Selector for element to stop at.

  * ##### externaloptionalfilterSelector: AcceptedFilters<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

    If specified filter for siblings.

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

  The next nodes.

### [**](#not)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/traversing.d.ts#L432)externalnot

* ****not**\<T>(this, match): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

- Remove elements from the set of matched elements. Given a Cheerio object that represents a set of DOM elements, the `.not()` method constructs a new Cheerio object from a subset of the matching elements. The supplied selector is tested against each element; the elements that don't match the selector will be included in the result.

  The `.not()` method can take a function as its argument in the same way that `.filter()` does. Elements for which the function returns `true` are excluded from the filtered set; all other elements are included.

  * **@example**

    ```
    $('li').not('.apple').length;
    //=> 2
    ```

  * **@example**

    ```
    $('li').not(function (i, el) {
      // this === el
      return $(this).attr('class') === 'orange';
    }).length; //=> 2
    ```

  * **@see**

    <https://api.jquery.com/not/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externalmatch: AcceptedFilters\<T>

    Value to look for, following the rules above.

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  The filtered collection.

### [**](#parent)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/traversing.d.ts#L44)externalparent

* ****parent**\<T>(this, selector): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

- Get the parent of each element in the current set of matched elements, optionally filtered by a selector.

  * **@example**

    ```
    $('.pear').parent().attr('id');
    //=> fruits
    ```

  * **@see**

    <https://api.jquery.com/parent/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externaloptionalselector: AcceptedFilters<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

    If specified filter for parent.

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

  The parents.

### [**](#parents)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/traversing.d.ts#L63)externalparents

* ****parents**\<T>(this, selector): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

- Get a set of parents filtered by `selector` of each element in the current set of match elements.

  * **@example**

    ```
    $('.orange').parents().length;
    //=> 2
    $('.orange').parents('#fruits').length;
    //=> 1
    ```

  * **@see**

    <https://api.jquery.com/parents/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externaloptionalselector: AcceptedFilters<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

    If specified filter for parents.

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

  The parents.

### [**](#parentsUntil)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/traversing.d.ts#L81)externalparentsUntil

* ****parentsUntil**\<T>(this, selector, filterSelector): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

- Get the ancestors of each element in the current set of matched elements, up to but not including the element matched by the selector, DOM node, or cheerio object.

  * **@example**

    ```
    $('.orange').parentsUntil('#food').length;
    //=> 1
    ```

  * **@see**

    <https://api.jquery.com/parentsUntil/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externaloptionalselector: null | AcceptedFilters<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

    Selector for element to stop at.

  * ##### externaloptionalfilterSelector: AcceptedFilters<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

    Optional filter for parents.

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

  The parents.

### [**](#prev)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/traversing.d.ts#L177)externalprev

* ****prev**\<T>(this, selector): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

- Gets the previous sibling of the first selected element optionally filtered by a selector.

  * **@example**

    ```
    $('.orange').prev().hasClass('apple');
    //=> true
    ```

  * **@see**

    <https://api.jquery.com/prev/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externaloptionalselector: AcceptedFilters<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

    If specified filter for siblings.

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

  The previous nodes.

### [**](#prevAll)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/traversing.d.ts#L197)externalprevAll

* ****prevAll**\<T>(this, selector): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

- Gets all the preceding siblings of the first selected element, optionally filtered by a selector.

  * **@example**

    ```
    $('.pear').prevAll();
    //=> [<li class="orange">Orange</li>, <li class="apple">Apple</li>]

    $('.pear').prevAll('.orange');
    //=> [<li class="orange">Orange</li>]
    ```

  * **@see**

    <https://api.jquery.com/prevAll/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externaloptionalselector: AcceptedFilters<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

    If specified filter for siblings.

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

  The previous nodes.

### [**](#prevUntil)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/traversing.d.ts#L215)externalprevUntil

* ****prevUntil**\<T>(this, selector, filterSelector): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

- Gets all the preceding siblings up to but not including the element matched by the selector, optionally filtered by another selector.

  * **@example**

    ```
    $('.pear').prevUntil('.apple');
    //=> [<li class="orange">Orange</li>]
    ```

  * **@see**

    <https://api.jquery.com/prevUntil/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externaloptionalselector: null | AcceptedFilters<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

    Selector for element to stop at.

  * ##### externaloptionalfilterSelector: AcceptedFilters<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

    If specified filter for siblings.

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

  The previous nodes.

### [**](#siblings)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/traversing.d.ts#L235)externalsiblings

* ****siblings**\<T>(this, selector): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

- Get the siblings of each element (excluding the element) in the set of matched elements, optionally filtered by a selector.

  * **@example**

    ```
    $('.pear').siblings().length;
    //=> 2

    $('.pear').siblings('.orange').length;
    //=> 1
    ```

  * **@see**

    <https://api.jquery.com/siblings/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externaloptionalselector: AcceptedFilters<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

    If specified filter for siblings.

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>

  The siblings.

### [**](#slice)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/traversing.d.ts#L593)externalslice

* ****slice**\<T>(this, start, end): [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

- Gets the elements matching the specified range (0-based position).

  * **@example**

    ```
    $('li').slice(1).eq(0).text();
    //=> 'Orange'

    $('li').slice(1, 2).length;
    //=> 1
    ```

  * **@see**

    <https://api.jquery.com/slice/>

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  * ##### externaloptionalstart: number

    A position at which the elements begin to be selected. If negative, it indicates an offset from the end of the set.

  * ##### externaloptionalend: number

    A position at which the elements stop being selected. If negative, it indicates an offset from the end of the set. If omitted, the range continues until the end of the set.

  #### Returns [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  The elements matching the specified range.

## Other<!-- -->[**](#__CATEGORY__)

### [**](#cheerio)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/cheerio.d.ts#L65)externalcheerio

**cheerio: \[cheerio object]

### [**](#length)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/cheerio.d.ts#L16)externallength

**length: number

Implementation of ArrayLike.length

### [**](#options)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/cheerio.d.ts#L18)externaloptions

**options: InternalOptions

### [**](#prevObject)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/cheerio.d.ts#L35)externalprevObject

**prevObject: undefined | [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<any>

### [**](#splice)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/cheerio.d.ts#L66)externalsplice

**splice: (start, end) => any\[]

#### Type declaration

* * **(start, end): any\[]

  - Returns a copy of a section of an array. For both start and end, a negative index can be used to indicate an offset from the end of the array. For example, -2 refers to the second to last element of the array.

    ***

    #### Parameters

    * ##### externaloptionalstart: number

      The beginning index of the specified portion of the array. If start is undefined, then the slice begins at index 0.

    * ##### externaloptionalend: number

      The end index of the specified portion of the array. This is exclusive of the element at the index 'end'. If end is undefined, then the slice extends to the end of the array.

    #### Returns any\[]

### [**](#\[iterator])[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/website/node_modules/typescript/src/lib.es2015.iterable.d.ts#L49)external\[iterator]

* ****\[iterator]**(): Iterator\<T, any, any>

- #### Returns Iterator\<T, any, any>

### [**](#filterArray)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/traversing.d.ts#L385)externalfilterArray

* ****filterArray**\<T>(nodes, match, xmlMode, root): [Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)\[] | T\[]

- #### Parameters

  * ##### externalnodes: T\[]
  * ##### externalmatch: AcceptedFilters\<T>
  * ##### externaloptionalxmlMode: boolean
  * ##### externaloptionalroot: Document

  #### Returns [Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)\[] | T\[]

### [**](#toArray)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/cheerio/src/api/traversing.d.ts#L551)externaltoArray

* ****toArray**\<T>(this): T\[]

- Retrieve all the DOM elements contained in the jQuery set as an array.

  * **@example**

    ```
    $('li').toArray();
    //=> [ {...}, {...}, {...} ]
    ```

  ***

  #### Parameters

  * ##### externalthis: [Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)\<T>

  #### Returns T\[]

  The contained items.
