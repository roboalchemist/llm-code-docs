# Source: https://docs.asapp.com/generativeagent/configuring/tasks-and-functions/keep-fields.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Keep Fields

> Learn how to keep fields from API responses so GenerativeAgent can use them for more calls

The history of responses in conversations is part of the data that GenerativeAgent continually uses as context to reply, analyze, and respond to your customers.

As GenerativeAgent makes constant calls to APIs via Functions, response history can grow. This can result in a lot of data in the conversation history and make it more difficult for GenerativeAgent to identify the most relevant fields or data to use in subsequent calls.

While you can control this by specifying the data to return within the underlying API Connection, you can also use a different set of fields for multiple Tasks using the same Function.

With the Keep Fields functionality, you can configure which fields to keep in the context for that Task.

<Warning>
  Most users will not need to configure Keep Fields and instead rely on specifying the fields to keep in the underlying [API Connection](/generativeagent/configuring/connect-apis).
</Warning>

## Configure a Keep Field

Keep Fields are part of the Function page.

To configure a Keep Field:

1. Identify the Function within a Task
   * Determine the function that you want to configure fields to keep.
2. Go to the Keep Field Configuration
   * In the Function settings, see the Keep Configuration table.
3. Specify Keep Fields
   * List all the fields that this function should retain. Use a nested list format to specify the paths of the fields you want to keep.

<Note>
  Each path should be an array of strings representing the keys to traverse in the JSON structure.
</Note>

Inside of the Function options, you can add Keep Fields.

### Specify fields within objects

JSON responses on API Connections often contain arrays of objects.

To specify fields within these objects, you need to indicate that you are traversing an array.

Use the `[]` notation to denote array elements in the path when specifying which fields to keep.

This is necessary because JSON structures can include arrays, and you need to indicate that you are referring to elements within those arrays.

## Example Keep Field Configuration

See this example of a configuration to keep all fields except for `scheduledDepartureTime` under `origin` within `segments` of `originalSlice`:

```json  theme={null}
[
    ["response", "flightChanged"],
    ["response", "flightChangeReason"],
    ["response", "flownStatus"],
    ["response", "flightStatus"],
    ["response", "isReaccommodated"],
    ["response", "eligibleToRebook"],
    ["response", "originalSlice", "available"],
    ["response", "originalSlice", "origin"],
    ["response", "originalSlice", "destination"],
    ["response", "originalSlice", "importantInformation"],
    ["response", "originalSlice", "segments", "[]", "flightNumber"],
    ["response", "originalSlice", "segments", "[]", "status"],
    ["response", "originalSlice", "segments", "[]", "bookingCode"],
    ["response", "originalSlice", "segments", "[]", "impacted"],
    ["response", "originalSlice", "segments", "[]", "numberOfLegs"],
    ["response", "originalSlice", "segments", "[]", "origin", "estimatedDepartureDate"],
    ["response", "originalSlice", "segments", "[]", "origin", "estimatedDepartureTime"],
    ["response", "originalSlice", "segments", "[]", "origin", "scheduledDepartureDate"],
    ["response", "originalSlice", "segments", "[]", "origin", "airportCode"],
    ["response", "originalSlice", "segments", "[]", "origin", "airportCity"],
    ["response", "originalSlice", "segments", "[]", "destination", "estimatedArrivalDate"],
    ["response", "originalSlice", "segments", "[]", "destination", "estimatedArrivalTime"],
    ["response", "originalSlice", "segments", "[]", "destination", "scheduledArrivalDate"],
    ["response", "originalSlice", "segments", "[]", "destination", "scheduledArrivalTime"],
    ["response", "originalSlice", "segments", "[]", "destination", "airportCode"],
    ["response", "originalSlice", "segments", "[]", "destination", "airportCity"],
    ["response", "rebookedSlice", "available"],
    ["response", "rebookedSlice", "origin", "estimatedDepartureDate"],
    ["response", "rebookedSlice", "origin", "estimatedDepartureTime"],
    ["response", "rebookedSlice", "origin", "scheduledDepartureDate"],
    ["response", "rebookedSlice", "origin", "scheduledDepartureTime"],
    ["response", "rebookedSlice", "origin", "airportCode"],
    ["response", "rebookedSlice", "origin", "airportCity"],
    ["response", "rebookedSlice", "destination", "estimatedDepartureDate"],
    ["response", "rebookedSlice", "destination", "estimatedDepartureTime"],
    ["response", "rebookedSlice", "destination", "scheduledDepartureDate"],
    ["response", "rebookedSlice", "destination", "scheduledDepartureTime"],
    ["response", "rebookedSlice", "destination", "airportCode"],
    ["response", "rebookedSlice", "destination", "airportCity"],
    ["response", "rebookedSlice", "importantInformation", "[]", "alert"],
    ["response", "rebookedSlice", "importantInformation", "[]", "value"],
    ["response", "rebookedSlice", "importantInformation", "[]", "alertPriority"],
    ["response", "rebookedSlice", "segments", "[]", "flightNumber"],
    ["response", "rebookedSlice", "segments", "[]", "status"],
    ["response", "rebookedSlice", "segments", "[]", "bookingCode"],
    ["response", "rebookedSlice", "segments", "[]", "impacted"],
    ["response", "rebookedSlice", "segments", "[]", "numberOfLegs"],
    ["response", "rebookedSlice", "segments", "[]", "origin", "estimatedDepartureDate"],
    ["response", "rebookedSlice", "segments", "[]", "origin", "estimatedDepartureTime"],
    ["response", "rebookedSlice", "segments", "[]", "origin", "scheduledDepartureDate"],
    ["response", "rebookedSlice", "segments", "[]", "origin", "airportCode"],
    ["response", "rebookedSlice", "segments", "[]", "origin", "airportCity"],
    ["response", "rebookedSlice", "segments", "[]", "destination", "estimatedArrivalDate"],
    ["response", "rebookedSlice", "segments", "[]", "destination", "estimatedArrivalTime"],
    ["response", "rebookedSlice", "segments", "[]", "destination", "scheduledArrivalDate"],
    ["response", "rebookedSlice", "segments", "[]", "destination", "scheduledArrivalTime"],
    ["response", "rebookedSlice", "segments", "[]", "destination", "airportCode"],
    ["response", "rebookedSlice", "segments", "[]", "destination", "airportCity"]
]

```
