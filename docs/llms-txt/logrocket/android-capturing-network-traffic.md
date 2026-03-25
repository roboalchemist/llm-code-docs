# Source: https://docs.logrocket.com/reference/android-capturing-network-traffic.md

# Capture and Sanitize Network Data (Android)

Capture and Sanitize Network Requests

The LogRocket Android SDK does not automatically capture Network Requests in your application. A fluent builder interface is provided by the SDK to simplify capturing network requests, and we have provided a sample OkHttp interceptor for capturing requests from the OkHttp library.

## Request Builder API

Call on `SDK.newRequestBuilder()` to create an instance of a request builder. Populate the builder with the network request data. Then call on `.capture()` to record the request event and return an instance of the corresponding response builder.

```java Java
IResponseBuilder responseBuilder = SDK.newRequestBuilder()
                                      .setUrl("https://logrocket.com/")
                                      .capture();
```

#### `setUrl(String url)`

URL of the network request

#### `setBody(String body)`

Body of the network request. Limit set to 4 MB

#### `setMethod(String method)`

Method of the network request. Must be one of the following: GET, HEAD, POST, PUT, DELETE, CONNECT, OPTIONS, TRACE, PATCH

#### `setHeaders(Map<String, String> headers)`

Map of header key-value pairs of the network request

#### `putHeader(String name, String value)`

A single header key-value pair of the network request

## Response Builder API

Once the request has been captured, populate the response builder with the network response data and then call on `.capture()` to record the response event.

#### `setStatusCode(int statusCode)`

Status code of the network response

#### `setDuration(double duration)`

Time between network request and response

#### `setBody(String body)`

Body of the network response. Limit set to 4 MB

#### `setHeaders(Map<String, String> headers)`

Map of header key-value pairs of the network response

#### `putHeader(String name, String value)`

A single header key-value pair of the network response

## Capturing Failed Network Responses

Even when a network request has failed, make sure to capture a response to avoid a never ending request. Set the status code to 0 and set the duration before capturing.

```java
responseBuilder
      .setStatusCode(0)
      .setDuration(endTime - startTime)
      .capture();
```

## Example

```java java.net.HttpURLConnection Example
import com.logrocket.core.SDK;
import com.logrocket.core.network.IResponseBuilder;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;

public class HttpURLConnectionExample {

  private void sendGetRequest() throws IOException {
    URL endpoint = new URL("https://example.com/");

    IResponseBuilder responseBuilder =
        SDK.newRequestBuilder()
            .setUrl(endpoint.toString())
            .setMethod("GET")
            .capture();
    long startTime = System.currentTimeMillis();

    try {
      HttpURLConnection conn = (HttpURLConnection) endpoint.openConnection();

      responseBuilder
          .setStatusCode(conn.getResponseCode())
          .setDuration(System.currentTimeMillis() - startTime)
          // The body field on both the Request and Response builders must be a String.
          // Content must be sanitized before registering to the response builder.
          .setBody(readRedactedResponseBody(conn))
          // Redact sensitive fields before adding to the response builder. The HttpURLConnection
          // provides an array of values for each key, but we only accept a single value.
          .setHeaders(flattenAndRedactHeaders(conn.getHeaderFields()))
          .capture();

      // Work with your response!
    } catch (IOException err) {
      // Network failures are represented as Responses with a status code of 0. If a captured
      // request does not have a matching response captured it will appear as an unending request
      // during session playback.

      responseBuilder
          .setStatusCode(0)
          .setDuration(System.currentTimeMillis() - startTime)
          .capture();

      // Re-surface the actual IOException
      throw err;
    }
  }

  private String readRedactedResponseBody(HttpURLConnection conn) throws IOException {
    if (conn.getResponseCode() == HttpURLConnection.HTTP_OK) {
      BufferedReader in = new BufferedReader(new InputStreamReader(conn.getInputStream()));
      String inputLine;
      StringBuilder response = new StringBuilder();

      while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
      }
      in.close();

      return redactBody(response.toString());
    }

    return "";
  }

  private String redactBody(String body) {
    if (body.contains("ignore")) {
      return "";
    }
    return body;
  }

  private Map<String, String> flattenAndRedactHeaders(Map<String,List<String>> headers) {
    Map<String, String> result = new HashMap<>();

    for (Entry<String, List<String>> entry : headers.entrySet()) {
      String key = entry.getKey();

      // Do not capture auth related headers.
      if (key.toLowerCase().equals("authentication") || key.toLowerCase().equals("authorization")) {
        continue;
      }

      List<String> values = entry.getValue();
      result.put(key, joinValues(values));
    }

    return result;
  }

  private String joinValues(List<String> values) {
    StringBuilder sb = new StringBuilder();

    for (int i = 0; i < values.size(); i++) {
      sb.append(values.get(i));
      if (i != values.size() - 1) {
        sb.append(",");
      }
    }

    return sb.toString();
  }
}
```

```java OKHttp Interceptor
import android.util.Log;
import com.logrocket.core.SDK;
import com.logrocket.core.network.IResponseBuilder;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Objects;
import okhttp3.Headers;
import okhttp3.Interceptor;
import okhttp3.Protocol;
import okhttp3.Request;
import okhttp3.Response;
import okio.Buffer;
import okio.BufferedSource;

/**
 * This example interceptor was built against OkHttp3 v4.9.0.
 *
 * @link https://square.github.io/okhttp/interceptors/
 */
public class NetworkInterceptor implements Interceptor {
  @Override
  public Response intercept(Chain chain) throws IOException {
    Request request = chain.request();
    IResponseBuilder responseBuilder = this.captureRequest(request);

    try {
      Response response = chain.proceed(request);

      this.captureResponse(responseBuilder, response);

      return response;
    } catch (IOException e) {
      // Network failures are represented as Responses with a status code of 0. If a captured
      // request does not have a matching response captured it will appear as an unending request
      // during session playback.

      this.captureResponse(
          responseBuilder,
          new Response.Builder()
              .request(chain.request())
              .message("Failed request")
              .protocol(Protocol.HTTP_2)
              .code(0)
              .build());

      throw e;
    }
  }

  private IResponseBuilder captureRequest(Request request) {
    String body = "";

    if (request.body() != null) {
      Request copy = request.newBuilder().build();
      Buffer buffer = new Buffer();

      try {
        Objects.requireNonNull(copy.body()).writeTo(buffer);
        body = buffer.readUtf8();
      } catch (Throwable th) {
        Log.e("LogRocket-Interceptor", "Failed to read request body", th);
      }
    }

    return SDK.newRequestBuilder()
        .setUrl(request.url().toString())
        .setMethod(request.method())
        .setHeaders(collectHeaders(request.headers()))
        .setBody(body)
        .capture();
  }

  private void captureResponse(IResponseBuilder builder, Response response) {
    String body = "";

    if (response.body() != null) {
      try {
        BufferedSource source = Objects.requireNonNull(response.body()).source();
        source.request(Long.MAX_VALUE);
        Buffer buffer = source.getBuffer();
        body = buffer.clone().readString(StandardCharsets.UTF_8);
      } catch (Throwable th) {
        Log.e("LogRocket-Interceptor", "Failed to read response body", th);
      }
    }

    builder
        .setStatusCode(response.code())
        .setDuration(response.receivedResponseAtMillis() - response.sentRequestAtMillis())
        .setHeaders(collectHeaders(response.headers()))
        .setBody(body)
        .capture();
  }

  private static Map<String, String> collectHeaders(Headers headers) {
    Map<String, String> headersMap = new HashMap<>();

    for (Entry<String, List<String>> entry : headers.toMultimap().entrySet()) {
      String key = entry.getKey();

      // Do not capture auth related headers.
      if (key.toLowerCase().equals("authentication") || key.toLowerCase().equals("authorization")) {
        continue;
      }

      List<String> values = entry.getValue();
      headersMap.put(key, joinValues(values));
    }

    return headersMap;
  }

  private static String joinValues(List<String> values) {
    StringBuilder sb = new StringBuilder();

    for (int i = 0; i < values.size(); i++) {
      sb.append(values.get(i));
      if (i != values.size() - 1) {
        sb.append(",");
      }
    }

    return sb.toString();
  }
}
```