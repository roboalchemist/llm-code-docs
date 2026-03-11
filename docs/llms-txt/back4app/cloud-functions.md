# Source: https://docs-containers.back4app.com/docs/get-started/cloud-functions.md

---
title: Cloud Code functions
slug: docs/get-started/cloud-functions
description: In this guide you'll learn how to write Functions and Calling via your SDK
image: https://www.back4app.com/_public/img/back4app-og.png
createdAt: 2024-01-23T19:42:51.820Z
updatedAt: 2025-01-27T19:41:44.728Z
---

**Cloud Code** is a powerful tool that enables you to execute JavaScript functions directly on the server, adding advanced features to your application without the need to manage your own servers. Running in Back4app’s environment ensures scalability and simplicity.

With Cloud Code, you can:

- Automate database actions in response to events.
- Create custom validations for requests.
- Integrate your application with external services using npm libraries.

## Prerequisites

:::hint{type="info"}
To complete this tutorial, you will need an app created at Back4app.
&#x20;Follow the [**Create a new App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create an app at Back4app.
:::

## Goal

- To deploy and execute a cloud function from your App

## 1 - Access your cloud code

Go to the **Cloud Code** section in your Back4app dashboard. You’ll find two main folders: `cloud` and `public`.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/QHCbDWjHiW7Wo3QrIj64o_screenshot-2024-11-15-at-152832.png)



## **2 - Edit the main.js file**

The main.js file is where your Cloud Code functions are defined.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/8ppF7oBa6LFWR4-FpSEFd_screenshot-2024-11-15-at-153229.png)

If needed, you can import functions from other files using:

:::CodeblockTabs
main.js

```javascript
require('./fileName.js');
```
:::

## 3 - Create your first Cloud Code Function

Some basic function examples include:

- A simple greeting function:

:::CodeblockTabs
main.js

```javascript
Parse.Cloud.define("hello", async (request) => {
    console.log("Hello from Cloud Code!");
    return "Hello from Cloud Code!";
});
```
:::

- A function to sum two numbers:

```javascript
Parse.Cloud.define("sumNumbers", async (request) => {
    return request.params.number1 + request.params.number2;
});
```

## 4- Deploy your code to the server

Once your functions are ready, click the **Deploy** button to publish them to the Back4app environment.&#x20;

## 5 - Test your cloud code function

You can test your functions directly via the API using tools like cURL or any preferred SDK. Below is an example for calling the `hello` function:

:::CodeblockTabs
```javascript
Parse.Cloud.run('hello')
  .then((result) => {
    console.log(result); // Output: "Hello from Cloud Code!"
  })
  .catch((error) => {
    console.error('Error:', error);
  });
```

Flutter

```dart
ParseCloudFunction function = ParseCloudFunction('hello');
ParseResponse response = await function.execute();

if (response.success) {
  print(response.result); // Output: "Hello from Cloud Code!"
} else {
  print('Error: ${response.error.message}');
}
```

Android

```java
ParseCloud.callFunctionInBackground("hello", new HashMap<>(), new FunctionCallback<Object>() {
    @Override
    public void done(Object result, ParseException e) {
        if (e == null) {
            Log.d("Cloud Code", result.toString()); // Output: "Hello from Cloud Code!"
        } else {
            Log.e("Cloud Code Error", e.getMessage());
        }
    }
});
```

iOS

```swift
ParseCloud.callFunction("hello", parameters: nil) { result in
    switch result {
    case .success(let response):
        print("Response: \(response)") // Output: "Hello from Cloud Code!"
    case .failure(let error):
        print("Error: \(error.localizedDescription)")
    }
}
```

.NET

```csharp
var result = await ParseCloud.CallFunctionAsync<string>("hello", null);
Console.WriteLine(result); // Output: "Hello from Cloud Code!"
```

```php
use Parse\ParseCloud;

try {
    $result = ParseCloud::run("hello");
    echo $result; // Output: "Hello from Cloud Code!"
} catch (Exception $ex) {
    echo "Error: " . $ex->getMessage();
}
```

REST API

```curl
curl -X POST \
-H "X-Parse-Application-Id: APPLICATION-ID" \
-H "X-Parse-REST-API-Key: REST-API-KEY" \
--data-urlencode "" \
https://parseapi.back4app.com/functions/hello
```
:::

## 6 - Additional Features

- **Data Manipulation**: Create, edit, or retrieve objects in your database with specific functions, such as this example for creating a ToDo item:

:::CodeblockTabs
main.js

```javascript
Parse.Cloud.define("createToDo", async (request) => {
    const todo = new Parse.Object('ToDo');
    todo.set('title', request.params.title);
    todo.set('done', request.params.done);
    return await todo.save();
});
```
:::

- **Advanced Queries**: Retrieve information directly from the database:

:::CodeblockTabs
main.js

```javascript
Parse.Cloud.define("getListToDo", async (request) => {
    const query = new Parse.Query("ToDo");
    query.equalTo("done", true);
    query.descending("title");
    return await query.find();
});
```
:::

## Conclusion

With Cloud Code, you can effortlessly build robust and customized solutions. It’s ideal for automation, integrations, and validations and works seamlessly with any technology, such as Flutter, React Native, or REST API.

If you encounter any issues, the [**Back4app support team**](https://www.back4app.com/support) is available to assist you.
