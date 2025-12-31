# Source: https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.Value.md.txt

# Value | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [remoteConfig](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig).
- Value

Wraps a value with metadata and type-safe getters.

## Index

### Methods

- [asBoolean](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.Value#asboolean)
- [asNumber](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.Value#asnumber)
- [asString](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.Value#asstring)
- [getSource](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.Value#getsource)

## Methods

### asBoolean

- asBoolean ( ) : boolean
- Gets the value as a boolean.

  The following values (case insensitive) are interpreted as true:
  "1", "true", "t", "yes", "y", "on". Other values are interpreted as false.

  #### Returns boolean

### asNumber

- asNumber ( ) : number
- Gets the value as a number. Comparable to calling `Number(value) || 0`.

  #### Returns number

### asString

- asString ( ) : string
- Gets the value as a string.

  #### Returns string

### getSource

- getSource ( ) : [ValueSource](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig#valuesource)
- Gets the [ValueSource](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig#valuesource) for the given key.

  #### Returns [ValueSource](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig#valuesource)