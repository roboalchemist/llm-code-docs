# Source: https://docs.wiremock.io/user-rate-limits.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wiremock.io/llms.txt
> Use this file to discover all available pages before exploring further.

# User Configurable Rate Limits

> Configuring your own rate limiters in order to simulate the real thing.

You can configure your own rate limiters and apply them to your stubs, allowing
you to simulate the real-world rate limiters protecting the APIs you're mocking.

## Add rate limits to a mock api

Rate limits are defined in your mock api settings page.

You can choose one of your rate limits to be the default rate limit for the mock API, which means it will apply to all stubs, unless a different rate limit is selected for a specific stub.

<img src="https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/rate-limit.png?fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=0462ef4f5f47a00dc93b4910be3e9a9e" title="Rate limit settings" width="80%" data-og-width="2136" data-og-height="798" data-path="images/screenshots/rate-limit.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/rate-limit.png?w=280&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=daca46b215b705eba7f1f35a1ebc31df 280w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/rate-limit.png?w=560&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=a0b442a3538f050e54cb25fd3c426569 560w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/rate-limit.png?w=840&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=199b6f7bb779b32063e6b4691dc4fd24 840w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/rate-limit.png?w=1100&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=92a34bf06033e62abc2b8e4d259e732d 1100w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/rate-limit.png?w=1650&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=f364423321f6a85f0b0a5e94422ea9f4 1650w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/rate-limit.png?w=2500&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=6db3243c1f7789d51a1d12a7a0c4b6cc 2500w" />

Once created rate limit names cannot be changed as then name is used as the unique identifier
when assigning to a stub.

If you would like to update the name please create a new rate limit
and attached to the new rate limit to your stub.

## Add rate limit to a stub

Rate limits can be applied to a stub in the "Response" section.

<img src="https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/rate-limit-stub.png?fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=ba8fc8f80260148083d43c386c20f6c0" title="Rate limit settings" width="80%" data-og-width="1312" data-og-height="382" data-path="images/screenshots/rate-limit-stub.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/rate-limit-stub.png?w=280&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=c05288dd04eb2f2b32921ff6de0d8690 280w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/rate-limit-stub.png?w=560&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=0fc3b7bf98d9d24a0c5fbf6b42e6cdb2 560w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/rate-limit-stub.png?w=840&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=05c33067e379f60ccfbfc05a805c179c 840w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/rate-limit-stub.png?w=1100&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=0a1339f2cf3bcdb451fd20cbf0f914de 1100w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/rate-limit-stub.png?w=1650&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=03d08e819895768353501a29dc1b0b71 1650w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/rate-limit-stub.png?w=2500&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=0c3baab5fd929140f1be6d89cc1f7b2f 2500w" />

Stubs will by default have either no rate limit, or the default rate limit selected at the API level.

Even if the API has a default rate limit, you can selected another of your previously created rate limits to allow for any individual stub to perform with a rate limit other than the default.

## Creating a rate limiter via API

A rate limiter is defined by an object in your mock API's settings document. The
JSON attribute key is then used to apply the rate limiter to specific stub mappings.

A rate limiter has two mandatory parameters:

* `unit` - the time unit the rate is being expressed in e.g. `nanoseconds`, `seconds`, `minutes`
* `rate` - the number of requests per the time unit permitted e.g. `15`

You can also optionally allow bursting by setting:

* `burst` - the number of requests that can be made in a burst over the set rate limit

You set the rate limit by making a `PUT` request to `https://<your mock API>.wiremockapi.cloud/__admin/ext/settings/extended/rateLimits`
containing the JSON object configuring all of your rate limits e.g.

```json  theme={null}
{
  "rateLimits": {
    "management": {
      "rate": 15,
      "unit": "seconds",
      "burst": 50
    },
    "authentication": {
      "rate": 100,
      "unit": "seconds"
    }
  }
}
```

If you've got admin API security turned on you'll need to supply your API key e.g.

```bash  theme={null}
curl -H 'Authorization:Token <your API token>' \
  https://<your mock API>.wiremockapi.cloud/__admin/ext/settings/extended/rateLimits \
  -X PUT -d '{
 "rateLimits": {
   "management": {
     "rate": 15,
     "unit": "seconds",
     "burst": 50
   },
   "authentication": {
     "rate": 100,
     "unit": "seconds"
   }
  }
}'
```

## Applying to your stubs

To rate limit a particular stub according to one of your named configurations you
need to create or edit the stub via the API, so that you can enable the `rate-limit`
transformer and set the name of the rate limit to be used.

You do this by `POST`ing the JSON to `https://<your mock API>.wiremockapi.cloud/__admin/mappings`.

Taking the above example, if I wanted to use the "authentication" rate limit in my
login handler stub, I'd do as follows:

```json  theme={null}
{
  "name": "Login handler",
  "request": {
    "urlPath": "/login",
    "method": "POST"
  },
  "response": {
    "status": 200,
    "body": "{ \"message\": \"Successfully logged in {{jsonPath request.body '$.username'}}\"",
    "transformers": [
      "response-template",
      "rate-limit"
    ],
    "transformerParameters": {
      "rateLimitName": "authentication"
    }
  },
  "persistent": true
}
```

The critical parts here are the `rate-limit` element in the `transformers` array,
and `"rateLimitName": "authentication"` under `transformerParameters`.

Once you've created a stub this way you will start to see 429 responses when the
request rate to **all stubs associated with the named rate limit** exceeds the limit.
