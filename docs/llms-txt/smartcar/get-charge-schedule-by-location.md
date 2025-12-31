# Source: https://smartcar.com/docs/api-reference/ford/get-charge-schedule-by-location.md

# Charge Schedule by Location

> Returns all saved charging locations for a vehicle and their associated charging limits, schedules and configurations.

<Snippet file="api-reference/note-bse-ford.mdx" />

## Permission

`read_charge_locations`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/charge/schedule_by_location" \
  -H "Authorization: Bearer {token}" \
  -X "GET"
  ```

  ```python Python theme={null}
  chargeScheduleByLocation = vehicle.request(
          "GET", 
          "{make}/charge/schedule_by_location"
      )
  ```

  ```js Node theme={null}
  const chargeScheduleByLocation = await vehicle.request(
          "GET", 
          "{make}/charge/schedule_by_location"
      );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("GET")
        .path("{make}/charge/schedule_by_location")
        .build();
  VehicleResponse getChargeScheduleByLocation = vehicle.request(request)
  ```

  ```ruby Ruby theme={null}
  chargeScheduleByLocation = vehicle.request(
          "GET", 
          "{make}/charge/schedule_by_location"
      )
  ```
</RequestExample>

## Response

<ResponseField name="chargingLocations" type="[object] | [empty]">
  An array of charging locations. Empty if none are currently set on the vehicle.

  <Expandable>
    <ResponseField name="chargeLimit" type="number">
      The maximum charge limit for the vehicle at the location as a percent.
    </ResponseField>

    <ResponseField name="location" type="object">
      The latitude and longitude of the charging location.

      <Expandable title="location">
        <ResponseField name="longitude" type="number">
          The longitude of the charging location.
        </ResponseField>

        <ResponseField name="latitude" type="number">
          The latitude of the charging location.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="chargingSchedules" type="object">
      The weekday and weekend charging schedules for the vehicle at the location.

      <Expandable>
        <ResponseField name="weekday" type="[object] | [empty]">
          The charging schedule for the vehicle on weekdays (Monday - Friday).

          <Expandable>
            <ResponseField name="start" type="string">
              The exact hour a vehicle should start charging in HH:00 e.g. 17:00.
            </ResponseField>

            <ResponseField name="end" type="string">
              The exact hour a vehicle should stop charging in HH:00 e.g. 21:00.
            </ResponseField>
          </Expandable>
        </ResponseField>

        <ResponseField name="weekend" type="[object] | [empty]">
          The charging schedule for the vehicle on weekends (Saturday - Sunday).

          <Expandable>
            <ResponseField name="start" type="string">
              The exact hour a vehicle should start charging in HH:00 e.g. 17:00.
            </ResponseField>

            <ResponseField name="end" type="string">
              The exact hour a vehicle should stop charging in HH:00 e.g. 21:00.
            </ResponseField>
          </Expandable>
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
    "chargingLocations": [
      {
        "chargeLimit": 0.8,
        "chargingSchedules": {
          "weekday": [
            {
              "end": "17:00",
              "start": "09:00"
            }
          ],
          "weekend": [
            {
              "end": "17:00",
              "start": "09:00"
            }
          ]
        },
        "location": {
          "latitude": 48.8566,
          "longitude": 2.3522
        }
      }
    ]
  }
  ```
</ResponseExample>

## Example Schedule States

<AccordionGroup>
  <Accordion title="Vehicle will charge at any time">
    ```json  theme={null}
    {
      "chargingLocations": [
        {
          "chargeLimit": 0.8,
          "chargingSchedules": {
            "weekday": [],
            "weekend": []
          },
          "location": {
            "latitude": 48.8566,
            "longitude": 2.3522
          }
        }
      ]
    }
    ```
  </Accordion>

  <Accordion title="Vehicle has a schedule for Weekdays only">
    ```json  theme={null}
    {
      "chargingLocations": [
        {
          "chargeLimit": 0.8,
          "chargingSchedules": {
            "weekday": [
              {
                "end": "17:00",
                "start": "09:00"
              }
            ],
            "weekend": []
          },
          "location": {
            "latitude": 48.8566,
            "longitude": 2.3522
          }
        }
      ]
    }
    ```
  </Accordion>

  <Accordion title="Vehicle has a schedule for Weekends only">
    ```json  theme={null}
    {
        "chargingLocation" : {   
            "chargeLimit": 0.9, 
            "chargingSchedules": {
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
</AccordionGroup>
