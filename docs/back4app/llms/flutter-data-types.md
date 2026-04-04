# Source: https://docs-containers.back4app.com/docs/flutter/parse-sdk/data-objects/flutter-data-types.md

---
title: Data Types
slug: docs/flutter/parse-sdk/data-objects/flutter-data-types
description: In this guide you learn about Datatype of Parse using Flutter and how to read and save this data.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-15T14:18:16.681Z
updatedAt: 2025-01-17T21:03:58.489Z
---

This guide introduces Parse data types in Flutter, using examples from the `main.dart` file. Parse data storage revolves around ParseObject, which contains key-value pairs of JSON-compatible data, making it schemaless. This means you can store any data without defining a schema in advance.

You can set whatever key-value pairs you want, and our backend will store them.

For example, let’s say you’re tracking high scores for a game. A single Parse Object could contain:

:::BlockQuote
score: 1337, playerName: "Sean Plott", cheatMode: false
:::

:::hint{type="info"}
We suggest you `NameYourClassesLikeThis` and `nameYourKeysLikeThis` to enhance code readability and maintainability.
:::

## Understanding our App

To better understand Back4app, let's explore code examples of Parse operations in a Flutter application with the major supported data types. This guide won’t explain any Flutter app code as the primary focus is using Parse with Flutter.

## Prerequisites

To complete this tutorial, you will need:

:::hint{type="info"}
- [**Android Studio&#x20;**](https://developer.android.com/studio)or [**VS Code installed**](https://code.visualstudio.com/) (with [**Plugins**](https://docs.flutter.dev/get-started/editor) Dart and Flutter)
- An app [**created**](https://www.back4app.com/docs/get-started/new-parse-app) on Back4app:
  - **Note:&#x20;**&#x46;ollow the [**New Parse App Tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create a Parse App on Back4app.
- A Flutter app connected to Back4app.
  - **Note:&#x20;**&#x46;ollow the [**Install Parse SDK on the Flutter project**](https://www.back4app.com/docs/flutter/parse-sdk/parse-flutter-sdk) to create a Flutter Project connected to Back4app.
- A device (or virtual device) running Android or iOS.
:::

## 1 - Working with Parse Objects

Each ParseObject has a class name (e.g., GamePoint) used to distinguish different data types. Here’s how you can create and save a new Parse object with data types `string`, `int`, & `boolean`:

```dart
final gamePoint = ParseObject('GamePoint')
  ..set('score', 1337)
  ..set('playerName', 'Sean Plott')
  ..set('cheatMode', false);
await gamePoint.save();
```

**To query the new Parse object and retrieve the data types:**

```dart
  final QueryBuilder<ParseObject> queryGamePoints = QueryBuilder<ParseObject>(ParseObject('GamePoint'));

  final ParseResponse response = await queryGamePoints.query();

  if (response.success && response.results != null) {
    for (var gamePoint in response.results!) {
      final score = gamePoint.get<int>('score');
      final playerName = gamePoint.get<String>('playerName');
      final cheatMode = gamePoint.get<bool>('cheatMode');
      
    }
```

## 2 - Counters

You can increment or decrement an integer field in a ParseObject using the `set()` method.

However, this isn't effective and can lead to problems if multiple clients are trying to update the same counter. Parse provides two methods that automatically increment and decrement any number field to store counter-type data.

`setIncrement()`

`setDecrement()`

An update to increment a counter `int` value will be written as:

```dart
 final gamePoint = ParseObject('GamePoint')
  ..objectId = 'yourObjectId'
  ..setIncrement('intField', 1);
 await gamePoint.save();
```

To decrement:

```dart
 final gamePoint = ParseObject('GamePoint')
  ..objectId = 'yourObjectId'
  ..setDecrement('intField', 1);
 await gamePoint.save();
```

Using `setIncrement()` and `setDecrement()` with the `save()` call allows you to update a value as part of a larger save operation where you may be modifying multiple fields. This is better to avoid extra network requests.

## 3 - Lists

Parse provides methods to work with list data, including `setAdd`, `setAddUnique`, `setRemove`, and their respective `All` versions.

List: `["a","b","c"]`

### 3.1 - setAdd

```dart
final gamePoint = ParseObject('GamePoint')
..objectId = 'yourObjectId'
..setAdd('listStringField', 'd');
await gamePoint.save();
```

Result: `["a","b","c","d"]`

### 3.2 - setAddAll

```dart
final gamePoint = ParseObject('GamePoint')
..objectId = 'yourObjectId'
..setAddAll('listStringField', ['e','f']);
await gamePoint.save();
```

Result: `["a","b","c","d","e","f"]`

`setAddAll` does not add duplicate elements if the list already contains them.

### 3.3 - setAddUnique

```dart
final gamePoint = ParseObject('GamePoint')
..objectId = 'yourObjectId'
..setAddUnique('listStringField', ['a', 'e', 'g']);
await gamePoint.save();
```

Result: `["a","b","c","d","e","f","g"]`

### 3.4 - setRemove

```dart
final gamePoint = ParseObject('GamePoint')
 ..objectId = 'yourObjectId'
 ..setRemove('listStringField', 'd');
 await gamePoint.save();
```

Result: `["a","b","c","e","f","g"]`

## 4 - Remove field from ParseObject

You can delete a single field from an object by using the unset operation:

```dart
final gamePoint = ParseObject('GamePoint')
..objectId = 'yourObjectId'
..unset("listStringField");
```

## 5 -  Files

ParseFile lets you store and retrieve application files in the Cloud.
Below is a basic example of uploading a local image file to Back4App:

```dart
// Create ParseFile object
 final parseFile = ParseFile(File(image.path));

 final response = await parseFile.save();

 if (response.success) {
   print('File uploaded successfully: ${parseFile.url}');

   // Save this file in an object 
   final gamePoint = ParseObject('GamePoint')
     ..set('title', 'Post with an Image')
     ..set('imageFile', parseFile); // Saving the file as a field

   final postResponse = await gamePoint.save();
   }
```

This code snippet shows how to retrieve the image file:

```dart
final query = QueryBuilder<ParseObject>(ParseObject('GamePoint'));

  final response = await query.query();

  if (response.success && response.results != null) {
    for (var gamePoint in response.results!) {
      ParseFileBase? varFile = gamePoint.get<ParseFileBase>('file');
      if (varFile != null) {
        final fileUrl = varFile.url;
        print('Game Title: Image URL: $fileUrl');
      } else {
        print('No file found for this object.');
      }
    }
  }
```

Starting from `Parse Server 5.2.3` they are breaking changes that could cause errors during an attempt to upload files. Follow [**this guide**](https://www.back4app.com/docs/platform/parse-server-version#O-CiL) to fix any upload issues you may experience.

A later guide will further discuss and show templates on how to [**save and display Files with Parse**](https://www.back4app.com/docs/flutter/parse-sdk/flutter-save-file).

## 6 - GeoPoint

Parse allows you to associate real-world latitude and longitude coordinates with an object with its GeoPoint data type. Adding a ParseGeoPoint to a ParseObject will enable queries to consider the proximity of an object to a reference point.

Example:

```dart
 // Request permission here and get the current location: the `position` object.
 
 // Create GeoPoint object
  final geoPoint = ParseGeoPoint(latitude: position.latitude, longitude: position.longitude);

 // Create an object with the GeoPoint
  final gamePoint = ParseObject('GamePoint')
    ..set('name', 'Current Location')
    ..set('location', geoPoint); // Save the GeoPoint in a field

  final response = await gamePoint.save();
```

You can find a standalone example of saving Geopoint location in this [**main.dart**](https://github.com/templates-back4app/Flutter_DataTypes/blob/18c4c372eb49c1cd950eeaac355564134a5e70c4/lib/src/main.dart) file.

## Full App Example

This example demonstrates how to:

- Create, delete, and update a `GamePoint` Parse object.
- Handle various data types, including strings, doubles, booleans, files, geopoint, lists, and dates.

On iOS, you will need to grant your simulator the necessary access permissions.

:::hint{type="info"}
- iOS provides a developer guide on protected resources. The example applications in this guide will require the [**Location**](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationwheninuseusagedescription) and  [**Photos**](https://developer.apple.com/documentation/bundleresources/information-property-list/nsphotolibraryaddusagedescription) permission keys found in that guide to work. Add the keys to the `Info.plist` file, located at `/ios/Runner/Info.plist`:
:::

You can skip the above step if you are running your Flutter app on the web:

```dart
import 'dart:async';

import 'package:flutter/material.dart';
import 'package:parse_server_sdk_flutter/parse_server_sdk_flutter.dart';
import 'package:image_picker/image_picker.dart';
import 'package:flutter/foundation.dart';
import 'dart:io';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  const keyParseApplicationId = 'YOUR_APPLICATION_ID';
  const keyParseClientKey = 'YOUR_CLIENT_KEY';
  const keyParseServerUrl = 'https://parseapi.back4app.com';
  await Parse().initialize(
    keyParseApplicationId,
    keyParseServerUrl,
    clientKey: keyParseClientKey,
    autoSendSessionId: true,
    debug: true,
  );

  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'DataTypes',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key});

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final TextEditingController _stringController = TextEditingController();
  final TextEditingController _doubleController = TextEditingController();
  final TextEditingController _listStringController = TextEditingController();
  final TextEditingController _listIntController = TextEditingController();
  final TextEditingController _pointerController = TextEditingController();
  final TextEditingController _objectIdController = TextEditingController();
  final TextEditingController _uniqueValueController = TextEditingController();
  final TextEditingController _removeValueController = TextEditingController();

  bool _boolValue = false;
  DateTime _selectedDate = DateTime.now();
  final String _responseMessage = '';
  XFile? pickedFile;
  bool isLoading = false;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('DataTypes'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: SingleChildScrollView(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: <Widget>[
              _buildTextField('String Field', _stringController),
              const SizedBox(height: 20),
              _buildTextField('Double Field', _doubleController,
                  isNumeric: true),
              const SizedBox(height: 20),
              _buildSwitch('Bool Field', _boolValue, (value) {
                setState(() {
                  _boolValue = value;
                });
              }),
              const SizedBox(height: 20),
              TextButton(
                onPressed: () => _selectDate(context),
                child: Text(
                    'Select Date: ${_selectedDate.toLocal()}'.split(' ')[0]),
              ),
              const SizedBox(height: 20),
              _buildTextField(
                  'List String Field (comma-separated)', _listStringController),
              const SizedBox(height: 20),
              _buildTextField(
                  'List Int Field (comma-separated)', _listIntController),
              const SizedBox(height: 20),
              _buildTextField('Pointer Field (Object ID)', _pointerController),
              const SizedBox(height: 20),
              _buildImagePicker(),
              const SizedBox(height: 20),
              ElevatedButton(
                onPressed: _saveData,
                child: const Text('Save'),
              ),
              const SizedBox(height: 20),
              ElevatedButton(
                onPressed: () async {
                  await _deleteData(_objectIdController.text);
                  // await dummyFunction();
                },
                child: const Text('Delete'),
              ),
              const SizedBox(height: 20),
              _buildTextField(
                  'Object ID to Delete or Update', _objectIdController),
              ElevatedButton(
                onPressed: () async {
                  await _updateData(_objectIdController.text);
                },
                child: const Text('Update'),
              ),
              const SizedBox(height: 20),
              _buildIncrementDecrementButtons(),
              const SizedBox(height: 20),
              _buildListOperations(),
              const SizedBox(height: 20),
              Text(_responseMessage),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildTextField(String label, TextEditingController controller,
      {bool isNumeric = false}) {
    return TextField(
      controller: controller,
      keyboardType: isNumeric ? TextInputType.number : TextInputType.text,
      decoration: InputDecoration(
        border: const OutlineInputBorder(),
        labelText: label,
      ),
    );
  }

  Widget _buildSwitch(String label, bool value, Function(bool) onChanged) {
    return SwitchListTile(
      title: Text(label),
      value: value,
      onChanged: onChanged,
    );
  }

  Widget _buildImagePicker() {
    return GestureDetector(
      child: pickedFile != null
          ? Container(
              width: 250,
              height: 250,
              decoration: BoxDecoration(border: Border.all(color: Colors.blue)),
              child: kIsWeb
                  ? Image.network(pickedFile!.path)
                  : Image.file(File(pickedFile!.path)),
            )
          : Container(
              width: 250,
              height: 250,
              decoration: BoxDecoration(border: Border.all(color: Colors.blue)),
              child: const Center(
                  child: Text('Click here to pick image from GamePoint')),
            ),
      onTap: () async {
        final picker = ImagePicker();
        XFile? image = (await picker.pickImage(source: ImageSource.gallery));
        if (image != null) {
          setState(() {
            pickedFile = image;
          });
        }
      },
    );
  }

  Widget _buildIncrementDecrementButtons() {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      children: [
        Expanded(
          child: ElevatedButton(
            onPressed: () async {
              await _incrementField(_objectIdController.text);
            },
            child: const Text('+ Double'),
          ),
        ),
        const SizedBox(width: 10), // Adding some space between buttons
        Expanded(
          child: ElevatedButton(
            onPressed: () async {
              await _decrementField(_objectIdController.text);
            },
            child: const Text('- Double'),
          ),
        ),
      ],
    );
  }

  Widget _buildListOperations() {
    return Column(
      children: [
        _buildTextField('Unique Value to Add', _uniqueValueController),
        ElevatedButton(
          onPressed: () async {
            await _addUniqueToList(
                _objectIdController.text, _uniqueValueController.text);
          },
          child: const Text('Add Unique'),
        ),
        const SizedBox(height: 20),
        _buildTextField('Value to Remove', _removeValueController),
        ElevatedButton(
          onPressed: () async {
            await _removeFromList(
                _objectIdController.text, _removeValueController.text);
          },
          child: const Text('Remove'),
        ),
      ],
    );
  }

  Future<void> _saveData() async {
    //Parse values
    String stringValue = _stringController.text;
    List<String> listStringValue = _listStringController.text.isNotEmpty
        ? _listStringController.text
            .split(',') // Split by comma
            .map((e) =>
                e.trim()) // Remove any surrounding whitespace from each element
            .toList()
        : [];
    List<int> listtIntValue = _listIntController.text.isNotEmpty
        ? _listIntController.text
            .split(',') // Split by comma
            .map(
                (e) => int.parse(e.trim())) // Convert each string to an integer
            .toList()
        : [];
    double? doubleValue;
    if (_doubleController.text.isNotEmpty) {
      doubleValue = double.parse(_doubleController.text);
    }
    bool boolValue = _boolValue;
    DateTime selectedDate = _selectedDate;

    final gamePoint = ParseObject('GamePoint')
      ..set('bool', boolValue)
      ..set('date', selectedDate);
    if (stringValue.isNotEmpty) gamePoint.set('string', stringValue);
    if (doubleValue != null) gamePoint.set('double', doubleValue);
    if (listStringValue.isNotEmpty) {
      gamePoint.setAddAll('listString', listStringValue);
    }
    if (listtIntValue.isNotEmpty) gamePoint.setAddAll('listint', listtIntValue);
    if (_pointerController.text.isNotEmpty) {
      gamePoint.set('pointer', _parsePointer(_pointerController.text));
    }

    if (pickedFile != null) {
      setState(() {
        isLoading = true;
      });

      ParseFileBase? parseFile;

      if (kIsWeb) {
        parseFile =
            ParseWebFile(await pickedFile!.readAsBytes(), name: 'file.jpg');
      } else {
        parseFile = ParseFile(File(pickedFile!.path));
      }
      await parseFile.save();

      gamePoint.set('file', parseFile);
    }

    var apiResponse = await gamePoint.save();

    if (apiResponse.success && apiResponse.results != null) {
      setState(() {
        isLoading = false;
        pickedFile = null;
      });

      ScaffoldMessenger.of(context)
        ..removeCurrentSnackBar()
        ..showSnackBar(const SnackBar(
          content: Text(
            'File saved successfully on Back4app',
            style: TextStyle(color: Colors.white),
          ),
          duration: Duration(seconds: 3),
          backgroundColor: Colors.blue,
        ));
    } else {
      print("This is your request error: ${apiResponse.error}");
    }
  }

  Future<void> _updateData(String objectId) async {
    final gamePoint = ParseObject('GamePoint')..objectId = objectId;
    // Update fields with new values
    if (_stringController.text.isNotEmpty) {
      gamePoint.set('string', _stringController.text);
    }

    if (_doubleController.text.isNotEmpty) {
      gamePoint.set('double', double.parse(_doubleController.text));
    }

    gamePoint.set('bool', _boolValue);
    gamePoint.set('date', _selectedDate);

    if (_listStringController.text.isNotEmpty) {
      List<String> listStringValue =
          _listStringController.text.split(',').map((e) => e.trim()).toList();
      gamePoint.setAddAll('listString', listStringValue);
    }

    if (_listIntController.text.isNotEmpty) {
      List<int> listIntValue = _listIntController.text
          .split(',')
          .map((e) => int.parse(e.trim()))
          .toList();
      gamePoint.setAddUnique('listint', listIntValue);
    }

    if (_pointerController.text.isNotEmpty) {
      gamePoint.set('pointer', _parsePointer(_pointerController.text));
    }

    if (pickedFile != null) {
      ParseFileBase? parseFile;
      if (kIsWeb) {
        parseFile =
            ParseWebFile(await pickedFile!.readAsBytes(), name: 'file.jpg');
      } else {
        parseFile = ParseFile(File(pickedFile!.path));
      }
      await parseFile.save();
      gamePoint.set('file', parseFile);
    }

    // Save the updated object
    var response = await gamePoint.save();

    if (response.success) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Data updated successfully!')),
      );
    } else {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
            content: Text('Error updating data: ${response.error!.message}')),
      );
    }
  }

  Future<void> _incrementField(String objectId) async {
    final gamePoint = ParseObject('GamePoint')
      ..objectId = objectId
      ..setIncrement('double', 1);
    await gamePoint.save();
  }

  Future<void> _decrementField(String objectId) async {
    final gamePoint = ParseObject('GamePoint')
      ..objectId = objectId
      ..setDecrement('double', -1);
    await gamePoint.save();
  }

  Future<void> _addUniqueToList(String objectId, String value) async {
    final gamePoint = ParseObject('GamePoint')
      ..objectId = objectId
      ..setAddUnique('listString', value);
    await gamePoint.save();
  }

  Future<void> _removeFromList(String objectId, String value) async {
    final gamePoint = ParseObject('GamePoint')
      ..objectId = objectId
      ..setRemove('listString', value);
    await gamePoint.save();
  }

  Future<void> _selectDate(BuildContext context) async {
    final DateTime? picked = await showDatePicker(
      context: context,
      initialDate: _selectedDate,
      firstDate: DateTime(2000),
      lastDate: DateTime(2101),
    );
    if (picked != null && picked != _selectedDate) {
      setState(() {
        _selectedDate = picked;
      });
    }
  }

  Future<void> _deleteData(String objectId) async {
    // Delete data logic
    final parseObject = ParseObject('GamePoint')
      ..objectId = objectId
      ..unset("listString");

    await parseObject.save();
  }

  // Convert Pointer field to a suitable format
  ParseObject _parsePointer(String objectId) {
    // There should be an existing Game class with objects
    final pointer = ParseObject('Game')..objectId = objectId;
    return pointer;
  }
}
```

This code initializes the Parse SDK in Flutter, sets up the main application, and displays a simple home page with a title.

## Conclusion

In this guide, you learned about ParseObjects and the various datatypes available to Parse. You also learned how to handle operations like saving and retrieving the datatypes to and from your back4app backend.
