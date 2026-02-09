# Source: https://smartcar.com/docs/api-reference/management/get-vehicle-connections.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Vehicle Connections

> Returns a paged list of all vehicles that are connected to the application associated with the management API token used, sorted in descending order by connection date.

## Request

**Header**

<ParamField header="Authorization" type="string" required>
  In the format `Basic base64(default:{application_management_token})`. You can find your `application_management_token` under
  your Application Configuration in the Smartcar Dashboard.
</ParamField>

**Query**

<ParamField query="limit" default="10" type="integer">
  Number of connections to return per page. `Max: 100`
</ParamField>

<ParamField query="cursor" type="string">
  Used for accessing pages other than the first page. Each page returned has a cursor value
  that can be passed here to fetch the “next” page.
</ParamField>

<ParamField query="user_id" type="string">
  Filter for connections created by the provider user ID.
</ParamField>

<ParamField query="vehicle_id" type="string">
  Filter for connections to the provided vehicle ID.
</ParamField>

<ParamField query="mode" type="string">
  Filter for connections by either `live`, `simulated`, or the deprecated `test` mode.
</ParamField>

<RequestExample>
  ```bash cURL theme={null}
  curl -X GET "https://management.smartcar.com/v2.0/management/connections" \
    -H "Authorization: Basic $(echo -n "default:$SMARTCAR_APP_MANAGEMENT_TOKEN" | base64)" \
    -H "Content-Type: application/json"
  ```

  ```python Python theme={null}
  import os
  import base64
  import requests

  token = os.getenv("SMARTCAR_APP_MANAGEMENT_TOKEN")
  auth_header = base64.b64encode(f"default:{token}".encode()).decode()

  headers = {
      "Authorization": f"Basic {auth_header}",
      "Content-Type": "application/json"
  }

  response = requests.get(
      "https://management.smartcar.com/v2.0/management/connections",
      headers=headers
  )
  ```

  ```javascript Node theme={null}
  const basicAuth = Buffer.from(`default:${process.env.SMARTCAR_APP_MANAGEMENT_TOKEN}`).toString('base64');

  const response = await fetch(
      "https://management.smartcar.com/v2.0/management/connections",
      {
          method: 'GET',
          headers: {
              'Authorization': `Basic ${basicAuth}`,
              'Content-Type': 'application/json'
          }
      }
  );
  ```

  ```java Java theme={null}
  import java.net.HttpURLConnection;
  import java.net.URL;
  import java.util.Base64;

  String token = System.getenv("SMARTCAR_APP_MANAGEMENT_TOKEN");
  String auth = Base64.getEncoder().encodeToString(("default:" + token).getBytes());

  URL url = new URL("https://management.smartcar.com/v2.0/management/connections");
  HttpURLConnection conn = (HttpURLConnection) url.openConnection();
  conn.setRequestMethod("GET");
  conn.setRequestProperty("Authorization", "Basic " + auth);
  conn.setRequestProperty("Content-Type", "application/json");

  int responseCode = conn.getResponseCode();
  ```

  ```ruby Ruby theme={null}
  require 'net/http'
  require 'uri'
  require 'base64'

  token = ENV['SMARTCAR_APP_MANAGEMENT_TOKEN']
  auth = Base64.strict_encode64("default:#{token}")

  uri = URI("https://management.smartcar.com/v2.0/management/connections")
  request = Net::HTTP::Get.new(uri)
  request['Authorization'] = "Basic #{auth}"
  request['Content-Type'] = 'application/json'

  response = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) do |http|
    http.request(request)
  end
  ```
</RequestExample>

## Response

<ResponseField name="connections" type="array">
  An array of connections

  <Expandable title="connections">
    <ResponseField name="userId" type="string">
      ID of the user that authorized this connection (UUID v4).
    </ResponseField>

    <ResponseField name="vehicleId" type="string">
      ID of the vehicle connected (UUID v4).
    </ResponseField>

    <ResponseField name="connectedAt" type="string">
      Time at which the connection was created in UTC.
    </ResponseField>

    <ResponseField name="mode" type="string">
      Vehicle mode: live, simulated, or test (deprecated).
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="paging" type="Object">
  Metadata about the current query

  <Expandable>
    <ResponseField name="cursor" type="string">
      The cursor parameter that should be used to fetch the next page of results.
      This field will be null if there are no more pages.
    </ResponseField>
  </Expandable>
</ResponseField>
