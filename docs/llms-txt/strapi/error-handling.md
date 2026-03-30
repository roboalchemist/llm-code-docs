# Error handling

Strapi is natively handling errors with a standard format.

There are 2 use cases for error handling:

- As a developer querying content through the [REST](/cms/api/rest) or [GraphQL](/cms/api/graphql) APIs, you might [receive errors](#receiving-errors) in response to the requests.
- As a developer customizing the backend of your Strapi application, you could use controllers and services to [throw errors](#throwing-errors).

## Receiving errors

Errors are included in the response object with the `error` key and include information such as the HTTP status code, the name of the error, and additional information.

### REST errors

Errors thrown by the REST API are included in the [response](/cms/api/rest#requests) that has the following format:

```json
{
  "data": null,
  "error": {
    "status": "", // HTTP status
    "name": "", // Strapi error name ('ApplicationError' or 'ValidationError')
    "message": "", // A human readable error message
    "details": {
      // error info specific to the error type
    }
  }
}
```

### GraphQL errors

Errors thrown by the GraphQL API are included in the response that has the following format:

```json
{ "errors": [
    {
      "message": "", // A human reable error message
      "extensions": {
        "error": {
          "name": "", // Strapi error name ('ApplicationError' or 'ValidationError'),
          "message": "", // A human reable error message (same one as above);
          "details": {}, // Error info specific to the error type
        },
        "code": "" // GraphQL error code (ex: BAD_USER_INPUT)
      }
    }
  ],
  "data": {
    "graphQLQueryName": null
  }
}
```

## Throwing errors

<br/>

### Controllers and middlewares

The recommended way to throw errors when developing any custom logic with Strapi is to have the [controller](/cms/backend-customization/controllers) or [middleware](/cms/backend-customization/middlewares) respond with the correct status and body.

This can be done by calling an error function on the context (i.e. `ctx`). Available error functions are listed in the 

</Tabs>

### Services and models lifecycles

Once you are working at a deeper layer than the controllers or middlewares there are dedicated error classes that can be used to throw errors. These classes are extensions of 

</Tabs>

#### Example: Throwing an error in a model lifecycle**

This example shows building a [custom model lifecycle](/cms/backend-customization/models#lifecycle-hooks) and being able to throw an error that stops the request and will return proper error messages to the admin panel. Generally you should only throw an error in `beforeX` lifecycles, not `afterX` lifecycles.

</Tabs>

### Policies

[Policies](/cms/backend-customization/policies) are a special type of middleware that are executed before a controller. They are used to check if the user is allowed to perform the action or not. If the user is not allowed to perform the action and a `return false` is used then a generic error will be thrown. As an alternative, you can throw a custom error message using a nested class extensions from the Strapi `ForbiddenError` class, `ApplicationError` class (see [Default error classes](#default-error-classes) for both classes), and finally the 

</Tabs>

### Default error classes

The default error classes are available from the `@strapi/utils` package and can be imported and used in your code. Any of the default error classes can be extended to create a custom error class. The custom error class can then be used in your code to throw errors.

<!-- Not sure if it's worth keeping this tab or not as it's very specific to Strapi internal use-cases -->
<!-- ::: tab Validation

The `ValidationError` and `YupValidationError` classes are specific error classes designed to be used with the built in validations system and specifically format the errors coming from 

</Tabs>