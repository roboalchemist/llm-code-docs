# Source: https://crawlee.dev/js/api/core/interface/CreateSession.md

# CreateSession<!-- -->

Factory user-function which creates customized [Session](https://crawlee.dev/js/api/core/class/Session.md) instances.

### Callable

* ****CreateSession**(sessionPool, options): [Session](https://crawlee.dev/js/api/core/class/Session.md) | Promise<[Session](https://crawlee.dev/js/api/core/class/Session.md)>

***

* #### Parameters

  * ##### sessionPool: [SessionPool](https://crawlee.dev/js/api/core/class/SessionPool.md)

    Pool requesting the new session.

  * ##### optionaloptions: { sessionOptions?<!-- -->: [SessionOptions](https://crawlee.dev/js/api/core/interface/SessionOptions.md) }
    * ##### optionalsessionOptions: [SessionOptions](https://crawlee.dev/js/api/core/interface/SessionOptions.md)

  #### Returns [Session](https://crawlee.dev/js/api/core/class/Session.md) | Promise<[Session](https://crawlee.dev/js/api/core/class/Session.md)>
