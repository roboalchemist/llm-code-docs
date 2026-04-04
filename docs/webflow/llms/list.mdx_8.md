# Source: https://developers.webflow.com/data/reference/ecommerce/products/list.mdx

# List Products & SKUs

GET https://api.webflow.com/v2/sites/{site_id}/products

Retrieve all products for a site.

Use `limit` and `offset` to page through all products with subsequent requests. All SKUs for each product
will also be fetched and returned. The `limit`, `offset` and `total` values represent Products only and do not include any SKUs.

Required scope | `ecommerce:read`


Reference: https://developers.webflow.com/data/reference/ecommerce/products/list

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /sites/{site_id}/products:
    get:
      operationId: list
      summary: List Products & SKUs
      description: >
        Retrieve all products for a site.


        Use `limit` and `offset` to page through all products with subsequent
        requests. All SKUs for each product

        will also be fetched and returned. The `limit`, `offset` and `total`
        values represent Products only and do not include any SKUs.


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
        - name: offset
          in: query
          description: >-
            Offset used for pagination if the results have more than limit
            records
          required: false
          schema:
            type: integer
        - name: limit
          in: query
          description: 'Maximum number of records to be returned (max limit: 100)'
          required: false
          schema:
            type: integer
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
                $ref: '#/components/schemas/products_list_Response_200'
        '400':
          description: Validation failure
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List-productsRequestBadRequestError'
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List-productsRequestUnauthorizedError'
        '403':
          description: Provided access token is valid, but is missing the required scopes.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List-productsRequestForbiddenError'
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List-productsRequestNotFoundError'
        '409':
          description: The site does not have ecommerce enabled.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List-productsRequestConflictError'
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List-productsRequestTooManyRequestsError'
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List-productsRequestInternalServerError'
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsProductFieldDataSkuPropertiesItemsEnumItems:
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
        SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsProductFieldDataSkuPropertiesItemsEnumItems
    SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsProductFieldDataSkuPropertiesItems:
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
              #/components/schemas/SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsProductFieldDataSkuPropertiesItemsEnumItems
          description: >-
            The individual Product variants that are contained within the
            collection
      required:
        - id
        - name
        - enum
      description: A variant/option type for a SKU
      title: >-
        SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsProductFieldDataSkuPropertiesItems
    SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsProductFieldDataTaxCategory:
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
        SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsProductFieldDataTaxCategory
    SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsProductFieldDataEcProductType:
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
        SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsProductFieldDataEcProductType
    SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsProductFieldData:
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
              #/components/schemas/SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsProductFieldDataSkuPropertiesItems
          description: Variant types to include in SKUs
        category:
          type: array
          items:
            type: string
          description: The category your product belongs to.
        tax-category:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsProductFieldDataTaxCategory
          description: Product tax class
        default-sku:
          type: string
          format: objectid
          description: The default SKU associated with this product.
        ec-product-type:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsProductFieldDataEcProductType
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
        SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsProductFieldData
    SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsProduct:
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
            #/components/schemas/SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsProductFieldData
          description: >-
            Contains content-specific details for a product, covering both
            standard (e.g., title, description) and custom fields tailored to
            the product setup.
      description: The Product object
      title: >-
        SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsProduct
    SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsSkusItemsFieldDataPrice:
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
        SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsSkusItemsFieldDataPrice
    SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsSkusItemsFieldDataCompareAtPrice:
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
        SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsSkusItemsFieldDataCompareAtPrice
    SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsSkusItemsFieldDataEcSkuBillingMethod:
      type: string
      enum:
        - one-time
        - subscription
      description: >-
        [Billing
        method](https://help.webflow.com/hc/en-us/articles/33961432087955-Add-and-manage-products-and-categories#billing-methods)for
        the SKU
      title: >-
        SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsSkusItemsFieldDataEcSkuBillingMethod
    SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsSkusItemsFieldDataEcSkuSubscriptionPlanInterval:
      type: string
      enum:
        - day
        - week
        - month
        - year
      description: Interval of subscription renewal
      title: >-
        SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsSkusItemsFieldDataEcSkuSubscriptionPlanInterval
    SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsSkusItemsFieldDataEcSkuSubscriptionPlanPlansItemsPlatform:
      type: string
      enum:
        - stripe
      description: The platform of the subscription plan
      title: >-
        SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsSkusItemsFieldDataEcSkuSubscriptionPlanPlansItemsPlatform
    SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsSkusItemsFieldDataEcSkuSubscriptionPlanPlansItemsStatus:
      type: string
      enum:
        - active
        - inactive
        - canceled
      description: The status of the plan
      title: >-
        SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsSkusItemsFieldDataEcSkuSubscriptionPlanPlansItemsStatus
    SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsSkusItemsFieldDataEcSkuSubscriptionPlanPlansItems:
      type: object
      properties:
        platform:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsSkusItemsFieldDataEcSkuSubscriptionPlanPlansItemsPlatform
          description: The platform of the subscription plan
        id:
          type: string
          description: The unique identifier of the plan
        status:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsSkusItemsFieldDataEcSkuSubscriptionPlanPlansItemsStatus
          description: The status of the plan
      title: >-
        SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsSkusItemsFieldDataEcSkuSubscriptionPlanPlansItems
    SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsSkusItemsFieldDataEcSkuSubscriptionPlan:
      type: object
      properties:
        interval:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsSkusItemsFieldDataEcSkuSubscriptionPlanInterval
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
              #/components/schemas/SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsSkusItemsFieldDataEcSkuSubscriptionPlanPlansItems
      description: >-
        [Subscription
        plan](https://help.webflow.com/hc/en-us/articles/33961432087955-Add-and-manage-products-and-categories#subscription)
        for the SKU
      title: >-
        SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsSkusItemsFieldDataEcSkuSubscriptionPlan
    SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsSkusItemsFieldDataSkuPropertiesItemsEnumItems:
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
        SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsSkusItemsFieldDataSkuPropertiesItemsEnumItems
    SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsSkusItemsFieldDataSkuPropertiesItems:
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
              #/components/schemas/SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsSkusItemsFieldDataSkuPropertiesItemsEnumItems
          description: >-
            The individual Product variants that are contained within the
            collection
      required:
        - id
        - name
        - enum
      description: A variant/option type for a SKU
      title: >-
        SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsSkusItemsFieldDataSkuPropertiesItems
    SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsSkusItemsFieldData:
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
            #/components/schemas/SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsSkusItemsFieldDataPrice
          description: price of SKU
        compare-at-price:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsSkusItemsFieldDataCompareAtPrice
          description: comparison price of SKU
        ec-sku-billing-method:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsSkusItemsFieldDataEcSkuBillingMethod
          description: >-
            [Billing
            method](https://help.webflow.com/hc/en-us/articles/33961432087955-Add-and-manage-products-and-categories#billing-methods)for
            the SKU
        ec-sku-subscription-plan:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsSkusItemsFieldDataEcSkuSubscriptionPlan
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
              #/components/schemas/SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsSkusItemsFieldDataSkuPropertiesItems
          description: The properties of the SKU
      required:
        - name
        - slug
        - price
      description: Standard and Custom fields for a SKU
      title: >-
        SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsSkusItemsFieldData
    SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsSkusItems:
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
            #/components/schemas/SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsSkusItemsFieldData
          description: Standard and Custom fields for a SKU
      description: The SKU object
      title: >-
        SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsSkusItems
    SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItems:
      type: object
      properties:
        product:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsProduct
          description: The Product object
        skus:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItemsSkusItems
          description: A list of SKU Objects
      description: A product and its SKUs.
      title: SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItems
    SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaPagination:
      type: object
      properties:
        limit:
          type: integer
          description: The limit used for pagination
        offset:
          type: integer
          description: The offset used for pagination
        total:
          type: integer
          description: The total number of records
      required:
        - limit
        - offset
        - total
      description: Pagination object
      title: SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaPagination
    products_list_Response_200:
      type: object
      properties:
        items:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaItemsItems
          description: >-
            List of Item objects within the Collection. Contains product and
            skus keys for each Item
        pagination:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaPagination
          description: Pagination object
      description: Results from product list
      title: products_list_Response_200
    SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaCode:
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
      title: SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaCode
    SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaDetailsItems
    List-productsRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: List-productsRequestBadRequestError
    List-productsRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: List-productsRequestUnauthorizedError
    List-productsRequestForbiddenError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: List-productsRequestForbiddenError
    List-productsRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: List-productsRequestNotFoundError
    List-productsRequestConflictError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: List-productsRequestConflictError
    List-productsRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: List-productsRequestTooManyRequestsError
    List-productsRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdProductsGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: List-productsRequestInternalServerError
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
client.products.list(
    site_id="580e63e98c9a982ac9b8b741",
    offset=1,
    limit=1,
)

```

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.products.list("580e63e98c9a982ac9b8b741", {
    offset: 1,
    limit: 1
});

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/products?offset=0&limit=100"

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

url = URI("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/products?offset=0&limit=100")

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

HttpResponse<String> response = Unirest.get("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/products?offset=0&limit=100")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/products?offset=0&limit=100', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/products?offset=0&limit=100");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/products?offset=0&limit=100")! as URL,
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