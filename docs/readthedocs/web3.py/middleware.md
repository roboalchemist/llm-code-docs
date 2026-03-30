# Middleware

`Web3` is instantiated with layers of middleware by default. They sit between the public
`Web3` methods and the Providers, and are used to perform sanity checks, convert data
types, enable ENS support, and more. Each layer can modify the request and/or response.
While several middleware are enabled by default, others are available for optional use,
and you’re free to create your own!

Each middleware layer gets invoked before the request reaches the provider, and then
processes the result after the provider returns, in reverse order. However, it is
possible for a middleware to return early from a call without the request ever getting
to the provider (or even reaching the middleware that are in deeper layers).

## Configuring Middleware

Middleware can be added, removed, replaced, and cleared at runtime. To make that easier, you
can name the middleware for later reference.

### Middleware Order

Think of the middleware as being layered in an onion, where you initiate a web3.py request at
the outermost layer of the onion, and the Ethereum node (like geth) receives and responds
to the request inside the innermost layer of the onion. Here is a (simplified) diagram:

```
                            New request from web3.py

                                        |
                                        |
                                        v

                                `````Layer 2``````
                         ```````                  ```````
                    `````               |                ````
                 ````                   v                    ````
              ```                                                ```
            `.               ````````Layer 1```````                `.`
          ``             ````                      `````              .`
        `.            ```               |               ```            `.`
       .`          ```                  v                  ```           `.
     `.          `.`                                         ```           .`
    ``          .`                  `Layer 0`                  ``           .`
   ``         `.               `````        ``````               .           .`
  `.         ``             ```         |        ```              .`          .
  .         ``            `.`           |           ``             .           .
 .         `.            ``       JSON-RPC call       .`            .          .`
 .         .            ``              |              .            ``          .
``         .            .               v               .            .          .
.         .`           .                                .            .          ``
.         .            .          Ethereum node         .`           .           .
.         .            .                                .            .           .
.         ``           `.               |               .            .           .
.          .            .`              |              .`            .          .
`.         .`            .`          Response         .`            .`          .
 .          .             `.`           |           `.`            `.           .
 `.          .              ```         |        ````             `.           .
  .          `.               `````     v     ````               `.           ``
   .           .`                 ```Layer 0``                  ``           `.
    .           `.                                            `.`           `.
     .            `.                    |                   `.`            `.
      .`            ```                 |                 ```             .`
       `.              ```              v             ````              `.`
         ``               ``````                 `````                 .`
           ``                   `````Layer 1`````                   `.`
             ```                                                  ```
               ````                     |                      ```
                  `````                 v                  ````
                      ``````                          `````
                            `````````Layer 2``````````

                                        |
                                        v

                             Returned value in web3.py

```
