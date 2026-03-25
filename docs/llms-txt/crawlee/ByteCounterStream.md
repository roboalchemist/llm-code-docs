# Source: https://crawlee.dev/js/api/http-crawler/function/ByteCounterStream.md

# ByteCounterStream<!-- -->

### Callable

* ****ByteCounterStream**(\_\_namedParameters): Transform

***

* Creates a transform stream that logs the progress of the incoming data. This `Transform` calls the `logProgress` function every `loggingInterval` milliseconds with the number of bytes received so far.

  Can be used e.g. to log the progress of a download.

  ***

  #### Parameters

  * ##### \_\_namedParameters: { loggingInterval?<!-- -->: number; logTransferredBytes: (transferredBytes) => void }
    * ##### optionalloggingInterval: number = <!-- -->5000
    * ##### logTransferredBytes: (transferredBytes) => void

  #### Returns Transform

  Transform stream logging the progress of the incoming data.
