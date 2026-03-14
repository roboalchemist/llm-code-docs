# Source: https://rolldown.rs/reference/Interface.RolldownMagicString.md

---
url: /reference/Interface.RolldownMagicString.md
---
# Interface: RolldownMagicString

## Extends

* `BindingMagicString`

## Properties

### isRolldownMagicString

* **Type**: `true`

## Accessors

### filename

#### Get Signature

* **Type**: () => `string` | `null`

##### Returns

`string` | `null`

#### Inherited from

`NativeBindingMagicString.filename`

***

### offset

#### Get Signature

* **Type**: () => `number`

##### Returns

`number`

#### Set Signature

* **Type**: (`offset`: `number`) => `void`

##### Parameters

###### offset

`number`

##### Returns

`void`

#### Inherited from

`NativeBindingMagicString.offset`

***

### original

#### Get Signature

* **Type**: () => `string`

##### Returns

`string`

#### Inherited from

`NativeBindingMagicString.original`

## Methods

### append()

* **Type**: (`content`: `string`) => `this`

#### Parameters

##### content

`string`

#### Returns

`this`

#### Inherited from

`NativeBindingMagicString.append`

***

### appendLeft()

* **Type**: (`index`: `number`, `content`: `string`) => `this`

#### Parameters

##### index

`number`

##### content

`string`

#### Returns

`this`

#### Inherited from

`NativeBindingMagicString.appendLeft`

***

### appendRight()

* **Type**: (`index`: `number`, `content`: `string`) => `this`

#### Parameters

##### index

`number`

##### content

`string`

#### Returns

`this`

#### Inherited from

`NativeBindingMagicString.appendRight`

***

### clone()

* **Type**: () => `BindingMagicString`

Returns a clone of the MagicString instance.

#### Returns

`BindingMagicString`

#### Inherited from

`NativeBindingMagicString.clone`

***

### generateDecodedMap()

* **Type**: (`options?`: `BindingSourceMapOptions` | `null`) => `BindingDecodedMap`

Generates a decoded source map for the transformations applied to this MagicString.
Returns a BindingDecodedMap object with mappings as an array of arrays.

#### Parameters

##### options?

`BindingSourceMapOptions` | `null`

#### Returns

`BindingDecodedMap`

#### Inherited from

`NativeBindingMagicString.generateDecodedMap`

***

### generateMap()

* **Type**: (`options?`: `BindingSourceMapOptions` | `null`) => `BindingSourceMap`

Generates a source map for the transformations applied to this MagicString.
Returns a BindingSourceMap object with version, file, sources, sourcesContent, names, mappings.

#### Parameters

##### options?

`BindingSourceMapOptions` | `null`

#### Returns

`BindingSourceMap`

#### Inherited from

`NativeBindingMagicString.generateMap`

***

### hasChanged()

* **Type**: () => `boolean`

#### Returns

`boolean`

#### Inherited from

`NativeBindingMagicString.hasChanged`

***

### indent()

* **Type**: (`indentor?`: `string` | `null`) => `this`

#### Parameters

##### indentor?

`string` | `null`

#### Returns

`this`

#### Inherited from

`NativeBindingMagicString.indent`

***

### insert()

* **Type**: (`index`: `number`, `content`: `string`) => `void`

Deprecated method that throws an error directing users to use prependRight or appendLeft.
This matches the original magic-string API which deprecated this method.

#### Parameters

##### index

`number`

##### content

`string`

#### Returns

`void`

#### Inherited from

`NativeBindingMagicString.insert`

***

### isEmpty()

* **Type**: () => `boolean`

#### Returns

`boolean`

#### Inherited from

`NativeBindingMagicString.isEmpty`

***

### lastChar()

* **Type**: () => `string`

Returns the last character of the generated string, or an empty string if empty.

#### Returns

`string`

#### Inherited from

`NativeBindingMagicString.lastChar`

***

### lastLine()

* **Type**: () => `string`

Returns the content after the last newline in the generated string.

#### Returns

`string`

#### Inherited from

`NativeBindingMagicString.lastLine`

***

### length()

* **Type**: () => `number`

#### Returns

`number`

#### Inherited from

`NativeBindingMagicString.length`

***

### move()

* **Type**: (`start`: `number`, `end`: `number`, `index`: `number`) => `this`

Alias for `relocate` to match the original magic-string API.
Moves the characters from `start` to `end` to `index`.
Returns `this` for method chaining.

#### Parameters

##### start

`number`

##### end

`number`

##### index

`number`

#### Returns

`this`

#### Inherited from

`NativeBindingMagicString.move`

***

### overwrite()

* **Type**: (`start`: `number`, `end`: `number`, `content`: `string`) => `this`

#### Parameters

##### start

`number`

##### end

`number`

##### content

`string`

#### Returns

`this`

#### Inherited from

`NativeBindingMagicString.overwrite`

***

### prepend()

* **Type**: (`content`: `string`) => `this`

#### Parameters

##### content

`string`

#### Returns

`this`

#### Inherited from

`NativeBindingMagicString.prepend`

***

### prependLeft()

* **Type**: (`index`: `number`, `content`: `string`) => `this`

#### Parameters

##### index

`number`

##### content

`string`

#### Returns

`this`

#### Inherited from

`NativeBindingMagicString.prependLeft`

***

### prependRight()

* **Type**: (`index`: `number`, `content`: `string`) => `this`

#### Parameters

##### index

`number`

##### content

`string`

#### Returns

`this`

#### Inherited from

`NativeBindingMagicString.prependRight`

***

### relocate()

* **Type**: (`start`: `number`, `end`: `number`, `to`: `number`) => `this`

#### Parameters

##### start

`number`

##### end

`number`

##### to

`number`

#### Returns

`this`

#### Inherited from

`NativeBindingMagicString.relocate`

***

### remove()

* **Type**: (`start`: `number`, `end`: `number`) => `this`

#### Parameters

##### start

`number`

##### end

`number`

#### Returns

`this`

#### Inherited from

`NativeBindingMagicString.remove`

***

### replace()

* **Type**: (`from`: `string`, `to`: `string`) => `this`

#### Parameters

##### from

`string`

##### to

`string`

#### Returns

`this`

#### Inherited from

`NativeBindingMagicString.replace`

***

### replaceAll()

* **Type**: (`from`: `string`, `to`: `string`) => `this`

#### Parameters

##### from

`string`

##### to

`string`

#### Returns

`this`

#### Inherited from

`NativeBindingMagicString.replaceAll`

***

### reset()

* **Type**: (`start`: `number`, `end`: `number`) => `this`

Resets the portion of the string from `start` to `end` to its original content.
This undoes any modifications made to that range.
Supports negative indices (counting from the end).

#### Parameters

##### start

`number`

##### end

`number`

#### Returns

`this`

#### Inherited from

`NativeBindingMagicString.reset`

***

### slice()

* **Type**: (`start?`: `number` | `null`, `end?`: `number` | `null`) => `string`

Returns the content between the specified original character positions.
Supports negative indices (counting from the end).

#### Parameters

##### start?

`number` | `null`

##### end?

`number` | `null`

#### Returns

`string`

#### Inherited from

`NativeBindingMagicString.slice`

***

### snip()

* **Type**: (`start`: `number`, `end`: `number`) => `BindingMagicString`

Returns a clone with content outside the specified range removed.

#### Parameters

##### start

`number`

##### end

`number`

#### Returns

`BindingMagicString`

#### Inherited from

`NativeBindingMagicString.snip`

***

### toString()

* **Type**: () => `string`

#### Returns

`string`

#### Inherited from

`NativeBindingMagicString.toString`

***

### trim()

* **Type**: (`charType?`: `string` | `null`) => `this`

Trims whitespace or specified characters from the start and end.

#### Parameters

##### charType?

`string` | `null`

#### Returns

`this`

#### Inherited from

`NativeBindingMagicString.trim`

***

### trimEnd()

* **Type**: (`charType?`: `string` | `null`) => `this`

Trims whitespace or specified characters from the end.

#### Parameters

##### charType?

`string` | `null`

#### Returns

`this`

#### Inherited from

`NativeBindingMagicString.trimEnd`

***

### trimLines()

* **Type**: () => `this`

Trims newlines from the start and end.

#### Returns

`this`

#### Inherited from

`NativeBindingMagicString.trimLines`

***

### trimStart()

* **Type**: (`charType?`: `string` | `null`) => `this`

Trims whitespace or specified characters from the start.

#### Parameters

##### charType?

`string` | `null`

#### Returns

`this`

#### Inherited from

`NativeBindingMagicString.trimStart`

***

### update()

* **Type**: (`start`: `number`, `end`: `number`, `content`: `string`) => `this`

#### Parameters

##### start

`number`

##### end

`number`

##### content

`string`

#### Returns

`this`

#### Inherited from

`NativeBindingMagicString.update`
