# Source: https://crawlee.dev/js/api/core/function/useState.md

# useState<!-- -->

### Callable

* ****useState**\<State>(name, defaultValue, options): Promise\<State>

***

* Easily create and manage state values. All state values are automatically persisted.

  Values can be modified by simply using the assignment operator.

  ***

  #### Parameters

  * ##### optionalname: string

    The name of the store to use.

  * ##### defaultValue: State = <!-- -->...

    If the store does not yet have a value in it, the value will be initialized with the `defaultValue` you provide.

  * ##### optionaloptions: [UseStateOptions](https://crawlee.dev/js/api/core/interface/UseStateOptions.md)

    An optional object parameter where a custom `keyValueStoreName` and `config` can be passed in.

  #### Returns Promise\<State>
