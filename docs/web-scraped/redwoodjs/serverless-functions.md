# Source: https://docs.redwoodjs.com/docs/serverless-functions

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [Serverless Functions (API Endpoints)]

[Version: 8.8]

On this page

<div>

# Serverless Functions (API Endpoints)

</div>

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]info

You can think of serverless functions as API Endpoints, and in the future we\'ll update the terminology used.

Originally, Redwood apps were intended to be deployed as serverless functions to AWS Lambda. Whenever a Redwood app is deployed to a \"serverful\" environment such as Fly or Render, a Fastify server is started and your Redwood app\'s functions in `api/src/functions` are automatically registered onto the server. Request adapters are also automatically configured to handle the translation between Fastify\'s request and reply objects to the functions\' AWS Lambda signature.

Redwood looks for serverless functions in `api/src/functions`. Each function is mapped to a URI based on its filename. For example, you can find `api/src/functions/graphql.js` at `http://localhost:8911/graphql`.

## Creating Serverless Functions[​](#creating-serverless-functions "Direct link to Creating Serverless Functions") 

Creating serverless functions is easy with Redwood\'s function generator:

``` 
yarn rw g function <name>
```

This will generate a stub serverless function in the folder `api/src/functions/<name>`, along with a test and an empty scenarios file.

*Example of a bare minimum handler you need to get going:*

``` 
export const handler = async (event, context) => ,
    body: JSON.stringify( function',
    }),
  }
}
```

## The handler[​](#the-handler "Direct link to The handler") 

For a lambda function to be a lambda function, it must export a handler that returns a status code. The handler receives two arguments: `event` and `context`. Whatever it returns is the `response`, which should include a `statusCode` at the very least.

> **File/Folder Structure**
>
> For example, with a target function endpoint name of /hello, you could save the function file in one of the following ways:
>
> -   `./api/src/functions/hello.ts`
> -   `./api/src/functions/hello/hello.ts`
> -   `./api/src/functions/hello/index.ts`
>
> Other files in the folder will *not* be exposed as an endpoint

### Re-using/Sharing code[​](#re-usingsharing-code "Direct link to Re-using/Sharing code") 

You can use code in `api/src` in your serverless function, some examples:

``` 
// importing `db` directly
import  from 'src/lib/db'

// importing services
import  from 'src/services/subscriptions'

// importing a custom shared library
import  from 'src/lib/errorHandling'
```

If you just want to move some logic into another file, that\'s totally fine too!

``` 
api/src
├── functions
│   ├── graphql.ts
│   └── helloWorld
│   ├── helloWorld.scenarios.ts
│   ├── helloWorld.test.ts
│   └── helloWorld.ts    # <-- imports hellWorldLib
│   └── helloWorldLib.ts # <-- exports can be used in the helloWorld
```

## Developing locally[​](#developing-locally "Direct link to Developing locally") 

When you run `yarn rw dev` - it\'ll watch for changes and make your functions available at:

-   `localhost:8911/` and
-   `localhost:8910/.redwood/functions/` (used by the web side).

Note that the `.redwood/functions` path is determined by your setting in your [redwood.toml](/docs/app-configuration-redwood-toml#web) - and is used both in development and in the deployed Redwood app

## Testing[​](#testing "Direct link to Testing") 

You can write tests and scenarios for your serverless functions very much like you would for services, but it\'s important to properly mock the information that the function `handler` needs.

To help you mock the `event` and `context` information, we\'ve provided several api testing fixture utilities:

Mock

Usage

`mockHttpEvent`

Use this to mock out the http request `event` that is received by your function in unit tests. Here you can set `headers`, `httpMethod`, `queryStringParameters` as well as the `body` and if the body `isBase64Encoded`. The `event` contains information from the invoker as JSON-formatted string whose structure will vary. See [Working with AWS Lambda proxy integrations for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html) for the payload format.

`mockContext`

Use this function to mock the http `context`. Your function handler receives a context object with properties that provide information about the invocation, function, and execution environment. See [AWS Lambda context object in Node.js](https://docs.aws.amazon.com/lambda/latest/dg/nodejs-context.html) for what context properties you can mock.

`mockSignedWebhook`

Use this function to mock a signed webhook. This is a specialized `mockHttpEvent` mock that also signs the payload and adds a signature header needed to verify that the webhook is trustworthy. See [How to Receive and Verify an Incoming Webhook](/docs/webhooks#how-to-receive-and-verify-an-incoming-webhook) to learn more about signing and verifying webhooks.

### How to Test Serverless Functions[​](#how-to-test-serverless-functions "Direct link to How to Test Serverless Functions") 

Let\'s learn how to test a serverless function by first creating a simple function that divides two numbers.

As with all serverless lambda functions, the handler accepts an `APIGatewayEvent` which contains information from the invoker. That means it will have the HTTP headers, the querystring parameters, the method (GET, POST, PUT, etc), cookies, and the body of the request. See [Working with AWS Lambda proxy integrations for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html) for the payload format.

Let\'s generate our function:

``` 
yarn rw generate function divide
```

We\'ll use the querystring to pass the `dividend` and `divisor` to the function handler on the event as seen here to divide 10 by 2.

``` 
// request
http://localhost:8911/divide?dividend=10 &
divisor=2
```

If the function can successfully divide the two numbers, the function returns a body payload back in the response with a [HTTP 200 Success](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200) status:

``` 
// response

```

And, we\'ll have some error handling to consider the case when either the dividend or divisor is missing and return a [HTTP 400 Bad Request](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/400) status code; or, if we try to divide by zero or something else goes wrong, we return a [500 Internal Server Error](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500).

api/src/functions/divide/divide.ts

``` 
import type  from 'aws-lambda'

export const handler = async (event: APIGatewayEvent) =>  = event.queryStringParameters

    // make sure the values to divide are provided
    if (dividend === undefined || divisor === undefined) 

    // divide the two numbers
    const quotient = parseInt(dividend) / parseInt(divisor)
    message = `$ / $ = $`

    // check if the numbers could be divided
    if (!isFinite(quotient))  by $`
      throw Error(message)
    }

    return ,
    }
  } catch (error) ,
    }
  }
}
```

Sure, you could launch a browser or use Curl or some other manual approach and try out various combinations to test the success and error cases, but we want to automate the tests as part of our app\'s CI.

That means we need to write some tests.

#### Function Unit Tests[​](#function-unit-tests "Direct link to Function Unit Tests") 

To test a serverless function, you\'ll work with the test script associated with the function. You\'ll find it in the same directory as your function:

``` 
api
├── src
│ ├── functions
│ │ ├── divide
│ │ │ ├── divide.ts
│ │ │ ├── divide.test.ts
```

The setup steps are to:

-   write your test cases by mocking the event using `mockHttpEvent` to contain the information you want to give the handler
-   invoke the handler with the mocked event
-   extract the result body
-   test that the values match what you expect

The boilerplate steps are generated automatically for you by the function generator Let\'s look at a series of tests that mock the event with different information in each.

First, let\'s write a test that divides 20 by 5 and we\'ll expect to get 4 as the quotient:

api/src/functions/divideBy/divide.test.ts

``` 
import  from '@redwoodjs/testing/api'
import  from './divide'

describe('divide serverless function',  () => ,
    })

    const result = await handler(httpEvent)
    const body = result.body

    expect(result.statusCode).toBe(200)
    expect(body.message).toContain('=')
    expect(body.quotient).toEqual(4)
  })
```

Then we can also add a test to handle the error when we don\'t provide a dividend:

api/src/functions/divideBy/divide.test.ts

``` 
it('requires a dividend', async () => ,
  })

  const result = await handler(httpEvent)
  const body = result.body
  expect(result.statusCode).toBe(400)
  expect(body.message).toContain('Please specify both')
  expect(body.quotient).toBeUndefined
})
```

And finally, we can also add a test to handle the error when we try to divide by 0:

``` 
  it('cannot divide by 0', async () => ,
    })

    const result = await handler(httpEvent)
    const body = result.body

    expect(result.statusCode).toBe(500)
    expect(body.message).toContain('Could not divide')
    expect(body.quotient).toBeUndefined
  })
})
```

The `divide` function is a simple example, but you can use the `mockHttpEvent` to set any event values you handler needs to test more complex functions.

You can also `mockContext` and pass the mocked `context` to the handler and even create scenario data if your function interacts with your database. For an example of using scenarios when test functions, please look at a specialized serverless function: the [webhook below](#how-to-test-webhooks).

#### Running Function Tests[​](#running-function-tests "Direct link to Running Function Tests") 

To run an individual serverless function test:

``` 
yarn rw test api divide
```

When the test run completes (and succeeds), you see the results:

``` 
 PASS   api  api/src/functions/divide/divide.test.ts (12.69 s)
  divide serverless function
    ✓ divides two numbers successfully (153 ms)
    ✓ requires a dividend (48 ms)
    ✓ requires a divisor (45 ms)
    ✓ cannot divide by 0 (47 ms)

Test Suites: 1 passed, 1 total
Tests:       4 passed, 4 total
Snapshots:   0 total
Time:        13.155 s
Ran all test suites matching /divide.test.ts|divide.test.ts|false/i.
```

If the test fails, you can update your function or test script and the test will automatically re-run.

### Using Test Fixtures[​](#using-test-fixtures "Direct link to Using Test Fixtures") 

Often times your serverless function will have a variety of test cases, but because it may not interact with the database, you don\'t want to use scenarios (since that creates records in your test database). But, you still want a way to define these cases in a more declarative way for readability and maintainability \-- and you can using fixtures.

First, let\'s create a fixture for the `divide` function alongside your function and test as `divide.fixtures.ts`:

``` 
api
├── src
│ ├── functions
│ │ ├── divide
│ │ │ ├── divide.ts
│ │ │ ├── divide.test.ts
│ │ │ ├── divide.fixtures.ts // your fixture < --
```

Let\'s define a fixture for a new test case: when the function is invoked, but it is missing a divisor:

api/src/functions/divide/divide.fixtures.ts

``` 
import  from '@redwoodjs/testing/api'

export const missingDivisor = () =>
  mockHttpEvent(,
  })
```

The `missingDivisor()` fixture constructs and mocks the event for the test case \-- that is, we don\'t provide a divisor value in the `queryStringParameters` in the mocked http event.

Now, let\'s use this fixture in a test by providing the handler with the event we mocked in the fixture:

api/src/functions/divide/divide.test.ts

``` 
import  from './divide.fixtures'

describe('divide serverless function', () => )

  // ...
})
```

Now, if we decide to change the test case date, we simply modify the fixture and re-run our tests.

You can then define multiple fixtures to define all the cases in a central place, export each, and then use in your tests for more maintainable and readable tests.

### How to Test Webhooks[​](#how-to-test-webhooks "Direct link to How to Test Webhooks") 

[Webhooks](/docs/webhooks) are specialized serverless functions that will verify a signature header to ensure you can trust the incoming request and use the payload with confidence.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

Want to learn more about webhooks? See a [Detailed discussion of webhooks](/docs/webhooks) to find out how webhooks can give your app the power to create complex workflows, build one-to-one automation, and sync data between apps.

In the following example, we\'ll have the webhook interact with our app\'s database, so we can see how we can use **scenario testing** to create data that the handler can access and modify.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6Ij48L3BhdGg+PC9zdmc+)]**Why testing webhooks is hard**

Because your webhook is typically sent from a third-party\'s system, manually testing webhooks can be difficult. For one thing, you often have to create some kind of event in their system that will trigger the event \-- and you\'ll often have to do that in a production environment with real data. Second, for each case you\'ll have to find data that represents each case and issue a hook for each \-- which can take a lot of time and is tedious.

Also, you\'ll be using production secrets to sign the payload. And finally, since your third-party needs to send you the incoming webhook you\'ll most likely have to launch a local tunnel to expose your development machine publicly in order to receive them.

Instead, we can automate and mock the webhook to contain a signed payload that we can use to test the handler.

By writing these tests, you can iterate and implement the webhook logic much faster and easier without having to rely on a third party to send you data, or setting up tunneling, or triggering events on the external system.

For our webhook test example, we\'ll create a webhook that updates a Order\'s Status by looking up the order by its Tracking Number and then updating the status to by Delivered (if our rules allow it).

Because we\'ll be interacting with data, our app has an `Order` model defined in the Prisma schema that has a unique `trackingNumber` and `status`:

/api/db/schema.prisma

``` 
model Order 
```

Let\'s generate our webhook function:

``` 
yarn rw generate function updateOrderStatus
```

``` 
api
├── src
│ ├── functions
│ │ ├── updateOrderStatus
│ │ │ ├── updateOrderStatus.ts
│ │ │ ├── updateOrderStatus.scenarios.ts
│ │ │ ├── updateOrderStatus.test.ts
```

The `updateOrderStatus` webhook will expect:

-   a signature header named `X-Webhook-Signature`
-   that the signature in that header will signed using the [SHA256 method](/docs/webhooks#sha256-verifier-used-by-github-discourse)
-   verify the signature and throw an [401 Unauthorized](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/401) error if the event cannot be trusted (that is, it failed signature verification)
-   if verified, then proceed to
-   find the order by the tracking number provided
-   check that the order\'s current status allows the status to be changed
-   and if so, update the error and return the order and message
-   or if not, return a [500 internal server error](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500) with a message that the order couldn\'t be updated

``` 
import type  from 'aws-lambda'
import  from '@redwoodjs/api/webhooks'
import  from 'src/lib/db'

export const handler = async (event: APIGatewayEvent) =>  as VerifyOptions

    verifyEvent('sha256Verifier', )

    // Safely use the validated webhook payload body
    const body = JSON.parse(event.body)
    const trackingNumber = body.trackingNumber
    const status = body.status

    // You can only update the status if the order's current status allows
    switch (status) 

    // updated the order with the new status
    // using the trackingNumber provided
    const order = await db.order.update(,
      },
      data: ,
    })

    return  to $ at $`,
      }),
    }
  } catch (error) 
    } else ),
      }
    }
  }
}
```

#### Webhook Test Scenarios[​](#webhook-test-scenarios "Direct link to Webhook Test Scenarios") 

Since our `updateOrderStatus` webhook will query an order by its tracking number and then attempt to update its status, we\'ll want to seed our test run with some scenario data that helps us have records we can use to test that the webhook does what we expect it to in each situation.

Let\'s create three orders for with different status: `PLACED`, `SHIPPED`, and `DELIVERED`.

We\'ll use these to test that you cannot update an order to the delivered status unless it is currently \"shipped:.

We can refer to these individual orders in our tests as `scenario.order.placed`, `scenario.order.shipped` , or `scenario.order.delivered`.

api/src/functions/updateOrderStatus/updateOrderStatus.scenarios.ts

``` 
export const standard = defineScenario(,
    },
    shipped: ,
    },
    delivered: ,
    },
  },
})
```

#### Webhook Unit Tests[​](#webhook-unit-tests "Direct link to Webhook Unit Tests") 

The webhook test setup needs to:

-   import your api testing utilities, such as `mockSignedWebhook`
-   import your function handler

In each test scenario we will:

-   get the scenario order data
-   create a webhook payload with a tracking number and a status what we want to change its order to
-   mock and sign the webhook using `mockSignedWebhook` that specifies the verifier method, signature header, and the secret that will verify that signature
-   invoke the handler with the mocked signed event
-   extract the result body (and parse it since it will be JSON data)
-   test that the values match what you expect

In our first scenario, we\'ll use the shipped order to test that we can update the order given a valid tracking number and change its status to delivered:

api/src/functions/updateOrderStatus/updateOrderStatus.test.ts

``` 
import  from '@redwoodjs/testing/api'
import  from './updateOrderStatus'

describe('updates an order via a webhook', () => 

    const event = mockSignedWebhook()

    const result = await handler(event)

    const body = JSON.parse(result.body)

    expect(result.statusCode).toBe(200)
    expect(body.message).toContain(`Updated order $`)
    expect(body.message).toContain(`to $`)
    expect(body.order.id).toEqual(order.id)
    expect(body.order.status).toEqual(payload.status)
  })
```

But, we also want to test what happens if the webhook receives an invalid signature header like `X-Webhook-Signature-Invalid`.

Because the header isn\'t what the webhook expects (it wants to see a header named `X-Webhook-Signature`), this request is not verified and will return a 401 Unauthorized and not try to update the order at all.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

For brevity we didn\'t test that the order\'s status wasn\'t changed, but that could be checked as well

``` 
scenario(
  'with an invalid signature header, the webhook is unauthorized',
  async (scenario) => 
    const event = mockSignedWebhook()

    const result = await handler(event)

    expect(result.statusCode).toBe(401)
  }
)
```

Next, we test what happens if the event payload is signed, but with a different secret than it expects; that is it was signed using the wrong secret (`MY-NAME-IS-WERNER-BRANDES-VERIFY-ME` and not `MY-VOICE-IS-MY-PASSPORT-VERIFY-ME`).

Again, we expect as 401 Unauthorized response.

``` 
scenario(
  'with the wrong webhook secret the webhook is unauthorized',
  async (scenario) => 
    const event = mockSignedWebhook()

    const result = await handler(event)

    expect(result.statusCode).toBe(401)
  }
)
```

Next, what happens if the order cannot be found? We\'ll try a tracking number that doesn\'t exist (that is we did not create it in our scenario order data):

``` 
scenario(
  'when the tracking number cannot be found, returns an error',
  async (scenario) => 
    const event = mockSignedWebhook()

    const result = await handler(event)

    const body = JSON.parse(result.body)

    expect(result.statusCode).toBe(500)
    expect(body).toHaveProperty('error')
  }
)
```

Last, we want to test a business rule that says you cannot update an order to be delivered if it already is delivered

Therefore our scenario uses the `scenario.order.delivered` data where the order has a placed status.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6Ij48L3BhdGg+PC9zdmc+)]tip

You\'ll have additional tests here to check that if the order is placed you cannot update it to be delivered and if the order is shipped you cannot update to be placed, etc

``` 
  scenario('when the order has already been delivered, returns an error',
            async (scenario) => 
    const event = mockSignedWebhook()

    const result = await handler(event)

    const body = JSON.parse(result.body)

    expect(result.statusCode).toBe(500)
    expect(body).toHaveProperty('error')
    expect(body.message).toEqual('Unable to update the order status')
  })
})
```

As with other serverless function testing, you can also `mockContext` and pass the mocked context to the handler if your webhook requires that information.

#### Running Webhook Tests[​](#running-webhook-tests "Direct link to Running Webhook Tests") 

To run an individual webhook test:

``` 
yarn rw test api updateOrderStatus
```

When the test run completes (and succeeds), you see the results:

``` 
 PASS   api  api/src/functions/updateOrderStatus/updateOrderStatus.test.ts (10.3 s)
  updates an order via a webhook
    ✓ with a shipped order, updates the status to DELIVERED (549 ms)
    ✓ with an invalid signature header, the webhook is unauthorized (51 ms)
    ✓ with the wrong webhook secret the webhook is unauthorized (44 ms)
    ✓ when the tracking number cannot be found, returns an error (54 ms)
    ✓ when the order has not yet shipped, returns an error (57 ms)
    ✓ when the order has already been delivered, returns an error (73 ms)

Test Suites: 1 passed, 1 total
Tests:       6 passed, 6 total
Snapshots:   0 total
Time:        10.694 s, estimated 36 s
Ran all test suites matching /updateOrderStatus.test.ts|updateOrderStatus.test.ts|false/i.
```

If the test fails, you can update your function or test script and the test will automatically re-run.

## Security considerations[​](#security-considerations "Direct link to Security considerations") 

When deployed, **a custom serverless function is an open API endpoint and is your responsibility to secure appropriately**. 🔐

That means *anyone* can access your function and perform any tasks it\'s asked to do. In many cases, this is completely appropriate and desired behavior.

But, in some cases, for example when the function interacts with third parties, like sending email, or when it retrieves sensitive information from a database, you may want to ensure that only verified requests from trusted sources can invoke your function.

And, in some other cases, you may even want to limit how often the function is called over a set period of time to avoid denial-of-service-type attacks.

### Webhooks[​](#webhooks "Direct link to Webhooks") 

If your function receives an incoming Webhook from a third party, see [Webhooks](/docs/webhooks) in the RedwoodJS documentation to verify and trust its payload.

### Serverless Functions with Redwood User Authentication[​](#serverless-functions-with-redwood-user-authentication "Direct link to Serverless Functions with Redwood User Authentication") 

Serverless functions can use the same user-authentication strategy used by GraphQL Directives to [secure your services](/docs/graphql#secure-services) via the `useRequireAuth` wrapper.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6Ij48L3BhdGg+PC9zdmc+)]tip

If you need to protect an endpoint via authentication that isn\'t user-based, you should consider using [Webhooks](/docs/webhooks) with a signed payload and verifier.

#### How to Secure a Function with Redwood Auth[​](#how-to-secure-a-function-with-redwood-auth "Direct link to How to Secure a Function with Redwood Auth") 

The `useRequireAuth` wrapper configures your handler\'s `context` so that you can use any of the `requireAuth`-related authentication helpers in your serverless function:

-   import `useRequireAuth` from `@redwoodjs/graphql-server`
-   import your app\'s custom `getCurrentUser` and the `isAuthenticated` check from `src/lib/auth`
-   import your auth provider\'s `authDecoder`
-   implement your serverless function as you would, but do not `export` it (see `myHandler` below).
-   pass your implementation, `getCurrentUser` and `authDecoder` to the `useRequireAuth` wrapper and export its return
-   check if the user `isAuthenticated()` and, if not, handle the unauthenticated case by returning a `401` status code (for example)

``` 
import type  from 'aws-lambda'

import  from '@redwoodjs/auth-dbauth-api'
import  from '@redwoodjs/graphql-server'

import  from 'src/lib/auth'
import  from 'src/lib/logger'

const myHandler = async (event: APIGatewayEvent, context: Context) => ,
      body: JSON.stringify(),
    }
  } else 
  }
}

export const handler = useRequireAuth()
```

Now anywhere `context` is used, such as in services or when using `hasRole()` or `isAuthenticated()` from your `auth` lib, `currentUser` will be set and `requireAuth`-related functions will be able to verify the authentication state or if the user has the required roles.

In short, you can now use any of your auth functions like `isAuthenticated()`, `hasRole()`, or `requireAuth()` in your serverless function.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

If you intend to implement a feature that requires user authentication, then using GraphQL, auth directives, and services is the preferred approach.

#### Using your Authenticated Serverless Function[​](#using-your-authenticated-serverless-function "Direct link to Using your Authenticated Serverless Function") 

As there is no login flow when using functions, the `useRequireAuth` check assumes that your user is already authenticated and you have access to their JWT access token.

In your request, you must include the following headers:

-   the auth provider type that your application is using, e.g. `dbAuth`
-   the Bearer token (JWT access token)
-   if using dbAuth, then also the dbAuth Cookie

For example:

``` 
Authorization: Bearer myJWT.accesstoken.signature
auth-provider: supabase
Content-Type: application/json
```

### Other security considerations[​](#other-security-considerations "Direct link to Other security considerations") 

In addition to securing your serverless functions, you may consider logging, rate limiting and whitelisting as ways to protect your functions from abuse or misuse. Some of these benefits can be achieved with middleware like [middy](https://middy.js.org/), since our functions should be compatible with the lambda functions ecosystem.

#### Visibility via Logging[​](#visibility-via-logging "Direct link to Visibility via Logging") 

Logging in production --- and monitoring for suspicious activity, unknown IP addresses, errors, etc. --- can be a critical part of keeping your serverless functions and your application safe.

Third-party log services like [logFlare](https://logflare.app/), [Datadog](https://www.datadoghq.com/) and [LogDNA](https://www.logdna.com/) all have features that store logs for inspection, but also can trigger alerts and notifications if something you deem untoward occurs.

See [Logger](/docs/logger) in the RedwoodJS docs for more information about how to setup and use logging services.

#### Rate Limiting[​](#rate-limiting "Direct link to Rate Limiting") 

Rate limiting (or throttling) how often a function executes by a particular IP addresses or user account is a common way of stemming api abuse (for example, a distributed Denial-of-Service, or DDoS, attack).

As LogRocket [says](https://blog.logrocket.com/rate-limiting-node-js/):

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]info

Rate limiting is a very powerful feature for securing backend APIs from malicious attacks and for handling unwanted streams of requests from users. In general terms, it allows us to control the rate at which user requests are processed by our server.

API Gateways like [Kong](https://docs.konghq.com/hub/kong-inc/rate-limiting/) offer plugins to configure how many HTTP requests can be made in a given period of seconds, minutes, hours, days, months, or years.

Currently, RedwoodJS does not offer rate limiting in the framework, but your deployment target infrastructure may. This is a feature RedwoodJS will investigate for future releases.

For more information about Rate Limiting in Node.js, consider:

-   [Understanding and implementing rate limiting in Node.js](https://blog.logrocket.com/rate-limiting-node-js/) on LogRocket

#### IP Address Whitelisting[​](#ip-address-whitelisting "Direct link to IP Address Whitelisting") 

Because the `event` passed to the function handler contains the request\'s IP address, you could decide to whitelist only certain known and trusted IP addresses.

``` 
const ipAddress = () => 
```

If the IP address in the event does not match, then you can raise an error and return `401 Unauthorized` status.

## Returning Binary Data[​](#returning-binary-data "Direct link to Returning Binary Data") 

By default, RedwoodJS functions return strings or JSON. If you need to return binary data, your function will need to encode it as Base64 and then set the `isBase64Encoded` response parameter to `true`. Note that this is best suited to relatively small responses. The entire response body will be loaded into memory as a string, and many serverless hosting environments will limit your function to eg. 10 seconds, so if your file takes longer than that to process and download it may get cut off. For larger or static files, it may be better to upload files to an object store like S3 and generate a [pre-signed URL](https://stackoverflow.com/questions/38831829/nodejs-aws-sdk-s3-generate-presigned-url) that the client can use to download the file directly.

Here\'s an example of how to return a binary file from the filesystem:

api/src/functions/myCustomFunction.ts

``` 
import type  from 'aws-lambda'
import fs from 'fs'

export const handler = async (event: APIGatewayEvent, context: Context) => ,
    body: file.toString('base64'),
    isBase64Encoded: true,
  }
}
```

## How-To[​](#how-to "Direct link to How-To") 

We have prepared a simple [How-To](/docs/how-to/custom-function/) for you on how to setup a custom function to retrieve the server time, including consideration of CORS.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/serverless-functions.md)