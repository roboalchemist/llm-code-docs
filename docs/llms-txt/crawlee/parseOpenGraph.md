# Source: https://crawlee.dev/js/api/utils/function/parseOpenGraph.md

# parseOpenGraph<!-- -->

### Callable

* ****parseOpenGraph**(raw, additionalProperties): Dictionary\<OpenGraphResult>
* ****parseOpenGraph**($, additionalProperties): Dictionary\<OpenGraphResult>

***

* Easily parse all OpenGraph properties from a page with just a `CheerioAPI` object.

  ***

  #### Parameters

  * ##### raw: string

  * ##### optionaladditionalProperties: [OpenGraphProperty](https://crawlee.dev/js/api/utils/interface/OpenGraphProperty.md)\[]

    Any potential additional `OpenGraphProperty` items you'd like to be scraped. Currently existing properties are kept up to date.

  #### Returns Dictionary\<OpenGraphResult>

  Scraped OpenGraph properties as an object.
