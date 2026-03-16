# Source: https://docs.brightdata.com/api-reference/proxy-manager/refresh_ips_or_gips_in_zone.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Refresh IP/gIP in a zone

**API endpoint:** `POST` `/api/refresh_ips`

## `POST` body

<ParamField body="zone" type="string" required>
  Zone name
</ParamField>

<ParamField body="ips" type="array">
  Static IPs. e.g. `ips=["ip1","ip2"]`
</ParamField>

<ParamField body="vips" type="array">
  gIPs. e.g. `vips=["gip1","gip2"] [array]`
</ParamField>

<ResponseExample>
  ```json Sample Response theme={null}
  {
    "ips": [
  	{
  	  "ip":"10.0.0.1",
  	  "maxmind":"us"
  	},
  	{
  	  "ip":"20.0.0.1",
  	  "maxmind":"us"
  	}
    ]
  }
  ```
</ResponseExample>

<RequestExample>
  ```sh Shell theme={null}
  curl "http://127.0.0.1:22999/api/refresh_ips" -H "Content-Type: application/json" -d '{"zone":"ZONE","ips":["10.0.0.1"]}'
  ```

  ```js NodeJS theme={null}
  #!/usr/bin/env node

  require('request-promise')({
  method: 'POST',
  url: 'http://127.0.0.1:22999/api/refresh_ips',
  json: {'zone':'ZONE','ips':['10.0.0.1']}
  }).then(function(data){ console.log(data); },
  function(err){ console.error(err); });
  ```

  ```java Java theme={null}
  package example;

  import org.apache.http.HttpHost;
  import org.apache.http.client.fluent.*;

  public class Example {
    public static void main(String[] args) throws Exception {
     String body = "{\"zone\":\"ZONE\",\"ips\":[\"10.0.0.1\"]}";
      String res = Executor.newInstance()
       .execute(Request.Post("http://127.0.0.1:22999/api/refresh_ips")
       .bodyString(body, ContentType.APPLICATION_JSON))
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
        Method = HttpMethod.Post,
       RequestUri = new Uri("http://127.0.0.1:22999/api/refresh_ips"),
       Content = new StringContent(JsonConvert.SerializeObject(new {
         zone = "ZONE",
         ips = ["10.0.0.1"]
       }), Encoding.UTF8, "application/json"))
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

  data = {'zone':'ZONE','ips':['10.0.0.1']}

  r = requests.post('http://127.0.0.1:22999/api/refresh_ips', data=json.dumps(data))

  print(r.content)
  ```
</RequestExample>
