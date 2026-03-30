# Source: https://crawlee.dev/js/api/core/interface/RecoverableStateOptions.md

# RecoverableStateOptions<!-- --> \<TStateModel>

Options for configuring the RecoverableState

### Hierarchy

* [RecoverableStatePersistenceOptions](https://crawlee.dev/js/api/core/interface/RecoverableStatePersistenceOptions.md)
  * *RecoverableStateOptions*

## Index[**](#Index)

### Properties

* [**config](#config)
* [**defaultState](#defaultState)
* [**deserialize](#deserialize)
* [**logger](#logger)
* [**persistenceEnabled](#persistenceEnabled)
* [**persistStateKey](#persistStateKey)
* [**persistStateKvsId](#persistStateKvsId)
* [**persistStateKvsName](#persistStateKvsName)
* [**serialize](#serialize)

## Properties<!-- -->[**](#Properties)

### [**](#config)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/recoverable_state.ts#L49)optionalconfig

**config?

<!-- -->

: [Configuration](https://crawlee.dev/js/api/core/class/Configuration.md)

Configuration instance to use

### [**](#defaultState)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/recoverable_state.ts#L39)defaultState

**defaultState: TStateModel

The default state used if no persisted state is found. A deep copy is made each time the state is used.

### [**](#deserialize)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/recoverable_state.ts#L62)optionaldeserialize

**deserialize?

<!-- -->

: (serializedState) => TStateModel

Optional function to transform a JSON-serialized object back to the state model. If not provided, JSON.parse is used. It is advisable to perform validation in this function and to throw an exception if it fails.

***

#### Type declaration

* * **(serializedState): TStateModel

  - #### Parameters

    * ##### serializedState: string

    #### Returns TStateModel

### [**](#logger)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/recoverable_state.ts#L44)optionallogger

**logger?

<!-- -->

: [Log](https://crawlee.dev/js/api/core/class/Log.md)

A logger instance for logging operations related to state persistence

### [**](#persistenceEnabled)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/recoverable_state.ts#L15)optionalinheritedpersistenceEnabled

**persistenceEnabled?

<!-- -->

: boolean

Inherited from RecoverableStatePersistenceOptions.persistenceEnabled

Flag to enable or disable state persistence

### [**](#persistStateKey)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/recoverable_state.ts#L10)inheritedpersistStateKey

**persistStateKey: string

Inherited from RecoverableStatePersistenceOptions.persistStateKey

The key under which the state is stored in the KeyValueStore

### [**](#persistStateKvsId)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/recoverable_state.ts#L27)optionalinheritedpersistStateKvsId

**persistStateKvsId?

<!-- -->

: string

Inherited from RecoverableStatePersistenceOptions.persistStateKvsId

The identifier of the KeyValueStore to use for persistence. If neither a name nor an id are supplied, the default store will be used.

### [**](#persistStateKvsName)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/recoverable_state.ts#L21)optionalinheritedpersistStateKvsName

**persistStateKvsName?

<!-- -->

: string

Inherited from RecoverableStatePersistenceOptions.persistStateKvsName

The name of the KeyValueStore to use for persistence. If neither a name nor an id are supplied, the default store will be used.

### [**](#serialize)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/recoverable_state.ts#L55)optionalserialize

**serialize?

<!-- -->

: (state) => string

Optional function to transform the state to a JSON string before persistence. If not provided, JSON.stringify will be used.

***

#### Type declaration

* * **(state): string

  - #### Parameters

    * ##### state: TStateModel

    #### Returns string
