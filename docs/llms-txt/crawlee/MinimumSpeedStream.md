# Source: https://crawlee.dev/js/api/http-crawler/function/MinimumSpeedStream.md

# MinimumSpeedStream<!-- -->

### Callable

* ****MinimumSpeedStream**(\_\_namedParameters): Transform

***

* Creates a transform stream that throws an error if the source data speed is below the specified minimum speed. This `Transform` checks the amount of data every `checkProgressInterval` milliseconds. If the stream has received less than `minSpeedKbps * historyLengthMs / 1000` bytes in the last `historyLengthMs` milliseconds, it will throw an error.

  Can be used e.g. to abort a download if the network speed is too slow.

  ***

  #### Parameters

  * ##### \_\_namedParameters: { checkProgressInterval?<!-- -->: number; historyLengthMs?<!-- -->: number; minSpeedKbps: number }
    * ##### optionalcheckProgressInterval: number = <!-- -->5e3
    * ##### optionalhistoryLengthMs: number = <!-- -->10e3
    * ##### minSpeedKbps: number

  #### Returns Transform

  Transform stream that monitors the speed of the incoming data.
