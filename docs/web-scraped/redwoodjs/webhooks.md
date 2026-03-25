# Source: https://docs.redwoodjs.com/docs/webhooks

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [Webhooks]

[Version: 8.8]

On this page

<div>

# Webhooks

</div>

If you\'ve used [IFTTT](https://ifttt.com/maker_webhooks), [Pipedream](https://pipedream.com/docs/api/rest/webhooks/), or [Zapier](https://zapier.com/apps/webhook/integrations) then you\'re familiar with how webhooks can give your app the power to create complex workflows, build one-to-one automation, and sync data between apps. RedwoodJS helps you work with webhooks by giving you the tools to both receive and verify incoming webhooks and sign outgoing ones with ease.

## What is a webhook[​](#what-is-a-webhook "Direct link to What is a webhook") 

Simply put, webhooks are a common way that third-party services notify your RedwoodJS application when an event of interest happens. They are a form of messaging and automation allowing distinct web applications to communicate with each other and send real-time data from one application to another whenever a given event occurs.

The third-party considers these \"outgoing Webhooks\" and therefore your application receives \"incoming Webhooks\".

When the api side of your Redwood app receives a webhook, it can parse it, process it, save it to replay later, or any other action needed.

Webhooks are different from other integration methods in that the third-party pushes new events to your app instead of your app constantly pulling or polling for new data.

### Examples of Webhooks[​](#examples-of-webhooks "Direct link to Examples of Webhooks") 

Some examples of outgoing Webhooks are:

-   Netlify successfully [deploys a site](https://docs.netlify.com/site-deploys/notifications/#outgoing-webhooks)
-   Someone [pushes a PR to GitHub](https://docs.github.com/en/developers/webhooks-and-events/creating-webhooks)
-   Someone [posts in Discourse](https://meta.discourse.org/t/setting-up-webhooks/49045)
-   Stripe [completes a purchase](https://stripe.com/docs/webhooks)
-   A cron/scheduled task wants to invoke a long running [background function on Netlify](https://docs.netlify.com/functions/background-functions/)
-   and more webhook integrations via services like [IFTTT](https://ifttt.com/maker_webhooks), [Pipedream](https://pipedream.com/docs/api/rest/webhooks/) and [Zapier](https://zapier.com/apps/webhook/integrations)

If you were to subscribe to one of these webhooks, you\'d point it to an endpoint in your RedwoodJS api \-- ie, a serverless function. But, because that function is out \"in the cloud\" you need to ensure that these run **only when they should**. That means your function must:

-   verify it comes from the place you expect
-   trust the party
-   know the payload sent in the hook hasn\'t been tampered with
-   ensure that the hook isn\'t reprocessed or replayed (sometimes)

That is, you need to **verify your incoming webhooks**.

## Verifying Webhooks with RedwoodJS Made Easy[​](#verifying-webhooks-with-redwoodjs-made-easy "Direct link to Verifying Webhooks with RedwoodJS Made Easy") 

The RedwoodJS [`api/webhooks` package](https://github.com/redwoodjs/redwood/blob/main/packages/api/src/webhooks/index.ts) makes it easy to receive and verify incoming webhooks by implementing many of the most commonly used Webhook signature verifiers.

### Webhook Verification[​](#webhook-verification "Direct link to Webhook Verification") 

Webhooks have a few ways of letting you know they should be trusted. The most common is by sending along a \"signature\" header. They typically sign their payload with a secret key (in a few ways) and expect you to validate the signature before processing it.

### Webhook Signature Verifiers[​](#webhook-signature-verifiers "Direct link to Webhook Signature Verifiers") 

Common signature verification methods are:

-   SHA256 ([GitHub](https://docs.github.com/en/developers/webhooks-and-events/securing-your-webhooks#validating-payloads-from-github) and [Discourse](https://meta.discourse.org/t/setting-up-webhooks/49045))
-   Base64 SHA256 ([Svix](https://docs.svix.com/receiving/verifying-payloads/how-manual) and [Clerk](https://docs.clerk.dev/reference/webhooks#verifying-requests))
-   SHA1 ([Vercel](https://vercel.com/docs/integrations?query=webhook%20sha1#webhooks/securing-webhooks))
-   JWT ([Netlify](https://docs.netlify.com/site-deploys/notifications/#outgoing-webhooks))
-   Timestamp Scheme ([Stripe](https://stripe.com/docs/webhooks/best-practices) / Redwood default)
-   Secret Key (Custom, [Orbit](https://docs.orbit.love/docs/webhooks))

RedwoodJS adds a way to do no verification as well of testing or in the case your third party doesn\'t sign the payload.

-   SkipVerifier (bypass verification, or no verification)

RedwoodJS implements [signatureVerifiers](https://github.com/redwoodjs/redwood/tree/main/packages/api/src/auth/verifiers) for each of these so you can get started integrating your app with third-parties right away.

``` 
export type SupportedVerifiers =
  | SkipVerifier
  | SecretKeyVerifier
  | Sha1Verifier
  | Sha256Verifier
  | Base64Sha1Verifier
  | Base64Sha256Verifier
  | TimestampSchemeVerifier
  | JwtVerifier
```

Each `SupportedVerifier` implements a method to `sign` and `verify` a payload with a secret (if needed).

When the webhook needs [creates a verifier](https://github.com/redwoodjs/redwood/blob/main/packages/api/src/auth/verifiers/index.ts#L12) in order to `verifyEvent`, `verifySignature` or `signPayload` it does so via:

``` 
createVerifier(type, options)
```

where type is one of the supported verifiers and `VerifyOptions` sets the options the verifier needs to sign or verify.

``` 
/**
 * VerifyOptions
 *
 * Used when verifying a signature based on the verifier's requirements
 *
 * @param  signatureHeader - Optional Header that contains the signature
 * to verify. Will default to DEFAULT_WEBHOOK_SIGNATURE_HEADER
 * @param  signatureTransformer - Optional
 * function that receives the signature from the headers and returns a new
 * signature to use in the Verifier
 * @param  currentTimestampOverride - Optional timestamp to use as the
 * "current" timestamp, in msec
 * @param  eventTimestamp - Optional timestamp to use as the event
 * timestamp, in msec. If this is provided the webhook verification will fail
 * if the eventTimestamp is too far from the current time (or the time passed
 * as the `currentTimestampOverride` option)
 * @param  tolerance - Optional tolerance in msec
 * @param  issuer - Options JWT issuer for JWTVerifier
 */
export interface VerifyOptions 
```

## How to Receive and Verify an Incoming Webhook[​](#how-to-receive-and-verify-an-incoming-webhook "Direct link to How to Receive and Verify an Incoming Webhook") 

The `api/webhooks` package exports [verifyEvent and verifySignature](https://github.com/redwoodjs/redwood/blob/main/packages/api/src/webhooks/index.ts) to apply [verification methods](https://github.com/redwoodjs/redwood/tree/main/packages/api/src/auth/verifiers) and verify the event or some portion of the event payload with a signature as defined in its [VerifyOptions](https://github.com/redwoodjs/redwood/blob/main/packages/api/src/webhooks/common.ts). If the signature fails verification, a `WebhookSignError` is raised which can be caught to return a `401` unauthorized.

Typically, for each integration you\'ll define 1) the events that triggers the webhook or the schedule via cron/conditions to send the webhook, 2) a secret, and 3) the endpoint to send the webhook to (ie, your endpoint).

When the third-party creates the outgoing webhook payload, they\'ll sign it (typically the event request body) and add that signature to the request headers with some key.

When your endpoint receives the request (incoming webhook), it can extract the signature using the signature header key set in `VerifyOptions`, transform it using the `signatureTransformer` function also defined in `VerifyOptions`, use the appropriate verifier, and validate the payload to ensure it comes from a trusted source.

Note that:

-   `verifyEvent` will detect if the event body is base64 encoded, then decode and validate the payload with the signature verifier
-   signatureHeader specified in `VerifyOptions` will be converted to lowercase when fetching the signature from the event headers

You can then use the payload data with confidence in your function.

### SHA256 Verifier (used by GitHub, Discourse)[​](#sha256-verifier-used-by-github-discourse "Direct link to SHA256 Verifier (used by GitHub, Discourse)") 

SHA256 HMAC is one of the most popular signatures. It\'s used by [Discourse](https://meta.discourse.org/t/setting-up-webhooks/49045) and [GitHub](https://docs.github.com/en/developers/webhooks-and-events/securing-your-webhooks#validating-payloads-from-github).

When your secret token is set, GitHub uses it to create a hash signature with each payload. This hash signature is included with the headers of each request as `X-Hub-Signature-256`.

For Discourse, when an event is triggered, it `POST`s a webhook with `X-Discourse-Event-Signature` in the HTTP header to your endpoint. It's computed by SHA256.

``` 
import type  from 'aws-lambda'
import  from '@redwoodjs/api/webhooks'

import  from 'src/lib/logger'

export const handler = async (event: APIGatewayEvent) => 
  const webhookLogger = logger.child()

  webhookLogger.trace('Invoked discourseWebhook function')

  try  as VerifyOptions

    verifyEvent('sha256Verifier', )

    webhookLogger.debug(, 'Headers')

    const payload = JSON.parse(event.body)

    webhookLogger.debug(, 'Body payload')

    // Safely use the validated webhook payload

    return ,
      statusCode: 200,
      body: JSON.stringify(),
    }
  } catch (error) 
    } else , error.message)

      return ,
        statusCode: 500,
        body: JSON.stringify(),
      }
    }
  }
}
```

### Base64 SHA256 Verifier (used by Svix, Clerk)[​](#base64-sha256-verifier-used-by-svix-clerk "Direct link to Base64 SHA256 Verifier (used by Svix, Clerk)") 

This is a variation on the SHA256 HMAC verification that works with binary buffers encoded with base64. It\'s used by [Svix](https://docs.svix.com/receiving/verifying-payloads/how-manual) and [Clerk](https://docs.clerk.dev/reference/webhooks#verifying-requests).

Svix (and by extension, Clerk) gives you a secret token that it uses to create a hash signature with each payload. This hash signature is included with the headers of each request as `svix-signature`.

> Some production environments, like Vercel, might base64 encode the request body string. In that case, the body must be conditionally parsed.
>
> ::: 
> ::: codeBlockContent_QJqH
> ``` 
> export const handler = async (event: APIGatewayEvent) => 
import type  from 'aws-lambda'
import  from '@redwoodjs/api/webhooks'

import  from 'src/lib/logger'

export const handler = async (event: APIGatewayEvent) => 
  const webhookLogger = logger.child()

  webhookLogger.trace('Invoked clerkWebhook function')

  try 
        }
      },
    }

    const svix_id = event.headers['svix-id']
    const svix_timestamp = event.headers['svix-timestamp']

    verifyEvent('base64Sha256Verifier', .$.$`,
      options,
    })

    webhookLogger.debug(, 'Headers')

    const payload = JSON.parse(event.body)

    webhookLogger.debug(, 'Body payload')

    // Safely use the validated webhook payload

    return ,
      statusCode: 200,
      body: JSON.stringify(),
    }
  } catch (error) 
    } else , error.message)

      return ,
        statusCode: 500,
        body: JSON.stringify(),
      }
    }
  }
}
```

### SHA1 Verifier (used by Vercel)[​](#sha1-verifier-used-by-vercel "Direct link to SHA1 Verifier (used by Vercel)") 

-   [Vercel](https://vercel.com/docs/integrations?query=webhook%20sha1#webhooks/securing-webhooks)

Vercel signs its webhooks with SHA also base64 encodes the event.

RedwoodJS `verifyEvent` will detect is the event is base64 encoded, decode and then validate the payload with the signature.

``` 
import type  from 'aws-lambda'
import  from '@redwoodjs/api/webhooks'

import  from 'src/lib/logger'

export const handler = async (event: APIGatewayEvent) => 
  const webhookLogger = logger.child()

  webhookLogger.trace('Invoked vercelWebhook function')

  try  as VerifyOptions

    verifyEvent('sha256Verifier', )

    webhookLogger.debug(, 'Headers')

    const payload = JSON.parse(event.body)

    webhookLogger.debug(, 'Body payload')

    // Safely use the validated webhook payload

    return ,
      statusCode: 200,
      body: JSON.stringify(),
    }
  } catch (error) 
    } else , error.message)

      return ,
        statusCode: 500,
        body: JSON.stringify(),
      }
    }
  }
}
```

### TimestampScheme Verifier (used by Stripe)[​](#timestampscheme-verifier-used-by-stripe "Direct link to TimestampScheme Verifier (used by Stripe)") 

The TimestampScheme verifier not only signs the payload with a secret (SHA256), but also includes a timestamp to prevent [replay attacks](https://en.wikipedia.org/wiki/Replay_attack) and a scheme (i.e., a version) to further protect webhooks.

A replay attack is when an attacker intercepts a valid payload and its signature, then re-transmits them. To mitigate such attacks, third-parties like Stripe includes a timestamp in the Stripe-Signature header. Because this timestamp is part of the signed payload, it is also verified by the signature, so an attacker cannot change the timestamp without invalidating the signature. If the signature is valid but the timestamp is too old, you can have your application reject the payload.

When verifying, there is a default tolerance of five minutes between the event timestamp and the current time but you can override this default by setting the [`tolerance` option](https://github.com/redwoodjs/redwood/blob/main/packages/api/src/auth/verifiers/timestampSchemeVerifier.ts) in the `VerifyOptions` passed to the verifier to another value (in milliseconds).

Also, if for some reason you need to adjust the timestamp used to compare the tolerance to a different time (say in the past), then you may override this by setting the [`currentTimestampOverride` option](https://github.com/redwoodjs/redwood/blob/main/packages/api/src/auth/verifiers/timestampSchemeVerifier.ts) in the `VerifyOptions` passed to the verifier.

-   [Stripe](https://stripe.com/docs/webhooks/best-practices)
-   Used in a Cron Job that triggers a Webhook periodically to background task via a serverless function

The TimestampScheme is particularly useful when used with cron jobs because if for some reason the webhook is delayed between when it is created and sent/received your app can discard it and thus old information would not risk overwriting newer data.

``` 
import type  from 'aws-lambda'

import  from '@redwoodjs/api/webhooks'
import  from 'src/lib/logger'
import  from 'src/lib/orbit/jobs/loadActivitiesJob'

/**
 * The handler function is your code that processes http request events.
 * You can use return and throw to send a response or error, respectively.
 *
 * @typedef  APIGatewayEvent
 * @typedef  Context
 * @param  event - an object which contains information from the invoker.
 * @param  context - contains information about the invocation,
 * function, and execution environment.
 */
export const handler = async (event: APIGatewayEvent) => 

  const webhookLogger = logger.child()

  webhookLogger.trace('>> in loadOrbitActivities-background')

  try  as VerifyOptions

    verifyEvent('timestampSchemeVerifier', )

    await perform()

    return ,
      statusCode: 200,
      body: JSON.stringify(`,
      }),
    }
  } catch (error) ,
        'Unauthorized'
      )
      return 
    } else ,
        error.message
      )
      return ,
        statusCode: 500,
        body: JSON.stringify(),
      }
    }
  }
}
```

### JWT Signature (used by Netlify)[​](#jwt-signature-used-by-netlify "Direct link to JWT Signature (used by Netlify)") 

-   [Netlify Outgoing Webhooks](https://docs.netlify.com/site-deploys/notifications/#outgoing-webhooks)

The JSON Web Token (JWT) Verifier not only cryptographically compares the signature to the payload to ensure it hasn\'t been tampered with, but also gives the added JWT claims like `issuer` and `expires` --- you can trust that the Webhook was sent by a trusted sounds and isn\'t out of date.

Here, the `VerifyOptions` not only specify the expected signature header, but allow will check that the `iss` claim is netlify.

``` 
    const options =  as VerifyOptions
```

See: [Introduction to JSON Web Tokens](https://jwt.io/introduction) for more information.

``` 
import type  from 'aws-lambda'
import  from '@redwoodjs/api/webhooks'

import  from 'src/lib/logger'

/**
 * The handler function is your code that processes http request events.
 * You can use return and throw to send a response or error, respectively.
 *
 * @typedef  APIGatewayEvent
 * @typedef  Context
 * @param  event - an object which contains information from the invoker.
 * @param  context - contains information about the invocation,
 * function, and execution environment.
 */
export const handler = async (event: APIGatewayEvent) => 
  const webhookLogger = logger.child()

  try  as VerifyOptions

    verifyEvent('jwtVerifier', )
    const payload = JSON.parse(event.body)

    // Safely use the validated webhook payload

    webhookLogger.debug(, 'Now I can do things with the payload')

    return ,
      statusCode: 200,
      body: JSON.stringify(),
    }
  } catch (error) 
    } else , error.message)
      return ,
        statusCode: 500,
        body: JSON.stringify(),
      }
    }
  }
}
```

### Secret Key Verifier (used by Orbit)[​](#secret-key-verifier-used-by-orbit "Direct link to Secret Key Verifier (used by Orbit)") 

-   [Orbit Webhook Doc](https://docs.orbit.love/docs/webhooks)

The Secret Key verifiers used by [Orbit](https://docs.orbit.love/docs/webhooks) acts very much like a password. It doesn\'t perform some cryptographic comparison of the signature with the payload received, but rather simple checks if the expected key or token is present.

``` 
//import type  from 'aws-lambda'
import  from '@redwoodjs/api/webhooks'

import  from 'deserialize-json-api'
import  from 'src/lib/orbit/loaders/activityLoader'

import  from 'src/lib/logger'

const webhookDetails = (event) => 
}

/**
 * The handler function is your code that processes http request events.
 * You can use return and throw to send a response or error, respectively.
 *
 * Important: When deployed, a custom serverless function is an open API endpoint and
 * is your responsibility to secure appropriately.
 *
 * @see 
 * in the RedwoodJS documentation for more information.
 *
 * @typedef  APIGatewayEvent
 * @typedef  Context
 * @param  event - an object which contains information from the invoker.
 * @param  context - contains information about the invocation,
 * function, and execution environment.
 */
export const handler = async (event) => )

  webhookLogger.info(`>> in webhook`)

  try 
    verifyEvent('secretKeyVerifier', )

    if (orbitInfo.orbitEventType === 'activity:created') ,
        statusCode: 200,
        body: JSON.stringify(),
      }
    } else `
      )
      return ,
        statusCode: 400,
        body: JSON.stringify(`,
        }),
      }
    }
  } catch (error) 
    } else , error.message)
      return ,
        statusCode: 500,
        body: JSON.stringify(),
      }
    }
  }
}
```

### Skip Verifier (used by Livestorm)[​](#skip-verifier-used-by-livestorm "Direct link to Skip Verifier (used by Livestorm)") 

[Livestorm](https://support.livestorm.co/article/119-webhooks) sends webhooks but doesn\'t sign them with a secret.

Here, you can use the `skipVerifier` \-- or choose not to validate altogether, but setting up to `verifyEvent` would let you quickly change the verification method if their changes.

You can also use the `skipVerifier` in testing or in `dev` so that you needn\'t share your secrets with other developers.

In that case, you might set `WEBHOOK_VERIFICATION=skipVerifier` and use the envar in `verifyEvent(process.env.WEBHOOK_VERIFICATION, )`.

``` 
import type  from 'aws-lambda'
import  from '@redwoodjs/api/webhooks'

import  from 'src/lib/logger'

/**
 * The handler function is your code that processes http request events.
 * You can use return and throw to send a response or error, respectively.
 *
 * @typedef  APIGatewayEvent
 * @typedef  Context
 * @param  event - an object which contains information from the invoker.
 * @param  context - contains information about the invocation,
 * function, and execution environment.
 */
export const handler = async (event: APIGatewayEvent) => 
  const webhookLogger = logger.child()

  webhookLogger.trace('Livestorm')

  webhookLogger.debug(, 'The Livestorm event')

  // Use the webhook payload
  // Note: since the payload is not signed, you may want to validate other header info

  try )

    const data = JSON.parse(event.body)

    webhookLogger.debug(, 'Data from Livestorm')

    return ,
      statusCode: 200,
      body: JSON.stringify(),
    }
  } catch (error) 
    } else , error.message)

      return ,
        statusCode: 500,
        body: JSON.stringify(),
      }
    }
  }
}
```

## Signing a Payload for an Outgoing Webhook[​](#signing-a-payload-for-an-outgoing-webhook "Direct link to Signing a Payload for an Outgoing Webhook") 

To sign a payload for an outgoing webhook, the `api/webhooks` package exports [signPayload](https://github.com/redwoodjs/redwood/blob/main/packages/api/src/webhooks/index.ts), a function that signs a payload using a [verification method](https://github.com/redwoodjs/redwood/tree/main/packages/api/src/auth/verifiers), creating your \"webhook signature\". Once you have the signature, you can add it to your request\'s http headers with a name of your choosing, and then post the request to the endpoint:

``` 
import got from 'got'
import  from '@redwoodjs/api/webhooks'

const YOUR_OUTGOING_WEBHOOK_DESTINATION_URL = 'https://example.com/receive'
const YOUR_WEBHOOK_SIGNATURE = process.env.WEBHOOK_SIGNATURE

export const sendOutGoingWebhooks = async () => )

  await got.post(YOUR_OUTGOING_WEBHOOK_DESTINATION_URL, ,
    headers: ,
  })
}
```

## How To Test Webhooks[​](#how-to-test-webhooks "Direct link to How To Test Webhooks") 

Because your webhook is typically sent from a third-party\'s system, manually testing webhooks can be difficult and time-consuming. See [How To Test Webhooks](/docs/serverless-functions#how-to-test-webhooks) to learn how to write tests that can automate tests and help you implement your webhook handler.

## More Information[​](#more-information "Direct link to More Information") 

Want to learn more about webhooks?

-   [Webhook.site lets you easily inspect, test and automate (with the visual Custom Actions builder, or WebhookScript) any incoming HTTP request or e-mail.](https://webhook.site/#!/)
-   [What is a Webhook](https://simonfredsted.com/1583) by Simon Fredsted
-   [About Webhooks](https://docs.github.com/en/developers/webhooks-and-events/about-webhooks) on GitHub
-   [What are Webhooks? A simple guide to connection apps with webhooks](https://zapier.com/blog/what-are-webhooks/) on Zapier
-   [What are Webhooks? Easy Explanation & Tutorial](https://snipcart.com/blog/what-are-webhooks-explained-example) on Snipcart
-   [What are Webhooks and Why You Can't Afford to Ignore Them](https://www.chargebee.com/blog/what-are-webhooks-explained/) on Charbee
-   [What is a webhook: How they work and how to set them up](https://www.getvero.com/resources/webhooks/) on Vero

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/webhooks.md)