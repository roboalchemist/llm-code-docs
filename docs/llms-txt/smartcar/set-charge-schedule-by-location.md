# Source: https://smartcar.com/docs/api-reference/ford/set-charge-schedule-by-location.md

# Charge Schedule by Location

> Set all schedules for the specified charging location.

<Snippet file="api-reference/note-bse-ford.mdx" />

## Permission

`control_charge`

## Request

<Info>
  In order to set a schedule, you must use a location from the [`GET Charge Schedule by Location`](/api-reference/ford/get-charge-schedule-by-location) endpoint.
  If the location you want to manage is not in the response, the vehicle owner has not charged at that location within the last 90 days and it has been
  removed from their app's saved charging location list.
</Info>

**Path**

<Snippet file="api-reference/path-bse.mdx" />

**Query**

<ParamField query="longitude" type="number" required>
  The longitude of a charging location from [`GET Charge Schedule by Location`](/api-reference/ford/get-charge-schedule-by-location)
</ParamField>

<ParamField query="latitude" type="number" required>
  The latitude of a charging location from [`GET Charge Schedule by Location`](/api-reference/ford/get-charge-schedule-by-location)
</ParamField>

**Body**

<ParamField body="chargingLocation" type="object" required>
  <Expandable defaultOpen="true" title="chargingLocation">
    <ParamField body="chargeLimit" type="number" required>
      The maximum charge limit for the vehicle at the location as a percent between `0.5` and `1`.
    </ParamField>

    <ParamField body="chargingWindows" type="object" required>
      The weekday and weekend charging schedules for the vehicle at the location.

      <Expandable defaultOpen="true">
        <ParamField body="weekday" type="[object]" required>
          The charging schedule for the vehicle on weekdays (Monday - Friday).

          <Expandable defaultOpen="true">
            <ParamField body="start" type="string" required>
              The exact hour a vehicle should start charging in HH:00 e.g. 17:00.
            </ParamField>

            <ParamField body="end" type="string" required>
              The exact hour a vehicle should stop charging in HH:00 e.g. 21:00.
            </ParamField>
          </Expandable>
        </ParamField>

        <ParamField body="weekend" type="[object]" required>
          The charging schedule for the vehicle on weekends (Saturday - Sunday).

          <Expandable defaultOpen="true">
            <ParamField body="start" type="string" required>
              The exact hour a vehicle should start charging in HH:00 e.g. 17:00.
            </ParamField>

            <ParamField body="end" type="string" required>
              The exact hour a vehicle should stop charging in HH:00 e.g. 21:00.
            </ParamField>
          </Expandable>
        </ParamField>
      </Expandable>
    </ParamField>
  </Expandable>
</ParamField>

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/charge/schedule_by_location?longitude=2.3522&latitude=48.8566" \
      -H "Authorization: Bearer {token}" \
      -X "PUT" \
      -H "Content-Type: application/json" \
      -d '{chargingLocation:{"chargeLimit": 0.9, "chargingWindows": {"weekday": [{"start": "09:00", "end": "17:00"}], "weekend": [{"start": "09:00", "end": "17:00"}]}}}'
  ```

  ```python Python theme={null}
  setChargeScheduleByLocation = vehicle.request(
          "PUT", 
          "{make}/charge/schedule_by_location?longitude=2.3522&latitude=48.8566", 
          {
            "chargingLocation" : {   
                "chargeLimit": 0.9, 
                "chargingWindows": {
                    "weekday": [
                        {   
                            "start": "09:00", 
                            "end": "10:00"
                        }
                    ], 
                    "weekend": [
                        {   
                            "start": "09:00", 
                            "end": "10:00"
                        }
                    ]
                }
            }
        }
      )
  ```

  ```js Node theme={null}
  const setChargeScheduleByLocation = vehicle.request(
        "PUT", 
        "{make}/charge/schedule_by_location?longitude=2.3522&latitude=48.8566", 
        {
          "chargingLocation" : {   
              "chargeLimit": 0.9, 
              "chargingWindows": {
                  "weekday": [
                      {   
                          "start": "09:00", 
                          "end": "10:00"
                      }
                  ], 
                  "weekend": [
                      {   
                          "start": "09:00", 
                          "end": "10:00"
                      }
                  ]
              }
          }
        }
      );
  ```

  ```java Java theme={null}
  JsonArrayBuilder weekday = Json.createArrayBuilder().add(
      Json.createObjectBuilder().add("start", "05:00").add("end", "07:00"));

  JsonArrayBuilder weekend = Json.createArrayBuilder().add(
      Json.createObjectBuilder().add("start", "06:00").add("end", "07:00"));

  JsonObject chargingWindows = Json.createObjectBuilder()
                                      .add("weekday", weekday)
                                      .add("weekend", weekend)
                                      .build();

  JsonObject chargingLocation = Json.createObjectBuilder()
                                      .add("chargeLimit", 1.0)
                                      .add("chargingWindows", chargingWindows)
                                      .build();

  SmartcarVehicleRequest request =
      new SmartcarVehicleRequest.Builder()
          .method("PUT")
          .path("ford/charge/schedule_by_location")
          .addQueryParameter("latitude", "37.749008")
          .addQueryParameter("longitude", "-122.46981")
          .addBodyParameter("chargingLocation", chargingLocation)
          .build();

  VehicleResponse chargeSched = vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  setChargeScheduleByLocation = vehicle.request(
        "PUT", 
        "{make}/charge/schedule_by_location?longitude=2.3522&latitude=48.8566", 
        {
          "chargingLocation" : {   
              "chargeLimit": 0.9, 
              "chargingWindows": {
                  "weekday": [
                      {   
                          "start": "09:00", 
                          "end": "10:00"
                      }
                  ], 
                  "weekend": [
                      {   
                          "start": "09:00", 
                          "end": "10:00"
                      }
                  ]
              }
          }
        }
      )
  ```
</RequestExample>

## Response

<ResponseField name="message" type="string">
  If the request is successful, Smartcar will return a message.
</ResponseField>

<ResponseField name="status" type="string">
  If the request is successful, Smartcar will return `success`.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
    "message": "Successfully sent request to vehicle",
    "status": "success"
  }
  ```
</ResponseExample>

## Example Request Bodies

<AccordionGroup>
  <Accordion title="Set a schedule for Weekdays and Weekends">
    ```json  theme={null}
    {
      "chargingLocation" : {   
          "chargeLimit": 0.9, 
          "chargingWindows": {
              "weekday": [
                  {   
                      "start": "17:00", 
                      "end": "06:00"
                  }
              ], 
              "weekend": [
                  {   
                      "start": "16:00", 
                      "end": "07:00"
                  }
              ]
          }
      }
    }
    ```
  </Accordion>

  <Accordion title="Set a schedule for only Weekdays">
    ```json  theme={null}
    {
      "chargingLocation" : {   
          "chargeLimit": 0.9, 
          "chargingWindows": {
              "weekday": [
                  {   
                      "start": "17:00", 
                      "end": "06:00"
                  }
              ], 
              "weekend": []
          }
      }
    }
    ```
  </Accordion>

  <Accordion title="Set a schedule for only Weekends">
    ```json  theme={null}
    {
        "chargingLocation" : {   
            "chargeLimit": 0.9, 
            "chargingWindows": {
                "weekday": [], 
                "weekend": [
                    {   
                        "start": "16:00", 
                        "end": "07:00"
                    }
                ]
            }
        }
    }
    ```
  </Accordion>

  <Accordion title="Clear schedules">
    ```json  theme={null}
    {
        "chargingLocation" : {   
            "chargeLimit": 0.9, 
            "chargingWindows": {
                "weekday": [], 
                "weekend": []
            }
        }
    }
    ```
  </Accordion>
</AccordionGroup>
