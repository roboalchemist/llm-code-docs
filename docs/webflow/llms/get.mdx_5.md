# Source: https://developers.webflow.com/data/reference/ecommerce/products/get.mdx

# Get Product and SKUs

GET https://api.webflow.com/v2/sites/{site_id}/products/{product_id}

Retrieve a single product by its ID. All of its SKUs will also be
retrieved.

Required scope | `ecommerce:read`


Reference: https://developers.webflow.com/data/reference/ecommerce/products/get

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /sites/{site_id}/products/{product_id}:
    get:
      operationId: get
      summary: Get Product and SKUs
      description: |
        Retrieve a single product by its ID. All of its SKUs will also be
        retrieved.

        Required scope | `ecommerce:read`
      tags:
        - subpackage_products
      parameters:
        - name: site_id
          in: path
          description: Unique identifier for a Site
          required: true
          schema:
            type: string
            format: objectid
        - name: product_id
          in: path
          description: Unique identifier for a Product
          required: true
          schema:
            type: string
            format: objectid
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Request was successful
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/products_get_Response_200'
        '400':
          description: Request body was incorrectly formatted.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-productRequestBadRequestError'
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-productRequestUnauthorizedError'
        '403':
          description: Provided access token is valid, but is missing the required scopes.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-productRequestForbiddenError'
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-productRequestNotFoundError'
        '409':
          description: The site does not have ecommerce enabled.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-productRequestConflictError'
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-productRequestTooManyRequestsError'
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-productRequestInternalServerError'
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaProductFieldDataSkuPropertiesItemsEnumItems:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier for a Product variant/Option
        name:
          type: string
          description: Name of the Product variant/Option
        slug:
          type: string
          description: Slug for the Product variant/Option in the Site URL structure
      required:
        - id
        - name
        - slug
      description: Enumerated Product variants/Options for the SKU
      title: >-
        SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaProductFieldDataSkuPropertiesItemsEnumItems
    SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaProductFieldDataSkuPropertiesItems:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier for a collection of Product Variants
        name:
          type: string
          description: Name of the collection of Product Variants
        enum:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaProductFieldDataSkuPropertiesItemsEnumItems
          description: >-
            The individual Product variants that are contained within the
            collection
      required:
        - id
        - name
        - enum
      description: A variant/option type for a SKU
      title: >-
        SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaProductFieldDataSkuPropertiesItems
    SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaProductFieldDataTaxCategory:
      type: string
      enum:
        - standard-taxable
        - standard-exempt
        - books-religious
        - books-textbook
        - clothing
        - clothing-swimwear
        - digital-goods
        - digital-service
        - drugs-non-prescription
        - drugs-prescription
        - food-bottled-water
        - food-candy
        - food-groceries
        - food-prepared
        - food-soda
        - food-supplements
        - magazine-individual
        - magazine-subscription
        - service-admission
        - service-advertising
        - service-dry-cleaning
        - service-hairdressing
        - service-installation
        - service-miscellaneous
        - service-parking
        - service-printing
        - service-professional
        - service-repair
        - service-training
      description: Product tax class
      title: >-
        SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaProductFieldDataTaxCategory
    SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaProductFieldDataEcProductType:
      type: string
      enum:
        - ff42fee0113744f693a764e3431a9cc2
        - f22027db68002190aef89a4a2b7ac8a1
        - c599e43b1a1c34d5a323aedf75d3adf6
        - b6ccc1830db4b1babeb06a9ac5f6dd76
      description: >-
        <a
        href="https://university.webflow.com/lesson/add-and-manage-products-and-categories?topics=ecommerce#how-to-understand-product-types">Product
        types.</a> Enums reflect the following values in order: Physical,
        Digital, Service, Advanced"
      title: >-
        SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaProductFieldDataEcProductType
    SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaProductFieldData:
      type: object
      properties:
        name:
          type: string
          description: Name of the Product
        slug:
          type: string
          description: URL structure of the Product in your site.
        description:
          type: string
          description: A description of your product
        shippable:
          type: boolean
          description: Boolean determining if the Product is shippable
        sku-properties:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaProductFieldDataSkuPropertiesItems
          description: Variant types to include in SKUs
        category:
          type: array
          items:
            type: string
          description: The category your product belongs to.
        tax-category:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaProductFieldDataTaxCategory
          description: Product tax class
        default-sku:
          type: string
          format: objectid
          description: The default SKU associated with this product.
        ec-product-type:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaProductFieldDataEcProductType
          description: >-
            <a
            href="https://university.webflow.com/lesson/add-and-manage-products-and-categories?topics=ecommerce#how-to-understand-product-types">Product
            types.</a> Enums reflect the following values in order: Physical,
            Digital, Service, Advanced"
      description: >-
        Contains content-specific details for a product, covering both standard
        (e.g., title, description) and custom fields tailored to the product
        setup.
      title: >-
        SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaProductFieldData
    SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaProduct:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier for the Product
        cmsLocaleId:
          type: string
          description: Identifier for the locale of the CMS item
        lastPublished:
          type: string
          format: date-time
          description: The date the Product was last published
        lastUpdated:
          type: string
          format: date-time
          description: The date the Product was last updated
        createdOn:
          type: string
          format: date-time
          description: The date the Product was created
        isArchived:
          type: boolean
          default: false
          description: Boolean determining if the Product is set to archived
        isDraft:
          type: boolean
          default: false
          description: Boolean determining if the Product is set to draft
        fieldData:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaProductFieldData
          description: >-
            Contains content-specific details for a product, covering both
            standard (e.g., title, description) and custom fields tailored to
            the product setup.
      description: The Product object
      title: >-
        SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaProduct
    SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaSkusItemsFieldDataPrice:
      type: object
      properties:
        value:
          type: number
          format: double
          description: Price of SKU
        unit:
          type: string
          description: Currency of Item
        currency:
          type: string
          description: Currency of Item (alternative representation)
      description: price of SKU
      title: >-
        SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaSkusItemsFieldDataPrice
    SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaSkusItemsFieldDataCompareAtPrice:
      type: object
      properties:
        value:
          type: number
          format: double
          description: Price of SKU
        unit:
          type: string
          description: Currency of Item
      description: comparison price of SKU
      title: >-
        SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaSkusItemsFieldDataCompareAtPrice
    SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuBillingMethod:
      type: string
      enum:
        - one-time
        - subscription
      description: >-
        [Billing
        method](https://help.webflow.com/hc/en-us/articles/33961432087955-Add-and-manage-products-and-categories#billing-methods)for
        the SKU
      title: >-
        SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuBillingMethod
    SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanInterval:
      type: string
      enum:
        - day
        - week
        - month
        - year
      description: Interval of subscription renewal
      title: >-
        SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanInterval
    SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanPlansItemsPlatform:
      type: string
      enum:
        - stripe
      description: The platform of the subscription plan
      title: >-
        SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanPlansItemsPlatform
    SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanPlansItemsStatus:
      type: string
      enum:
        - active
        - inactive
        - canceled
      description: The status of the plan
      title: >-
        SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanPlansItemsStatus
    SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanPlansItems:
      type: object
      properties:
        platform:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanPlansItemsPlatform
          description: The platform of the subscription plan
        id:
          type: string
          description: The unique identifier of the plan
        status:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanPlansItemsStatus
          description: The status of the plan
      title: >-
        SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanPlansItems
    SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlan:
      type: object
      properties:
        interval:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanInterval
          description: Interval of subscription renewal
        frequency:
          type: number
          format: double
          description: Frequncy of billing within interval
        trial:
          type: number
          format: double
          description: Number of days of a trial
        plans:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanPlansItems
      description: >-
        [Subscription
        plan](https://help.webflow.com/hc/en-us/articles/33961432087955-Add-and-manage-products-and-categories#subscription)
        for the SKU
      title: >-
        SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlan
    SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaSkusItemsFieldDataSkuPropertiesItemsEnumItems:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier for a Product variant/Option
        name:
          type: string
          description: Name of the Product variant/Option
        slug:
          type: string
          description: Slug for the Product variant/Option in the Site URL structure
      required:
        - id
        - name
        - slug
      description: Enumerated Product variants/Options for the SKU
      title: >-
        SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaSkusItemsFieldDataSkuPropertiesItemsEnumItems
    SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaSkusItemsFieldDataSkuPropertiesItems:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier for a collection of Product Variants
        name:
          type: string
          description: Name of the collection of Product Variants
        enum:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaSkusItemsFieldDataSkuPropertiesItemsEnumItems
          description: >-
            The individual Product variants that are contained within the
            collection
      required:
        - id
        - name
        - enum
      description: A variant/option type for a SKU
      title: >-
        SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaSkusItemsFieldDataSkuPropertiesItems
    SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaSkusItemsFieldData:
      type: object
      properties:
        sku-values:
          type: object
          additionalProperties:
            type: string
          description: >
            A mapping between SKU properties and their values, represented as
            key-value pairs. Each key represents a SKU Property ID (e.g.
            "color") and maps to its corresponding SKU Value ID (e.g. "blue").
            This structure defines the specific variant combination for a SKU.
        name:
          type: string
          description: Name of the Product
        slug:
          type: string
          description: URL structure of the Product in your site.
        price:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaSkusItemsFieldDataPrice
          description: price of SKU
        compare-at-price:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaSkusItemsFieldDataCompareAtPrice
          description: comparison price of SKU
        ec-sku-billing-method:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuBillingMethod
          description: >-
            [Billing
            method](https://help.webflow.com/hc/en-us/articles/33961432087955-Add-and-manage-products-and-categories#billing-methods)for
            the SKU
        ec-sku-subscription-plan:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlan
          description: >-
            [Subscription
            plan](https://help.webflow.com/hc/en-us/articles/33961432087955-Add-and-manage-products-and-categories#subscription)
            for the SKU
        main-image:
          type: string
          description: The URL for the main image of the SKU
        sku:
          type: string
          description: A unique identifier for the SKU
        sku-properties:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaSkusItemsFieldDataSkuPropertiesItems
          description: The properties of the SKU
      required:
        - name
        - slug
        - price
      description: Standard and Custom fields for a SKU
      title: >-
        SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaSkusItemsFieldData
    SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaSkusItems:
      type: object
      properties:
        id:
          type: string
          format: objectid
          description: Unique identifier for the Product
        cmsLocaleId:
          type: string
          description: Identifier for the locale of the CMS item
        lastPublished:
          type: string
          format: date-time
          description: The date the Product was last published
        lastUpdated:
          type: string
          format: date-time
          description: The date the Product was last updated
        createdOn:
          type: string
          format: date-time
          description: The date the Product was created
        fieldData:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaSkusItemsFieldData
          description: Standard and Custom fields for a SKU
      description: The SKU object
      title: >-
        SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaSkusItems
    products_get_Response_200:
      type: object
      properties:
        product:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaProduct
          description: The Product object
        skus:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaSkusItems
          description: A list of SKU Objects
      description: A product and its SKUs.
      title: products_get_Response_200
    SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaCode:
      type: string
      enum:
        - bad_request
        - collection_not_found
        - conflict
        - duplicate_collection
        - duplicate_user_email
        - ecommerce_not_enabled
        - forbidden
        - forms_require_republish
        - incompatible_webhook_filter
        - internal_error
        - invalid_auth_version
        - invalid_credentials
        - invalid_domain
        - invalid_user_email
        - item_not_found
        - missing_scopes
        - no_domains
        - not_authorized
        - not_enterprise_plan_site
        - not_enterprise_plan_workspace
        - order_not_found
        - resource_not_found
        - too_many_requests
        - unsupported_version
        - unsupported_webhook_trigger_type
        - user_limit_reached
        - user_not_found
        - users_not_enabled
        - validation_error
      description: Error code
      title: SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaCode
    SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: >-
        SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaDetailsItems
    Get-productRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaCode
          description: Error code
        message:
          type: string
          description: Error message
        externalReference:
          type: string
          description: Link to more information
        details:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-productRequestBadRequestError
    Get-productRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaCode
          description: Error code
        message:
          type: string
          description: Error message
        externalReference:
          type: string
          description: Link to more information
        details:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-productRequestUnauthorizedError
    Get-productRequestForbiddenError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaCode
          description: Error code
        message:
          type: string
          description: Error message
        externalReference:
          type: string
          description: Link to more information
        details:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-productRequestForbiddenError
    Get-productRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaCode
          description: Error code
        message:
          type: string
          description: Error message
        externalReference:
          type: string
          description: Link to more information
        details:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-productRequestNotFoundError
    Get-productRequestConflictError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaCode
          description: Error code
        message:
          type: string
          description: Error message
        externalReference:
          type: string
          description: Link to more information
        details:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-productRequestConflictError
    Get-productRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaCode
          description: Error code
        message:
          type: string
          description: Error message
        externalReference:
          type: string
          description: Link to more information
        details:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-productRequestTooManyRequestsError
    Get-productRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaCode
          description: Error code
        message:
          type: string
          description: Error message
        externalReference:
          type: string
          description: Link to more information
        details:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdProductsProductIdGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-productRequestInternalServerError
  securitySchemes:
    OAuth2:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.products.get(
    site_id="580e63e98c9a982ac9b8b741",
    product_id="580e63fc8c9a982ac9b8b745",
)

```

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.products.get("580e63e98c9a982ac9b8b741", "580e63fc8c9a982ac9b8b745");

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```