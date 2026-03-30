# Source: https://www.apollographql.com/docs/graphos/schema-design/guides/errors-as-data-explained.md

# Errors as Data Explained

If you're an enterprise customer looking for more material on this topic, try the [Enterprise best practices: Schema design](https://www.apollographql.com/tutorials/schema-design-best-practices) course on Odyssey.

Not an enterprise customer? [Learn about GraphOS for Enterprise.](https://www.apollographql.com/pricing?referrer=docs-content)

The GraphQL specification designates an [`errors` array](https://spec.graphql.org/October2021/#sec-Errors) to represent errors that occurred during a request.

```json
{
  "data": {
    "checkout": null
  },
  "errors": [
    {
      "path": ["checkout"],
      "locations": [
        { "line": 3, "column": 5 }
      ],
      "message": "Failed to process checkout",
      "extensions": {
        "code": "INTERNAL_SERVER_ERROR",
        "timestamp": "2024-10-29T10:00:00Z"
      }
    }
  ]
}
```

These top-level errors work well for certain types of errors but are less ideal for others.
Top-level errors lack a specified structure and strong typing—key benefits of a GraphQL schema—which makes them less useful for clients.

*Errors as data* is an approach to error handling that includes error types as part of your GraphQL schema, and subsequently as part of the `data` object in the response payload.
This approach allows clients to respond intelligently and provide a better end-user experience. It also enhances the developer experience via more maintainable code.

Errors as data is just one pattern for handling GraphQL errors. Check out Production Ready GraphQL's [Guide to GraphQL Errors](https://productionreadygraphql.com/2020-08-01-guide-to-graphql-errors) for an overview of other approaches.

## When to use errors as data

In the errors as data pattern, you encode errors into your schema *when the information the errors provide is relevant to the end-user experience*.
Other types of errors should remain in the `errors` array.

In general, the `errors` array is reserved for *system errors*—those that would typically result in an HTTP 500 error.
These errors are usually unexpected and can't be handled gracefully by the client. As a result, they should be logged and monitored on the server side, while the client should display a generic error message.

System errors can include situations like:

* Server crashes
* Unhandled exceptions
* Exhausted resources (for example, memory or CPU)

In contrast, *business logic errors* are useful for the client to know and pass on to the user.
For example, if a `checkout` mutation can't complete an order, the reasons why (insufficient stock, invalid payment method, shipping restrictions, etc.) would prompt different user experiences and next steps.
To more easily differentiate the user experience, these errors should become part of the known response types within your schema.

## How to implement errors as data

The errors as data pattern uses union types to represent different response scenarios.
Union types allow a single field to return one of several types, thus ideal for managing success and error cases.
This technique helps developers create flexible and expressive APIs that handle different scenarios efficiently.

### Example implementation

This example uses a `checkout` mutation that processes a user's cart and creates an order.
The possible responses for this mutation include:

* a successful order creation
* insufficient stock to process the order
* invalid payment method

You can use union types to represent these different response scenarios.

```graphql
union CheckoutResponse =
    Order
  | InsufficientStockError
  | InvalidPaymentMethodError

type Mutation {
  checkout(paymentMethod: ID!): CheckoutResponse
}

type Order {
  id: ID!
  items: [OrderItem!]!
  totalPrice: Float!
  status: String!
}

type OrderItem {
  id: ID!
  product: Product!
  quantity: Int!
  price: Float!
}

type Product {
  id: ID!
  name: String!
  price: Float!
}

interface CheckoutError {
  message: String!
}

type InsufficientStockError implements CheckoutError {
  message: String!
  product: Product!
  availableStock: Int!
}

type InvalidPaymentMethodError implements CheckoutError {
  message: String!
  paymentMethod: ID!
}
```

In the above schema, the `checkout` mutation returns a `CheckoutResponse` union type that can be one of the following types: `Order`, `InsufficientStockError`, or `InvalidPaymentMethodError`.

Additionally, the error types `InsufficientStockError` and `InvalidPaymentMethodError` implement a shared interface, `CheckoutError`, to provide consistent fields across different error types.
The client can then handle each of these cases explicitly.

### Example response handling

Now, let's look at a sample operation and the possible response handling:

```graphql
mutation OrderCheckout($payment: ID!) {
  checkout(paymentMethod: $payment) {
    ... on Order {
      id
      items {
        product {
          name
        }
        quantity
        price
      }
      totalPrice
      status
    }
    ... on InsufficientStockError {
      message
      product {
        name
      }
      availableStock
    }
    ... on InvalidPaymentMethodError {
      message
      paymentMethod
    }
  }
}
```

In this mutation, the client requests different fields for each possible response type:

* For a successful order creation (`Order`), the client retrieves the order details, including the items, total price, and status.
* For an insufficient stock error (`InsufficientStockError`), the client retrieves the error message, the affected product, and the available stock information. This information can be used to display a user-friendly error message and suggest alternative actions, such as updating the cart.
* For an invalid payment method error (`InvalidPaymentMethodError`), the client retrieves the error message and the problematic payment method ID. This can be used to inform the user about the issue and prompt them to update their payment information.

Using the `CheckoutResponse` union type, the API provides a clean and flexible way to handle the different response scenarios during the checkout process.
This allows the client to handle each case explicitly while providing strong typing for operation responses and a better developer experience.
