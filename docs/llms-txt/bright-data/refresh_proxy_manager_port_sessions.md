# Source: https://docs.brightdata.com/api-reference/proxy-manager/refresh_proxy_manager_port_sessions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Refresh Proxy Manager Port Session

**API endpoint:** `GET` `/api/refresh_sessions/{PORT}`

## Path Parameter

<ParamField path="PORT" type="string" required>
  Existing proxy port number
</ParamField>

<RequestExample>
  ```sh Shell theme={null}
  curl "http://127.0.0.1:22999/api/refresh_sessions/{PORT}"
  ```

  ```js NodeJS theme={null}
  #!/usr/bin/env node

  require('request-promise')({

  url: 'http://127.0.0.1:22999/api/refresh_sessions/{PORT}'

  }).then(function(data){ console.log(data); },

  function(err){ console.error(err); });
  ```

  ```java Java theme={null}
  package example;

   

  import org.apache.http.HttpHost;

  import org.apache.http.client.fluent.*;

   

  public class Example {

    public static void main(String[] args) throws Exception {

      String res = Executor.newInstance()

       .execute(Request.Get("http://127.0.0.1:22999/api/refresh_sessions/{PORT}"))

       .returnContent().asString();

      System.out.println(res)

    }

  }
  ```

  ```cs C# theme={null}
  using System;

  using System.Net;

  using System.Net.Http;

  using System.Net.Http.Headers;

   

  public class Program {

    public static async Task Main() {

      var client = new HttpClient();

      var requestMessage = new HttpRequestMessage {

        Method = HttpMethod.Get,

       RequestUri = new Uri("http://127.0.0.1:22999/api/refresh_sessions/{PORT}")

      };

      var response = await client.SendAsync(requestMessage);

      var responseString = await response.Content.ReadAsStringAsync();

      Console.WriteLine(responseString);

    }

  }
  ```

  ```python Python theme={null}
  #!/usr/bin/env python


  import requests



  r = requests.get('http://127.0.0.1:22999/api/refresh_sessions/{PORT}')

  print(r.content)
  ```
</RequestExample>
