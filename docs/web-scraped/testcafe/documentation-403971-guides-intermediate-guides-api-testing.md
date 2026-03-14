# Source: https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing

Title: API Testing | Intermediate Guides | Guides

URL Source: https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing

Markdown Content:
TestCafe includes a comprehensive set of server-side API testing tools. You can add dedicated API tests to your test suite, or include API testing methods in existing functional tests.

The inclusion of API tests or checks significantly increases your test coverage, and allows you test your application’s server-side components right alongside its client side.

You can use the `t.request` method to do the following:

*   Send requests to your application’s web server to prepare the testing environment;
*   Send requests to your application’s web server to verify the success of post-test cleanup.

The `request` method requires access to the [TestController](https://testcafe.io/documentation/402665/reference/test-api/testcontroller) object. You cannot chain this method with other TestController methods.

[](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#how-api-testing-works)How API testing works[](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#how-api-testing-works)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

API tests send HTTP requests to the server and compare the server’s responses to the expected outcome.

Use the `request` method to [send HTTP requests](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#send-http-requests). Use assertions to [verify HTTP responses](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#observe-http-responses).

[](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#quick-guide)Quick Guide[](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#quick-guide)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1.   API tests do not need page access. You can omit the URL when you define the fixture.

```
fixture`request`;
```
2.   Declare a new test. Asynchronously call the `request` method from the test body. Save the results to an object.

```
const results = await t.request(`http://localhost:3000/api/data`);
```
3.   Use assertions to check the object’s properties.

```
await t
        .expect(results.status).eql(200)
        .expect(results.statusText).eql('OK')
        .expect(results.headers).contains({ 'content-type': 'application/json; charset=utf-8' })
        .expect(results.body.data).eql({
            name:     'John Hearts',
            position: 'CTO',
        });
```

[](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#send-http-requests)Send HTTP Requests[](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#send-http-requests)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The `request` method is asynchronous. To send a simple `GET` request, pass the target URL to the `request` method:

```
await t.request(`http://localhost:3000/api/data`);
```

If you want to specify multiple [request parameters](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#request-parameters), store them in an object:

```
await t.request({url: 'http://example.com', method: 'head'});
```

### [](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#request-parameters)Request Parameters[](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#request-parameters)

You can specify the following request parameters:

*   [The target URL](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#specify-the-url) - mandatory
*   [The HTTP method](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#specify-the-http-method)
*   [The request body](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#request-body)
*   [URL query parameters](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#url-query-parameters)
*   [Receive credentials?](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#receive-credentials)
*   [Basic HTTP authentication credentials](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#http-authentication)
*   [Request headers](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#request-headers)
*   [Request timeout](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#request-timeout)
*   [Proxy settings](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#proxy-settings)
*   [Response format](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#response-format)

### [](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#specify-the-url)Specify the URL[](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#specify-the-url)

Every HTTP request needs a target URL. The target URL can be either absolute or relative. If you specify a _relative_ URL, TestCafe calculates the absolute URL in relation to the current page.

There are two ways to specify the target URL.

*   You can pass the URL string directly to the `request` method:

```
await t.request(`http://localhost:3000/api/data`);
```
*   Alternatively, use the `url`[option](https://testcafe.io/documentation/403981/reference/test-api/testcontroller/request#options):

```
await t.request({
    url: 'http://localhost:3000/api/data'
});
```

If you define both, the first argument takes priority:

```
await t.request(`http://localhost:3000/api/1`, {url: 'http://localhost:3000/api/2'}); // sends a request to /api/1
```

### [](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#specify-the-http-method)Specify the HTTP Method[](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#specify-the-http-method)

Note

The `request` method does not support CORS.

Your requests can use any [standard HTTP protocol method](https://www.rfc-editor.org/rfc/rfc9110.html#name-methods). If you don’t specify the HTTP method, the `request` method sends a `GET` request.

You can specify the HTTP method with the `method` property:

```
await t.request({
    url: 'http://localhost:3000/api/data',
    method: 'head'
});
```

Alternatively, you can append [select HTTP methods](https://testcafe.io/documentation/403981/reference/test-api/testcontroller/request#methods) to the `request` method itself:

```
await t.request.head({
    url: 'http://localhost:3000/api/data'
});
```

### [](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#request-body)Request Body[](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#request-body)

Use the `body` option to specify request body.

```
await t.request.patch({
    url: 'http://localhost:3000/api/data', 
    body: {name: 'Jane Doe', position: 'CTO'}
});
```

### [](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#url-query-parameters)URL Query Parameters[](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#url-query-parameters)

Use the `params` option to specify URL query parameters. Make sure your parameters meet the requirements of the [URLSearchParams API](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams).

```
await t.request.patch({
    url: 'http://localhost:3000/api/data', 
    params: {
        uid: 503, 
        auth: true
    }
});
```

### [](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#receive-credentials)Receive Credentials[](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#receive-credentials)

The `withCredentials` option determines whether the response should include credentials such as cookies and authorization headers.

The default value of the `withCredentials` option is `false`. If you enable the `withCredentials` option, TestCafe _applies_ the credentials that it receives to the current page.

Do not enable the `withCredentials` option for same-origin requests.

```
await t.request({
    url: 'http://localhost:3000/api/data', 
    withCredentials: true
});
```

### [](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#http-authentication)HTTP Authentication[](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#http-authentication)

The `auth` option enables [Basic HTTP Authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Authentication). It accepts two arguments — the username and the password.

```
await t.request({
    url: 'http://localhost:3000/api/data', 
    auth: {
        username: 'admin', 
        password: '1234'
    }
});
```

The `headers` option specifies request headers.

```
await t.request({
    url: 'http://localhost:3000/api/data', 
    headers: {
        "Accept": "text/html"
    }
});
```

### [](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#request-timeout)Request Timeout[](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#request-timeout)

The `timeout` option specifies the timeout value in milliseconds. The method fails if the request does not resolve within the timeout window. The default `timeout` value is 25000 ms.

```
await t.request({
    url: 'http://localhost:3000/api/data', 
    timeout: 40000
});
```

### [](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#proxy-settings)Proxy Settings[](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#proxy-settings)

The `proxy` option specifies proxy settings.

```
await t.request({
    url: 'http://localhost:3000/api/data', 
    proxy: {
        protocol: 'http',    
        host: 'http://www.proxy.com',
        port: 3200,
        auth: {
            username: 'proxyUser22',
            password: '12345'
        };
    }
});
```

### [](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#response-format)Response Format[](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#response-format)

TestCafe **formats** the body of the response for easier parsing (see [Observe Response Body](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#response-body)). To receive **raw** response data, enable the `rawResponse` option:

```
await t.request({
    url: 'http://localhost:3000/api/data', 
    rawResponse: true
});
```

The default value of `rawResponse` is `false`.

[](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#observe-http-responses)Observe HTTP Responses[](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#observe-http-responses)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The `request` method returns an object with the following properties:

*   [status](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#response-status)
*   [statusText](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#response-status-text)
*   [headers](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#response-headers)
*   [body](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#response-body)

You can examine the HTTP response in one of two ways:

*   Execute the `request` method [inside an assertion](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#execute-a-request-inside-an-assertion);
*   [Save the return value](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#save-the-return-value) of the `request` method.

### [](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#execute-a-request-inside-an-assertion)Execute a request inside an assertion[](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#execute-a-request-inside-an-assertion)

If you pass the `t.request` method to an assertion, the method becomes subject to the [Smart Assertion Query Mechanism](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#smart-assertion-query-mechanism). If your request fails, TestCafe repeats it within the assertion timeout until the request succeeds.

```
await t.expect(t.request(`http://localhost:3000/helloworld`).body).contains('Hello World') // true

await t.expect(t.request.post({url: `http://localhost:3000/user`, timeout: 30000}).status).eql(200, 'ok posting', {timeout: 50000}) // true
```

### [](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#save-the-return-value)Save the return value[](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#save-the-return-value)

Alternatively, you can save the return value of the `request` method and use assertions later on in the test.

```
const response = await t.request(`http://localhost:3000/helloworld`);
console.log(response.body) // 'Hello World'
t.expect(response.body).contains('Hello World') // true
```

If you only need to examine a single property, you can append the name of the property to the request method:

```
const responseBody = await t.request(`http://localhost:3000/helloworld`).body;
console.log(responseBody) // 'Hello World'
t.expect(responseBody).contains('Hello World') // true
```

### [](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#response-status)Response Status[](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#response-status)

The `status` property contains the status code of the HTTP response.

```
const response= await t.request(`http://localhost:3000/helloworld`);
console.log(response.status) // '200'
```

### [](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#response-status-text)Response Status Text[](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#response-status-text)

The `statusText` property contains the status text of the HTTP response.

```
const response= await t.request(`http://localhost:3000/helloworld`);
console.log(response.statusText) // 'OK'
```

The `headers` property contains the headers of the HTTP response.

```
const response= await t.request(`http://localhost:3000/helloworld`);
console.log(response.headers) // "{'content-type': 'application/json; charset=utf-8'}"
```

### [](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#response-body)Response Body[](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#response-body)

The `responseBody` property contains the body of the response. TestCafe **formats** the property for easier parsing.

*   If the `content-type` of the response is `text/html` or `text/plain`, the response body is a `String`.
```
const responseBody = await t.request(`http://localhost:3000/helloworld`).body;
console.log(responseBody) // 'Hello World'
```
*   If the `content-type` of the response is `application/json`, the `responseBody` property is an `Object`.
```
const responseBody = await t.request(`http://localhost:3000/json/api`).body;
console.log(responseBody) // '{"message": "Hello World"}'
```
*   If the `content-type` of the response is neither `application/json` nor `text/plain`, the `responseBody` property becomes a `Buffer`.
```
const responseBody = await t.request(`http://localhost:3000/json/api`).body;
console.log(responseBody) // '<Buffer 61 62 63 ... >'
```

If you enable the [rawResponse option](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#response-format), TestCafe does not format the `responseBody` property.

[](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#limitations)Limitations[](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing#limitations)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   The `request` method does not support CORS. 
*   The `request` method is a server-side method. TestCafe executes it within a Node.JS environment. You cannot debug it in the browser’s **Network** tab.
