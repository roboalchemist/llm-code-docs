# Source: https://crawlee.dev/js/api/core/interface/RecoverableStatePersistenceOptions.md

# RecoverableStatePersistenceOptions<!-- -->

### Hierarchy

* *RecoverableStatePersistenceOptions*
  * [RecoverableStateOptions](https://crawlee.dev/js/api/core/interface/RecoverableStateOptions.md)

## Index[**](#Index)

### Properties

* [**persistenceEnabled](#persistenceEnabled)
* [**persistStateKey](#persistStateKey)
* [**persistStateKvsId](#persistStateKvsId)
* [**persistStateKvsName](#persistStateKvsName)

## Properties<!-- -->[**](#Properties)

### [**](#persistenceEnabled)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/recoverable_state.ts#L15)optionalpersistenceEnabled

**persistenceEnabled?

<!-- -->

: boolean

Flag to enable or disable state persistence

### [**](#persistStateKey)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/recoverable_state.ts#L10)persistStateKey

**persistStateKey: string

The key under which the state is stored in the KeyValueStore

### [**](#persistStateKvsId)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/recoverable_state.ts#L27)optionalpersistStateKvsId

**persistStateKvsId?

<!-- -->

: string

The identifier of the KeyValueStore to use for persistence. If neither a name nor an id are supplied, the default store will be used.

### [**](#persistStateKvsName)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/recoverable_state.ts#L21)optionalpersistStateKvsName

**persistStateKvsName?

<!-- -->

: string

The name of the KeyValueStore to use for persistence. If neither a name nor an id are supplied, the default store will be used.
