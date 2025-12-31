# Source: https://smartcar.com/docs/api-reference/management/delete-vehicle-connections.md

# Vehicle Connections

> Deletes all vehicle connections associated with a Smartcar user ID or a specific vehicle.

## Request

**Header**

<ParamField header="Authorization" type="string" required>
  In the format `Basic base64(default:{application_management_token})`. You can find your `application_management_token` under
  your Application Configuration in the Smartcar Dashboard.
</ParamField>

**Query**

<ParamField query="user_id" type="string" />

<ParamField query="vehicle_id" type="string" />

You can delete connections in three ways:

* Provide a `vehicle_id` to remove all connections for that vehicle across all users.
* Provide a `user_id` to remove all vehicles linked to that user.
* Provide both a `vehicle_id` and `user_id` to remove only that vehicle for that specific user.

<RequestExample>
  ```bash cURL theme={null}
    curl -X DELETE "https://management.smartcar.com/v2.0/management/connections/?user_id=UUID12345&vehicle_id=UUID67890" \
    -H "Authorization: Basic $(echo -n "default:$SMARTCAR_APP_MANAGEMENT_TOKEN" | base64)"
  ```

  ```python Python theme={null}
    import os
    import base64
    import requests

    user_id = "UUID12345"
    vehicle_id = "UUID67890"
    token = os.getenv("SMARTCAR_APP_MANAGEMENT_TOKEN")

    auth_header = base64.b64encode(f"default:{token}".encode()).decode()
    headers = {
        "Authorization": f"Basic {auth_header}",
        "Content-Type": "application/json",
    }

    url = (
        "https://management.smartcar.com/v2.0/management/connections/"
        f"?user_id={user_id}&vehicle_id={vehicle_id}"
    )

    response = requests.delete(url, headers=headers)
  ```

  ```javascript Node theme={null}
    const basicAuth = Buffer.from(`default:${process.env.SMARTCAR_APP_MANAGEMENT_TOKEN}`).toString('base64');
    const disconnectResponse = await fetch(
    `https://management.smartcar.com/v2.0/management/connections/?user_id=${smartcar_user_id}&vehicle_id=${smartcar_vehicle_id}`,
    {
        method: 'DELETE',
        headers: {
          'Authorization': `Basic ${basicAuth}`,
          'Content-Type': 'application/json',
        },
      }
    );
  ```

  ```java Java theme={null}
    import java.net.HttpURLConnection;
    import java.net.URL;
    import java.util.Base64;

    String userId = "UUID12345";
    String vehicleId = "UUID67890";
    String token = System.getenv("SMARTCAR_APP_MANAGEMENT_TOKEN");
    String auth = Base64.getEncoder().encodeToString(("default:" + token).getBytes());

    URL url = new URL("https://management.smartcar.com/v2.0/management/connections/?user_id=" + userId + "&vehicle_id=" + vehicleId);
    HttpURLConnection conn = (HttpURLConnection) url.openConnection();
    conn.setRequestMethod("DELETE");
    conn.setRequestProperty("Authorization", "Basic " + auth);
    conn.setRequestProperty("Content-Type", "application/json");

    int responseCode = conn.getResponseCode();
  ```

  ```ruby Ruby theme={null}
    require 'net/http'
    require 'uri'
    require 'base64'

    user_id = "UUID12345"
    vehicle_id = "UUID67890"
    token = ENV['SMARTCAR_APP_MANAGEMENT_TOKEN']
    auth = Base64.strict_encode64("default:#{token}")
    uri = URI("https://management.smartcar.com/v2.0/management/connections/?user_id=#{user_id}&vehicle_id=#{vehicle_id}")
    request = Net::HTTP::Delete.new(uri)
    request['Authorization'] = "Basic #{auth}"
    request['Content-Type'] = 'application/json'
    response = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) do |http|
      http.request(request)
    end
    puts response.body
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={null}
  {
    "connections": [
      {
        "userId": "<string>",
        "vehicleId": "<string>"
      }
    ]
  }
  ```
</ResponseExample>

## Response

<ResponseField name="connections" type="array">
  An array of connections

  <Expandable title="connections">
    <ResponseField name="userId" type="string">
      ID of the user that authorized the deleted connection (UUID v4)
    </ResponseField>

    <ResponseField name="vehicleId" type="string">
      ID of the vehicle disconnected (UUID v4)
    </ResponseField>
  </Expandable>
</ResponseField>
