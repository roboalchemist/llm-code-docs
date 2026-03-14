# Source: https://docs.logrocket.com/reference/network.md

# Sanitize Network Data

Control how data is passed in network requests or responses

By default, the LogRocket React Native SDK captures all network requests made through [XMLHttpRequests](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest) and the [Javascript Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch).

## Sanitize a network request

#### `requestSanitizer` - Function

##### optional

Use requestSanitizer to scrub sensitive data from network requests or to ignore request/response pairs.

To ignore a request/response pair return `null` from the `requestSanitizer`. You can also redact fields on the `request` object by modifying the object. Make sure that you still return the modified request from the function:

```javascript Ignore network pair by url
// Add this to your existing init call, do not call init twice!
LogRocket.init(YOUR_APP_ID, {
  network: {
    requestSanitizer: request => {
      // if the url contains 'ignore'
      if (request.url.toLowerCase().indexOf('ignore') !== -1) {
        // ignore the request response pair
        return null;
      }
      
      // otherwise log the request normally
      return request;
    },
  },
});
```

```javascript Remove body from request
// Add this to your existing init call, do not call init twice!
LogRocket.init(YOUR_APP_ID, {
  network: {
    requestSanitizer: request => {
      // if the url contains 'ignore'
      if (request.url.toLowerCase().indexOf('ignore') !== -1) {
        // scrub out the body
        return {
          ...request,
          body: null,
        };
      }
        
      return request;
    },
  },
});
```

```javascript Remove header value from request
// Add this to your existing init call, do not call init twice!
LogRocket.init(YOUR_APP_ID, {
  network: {
    requestSanitizer: request => {
      return {
        ...request,
        headers: {
          ...request.headers,
          'x-auth-token': null,
        },
      };
    },
  },
});
```

```javascript Scrub header value from request
// Add this to your existing init call, do not call init twice!
LogRocket.init(YOUR_APP_ID, {
  network: {
    requestSanitizer: request => {
      return {
        ...request,
        headers: {
          ...request.headers,
          'x-auth-token': '',
        },
      };
    },
  },
});
```

## Sanitize a network response

#### `responseSanitizer` - Function

##### optional

Use the `responseSanitizer` to redact sensitive data from network response. Return `null` from the function to redact all response fields and only record timing data.

```javascript Remove body from responses
// Add this to your existing init call, do not call init twice!
LogRocket.init(YOUR_APP_ID, {
  network: {
    responseSanitizer: (response) => {
      if (response.body?.includes('<field to redact>')) {
        return {
          ...response,
          body: undefined,
        };
      }
      return response;
    },
  },
});
```

```javascript Remove all response data
// Add this to your existing init call, do not call init twice!
LogRocket.init(YOUR_APP_ID, {
  network: {
    responseSanitizer: response => {
      return null;
    },
  },
});
```

```javascript Remove Individual Field From Response Body Entirely
if (response.body.**field_to_delete**) {
  return {
    ...response,
    body: {
    	...response.body,
    **field_to_delete**: undefined,
    },
	};
}
```

```javascript Obfuscate Individual Response Field Value
if (response.body.**field_to_hide**) {
  return {
    ...response,
    body: {
    	...response.body,
    **field_to_hide**: '**redacted**',
    },
	};
}
return response
```

> 📘 logrocket-fuzzy-search-sanitizer
>
> Joshua Bailey, a LogRocket user, contributed a plugin for more easily sanitizing data from network requests and responses. Check it out here: [https://github.com/LogRocket/logrocket-fuzzy-search-sanitizer](https://github.com/LogRocket/logrocket-fuzzy-search-sanitizer)

## Disable recording of network data

#### `isEnabled` - Boolean

##### optional (default - *true*)

If you wish to disable all network data recording, you may set `isEnabled` to `false`.

```javascript Disable network logging
// Add this to your existing init call, do not call init twice!
LogRocket.init(YOUR_APP_ID, {
  network: {
    isEnabled: false,
  },
});
```

> 📘 Sanitizing headers and bodies to maintain timing and error data
>
> When possible, we recommend using the `requestSanitizer` and `responseSanitizer` to remove all headers and bodies, instead of `isEnabled: false`.  Sanitizing the headers and bodies specifically will allow LogRocket to still detect failed network requests, network errors, and slow network requests.