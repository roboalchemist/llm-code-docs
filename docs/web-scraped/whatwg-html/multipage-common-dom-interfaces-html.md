# Source: https://html.spec.whatwg.org/multipage/common-dom-interfaces.html

Title: HTML Standard

URL Source: https://html.spec.whatwg.org/multipage/common-dom-interfaces.html

Published Time: Mon, 16 Mar 2026 07:32:47 GMT

Markdown Content:
[![Image 1: WHATWG](https://resources.whatwg.org/logo.svg)](https://whatwg.org/)
Living Standard — Last Updated 16 March 2026

[← 2.4 URLs](https://html.spec.whatwg.org/multipage/urls-and-fetching.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [2.7 Safe passing of structured data →](https://html.spec.whatwg.org/multipage/structured-data.html)
1.       1.   [2.6 Common DOM interfaces](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#common-dom-interfaces)
        1.   [2.6.1 Reflecting content attributes in IDL attributes](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflecting-content-attributes-in-idl-attributes)
        2.   [2.6.2 Using reflect via IDL extended attributes](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#using-reflect-via-idl-extended-attributes)
        3.   [2.6.3 Using reflect in specifications](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#using-reflect-in-specifications)
        4.   [2.6.4 Collections](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#collections)
            1.   [2.6.4.1 The `HTMLAllCollection` interface](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#the-htmlallcollection-interface)
                1.   [2.6.4.1.1 [[Call]] ( thisArgument, argumentsList )](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#HTMLAllCollection-call)

            2.   [2.6.4.2 The `HTMLFormControlsCollection` interface](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#the-htmlformcontrolscollection-interface)
            3.   [2.6.4.3 The `HTMLOptionsCollection` interface](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#the-htmloptionscollection-interface)

        5.   [2.6.5 The `DOMStringList` interface](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#the-domstringlist-interface)

### 2.6 Common DOM interfaces[](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#common-dom-interfaces)

#### 2.6.1 Reflecting content attributes in IDL attributes[](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflecting-content-attributes-in-idl-attributes)

The building blocks for reflecting are as follows:

*   A reflected target is an element or `ElementInternals` object. It is typically clear from context and typically identical to the interface of the [reflected IDL attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-idl-attribute). It is always identical to that interface when it is an `ElementInternals` object.

*   A reflected IDL attribute is an attribute interface member.

*   A reflected content attribute name is a string. When the [reflected target](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-target) is an element, it represents the local name of a content attribute whose namespace is null. When the [reflected target](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-target) is an `ElementInternals` object, it represents a key of the [reflected target](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-target)'s [target element](https://html.spec.whatwg.org/multipage/custom-elements.html#internals-target)'s [internal content attribute map](https://html.spec.whatwg.org/multipage/custom-elements.html#internal-content-attribute-map).

A [reflected IDL attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-idl-attribute) can be defined to reflect a [reflected content attribute name](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-content-attribute-name) of a [reflected target](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-target). In general this means that the IDL attribute getter returns the current value of the content attribute, and the setter changes the value of the content attribute to the given value.

[Reflected targets](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-target) have these associated algorithms:

*   get the element: takes no arguments; returns an element.
*   get the content attribute: takes no arguments; returns null or a string.
*   set the content attribute: takes a string value; returns nothing.
*   delete the content attribute: takes no arguments; returns nothing.

For a [reflected target](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-target) that is an element element, these are defined as follows:

[get the element](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#get-the-element)
1.   Return element.

This results in somewhat redundant data structures for `ElementInternals` objects as their [target element](https://html.spec.whatwg.org/multipage/custom-elements.html#internals-target)'s [internal content attribute map](https://html.spec.whatwg.org/multipage/custom-elements.html#internal-content-attribute-map) cannot be directly manipulated and as such reflection is only happening in a single direction. This approach was nevertheless chosen to make it less error-prone to define IDL attributes that are shared between [reflected targets](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-target) and benefit from common API semantics.

* * *

IDL attributes of type `DOMString` or `DOMString?` that [reflect](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflect)[enumerated](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#enumerated-attribute) content attributes can be limited to only known values. Per the processing models below, those will cause the getters for such IDL attributes to only return keywords for those enumerated attributes, or the empty string or null.

If a [reflected IDL attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-idl-attribute) has the type `DOMString`:

*   
The getter steps are:

    1.   Let element be the result of running [this](https://webidl.spec.whatwg.org/#this)'s [get the element](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#get-the-element).

    2.   Let contentAttributeValue be the result of running [this](https://webidl.spec.whatwg.org/#this)'s [get the content attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#get-the-content-attribute).

    3.   Let attributeDefinition be the attribute definition of element's content attribute whose namespace is null and local name is the [reflected content attribute name](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-content-attribute-name).

    4.   If attributeDefinition indicates it is an [enumerated attribute](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#enumerated-attribute) and the [reflected IDL attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-idl-attribute) is defined to be [limited to only known values](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#limited-to-only-known-values):

        1.   If contentAttributeValue does not correspond to any state of attributeDefinition (e.g., it is null and there is no _[missing value default](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#missing-value-default)_), or if it is in a state of attributeDefinition with no associated keyword value, then return the empty string.

        2.   Return the [canonical keyword](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#canonical-keyword) for the state of attributeDefinition that contentAttributeValue corresponds to.

    5.   If contentAttributeValue is null, then return the empty string.

    6.   Return contentAttributeValue.

*   The setter steps are to run [this](https://webidl.spec.whatwg.org/#this)'s [set the content attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#set-the-content-attribute) with the given value.

If a [reflected IDL attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-idl-attribute) has the type `DOMString?`:

*   
The getter steps are:

    1.   Let element be the result of running [this](https://webidl.spec.whatwg.org/#this)'s [get the element](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#get-the-element).

    2.   Let contentAttributeValue be the result of running [this](https://webidl.spec.whatwg.org/#this)'s [get the content attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#get-the-content-attribute).

    3.   Let attributeDefinition be the attribute definition of element's content attribute whose namespace is null and local name is the [reflected content attribute name](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-content-attribute-name).

    4.   If attributeDefinition indicates it is an [enumerated attribute](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#enumerated-attribute):

        1.   [Assert](https://infra.spec.whatwg.org/#assert): the [reflected IDL attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-idl-attribute) is [limited to only known values](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#limited-to-only-known-values).

        2.   [Assert](https://infra.spec.whatwg.org/#assert): contentAttributeValue corresponds to a state of attributeDefinition.

        3.   If contentAttributeValue corresponds to a state of attributeDefinition with no associated keyword value, then return null.

        4.   Return the [canonical keyword](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#canonical-keyword) for the state of attributeDefinition that contentAttributeValue corresponds to.

    5.   Return contentAttributeValue.

*   
The setter steps are:

    1.   If the given value is null, then run [this](https://webidl.spec.whatwg.org/#this)'s [delete the content attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#delete-the-content-attribute).

    2.   Otherwise, run [this](https://webidl.spec.whatwg.org/#this)'s [set the content attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#set-the-content-attribute) with the given value.

If a [reflected IDL attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-idl-attribute) has the type `USVString`, optionally treated as a URL:

*   
The getter steps are:

    1.   Let element be the result of running [this](https://webidl.spec.whatwg.org/#this)'s [get the element](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#get-the-element).

    2.   Let contentAttributeValue be the result of running [this](https://webidl.spec.whatwg.org/#this)'s [get the content attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#get-the-content-attribute).

    3.   If the [reflected IDL attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-idl-attribute) is [treated as a URL](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#treated-as-a-url):

        1.   If contentAttributeValue is null, then return the empty string.

        2.   Let urlString be the result of [encoding-parsing-and-serializing a URL](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#encoding-parsing-and-serializing-a-url) given contentAttributeValue, relative to element's [node document](https://dom.spec.whatwg.org/#concept-node-document).

        3.   If urlString is not failure, then return urlString.

    4.   Return contentAttributeValue, [converted to a scalar value string](https://infra.spec.whatwg.org/#javascript-string-convert).

*   The setter steps are to run [this](https://webidl.spec.whatwg.org/#this)'s [set the content attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#set-the-content-attribute) with the given value.

If a [reflected IDL attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-idl-attribute) has the type `boolean`:

*   
The getter steps are:

    1.   Let contentAttributeValue be the result of running [this](https://webidl.spec.whatwg.org/#this)'s [get the content attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#get-the-content-attribute).

    2.   If contentAttributeValue is null, then return false.

    3.   Return true.

*   
The setter steps are:

    1.   If the given value is false, then run [this](https://webidl.spec.whatwg.org/#this)'s [delete the content attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#delete-the-content-attribute).

    2.   If the given value is true, then run [this](https://webidl.spec.whatwg.org/#this)'s [set the content attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#set-the-content-attribute) with the empty string.

This corresponds to the rules for [boolean content attributes](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#boolean-attribute).

If a [reflected IDL attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-idl-attribute) has the type `long`, optionally limited to only non-negative numbers and optionally with a default value defaultValue:

*   
The getter steps are:

    1.   Let contentAttributeValue be the result of running [this](https://webidl.spec.whatwg.org/#this)'s [get the content attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#get-the-content-attribute).

    2.   If contentAttributeValue is not null:

        1.   Let parsedValue be the result of [integer parsing](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#rules-for-parsing-integers)contentAttributeValue if the [reflected IDL attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-idl-attribute) is not [limited to only non-negative numbers](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#limited-to-only-non-negative-numbers); otherwise the result of [non-negative integer parsing](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#rules-for-parsing-non-negative-integers)contentAttributeValue.

        2.   If parsedValue is not an error and is within the `long` range, then return parsedValue.

    3.   If the [reflected IDL attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-idl-attribute) has a [default value](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#default-value), then return defaultValue.

    4.   If the [reflected IDL attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-idl-attribute) is [limited to only non-negative numbers](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#limited-to-only-non-negative-numbers), then return −1.

    5.   Return 0.

*   
The setter steps are:

    1.   If the [reflected IDL attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-idl-attribute) is [limited to only non-negative numbers](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#limited-to-only-non-negative-numbers) and the given value is negative, then throw an ["`IndexSizeError`"](https://webidl.spec.whatwg.org/#indexsizeerror)`DOMException`.

    2.   Run [this](https://webidl.spec.whatwg.org/#this)'s [set the content attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#set-the-content-attribute) with the given value converted to the shortest possible string representing the number as a [valid integer](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#valid-integer).

If a [reflected IDL attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-idl-attribute) has the type `unsigned long`, optionally limited to only positive numbers, limited to only positive numbers with fallback, or clamped to the range [clampedMin, clampedMax], and optionally with a [default value](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#default-value)defaultValue:

*   
The getter steps are:

    1.   Let contentAttributeValue be the result of running [this](https://webidl.spec.whatwg.org/#this)'s [get the content attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#get-the-content-attribute).

    2.   Let minimum be 0.

    3.   If the [reflected IDL attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-idl-attribute) is [limited to only positive numbers](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#limited-to-only-non-negative-numbers-greater-than-zero) or [limited to only positive numbers with fallback](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#limited-to-only-non-negative-numbers-greater-than-zero-with-fallback), then set minimum to 1.

    4.   If the [reflected IDL attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-idl-attribute) is [clamped to the range](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#clamped-to-the-range), then set minimum to clampedMin.

    5.   Let maximum be 2147483647 if the [reflected IDL attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-idl-attribute) is not [clamped to the range](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#clamped-to-the-range); otherwise clampedMax.

    6.   If contentAttributeValue is not null:

        1.   Let parsedValue be the result of [non-negative integer parsing](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#rules-for-parsing-non-negative-integers)contentAttributeValue.

        2.   If parsedValue is not an error and is in the range minimum to maximum, inclusive, then return parsedValue.

        3.   If parsedValue is not an error and the [reflected IDL attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-idl-attribute) is [clamped to the range](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#clamped-to-the-range):

            1.   If parsedValue is less than minimum, then return minimum.

            2.   Return maximum.

    7.   If the [reflected IDL attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-idl-attribute) has a [default value](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#default-value), then return defaultValue.

    8.   Return minimum.

*   
The setter steps are:

    1.   If the [reflected IDL attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-idl-attribute) is [limited to only positive numbers](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#limited-to-only-non-negative-numbers-greater-than-zero) and the given value is 0, then throw an ["`IndexSizeError`"](https://webidl.spec.whatwg.org/#indexsizeerror)`DOMException`.

    2.   Let minimum be 0.

    3.   If the [reflected IDL attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-idl-attribute) is [limited to only positive numbers](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#limited-to-only-non-negative-numbers-greater-than-zero) or [limited to only positive numbers with fallback](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#limited-to-only-non-negative-numbers-greater-than-zero-with-fallback), then set minimum to 1.

    4.   Let newValue be minimum.

    5.   If the [reflected IDL attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-idl-attribute) has a [default value](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#default-value), then set newValue to defaultValue.

    6.   If the given value is in the range minimum to 2147483647, inclusive, then set newValue to it.

    7.   Run [this](https://webidl.spec.whatwg.org/#this)'s [set the content attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#set-the-content-attribute) with newValue converted to the shortest possible string representing the number as a [valid non-negative integer](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#valid-non-negative-integer).

[Clamped to the range](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#clamped-to-the-range) has no effect on the setter steps.

If a [reflected IDL attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-idl-attribute) has the type `double`, optionally [limited to only positive numbers](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#limited-to-only-non-negative-numbers-greater-than-zero) and optionally with a [default value](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#default-value)defaultValue:

*   
The getter steps are:

    1.   Let contentAttributeValue be the result of running [this](https://webidl.spec.whatwg.org/#this)'s [get the content attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#get-the-content-attribute).

    2.   If contentAttributeValue is not null:

        1.   Let parsedValue be the result of [floating-point number parsing](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#rules-for-parsing-floating-point-number-values)contentAttributeValue.

        2.   If parsedValue is not an error and is greater than 0, then return parsedValue.

        3.   If parsedValue is not an error and the [reflected IDL attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-idl-attribute) is not [limited to only positive numbers](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#limited-to-only-non-negative-numbers-greater-than-zero), then return parsedValue.

    3.   If the [reflected IDL attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-idl-attribute) has a [default value](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#default-value), then return defaultValue.

    4.   Return 0.

*   
The setter steps are:

    1.   If the [reflected IDL attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-idl-attribute) is [limited to only positive numbers](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#limited-to-only-non-negative-numbers-greater-than-zero) and the given value is not greater than 0, then return.

    2.   Run [this](https://webidl.spec.whatwg.org/#this)'s [set the content attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#set-the-content-attribute) with the given value, converted to the [best representation of the number as a floating-point number](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#best-representation-of-the-number-as-a-floating-point-number).

The values Infinity and Not-a-Number (NaN) values throw an exception on setting, as defined in Web IDL. [[WEBIDL]](https://html.spec.whatwg.org/multipage/references.html#refsWEBIDL)

If a [reflected IDL attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-idl-attribute) has the type `DOMTokenList`, then its getter steps are to return a `DOMTokenList` object whose associated element is [this](https://webidl.spec.whatwg.org/#this) and associated attribute's local name is the [reflected content attribute name](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-content-attribute-name). Specification authors cannot reflect IDL attributes of this type on `ElementInternals`.

If a [reflected IDL attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-idl-attribute) has the type `T?`, where T is either `Element` or an interface that inherits from `Element`, then with attr being the [reflected content attribute name](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-content-attribute-name):

*   Its [reflected target](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-target) has an explicitly set attr-element, which is a weak reference to an element or null. It is initially null.

*   
Its [reflected target](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-target)reflectedTarget has a get the attr-associated element algorithm, that runs these steps:

    1.   Let element be the result of running reflectedTarget's [get the element](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#get-the-element).

    2.   Let contentAttributeValue be the result of running reflectedTarget's [get the content attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#get-the-content-attribute).

    3.   If reflectedTarget's [explicitly set attr-element](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#explicitly-set-attr-element) is not null:

        1.   If reflectedTarget's [explicitly set attr-element](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#explicitly-set-attr-element) is a [descendant](https://dom.spec.whatwg.org/#concept-tree-descendant) of any of element's [shadow-including ancestors](https://dom.spec.whatwg.org/#concept-shadow-including-ancestor), then return reflectedTarget's [explicitly set attr-element](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#explicitly-set-attr-element).

        2.   Return null.

    4.   Otherwise, if contentAttributeValue is not null, return the first element candidate, in [tree order](https://dom.spec.whatwg.org/#concept-tree-order), that meets the following criteria:

        *   candidate's [root](https://dom.spec.whatwg.org/#concept-tree-root) is the same as element's [root](https://dom.spec.whatwg.org/#concept-tree-root);

        *   candidate's [ID](https://dom.spec.whatwg.org/#concept-id) is contentAttributeValue; and

        *   candidate[implements](https://webidl.spec.whatwg.org/#implements)T.

If no such element exists, then return null.

    5.   Return null.

*   The getter steps are to return the result of running [this](https://webidl.spec.whatwg.org/#this)'s [get the attr-associated element](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#attr-associated-element).

*   
The setter steps are:

    1.   If the given value is null, then:

        1.   Set [this](https://webidl.spec.whatwg.org/#this)'s [explicitly set attr-element](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#explicitly-set-attr-element) to null.

        2.   Run [this](https://webidl.spec.whatwg.org/#this)'s [delete the content attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#delete-the-content-attribute).

        3.   Return.

    2.   Run [this](https://webidl.spec.whatwg.org/#this)'s [set the content attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#set-the-content-attribute) with the empty string.

    3.   Set [this](https://webidl.spec.whatwg.org/#this)'s [explicitly set attr-element](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#explicitly-set-attr-element) to a weak reference to the given value.

*   
For element [reflected targets](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-target) only: the following [attribute change steps](https://dom.spec.whatwg.org/#concept-element-attributes-change-ext), given element, localName, oldValue, value, and namespace, are used to synchronize between the content attribute and the IDL attribute:

    1.   If localName is not attr or namespace is not null, then return.

    2.   Set element's [explicitly set attr-element](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#explicitly-set-attr-element) to null.

[Reflected IDL attributes](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-idl-attribute) of this type are strongly encouraged to have their identifier end in "`Element`" for consistency.

If a [reflected IDL attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-idl-attribute) has the type `FrozenArray<T>?`, where T is either `Element` or an interface that inherits from `Element`, then with attr being the [reflected content attribute name](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-content-attribute-name):

*   Its [reflected target](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-target) has an explicitly set attr-elements, which is either a [list](https://infra.spec.whatwg.org/#list) of weak references to elements or null. It is initially null.

*   Its [reflected target](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-target) has a cached attr-associated elements, which is a [list](https://infra.spec.whatwg.org/#list) of elements. It is initially « ».

*   Its [reflected target](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-target) has a cached attr-associated elements object, which is a `FrozenArray<T>?`. It is initially null.

*   
Its [reflected target](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-target)reflectedTarget has a get the attr-associated elements algorithm, which runs these steps:

    1.   Let elements be an empty [list](https://infra.spec.whatwg.org/#list).

    2.   Let element be the result of running reflectedTarget's [get the element](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#get-the-element).

    3.   If reflectedTarget's [explicitly set attr-elements](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#explicitly-set-attr-elements) is not null:

        1.   [For each](https://infra.spec.whatwg.org/#list-iterate)attrElement in reflectedTarget's [explicitly set attr-elements](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#explicitly-set-attr-elements):

            1.   If attrElement is not a [descendant](https://dom.spec.whatwg.org/#concept-tree-descendant) of any of element's [shadow-including ancestors](https://dom.spec.whatwg.org/#concept-shadow-including-ancestor), then [continue](https://infra.spec.whatwg.org/#iteration-continue).

            2.   [Append](https://infra.spec.whatwg.org/#list-append)attrElement to elements.

    4.   Otherwise:

        1.   Let contentAttributeValue be the result of running reflectedTarget's [get the content attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#get-the-content-attribute).

        2.   If contentAttributeValue is null, then return null.

        3.   Let tokens be contentAttributeValue, [split on ASCII whitespace](https://infra.spec.whatwg.org/#split-on-ascii-whitespace).

        4.   [For each](https://infra.spec.whatwg.org/#list-iterate)id of tokens:

            1.   Let candidate be the first element, in [tree order](https://dom.spec.whatwg.org/#concept-tree-order), that meets the following criteria:

                *   candidate's [root](https://dom.spec.whatwg.org/#concept-tree-root) is the same as element's [root](https://dom.spec.whatwg.org/#concept-tree-root);

                *   candidate's [ID](https://dom.spec.whatwg.org/#concept-id) is id; and

                *   candidate[implements](https://webidl.spec.whatwg.org/#implements)T.

If no such element exists, then [continue](https://infra.spec.whatwg.org/#iteration-continue).

            2.   [Append](https://infra.spec.whatwg.org/#list-append)candidate to elements.

    5.   Return elements.

*   
The getter steps are:

    1.   Let elements be the result of running [this](https://webidl.spec.whatwg.org/#this)'s [get the attr-associated elements](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#attr-associated-elements).

    2.   If the contents of elements is equal to the contents of [this](https://webidl.spec.whatwg.org/#this)'s [cached attr-associated elements](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#cached-attr-associated-elements), then return [this](https://webidl.spec.whatwg.org/#this)'s [cached attr-associated elements object](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#cached-attr-associated-elements-object).

    3.   Let elementsAsFrozenArray be elements, [converted](https://webidl.spec.whatwg.org/#es-type-mapping) to a `FrozenArray<T>?`.

    4.   Set [this](https://webidl.spec.whatwg.org/#this)'s [cached attr-associated elements](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#cached-attr-associated-elements) to elements.

    5.   Set [this](https://webidl.spec.whatwg.org/#this)'s [cached attr-associated elements object](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#cached-attr-associated-elements-object) to elementsAsFrozenArray.

    6.   Return elementsAsFrozenArray.

This extra caching layer is necessary to preserve the invariant that `element.reflectedElements === element.reflectedElements`.

*   
The setter steps are:

    1.   If the given value is null:

        1.   Set [this](https://webidl.spec.whatwg.org/#this)'s [explicitly set attr-elements](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#explicitly-set-attr-elements) to null.

        2.   Run [this](https://webidl.spec.whatwg.org/#this)'s [delete the content attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#delete-the-content-attribute).

        3.   Return.

    2.   Run [this](https://webidl.spec.whatwg.org/#this)'s [set the content attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#set-the-content-attribute) with the empty string.

    3.   Let elements be an empty [list](https://infra.spec.whatwg.org/#list).

    4.   [For each](https://infra.spec.whatwg.org/#list-iterate)element in the given value:

        1.   [Append](https://infra.spec.whatwg.org/#list-append) a weak reference to element to elements.

    5.   Set [this](https://webidl.spec.whatwg.org/#this)'s [explicitly set attr-elements](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#explicitly-set-attr-elements) to elements.

*   
For element [reflected targets](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-target) only: the following [attribute change steps](https://dom.spec.whatwg.org/#concept-element-attributes-change-ext), given element, localName, oldValue, value, and namespace, are used to synchronize between the content attribute and the IDL attribute:

    1.   If localName is not attr or namespace is not null, then return.

    2.   Set element's [explicitly set attr-elements](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#explicitly-set-attr-elements) to null.

[Reflected IDL attributes](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-idl-attribute) of this type are strongly encouraged to have their identifier end in "`Elements`" for consistency.

#### 2.6.2 Using reflect via IDL extended attributes[](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#using-reflect-via-idl-extended-attributes)

[Reflection](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflect) can be used from IDL through [extended attributes](https://webidl.spec.whatwg.org/#dfn-extended-attribute). `[Reflect]`, `[ReflectSetter]`, `[ReflectURL]`, `[ReflectNonNegative]`, `[ReflectPositive]`, and `[ReflectPositiveWithFallback]` all trigger [reflection](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflect). These must either take no arguments, or take a string; they must not appear on anything other than an interface member attribute; and only one of these can be used at a time.

For one of these primary reflection [extended attributes](https://webidl.spec.whatwg.org/#dfn-extended-attribute), its [reflected content attribute name](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-content-attribute-name) is the string value it takes, if one is provided; otherwise it is the IDL attribute name [converted to ASCII lowercase](https://infra.spec.whatwg.org/#ascii-lowercase).

IDL attributes with the `[Reflect]`[extended attribute](https://webidl.spec.whatwg.org/#dfn-extended-attribute) must [reflect](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflect)`[Reflect]`'s [reflected content attribute name](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-content-attribute-name).

IDL attributes with the `[ReflectSetter]`[extended attribute](https://webidl.spec.whatwg.org/#dfn-extended-attribute) on setting must [reflect](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflect)`[ReflectSetter]`'s [reflected content attribute name](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-content-attribute-name).

The `[ReflectURL]`[extended attribute](https://webidl.spec.whatwg.org/#dfn-extended-attribute) must only appear on attributes with a type of `USVString`.

IDL attributes with the `[ReflectURL]`[extended attribute](https://webidl.spec.whatwg.org/#dfn-extended-attribute) must [reflect](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflect), [as a URL](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#treated-as-a-url), `[ReflectURL]`'s [reflected content attribute name](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-content-attribute-name).

The `[ReflectNonNegative]`[extended attribute](https://webidl.spec.whatwg.org/#dfn-extended-attribute) must only appear on attributes with a type of `long`.

IDL attributes with the `[ReflectNonNegative]`[extended attribute](https://webidl.spec.whatwg.org/#dfn-extended-attribute) must [reflect](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflect), [limited to only non-negative numbers](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#limited-to-only-non-negative-numbers), `[ReflectNonNegative]`'s [reflected content attribute name](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-content-attribute-name).

The `[ReflectPositive]` and `[ReflectPositiveWithFallback]`[extended attributes](https://webidl.spec.whatwg.org/#dfn-extended-attribute) must only appear on attributes with a type of `double` or 
```
unsigned
  long
```
.

IDL attributes with the `[ReflectPositive]`[extended attribute](https://webidl.spec.whatwg.org/#dfn-extended-attribute) must [reflect](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflect), [limited to only positive numbers](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#limited-to-only-non-negative-numbers-greater-than-zero), `[ReflectPositive]`'s [reflected content attribute name](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-content-attribute-name).

IDL attributes with the `[ReflectPositiveWithFallback]`[extended attribute](https://webidl.spec.whatwg.org/#dfn-extended-attribute) must [reflect](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflect), [limited to only positive numbers with fallback](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#limited-to-only-non-negative-numbers-greater-than-zero-with-fallback), `[ReflectPositiveWithFallback]`'s [reflected content attribute name](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-content-attribute-name).

* * *

To supplement the above [extended attributes](https://webidl.spec.whatwg.org/#dfn-extended-attribute) we also introduce `[ReflectRange]`, and `[ReflectDefault]`. These augment how [reflection](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflect) works and also must only appear on interface member attributes.

The `[ReflectRange]`[extended attribute](https://webidl.spec.whatwg.org/#dfn-extended-attribute) must take an integer list limited to two values. It must only be used on attributes with a type of `unsigned long`. Additionally, it must also only appear alongside `[Reflect]`.

IDL attributes with the `[ReflectRange]`[extended attribute](https://webidl.spec.whatwg.org/#dfn-extended-attribute) are [clamped to the range](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#clamped-to-the-range) [clampedMin, clampedMax] where clampedMin is the first, and clampedMax is the second argument to the list provided to `[ReflectRange]`.

The `[ReflectDefault]`[extended attribute](https://webidl.spec.whatwg.org/#dfn-extended-attribute) must only be used on attributes with a type of `double`, `long`, or `unsigned long`. When used on an attribute of type `double`, it must take a decimal; otherwise it must take an integer. Additionally, it must also only appear alongside `[Reflect]`, `[ReflectNonNegative]`, `[ReflectPositive]`, or `[ReflectPositiveWithFallback]`.

IDL attributes with the `[ReflectDefault]`[extended attribute](https://webidl.spec.whatwg.org/#dfn-extended-attribute) have a [default value](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#default-value) provided by the argument provided to `[ReflectDefault]`.

#### 2.6.3 Using reflect in specifications[](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#using-reflect-in-specifications)

[Reflection](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflect) is primarily about improving web developer ergonomics by giving them typed access to content attributes through [reflected IDL attributes](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-idl-attribute). The ultimate source of truth, which the web platform builds upon, is the content attributes themselves. That is, specification authors must not use the [reflected IDL attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-idl-attribute) getter or setter steps, but instead must use the content attribute presence and value. (Or an abstraction on top, such as the state of an [enumerated attribute](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#enumerated-attribute).)

Two important exceptions to this are [reflected IDL attributes](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-idl-attribute) whose type is one of the following:

*   `T?`, where T is either `Element` or an interface that inherits from `Element`

*   `FrozenArray<T>?`, where T is either `Element` or an interface that inherits from `Element`

For those, specification authors must use the [reflected target](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-target)'s [get the attr-associated element](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#attr-associated-element) and [get the attr-associated elements](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#attr-associated-elements), respectively. The content attribute presence and value must not be used as they cannot be fully synchronized with the [reflected IDL attribute](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-idl-attribute).

A [reflected target](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflected-target)'s [explicitly set attr-element](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#explicitly-set-attr-element), [explicitly set attr-elements](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#explicitly-set-attr-elements), [cached attr-associated elements](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#cached-attr-associated-elements), and [cached attr-associated elements object](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#cached-attr-associated-elements-object) are to be treated as internal implementation details and not to be built upon.

#### 2.6.4 Collections[](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#collections)

The `HTMLFormControlsCollection` and `HTMLOptionsCollection` interfaces are [collections](https://dom.spec.whatwg.org/#concept-collection) derived from the `HTMLCollection` interface. The `HTMLAllCollection` interface is a [collection](https://dom.spec.whatwg.org/#concept-collection), but is not so derived.

##### 2.6.4.1 The `HTMLAllCollection` interface[](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#the-htmlallcollection-interface)

The `HTMLAllCollection` interface is used for the legacy `document.all` attribute. It operates similarly to `HTMLCollection`; the main differences are that it allows a staggering variety of different (ab)uses of its methods to all end up returning something, and that it can be called as a function as an alternative to property access.

All `HTMLAllCollection` objects are rooted at a `Document` and have a filter that matches all elements, so the elements [represented by the collection](https://dom.spec.whatwg.org/#represented-by-the-collection) of an `HTMLAllCollection` object consist of all the descendant elements of the root `Document`.

Objects that implement the `HTMLAllCollection` interface are [legacy platform objects](https://webidl.spec.whatwg.org/#dfn-legacy-platform-object) with an additional [[Call]] internal method described in the [section below](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#HTMLAllCollection-call). They also have an [[[IsHTMLDDA]]](https://tc39.es/ecma262/#sec-IsHTMLDDA-internal-slot) internal slot.

Objects that implement the `HTMLAllCollection` interface have several unusual behaviors, due of the fact that they have an [[[IsHTMLDDA]]](https://tc39.es/ecma262/#sec-IsHTMLDDA-internal-slot) internal slot:

*   The [ToBoolean](https://tc39.es/ecma262/#sec-toboolean) abstract operation in JavaScript returns false when given objects implementing the `HTMLAllCollection` interface.

*   The [IsLooselyEqual](https://tc39.es/ecma262/#sec-islooselyequal) abstract operation, when given objects implementing the `HTMLAllCollection` interface, returns true when compared to the `undefined` and `null` values. (Comparisons using the [IsStrictlyEqual](https://tc39.es/ecma262/#sec-isstrictlyequal) abstract operation, and IsLooselyEqual comparisons to other values such as strings or objects, are unaffected.)

*   The `typeof` operator in JavaScript returns the string `"undefined"` when applied to objects implementing the `HTMLAllCollection` interface.

These special behaviors are motivated by a desire for compatibility with two classes of legacy content: one that uses the presence of `document.all` as a way to detect legacy user agents, and one that only supports those legacy user agents and uses the `document.all` object without testing for its presence first. [[JAVASCRIPT]](https://html.spec.whatwg.org/multipage/references.html#refsJAVASCRIPT)

```
[Exposed=Window,
 LegacyUnenumerableNamedProperties]
interface HTMLAllCollection {
  readonly attribute unsigned long length;
  getter Element (unsigned long index);
  getter (HTMLCollection or Element)? namedItem(DOMString name);
  (HTMLCollection or Element)? item(optional DOMString nameOrIndex);

  // Note: HTMLAllCollection objects have a custom [[Call]] internal method and an [[IsHTMLDDA]] internal slot.
};
```

The [supported property names](https://webidl.spec.whatwg.org/#dfn-supported-property-names) consist of the non-empty values of all the `id` attributes of all the elements [represented by the collection](https://dom.spec.whatwg.org/#represented-by-the-collection), and the non-empty values of all the `name` attributes of all the ["all"-named elements](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#all-named-elements)[represented by the collection](https://dom.spec.whatwg.org/#represented-by-the-collection), in [tree order](https://dom.spec.whatwg.org/#concept-tree-order), ignoring later duplicates, with the `id` of an element preceding its `name` if it contributes both, they differ from each other, and neither is the duplicate of an earlier entry.

The indexed property getter must return the result of [getting the "all"-indexed element](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#concept-get-all-indexed) from [this](https://webidl.spec.whatwg.org/#this) given the passed index.

The `namedItem(name)` method steps are to return the result of [getting the "all"-named element(s)](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#concept-get-all-named) from [this](https://webidl.spec.whatwg.org/#this) given name.

The `item(nameOrIndex)` method steps are:

1.   If nameOrIndex was not provided, return null.

2.   Return the result of [getting the "all"-indexed or named element(s)](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#concept-get-all-indexed-or-named) from [this](https://webidl.spec.whatwg.org/#this), given nameOrIndex.

* * *

The following elements are "all"-named elements: `a`, `button`, `embed`, `form`, `frame`, `frameset`, `iframe`, `img`, `input`, `map`, `meta`, `object`, `select`, and `textarea`

To get the "all"-indexed element from an `HTMLAllCollection`collection given an index index, return the index th element in collection, or null if there is no such index th element.

To get the "all"-named element(s) from an `HTMLAllCollection`collection given a name name, perform the following steps:

1.   If name is the empty string, return null.

2.   Let subCollection be an `HTMLCollection` object rooted at the same `Document` as collection, whose filter matches only elements that are either:

    *   ["all"-named elements](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#all-named-elements) with a `name` attribute equal to name, or

    *   elements with an [ID](https://dom.spec.whatwg.org/#concept-id) equal to name.

3.   If there is exactly one element in subCollection, then return that element.

4.   Otherwise, if subCollection is empty, return null.

5.   Otherwise, return subCollection.

To get the "all"-indexed or named element(s) from an `HTMLAllCollection`collection given nameOrIndex:

1.   If nameOrIndex, [converted](https://webidl.spec.whatwg.org/#es-type-mapping) to a JavaScript String value, is an [array index property name](https://webidl.spec.whatwg.org/#dfn-array-index-property-name), return the result of [getting the "all"-indexed element](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#concept-get-all-indexed) from collection given the number represented by nameOrIndex.

2.   Return the result of [getting the "all"-named element(s)](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#concept-get-all-named) from collection given nameOrIndex.

###### 2.6.4.1.1 [[Call]] ( thisArgument, argumentsList )[](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#HTMLAllCollection-call)

1.   If argumentsList's [size](https://infra.spec.whatwg.org/#list-size) is zero, or if argumentsList[0] is undefined, return null.

2.   Let nameOrIndex be the result of [converting](https://webidl.spec.whatwg.org/#es-type-mapping)argumentsList[0] to a `DOMString`.

3.   Let result be the result of [getting the "all"-indexed or named element(s)](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#concept-get-all-indexed-or-named) from this `HTMLAllCollection` given nameOrIndex.

4.   Return the result of [converting](https://webidl.spec.whatwg.org/#es-type-mapping)result to an ECMAScript value.

The thisArgument is ignored, and thus code such as `Function.prototype.call.call(document.all, null, "x")` will still search for elements. (`document.all.call` does not exist, since `document.all` does not inherit from `Function.prototype`.)

##### 2.6.4.2 The `HTMLFormControlsCollection` interface[](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#the-htmlformcontrolscollection-interface)

The `HTMLFormControlsCollection` interface is used for [collections](https://dom.spec.whatwg.org/#concept-collection) of [listed elements](https://html.spec.whatwg.org/multipage/forms.html#category-listed) in `form` elements.

[HTMLFormControlsCollection](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormControlsCollection "The HTMLFormControlsCollection interface represents a collection of HTML form control elements, returned by the HTMLFormElement interface's elements property.")

Support in all current engines.

Firefox 1+Safari 4+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer No

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

[RadioNodeList](https://developer.mozilla.org/en-US/docs/Web/API/RadioNodeList "The RadioNodeList interface represents a collection of radio elements in a <form> or a <fieldset> element.")

Support in all current engines.

Firefox 33+Safari 7+Chrome 21+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 9+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

```
[Exposed=Window]
interface HTMLFormControlsCollection : HTMLCollection {
  // inherits length and item()
  getter (RadioNodeList or Element)? namedItem(DOMString name); // shadows inherited namedItem()
};

[Exposed=Window]
interface RadioNodeList : NodeList {
  attribute DOMString value;
};
```
`collection.length`
Returns the number of elements in collection.

`element = collection.item(index)``element = collection[index]`
Returns the item at index index in collection. The items are sorted in [tree order](https://dom.spec.whatwg.org/#concept-tree-order).

`element = collection.namedItem(name)`

[HTMLFormControlsCollection/namedItem](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormControlsCollection/namedItem "The HTMLFormControlsCollection.namedItem() method returns the RadioNodeList or the Element in the collection whose name or id match the specified name, or null if no node matches.")

Support in all current engines.

Firefox 33+Safari 4+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer No

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

`radioNodeList = collection.namedItem(name)``element = collection[name]``radioNodeList = collection[name]`
Returns the item with [ID](https://dom.spec.whatwg.org/#concept-id) or `name`name from collection.

If there are multiple matching items, then a `RadioNodeList` object containing all those elements is returned.

`radioNodeList.value`
Returns the value of the first checked radio button represented by radioNodeList.

`radioNodeList.value = value`
Checks the first radio button represented by radioNodeList that has value value.

The [supported property names](https://webidl.spec.whatwg.org/#dfn-supported-property-names) consist of the non-empty values of all the `id` and `name` attributes of all the elements [represented by the collection](https://dom.spec.whatwg.org/#represented-by-the-collection), in [tree order](https://dom.spec.whatwg.org/#concept-tree-order), ignoring later duplicates, with the `id` of an element preceding its `name` if it contributes both, they differ from each other, and neither is the duplicate of an earlier entry.

The `namedItem(name)` method must act according to the following algorithm:

1.   If name is the empty string, return null and stop the algorithm.
2.   If, at the time the method is called, there is exactly one node in the collection that has either an `id` attribute or a `name` attribute equal to name, then return that node and stop the algorithm.
3.   Otherwise, if there are no nodes in the collection that have either an `id` attribute or a `name` attribute equal to name, then return null and stop the algorithm.
4.   Otherwise, create a new `RadioNodeList` object representing a [live](https://html.spec.whatwg.org/multipage/infrastructure.html#live) view of the `HTMLFormControlsCollection` object, further filtered so that the only nodes in the `RadioNodeList` object are those that have either an `id` attribute or a `name` attribute equal to name. The nodes in the `RadioNodeList` object must be sorted in [tree order](https://dom.spec.whatwg.org/#concept-tree-order).
5.   Return that `RadioNodeList` object.

* * *

Members of the `RadioNodeList` interface inherited from the `NodeList` interface must behave as they would on a `NodeList` object.

[RadioNodeList/value](https://developer.mozilla.org/en-US/docs/Web/API/RadioNodeList/value "If the underlying element collection contains radio buttons, the RadioNodeList.value property represents the checked radio button. On retrieving the value property, the value of the currently checked radio button is returned as a string. If the collection does not contain any radio buttons or none of the radio buttons in the collection is in checked state, the empty string is returned. On setting the value property, the first radio button input element whose value property is equal to the new value will be set to checked.")

Support in all current engines.

Firefox 33+Safari 7+Chrome 21+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 9+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

The `value` IDL attribute on the `RadioNodeList` object, on getting, must return the value returned by running the following steps:

1.   Let element be the first element in [tree order](https://dom.spec.whatwg.org/#concept-tree-order) represented by the `RadioNodeList` object that is an `input` element whose `type` attribute is in the [Radio Button](https://html.spec.whatwg.org/multipage/input.html#radio-button-state-(type=radio)) state and whose [checkedness](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-fe-checked) is true. Otherwise, let it be null.

2.   If element is null, return the empty string.

3.   If element is an element with no `value` attribute, return the string "`on`".

4.   Otherwise, return the value of element's `value` attribute.

On setting, the `value` IDL attribute must run the following steps:

1.   If the new value is the string "`on`": let element be the first element in [tree order](https://dom.spec.whatwg.org/#concept-tree-order) represented by the `RadioNodeList` object that is an `input` element whose `type` attribute is in the [Radio Button](https://html.spec.whatwg.org/multipage/input.html#radio-button-state-(type=radio)) state and whose `value` content attribute is either absent, or present and equal to the new value, if any. If no such element exists, then instead let element be null.

Otherwise: let element be the first element in [tree order](https://dom.spec.whatwg.org/#concept-tree-order) represented by the `RadioNodeList` object that is an `input` element whose `type` attribute is in the [Radio Button](https://html.spec.whatwg.org/multipage/input.html#radio-button-state-(type=radio)) state and whose `value` content attribute is present and equal to the new value, if any. If no such element exists, then instead let element be null.

2.   If element is not null, then set its [checkedness](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-fe-checked) to true.

##### 2.6.4.3 The `HTMLOptionsCollection` interface[](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#the-htmloptionscollection-interface)

[HTMLOptionsCollection](https://developer.mozilla.org/en-US/docs/Web/API/HTMLOptionsCollection "The HTMLOptionsCollection interface represents a collection of <option> HTML elements (in document order) and offers methods and properties for selecting from the list as well as optionally altering its items. This object is returned only by the options property of select.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 6+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android 37+Samsung Internet?Opera Android 12.1+

The `HTMLOptionsCollection` interface is used for [collections](https://dom.spec.whatwg.org/#concept-collection) of `option` elements. It is always rooted on a `select` element and has attributes and methods that manipulate that element's descendants.

```
[Exposed=Window]
interface HTMLOptionsCollection : HTMLCollection {
  // inherits item(), namedItem()
  [CEReactions] attribute unsigned long length; // shadows inherited length
  [CEReactions] setter undefined (unsigned long index, HTMLOptionElement? option);
  [CEReactions] undefined add((HTMLOptionElement or HTMLOptGroupElement) element, optional (HTMLElement or long)? before = null);
  [CEReactions] undefined remove(long index);
  attribute long selectedIndex;
};
```
`collection.length`
Returns the number of elements in collection.

`collection.length = value`
When set to a smaller number than the existing length, truncates the number of `option` elements in the container corresponding to collection.

When set to a greater number than the existing length, if that number is less than or equal to 100000, adds new blank `option` elements to the container corresponding to collection.

`element = collection.item(index)``element = collection[index]`
Returns the item at index index in collection. The items are sorted in [tree order](https://dom.spec.whatwg.org/#concept-tree-order).

`collection[index] = element`
When index is a greater number than the number of items in collection, adds new blank `option` elements in the corresponding container.

When set to null, removes the item at index index from collection.

When set to an `option` element, adds or replaces it at index index in collection.

`element = collection.namedItem(name)``element = collection[name]`
Returns the item with [ID](https://dom.spec.whatwg.org/#concept-id) or `name`name from collection.

If there are multiple matching items, then the first is returned.

`collection.add(element[, before])`
Inserts element before the node given by before.

The before argument can be a number, in which case element is inserted before the item with that number, or an element from collection, in which case element is inserted before that element.

If before is omitted, null, or a number out of range, then element will be added at the end of the list.

Throws a ["`HierarchyRequestError`"](https://webidl.spec.whatwg.org/#hierarchyrequesterror)`DOMException` if element is an ancestor of the element into which it is to be inserted.

`collection.remove(index)`
Removes the item with index index from collection.

`collection.selectedIndex`
Returns the index of the first selected item, if any, or −1 if there is no selected item.

`collection.selectedIndex = index`
Changes the selection to the `option` element at index index in collection.

The `length` setter steps are:

1.   Let current be the number of nodes [represented by the collection](https://dom.spec.whatwg.org/#represented-by-the-collection).

2.   If the given value is greater than current, then:

    1.   If the given value is greater than 100,000, then return.

    2.   Let n be value − current.

    3.   Append n new `option` elements with no attributes and no child nodes to the `select` element on which [this](https://webidl.spec.whatwg.org/#this) is rooted.

3.   If the given value is less than current, then:

    1.   Let n be current − value.

    2.   Remove the last n nodes in the collection from their parent nodes.

Setting `length` never removes or adds any `optgroup` elements, and never adds new children to existing `optgroup` elements (though it can remove children from them).

The [supported property names](https://webidl.spec.whatwg.org/#dfn-supported-property-names) consist of the non-empty values of all the `id` and `name` attributes of all the elements [represented by the collection](https://dom.spec.whatwg.org/#represented-by-the-collection), in [tree order](https://dom.spec.whatwg.org/#concept-tree-order), ignoring later duplicates, with the `id` of an element preceding its `name` if it contributes both, they differ from each other, and neither is the duplicate of an earlier entry.

The `add(element, before)` method must act according to the following algorithm:

1.   If element is an ancestor of the `select` element on which the `HTMLOptionsCollection` is rooted, then throw a ["`HierarchyRequestError`"](https://webidl.spec.whatwg.org/#hierarchyrequesterror)`DOMException`.

2.   If before is an element, but that element isn't a descendant of the `select` element on which the `HTMLOptionsCollection` is rooted, then throw a ["`NotFoundError`"](https://webidl.spec.whatwg.org/#notfounderror)`DOMException`.

3.   If element and before are the same element, then return.

4.   If before is a node, then let reference be that node. Otherwise, if before is an integer, and there is a before th node in the collection, let reference be that node. Otherwise, let reference be null.

5.   If reference is not null, let parent be the parent node of reference. Otherwise, let parent be the `select` element on which the `HTMLOptionsCollection` is rooted.

6.   [Pre-insert](https://dom.spec.whatwg.org/#concept-node-pre-insert)element into parent node before reference.

The `remove(index)` method must act according to the following algorithm:

1.   If the number of nodes [represented by the collection](https://dom.spec.whatwg.org/#represented-by-the-collection) is zero, return.

2.   If index is not a number greater than or equal to 0 and less than the number of nodes [represented by the collection](https://dom.spec.whatwg.org/#represented-by-the-collection), return.

3.   Let element be the index th element in the collection.

4.   Remove element from its parent node.

The `selectedIndex` IDL attribute must act like the identically named attribute on the `select` element on which the `HTMLOptionsCollection` is rooted

#### 2.6.5 The `DOMStringList` interface[](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#the-domstringlist-interface)

[DOMStringList](https://developer.mozilla.org/en-US/docs/Web/API/DOMStringList "The DOMString interface is a legacy type returned by some APIs and represents a non-modifiable list of strings (DOMString). Modern APIs use Array objects (in WebIDL: sequence<DOMString>) instead.")

Support in all current engines.

Firefox 1+Safari 5.1+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android 3+Samsung Internet?Opera Android 12.1+

The `DOMStringList` interface is a non-fashionable retro way of representing a list of strings.

```
[Exposed=(Window,Worker)]
interface DOMStringList {
  readonly attribute unsigned long length;
  getter DOMString? item(unsigned long index);
  boolean contains(DOMString string);
};
```

New APIs must use `sequence<DOMString>` or equivalent rather than `DOMStringList`.

`strings.length`
Returns the number of strings in strings.

`strings[index]``strings.item(index)`
Returns the string with index index from strings.

`strings.contains(string)`
Returns true if strings contains string, and false otherwise.

Each `DOMStringList` object has an associated [list](https://infra.spec.whatwg.org/#list).

[DOMStringList/length](https://developer.mozilla.org/en-US/docs/Web/API/DOMStringList/length "The read-only length property indicates the number of strings in the DOMStringList.")

Support in all current engines.

Firefox 1+Safari 5.1+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android 37+Samsung Internet?Opera Android 12.1+

The `length` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)'s associated list's [size](https://infra.spec.whatwg.org/#list-size).

[DOMStringList/item](https://developer.mozilla.org/en-US/docs/Web/API/DOMStringList/item "The item() method returns a string from a DOMStringList by index.")

Support in all current engines.

Firefox 1+Safari 5.1+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android 3+Samsung Internet?Opera Android 12.1+

The `item(index)` method steps are to return the index th item in [this](https://webidl.spec.whatwg.org/#this)'s associated list, or null if index plus one is greater than [this](https://webidl.spec.whatwg.org/#this)'s associated list's [size](https://infra.spec.whatwg.org/#list-size).

[DOMStringList/contains](https://developer.mozilla.org/en-US/docs/Web/API/DOMStringList/contains "The contains() method returns a boolean indicating whether the given string is in the list.")

Support in all current engines.

Firefox 1.5+Safari 5.1+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android 3+Samsung Internet?Opera Android 12.1+

The `contains(string)` method steps are to return true if [this](https://webidl.spec.whatwg.org/#this)'s associated list [contains](https://infra.spec.whatwg.org/#list-contain)string, and false otherwise.

[← 2.4 URLs](https://html.spec.whatwg.org/multipage/urls-and-fetching.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [2.7 Safe passing of structured data →](https://html.spec.whatwg.org/multipage/structured-data.html)
