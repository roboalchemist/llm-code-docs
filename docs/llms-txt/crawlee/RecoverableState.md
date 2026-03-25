# Source: https://crawlee.dev/js/api/core/class/RecoverableState.md

# RecoverableState<!-- --> \<TStateModel>

A class for managing persistent recoverable state using a plain JavaScript object.

This class facilitates state persistence to a `KeyValueStore`, allowing data to be saved and retrieved across migrations or restarts. It manages the loading, saving, and resetting of state data, with optional persistence capabilities.

The state is represented by a plain JavaScript object that can be serialized to and deserialized from JSON. The class automatically hooks into the event system to persist state when needed.

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Accessors

* [**currentValue](#currentValue)

### Methods

* [**initialize](#initialize)
* [**persistState](#persistState)
* [**reset](#reset)
* [**teardown](#teardown)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/recoverable_state.ts#L93)constructor

* ****new RecoverableState**\<TStateModel>(options): [RecoverableState](https://crawlee.dev/js/api/core/class/RecoverableState.md)\<TStateModel>

- Initialize a new recoverable state object.

  ***

  #### Parameters

  * ##### options: [RecoverableStateOptions](https://crawlee.dev/js/api/core/interface/RecoverableStateOptions.md)\<TStateModel>

    Configuration options for the recoverable state

  #### Returns [RecoverableState](https://crawlee.dev/js/api/core/class/RecoverableState.md)\<TStateModel>

## Accessors<!-- -->[**](#Accessors)

### [**](#currentValue)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/recoverable_state.ts#L157)currentValue

* **get currentValue(): TStateModel

- Get the current state.

  ***

  #### Returns TStateModel

## Methods<!-- -->[**](#Methods)

### [**](#initialize)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/recoverable_state.ts#L115)initialize

* ****initialize**(): Promise\<TStateModel>

- Initialize the recoverable state.

  This method must be called before using the recoverable state. It loads the saved state if persistence is enabled and registers the object to listen for PERSIST\_STATE events.

  ***

  #### Returns Promise\<TStateModel>

  The loaded state object

### [**](#persistState)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/recoverable_state.ts#L191)persistState

* ****persistState**(eventData): Promise\<void>

- Persist the current state to the KeyValueStore.

  This method is typically called in response to a PERSIST\_STATE event, but can also be called directly when needed.

  ***

  #### Parameters

  * ##### optionaleventData: { isMigrating: boolean }

    Optional data associated with a PERSIST\_STATE event

    * ##### isMigrating: boolean

  #### Returns Promise\<void>

### [**](#reset)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/recoverable_state.ts#L171)reset

* ****reset**(): Promise\<void>

- Reset the state to the default values and clear any persisted state.

  Resets the current state to the default state and, if persistence is enabled, clears the persisted state from the KeyValueStore.

  ***

  #### Returns Promise\<void>

### [**](#teardown)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/recoverable_state.ts#L144)teardown

* ****teardown**(): Promise\<void>

- Clean up resources used by the recoverable state.

  If persistence is enabled, this method deregisters the object from PERSIST\_STATE events and persists the current state one last time.

  ***

  #### Returns Promise\<void>
