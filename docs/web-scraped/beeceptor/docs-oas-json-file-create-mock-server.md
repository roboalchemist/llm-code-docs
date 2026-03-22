# Source: https://beeceptor.com/docs/oas-json-file-create-mock-server/

Title: OpenAPI Mock Server | Beeceptor

URL Source: https://beeceptor.com/docs/oas-json-file-create-mock-server/

Markdown Content:
The OpenAPI Specification (OAS) is a widely adopted, language-agnostic format for defining RESTful APIs. It enables developers to describe the structure of their APIs using a declarative format in either YAML or JSON, without needing to access or write the actual server-side implementation.

Beeceptor gives you more power to 'activate' the contracts by creating **mock server with test data**, in one click, from your OpenAPI spec definition. With this feature, you can upload your OAS file, instantly spin up a mock server, and begin testing or demonstrating your APIs without writing a single line of backend code.

info

AI-Powered Intelligent Mocking is part of the paid plans. You can [try it here](https://beeceptor.com/openapi-mock-server/?utm_source=beeceptor&utm_campaign=) for free with a limit of 50 requests per day.

Upload OpenAPI Specification[​](https://beeceptor.com/docs/oas-json-file-create-mock-server/#upload-openapi-specification "Direct link to Upload OpenAPI Specification")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Beeceptor supports both YAML and JSON representations of the OpenAPI Specification.

### How to Upload[​](https://beeceptor.com/docs/oas-json-file-create-mock-server/#how-to-upload "Direct link to How to Upload")

1.   Navigate to your Beeceptor dashboard.
2.   Go to _Account Menu_>_Your Endpoints_ and select an endpoint.
3.   Click on _Settings_ for the selected endpoint.
4.   Find the _OpenAPI Setup_ section.

![Image 1: uploading-oas-in-beeceptor](https://beeceptor.com/docs/assets/images/my-endpoints-settings-1e17b993fe8a0efc462fdadeeca23444.png)

From this interface, you can:

*   Upload a new OAS file to generate your mock server.
*   Download an already-configured specification.
*   Remove an existing specification if it's no longer needed.

![Image 2: uploading-oas-in-beeceptor](https://beeceptor.com/docs/assets/images/my-endpoints-oas-settings-39d603fb43141e849e3344c975259faa.png)

Once uploaded, Beeceptor automatically parses the spec and prepares mock responses based on your API definitions.

Request Matching Logic[​](https://beeceptor.com/docs/oas-json-file-create-mock-server/#request-matching-logic "Direct link to Request Matching Logic")
------------------------------------------------------------------------------------------------------------------------------------------------------

After a successful upload of the OpenAPI specification, Beeceptor automatically starts matching incoming HTTP requests based on your defined paths and operations.

**Matching Priority**

1.   **Mock Rules (Highest Priority)** – If any user-defined mock rule matches the incoming request, Beeceptor serves that response.
2.   **OpenAPI Spec** – If no mock rule matches, Beeceptor falls back to the specification. It looks for matching path and operation and serves a default response based on the API schema.

Response Generation[​](https://beeceptor.com/docs/oas-json-file-create-mock-server/#response-generation "Direct link to Response Generation")
---------------------------------------------------------------------------------------------------------------------------------------------

Beeceptor supports two modes of response generation based on your OpenAPI specification:

### 1. Static Response Generation[​](https://beeceptor.com/docs/oas-json-file-create-mock-server/#1-static-response-generation "Direct link to 1. Static Response Generation")

In static mode, Beeceptor responds with basic placeholder data that conforms to your API's data types and schema. If examples are provided in the spec, Beeceptor uses those. Otherwise, it generates dummy values to match the structure.

**Example Output:**

`{  "id": "string",  "name": "string",  "price": 0,  "stock": 0}`

This is ideal for validating contracts, testing integration flows, and ensuring clients correctly handle data types.

### 2. AI-Powered Intelligent Mocking[​](https://beeceptor.com/docs/oas-json-file-create-mock-server/#2-ai-powered-intelligent-mocking "Direct link to 2. AI-Powered Intelligent Mocking")

With Intelligent Mocking, Beeceptor uses AI to generate realistic test data based on the API schema, field names, and descriptions.

For example, if a field is called `product_name`, Beeceptor will generate a demo-friendly name like "Wireless Headphones" instead of a generic "string".

Benefits:

*   Great for demos and presentations
*   Helps frontend teams work independently with realistic data
*   Eliminates need for hand-written examples or seed data

To enable this feature, select the "Enable intelligent API mocking" option in your endpoint settings when uploading a new OpenAPI specification file.

Example: E-commerce Product Catalog[​](https://beeceptor.com/docs/oas-json-file-create-mock-server/#example-e-commerce-product-catalog "Direct link to Example: E-commerce Product Catalog")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Let’s walk through a simple OpenAPI example for an e-commerce application that includes two endpoints: one for listing products, and another for retrieving a single product's details.

### OpenAPI Spec (YAML)[​](https://beeceptor.com/docs/oas-json-file-create-mock-server/#openapi-spec-yaml "Direct link to OpenAPI Spec (YAML)")

With Beeceptor, you can upload this spec and get immediately functional endpoints that respond with either static placeholder data or AI-generated product listings.

`openapi: 3.1.0info:  title: Products API  version: 1.0.0  description: An API spec exposing product listing and product details     for use in an e-commerce storefront or catalog service.servers:  - url: https://api.demo-ecommerce.com/v1    description: Production environmentcomponents:  schemas:    Product:      type: object      required: [id, name, price, stock, category]      properties:        id:          type: string          format: uuid        name:          type: string        description:          type: string        price:          type: number          format: float        category:          type: string        image_url:          type: string          format: uri        stock:          type: integer          example: 94        created_at:          type: string          format: date-time        updated_at:          type: string          format: date-timepaths:  /products:    get:      summary: List all products with filters      parameters:        - name: search          in: query          schema:            type: string        - name: min_price          in: query          schema:            type: number        - name: max_price          in: query          schema:            type: number      responses:        '200':          description: List of products          content:            application/json:              schema:                type: array                items:                  $ref: '#/components/schemas/Product'  /products/{id}:    get:      summary: Get product details by ID      parameters:        - name: id          in: path          required: true          schema:            type: string            format: uuid      responses:        '200':          description: Product details          content:            application/json:              schema:                $ref: '#/components/schemas/Product'`

### Intelligent Mock Responses (AI-Generated)[​](https://beeceptor.com/docs/oas-json-file-create-mock-server/#intelligent-mock-responses-ai-generated "Direct link to Intelligent Mock Responses (AI-Generated)")

When Intelligent Mocking is enabled, Beeceptor uses AI to generate contextual and semantically meaningful mock responses based on your OpenAPI schema. Unlike static mocks that fill fields with generic or random data, intelligent mocks consider the field names, data types, and even descriptions to generate values that align with real-world expectations.

Here’s a sample AI-generated response for a `Product` schema:

`{  "id": "e2105e71-22a9-438c-8c10-17d89bc0435a",  "name": "Modern Ceramic Tuna",  "price": 638.69,  "stock": 478,  "category": "Books",  "updated_at": "2025-05-22T00:00:00.0Z",  "description": "The sleek and mediocre Fish comes with pink LED lighting for smart functionality",  "created_at": "2024-08-24T00:00:00.0Z",  "image_url": "https://picsum.photos/seed/oJ07L/640/480"}`

What's Contextual Here?

*   `name`: Rather than a placeholder like "string" or "dolore est elit do", Beeceptor generates a plausible product name — "Modern Ceramic Tuna" — following naming patterns common in e-commerce catalogs.
*   `price`: The value 638.69 respects the expected price range for a commercial product and uses a valid floating-point format, making it more suitable for UI rendering and calculations.
*   `created_at`&`updated_at`: These timestamps follow ISO 8601 format, and both appears in the past, reflecting a real-world data lifecycle.
*   `description`: Instead of placeholder text like "lorem ipsum", it generates a quirky and product-relevant sentence that enhances realism in frontend components and marketing-style presentations.

### Static Response (Default Mode)[​](https://beeceptor.com/docs/oas-json-file-create-mock-server/#static-response-default-mode "Direct link to Static Response (Default Mode)")

Without Intelligent Mocking, Beeceptor generates static mock responses based only on data types. These placeholder values serve the purpose of contract validation but may lack realism or usability for visual or functional testing.

Example static mock response:

`{  "id": "0126485e-5960-38bc-6189-8dd1f7bfab33",  "name": "dolore est elit do",  "price": 3.2442671449221092e+38,  "stock": -42370641,  "category": "dolore",  "image_url": "https://toNgXNxuRUFfdwioCGKGss.ygdYfb8lexDa.M9-5vWL1ddJzn-YvZDu",  "created_at": "1932-09-28T18:03:37.0Z",  "updated_at": "1926-06-28T06:27:22.0Z",  "description": "in elit"}`

The values in static mode may appear random or outdated and aren't suitable for demo environments without further customization.

Summary[​](https://beeceptor.com/docs/oas-json-file-create-mock-server/#summary "Direct link to Summary")
---------------------------------------------------------------------------------------------------------

Beeceptor’s OpenAPI integration provides a fast and reliable way to mock REST APIs using your OpenAPI Specification (OAS). By uploading a YAML or JSON spec, you can **instantly spin up a mock server** that responds according to your API definition, no backend code required. For an enhanced experience, enable AI-powered intelligent mocking to generate **realistic, contract-compliant test data** automatically.

For **API publishers**, this feature helps deliver a smooth onboarding experience to API consumers. Developers can explore and test your APIs without needing API keys or a developer account, making it easier to evaluate and integrate with your platform.

For **API consumers**, especially when working with unavailable or rate-limited APIs, Beeceptor enables a contract-first development approach. You can build and test your integration against the mock server, reducing dependency on real environments and speeding up your development workflow.

See Also[​](https://beeceptor.com/docs/oas-json-file-create-mock-server/#see-also "Direct link to See Also")
------------------------------------------------------------------------------------------------------------

*   [Customize Test Data for OpenAPI](https://beeceptor.com/docs/openapi-mock-server-test-data-generator/) - Review and adjust how mock responses generate field values to produce realistic and predictable API responses.
*   [gRPC Mock Server](https://beeceptor.com/docs/grpc-mock-server/) - Create mock gRPC services with the same AI-driven response generation.
