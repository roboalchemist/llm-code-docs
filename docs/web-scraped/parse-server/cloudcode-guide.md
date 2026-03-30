# Source: https://docs.parseplatform.org/cloudcode/guide/

Title: Parse

URL Source: https://docs.parseplatform.org/cloudcode/guide/

Published Time: Sat, 07 Feb 2026 17:30:01 GMT

Markdown Content:
[](https://docs.parseplatform.org/cloudcode/guide/#cloud-functions)Cloud Functions
----------------------------------------------------------------------------------

Let’s look at a slightly more complex example where Cloud Code is useful. One reason to do computation in the cloud is so that you don’t have to send a huge list of objects down to a device if you only want a little bit of information. For example, let’s say you’re writing an app that lets people review movies. A single `Review` object could look like:

```
{
  "movie": "The Matrix",
  "stars": 5,
  "comment": "Too bad they never made any sequels."
}
```

If you wanted to find the average number of stars for The Matrix, you could query for all of the reviews, and average the stars on the device. However, this uses a lot of bandwidth when you only need a single number. With Cloud Code, we can just pass up the name of the movie, and return the average star rating.

Cloud functions accept a JSON parameters dictionary on the `request` object, so we can use that to pass up the movie name. The entire Parse JavaScript SDK is available in the cloud environment, so we can use that to query over `Review` objects. Together, the code to implement `averageStars` looks like:

```
Parse.Cloud.define("averageStars", async (request) => {
  const query = new Parse.Query("Review");
  query.equalTo("movie", request.params.movie);
  const results = await query.find();
  let sum = 0;
  for (let i = 0; i < results.length; ++i) {
    sum += results[i].get("stars");
  }
  return sum / results.length;
});
```

The only difference between using `averageStars` and `hello` is that we have to provide the parameter that will be accessed in `request.params.movie` when we call the Cloud function. Read on to learn more about how Cloud functions can be called.

Cloud functions can be called from any of the client SDKs, as well as through the REST API. For example, to call the Cloud function named `averageStars` with a parameter named `movie` from an Android app:

```
HashMap<String, Object> params = new HashMap<String, Object>();
params.put("movie", "The Matrix");
ParseCloud.callFunctionInBackground("averageStars", params, new FunctionCallback<Float>() {
   void done(Float ratings, ParseException e) {
       if (e == null) {
          // ratings is 4.5
       }
   }
});
```

To call the same Cloud function from an iOS app:

```
// Objective-C
[PFCloud callFunctionInBackground:@"averageStars"
                   withParameters:@{@"movie": @"The Matrix"}
                            block:^(NSNumber *ratings, NSError *error) {
  if (!error) {
     // ratings is 4.5
  }
}];
```

```
// Swift
PFCloud.callFunction(inBackground: "averageRatings", withParameters: ["movie":"The Matrix"]) {
	(response, error) in
	let ratings = response as? Float
	// ratings is 4.5
}
```

This is how you would call the same Cloud function using PHP:

```
$ratings = ParseCloud::run("averageRatings", ["movie" => "The Matrix"]);
// $ratings is 4.5
```

The following example shows how you can call the “averageRatings” Cloud function from a .NET C# app such as in the case of Windows 10, Unity, and Xamarin applications:

```
IDictionary<string, object> params = new Dictionary<string, object>
{
    { "movie", "The Matrix" }
};
ParseCloud.CallFunctionAsync<IDictionary<string, object>>("averageStars", params).ContinueWith(t => {
  var ratings = t.Result;
  // ratings is 4.5
});
```

You can also call Cloud functions using the REST API:

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{ "movie": "The Matrix" }' \
  https://YOUR.PARSE-SERVER.HERE/parse/functions/averageStars
```

And finally, to call the same function from a JavaScript app:

```
const params =  { movie: "The Matrix" };
const ratings = await Parse.Cloud.run("averageStars", params);
// ratings should be 4.5
```

In general, these arguments will be passed into Cloud Functions:

1.   **`request`** - The request object contains information about the request. The following fields are set:
2.   **`params`** - The parameters object sent to the function by the client.
3.   **`user`** - The `Parse.User` that is making the request. This will not be set if there was no logged-in user.

If the function is successful, the response in the client looks like:

```
{ "result": 4.8 }
```

If there is an error, the response in the client looks like:

```
{
  "code": 141,
  "error": "movie lookup failed"
}
```

[](https://docs.parseplatform.org/cloudcode/guide/#implementing-cloud-function-validation)Implementing cloud function validation
--------------------------------------------------------------------------------------------------------------------------------

_Available only on parse-server cloud code starting 4.4.0_

It’s important to make sure the parameters required for a Cloud function are provided, and are in the necessary format. Starting with Parse Server 4.4.0, you can now specify a validator function or object which will be called prior to your cloud function.

Let’s take a look at the `averageStars` example. If you wanted to make sure that `request.params.movie` is provided, and `averageStars` can only be called by logged in users, you could add a validator object to the function.

```
Parse.Cloud.define("averageStars", async (request) => {
  const query = new Parse.Query("Review");
  query.equalTo("movie", request.params.movie);
  const results = await query.find();
  let sum = 0;
  for (let i = 0; i < results.length; ++i) {
    sum += results[i].get("stars");
  }
  return sum / results.length;
},{
  fields : ['movie'],
  requireUser: true
});
```

If the rules specified in the validator object aren’t met, the Cloud Function won’t run. This means that you can confidently build your function, knowing that `request.params.movie` is defined, as well as `request.user`.

### [](https://docs.parseplatform.org/cloudcode/guide/#more-advanced-validation)More Advanced Validation

Often, not only is it important that `request.params.movie` is defined, but also that it’s the correct data type. You can do this by providing an `Object` to the `fields` parameter in the Validator.

```
Parse.Cloud.define("averageStars", async (request) => {
  const query = new Parse.Query("Review");
  query.equalTo("movie", request.params.movie);
  const results = await query.find();
  let sum = 0;
  for (let i = 0; i < results.length; ++i) {
    sum += results[i].get("stars");
  }
  return sum / results.length;
},{
  fields : {
    movie : {
      required: true,
      type: String,
      options: val => {
        return val.length < 20;
      },
      error: "Movie must be less than 20 characters"
    }
  },
  requireUserKeys: {
    accType : {
      options: 'reviewer',
      error: 'Only reviewers can get average stars'
    }
  }
});
```

This function will only run if:

*   `request.params.movie` is defined
*   `request.params.movie` is a String
*   `request.params.movie` is less than 20 characters
*   `request.user` is defined
*   `request.user.get('accType')` is defined
*   `request.user.get('accType')` is equal to ‘reviewer’

However, the requested user could set ‘accType’ to reviewer, and then recall the function. Here, you could provide validation on a `Parse.User``beforeSave` trigger. `beforeSave` validators have a few additional options available, to help you make sure your data is secure.

```
Parse.Cloud.beforeSave(Parse.User, () => {
  // any additional beforeSave logic here
}, {
    fields: {
      accType: {
        default: 'viewer',
        constant: true
      },
    },
});
```

This means that the field `accType` on `Parse.User` will be ‘viewer’ on signup, and will be unchangable, unless `masterKey` is provided.

The full range of built-in Validation Options are:

*   `requireMaster`: whether the function requires a `masterKey` to run.
*   `requireUser`: whether the function requires a `request.user` to run.
*   `validateMasterKey`: whether the validator should run on `masterKey` (defaults to false).
*   `fields`: an `Array` or `Object` of fields that are required on the request.
*   `requireAnyUserRoles`: an `Array` or `function` that returns an array. `request.user` must match one of the specified roles.
*   `requireAllUserRoles`: an `Array` or `function` that returns an array. `request.user` must match all of the specified roles.
*   `requireUserKeys`: an `Array` of fields to be validated on `request.user`.

The full range of built-in Validation Options on `.fields` are:

*   `type`: the type of the `request.params[field]` or `request.object.get(field)`.
*   `default`: what the field should default to if it’s `null`.
*   `required`: whether the field is required.
*   `options`: a singular option, array of options, or custom function of allowed values for the field.
*   `constant`: whether the field is immutable.
*   `error`: a custom error message if validation fails.

You can also pass a function to the Validator. This can help you apply reoccuring logic to your Cloud Code.

```
const validationRules = request => {
  if (request.master) {
    return;
  }
  if (!request.user || request.user.id !== 'masterUser') {
    throw 'Unauthorized';
  }
}

Parse.Cloud.define('adminFunction', request => {
// do admin code here, confident that request.user.id is masterUser, or masterKey is provided
},validationRules)

Parse.Cloud.define('adminFunctionTwo', request => {
// do admin code here, confident that request.user.id is masterUser, or masterKey is provided
},validationRules)
```

### [](https://docs.parseplatform.org/cloudcode/guide/#considerations)Considerations

*   The validation function will run prior to your Cloud Code Functions. You can use async and promises here, but try to keep the validation as simple and fast as possible so your cloud requests resolve quickly.
*   As previously mentioned, cloud validator objects will not validate if a masterKey is provided, unless `validateMasterKey:true` is set. However, if you set your validator to a function, the function will **always** run.

This range of options should help you write more secure Cloud Code. If you need help in any way, feel free to reach out on our [developer supported community forum](https://community.parseplatform.org/).

[](https://docs.parseplatform.org/cloudcode/guide/#cloud-jobs)Cloud Jobs
------------------------------------------------------------------------

Sometimes you want to execute long running functions, and you don’t want to wait for the response. Cloud Jobs are meant for just that.

[](https://docs.parseplatform.org/cloudcode/guide/#define-a-job)Define a Job
----------------------------------------------------------------------------

```
Parse.Cloud.job("myJob", (request) =>  {
      // params: passed in the job call
      // headers: from the request that triggered the job
      // log: the ParseServer logger passed in the request
      // message: a function to update the status message of the job object
      const { params, headers, log, message } = request;
      message("I just started");
      return doSomethingVeryLong(request);
    });
```

[](https://docs.parseplatform.org/cloudcode/guide/#running-a-job)Running a Job
------------------------------------------------------------------------------

Calling jobs is done via the REST API and is protected by the master key.

```
curl -X POST -H 'X-Parse-Application-Id: appId' -H 'X-Parse-Master-Key: masterKey' https://my-parse-server.com/parse/jobs/myJob
```

The response will consist of an empty body and contain the `X-Parse-Job-Status-Id: a1c3e5g7i9k` header. With the _JobStatus’s objectId that has just been created.

You can pass some data alongside the call if you want to customize the job execution.

[](https://docs.parseplatform.org/cloudcode/guide/#scheduling-a-job)Scheduling a Job
------------------------------------------------------------------------------------

We don’t support at the moment job scheduling and highly recommend to use a 3rd party system for scheduling your jobs.

*   On [AWS Elastic Beanstalk](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features-managing-env-tiers.html#worker-periodictasks)
*   On [Google App Engine](https://cloud.google.com/appengine/docs/flexible/nodejs/scheduling-jobs-with-cron-yaml)
*   On [Heroku](https://devcenter.heroku.com/articles/scheduler#scheduling-jobs)

[](https://docs.parseplatform.org/cloudcode/guide/#viewing-jobs)Viewing Jobs
----------------------------------------------------------------------------

Viewing jobs is supported on parse-dashboard starting version 1.0.19, but you can also query the _JobStatus class with a masterKey call to fetch your recent jobs.

[](https://docs.parseplatform.org/cloudcode/guide/#save-triggers)Save Triggers
------------------------------------------------------------------------------

[](https://docs.parseplatform.org/cloudcode/guide/#beforesave)beforeSave
------------------------------------------------------------------------

### [](https://docs.parseplatform.org/cloudcode/guide/#implementing-data-validation)Implementing data validation

Another reason to run code in the cloud is to enforce a particular data format. For example, you might have both an Android and an iOS app, and you want to validate data for each of those. Rather than writing code once for each client environment, you can write it just once with Cloud Code.

Let’s take a look at our movie review example. When you’re choosing how many stars to give something, you can typically only give 1, 2, 3, 4, or 5 stars. You can’t give -6 stars or 1337 stars in a review. If we want to reject reviews that are out of bounds, we can do this with the `beforeSave` method:

```
Parse.Cloud.beforeSave("Review", (request) => {
// do any additional beforeSave logic here
},{
  fields: {
    stars : {
      required:true,
      options: stars => {
        return stars >= 1 && stars =< 5;
      },
      error: 'Your review must be between one and five stars'
    }
  }
});
```

If the function throws, the `Review` object will not be saved, and the client will get an error. If nothing is thrown the object will be saved normally.

One useful tip is that even if your mobile app has many different versions, the same version of Cloud Code applies to all of them. Thus, if you launch an application that doesn’t correctly check the validity of input data, you can still fix this problem by adding a validation with `beforeSave`.

### [](https://docs.parseplatform.org/cloudcode/guide/#modifying-objects-on-save)Modifying Objects on Save

In some cases, you don’t want to throw out invalid data. You just want to tweak it a bit before saving it. `beforeSave` can handle this case, too. Any adjustment you make to request.object will be saved.

In our movie review example, we might want to ensure that comments aren’t too long. A single long comment might be tricky to display. We can use `beforeSave` to truncate the `comment` field to 140 characters:

```
Parse.Cloud.beforeSave("Review", (request) => {
  const comment = request.object.get("comment");
  if (comment.length > 140) {
    // Truncate and add a ...
    request.object.set("comment", comment.substring(0, 137) + "...");
  }
});
```

### [](https://docs.parseplatform.org/cloudcode/guide/#predefined-classes)Predefined Classes

If you want to use `beforeSave` for a predefined class in the Parse JavaScript SDK (e.g. [Parse.User](https://parseplatform.org/Parse-SDK-JS/api/classes/Parse.User.html)), you should not pass a String for the first argument. Instead, you should pass the class itself, for example:

```
Parse.Cloud.beforeSave(Parse.User, async (request) => {
    // code here
},
  // Validation Object or Validation Function
)
```

[](https://docs.parseplatform.org/cloudcode/guide/#aftersave)afterSave
----------------------------------------------------------------------

In some cases, you may want to perform some action, such as a push, after an object has been saved. You can do this by registering a handler with the `afterSave` method. For example, suppose you want to keep track of the number of comments on a blog post. You can do that by writing a function like this:

```
Parse.Cloud.afterSave("Comment", (request) => {
  const query = new Parse.Query("Post");
  query.get(request.object.get("post").id)
    .then(function(post) {
      post.increment("comments");
      return post.save();
    })
    .catch(function(error) {
      console.error("Got an error " + error.code + " : " + error.message);
    });
});
```

### [](https://docs.parseplatform.org/cloudcode/guide/#async-behavior)Async Behavior

In the example above, the client will receive a successful response before the promise in the handler completes, regardless of how the promise resolves. For instance, the client will receive a successful response even if the handler throws an exception. Any errors that occurred while running the handler can be found in the Cloud Code log.

You can use an `afterSave` handler to perform lengthy operations after sending a response back to the client. In order to respond to the client before the `afterSave` handler completes, your handler may not return a promise and your `afterSave` handler may not use async/await.

### [](https://docs.parseplatform.org/cloudcode/guide/#predefined-classes-1)Predefined Classes

If you want to use `afterSave` for a predefined class in the Parse JavaScript SDK (e.g. [Parse.User](https://parseplatform.org/Parse-SDK-JS/api/classes/Parse.User.html)), you should not pass a String for the first argument. Instead, you should pass the class itself, for example:

```
Parse.Cloud.afterSave(Parse.User, async (request) => {
    // code here
})
```

[](https://docs.parseplatform.org/cloudcode/guide/#context)Context
------------------------------------------------------------------

When saving a `Parse.Object` you may pass a `context` dictionary that is accessible in the Cloud Code Save Triggers. More info in the [JavaScript Guide](https://docs.parseplatform.org/js/guide/#cloud-code-context).

The context is also passed from a `beforeSave` handler to an `afterSave` handler. The following example sends emails to users who are being added to a [Parse.Role’s users relation](https://parseplatform.org/Parse-SDK-JS/api/2.1.0/Parse.Role.html#getUsers) asynchronously, so the client receives a response before the emails complete sending:

```
const beforeSave = function beforeSave(request) {
  const { object: role } = request;
  // Get users that will be added to the users relation.
  const usersOp = role.op('users');
  if (usersOp && usersOp.relationsToAdd.length > 0) {
    // add the users being added to the request context
    request.context = { buyers: usersOp.relationsToAdd };
  }
};

const afterSave = function afterSave(request) {
  const { object: role, context } = request;
  if (context && context.buyers) {
    const purchasedItem = getItemFromRole(role);
    const promises = context.buyers.map(emailBuyer.bind(null, purchasedItem));
    item.increment('orderCount', context.buyers.length);
    promises.push(item.save(null, { useMasterKey: true }));
    Promise.all(promises).catch(request.log.error.bind(request.log));
  }
};
```

[](https://docs.parseplatform.org/cloudcode/guide/#delete-triggers)Delete Triggers
----------------------------------------------------------------------------------

[](https://docs.parseplatform.org/cloudcode/guide/#beforedelete)beforeDelete
----------------------------------------------------------------------------

You can run custom Cloud Code before an object is deleted. You can do this with the `beforeDelete` method. For instance, this can be used to implement a restricted delete policy that is more sophisticated than what can be expressed through [ACLs](https://parseplatform.org/Parse-SDK-JS/api//classes/Parse.ACL.html). For example, suppose you have a photo album app, where many photos are associated with each album, and you want to prevent the user from deleting an album if it still has a photo in it. You can do that by writing a function like this:

```
Parse.Cloud.beforeDelete("Album", async (request) => {
  const query = new Parse.Query("Photo");
  query.equalTo("album", request.object);
  const count = await query.count({useMasterKey:true})
  if (count > 0) {
    throw "Can't delete album if it still has photos.";
  }
});
```

If the function throws, the `Album` object will not be deleted, and the client will get an error. Otherwise,the object will be deleted normally.

### [](https://docs.parseplatform.org/cloudcode/guide/#predefined-classes-2)Predefined Classes

If you want to use `beforeDelete` for a predefined class in the Parse JavaScript SDK (e.g. [Parse.User](https://parseplatform.org/Parse-SDK-JS/api/classes/Parse.User.html)), you should not pass a String for the first argument. Instead, you should pass the class itself, for example:

```
Parse.Cloud.beforeDelete(Parse.User, async (request) => {
    // code here
})
```

[](https://docs.parseplatform.org/cloudcode/guide/#afterdelete)afterDelete
--------------------------------------------------------------------------

In some cases, you may want to perform some action, such as a push, after an object has been deleted. You can do this by registering a handler with the `afterDelete` method. For example, suppose that after deleting a blog post, you also want to delete all associated comments. You can do that by writing a function like this:

```
Parse.Cloud.afterDelete("Post", (request) => {
  const query = new Parse.Query("Comment");
  query.equalTo("post", request.object);
  query.find()
    .then(Parse.Object.destroyAll)
    .catch((error) => {
      console.error("Error finding related comments " + error.code + ": " + error.message);
    });
});
```

The `afterDelete` handler can access the object that was deleted through `request.object`. This object is fully fetched, but cannot be refetched or resaved.

The client will receive a successful response to the delete request after the handler terminates, regardless of how the `afterDelete` terminates. For instance, the client will receive a successful response even if the handler throws an exception. Any errors that occurred while running the handler can be found in the Cloud Code log.

### [](https://docs.parseplatform.org/cloudcode/guide/#predefined-classes-3)Predefined Classes

If you want to use `afterDelete` for a predefined class in the Parse JavaScript SDK (e.g. [Parse.User](https://parseplatform.org/Parse-SDK-JS/api/classes/Parse.User.html)), you should not pass a String for the first argument. Instead, you should pass the class itself, for example:

```
Parse.Cloud.afterDelete(Parse.User, async (request) => {
    // code here
})
```

[](https://docs.parseplatform.org/cloudcode/guide/#file-triggers)File Triggers
------------------------------------------------------------------------------

[](https://docs.parseplatform.org/cloudcode/guide/#beforesave-1)beforeSave
--------------------------------------------------------------------------

With the `beforeSave` method you can run custom Cloud Code before any file is saved. Returning a new `Parse.File` will save the new file instead of the one sent by the client.

### [](https://docs.parseplatform.org/cloudcode/guide/#examples)Examples

```
// Changing the file name
Parse.Cloud.beforeSave(Parse.File, async (request) => {
  const { file } = request;
  const fileData = await file.getData();
  const newFile = new Parse.File('a-new-file-name.txt', { base64: fileData });
  return newFile;
});

// Returning an already saved file
Parse.Cloud.beforeSave(Parse.File, (request) => {
  const { user } = request;
  const avatar = user.get('avatar'); // this is a Parse.File that is already saved to the user object
  return avatar;
});

// Saving a different file from uri
Parse.Cloud.beforeSave(Parse.File, (request) => {
  const newFile = new Parse.File('some-file-name.txt', { uri: 'www.somewhere.com/file.txt' });
  return newFile;
});
```

### [](https://docs.parseplatform.org/cloudcode/guide/#metadata-and-tags)Metadata and Tags

Adding Metadata and Tags to your files allows you to add additional bits of data to the files that are stored within your storage solution (i.e AWS S3). The `beforeSave` hook is a great place to set the metadata and/or tags on your files.

Note: not all storage adapters support metadata and tags. Check the documentation for the storage adapter you’re using for compatibility.

```
// Adding metadata and tags
Parse.Cloud.beforeSave(Parse.File, (request) => {
  const { file, user } = request;
  file.addMetadata('createdById', user.id);
  file.addTag('groupId', user.get('groupId'));
});
```

[](https://docs.parseplatform.org/cloudcode/guide/#aftersave-1)afterSave
------------------------------------------------------------------------

The `afterSave` method is a great way to keep track of all of the files stored in your app. For example:

```
Parse.Cloud.afterSave(Parse.File, async (request) => {
  const { file, fileSize, user } = request;
  const fileObject = new Parse.Object('FileObject');
  fileObject.set('file', file);
  fileObject.set('fileSize', fileSize);
  fileObject.set('createdBy', user);
  const token = { sessionToken: user.getSessionToken() };
  await fileObject.save(null, token);
});
```

[](https://docs.parseplatform.org/cloudcode/guide/#beforedelete-1)beforeDelete
------------------------------------------------------------------------------

You can run custom Cloud Code before any file gets deleted. For example, lets say you want to add logic that only allows files to be deleted by the user who created it. You could use a combination of the `afterSave` and the `beforeDelete` methods as follows:

```
Parse.Cloud.afterSave(Parse.File, async (request) => {
  const { file, user } = request;
  const fileObject = new Parse.Object('FileObject');
  fileObject.set('fileName', file.name());
  fileObject.set('createdBy', user);
  await fileObject.save(null, { useMasterKey: true );
});

Parse.Cloud.beforeDelete(Parse.File, async (request) => {
  const { file, user } = request;
  const query = new Parse.Query('FileObject');
  query.equalTo('fileName', file.name());
  const fileObject = await query.first({ useMasterKey: true });
  if (fileObject.get('createdBy').id !== user.id) {
    throw 'You do not have permission to delete this file';
  }
});
```

[](https://docs.parseplatform.org/cloudcode/guide/#afterdelete-1)afterDelete
----------------------------------------------------------------------------

In the above `beforeDelete` example the `FileObject` collection is used to keep track of saved files in your app. The `afterDelete` trigger is a good place to clean up these objects once a file has been successfully deleted.

```
Parse.Cloud.afterDelete(Parse.File, async (request) => {
  const { file } = request;
  const query = new Parse.Query('FileObject');
  query.equalTo('fileName', file.name());
  const fileObject = await query.first({ useMasterKey: true });
  await fileObject.destroy({ useMasterKey: true });
});
```

[](https://docs.parseplatform.org/cloudcode/guide/#beforefind)beforeFind
------------------------------------------------------------------------

_Available only on parse-server cloud code starting 8.1.0_

The beforeFind trigger allows you to intercept file retrieval requests and perform logic before the file is served. This is useful for adding access control, logging, or modifying the file’s response behavior.

```
Parse.Cloud.beforeFind(Parse.File, (request) => {
  const { file, user, log } = request;
  log.info(`User ${user.id} is trying to access file ${file.name()}`);
  if (!user || !user.get('isAdmin')) {
    throw 'Access denied: only admins can view this file';
  }
});
```

[](https://docs.parseplatform.org/cloudcode/guide/#afterfind)afterFind
----------------------------------------------------------------------

_Available only on parse-server cloud code starting 8.1.0_

The afterFind trigger allows you to modify the behavior of a file download after it has been retrieved. For example, you can enforce a forced download of the file or log usage statistics.

```
Parse.Cloud.afterFind(Parse.File, (request) => {
  const { file, log } = request;
  log.info(`File ${file.name()} was served to the user.`);
  if (file.name().endsWith('.txt')) {
    request.forceDownload = true;
  }
});
```

[](https://docs.parseplatform.org/cloudcode/guide/#find-triggers)Find Triggers
------------------------------------------------------------------------------

[](https://docs.parseplatform.org/cloudcode/guide/#beforefind-1)beforeFind
--------------------------------------------------------------------------

_Available only on parse-server cloud code starting 2.2.20_

In some cases you may want to transform an incoming query, adding an additional limit or increasing the default limit, adding extra includes or restrict the results to a subset of keys. You can do so with the `beforeFind` trigger.

### [](https://docs.parseplatform.org/cloudcode/guide/#examples-1)Examples

```
// Properties available
Parse.Cloud.beforeFind('MyObject', (req) => {
  let query = req.query; // the Parse.Query
  let user = req.user; // the user
  let triggerName = req.triggerName; // beforeFind
  let isMaster = req.master; // if the query is run with masterKey
  let isCount = req.count; // if the query is a count operation (available on parse-server 2.4.0 or up)
  let logger = req.log; // the logger
  let installationId = req.installationId; // The installationId
});

// Selecting keys
Parse.Cloud.beforeFind('MyObject', (req) => {
  let query = req.query; // the Parse.Query
  // Force the selection on some keys
  query.select(['key1', 'key2']);
});

// Asynchronous support
Parse.Cloud.beforeFind('MyObject', (req) => {
  let query = req.query;
  return aPromise().then((results) => {
    // do something with the results
    query.containedIn('key', results);
  });
});

// Returning a different query
Parse.Cloud.beforeFind('MyObject', (req) => {
  let query = req.query;
  let otherQuery = new Parse.Query('MyObject');
  otherQuery.equalTo('key', 'value');
  return Parse.Query.or(query, otherQuery);
});

// Rejecting a query
Parse.Cloud.beforeFind('MyObject', (req) =>  {
  // throw an error
  throw new Parse.Error(101, 'error');

  // rejecting promise
  return Promise.reject('error');
});

// Setting the read preference for a query
// -- as of Parse Server 2.5, Mongo Only
Parse.Cloud.beforeFind('MyObject2', (req) => {
  req.readPreference = 'SECONDARY_PREFERRED';
  req.subqueryReadPreference = 'SECONDARY';
  req.includeReadPreference = 'PRIMARY';
});
```

### [](https://docs.parseplatform.org/cloudcode/guide/#predefined-classes-4)Predefined Classes

If you want to use `beforeFind` for a predefined class in the Parse JavaScript SDK (e.g. [Parse.User](https://parseplatform.org/Parse-SDK-JS/api/classes/Parse.User.html)), you should not pass a String for the first argument. Instead, you should pass the class itself, for example:

```
Parse.Cloud.beforeFind(Parse.User, async (request) => {
    // code here
})
```

[](https://docs.parseplatform.org/cloudcode/guide/#afterfind-1)afterFind
------------------------------------------------------------------------

_Available only on parse-server cloud code starting 2.2.25_

In some cases you may want to manipulate the results of a query before they are sent to the client. You can do so with the `afterFind` trigger.

```
Parse.Cloud.afterFind('MyCustomClass', async (request) => {
    // code here
})
```

### [](https://docs.parseplatform.org/cloudcode/guide/#predefined-classes-5)Predefined Classes

If you want to use `afterFind` for a predefined class in the Parse JavaScript SDK (e.g. [Parse.User](https://parseplatform.org/Parse-SDK-JS/api/classes/Parse.User.html)), you should not pass a String for the first argument. Instead, you should pass the class itself, for example:

```
Parse.Cloud.afterFind(Parse.User, async (request) => {
    // code here
})
```

[](https://docs.parseplatform.org/cloudcode/guide/#session-triggers)Session Triggers
------------------------------------------------------------------------------------

[](https://docs.parseplatform.org/cloudcode/guide/#beforelogin)beforeLogin
--------------------------------------------------------------------------

_Available only on parse-server cloud code starting 3.3.0_

Sometimes you may want to run custom validation on a login request. The `beforeLogin` trigger can be used for blocking an account from logging in (for example, if they are banned), recording a login event for analytics, notifying user by email if a login occurred at an unusual IP address and more.

```
Parse.Cloud.beforeLogin(async request => {
  const { object: user }  = request;
  if(user.get('isBanned')) {
   throw new Error('Access denied, you have been banned.')
  }
});
```

### [](https://docs.parseplatform.org/cloudcode/guide/#considerations-1)Considerations

*   It waits for any promises to resolve
*   The user is not available on the request object - the user has not yet been provided a session until after beforeLogin is successfully completed
*   Like `afterSave` on `Parse.User`, it will not save mutations to the user unless explicitly saved

#### [](https://docs.parseplatform.org/cloudcode/guide/#the-trigger-will-run)The trigger will run…

*   On username & password logins
*   On `authProvider` logins

#### [](https://docs.parseplatform.org/cloudcode/guide/#the-trigger-wont-run)The trigger won’t run…

*   On sign up
*   If the login credentials are incorrect

[](https://docs.parseplatform.org/cloudcode/guide/#afterlogout)afterLogout
--------------------------------------------------------------------------

_Available only on parse-server cloud code starting 3.10.0_

Sometimes you may want to run actions after a user logs out. For example, the `afterLogout` trigger can be used for clean-up actions after a user logs out. The triggers contains the session object that has been deleted on logout. From this session object you can determine the user who logged out to perform user-specific tasks.

```
Parse.Cloud.afterLogout(async request => {
  const { object: session }  = request;
  const user = session.get('user');
  user.set('isOnline', false);
  user.save(null,{useMasterKey:true});
});
```

### [](https://docs.parseplatform.org/cloudcode/guide/#considerations-2)Considerations

*   Like with `afterDelete` triggers, the `_Session` object that is contained in the request has already been deleted.

#### [](https://docs.parseplatform.org/cloudcode/guide/#the-trigger-will-run-1)The trigger will run…

*   when the user logs out and a `_Session` object was deleted

### [](https://docs.parseplatform.org/cloudcode/guide/#the-trigger-wont-run-1)The trigger won’t run…

*   if a user logs out and no `_Session` object was found to delete
*   if a `_Session` object is deleted without the user logging out by calling the logout method of an SDK

[](https://docs.parseplatform.org/cloudcode/guide/#beforepasswordresetrequest)beforePasswordResetRequest
--------------------------------------------------------------------------------------------------------

_Available only in Cloud Code on Parse Server >= 8.5.0._

The `beforePasswordResetRequest` trigger is invoked before a password reset email is sent. It is triggered after the user is found by email, but before the reset token is generated and the email is sent. It can be used for blocking password reset requests, implementing rate limiting, or adding additional validation logic.

An example would be to prevent sending a password reset email if the user has a ban flag set in your application.

```
Parse.Cloud.beforePasswordResetRequest(request => {
  if (request.object.get('banned')) {
    throw new Parse.Error(Parse.Error.EMAIL_NOT_FOUND, 'User is banned.');
  }
});
```

You can also add rate limiting to prevent abuse of the password reset endpoint:

```
Parse.Cloud.beforePasswordResetRequest(async request => {
  if (request.object.get('banned')) {
    throw new Parse.Error(Parse.Error.EMAIL_NOT_FOUND, 'User is banned.');
  }
}, {
  rateLimit: {
    requestLimit: 5,
    windowMs: 60_000
  }
});
```

Considerations:

*   The user object is available on `request.object`, which is the user who requested the password reset.
*   If the function throws an error, the password reset email will not be sent.

The trigger will run:

*   When a password reset is requested via `/requestPasswordReset` endpoint.
*   After the user is found by email address.
*   Before the reset token is generated and the email is sent.

The trigger won’t run:

*   If the email address doesn’t match any user in the system.

[](https://docs.parseplatform.org/cloudcode/guide/#livequery-triggers)LiveQuery Triggers
----------------------------------------------------------------------------------------

[](https://docs.parseplatform.org/cloudcode/guide/#beforeconnect)beforeConnect
------------------------------------------------------------------------------

_Available only on parse-server cloud code starting 4.3.0_

You can run custom Cloud Code before a user attempts to connect to your LiveQuery server with the `beforeConnect` method. For instance, this can be used to only allow users that have logged in to connect to the LiveQuery server.

```
Parse.Cloud.beforeConnect(request => {
  if (!request.user) {
    throw "Please login before you attempt to connect."
  }
});
```

In most cases, the `connect` event is called the first time the client calls `subscribe`. If this is your use case, you can listen for errors using this event.

```
Parse.LiveQuery.on('error', (error) => {
  console.log(error);
});
```

[](https://docs.parseplatform.org/cloudcode/guide/#beforesubscribe)beforeSubscribe
----------------------------------------------------------------------------------

_Available only on parse-server cloud code starting 4.3.0_

In some cases you may want to transform the incoming subscription query. Examples include adding an additional limit, increasing the default limit, adding extra includes or restricting the results to a subset of keys. You can do so with the `beforeSubscribe` trigger.

```
Parse.Cloud.beforeSubscribe('MyObject', request => {
    if (!request.user.get('Admin')) {
        throw new Parse.Error(101, 'You are not authorized to subscribe to MyObject.');
    }
    let query = request.query; // the Parse.Query
    query.select("name","year")
});
```

[](https://docs.parseplatform.org/cloudcode/guide/#afterlivequeryevent)afterLiveQueryEvent
------------------------------------------------------------------------------------------

_Available only on parse-server cloud code starting 4.4.0_

In some cases you may want to manipulate the results of a Live Query before they are sent to the client. You can do so with the `afterLiveQueryEvent` trigger.

### [](https://docs.parseplatform.org/cloudcode/guide/#examples-2)Examples

```
// Changing values on object and original
Parse.Cloud.afterLiveQueryEvent('MyObject', request => {
  const object = request.object;
  object.set('name', '***');

  const original = request.original;
  original.set('name', 'yolo');
});

// Prevent LiveQuery trigger unless 'foo' is modified
Parse.Cloud.afterLiveQueryEvent('MyObject', (request) => {
  const object = request.object;
  const original = request.original;
  if (!original) {
    return;
  }
  if (object.get('foo') != original.get('foo')) {
    request.sendEvent = false;
  }
});
```

By default, ParseLiveQuery does not perform queries that require additional database operations. This is to keep your Parse Server as fast and efficient as possible. If you require this functionality, you can perform these in `afterLiveQueryEvent`.

```
// Including an object on LiveQuery event, on update only.
Parse.Cloud.afterLiveQueryEvent('MyObject', async (request) => {
  if (request.event != "update") {
    request.sendEvent = false;
    return;
  }
  const object = request.object;
  const pointer = object.get("child");
  await pointer.fetch();
});

// Extend matchesQuery functionality to LiveQuery
Parse.Cloud.afterLiveQueryEvent('MyObject', async (request) => {
  if (request.event != "create") {
    return;
  }
  const query = request.object.relation('children').query();
  query.equalTo('foo','bart');
  const first = await query.first();
  if (!first)  {
    request.sendEvent = false;
  }
});
```

### [](https://docs.parseplatform.org/cloudcode/guide/#considerations-3)Considerations

*   Live Query events won’t trigger until the `afterLiveQueryEvent` trigger has completed. Make sure any functions inside the trigger are efficient and restrictive to prevent bottlenecks.

[](https://docs.parseplatform.org/cloudcode/guide/#onlivequeryevent)onLiveQueryEvent
------------------------------------------------------------------------------------

_Available only on parse-server cloud code starting 2.6.2_

Sometimes you may want to monitor Live Query Events to be used with a 3rd Party such as datadog. The `onLiveQueryEvent` trigger can log events triggered, number of clients connected, number of subscriptions and errors.

```
Parse.Cloud.onLiveQueryEvent(({
  event,
  client,
  sessionToken,
  useMasterKey,
  installationId,
  clients,
  subscriptions,
  error
}) => {
  if (event !== 'ws_disconnect') {
    return;
  }
  // Do your magic
});
```

_client, sessionToken, useMasterKey and installationId are available on parse-server cloud code 3.8.0+_

To learn more, read the [Parse LiveQuery Protocol Specification](https://github.com/parse-community/parse-server/wiki/Parse-LiveQuery-Protocol-Specification)

[](https://docs.parseplatform.org/cloudcode/guide/#events)Events
----------------------------------------------------------------

*   connect
*   subscribe
*   unsubscribe
*   ws_connect
*   ws_disconnect
*   ws_disconnect_error

“connect” differs from “ws_connect”, the former means that the client completed the connect procedure as defined by Parse Live Query protocol, where “ws_connect” just means that a new websocket was created.

[](https://docs.parseplatform.org/cloudcode/guide/#security)Security
--------------------------------------------------------------------

[](https://docs.parseplatform.org/cloudcode/guide/#master-key)Master Key
------------------------------------------------------------------------

To override object and class access permissions, you can set `useMasterKey: true` if the request accepts the master key option.

### [](https://docs.parseplatform.org/cloudcode/guide/#examples-3)Examples

```
query.find({ useMasterKey: true });
```

```
object.save(null, { useMasterKey: true });
```

```
Parse.Object.saveAll(objects, { useMasterKey: true });
```

### [](https://docs.parseplatform.org/cloudcode/guide/#considerations-4)Considerations

*   If you set `masterKey: true` when fetching objects with a query or relation in [Cloud Functions](https://docs.parseplatform.org/cloudcode/guide/#cloud-functions) or [Find Triggers](https://docs.parseplatform.org/cloudcode/guide/#find-triggers), the complete object will be returned. You may want to remove object properties that the client should not be able to access before sending it to the client.

[](https://docs.parseplatform.org/cloudcode/guide/#networking)Networking
------------------------------------------------------------------------

[](https://docs.parseplatform.org/cloudcode/guide/#httprequest)httpRequest
--------------------------------------------------------------------------

You can use your favorite npm module to make HTTP requests, such as [axios](https://www.npmjs.com/package/axios). Parse Server also supports `Parse.Cloud.httpRequest` for legacy reasons. It allows you to send HTTP requests to any HTTP Server. This function takes an options object to configure the call.

A simple GET request would look like:

```
Parse.Cloud.httpRequest({
  url: 'https://www.awesomewebsite.com/'
}).then(function(httpResponse) {
  // success
  console.log(httpResponse.text);
},function(httpResponse) {
  // error
  console.error('Request failed with response code ' + httpResponse.status);
});
```

`Parse.Cloud.httpRequest` returns a Promise that will be resolved on a successful http status code; otherwise the Promise will be rejected. In the above example, we use `then()` to handle both outcomes.

A GET request that specifies the port number would look like:

```
Parse.Cloud.httpRequest({
  url: 'https://www.awesomewebsite.com:8080/'
}).then(function(httpResponse) {
  console.log(httpResponse.text);
}, function(httpResponse) {
  console.error('Request failed with response code ' + httpResponse.status);
});
```

Valid port numbers are 80, 443, and all numbers from 1025 through 65535.

By default, `Parse.Cloud.httpRequest` does not follow redirects caused by HTTP 3xx response codes, the `followRedirects: true` option can be used to change this.

```
Parse.Cloud.httpRequest({
  url: 'https://www.awesomewebsite.com/',
  followRedirects: true
}).then(function(httpResponse) {
  console.log(httpResponse.text);
}, function(httpResponse) {
  console.error('Request failed with response code ' + httpResponse.status);
});
```

### [](https://docs.parseplatform.org/cloudcode/guide/#query-parameters)Query Parameters

You can specify query parameters to append to the end of the url by setting `params` on the options object. You can either pass a JSON object of key value pairs like:

```
Parse.Cloud.httpRequest({
  url: 'http://www.google.com/search',
  params: {
    q : 'Sean Plott'
  }
}).then(function(httpResponse) {
  console.log(httpResponse.text);
}, function(httpResponse) {
  console.error('Request failed with response code ' + httpResponse.status);
});
```

or as a raw `String` like this:

```
Parse.Cloud.httpRequest({
  url: 'http://www.google.com/search',
  params: 'q=Sean Plott'
}).then(function(httpResponse) {
  console.log(httpResponse.text);
}, function(httpResponse) {
  console.error('Request failed with response code ' + httpResponse.status);
});
```

You can send HTTP Headers by setting the `header` attribute of the options object. Let’s say you want set the Content-Type of the request, you can do:

```
Parse.Cloud.httpRequest({
  url: 'http://www.example.com/',
  headers: {
    'Content-Type': 'application/json;charset=utf-8'
  }
}).then(function(httpResponse) {
  console.log(httpResponse.text);
}, function(httpResponse) {
  console.error('Request failed with response code ' + httpResponse.status);
});
```

### [](https://docs.parseplatform.org/cloudcode/guide/#sending-a-post-request)Sending a POST Request

You can send a post request by setting the `method` attribute of the options object. The body of the POST can be set using the `body`. A simple example would be:

```
Parse.Cloud.httpRequest({
  method: 'POST',
  url: 'http://www.example.com/create_post',
  body: {
    title: 'Vote for Pedro',
    body: 'If you vote for Pedro, your wildest dreams will come true'
  }
}).then(function(httpResponse) {
  console.log(httpResponse.text);
}, function(httpResponse) {
  console.error('Request failed with response code ' + httpResponse.status);
});
```

This will send a post to `http://www.example.com/create_post` with body that is the url form encoded `body` attribute. If you want the body to be JSON encoded, you can instead do:

```
Parse.Cloud.httpRequest({
  method: 'POST',
  url: 'http://www.example.com/create_post',
  headers: {
    'Content-Type': 'application/json;charset=utf-8'
  },
  body: {
    title: 'Vote for Pedro',
    body: 'If you vote for Pedro, your wildest dreams will come true'
  }
}).then(function(httpResponse) {
  console.log(httpResponse.text);
}, function(httpResponse) {
  console.error('Request failed with response code ' + httpResponse.status);
});
```

To ensure that your HTTP request body is encoded correctly, please always include the charset in your Content-Type header.

### [](https://docs.parseplatform.org/cloudcode/guide/#following-redirects)Following Redirects

By default, `Parse.Cloud.httpRequest` does not follow redirects caused by HTTP 3xx response codes. You can use the `followRedirects` option to change this behavior to follow redirects:

```
Parse.Cloud.httpRequest({
  url: 'http://www.example.com/',
  followRedirects: true
}).then(function(httpResponse) {
  console.log(httpResponse.text);
}, function(httpResponse) {
  console.error('Request failed with response code ' + httpResponse.status);
});
```

### [](https://docs.parseplatform.org/cloudcode/guide/#the-response-object)The Response Object

The response object passed into the `success` and `error` will contain:

*   **`status`** - The HTTP Response status.
*   **`headers`** - The response headers
*   **`buffer`** - The raw byte representation of the response body.
*   **`text`** - The raw response body.
*   **`data`** - The parsed response, if Cloud Code knows how to parse the content-type that was sent.
*   **`cookies`** - The cookies sent by the server. They are [Parse.Cloud.Cookie](https://parseplatform.org/Parse-SDK-JS/api//classes/Parse.Cloud.HTTPResponse.html) objects.

[](https://docs.parseplatform.org/cloudcode/guide/#cloud-code-webhooks)Cloud Code Webhooks
------------------------------------------------------------------------------------------

Webhooks allow you to write your server-side logic in your own environment with any tools you wish to use. This can be useful if you want to use a language other than JavaScript, host it yourself for improved testing capabilities, or if you require a specialized library or technology not available in Cloud Code. Webhooks are currently available for `beforeSave`, `afterSave`, `beforeDelete`, `afterDelete`, and Cloud functions. To specify a new webhook, you can use the Parse Dashboard in the Webhooks section located under Core.

We’ve written an example Cloud Code Webhooks server, in Express.js, which you can find on Github: [CloudCodeWebhooks-Express](https://github.com/ParsePlatform/CloudCodeWebhooks-Express).

Note: At the current time, custom webhooks cannot be set for the special classes _User and _Installation.

[](https://docs.parseplatform.org/cloudcode/guide/#cloud-function-webhooks)Cloud Function Webhooks
--------------------------------------------------------------------------------------------------

A webhook request for a Cloud function will contain the following parameters:

*   **master**: True if the master key was used and false otherwise.
*   **user**: If set, this will contain the Parse User who made the request, in our REST API format. This is not set if the master key is used.
*   **installationId**: If available, the installationId which made the request.
*   **params**: A JSON object containing the parameters passed to the function. For example: `{ "foo": "bar" }`
*   **functionName**: The name of the Cloud function.

To respond to this request, send a JSON object with the key `error` or `success` set. In the case of `success`, send back any data your client will expect; or simply `true` if your client doesn’t require any data. In the case of `error`, the value provided should be the error message you want to return.

To create a webhook for a Cloud function, start by writing the function’s code on your own server. Here’s the simple hello world function written in a Rails environment.

```
# We need to disable CSRF protection for webhooks to work. Instead we
# use the webhook key to prove authenticity. protect_from_forgery :except => :index

def index
  # Ensure the request is authorized. You can find this key on your app's settings page
  # and you should ALWAYS validate it in your request.
  if request.headers['X-Parse-Webhook-Key'] !== @webhook_key
    return render :json => { :error => "Request Unauthorized"}
  end

  # Check the function name and return a message if it's correct
  if params[:functionName] == "helloWorld"
    return render :json => { :success => "Hello World!" }
  end

  # Return an error if it's not the function we expected
  return render :json => { :error => "Unknown function"}
end
```

Here’s an example of the JSON data that would be sent in the request to this webhook:

```
// Sent to webhook
{
  "master": false,
  "user": {
    "createdAt": "2015-03-24T20:19:00.542Z",
    "objectId": "lValKpphWN",
    "sessionToken": "orU3ClA7sqMIN8g4KtmLe7eDM",
    "updatedAt": "2015-03-24T20:19:00.542Z",
    "username": "Matt"
  },
  "installationId": "b3ab24c6-2282-69fa-eeea-c1b36ea497c2",
  "params": {},
  "functionName": "helloWorld"
}
```

This response would indicate a success in the webhook:

```
// Returned from the webhook on success
{ "success": "Hello World!" }
```

This response would indicate an error in the webhook:

```
// Returned from the webhook on error
{ "error": "Error message >:(" }
```

You can activate this webhook from the Dashboard UI.

![Image 1](https://docs.parseplatform.org/assets/images/new_webhook.png)

Once the webhook is set, you can call it from any of our SDKs or from the REST API, the same way you would a normal Cloud function.

Here’s a more complex example where we use a webhook to perform some task for our billing pipeline. We’ll use the popular `resque` gem to enqueue a job that handles billing the given user. For this example, the function is named `chargeCustomer` and it should always be called with the master key.

```
# We need to disable CSRF protection for webhooks to work. Instead we
# use the webhook key to prove authenticity.
protect_from_forgery :except => :index

def index
  # Ensure the request is validated
  if request.headers['X-Parse-Webhook-Key'] !== @webhook_key
    return render :json => { :error => "Request Unauthorized"}
  end

  # Check the function name
  if params[:functionName] == "chargeCustomer" && params[:master] == true
    # extract the custom parameters sent with the function
    custom_params = params[:params]
    user_id = custom_params["userObjectId"]

    # enqueue a resque job to bill the user
    Resque.enqueue(BillingJob, user_id)

    # return a json object of this billing info
    return render :json => { :success => "User billed!" }
  end

  return render :json => { :error => "Unknown function"}
end
```

Here’s an example of the JSON data that would be sent in the request to this webhook:

```
// Sent to webhook
{
  "master": true,
  "installationId": "b3ab24c6-2282-69fa-eeea-c1b36ea497c2",
  "params": { "userObjectId": "6eaI2sTgH6" },
  "functionName": "chargeCustomer"
}
```

This response would indicate a success in the webhook:

```
// Returned from the webhook on success
{ "success": "User billed!" }
```

Set your webhook from the Dashboard UI. After that, it’s available from all SDKs and the REST API the same way you would a normal Cloud function

Webhooks are great when you want to use a specialized technology not available on Parse’s Cloud Code. In this case we made use of an open source library and integrated with a separate data source where our billing info might be stored for legacy reasons.

[](https://docs.parseplatform.org/cloudcode/guide/#beforesave-webhooks)beforeSave Webhooks
------------------------------------------------------------------------------------------

Let’s write a `beforeSave` trigger to truncate movie review comments that are more than 140 characters long using our own Rails server and a webhook.

For triggers, the following parameters are sent to your webhook.

*   **master**: True if the master key was used and false otherwise.
*   **user**: If set, this will contain the Parse User who made the request, in our REST API format.
*   **installationId**: If available, the installationId which made the request.
*   **object**: For triggers, this will contain the Parse Object, in our REST API format. For example: `{ "className": "TestObject", "foo": "bar" }`.
*   **triggerName**: “beforeSave”

To respond to a `beforeSave` request, send a JSON object with the key `error` or `success` set. This is the same as for Cloud functions, but there’s an extra capability with `beforeSave` triggers. By returning an error, you will cancel the save request and the object will not be stored on Parse. You can also return a JSON object in this following format to override the values that will be saved for the object:

```
{
  "className": "AwesomeClass",
  "existingColumn": "sneakyChange",
  "newColumn": "sneakyAddition"
}
```

Let’s [recreate our trigger](https://docs.parseplatform.org/cloudcode/guide/#cloud-code-beforesave-triggers) to truncate movie review comments that are longer than 140 characters.

```
# We need to disable CSRF protection for webhooks to work. Instead we
# use the webhook key to prove authenticity.
protect_from_forgery :except => :reviews

def reviews
  if request.headers['X-Parse-Webhook-Key'] != @webhook_key
    return render :json => { :error => "Request Unauthorized"}
  end

  review = params[:object]
  if params[:triggerName] == "beforeSave" && review["className"] == "Review"
    # truncate the object and return the new data
    if review["comment"].length > 140
      review["comment"] = review["comment"].truncate(140)
      return render :json => { :success => review }
    end

    # if the comment is ok we just return a success
    return render :json => { :success => true }
  end

  return render :json => { :error => "Unknown trigger"}
end
```

Here’s an example of the JSON data that would be sent in the request to this webhook:

```
// Sent to webhook
{
  "master": false,
  "user": {
    "createdAt": "2015-03-24T20:19:00.542Z",
    "objectId": "lValKpphWN",
    "sessionToken": "orU3ClA7sqMIN8g4KtmLe7eDM",
    "updatedAt": "2015-03-24T20:19:00.542Z",
    "username": "Matt"
  },
  "installationId": "b3ab24c6-2282-69fa-eeea-c1b36ea497c2",
  "triggerName": "beforeSave",
  "object": {
    "className": "Comment",
    "comment": "A very long comment that will be truncated to be just 140 characters. I sure love using Parse, it's just so easy to get started :)! Hopefully that part doesn't get truncated :/"
  }
}
```

This response would indicate a success in the webhook:

```
// Returned from the webhook on success
{
  "success": {
    "className": "Comment",
    "comment": "A very long comment that will be truncated to be just 140 characters. I sure love using Parse, it's just so easy to get started :)! Hopef..."
  }
}
```

[](https://docs.parseplatform.org/cloudcode/guide/#aftersave-webhooks)afterSave Webhooks
----------------------------------------------------------------------------------------

Like we’ve seen in Cloud Code, it’s also possible to run some code after an object has been saved using a webhook. The parameters sent to your webhook are the same as for `beforeSave` triggers but we’ll repeat them here for clarity.

*   **master**: True if the master key was used and false otherwise.
*   **user**: If set, this will contain the Parse User who made the request, in our REST API format.
*   **installationId**: If available, the installationId which made the request.
*   **object**: For triggers, this will contain the Parse Object, in our REST API format. For example: `{ "className": "TestObject", "foo": "bar" }`.
*   **triggerName**: “afterSave”

No response is required for `afterSave` triggers.

Let’s take the same example we created in Cloud Code [in the last chapter](https://docs.parseplatform.org/cloudcode/guide/#cloud-code-aftersave-triggers); keeping track of the number of comments on a blog post. But instead of storing the number in our Parse database, we’ll store the count in a separate data source accessible by our Rails app. This could be useful if you’re storing data that will be used to run custom analysics instead of being served to your users through a client.

```
# We need to disable CSRF protection for webhooks to work. Instead we
# use the webhook key to prove authenticity.
protect_from_forgery :except => :comments

def comments
  if request.headers['X-Parse-Webhook-Key'] != @webhook_key
    return render :nothing => true
  end

  comment = params[:object]
  if params[:triggerName] == "afterSave" && comment["className"] == "Comment"
    post = comment["post"]
    @post_model = Post.where("id = #{post["objectId"]}")
    @post_model.increment(:comments_count, 1)
    @post_model.save!
    return render :nothing => true
  end

  render :nothing => true
end
```

Here’s an example of the JSON data that would be sent in the request to this webhook:

```
// Sent to webhook
{
  "master": false,
  "user": {
    "createdAt": "2015-03-24T20:19:00.542Z",
    "objectId": "lValKpphWN",
    "sessionToken": "orU3ClA7sqMIN8g4KtmLe7eDM",
    "updatedAt": "2015-03-24T20:19:00.542Z",
    "username": "Matt"
  },
  "installationId": "b3ab24c6-2282-69fa-eeea-c1b36ea497c2",
  "triggerName": "afterSave",
  "object": {
    "objectId": "zPnDyvj0vd",
    "className": "Comment",
    "createdAt": "2015-03-25T00:00:57.055Z",
    "updatedAt": "2015-03-25T00:00:57.055Z",
    "post": {
      "__type": "Pointer",
      "className": "Post",
      "objectId": "jsUd72Sd2l"
    }
  }
}
```

[](https://docs.parseplatform.org/cloudcode/guide/#beforedelete-webhooks)beforeDelete Webhooks
----------------------------------------------------------------------------------------------

You also use webhooks for `beforeDelete` triggers. The parameters sent to your webhook are the same as for `beforeSave` and `afterSave` triggers but we’ll repeat them here for clarity.

*   **master**: True if the master key was used and false otherwise.
*   **user**: If set, this will contain the Parse User who made the request, in our REST API format.
*   **installationId**: If available, the installationId which made the request.
*   **object**: For triggers, this will contain the Parse Object, in our REST API format. For example: `{ "className": "TestObject", "foo": "bar" }`.
*   **triggerName**: “beforeDelete”

Just like for Cloud functions, to respond to a `beforeDelete` request, send a JSON object with the key `error` or `success` set. Returning an error will cancel the delete and the object will remain in your database.

As an example, let’s use this trigger to prohibit a user from deleting or creating a new blog posts if they haven’t paid their bill. We’ll assume the billing information is currently stored in a SQL database only accessible from our Rails server. We’ll use both the `beforeDelete` and the `beforeSave` triggers to disable all modifications to this class.

```
# We need to disable CSRF protection for webhooks to work. Instead we
# use the webhook key to prove authenticity.
protect_from_forgery :except => :posts

def posts
  if request.headers['X-Parse-Webhook-Key'] != @webhook_key
    return render :json => { :error => "Request Unauthorized"}
  end

  post = params[:object]
  if (params[:triggerName] == "beforeDelete" || params[:triggerName] == "beforeSave") && post["className"] == "Post"
    @user = User.find(post['user'])
    if !@user.paid_up
      return render :json => { :error => "You have outstanding charges on your account. Please update your credit card information before proceeding." }
    end

    return render :json => { :success => true }
  end
  return render :json => { :error => "Unknown trigger"}
end
```

Here’s an example of the JSON data that would be sent in the request to this webhook:

```
// Sent to webhook
{
  "master": false,
  "user": {
    "createdAt": "2015-03-24T20:19:00.542Z",
    "objectId": "lValKpphWN",
    "sessionToken": "orU3ClA7sqMIN8g4KtmLe7eDM",
    "updatedAt": "2015-03-24T20:19:00.542Z",
    "username": "Matt"
  },
  "installationId": "b3ab24c6-2282-69fa-eeea-c1b36ea497c2",
  "triggerName": "beforeDelete",
  "object": {
    "objectId": "jsUd72Sd2l",
    "className": "Post",
    "createdAt": "2015-03-25T00:00:57.055Z",
    "updatedAt": "2015-03-25T00:00:57.055Z"
  }
}
```

This response would indicate a success in the webhook:

```
// Returned from the webhook on success
{ "success": true }
```

As with previous examples, for this example to work you would also need to set up the webhooks in the Dashboard for your app.

[](https://docs.parseplatform.org/cloudcode/guide/#afterdelete-webhooks)afterDelete Webhooks
--------------------------------------------------------------------------------------------

The `afterDelete` trigger is also accessible via webhooks. The parameters sent to your webhook are the same as for other triggers but we’ll repeat them here for clarity.

*   **master**: True if the master key was used and false otherwise.
*   **user**: If set, this will contain the Parse User who made the request, in our REST API format.
*   **installationId**: If available, the installationId which made the request.
*   **object**: For triggers, this will contain the Parse Object, in our REST API format. For example: `{ "className": "TestObject", "foo": "bar" }`.
*   **triggerName**: “afterDelete”

No response is required for `afterDelete` triggers.

In our [webhooks example for the afterSave](https://docs.parseplatform.org/cloudcode/guide/#cloud-code-aftersave-triggers) trigger, we updated a count in our external SQL database to track the number of comments on a post. In this example, let’s decrement this count when a comment is deleted.

```
# We need to disable CSRF protection for webhooks to work. Instead we
# use the webhook key to prove authenticity.
protect_from_forgery :except => :comments

def comments
  if request.headers['X-Parse-Webhook-Key'] != @webhook_key
    return render :nothing => true
  end

  comment = params[:object]
  if params[:triggerName] == "afterDelete" && comment["className"] == "Comment"
    @post_model = Post.where("id = #{comment['post']}")
    @post_model.decrement(:comments_count, 1)
    @post_model.save!
    return render :nothing => true
  end

  render :nothing => true
end
```

Here’s an example of the JSON data that would be sent in the request to this webhook:

```
// Sent to webhook
{
  "master": false,
  "user": {
    "createdAt": "2015-03-24T20:19:00.542Z",
    "objectId": "lValKpphWN",
    "sessionToken": "orU3ClA7sqMIN8g4KtmLe7eDM",
    "updatedAt": "2015-03-24T20:19:00.542Z",
    "username": "Matt"
  },
  "installationId": "b3ab24c6-2282-69fa-eeea-c1b36ea497c2",
  "triggerName": "afterDelete",
  "object": {
    "objectId": "zPnDyvj0vd",
    "className": "Comment",
    "createdAt": "2015-03-25T00:00:57.055Z",
    "updatedAt": "2015-03-25T00:00:57.055Z",
    "post": {
      "__type": "Pointer",
      "className": "Post",
      "objectId": "jsUd72Sd2l"
    }
  }
}
```

After setting up your webhook in the Dashboard UI, you’ll be acurately decrementing comment counts!

[](https://docs.parseplatform.org/cloudcode/guide/#config)Config
----------------------------------------------------------------

Parse Config offers a convenient way to configure parameters in Cloud Code.

```
const config = await Parse.Config.get({useMasterKey: true});
const privateParam = config.get("privateParam");
```

By default, Parse Config parameters can be publicly read which may be undesired if the parameter contains sensitive information that should not be exposed to clients. A parameter can be made readable only with the master key by setting the `Requires master key?` property via the Parse Dashboard to `Yes`.
