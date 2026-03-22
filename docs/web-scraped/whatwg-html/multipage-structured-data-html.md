# Source: https://html.spec.whatwg.org/multipage/structured-data.html

Title: HTML Standard

URL Source: https://html.spec.whatwg.org/multipage/structured-data.html

Published Time: Mon, 16 Mar 2026 07:32:47 GMT

Markdown Content:
[![Image 1: WHATWG](https://resources.whatwg.org/logo.svg)](https://whatwg.org/)
Living Standard — Last Updated 16 March 2026

[← 2.6 Common DOM interfaces](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [3 Semantics, structure, and APIs of HTML documents →](https://html.spec.whatwg.org/multipage/dom.html)
1.       1.   [2.7 Safe passing of structured data](https://html.spec.whatwg.org/multipage/structured-data.html#safe-passing-of-structured-data)
        1.   [2.7.1 Serializable objects](https://html.spec.whatwg.org/multipage/structured-data.html#serializable-objects)
        2.   [2.7.2 Transferable objects](https://html.spec.whatwg.org/multipage/structured-data.html#transferable-objects)
        3.   [2.7.3 StructuredSerializeInternal ( value, forStorage [ , memory ] )](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializeinternal)
        4.   [2.7.4 StructuredSerialize ( value )](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserialize)
        5.   [2.7.5 StructuredSerializeForStorage ( value )](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializeforstorage)
        6.   [2.7.6 StructuredDeserialize ( serialized, targetRealm [ , memory ] )](https://html.spec.whatwg.org/multipage/structured-data.html#structureddeserialize)
        7.   [2.7.7 StructuredSerializeWithTransfer ( value, transferList )](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializewithtransfer)
        8.   [2.7.8 StructuredDeserializeWithTransfer ( serializeWithTransferResult, targetRealm )](https://html.spec.whatwg.org/multipage/structured-data.html#structureddeserializewithtransfer)
        9.   [2.7.9 Performing serialization and transferring from other specifications](https://html.spec.whatwg.org/multipage/structured-data.html#performing-structured-clones-from-other-specifications)
        10.   [2.7.10 Structured cloning API](https://html.spec.whatwg.org/multipage/structured-data.html#structured-cloning)

### 2.7 Safe passing of structured data[](https://html.spec.whatwg.org/multipage/structured-data.html#safe-passing-of-structured-data)

To support passing JavaScript objects, including [platform objects](https://webidl.spec.whatwg.org/#dfn-platform-object), across [realm](https://tc39.es/ecma262/#sec-code-realms) boundaries, this specification defines the following infrastructure for serializing and deserializing objects, including in some cases transferring the underlying data instead of copying it. Collectively this serialization/deserialization process is known as "structured cloning", although most APIs perform separate serialization and deserialization steps. (With the notable exception being the `structuredClone()` method.)

This section uses the terminology and typographic conventions from the JavaScript specification. [[JAVASCRIPT]](https://html.spec.whatwg.org/multipage/references.html#refsJAVASCRIPT)

#### 2.7.1 Serializable objects[](https://html.spec.whatwg.org/multipage/structured-data.html#serializable-objects)

[Serializable objects](https://html.spec.whatwg.org/multipage/structured-data.html#serializable-objects) support being serialized, and later deserialized, in a way that is independent of any given [realm](https://tc39.es/ecma262/#sec-code-realms). This allows them to be stored on disk and later restored, or cloned across [agent](https://tc39.es/ecma262/#sec-agents) and even [agent cluster](https://tc39.es/ecma262/#sec-agent-clusters) boundaries.

Not all objects are [serializable objects](https://html.spec.whatwg.org/multipage/structured-data.html#serializable-objects), and not all aspects of objects that are [serializable objects](https://html.spec.whatwg.org/multipage/structured-data.html#serializable-objects) are necessarily preserved when they are serialized.

[Platform objects](https://webidl.spec.whatwg.org/#dfn-platform-object) can be [serializable objects](https://html.spec.whatwg.org/multipage/structured-data.html#serializable-objects) if their [primary interface](https://webidl.spec.whatwg.org/#dfn-primary-interface) is decorated with the `[Serializable]` IDL [extended attribute](https://webidl.spec.whatwg.org/#dfn-extended-attribute). Such interfaces must also define the following algorithms:

serialization steps, taking a [platform object](https://webidl.spec.whatwg.org/#dfn-platform-object)value, a [Record](https://tc39.es/ecma262/#sec-list-and-record-specification-type)serialized, and a boolean forStorage
A set of steps that serializes the data in value into fields of serialized. The resulting data serialized into serialized must be independent of any [realm](https://tc39.es/ecma262/#sec-code-realms).

These steps may throw an exception if serialization is not possible.

These steps may perform a [sub-serialization](https://html.spec.whatwg.org/multipage/structured-data.html#sub-serialization) to serialize nested data structures. They should not call [StructuredSerialize](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserialize) directly, as doing so will omit the important memory argument.

The introduction of these steps should omit mention of the forStorage argument if it is not relevant to the algorithm.

deserialization steps, taking a [Record](https://tc39.es/ecma262/#sec-list-and-record-specification-type)serialized, a [platform object](https://webidl.spec.whatwg.org/#dfn-platform-object)value, and a [realm](https://tc39.es/ecma262/#sec-code-realms)targetRealm
A set of steps that deserializes the data in serialized, using it to set up value as appropriate. value will be a newly-created instance of the [platform object](https://webidl.spec.whatwg.org/#dfn-platform-object) type in question, with none of its internal data set up; setting that up is the job of these steps.

These steps may throw an exception if deserialization is not possible.

These steps may perform a [sub-deserialization](https://html.spec.whatwg.org/multipage/structured-data.html#sub-deserialization) to deserialize nested data structures. They should not call [StructuredDeserialize](https://html.spec.whatwg.org/multipage/structured-data.html#structureddeserialize) directly, as doing so will omit the important targetRealm and memory arguments.

It is up to the definition of individual platform objects to determine what data is serialized and deserialized by these steps. Typically the steps are very symmetric.

The `[Serializable]` extended attribute must take no arguments, and must only appear on an interface. It must not appear more than once on an interface.

For a given [platform object](https://webidl.spec.whatwg.org/#dfn-platform-object), only the object's [primary interface](https://webidl.spec.whatwg.org/#dfn-primary-interface) is considered during the (de)serialization process. Thus, if inheritance is involved in defining the interface, each `[Serializable]`-annotated interface in the inheritance chain needs to define standalone [serialization steps](https://html.spec.whatwg.org/multipage/structured-data.html#serialization-steps) and [deserialization steps](https://html.spec.whatwg.org/multipage/structured-data.html#deserialization-steps), including taking into account any important data that might come from inherited interfaces.

Let's say we were defining a platform object `Person`, which had associated with it two pieces of associated data:

*   a name value, which is a string; and

*   a best friend value, which is either another `Person` instance or null.

We could then define `Person` instances to be [serializable objects](https://html.spec.whatwg.org/multipage/structured-data.html#serializable-objects) by annotating the `Person` interface with the `[Serializable]`[extended attribute](https://webidl.spec.whatwg.org/#dfn-extended-attribute), and defining the following accompanying algorithms:

Their [serialization steps](https://html.spec.whatwg.org/multipage/structured-data.html#serialization-steps), given value and serialized:

1.   Set serialized.[[Name]] to value's associated name value.

2.   Let serializedBestFriend be the [sub-serialization](https://html.spec.whatwg.org/multipage/structured-data.html#sub-serialization) of value's associated best friend value.

3.   Set serialized.[[BestFriend]] to serializedBestFriend.

Their [deserialization steps](https://html.spec.whatwg.org/multipage/structured-data.html#deserialization-steps), given serialized, value, and targetRealm:

1.   Set value's associated name value to serialized.[[Name]].

2.   Let deserializedBestFriend be the [sub-deserialization](https://html.spec.whatwg.org/multipage/structured-data.html#sub-deserialization) of serialized.[[BestFriend]].

3.   Set value's associated best friend value to deserializedBestFriend.

Objects defined in the JavaScript specification are handled by the [StructuredSerialize](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserialize) abstract operation directly.

[](https://html.spec.whatwg.org/multipage/structured-data.html#cloneable-objects)Originally, this specification defined the concept of "cloneable objects", which could be cloned from one [realm](https://tc39.es/ecma262/#sec-code-realms) to another. However, to better specify the behavior of certain more complex situations, the model was updated to make the serialization and deserialization explicit.

#### 2.7.2 Transferable objects[](https://html.spec.whatwg.org/multipage/structured-data.html#transferable-objects)

[Transferable objects](https://html.spec.whatwg.org/multipage/structured-data.html#transferable-objects) support being transferred across [agents](https://tc39.es/ecma262/#sec-agents). Transferring is effectively recreating the object while sharing a reference to the underlying data and then detaching the object being transferred. This is useful to transfer ownership of expensive resources. Not all objects are [transferable objects](https://html.spec.whatwg.org/multipage/structured-data.html#transferable-objects) and not all aspects of objects that are [transferable objects](https://html.spec.whatwg.org/multipage/structured-data.html#transferable-objects) are necessarily preserved when transferred.

Transferring is an irreversible and non-idempotent operation. Once an object has been transferred, it cannot be transferred, or indeed used, again.

[Platform objects](https://webidl.spec.whatwg.org/#dfn-platform-object) can be [transferable objects](https://html.spec.whatwg.org/multipage/structured-data.html#transferable-objects) if their [primary interface](https://webidl.spec.whatwg.org/#dfn-primary-interface) is decorated with the `[Transferable]` IDL [extended attribute](https://webidl.spec.whatwg.org/#dfn-extended-attribute). Such interfaces must also define the following algorithms:

transfer steps, taking a [platform object](https://webidl.spec.whatwg.org/#dfn-platform-object)value and a [Record](https://tc39.es/ecma262/#sec-list-and-record-specification-type)dataHolder
A set of steps that transfers the data in value into fields of dataHolder. The resulting data held in dataHolder must be independent of any [realm](https://tc39.es/ecma262/#sec-code-realms).

These steps may throw an exception if transferral is not possible.

transfer-receiving steps, taking a [Record](https://tc39.es/ecma262/#sec-list-and-record-specification-type)dataHolder and a [platform object](https://webidl.spec.whatwg.org/#dfn-platform-object)value
A set of steps that receives the data in dataHolder, using it to set up value as appropriate. value will be a newly-created instance of the [platform object](https://webidl.spec.whatwg.org/#dfn-platform-object) type in question, with none of its internal data set up; setting that up is the job of these steps.

These steps may throw an exception if it is not possible to receive the transfer.

It is up to the definition of individual platform objects to determine what data is transferred by these steps. Typically the steps are very symmetric.

The `[Transferable]` extended attribute must take no arguments, and must only appear on an interface. It must not appear more than once on an interface.

For a given [platform object](https://webidl.spec.whatwg.org/#dfn-platform-object), only the object's [primary interface](https://webidl.spec.whatwg.org/#dfn-primary-interface) is considered during the transferring process. Thus, if inheritance is involved in defining the interface, each `[Transferable]`-annotated interface in the inheritance chain needs to define standalone [transfer steps](https://html.spec.whatwg.org/multipage/structured-data.html#transfer-steps) and [transfer-receiving steps](https://html.spec.whatwg.org/multipage/structured-data.html#transfer-receiving-steps), including taking into account any important data that might come from inherited interfaces.

[Platform objects](https://webidl.spec.whatwg.org/#dfn-platform-object) that are [transferable objects](https://html.spec.whatwg.org/multipage/structured-data.html#transferable-objects) have a [[Detached]] internal slot. This is used to ensure that once a platform object has been transferred, it cannot be transferred again.

Objects defined in the JavaScript specification are handled by the [StructuredSerializeWithTransfer](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializewithtransfer) abstract operation directly.

#### 2.7.3 StructuredSerializeInternal ( value, forStorage [ , memory ] )[](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializeinternal)

The [StructuredSerializeInternal](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializeinternal) abstract operation takes as input a JavaScript value value and serializes it to a [realm](https://tc39.es/ecma262/#sec-code-realms)-independent form, represented here as a [Record](https://tc39.es/ecma262/#sec-list-and-record-specification-type). This serialized form has all the information necessary to later deserialize into a new JavaScript value in a different realm.

This process can throw an exception, for example when trying to serialize un-serializable objects.

1.   If memory was not supplied, let memory be an empty [map](https://infra.spec.whatwg.org/#ordered-map).

The purpose of the memory map is to avoid serializing objects twice. This ends up preserving cycles and the identity of duplicate objects in graphs.

2.   If memory[value] [exists](https://infra.spec.whatwg.org/#map-exists), then return memory[value].

3.   Let deep be false.

4.   If value is undefined, null, [a Boolean](https://tc39.es/ecma262/#sec-ecmascript-language-types-boolean-type), [a Number](https://tc39.es/ecma262/#sec-ecmascript-language-types-number-type), [a BigInt](https://tc39.es/ecma262/#sec-ecmascript-language-types-bigint-type), or [a String](https://tc39.es/ecma262/#sec-ecmascript-language-types-string-type), then return { [[Type]]: "primitive", [[Value]]: value }.

5.   If value[is a Symbol](https://tc39.es/ecma262/#sec-ecmascript-language-types-symbol-type), then throw a ["`DataCloneError`"](https://webidl.spec.whatwg.org/#datacloneerror)`DOMException`.

6.   Let serialized be an uninitialized value.

7.   If value has a [[BooleanData]] internal slot, then set serialized to { [[Type]]: "Boolean", [[BooleanData]]: value.[[BooleanData]] }.

8.   Otherwise, if value has a [[NumberData]] internal slot, then set serialized to { [[Type]]: "Number", [[NumberData]]: value.[[NumberData]] }.

9.   Otherwise, if value has a [[BigIntData]] internal slot, then set serialized to { [[Type]]: "BigInt", [[BigIntData]]: value.[[BigIntData]] }.

10.   Otherwise, if value has a [[StringData]] internal slot, then set serialized to { [[Type]]: "String", [[StringData]]: value.[[StringData]] }.

11.   Otherwise, if value has a [[DateValue]] internal slot, then set serialized to { [[Type]]: "Date", [[DateValue]]: value.[[DateValue]] }.

12.   Otherwise, if value has a [[RegExpMatcher]] internal slot, then set serialized to { [[Type]]: "RegExp", [[RegExpMatcher]]: value.[[RegExpMatcher]], [[OriginalSource]]: value.[[OriginalSource]], [[OriginalFlags]]: value.[[OriginalFlags]] }.

13.   Otherwise, if value has an [[ArrayBufferData]] internal slot, then:

    1.   If [IsSharedArrayBuffer](https://tc39.es/ecma262/#sec-issharedarraybuffer)(value) is true, then:

        1.   If the [current settings object](https://html.spec.whatwg.org/multipage/webappapis.html#current-settings-object)'s [cross-origin isolated capability](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-cross-origin-isolated-capability) is false, then throw a ["`DataCloneError`"](https://webidl.spec.whatwg.org/#datacloneerror)`DOMException`.

This check is only needed when serializing (and not when deserializing) as the [cross-origin isolated capability](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-cross-origin-isolated-capability) cannot change over time and a `SharedArrayBuffer` cannot leave an [agent cluster](https://tc39.es/ecma262/#sec-agent-clusters).

        2.   If forStorage is true, then throw a ["`DataCloneError`"](https://webidl.spec.whatwg.org/#datacloneerror)`DOMException`.

        3.   If value has an [[ArrayBufferMaxByteLength]] internal slot, then set serialized to { [[Type]]: "GrowableSharedArrayBuffer", [[ArrayBufferData]]: value.[[ArrayBufferData]], [[ArrayBufferByteLengthData]]: value.[[ArrayBufferByteLengthData]], [[ArrayBufferMaxByteLength]]: value.[[ArrayBufferMaxByteLength]], [[AgentCluster]]: the [surrounding agent](https://tc39.es/ecma262/#surrounding-agent)'s [agent cluster](https://tc39.es/ecma262/#sec-agent-clusters) }.

        4.   Otherwise, set serialized to { [[Type]]: "SharedArrayBuffer", [[ArrayBufferData]]: value.[[ArrayBufferData]], [[ArrayBufferByteLength]]: value.[[ArrayBufferByteLength]], [[AgentCluster]]: the [surrounding agent](https://tc39.es/ecma262/#surrounding-agent)'s [agent cluster](https://tc39.es/ecma262/#sec-agent-clusters) }.

    2.   Otherwise:

        1.   If [IsDetachedBuffer](https://tc39.es/ecma262/#sec-isdetachedbuffer)(value) is true, then throw a ["`DataCloneError`"](https://webidl.spec.whatwg.org/#datacloneerror)`DOMException`.

        2.   Let size be value.[[ArrayBufferByteLength]].

        3.   Let dataCopy be ? [CreateByteDataBlock](https://tc39.es/ecma262/#sec-createbytedatablock)(size).

This can throw a `RangeError` exception upon allocation failure.

        4.   Perform [CopyDataBlockBytes](https://tc39.es/ecma262/#sec-copydatablockbytes)(dataCopy, 0, value.[[ArrayBufferData]], 0, size).

        5.   If value has an [[ArrayBufferMaxByteLength]] internal slot, then set serialized to { [[Type]]: "ResizableArrayBuffer", [[ArrayBufferData]]: dataCopy, [[ArrayBufferByteLength]]: size, [[ArrayBufferMaxByteLength]]: value.[[ArrayBufferMaxByteLength]] }.

        6.   Otherwise, set serialized to { [[Type]]: "ArrayBuffer", [[ArrayBufferData]]: dataCopy, [[ArrayBufferByteLength]]: size }.

14.   Otherwise, if value has a [[ViewedArrayBuffer]] internal slot, then:

    1.   If [IsArrayBufferViewOutOfBounds](https://tc39.es/ecma262/#sec-isarraybufferviewoutofbounds)(value) is true, then throw a ["`DataCloneError`"](https://webidl.spec.whatwg.org/#datacloneerror)`DOMException`.

    2.   Let buffer be the value of value's [[ViewedArrayBuffer]] internal slot.

    3.   Let bufferSerialized be ? [StructuredSerializeInternal](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializeinternal)(buffer, forStorage, memory).

    4.   [Assert](https://infra.spec.whatwg.org/#assert): bufferSerialized.[[Type]] is "ArrayBuffer", "ResizableArrayBuffer", "SharedArrayBuffer", or "GrowableSharedArrayBuffer".

    5.   If value has a [[DataView]] internal slot, then set serialized to { [[Type]]: "ArrayBufferView", [[Constructor]]: "DataView", [[ArrayBufferSerialized]]: bufferSerialized, [[ByteLength]]: value.[[ByteLength]], [[ByteOffset]]: value.[[ByteOffset]] }.

    6.   Otherwise:

        1.   [Assert](https://infra.spec.whatwg.org/#assert): value has a [[TypedArrayName]] internal slot.

        2.   Set serialized to { [[Type]]: "ArrayBufferView", [[Constructor]]: value.[[TypedArrayName]], [[ArrayBufferSerialized]]: bufferSerialized, [[ByteLength]]: value.[[ByteLength]], [[ByteOffset]]: value.[[ByteOffset]], [[ArrayLength]]: value.[[ArrayLength]] }.

15.   Otherwise, if value has a [[MapData]] internal slot, then:

    1.   Set serialized to { [[Type]]: "Map", [[MapData]]: a new empty [List](https://tc39.es/ecma262/#sec-list-and-record-specification-type) }.

    2.   Set deep to true.

16.   Otherwise, if value has a [[SetData]] internal slot, then:

    1.   Set serialized to { [[Type]]: "Set", [[SetData]]: a new empty [List](https://tc39.es/ecma262/#sec-list-and-record-specification-type) }.

    2.   Set deep to true.

17.   Otherwise, if value has an [[ErrorData]] internal slot and value is not a [platform object](https://webidl.spec.whatwg.org/#dfn-platform-object), then:

    1.   Let name be ? [Get](https://tc39.es/ecma262/#sec-get-o-p)(value, "name").

    2.   If name is not one of "Error", "EvalError", "RangeError", "ReferenceError", "SyntaxError", "TypeError", or "URIError", then set name to "Error".

    3.   Let valueMessageDesc be ? value.[[GetOwnProperty]]("`message`").

    4.   Let message be undefined if [IsDataDescriptor](https://tc39.es/ecma262/#sec-isdatadescriptor)(valueMessageDesc) is false, and ? [ToString](https://tc39.es/ecma262/#sec-tostring)(valueMessageDesc.[[Value]]) otherwise.

    5.   Set serialized to { [[Type]]: "Error", [[Name]]: name, [[Message]]: message }.

    6.   User agents should attach a serialized representation of any interesting accompanying data which are not yet specified, notably the `stack` property, to serialized.

See the Error Stacks proposal for in-progress work on specifying this data. [[JSERRORSTACKS]](https://html.spec.whatwg.org/multipage/references.html#refsJSERRORSTACKS)

18.   Otherwise, if value is an Array exotic object, then:

    1.   Let valueLenDescriptor be ? [OrdinaryGetOwnProperty](https://tc39.es/ecma262/#sec-ordinarygetownproperty)(value, "`length`").

    2.   Let valueLen be valueLenDescriptor.[[Value]].

    3.   Set serialized to { [[Type]]: "Array", [[Length]]: valueLen, [[Properties]]: a new empty [List](https://tc39.es/ecma262/#sec-list-and-record-specification-type) }.

    4.   Set deep to true.

19.   Otherwise, if value is a [platform object](https://webidl.spec.whatwg.org/#dfn-platform-object) that is a [serializable object](https://html.spec.whatwg.org/multipage/structured-data.html#serializable-objects):

    1.   If value has a [[[Detached]]](https://html.spec.whatwg.org/multipage/structured-data.html#detached) internal slot whose value is true, then throw a ["`DataCloneError`"](https://webidl.spec.whatwg.org/#datacloneerror)`DOMException`.

    2.   Let typeString be the identifier of the [primary interface](https://webidl.spec.whatwg.org/#dfn-primary-interface) of value.

    3.   Set serialized to { [[Type]]: typeString }.

    4.   Set deep to true.

20.   Otherwise, if value is a [platform object](https://webidl.spec.whatwg.org/#dfn-platform-object), then throw a ["`DataCloneError`"](https://webidl.spec.whatwg.org/#datacloneerror)`DOMException`.

21.   Otherwise, if [IsCallable](https://tc39.es/ecma262/#sec-iscallable)(value) is true, then throw a ["`DataCloneError`"](https://webidl.spec.whatwg.org/#datacloneerror)`DOMException`.

22.   Otherwise, if value has any internal slot other than [[Prototype]], [[Extensible]], or [[PrivateElements]], then throw a ["`DataCloneError`"](https://webidl.spec.whatwg.org/#datacloneerror)`DOMException`.

For instance, a [[PromiseState]] or [[WeakMapData]] internal slot.

23.   Otherwise, if value is an exotic object and value is not the [%Object.prototype%](https://tc39.es/ecma262/#sec-properties-of-the-object-prototype-object) intrinsic object associated with any [realm](https://tc39.es/ecma262/#sec-code-realms), then throw a ["`DataCloneError`"](https://webidl.spec.whatwg.org/#datacloneerror)`DOMException`.

For instance, a proxy object.

24.   Otherwise:

    1.   Set serialized to { [[Type]]: "Object", [[Properties]]: a new empty [List](https://tc39.es/ecma262/#sec-list-and-record-specification-type) }.

    2.   Set deep to true.

[%Object.prototype%](https://tc39.es/ecma262/#sec-properties-of-the-object-prototype-object) will end up being handled via this step and subsequent steps. The end result is that its exoticness is ignored, and after deserialization the result will be an empty object (not an [immutable prototype exotic object](https://tc39.es/ecma262/#immutable-prototype-exotic-object)).

25.   [Set](https://infra.spec.whatwg.org/#map-set)memory[value] to serialized.

26.   If deep is true, then:

    1.   If value has a [[MapData]] internal slot, then:

        1.   Let copiedList be a new empty [List](https://tc39.es/ecma262/#sec-list-and-record-specification-type).

        2.   [For each](https://infra.spec.whatwg.org/#list-iterate)[Record](https://tc39.es/ecma262/#sec-list-and-record-specification-type) { [[Key]], [[Value]] } entry of value.[[MapData]]:

            1.   Let copiedEntry be a new [Record](https://tc39.es/ecma262/#sec-list-and-record-specification-type) { [[Key]]: entry.[[Key]], [[Value]]: entry.[[Value]] }.

            2.   If copiedEntry.[[Key]] is not the special value _empty_, [append](https://infra.spec.whatwg.org/#list-append)copiedEntry to copiedList.

        3.   [For each](https://infra.spec.whatwg.org/#list-iterate)[Record](https://tc39.es/ecma262/#sec-list-and-record-specification-type) { [[Key]], [[Value]] } entry of copiedList:

            1.   Let serializedKey be ? [StructuredSerializeInternal](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializeinternal)(entry.[[Key]], forStorage, memory).

            2.   Let serializedValue be ? [StructuredSerializeInternal](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializeinternal)(entry.[[Value]], forStorage, memory).

            3.   [Append](https://infra.spec.whatwg.org/#list-append) { [[Key]]: serializedKey, [[Value]]: serializedValue } to serialized.[[MapData]].

    2.   Otherwise, if value has a [[SetData]] internal slot, then:

        1.   Let copiedList be a new empty [List](https://tc39.es/ecma262/#sec-list-and-record-specification-type).

        2.   [For each](https://infra.spec.whatwg.org/#list-iterate)entry of value.[[SetData]]:

            1.   If entry is not the special value _empty_, [append](https://infra.spec.whatwg.org/#list-append)entry to copiedList.

        3.   [For each](https://infra.spec.whatwg.org/#list-iterate)entry of copiedList:

            1.   Let serializedEntry be ? [StructuredSerializeInternal](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializeinternal)(entry, forStorage, memory).

            2.   [Append](https://infra.spec.whatwg.org/#list-append)serializedEntry to serialized.[[SetData]].

    3.   Otherwise, if value is a [platform object](https://webidl.spec.whatwg.org/#dfn-platform-object) that is a [serializable object](https://html.spec.whatwg.org/multipage/structured-data.html#serializable-objects), then perform the [serialization steps](https://html.spec.whatwg.org/multipage/structured-data.html#serialization-steps) for value's [primary interface](https://webidl.spec.whatwg.org/#dfn-primary-interface), given value, serialized, and forStorage.

The [serialization steps](https://html.spec.whatwg.org/multipage/structured-data.html#serialization-steps) may need to perform a sub-serialization. This is an operation which takes as input a value subValue, and returns [StructuredSerializeInternal](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializeinternal)(subValue, forStorage, memory). (In other words, a [sub-serialization](https://html.spec.whatwg.org/multipage/structured-data.html#sub-serialization) is a specialization of [StructuredSerializeInternal](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializeinternal) to be consistent within this invocation.)

    4.   Otherwise, for each key in ! [EnumerableOwnProperties](https://tc39.es/ecma262/#sec-enumerableownproperties)(value, key):

        1.   If ! [HasOwnProperty](https://tc39.es/ecma262/#sec-hasownproperty)(value, key) is true, then:

            1.   Let inputValue be ? value.[[Get]](key, value).

            2.   Let outputValue be ? [StructuredSerializeInternal](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializeinternal)(inputValue, forStorage, memory).

            3.   [Append](https://infra.spec.whatwg.org/#list-append) { [[Key]]: key, [[Value]]: outputValue } to serialized.[[Properties]].

27.   Return serialized.

It's important to realize that the [Records](https://tc39.es/ecma262/#sec-list-and-record-specification-type) produced by [StructuredSerializeInternal](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializeinternal) might contain "pointers" to other records that create circular references. For example, when we pass the following JavaScript object into [StructuredSerializeInternal](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializeinternal):

```
const o = {};
o.myself = o;
```

it produces the following result:

{ [[Type]]: "Object", [[Properties]]: « { [[Key]]: "myself", [[Value]]: _<a pointer to this whole structure>_ } » }

#### 2.7.4 StructuredSerialize ( value )[](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserialize)

1.   Return ? [StructuredSerializeInternal](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializeinternal)(value, false).

#### 2.7.5 StructuredSerializeForStorage ( value )[](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializeforstorage)

1.   Return ? [StructuredSerializeInternal](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializeinternal)(value, true).

#### 2.7.6 StructuredDeserialize ( serialized, targetRealm [ , memory ] )[](https://html.spec.whatwg.org/multipage/structured-data.html#structureddeserialize)

The [StructuredDeserialize](https://html.spec.whatwg.org/multipage/structured-data.html#structureddeserialize) abstract operation takes as input a [Record](https://tc39.es/ecma262/#sec-list-and-record-specification-type)serialized, which was previously produced by [StructuredSerialize](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserialize) or [StructuredSerializeForStorage](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializeforstorage), and deserializes it into a new JavaScript value, created in targetRealm.

This process can throw an exception, for example when trying to allocate memory for the new objects (especially `ArrayBuffer` objects).

1.   If memory was not supplied, let memory be an empty [map](https://infra.spec.whatwg.org/#ordered-map).

The purpose of the memory map is to avoid deserializing objects twice. This ends up preserving cycles and the identity of duplicate objects in graphs.

2.   If memory[serialized] [exists](https://infra.spec.whatwg.org/#map-exists), then return memory[serialized].

3.   Let deep be false.

4.   Let value be an uninitialized value.

5.   If serialized.[[Type]] is "primitive", then set value to serialized.[[Value]].

6.   Otherwise, if serialized.[[Type]] is "Boolean", then set value to a new Boolean object in targetRealm whose [[BooleanData]] internal slot value is serialized.[[BooleanData]].

7.   Otherwise, if serialized.[[Type]] is "Number", then set value to a new Number object in targetRealm whose [[NumberData]] internal slot value is serialized.[[NumberData]].

8.   Otherwise, if serialized.[[Type]] is "BigInt", then set value to a new BigInt object in targetRealm whose [[BigIntData]] internal slot value is serialized.[[BigIntData]].

9.   Otherwise, if serialized.[[Type]] is "String", then set value to a new String object in targetRealm whose [[StringData]] internal slot value is serialized.[[StringData]].

10.   Otherwise, if serialized.[[Type]] is "Date", then set value to a new Date object in targetRealm whose [[DateValue]] internal slot value is serialized.[[DateValue]].

11.   Otherwise, if serialized.[[Type]] is "RegExp", then set value to a new RegExp object in targetRealm whose [[RegExpMatcher]] internal slot value is serialized.[[RegExpMatcher]], whose [[OriginalSource]] internal slot value is serialized.[[OriginalSource]], and whose [[OriginalFlags]] internal slot value is serialized.[[OriginalFlags]].

12.   Otherwise, if serialized.[[Type]] is "SharedArrayBuffer", then:

    1.   If targetRealm's corresponding [agent cluster](https://tc39.es/ecma262/#sec-agent-clusters) is not serialized.[[AgentCluster]], then throw a ["`DataCloneError`"](https://webidl.spec.whatwg.org/#datacloneerror)`DOMException`.

    2.   Otherwise, set value to a new SharedArrayBuffer object in targetRealm whose [[ArrayBufferData]] internal slot value is serialized.[[ArrayBufferData]] and whose [[ArrayBufferByteLength]] internal slot value is serialized.[[ArrayBufferByteLength]].

13.   Otherwise, if serialized.[[Type]] is "GrowableSharedArrayBuffer", then:

    1.   If targetRealm's corresponding [agent cluster](https://tc39.es/ecma262/#sec-agent-clusters) is not serialized.[[AgentCluster]], then throw a ["`DataCloneError`"](https://webidl.spec.whatwg.org/#datacloneerror)`DOMException`.

    2.   Otherwise, set value to a new SharedArrayBuffer object in targetRealm whose [[ArrayBufferData]] internal slot value is serialized.[[ArrayBufferData]], whose [[ArrayBufferByteLengthData]] internal slot value is serialized.[[ArrayBufferByteLengthData]], and whose [[ArrayBufferMaxByteLength]] internal slot value is serialized.[[ArrayBufferMaxByteLength]].

14.   Otherwise, if serialized.[[Type]] is "ArrayBuffer", then set value to a new ArrayBuffer object in targetRealm whose [[ArrayBufferData]] internal slot value is serialized.[[ArrayBufferData]], and whose [[ArrayBufferByteLength]] internal slot value is serialized.[[ArrayBufferByteLength]].

If this throws an exception, catch it, and then throw a ["`DataCloneError`"](https://webidl.spec.whatwg.org/#datacloneerror)`DOMException`.

This step might throw an exception if there is not enough memory available to create such an ArrayBuffer object.

15.   Otherwise, if serialized.[[Type]] is "ResizableArrayBuffer", then set value to a new ArrayBuffer object in targetRealm whose [[ArrayBufferData]] internal slot value is serialized.[[ArrayBufferData]], whose [[ArrayBufferByteLength]] internal slot value is serialized.[[ArrayBufferByteLength]], and whose [[ArrayBufferMaxByteLength]] internal slot value is serialized.[[ArrayBufferMaxByteLength]].

If this throws an exception, catch it, and then throw a ["`DataCloneError`"](https://webidl.spec.whatwg.org/#datacloneerror)`DOMException`.

This step might throw an exception if there is not enough memory available to create such an ArrayBuffer object.

16.   Otherwise, if serialized.[[Type]] is "ArrayBufferView", then:

    1.   Let deserializedArrayBuffer be ? [StructuredDeserialize](https://html.spec.whatwg.org/multipage/structured-data.html#structureddeserialize)(serialized.[[ArrayBufferSerialized]], targetRealm, memory).

    2.   If serialized.[[Constructor]] is "DataView", then set value to a new DataView object in targetRealm whose [[ViewedArrayBuffer]] internal slot value is deserializedArrayBuffer, whose [[ByteLength]] internal slot value is serialized.[[ByteLength]], and whose [[ByteOffset]] internal slot value is serialized.[[ByteOffset]].

    3.   Otherwise, set value to a new typed array object in targetRealm, using the constructor given by serialized.[[Constructor]], whose [[ViewedArrayBuffer]] internal slot value is deserializedArrayBuffer, whose [[TypedArrayName]] internal slot value is serialized.[[Constructor]], whose [[ByteLength]] internal slot value is serialized.[[ByteLength]], whose [[ByteOffset]] internal slot value is serialized.[[ByteOffset]], and whose [[ArrayLength]] internal slot value is serialized.[[ArrayLength]].

17.   Otherwise, if serialized.[[Type]] is "Map", then:

    1.   Set value to a new Map object in targetRealm whose [[MapData]] internal slot value is a new empty [List](https://tc39.es/ecma262/#sec-list-and-record-specification-type).

    2.   Set deep to true.

18.   Otherwise, if serialized.[[Type]] is "Set", then:

    1.   Set value to a new Set object in targetRealm whose [[SetData]] internal slot value is a new empty [List](https://tc39.es/ecma262/#sec-list-and-record-specification-type).

    2.   Set deep to true.

19.   Otherwise, if serialized.[[Type]] is "Array", then:

    1.   Let outputProto be targetRealm.[[Intrinsics]].[[[%Array.prototype%](https://tc39.es/ecma262/#sec-properties-of-the-array-prototype-object)]].

    2.   Set value to ! [ArrayCreate](https://tc39.es/ecma262/#sec-arraycreate)(serialized.[[Length]], outputProto).

    3.   Set deep to true.

20.   Otherwise, if serialized.[[Type]] is "Object", then:

    1.   Set value to a new Object in targetRealm.

    2.   Set deep to true.

21.   Otherwise, if serialized.[[Type]] is "Error", then:

    1.   Let prototype be [%Error.prototype%](https://tc39.es/ecma262/#sec-properties-of-the-error-prototype-object).

    2.   If serialized.[[Name]] is "EvalError", then set prototype to [%EvalError.prototype%](https://html.spec.whatwg.org/multipage/infrastructure.html#evalerror.prototype).

    3.   If serialized.[[Name]] is "RangeError", then set prototype to [%RangeError.prototype%](https://html.spec.whatwg.org/multipage/infrastructure.html#rangeerror.prototype).

    4.   If serialized.[[Name]] is "ReferenceError", then set prototype to [%ReferenceError.prototype%](https://html.spec.whatwg.org/multipage/infrastructure.html#referenceerror.prototype).

    5.   If serialized.[[Name]] is "SyntaxError", then set prototype to [%SyntaxError.prototype%](https://html.spec.whatwg.org/multipage/infrastructure.html#syntaxerror.prototype).

    6.   If serialized.[[Name]] is "TypeError", then set prototype to [%TypeError.prototype%](https://html.spec.whatwg.org/multipage/infrastructure.html#typeerror.prototype).

    7.   If serialized.[[Name]] is "URIError", then set prototype to [%URIError.prototype%](https://html.spec.whatwg.org/multipage/infrastructure.html#urierror.prototype).

    8.   Let message be serialized.[[Message]].

    9.   Set value to [OrdinaryObjectCreate](https://tc39.es/ecma262/#sec-objectcreate)(prototype, « [[ErrorData]] »).

    10.   Let messageDesc be [PropertyDescriptor](https://tc39.es/ecma262/#sec-property-descriptor-specification-type) { [[Value]]: message, [[Writable]]: true, [[Enumerable]]: false, [[Configurable]]: true }.

    11.   If message is not undefined, then perform ! [OrdinaryDefineOwnProperty](https://tc39.es/ecma262/#sec-ordinarydefineownproperty)(value, "`message`", messageDesc).

    12.   Any interesting accompanying data attached to serialized should be deserialized and attached to value.

22.   Otherwise:

    1.   Let interfaceName be serialized.[[Type]].

    2.   If the interface identified by interfaceName is not [exposed](https://webidl.spec.whatwg.org/#dfn-exposed) in targetRealm, then throw a ["`DataCloneError`"](https://webidl.spec.whatwg.org/#datacloneerror)`DOMException`.

    3.   Set value to a new instance of the interface identified by interfaceName, created in targetRealm.

    4.   Set deep to true.

23.   [Set](https://infra.spec.whatwg.org/#map-set)memory[serialized] to value.

24.   If deep is true, then:

    1.   If serialized.[[Type]] is "Map", then:

        1.   [For each](https://infra.spec.whatwg.org/#list-iterate)[Record](https://tc39.es/ecma262/#sec-list-and-record-specification-type) { [[Key]], [[Value]] } entry of serialized.[[MapData]]:

            1.   Let deserializedKey be ? [StructuredDeserialize](https://html.spec.whatwg.org/multipage/structured-data.html#structureddeserialize)(entry.[[Key]], targetRealm, memory).

            2.   Let deserializedValue be ? [StructuredDeserialize](https://html.spec.whatwg.org/multipage/structured-data.html#structureddeserialize)(entry.[[Value]], targetRealm, memory).

            3.   [Append](https://infra.spec.whatwg.org/#list-append) { [[Key]]: deserializedKey, [[Value]]: deserializedValue } to value.[[MapData]].

    2.   Otherwise, if serialized.[[Type]] is "Set", then:

        1.   [For each](https://infra.spec.whatwg.org/#list-iterate)entry of serialized.[[SetData]]:

            1.   Let deserializedEntry be ? [StructuredDeserialize](https://html.spec.whatwg.org/multipage/structured-data.html#structureddeserialize)(entry, targetRealm, memory).

            2.   [Append](https://infra.spec.whatwg.org/#list-append)deserializedEntry to value.[[SetData]].

    3.   Otherwise, if serialized.[[Type]] is "Array" or "Object", then:

        1.   [For each](https://infra.spec.whatwg.org/#list-iterate)[Record](https://tc39.es/ecma262/#sec-list-and-record-specification-type) { [[Key]], [[Value]] } entry of serialized.[[Properties]]:

            1.   Let deserializedValue be ? [StructuredDeserialize](https://html.spec.whatwg.org/multipage/structured-data.html#structureddeserialize)(entry.[[Value]], targetRealm, memory).

            2.   Let result be ! [CreateDataProperty](https://tc39.es/ecma262/#sec-createdataproperty)(value, entry.[[Key]], deserializedValue).

            3.   [Assert](https://infra.spec.whatwg.org/#assert): result is true.

    4.   Otherwise:

        1.   Perform the appropriate [deserialization steps](https://html.spec.whatwg.org/multipage/structured-data.html#deserialization-steps) for the interface identified by serialized.[[Type]], given serialized, value, and targetRealm.

The [deserialization steps](https://html.spec.whatwg.org/multipage/structured-data.html#deserialization-steps) may need to perform a sub-deserialization. This is an operation which takes as input a previously-serialized [Record](https://tc39.es/ecma262/#sec-list-and-record-specification-type)subSerialized, and returns [StructuredDeserialize](https://html.spec.whatwg.org/multipage/structured-data.html#structureddeserialize)(subSerialized, targetRealm, memory). (In other words, a [sub-deserialization](https://html.spec.whatwg.org/multipage/structured-data.html#sub-deserialization) is a specialization of [StructuredDeserialize](https://html.spec.whatwg.org/multipage/structured-data.html#structureddeserialize) to be consistent within this invocation.)

25.   Return value.

#### 2.7.7 StructuredSerializeWithTransfer ( value, transferList )[](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializewithtransfer)

1.   Let memory be an empty [map](https://infra.spec.whatwg.org/#ordered-map).

In addition to how it is used normally by [StructuredSerializeInternal](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializeinternal), in this algorithm memory is also used to ensure that [StructuredSerializeInternal](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializeinternal) ignores items in transferList, and let us do our own handling instead.

2.   [For each](https://infra.spec.whatwg.org/#list-iterate)transferable of transferList:

    1.   If transferable has neither an [[ArrayBufferData]] internal slot nor a [[[Detached]]](https://html.spec.whatwg.org/multipage/structured-data.html#detached) internal slot, then throw a ["`DataCloneError`"](https://webidl.spec.whatwg.org/#datacloneerror)`DOMException`.

    2.   If transferable has an [[ArrayBufferData]] internal slot and [IsSharedArrayBuffer](https://tc39.es/ecma262/#sec-issharedarraybuffer)(transferable) is true, then throw a ["`DataCloneError`"](https://webidl.spec.whatwg.org/#datacloneerror)`DOMException`.

    3.   If memory[transferable] [exists](https://infra.spec.whatwg.org/#map-exists), then throw a ["`DataCloneError`"](https://webidl.spec.whatwg.org/#datacloneerror)`DOMException`.

    4.   [Set](https://infra.spec.whatwg.org/#map-set)memory[transferable] to { [[Type]]: an uninitialized value }.

transferable is not transferred yet as transferring has side effects and [StructuredSerializeInternal](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializeinternal) needs to be able to throw first.

3.   Let serialized be ? [StructuredSerializeInternal](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializeinternal)(value, false, memory).

4.   Let transferDataHolders be a new empty [List](https://tc39.es/ecma262/#sec-list-and-record-specification-type).

5.   [For each](https://infra.spec.whatwg.org/#list-iterate)transferable of transferList:

    1.   If transferable has an [[ArrayBufferData]] internal slot and [IsDetachedBuffer](https://tc39.es/ecma262/#sec-isdetachedbuffer)(transferable) is true, then throw a ["`DataCloneError`"](https://webidl.spec.whatwg.org/#datacloneerror)`DOMException`.

    2.   If transferable has a [[[Detached]]](https://html.spec.whatwg.org/multipage/structured-data.html#detached) internal slot and transferable.[[[Detached]]](https://html.spec.whatwg.org/multipage/structured-data.html#detached) is true, then throw a ["`DataCloneError`"](https://webidl.spec.whatwg.org/#datacloneerror)`DOMException`.

    3.   Let dataHolder be memory[transferable].

    4.   If transferable has an [[ArrayBufferData]] internal slot, then:

        1.   If transferable has an [[ArrayBufferMaxByteLength]] internal slot, then:

            1.   Set dataHolder.[[Type]] to "ResizableArrayBuffer".

            2.   Set dataHolder.[[ArrayBufferData]] to transferable.[[ArrayBufferData]].

            3.   Set dataHolder.[[ArrayBufferByteLength]] to transferable.[[ArrayBufferByteLength]].

            4.   Set dataHolder.[[ArrayBufferMaxByteLength]] to transferable.[[ArrayBufferMaxByteLength]].

        2.   Otherwise:

            1.   Set dataHolder.[[Type]] to "ArrayBuffer".

            2.   Set dataHolder.[[ArrayBufferData]] to transferable.[[ArrayBufferData]].

            3.   Set dataHolder.[[ArrayBufferByteLength]] to transferable.[[ArrayBufferByteLength]].

        3.   Perform ? [DetachArrayBuffer](https://tc39.es/ecma262/#sec-detacharraybuffer)(transferable).

Specifications can use the [[ArrayBufferDetachKey]] internal slot to prevent `ArrayBuffer`s from being detached. This is used in WebAssembly JavaScript Interface, for example. [[WASMJS]](https://html.spec.whatwg.org/multipage/references.html#refsWASMJS)

    5.   Otherwise:

        1.   [Assert](https://infra.spec.whatwg.org/#assert): transferable is a [platform object](https://webidl.spec.whatwg.org/#dfn-platform-object) that is a [transferable object](https://html.spec.whatwg.org/multipage/structured-data.html#transferable-objects).

        2.   Let interfaceName be the identifier of the [primary interface](https://webidl.spec.whatwg.org/#dfn-primary-interface) of transferable.

        3.   Set dataHolder.[[Type]] to interfaceName.

        4.   Perform the appropriate [transfer steps](https://html.spec.whatwg.org/multipage/structured-data.html#transfer-steps) for the interface identified by interfaceName, given transferable and dataHolder.

        5.   Set transferable.[[[Detached]]](https://html.spec.whatwg.org/multipage/structured-data.html#detached) to true.

    6.   [Append](https://infra.spec.whatwg.org/#list-append)dataHolder to transferDataHolders.

6.   Return { [[Serialized]]: serialized, [[TransferDataHolders]]: transferDataHolders }.

#### 2.7.8 StructuredDeserializeWithTransfer ( serializeWithTransferResult, targetRealm )[](https://html.spec.whatwg.org/multipage/structured-data.html#structureddeserializewithtransfer)

1.   Let memory be an empty [map](https://infra.spec.whatwg.org/#ordered-map).

Analogous to [StructuredSerializeWithTransfer](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializewithtransfer), in addition to how it is used normally by [StructuredDeserialize](https://html.spec.whatwg.org/multipage/structured-data.html#structureddeserialize), in this algorithm memory is also used to ensure that [StructuredDeserialize](https://html.spec.whatwg.org/multipage/structured-data.html#structureddeserialize) ignores items in serializeWithTransferResult.[[TransferDataHolders]], and let us do our own handling instead.

2.   Let transferredValues be a new empty [List](https://tc39.es/ecma262/#sec-list-and-record-specification-type).

3.   [For each](https://infra.spec.whatwg.org/#list-iterate)transferDataHolder of serializeWithTransferResult.[[TransferDataHolders]]:

    1.   Let value be an uninitialized value.

    2.   If transferDataHolder.[[Type]] is "ArrayBuffer", then set value to a new ArrayBuffer object in targetRealm whose [[ArrayBufferData]] internal slot value is transferDataHolder.[[ArrayBufferData]], and whose [[ArrayBufferByteLength]] internal slot value is transferDataHolder.[[ArrayBufferByteLength]].

In cases where the original memory occupied by [[ArrayBufferData]] is accessible during the deserialization, this step is unlikely to throw an exception, as no new memory needs to be allocated: the memory occupied by [[ArrayBufferData]] is instead just getting transferred into the new ArrayBuffer. This could be true, for example, when both the source and target realms are in the same process.

    3.   Otherwise, if transferDataHolder.[[Type]] is "ResizableArrayBuffer", then set value to a new ArrayBuffer object in targetRealm whose [[ArrayBufferData]] internal slot value is transferDataHolder.[[ArrayBufferData]], whose [[ArrayBufferByteLength]] internal slot value is transferDataHolder.[[ArrayBufferByteLength]], and whose [[ArrayBufferMaxByteLength]] internal slot value is transferDataHolder.[[ArrayBufferMaxByteLength]].

For the same reason as the previous step, this step is also unlikely to throw an exception.

    4.   Otherwise:

        1.   Let interfaceName be transferDataHolder.[[Type]].

        2.   If the interface identified by interfaceName is not exposed in targetRealm, then throw a ["`DataCloneError`"](https://webidl.spec.whatwg.org/#datacloneerror)`DOMException`.

        3.   Set value to a new instance of the interface identified by interfaceName, created in targetRealm.

        4.   Perform the appropriate [transfer-receiving steps](https://html.spec.whatwg.org/multipage/structured-data.html#transfer-receiving-steps) for the interface identified by interfaceName given transferDataHolder and value.

    5.   [Set](https://infra.spec.whatwg.org/#map-set)memory[transferDataHolder] to value.

    6.   [Append](https://infra.spec.whatwg.org/#list-append)value to transferredValues.

4.   Let deserialized be ? [StructuredDeserialize](https://html.spec.whatwg.org/multipage/structured-data.html#structureddeserialize)(serializeWithTransferResult.[[Serialized]], targetRealm, memory).

5.   Return { [[Deserialized]]: deserialized, [[TransferredValues]]: transferredValues }.

#### 2.7.9 Performing serialization and transferring from other specifications[](https://html.spec.whatwg.org/multipage/structured-data.html#performing-structured-clones-from-other-specifications)

Other specifications may use the abstract operations defined here. The following provides some guidance on when each abstract operation is typically useful, with examples.

[StructuredSerializeWithTransfer](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializewithtransfer)[StructuredDeserializeWithTransfer](https://html.spec.whatwg.org/multipage/structured-data.html#structureddeserializewithtransfer)
Cloning a value to another [realm](https://tc39.es/ecma262/#sec-code-realms), with a transfer list, but where the target realm is not known ahead of time. In this case the serialization step can be performed immediately, with the deserialization step delayed until the target realm becomes known.

`messagePort.postMessage()` uses this pair of abstract operations, as the destination realm is not known until the `MessagePort`[has been shipped](https://html.spec.whatwg.org/multipage/web-messaging.html#has-been-shipped).

[StructuredSerialize](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserialize)[StructuredSerializeForStorage](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializeforstorage)[StructuredDeserialize](https://html.spec.whatwg.org/multipage/structured-data.html#structureddeserialize)
Creating a [realm](https://tc39.es/ecma262/#sec-code-realms)-independent snapshot of a given value which can be saved for an indefinite amount of time, and then reified back into a JavaScript value later, possibly multiple times.

[StructuredSerializeForStorage](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializeforstorage) can be used for situations where the serialization is anticipated to be stored in a persistent manner, instead of passed between realms. It throws when attempting to serialize `SharedArrayBuffer` objects, since storing shared memory does not make sense. Similarly, it can throw or possibly have different behavior when given a [platform object](https://webidl.spec.whatwg.org/#dfn-platform-object) with custom [serialization steps](https://html.spec.whatwg.org/multipage/structured-data.html#serialization-steps) when the forStorage argument is true.

`history.pushState()` and `history.replaceState()` use [StructuredSerializeForStorage](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializeforstorage) on author-supplied state objects, storing them as [serialized state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#serialized-state) in the appropriate [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry). Then, [StructuredDeserialize](https://html.spec.whatwg.org/multipage/structured-data.html#structureddeserialize) is used so that the `history.state` property can return a clone of the originally-supplied state object.

`broadcastChannel.postMessage()` uses [StructuredSerialize](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserialize) on its input, then uses [StructuredDeserialize](https://html.spec.whatwg.org/multipage/structured-data.html#structureddeserialize) multiple times on the result to produce a fresh clone for each destination being broadcast to. Note that transferring does not make sense in multi-destination situations.

Any API for persisting JavaScript values to the filesystem would also use [StructuredSerializeForStorage](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializeforstorage) on its input and [StructuredDeserialize](https://html.spec.whatwg.org/multipage/structured-data.html#structureddeserialize) on its output.

In general, call sites may pass in Web IDL values instead of JavaScript values; this is to be understood to perform an implicit [conversion](https://webidl.spec.whatwg.org/#es-type-mapping) to the JavaScript value before invoking these algorithms.

* * *

Call sites that are not invoked as a result of author code synchronously calling into a user agent method must take care to properly [prepare to run script](https://html.spec.whatwg.org/multipage/webappapis.html#prepare-to-run-script) and [prepare to run a callback](https://html.spec.whatwg.org/multipage/webappapis.html#prepare-to-run-a-callback) before invoking [StructuredSerialize](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserialize), [StructuredSerializeForStorage](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializeforstorage), or [StructuredSerializeWithTransfer](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializewithtransfer) abstract operations, if they are being performed on arbitrary objects. This is necessary because the serialization process can invoke author-defined accessors as part of its final deep-serialization steps, and these accessors could call into operations that rely on the [entry](https://html.spec.whatwg.org/multipage/webappapis.html#concept-entry-everything) and [incumbent](https://html.spec.whatwg.org/multipage/webappapis.html#concept-incumbent-everything) concepts being properly set up.

`window.postMessage()` performs [StructuredSerializeWithTransfer](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializewithtransfer) on its arguments, but is careful to do so immediately, inside the synchronous portion of its algorithm. Thus it is able to use the algorithms without needing to [prepare to run script](https://html.spec.whatwg.org/multipage/webappapis.html#prepare-to-run-script) and [prepare to run a callback](https://html.spec.whatwg.org/multipage/webappapis.html#prepare-to-run-a-callback).

In contrast, a hypothetical API that used [StructuredSerialize](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserialize) to serialize some author-supplied object periodically, directly from a [task](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task) on the [event loop](https://html.spec.whatwg.org/multipage/webappapis.html#event-loop), would need to ensure it performs the appropriate preparations beforehand. As of this time, we know of no such APIs on the platform; usually it is simpler to perform the serialization ahead of time, as a synchronous consequence of author code.

#### 2.7.10 Structured cloning API[](https://html.spec.whatwg.org/multipage/structured-data.html#structured-cloning)

`result = self.structuredClone(value[, { transfer }])`
Takes the input value and returns a deep copy by performing the structured clone algorithm. [Transferable objects](https://html.spec.whatwg.org/multipage/structured-data.html#transferable-objects) listed in the `transfer` array are transferred, not just cloned, meaning that they are no longer usable in the input value.

Throws a ["`DataCloneError`"](https://webidl.spec.whatwg.org/#datacloneerror)`DOMException` if any part of the input value is not [serializable](https://html.spec.whatwg.org/multipage/structured-data.html#serializable-objects).

[structuredClone](https://developer.mozilla.org/en-US/docs/Web/API/structuredClone "The global structuredClone() method creates a deep clone of a given value using the structured clone algorithm.")

Support in all current engines.

Firefox 94+Safari 15.4+Chrome 98+

* * *

Opera?Edge 98+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

The 
```
structuredClone(value,
  options)
```
 method steps are:

1.   Let serialized be ? [StructuredSerializeWithTransfer](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializewithtransfer)(value, options["`transfer`"]).

2.   Let deserializeRecord be ? [StructuredDeserializeWithTransfer](https://html.spec.whatwg.org/multipage/structured-data.html#structureddeserializewithtransfer)(serialized, [this](https://webidl.spec.whatwg.org/#this)'s [relevant realm](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-realm)).

3.   Return deserializeRecord.[[Deserialized]].

[← 2.6 Common DOM interfaces](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [3 Semantics, structure, and APIs of HTML documents →](https://html.spec.whatwg.org/multipage/dom.html)
