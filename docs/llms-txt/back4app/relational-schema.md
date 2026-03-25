# Source: https://docs-containers.back4app.com/docs/get-started/relational-schema.md

---
title: Relational Schema
slug: docs/get-started/relational-schema
description: In this guide you will save relational data and perform relational queries on Back4App using the Parse SDKs
image: https://www.back4app.com/_public/img/back4app-og.png
createdAt: 2024-01-24T13:29:02.752Z
updatedAt: 2025-01-27T19:41:48.197Z
---

This guide explains how to work with relational schemas on Back4app, including creating related classes and performing efficient queries using Parse Server. You will learn how to use `Pointers` and `Relations` effectively, along with practical examples.

## **What is a Relational Schema?**

A relational schema organizes data into different classes connected to each other. In Parse Server, these relationships are managed through:

- **Pointers**: Refer directly to a single object.
- **Relations**: Manage multiple connections (many-to-many relationships).

These tools allow you to perform complex queries efficiently and consistently.

## Goals

By the end of this guide, you will be able to:

- Create relationships between classes using *Pointers* and *Relations*.
- Perform relational queries to retrieve connected data.
- Optimize your schema for better performance.

## Prerequisites

:::hint{type="info"}
- A Back4app application. [**Create an App Guide**](https://www.back4app.com/docs/get-started/new-parse-app).
- Parse SDK installed. [**Installation Guide**](https://www.back4app.com/docs/get-started/parse-sdk).
:::

## 1 - Creating Related Classes

### **Practical Example**: States and Cities

Imagine you want to model a system where cities are associated with states:

- Class State with the field state\_name.
- Class City with the field city\_name and a *Pointer* to State.

### **Creating Classes and Relationships**

:::CodeblockTabs
JavaScript

```javascript
async function createStateAndCity() {
  try {
    // Create a State
    const State = Parse.Object.extend('State');
    const california = new State();
    california.set('state_name', 'California');
    const savedState = await california.save();

    console.log(`State created with objectId: ${savedState.id}`);

    // Create a City with a pointer to State
    const City = Parse.Object.extend('City');
    const losAngeles = new City();
    losAngeles.set('city_name', 'Los Angeles');
    losAngeles.set('state', savedState);

    const savedCity = await losAngeles.save();
    console.log(`City created with objectId: ${savedCity.id}`);
  } catch (error) {
    console.error('Error creating state and city:', error.message);
  }
}

createStateAndCity();
```

Flutter

```dart
Future<void> createClasses() async {
  await Parse().initialize('YOUR_APP_ID', 'https://parseapi.back4app.com/',
      clientKey: 'YOUR_CLIENT_KEY', autoSendSessionId: true);

  // Create a State
  final state = ParseObject('State')
    ..set('state_name', 'California');
  final stateResult = await state.save();

  if (stateResult.success) {
    // Create a City with a pointer to State
    final city = ParseObject('City')
      ..set('city_name', 'Los Angeles')
      ..set('state', state);
    final cityResult = await city.save();

    if (cityResult.success) {
      print('State and City created successfully.');
    }
  }
}
```

Android

```java
public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Initialize Parse
        Parse.initialize(new Parse.Configuration.Builder(this)
                .applicationId("YOUR_APP_ID")
                .clientKey("YOUR_CLIENT_KEY")
                .server("https://parseapi.back4app.com/")
                .build()
        );

        // Create State and City
        createClasses();
    }

    private void createClasses() {
        // Create a State
        ParseObject state = new ParseObject("State");
        state.put("state_name", "California");

        state.saveInBackground(e -> {
            if (e == null) {
                Log.d("Parse", "State created successfully with objectId: " + state.getObjectId());

                // Save City with a pointer to State
                ParseObject city = new ParseObject("City");
                city.put("city_name", "Los Angeles");
                city.put("state", state);

                city.saveInBackground(ex -> {
                    if (ex == null) {
                        Log.d("Parse", "City created successfully with objectId: " + city.getObjectId());
                    } else {
                        Log.e("Parse", "Failed to create City: " + ex.getMessage());
                    }
                });
            } else {
                Log.e("Parse", "Failed to create State: " + e.getMessage());
            }
        });
    }
}
```

iOS

```swift
struct State: ParseObject {
    var objectId: String?
    var state_name: String?
    var createdAt: Date?
    var updatedAt: Date?
}

struct City: ParseObject {
    var objectId: String?
    var city_name: String?
    var state: State?
    var createdAt: Date?
    var updatedAt: Date?
}

func createClasses() async throws {
    try await ParseSwift.initialize(applicationId: "YOUR_APP_ID",
                                    clientKey: "YOUR_CLIENT_KEY",
                                    serverURL: URL(string: "https://parseapi.back4app.com")!)

    let state = State(state_name: "California")
    let savedState = try await state.save()

    var city = City(city_name: "Los Angeles", state: savedState)
    city = try await city.save()

    print("State and City created successfully.")
}
```

PHP

```php
require 'vendor/autoload.php';

use Parse\ParseClient;
use Parse\ParseObject;

ParseClient::initialize('YOUR_APP_ID', 'YOUR_CLIENT_KEY', 'https://parseapi.back4app.com/');

try {
    // Create a State
    $state = new ParseObject("State");
    $state->set("state_name", "California");
    $state->save();

    // Create a City with a pointer to State
    $city = new ParseObject("City");
    $city->set("city_name", "Los Angeles");
    $city->set("state", $state);
    $city->save();

    echo "State and City created successfully.";
} catch (Exception $ex) {
    echo "Error: " . $ex->getMessage();
}
```

.NET

```csharp
namespace ParseExampleApp
{
    class Program
    {
        static async Task Main(string[] args)
        {
            // Initialize Parse
            ParseClient.Initialize(new ParseClient.Configuration
            {
                ApplicationId = "YOUR_APP_ID",
                Server = "https://parseapi.back4app.com/",
                Key = "YOUR_CLIENT_KEY"
            });

            // Call the method to create State and City
            await CreateClassesAsync();
        }

        static async Task CreateClassesAsync()
        {
            try
            {
                // Create a State
                var state = new ParseObject("State");
                state["state_name"] = "California";
                await state.SaveAsync();
                Console.WriteLine($"State created with objectId: {state.ObjectId}");

                // Create a City with a Pointer to the State
                var city = new ParseObject("City");
                city["city_name"] = "Los Angeles";
                city["state"] = state; // Set the pointer to the State
                await city.SaveAsync();
                Console.WriteLine($"City created with objectId: {city.ObjectId}");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }
        }
    }
}
```

REST API

```curl
# Create State
curl -X POST \
-H "X-Parse-Application-Id: YOUR_APP_ID" \
-H "X-Parse-REST-API-Key: YOUR_REST_API_KEY" \
-H "Content-Type: application/json" \
-d '{"state_name": "California"}' \
https://parseapi.back4app.com/classes/State

# Use the objectId of the created state to create a city
curl -X POST \
-H "X-Parse-Application-Id: YOUR_APP_ID" \
-H "X-Parse-REST-API-Key: YOUR_REST_API_KEY" \
-H "Content-Type: application/json" \
-d '{"city_name": "Los Angeles", "state": {"__type": "Pointer", "className": "State", "objectId": "STATE_OBJECT_ID"}}' \
https://parseapi.back4app.com/classes/City
```
:::

## **2 - Querying Related Data**

Now that the data is related, you can perform queries to retrieve it.

### **Example 1**: Fetch Cities in a Specific State

:::CodeblockTabs
JavaScript

```javascript
const stateQuery = new Parse.Query("State");
stateQuery.equalTo("state_name", "California");

stateQuery.first().then(state => {
  const cityQuery = new Parse.Query("City");
  cityQuery.equalTo("state", state);
  return cityQuery.find();
}).then(cities => {
  cities.forEach(city => {
    console.log(`City: ${city.get("city_name")}`);
  });
}).catch(error => {
  console.error("Error fetching cities:", error.message);
});
```

Flutter

```dart
final stateQuery = QueryBuilder(ParseObject('State'))..whereEqualTo('state_name', 'California');

final stateResult = await stateQuery.query();
if (stateResult.success && stateResult.results != null) {
  final state = stateResult.results!.first;
  final cityQuery = QueryBuilder(ParseObject('City'))..whereEqualTo('state', state);
  final cityResult = await cityQuery.query();

  if (cityResult.success && cityResult.results != null) {
    for (var city in cityResult.results!) {
      print('City: ${city.get<String>('city_name')}');
    }
  }
}
```

Android

```java
ParseQuery<ParseObject> stateQuery = ParseQuery.getQuery("State");
stateQuery.whereEqualTo("state_name", "California");

stateQuery.getFirstInBackground((state, e) -> {
    if (e == null) {
        ParseQuery<ParseObject> cityQuery = ParseQuery.getQuery("City");
        cityQuery.whereEqualTo("state", state);
        cityQuery.findInBackground((cities, ex) -> {
            if (ex == null) {
                for (ParseObject city : cities) {
                    Log.d("Parse", "City: " + city.getString("city_name"));
                }
            } else {
                Log.e("Parse", "Error fetching cities: " + ex.getMessage());
            }
        });
    } else {
        Log.e("Parse", "Error fetching state: " + e.getMessage());
    }
});
```

iOS

```swift
let stateQuery = State.query("state_name" == "California")

stateQuery.first { result in
    switch result {
    case .success(let state):
        let cityQuery = City.query("state" == state)
        cityQuery.find { cityResult in
            switch cityResult {
            case .success(let cities):
                cities.forEach { city in
                    print("City: \(city.city_name ?? "Unknown")")
                }
            case .failure(let error):
                print("Error fetching cities: \(error.localizedDescription)")
            }
        }
    case .failure(let error):
        print("Error fetching state: \(error.localizedDescription)")
    }
}
```

PHP

```php
use Parse\ParseQuery;

// Query State
$stateQuery = new ParseQuery("State");
$stateQuery->equalTo("state_name", "California");
$state = $stateQuery->first();

if ($state) {
    // Query Cities
    $cityQuery = new ParseQuery("City");
    $cityQuery->equalTo("state", $state);
    $cities = $cityQuery->find();

    foreach ($cities as $city) {
        echo "City: " . $city->get("city_name") . "\n";
    }
}
```

.NET

```csharp
var stateQuery = new ParseQuery<ParseObject>("State").WhereEqualTo("state_name", "California");
var state = await stateQuery.FirstAsync();

if (state != null)
{
    var cityQuery = new ParseQuery<ParseObject>("City").WhereEqualTo("state", state);
    var cities = await cityQuery.FindAsync();

    foreach (var city in cities)
    {
        Console.WriteLine($"City: {city["city_name"]}");
    }
}
```

REST API

```curl
# Query State:
curl -X GET \
-H "X-Parse-Application-Id: YOUR_APP_ID" \
-H "X-Parse-REST-API-Key: YOUR_REST_API_KEY" \
"https://parseapi.back4app.com/classes/State?where={\"state_name\":\"California\"}"

# Query Cities:
# Replace STATE_OBJECT_ID with the objectId from the state query.
curl -X GET \
-H "X-Parse-Application-Id: YOUR_APP_ID" \
-H "X-Parse-REST-API-Key: YOUR_REST_API_KEY" \
"https://parseapi.back4app.com/classes/City?where={\"state\":{\"__type\":\"Pointer\",\"className\":\"State\",\"objectId\":\"STATE_OBJECT_ID\"}}"
```
:::

### **Example 2**: Query States with Related Cities

Create a query that returns states connected to any city:

:::CodeblockTabs
JavaScript

```javascript
const stateQuery = new Parse.Query("State");
const cityQuery = new Parse.Query("City");
cityQuery.matchesQuery("state", stateQuery);
cityQuery.include("state");

cityQuery.find().then(cities => {
  cities.forEach(city => {
    const state = city.get("state");
    console.log(`City: ${city.get("city_name")} belongs to state: ${state.get("state_name")}`);
  });
}).catch(error => {
  console.error("Error fetching data:", error.message);
});
```

Flutter

```dart
final stateQuery = QueryBuilder(ParseObject('State'));
final cityQuery = QueryBuilder(ParseObject('City'))
  ..whereMatchesQuery('state', stateQuery)
  ..includeObject(['state']);

final cityResult = await cityQuery.query();

if (cityResult.success && cityResult.results != null) {
  for (var city in cityResult.results!) {
    final state = city.get<ParseObject>('state');
    print('City: ${city.get<String>('city_name')} belongs to state: ${state?.get<String>('state_name')}');
  }
}
```

Android

```java
ParseQuery<ParseObject> stateQuery = ParseQuery.getQuery("State");
ParseQuery<ParseObject> cityQuery = ParseQuery.getQuery("City");
cityQuery.whereMatchesQuery("state", stateQuery);
cityQuery.include("state");

cityQuery.findInBackground((cities, e) -> {
    if (e == null) {
        for (ParseObject city : cities) {
            ParseObject state = city.getParseObject("state");
            Log.d("Parse", "City: " + city.getString("city_name") + " belongs to state: " + state.getString("state_name"));
        }
    } else {
        Log.e("Parse", "Error: " + e.getMessage());
    }
});
```

iOS

```swift
let stateQuery = State.query()
let cityQuery = City.query(matchesQuery(key: "state", query: stateQuery))
cityQuery.include("state")

cityQuery.find { result in
    switch result {
    case .success(let cities):
        cities.forEach { city in
            if let state = city.state {
                print("City: \(city.city_name ?? "Unknown") belongs to state: \(state.state_name ?? "Unknown")")
            }
        }
    case .failure(let error):
        print("Error: \(error.localizedDescription)")
    }
}
```

PHP

```php
use Parse\ParseQuery;

$stateQuery = new ParseQuery("State");
$cityQuery = new ParseQuery("City");
$cityQuery->matchesQuery("state", $stateQuery);
$cityQuery->includeKey("state");

$cities = $cityQuery->find();
foreach ($cities as $city) {
    $state = $city->get("state");
    echo "City: " . $city->get("city_name") . " belongs to state: " . $state->get("state_name") . "\n";
}
```

.NET

```csharp
var stateQuery = new ParseQuery<ParseObject>("State");
var cityQuery = new ParseQuery<ParseObject>("City").WhereMatchesQuery("state", stateQuery).Include("state");

var cities = await cityQuery.FindAsync();
foreach (var city in cities)
{
    var state = city.Get<ParseObject>("state");
    Console.WriteLine($"City: {city["city_name"]} belongs to state: {state["state_name"]}");
}
```

REST API

```curl
curl -X GET \
-H "X-Parse-Application-Id: YOUR_APP_ID" \
-H "X-Parse-REST-API-Key: YOUR_REST_API_KEY" \
"https://parseapi.back4app.com/classes/City?where={\"state\":{\"$inQuery\":{\"className\":\"State\"}}}&include=state"
```
:::

## **Best Practices**

To effectively work with relational schemas using Parse Server in Back4App, follow these best practices to ensure performance, maintainability, and scalability:

### **Choose the Right Relationship Type**

- **Use Pointers** for **one-to-one relationships**, such as linking a user to their profile.
- **Use Relations** for **many-to-many relationships**, such as linking a project to multiple tasks.

### **Efficient Querying**

- **Use&#x20;**`.include()` to load related data in the same query, reducing the need for multiple requests.
- **Limit results** using `limit()` and `skip()` to avoid fetching large datasets at once.
- **Index frequently queried fields** to speed up searches.

### **Avoid Excessive Nesting**

- **Keep queries flat** to reduce complexity and improve performance. Use nested queries sparingly and only when necessary.

### **Offload Complex Queries to Cloud Code**

- For **complex queries involving multiple relations** or large datasets, offload these to **Cloud Code** to keep the client lightweight and responsive.

## **Conclusion**

In this guide, you learned how to create relationships between classes and query-related objects on Back4app. Continue exploring the [**specific SDK documentation**](https://docs.parseplatform.org) to dive even deeper!
