# Source: https://crawlee.dev/js/api/playwright-crawler/class/RenderingTypePredictor.md

# RenderingTypePredictor<!-- -->

experimental

Stores rendering type information for previously crawled URLs and predicts the rendering type for URLs that have yet to be crawled and recommends when rendering type detection should be performed.

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**initialize](#initialize)
* [**predict](#predict)
* [**storeResult](#storeResult)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/rendering-type-prediction.ts#L52)constructor

* ****new RenderingTypePredictor**(\_\_namedParameters): [RenderingTypePredictor](https://crawlee.dev/js/api/playwright-crawler/class/RenderingTypePredictor.md)

- experimental

  #### Parameters

  * ##### \_\_namedParameters: RenderingTypePredictorOptions

  #### Returns [RenderingTypePredictor](https://crawlee.dev/js/api/playwright-crawler/class/RenderingTypePredictor.md)

## Methods<!-- -->[**](#Methods)

### [**](#initialize)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/rendering-type-prediction.ts#L94)initialize

* ****initialize**(): Promise\<void>

- experimental

  Initialize the predictor by restoring persisted state.

  ***

  #### Returns Promise\<void>

### [**](#predict)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/rendering-type-prediction.ts#L101)publicpredict

* ****predict**(\_\_namedParameters): { detectionProbabilityRecommendation: number; renderingType: [RenderingType](https://crawlee.dev/js/api/playwright-crawler.md#RenderingType) }

- experimental

  Predict the rendering type for a given URL and request label.

  ***

  #### Parameters

  * ##### \_\_namedParameters: [Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>

  #### Returns { detectionProbabilityRecommendation: number; renderingType: [RenderingType](https://crawlee.dev/js/api/playwright-crawler.md#RenderingType) }

  * ##### detectionProbabilityRecommendation: number
  * ##### renderingType: [RenderingType](https://crawlee.dev/js/api/playwright-crawler.md#RenderingType)

### [**](#storeResult)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/rendering-type-prediction.ts#L128)publicstoreResult

* ****storeResult**(requests, renderingType): void

- experimental

  Store the rendering type for a given URL and request label. This updates the underlying prediction model, which may be costly.

  ***

  #### Parameters

  * ##### requests: [Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary> | [Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>\[]
  * ##### renderingType: [RenderingType](https://crawlee.dev/js/api/playwright-crawler.md#RenderingType)

  #### Returns void
