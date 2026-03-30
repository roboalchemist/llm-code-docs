# Source: https://crawlee.dev/js/api/utils/function/createRequestDebugInfo.md

# createRequestDebugInfo<!-- -->

### Callable

* ****createRequestDebugInfo**(request, response, additionalFields): Dictionary

***

* Creates a standardized debug info from request and response. This info is usually added to dataset under the hidden `#debug` field.

  ***

  #### Parameters

  * ##### request: Request\<Dictionary>

    [Request](https://sdk.apify.com/docs/api/request) object.

  * ##### optionalresponse: IncomingMessage | Partial\<BrowserResponseLike> = <!-- -->{}

    Puppeteer [`Response`](https://pptr.dev/#?product=Puppeteer\&version=v1.11.0\&show=api-class-response) or NodeJS [`http.IncomingMessage`](https://nodejs.org/api/http.html#http_class_http_serverresponse).

  * ##### optionaladditionalFields: Dictionary = <!-- -->{}

    Object containing additional fields to be added.

  #### Returns Dictionary
