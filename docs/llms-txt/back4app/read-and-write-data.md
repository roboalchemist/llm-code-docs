# Source: https://docs-containers.back4app.com/docs/get-started/read-and-write-data.md

---
title: Reading and Writing data
slug: docs/get-started/read-and-write-data
description: In this guide you'll save Data Objects on Back4App and read them using the Parse SDKs
image: https://www.back4app.com/_public/img/back4app-og.png
createdAt: 2024-01-23T18:25:46.036Z
updatedAt: 2025-01-27T19:41:41.481Z
---

This guide will teach you how to **create, read, update, and delete** data objects on Back4app using the Parse SDK. Data storage on Back4app revolves around the `Parse.Object` class, which allows you to store key-value pairs of JSON-compatible data, providing flexibility and simplicity in data management.

## Objectives

- Understand how to perform data manipulation (CRUD) on Back4app using Parse SDK.
- Learn how to set up and use the Parse SDK across different platforms.

## Prerequisites

:::hint{type="info"}
**App on Back4app**: You need an app created on Back4app.

- [**Guide to creating a new app**](https://www.back4app.com/docs/get-started/new-parse-app).

**Parse SDK Installation**:

- [**Parse SDK installation guide**](https://www.back4app.com/docs/get-started/parse-sdk).
:::

## 1 - Creating Parse Objects

To store data in Back4app, you need to create a `ParseObject` associated with a specific class. For example, in a soccer-related application, you could create a `SoccerPlayers` class to store data about players.

:::CodeblockTabs
```javascript
async function saveNewPlayer() {
  const soccerPlayers = new Parse.Object("SoccerPlayers");
  soccerPlayers.set("playerName", "A. Wed");
  soccerPlayers.set("yearOfBirth", 1997);
  soccerPlayers.set("emailContact", "a.wed@email.io");
  soccerPlayers.set("attributes", ["fast", "good conditioning"]);

  try {
    const result = await soccerPlayers.save();
    console.log('New object created with objectId: ' + result.id);
  } catch (error) {
    console.error('Error: ' + error.message);
  }
}
```

Flutter

```dart
ParseObject soccerPlayers = ParseObject('SoccerPlayers')
  ..set('playerName', 'A. Wed')
  ..set('yearOfBirth', 1997)
  ..set('emailContact', 'a.wed@email.io')
  ..set('attributes', ['fast', 'good conditioning']);

ParseResponse response = await soccerPlayers.save();
if (response.success) {
  print('New object created with objectId: ${response.result.objectId}');
} else {
  print('Error: ${response.error.message}');
}
```

Android

```java
ParseObject soccerPlayers = new ParseObject("SoccerPlayers");
soccerPlayers.put("playerName", "A. Wed");
soccerPlayers.put("yearOfBirth", 1997);
soccerPlayers.put("emailContact", "a.wed@email.io");
soccerPlayers.put("attributes", Arrays.asList("fast", "good conditioning"));

soccerPlayers.saveInBackground(e -> {
  if (e == null) {
    Log.d("Parse", "New object created with objectId: " + soccerPlayers.getObjectId());
  } else {
    Log.e("ParseError", e.getMessage());
  }
});
```

iOS

```swift
let soccerPlayer = ParseObject(className: "SoccerPlayers")
soccerPlayer["playerName"] = "A. Wed"
soccerPlayer["yearOfBirth"] = 1997
soccerPlayer["emailContact"] = "a.wed@email.io"
soccerPlayer["attributes"] = ["fast", "good conditioning"]

soccerPlayer.save { result in
    switch result {
    case .success(let savedPlayer):
        print("New object created with objectId: \(savedPlayer.objectId!)")
    case .failure(let error):
        print("Error: \(error.localizedDescription)")
    }
}
```

PHP

```php
$soccerPlayers = new ParseObject("SoccerPlayers");
$soccerPlayers->set("playerName", "A. Wed");
$soccerPlayers->set("yearOfBirth", 1997);
$soccerPlayers->set("emailContact", "a.wed@email.io");
$soccerPlayers->setArray("attributes", ["fast", "good conditioning"]);

try {
    $soccerPlayers->save();
    echo 'New object created with objectId: ' . $soccerPlayers->getObjectId();
} catch (ParseException $ex) {
    echo 'Error: ' . $ex->getMessage();
}
```

.NET

```csharp
ParseObject soccerPlayers = new ParseObject("SoccerPlayers");
soccerPlayers["playerName"] = "A. Wed";
soccerPlayers["yearOfBirth"] = 1997;
soccerPlayers["emailContact"] = "a.wed@email.io";
soccerPlayers["attributes"] = new List<string> { "fast", "good conditioning" };

await soccerPlayers.SaveAsync();
Console.WriteLine("New object created with objectId: " + soccerPlayers.ObjectId);
```

REST API

```curl
curl -X POST \
  -H "X-Parse-Application-Id: APPLICATION_ID" \
  -H "X-Parse-REST-API-Key: REST_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "playerName": "A. Wed",
    "yearOfBirth": 1997,
    "emailContact": "a.wed@email.io",
    "attributes": ["fast", "good conditioning"]
  }' \
  https://parseapi.back4app.com/classes/SoccerPlayers
```
:::

After running this code, you can verify the new object in the **Database** section of the Back4app Dashboard. Note that you don’t need to manually create the SoccerPlayers class; it will be created automatically the first time an object is saved.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/KuqRY-K2J4cJ0sP4doJuA_screenshot-2024-11-13-at-161114.png)

## 2 - Reading Parse Objects

To retrieve saved data, you can use a `ParseQuery`. For instance, to fetch the player created above by its `objectId`:

:::CodeblockTabs
JS

```javascript
async function retrievePlayer() {
  const query = new Parse.Query("SoccerPlayers");
  
  try {
    const player = await query.get("HMcTr9rD3s");  // Replace with the actual objectId
    console.log("Player Name: " + player.get("playerName"));
    console.log("Year of Birth: " + player.get("yearOfBirth"));
    console.log("Email Contact: " + player.get("emailContact"));
  } catch (error) {
    console.error("Error retrieving object: " + error.message);
  }
}
```

Flutter

```dart
ParseResponse response = await ParseObject("SoccerPlayers").getObject("HMcTr9rD3s");  // Replace with the actual objectId

if (response.success) {
  ParseObject player = response.result;
  print("Player Name: ${player.get<String>('playerName')}");
  print("Year of Birth: ${player.get<int>('yearOfBirth')}");
  print("Email Contact: ${player.get<String>('emailContact')}");
} else {
  print("Error retrieving object: ${response.error.message}");
}
```

Android

```java
ParseQuery<ParseObject> query = ParseQuery.getQuery("SoccerPlayers");
query.getInBackground("HMcTr9rD3s", (player, e) -> {  // Replace with the actual objectId
  if (e == null) {
    Log.d("Parse", "Player Name: " + player.getString("playerName"));
    Log.d("Parse", "Year of Birth: " + player.getInt("yearOfBirth"));
    Log.d("Parse", "Email Contact: " + player.getString("emailContact"));
  } else {
    Log.e("ParseError", "Error retrieving object: " + e.getMessage());
  }
});
```

iOS

```swift
let query = ParseQuery(className: "SoccerPlayers")
query.get(objectId: "HMcTr9rD3s") { result in  // Replace with the actual objectId
    switch result {
    case .success(let player):
        print("Player Name: \(player["playerName"] ?? "No name")")
        print("Year of Birth: \(player["yearOfBirth"] ?? "No birth year")")
        print("Email Contact: \(player["emailContact"] ?? "No email")")
    case .failure(let error):
        print("Error retrieving object: \(error.localizedDescription)")
    }
}

```

PHP

```php
$query = new ParseQuery("SoccerPlayers");
try {
    $player = $query->get("HMcTr9rD3s");  // Replace with the actual objectId
    echo "Player Name: " . $player->get("playerName") . "\n";
    echo "Year of Birth: " . $player->get("yearOfBirth") . "\n";
    echo "Email Contact: " . $player->get("emailContact") . "\n";
} catch (ParseException $ex) {
    echo 'Error retrieving object: ' . $ex->getMessage();
}
```

.NET

```csharp
var query = ParseObject.GetQuery("SoccerPlayers");
var player = await query.GetAsync("HMcTr9rD3s");  // Replace with the actual objectId

Console.WriteLine("Player Name: " + player.Get<string>("playerName"));
Console.WriteLine("Year of Birth: " + player.Get<int>("yearOfBirth"));
Console.WriteLine("Email Contact: " + player.Get<string>("emailContact"));
```

REST API

```curl
curl -X GET \
  -H "X-Parse-Application-Id: APPLICATION_ID" \
  -H "X-Parse-REST-API-Key: REST_API_KEY" \
  https://parseapi.back4app.com/classes/SoccerPlayers/HMcTr9rD3s  # Replace with the actual objectId
```
:::

In addition to `objectId`, you can also query by other parameters (e.g., `yearOfBirth`, `playerName`), offering greater flexibility in data searches.

## 3 - Updating Parse Objects

To update an object, retrieve it first, set new values for the desired attributes, and call the `save()` method.

:::CodeblockTabs
```javascript
async function updatePlayer() {
  const query = new Parse.Query("SoccerPlayers");
  
  try {
    const player = await query.get("HMcTr9rD3s");  // Replace with the actual objectId
    player.set("yearOfBirth", 1998);
    await player.save();
    console.log("Object updated successfully!");
  } catch (error) {
    console.error("Error updating object: " + error.message);
  }
}
```

Flutter

```dart
ParseObject player = ParseObject("SoccerPlayers")..objectId = "HMcTr9rD3s";  // Replace with the actual objectId
player.set("yearOfBirth", 1998);

ParseResponse response = await player.save();
if (response.success) {
  print("Object updated successfully!");
} else {
  print("Error updating object: ${response.error.message}");
}

```

Android

```java
ParseQuery<ParseObject> query = ParseQuery.getQuery("SoccerPlayers");
query.getInBackground("HMcTr9rD3s", (player, e) -> {  // Replace with the actual objectId
  if (e == null) {
    player.put("yearOfBirth", 1998);
    player.saveInBackground(e1 -> {
      if (e1 == null) {
        Log.d("Parse", "Object updated successfully!");
      } else {
        Log.e("ParseError", "Error updating object: " + e1.getMessage());
      }
    });
  } else {
    Log.e("ParseError", "Error retrieving object: " + e.getMessage());
  }
});
```

iOS

```swift
let query = ParseQuery(className: "SoccerPlayers")
query.get(objectId: "HMcTr9rD3s") { result in  // Replace with the actual objectId
    switch result {
    case .success(var player):
        player["yearOfBirth"] = 1998
        player.save { saveResult in
            switch saveResult {
            case .success:
                print("Object updated successfully!")
            case .failure(let error):
                print("Error updating object: \(error.localizedDescription)")
            }
        }
    case .failure(let error):
        print("Error retrieving object: \(error.localizedDescription)")
    }
}
```

```php
$query = new ParseQuery("SoccerPlayers");
try {
    $player = $query->get("HMcTr9rD3s");  // Replace with the actual objectId
    $player->set("yearOfBirth", 1998);
    $player->save();
    echo "Object updated successfully!";
} catch (ParseException $ex) {
    echo 'Error updating object: ' . $ex->getMessage();
}
```

.NET

```csharp
var query = ParseObject.GetQuery("SoccerPlayers");
var player = await query.GetAsync("HMcTr9rD3s");  // Replace with the actual objectId

player["yearOfBirth"] = 1998;
await player.SaveAsync();
Console.WriteLine("Object updated successfully!");
```

REST API

```curl
curl -X PUT \
  -H "X-Parse-Application-Id: APPLICATION_ID" \
  -H "X-Parse-REST-API-Key: REST_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"yearOfBirth": 1998}' \
  https://parseapi.back4app.com/classes/SoccerPlayers/HMcTr9rD3s  # Replace with the actual objectId
```
:::

## 4 - Deleting Parse Objects

To delete an object, retrieve it by `objectId` and use the `destroy()` method.

:::CodeblockTabs
```javascript
async function deletePlayer() {
  const query = new Parse.Query("SoccerPlayers");
  
  try {
    const player = await query.get("HMcTr9rD3s");  // Replace with the actual objectId
    await player.destroy();
    console.log("Object deleted successfully!");
  } catch (error) {
    console.error("Error deleting object: " + error.message);
  }
}
```

Flutter

```dart
ParseObject player = ParseObject("SoccerPlayers")..objectId = "HMcTr9rD3s";  // Replace with the actual objectId

ParseResponse response = await player.delete();
if (response.success) {
  print("Object deleted successfully!");
} else {
  print("Error deleting object: ${response.error.message}");
}
```

Android

```java
ParseQuery<ParseObject> query = ParseQuery.getQuery("SoccerPlayers");
query.getInBackground("HMcTr9rD3s", (player, e) -> {  // Replace with the actual objectId
  if (e == null) {
    player.deleteInBackground(e1 -> {
      if (e1 == null) {
        Log.d("Parse", "Object deleted successfully!");
      } else {
        Log.e("ParseError", "Error deleting object: " + e1.getMessage());
      }
    });
  } else {
    Log.e("ParseError", "Error retrieving object: " + e.getMessage());
  }
});
```

iOS

```swift
let query = ParseQuery(className: "SoccerPlayers")
query.get(objectId: "HMcTr9rD3s") { result in  // Replace with the actual objectId
    switch result {
    case .success(let player):
        player.delete { deleteResult in
            switch deleteResult {
            case .success:
                print("Object deleted successfully!")
            case .failure(let error):
                print("Error deleting object: \(error.localizedDescription)")
            }
        }
    case .failure(let error):
        print("Error retrieving object: \(error.localizedDescription)")
    }
}
```

PHP

```php
$query = new ParseQuery("SoccerPlayers");
try {
    $player = $query->get("HMcTr9rD3s");  // Replace with the actual objectId
    $player->destroy();
    echo "Object deleted successfully!";
} catch (ParseException $ex) {
    echo 'Error deleting object: ' . $ex->getMessage();
}
```

.NET

```csharp
var query = ParseObject.GetQuery("SoccerPlayers");
var player = await query.GetAsync("HMcTr9rD3s");  // Replace with the actual objectId

await player.DeleteAsync();
Console.WriteLine("Object deleted successfully!");
```

REST API

```curl
curl -X DELETE \
  -H "X-Parse-Application-Id: APPLICATION_ID" \
  -H "X-Parse-REST-API-Key: REST_API_KEY" \
  https://parseapi.back4app.com/classes/SoccerPlayers/HMcTr9rD3s  # Replace with the actual objectId
```
:::

:::hint{type="info"}
Again, you don’t have to retrieve the object by its objectId. Parse has many search alternatives to retrieve information from ParseObjects, which you can find out more about in the official Parse documentation for each distinct technology.
:::

## Best Practices and Additional Tips

- **Naming Conventions**: Use ClassNamesLikeThis for classes and keyNamesLikeThis for keys to keep your code organized and readable.
- **Common Error Checks**: If you experience issues connecting to the Parse SDK, verify your [**SDK installation and configuration**](https://www.back4app.com/docs/get-started/parse-sdk).
- **Automatic Fields**: Remember that each Parse object automatically includes `createdAt`, `updatedAt`, and `objectId` fields.

## Next Steps

After persisting save and reading your first data on Back4app, we recommend keeping exploring the data storage using the guides below. You will find how to store supported data types, save and query relational data, use geopoints, and create optimized data models.

::::LinkArray
:::LinkArrayItem{headerType="IMAGE" headerImage="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/pEkmfq5PdkxC3lmfRzYsE_1.png"}
&#x20;       [**React Native**](https://www.back4app.com/docs/react-native/parse-sdk/react-native-sdk)
:::

:::LinkArrayItem{headerType="IMAGE" headerImage="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/tPONkoW1aPPhiAdTvbvrx_sem-nome-rectangle-sticker-landscape.png"}
[**Flutter**](https://www.back4app.com/docs/flutter/parse-sdk/parse-flutter-sdk)
:::

:::LinkArrayItem{headerType="IMAGE" headerImage="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/vqJJw7ljIhPJ1Yfz7mD9n_3.png"}
[**Android&#x20;**](https://www.back4app.com/docs/android/android-project-with-source-code-download)
:::

:::LinkArrayItem{headerType="IMAGE" headerImage="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/rzkB1YU-Feimt_SWfZUuC_4.png"}
[**iOS**](https://www.back4app.com/docs/ios/ios-app-template)
:::

:::LinkArrayItem{headerType="IMAGE" headerImage="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/GsQE6ru-jj2rRbUt7P3Tr_5.png"}
****[**Javascript**](https://www.back4app.com/docs/javascript/parse-javascript-sdk)
:::

:::LinkArrayItem{headerType="IMAGE" headerImage="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/35IqTes9QhdmijlReYBYZ_6.png"}
[**GraphQL**](https://www.back4app.com/docs/parse-graphql/graphql-getting-started)
:::

:::LinkArrayItem{headerType="IMAGE" headerImage="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/CS13bUltyBMZaO7SPfWC0_1.png"}
[**ReactJS**](https://www.back4app.com/docs/react/data-objects/react-crud-tutorial)
:::
::::

## Conclusion

This guide provides a solid starting point for working with data on Back4app, making data storage and manipulation across platforms easy using the Parse SDK. For any questions, feel free to reach out to [**Back4app support**](https://www.back4app.com/support)!
