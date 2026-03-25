# Source: https://docs-containers.back4app.com/docs/security/parse-security.md

---
title: App security Guidelines
slug: docs/security/parse-security
description: We’ll show you how to set up your app so that it's totally secure.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-02-26T19:04:53.335Z
updatedAt: 2025-01-17T01:09:35.828Z
---

# How to make a Secure App using Parse

## Introduction

**Ahoy Back4app community!**

This is a guest tutorial from Joren Winge at [**Startup Soul**](http://startup-soul.com/). We help startups build and launch their products fast. Our friends @ Back4app asked us to show you how to build a secure app on top of Back4app.

In this post, we’ll walk you through the steps to make a secure To-Do app on back4app. Security is important. If your app takes off at all you will need to make sure your app’s data is secure and that your system can’t be hacked.

## Security features on Parse

Lets first talk about the first level of security, ACLs - (access control list). ACLs are basically just rules you set when you create an object. Let’s say you create a to-do item, at the time of creation you can say who the item can be read by, and who it can be written by. You can assign certain users to be able to read that item or write to that item or you can set either one to the public which allows access to anyone. But ACLs don’t always work.

There are instances where you might need to have some more sophisticated logic instead of a simple ACL. Sometimes you can also paint yourself in a corner where you may need to give someone access to an object on a conditional basis instead of an absolute basis like with ACLs. So let’s skip using ACLs. They are too rigid and at the same time allow for too much access to the data. So I’m about to give you the secret to building a secure app on Back4App and Parse Server. You ready?

Class level permissions! Yes, we will set class level permissions for each table in our database. And the level of permission we will set is no permission at all. We will lock down each and every table so that no read or write access is allowed to anyone! Sounds extreme, I know, but this is the first step in creating a secure app. The only permission we will allow is on the User table which will be for the creation of new user objects and for the user to view his own data which is required for refreshing the current user.

We will secure the user from being able to view other users data by using ACLs. This is the one time we will use ACLs so I guess they are not totally useless. They are good to have but don’t rely on them to do everything. But how will we access the data you ask? Good question, glad you are thinking about it! Well, the secret to letting clients access the data in a controlled manner is to make each and every single interaction between the client and database filtered through a cloud code function. Yes, anytime you do anything with your app it will now be through a custom cloud code function. No more client-based PFQueries.

You pretty much skip using the entire client based Parse SDK except for Sign Up functions, Sign In functions, Forgot Password functions, and Log Out functions. For these, we still will use the native client SDKs. It’s just easier. Have you ever written cloud code before? No, you say? Well, it’s pretty easy. It’s just Javascript and it uses the Parse Javascript SDK but internally on your own app’s server. In fact, since Parse Server is based on Node JS, it’s pretty similar to writing routes with Express, but even easier since your query language is already installed and cloud code functions are a lot easier to write than an entire Node JS Express app.

So here is what we will do. We will use an iOS todo app that I have already created. We won’t bother with showing you how I created it. Instead, we will focus on writing cloud code and securing the database. The todo app will be a secure app where you can only access your own todos and you can only write your own todos. The data will be secure on the server safe from malicious rogue clients. I will also show you how to write a secure Parse background job - basically, the same thing as a cron job - so that you can have automated services send manipulate your data on a schedule. Sounds complicated but it’s not. Just imagine little server robots that do whatever you want on an automated schedule. Sounds cool right? Ok, so here we go!!!!!!

## Let’s set up the Back4app Secure ToDo App

**1) Create an App on Back4App:**

1. Create a new app on Back4App. Call the app ‘Secure ToDo App’. \* Note: Follow the [**New Parse App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create an app at Back4App. .
2. Go into the app’s Core Settings page and then click on Edit App Details.
3. Disable the checkbox called ‘Allow Client Class Creation’ to disable client class creation and hit save. We want to limit what the client can do as a rule.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/VNDlMYePW7A8bPrVK4-Yq_image.png)

**2) Set class level security permissions for the User class:**

1. Next we will set the permissions for the User class. Go into the Back4App database dashboard and click on the User class. Then click on the Security tab, then click on the gear icon in the top right. You should see a menu that says Simple/Advanced. Flip the slider to Advanced. You should then see the full class level permissions for this class. Disable the Find checkbox. Disable the Update and Delete checkbox. Finally, disable the Add Field checkbox. Then hit save. Your Security settings should look like this.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/FCpGNNzSvdsRQ8xJ1a_-G_image.png)

**3) Create the ToDo class:**

1. Hit Create a class and call it ToDo. Set the class type as custom.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/eU61hrjMThuTLTBivShRg_image.png)

**4) Set class level security permissions for the ToDo class:**

1. Next we will set the permissions for the ToDo class. Go into the Back4App database dashboard and click on the ToDo class. Then click on the Security tab, then click on the gear icon in the top right. You should see a menu that says Simple/Advanced. Flip the slider to Advanced. You should then see the full class level permissions for this class. Disable everything then hit save. Your Security settings should look like this.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/DhWsbHPtTx_UEDJxuCyht_image.png)

**5) Let’s add some columns to the ToDo class:**

1. First let’s join the ToDo class to the User class. We will do that by adding 2 columns.
2. The first column will be called ‘user’ and will be a pointer back to the user class.
3. Next let’s create a column for the user’s object id who created it. It will be a string type and will be called ‘userObjectId’.
4. Next let’s create a column to hold our actual todo information. It will also be a string and will be call ‘todoDescription’.
5. Let’s create a Boolean to hold the state of the todo. Let’s call it ‘finished’.
6. Finally let’s add one more column to hold the date you finished your todo. Let’s call it ‘finishedDate’ and set it to a date type.
7. Your ToDo class should look like this

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/IPxsB-USsmjzrX1ySC2WW_image.png)

**6) Let’s go over the client:**

The client is a pretty basic to do app. It uses the built in parse functions to login, create a new user, and reset your password. Besides that everything is cloud code based and secure. The user’s ACL’s are also set as soon as they login or signup just to be 100% sure the system is secure. Let’s start by writing the cloud code function to set the user’s ACL upon logging in or signing up.

:::hint{type="info"}
**At any time, you can access the complete iOS Project built with this tutorial at this&#x20;**[**GitHub repository**](https://github.com/mpc20001/secure-todo-app-swift-back4app-parse/tree/master/AddingParseSDK)**.**
:::

:::hint{type="info"}
**You can also access the Main.js cloud code file built for this tutorial at this&#x20;**[**GitHub repository.**](https://github.com/mpc20001/SecureToDoCloudCodeRepo)****
:::



- 1 . In the client go to ToDoController.swift and look for the function setUsersAclsNow. This function is called when you login or view the LoggedInViewController.swift. The function checks to see if you are logged in and if you are it calls the cloud function to setup your personal user ACL’s.

:::CodeblockTabs
ToDoController.swift

```swift
1   func setUsersAclsNow(){
2           if PFUser.current() != nil{
3               let cloudParams : [AnyHashable:String] = ["test":"test"]
4               PFCloud.callFunction(inBackground: setUsersAcls, withParameters: cloudParams, block: {
5                   (result: Any?, error: Error?) -> Void in
6                   if error != nil {
7                       //print(error.debugDescription)
8                       if let descrip = error?.localizedDescription{
9                           print(descrip)
10                      }
11                  }else{
12                      print(result as! String)
13                  }
14              })
15          }
16      }
```
:::



- 2 . Now let’s write the cloud code function

:::CodeblockTabs
Parse Server 3.X

```javascript
1   Parse.Cloud.define('setUsersAcls', async(request) => {
2       let currentUser = request.user;
3       currentUser.setACL(new Parse.ACL(currentUser));
4       return await currentUser.save(null, { useMasterKey: true });
5   });
```

Parse Server 2.X

```javascript
1   Parse.Cloud.define('setUsersAcls', function (request, response) {
2       var currentUser = request.user;
3       currentUser.setACL(new Parse.ACL(currentUser));
4       currentUser.save(null, {
5           useMasterKey: true,
6           success: function (object) {
7               response.success("Acls Updated");
8           },
9           error: function (object, error) {
10              response.error("Got an error " + error.code + " -  " + error.description);
11          }
12      });
13  });
```
:::

- 3 . This cloud code uses two key features of making your app secure, request.user and masterKey. Request.user let’s you access the user who is making the cloud code call and allows you to limit access for that user. In this case, we are using it to set the user’s acl’s to limit read access to the current user only. This way only the user can read their own information. The class level permissions prevent write access even for the current user. In this way users cannot modify their own information. They can only change things about their own user through cloud code. It is possible to import false information when the user first signs up, but I would reccomend writing a cloud code function to check the user’s information after a new user is created. The built in parse function for creating a new user is really helpful so i think it’s a decent tradeoff, but you can always set the default values for the user via cloud code right after they sign up. There are lots of fail safes you can also write into cloud code and have them run automatically and continously using background jobs to detect any malicious user information that was imported when the user was first created. If you want to be really secure, you can store any sensitive information like membership status or payment information on a separate table from the user table. That way the user cannot spoof any sensitive information on user creation.



- 4 . Next let’s look at creating a ToDo. In the client go to ToDoController.swift and look for the function saveToDo. This function is called when you create a new todo. The function takes a string that decribes the todo and saves it in the database.

:::CodeblockTabs
ToDoController.swift

```swift
1   func saveToDo(todoString:String, completion: @escaping (_ result: Bool, _ message:String, _ todoArray:[ToDo])->()){
2         var resultToDoArray:[ToDo] = []
3         let cloudParams : [AnyHashable:Any] = ["todoString":todoString]
4         PFCloud.callFunction(inBackground: createToDosForUser, withParameters: cloudParams, block: {
5             (result: Any?, error: Error?) -> Void in
6             if error != nil {
7                 if let descrip = error?.localizedDescription{
8                     completion(false, descrip, resultToDoArray)
9                 }
10            }else{
11                resultToDoArray = result as! [ToDo]
12                completion(true, "Success", resultToDoArray)
13            }
14        })
15    }
```
:::

- 5 . Now let’s write the cloud code function to save the todo in the database

:::CodeblockTabs
Parse Server 3.X

```javascript
1   Parse.Cloud.define("createToDosForUser", async(request) => {
2       let currentUser = request.user;
3       let todoString = request.params.todoString;
4       let ToDo = Parse.Object.extend("ToDo");
5       let todo = new ToDo();
6       todo.set("user", currentUser);
7       todo.set("userObjectId", currentUser.id);
8       todo.set("todoDescription", todoString);
9       todo.set("finished", false);
10      return await todo.save(null, { useMasterKey: true });
11  });
```

Parse Server 2.X

```javascript
1   Parse.Cloud.define("createToDosForUser", function(request, response) {
2       var currentUser = request.user;
3       var todoString = request.params.todoString;
4       var ToDo = Parse.Object.extend("ToDo");
5       var todo = new ToDo();
6       todo.set("user", currentUser);
7       todo.set("userObjectId", currentUser.id);
8       todo.set("todoDescription", todoString);
9       todo.set("finished", false);
10      todo.save(null, {
11          useMasterKey: true,
12          success: function (object) {
13              response.success([todo]);
14          },
15          error: function (object, error) {
16              response.error("Got an error " + error.code + " - " + error.description);
17          }
18      });
19  });
```
:::



- 6 . This cloud code function creates a todo object and sets the current user as the owner of the object. This is important so that only the user who created it can find it or modify it. By not allowing todos to be created in the client we are forcing the todo object to conform to our standards and making sure the todos are owned by the user who created them.

&#x20;

- 7 . Next let’s look at retrieving the todos that you created from the server. In the client go to ToDoController.swift and look for the function getToDosForDate. This function is called when you retrieve your todos. The function takes a date as a parameter and uses it to retrieve a list of todos that were created by you before that date in descending order. Using a date is a great way to write a lazy loading query that doesn’t use skips. Skip can sometimes fail on a large dataset.

:::CodeblockTabs
ToDoController.swift

```swift
1   func saveToDo(todoString:String, completion: @escaping (_ result: Bool, _ message:String, _ todoArray:[ToDo])->()){
2         var resultToDoArray:[ToDo] = []
3         let cloudParams : [AnyHashable:Any] = ["date":date]
4         PFCloud.callFunction(inBackground: getToDosForUser, withParameters: cloudParams, block: {
5             (result: Any?, error: Error?) -> Void in
6             if error != nil {
7                 if let descrip = error?.localizedDescription{
8                     completion(false, descrip, resultToDoArray)
9                 }
10            }else{
11                resultToDoArray = result as! [ToDo]
12                completion(true, "Success", resultToDoArray)
13            }
14        })
15    }
```
:::



- 8 . Now let’s write the cloud code function to retrieve todos from the database based on a starting date. We query for todos that are created before the parameter date so we use ‘query.lessThan’ because dates are basically numbers that get larger the farther in the future you are. I also included some tricky code here. Say we are including the user object who created the todo but we don’t want to share sensitive information about that user with other users we need to strip it from the json response. So we have a for loop where we take the user object out of the todo, remove the email and username from the json and then put it back in the todo. This is handy for removing sensitive data from an api call in situations where you cannot control what fields you return - such as an included user object. In this case we don’t really need it because this function will only return todos you created yourself. We do this by using CurrentUser again to query for only todos created by the CurrentUser that was attached to the request. The results are returned in descending order so that the latest todos appear first. When you need to lazy load another batch of todos you take the createdAt date from the last todo and use it as the date parameter for the next request.

:::CodeblockTabs
Parse Server 3.X

```javascript
1   Parse.Cloud.define("getToDosForUser", async(request) => {
2       let currentUser = request.user;
3       let date = request.params.date;
4       let query = new Parse.Query("ToDo");
5       query.equalTo("user", currentUser);
6       query.lessThan("createdAt", date);
7       query.descending("createdAt");
8       query.limit(100);
9       query.include("user");
10      let results = await query.find({ useMasterKey: true });
11      if(results.length === 0) throw new Error('No results found!');
12
13      let resultsArray = [];
14      for (let i = 0; i < results.length; i++) {
15          let todo = results[i];
16          let tempUser = todo.get("user");
17          let jsonUser = tempUser.toJSON();
18          delete jsonUser.email;
19          delete jsonUser.username;
20
21          jsonUser.__type = "Object";
22          jsonUser.className = "_User";
23
24          let cleanedTodo = todo.toJSON();
25          cleanedTodo.user = jsonUser;
26          cleanedTodo.__type = "Object";
27          cleanedTodo.className = "ToDo";
28          resultsArray.push(cleanedTodo);            
29      }
30      return resultsArray;
31  });
```

Parse Server 2.X

```javascript
1   Parse.Cloud.define("getToDosForUser", function(request, response) {
2       var currentUser = request.user;
3       var date = request.params.date;
4       var query = new Parse.Query("ToDo");
5       query.equalTo("user", currentUser);
6       query.lessThan("createdAt", date);
7       query.descending("createdAt");
8       query.limit(100);
9       query.include("user");
10      query.find({
11          useMasterKey: true,
12          success: function (results) {
13              var resultsArray = [];
14              for (var i = 0; i < results.length; i++) {
15                  var todo = results[i];
16                  var tempUser = todo.get("user");
17                  var jsonUser = tempUser.toJSON();
18                  delete jsonUser.email;
19                  delete jsonUser.username;
20
21                  jsonUser.__type = "Object";
22                  jsonUser.className = "_User";
23
24                  var cleanedTodo = todo.toJSON();
25                  cleanedTodo.user = jsonUser;
26                  cleanedTodo.__type = "Object";
27                  cleanedTodo.className = "ToDo";
28                  resultsArray.push(cleanedTodo);
29                }
30              response.success(resultsArray);
31          },
32          error: function (error) {
33              response.error("- Error - " + error.code + " " + error.message);
34          }
35     });
36  });
```
:::

- 9 . Now that we have the todos we can see them in the app and mark them as completed if we want. Lets cover that next.



- 10 . To mark a todo as completed just hit the ‘Mark As Completed’ button on any of the todos you created. This will fire off a method in the ToDoController.swift called ‘markToDosAsCompletedFor’ that takes the todo you selected as a parameter. It sends the todo.objectId to the server as a parameter and then returns the updated todo as a result.

:::CodeblockTabs
ToDoController.swift

```swift
1   func markToDosAsCompletedFor(todo:ToDo, completion: @escaping (_ result: Bool, _ message:String, _ todoArray:[ToDo])->()){
2           var resultToDoArray:[ToDo] = []
3           let cloudParams : [AnyHashable:Any] = ["todoId":todo.objectId ?? ""]
4           PFCloud.callFunction(inBackground: markToDoAsCompletedForUser, withParameters: cloudParams, block: {
5               (result: Any?, error: Error?) -> Void in
6               if error != nil {
7                   if let descrip = error?.localizedDescription{
8                       completion(false, descrip, resultToDoArray)
9                   }
10              }else{
11                  resultToDoArray = result as! [ToDo]
12                  completion(true, "Success", resultToDoArray)
13              }
14          })
15      }
```
:::



- 11 . Now we’ll write the cloud code to update this todo. It looks for the todo to update based on the objectId but it also uses the CurrentUser to make sure that the todo that is associated with the objectId was created by the user making the query. This makes sure that you can only view todos that you created and is thus secure. We include a limit of 1 result to make sure the server doesn’t continue to search after finding the todo. There’s another method for finding an object based on an objectId but I don’t like to use it since it can return weird results if it doesn’t find the object associated with the objectId. We are also setting the ‘finishedDate’ with the current date when the object was updated. By having the finishedDate set by this function only we’ve made sure the finishedDate is secure and cannot be faked or changed. We also used ‘query.equalTo(“finished”, false)’ to make sure that only an unfinished todo can be marked as finished and have the finishedDate set. That means once a todo has been marked as finished it can never be marked finished again at a later date.

:::CodeblockTabs
Parse Server 3.X

```javascript
1   Parse.Cloud.define("markToDoAsCompletedForUser", async(request) => {
2     let currentUser = request.user;
3     let todoId = request.params.todoId;
4     let query = new Parse.Query("ToDo");
5     query.equalTo("user", currentUser);
6     query.equalTo("objectId", todoId);
7     query.equalTo("finished", false);
8     let todo = await query.first({ useMasterKey: true });
9     if(Object.keys(todo).length === 0)  throw new Error('No results found!');
10    todo.set("finished", true);
11    let date = new Date();
12    todo.set("finishedDate", date);
13    try {
14      await todo.save(null, { useMasterKey: true}); 
15      return todo;   
16    } catch (error){
17      return("getNewStore - Error - " + error.code + " " + error.message);
18    }
19  });
```

Parse Server 2.X

```javascript
1   Parse.Cloud.define("markToDoAsCompletedForUser", function(request, response) {
2       var currentUser = request.user;
3       var todoId = request.params.todoId;
4       var query = new Parse.Query("ToDo");
5       query.equalTo("user", currentUser);
6       query.equalTo("objectId", todoId);
7       query.equalTo("finished", false);
8       query.limit(1);
9       query.find({
10          useMasterKey: true,
11          success: function (results) {
12              if (results.length > 0) {
13                  var todo = results[0];
14                  todo.set("finished", true);
15                  var date = new Date();
16                  todo.set("finishedDate", date);
17                  todo.save(null, {
18                      useMasterKey: true,
19                      success: function (object) {
20                          response.success([todo]);
21                      },
22                      error: function (object, error) {
23                          response.error("Got an error " + error.code + " : " + error.description);
24                      }
25                  });
26              } else {
27                  response.error("ToDo not found to update");
28              }
29
30          },
31          error: function (error) {
32              response.error("- Error - " + error.code + " " + error.message);
33          }
34      });
35  });
```
:::

**7) Wrap Up!**

1. And that’s it. You have built a secure todo app. Again, the key to making a secure app on parse server is disabling all class level permissions for all classes except for the User class. On the User class, you disable all permissions except CREATE, and GET. Also make sure to set all user’s ACL’s so that the user can only GET their own data. Then all your interactions go through cloud code and are filtered using the request.user aka the CurrentUser. So there ya go, you can now build secure systems on top of Parse server and Back4App. But wait you say? What about Background Jobs and Live Queries. Well, you have a good point, so I will cover that in two bonus sections next.



**8) Bonus Sections**

- 1 . Background jobs - sometimes you need to create a background job to run every hour, or every day or every week. If you are running with all you class level permissions turned off, your background job will not be able to query the database unless it’s set up correctly. This is kind of tricky to do so I want to include an example of it here. In this case we will create a background job that checks the database for unfinshed todos that are more than 1 year old and then automatically marks them as finished. The trick here is using ‘useMasterKey’ correctly.
  It has to be added to the query before the .then promise. Just follow this template and you should be able to write secure background jobs easily. You always start with writing a query that you want to iterate over the entire database and then make sure to include status.error if there is an error and end it with a status.success to make sure it completes. You can watch the logs on Back4App to see the background job working while you run it.

:::CodeblockTabs
Parse Server 3.X

```javascript
1   Parse.Cloud.job("markUnfinishedToDosOlderThan1YearAsFinished", async(request) => {
2       let date = new Date();
3       let intYear = date.getFullYear() - 1;
4       let query = new Parse.Query("ToDo");
5       query.equalTo("finished", intYear);
6       query.lessThan("createdAt", date);
7 
8       let todo = await query.find({ useMasterKey: true });
9       for (let i = 0; i < results.length; i++) {
10          let todo = results[i];
11          todo.set("finished", true);
12          todo.set("finishedDate", date);
13          try {
14              await todo.save(null, { useMasterKey: true});    
15          } catch (error){
16              console.log("getNewStore - Error - " + error.code + " " + error.message);
17          }
18      } 
19      return "Migration completed successfully.";
20  });
```

Parse Server 2.X

```javascript
1   Parse.Cloud.define("markToDoAsCompletedForUser", function(request, response) {
2       var currentUser = request.user;
3       var todoId = request.params.todoId;
4       var query = new Parse.Query("ToDo");
5       query.equalTo("user", currentUser);
6       query.equalTo("objectId", todoId);
7       query.equalTo("finished", false);
8       query.limit(1);
9       query.find({
10          useMasterKey: true,
11          success: function (results) {
12              if (results.length > 0) {
13                  var todo = results[0];
14                  todo.set("finished", true);
15                  var date = new Date();
16                  todo.set("finishedDate", date);
17                  todo.save(null, {
18                      useMasterKey: true,
19                      success: function (object) {
20                          response.success([todo]);
21                      },
22                      error: function (object, error) {
23                          response.error("Got an error " + error.code + " : " + error.description);
24                      }
25                  });
26              } else {
27                  response.error("ToDo not found to update");
28              }
29
30          },
31          error: function (error) {
32              response.error("- Error - " + error.code + " " + error.message);
33          }
34      });
35  });
```
:::



- 2 . Live Queries - sometimes you need to use Parse’s Live Query feature for something like a live chat app. You will want to use the live query to see when new messages for your user are created. Live Query is basically just Parse’s way of using sockets to get live updates. It’s pretty handy but it will not work with a class who’s FIND permissions have been turned off. So in this case we will turn the FIND permissions back on for the Message class and instead we will assign ACL’s for that message directly. The ACL should be set so that only the recipient can use a FIND to get the message from the server. Then you run your PF Live Query in your client looking for messages for your user and it will work flawlessly. If you are dealing with group messages, it’s a bit different. You can assign multiple people to be on the ACL but, it really doesn’t scale. Instead, there is a better way. You set the ACL to be based on a Role - Parse.Role - and then any user you want to have access to that message you just assign them to that Parse.Role. If you want to stop them from reading the messages for that group, you remove them from that role. This is way easier than removing them from every single message’s ACL and it scales for super large groups. This is the correct way to do it. I’m not going to leave a code sample for this as it’s too complex for this tutorial, but maybe I’ll explain how to do it in my next one. Thank you for reading this tutorial on security with Parse and Back4App. If you have questions feel free to [**contact me**](mailto\:iosdev22@gmail.com) and I’ll be happy to answer them.

Thanks! Joren
