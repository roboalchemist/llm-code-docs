# Source: https://firebase.google.com/docs/database/admin/start.md.txt

With the Admin SDK, you can read and write Realtime Database data with full admin privileges,
or with finer-grained limited privileges.
In this document, we'll guide you through adding the Firebase Admin SDK
to your project for accessing the Firebase Realtime Database.
Realtime Database instances can be created in different geographic regions, with separate
`firebaseio.com` and `firebasedatabase.app` URL schemes. Admin SDK
methods for setting URLs can use either scheme. For currently-supported regions and URL
schemes, see the guides topic on [selecting
locations in Firebase projects](https://firebase.google.com/docs/projects/locations#rtdb-locations).

## Admin SDK Setup

To get started with the Firebase Realtime Database on your server, you'll
first need to [set up the Firebase
Admin SDK](https://firebase.google.com/docs/admin/setup#prerequisites) in your language of choice.

> [!WARNING]
> If you are interested in using the Node.js SDK as a client for end-user
> access (for example, in a Node.js desktop or IoT application), as opposed
> to admin access from a privileged environment (like a server), you should
> instead follow the
> [instructions for setting up the client
> JavaScript SDK](https://firebase.google.com/docs/database/web/start).

## Admin SDK Authentication


Before you can access the Firebase Realtime Database from a server using the Firebase Admin SDK, you must
authenticate your server with Firebase. When you authenticate a server, rather than sign in with a
user account's credentials as you would in a client app, you authenticate with a
[*service account*](https://developers.google.com/identity/protocols/OAuth2ServiceAccount)
which identifies your server to Firebase.


You can get two different levels of access when you authenticate using the
Firebase Admin SDK:

| Firebase Admin SDK Auth Access Levels ||
|---|---|
| **Administrative privileges** | Complete read and write access to a project's Realtime Database. Use with caution to complete administrative tasks such as data migration or restructuring that require unrestricted access to your project's resources. |
| **Limited privileges** | Access to a project's Realtime Database, limited to only the resources your server needs. Use this level to complete administrative tasks that have well-defined access requirements. For example, when running a summarization job that reads data across the entire database, you can protect against accidental writes by setting a read-only security rule and then initializing the Admin SDK with privileges limited by that rule. |

### Authenticate with admin privileges


When you initialize the Firebase Admin SDK with the credentials for a service
account with the **Editor** role on your Firebase project, that instance has
complete read and write access to your project's Realtime Database.

##### Java

```java
// Fetch the service account key JSON file contents
FileInputStream serviceAccount = new FileInputStream("path/to/serviceAccount.json");

// Initialize the app with a service account, granting admin privileges
FirebaseOptions options = FirebaseOptions.builder()
    .setCredentials(GoogleCredentials.fromStream(serviceAccount))
    // The database URL depends on the https://firebase.google.com/docs/projects/locations#rtdb-locations
    .setDatabaseUrl("https://DATABASE_NAME.firebaseio.com")
    .build();
FirebaseApp.initializeApp(options);

// As an admin, the app has access to read and write all data, regardless of Security Rules
DatabaseReference ref = FirebaseDatabase.getInstance()
    .getReference("restricted_access/secret_document");
ref.addListenerForSingleValueEvent(new ValueEventListener() {
  @Override
  public void onDataChange(DataSnapshot dataSnapshot) {
    Object document = dataSnapshot.getValue();
    System.out.println(document);
  }

  @Override
  public void onCancelled(DatabaseError error) {
  }
});
```

##### Node.js

```javascript
var admin = require("firebase-admin");

// Fetch the service account key JSON file contents
var serviceAccount = require("path/to/serviceAccountKey.json");

// Initialize the app with a service account, granting admin privileges
admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  // The database URL depends on the https://firebase.google.com/docs/projects/locations#rtdb-locations
  databaseURL: "https://DATABASE_NAME.firebaseio.com"
});

// As an admin, the app has access to read and write all data, regardless of Security Rules
var db = admin.database();
var ref = db.ref("restricted_access/secret_document");
ref.once("value", function(snapshot) {
  console.log(snapshot.val());
});
```

##### Python

```python
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('path/to/serviceAccountKey.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://databaseName.firebaseio.com'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('restricted_access/secret_document')
print(ref.get())
```

##### Go

```go
ctx := context.Background()
conf := &firebase.Config{
	DatabaseURL: "https://databaseName.firebaseio.com",
}
// Fetch the service account key JSON file contents
opt := option.WithCredentialsFile("path/to/serviceAccountKey.json")

// Initialize the app with a service account, granting admin privileges
app, err := firebase.NewApp(ctx, conf, opt)
if err != nil {
	log.Fatalln("Error initializing app:", err)
}

client, err := app.Database(ctx)
if err != nil {
	log.Fatalln("Error initializing database client:", err)
}

// As an admin, the app has access to read and write all data, regradless of Security Rules
ref := client.NewRef("restricted_access/secret_document")
var data map[string]interface{}
if err := ref.Get(ctx, &data); err != nil {
	log.Fatalln("Error reading from database:", err)
}
fmt.Println(data)
```

> [!NOTE]
> Your service only has as much access as the service account used to
> authenticate it. For example, you can limit your service to read-only by using
> a service account with the Reader role on your project. Similarly, a service
> account with no role on the project is not able to read or write any data.

### Authenticate with limited privileges


As a best practice, a service should have access to only the resources it needs. To get
more fine-grained control over the resources a Firebase app instance can
access, use a unique identifier in your [Security Rules](https://firebase.google.com/docs/database/security)
to represent your service. Then set up appropriate rules which grant your service access
to the resources it needs. For example:

```
{
  "rules": {
    "public_resource": {
      ".read": true,
      ".write": true
    },
    "some_resource": {
      ".read": "auth.uid === 'my-service-worker'",
      ".write": false
    },
    "another_resource": {
      ".read": "auth.uid === 'my-service-worker'",
      ".write": "auth.uid === 'my-service-worker'"
    }
  }
}
```


Then, on your server, when you initialize the Firebase app, use the
`databaseAuthVariableOverride` option to override the `auth` object used by
your database rules. In this custom `auth` object, set the `uid` field to the
identifier you used to represent your service in your Security Rules.

##### Java

```java
// Fetch the service account key JSON file contents
FileInputStream serviceAccount = new FileInputStream("path/to/serviceAccountCredentials.json");

// Initialize the app with a custom auth variable, limiting the server's access
Map<String, Object> auth = new HashMap<String, Object>();
auth.put("uid", "my-service-worker");

FirebaseOptions options = new FirebaseOptions.Builder()
    .setCredential(FirebaseCredentials.fromCertificate(serviceAccount))
    // The database URL depends on the https://firebase.google.com/docs/projects/locations#rtdb-locations
    .setDatabaseUrl("https://DATABASE_NAME.firebaseio.com")
    .setDatabaseAuthVariableOverride(auth)
    .build();
FirebaseApp.initializeApp(options);

// The app only has access as defined in the Security Rules
DatabaseReference ref = FirebaseDatabase
    .getInstance()
    .getReference("/some_resource");
ref.addListenerForSingleValueEvent(new ValueEventListener() {
    @Override
    public void onDataChange(DataSnapshot dataSnapshot) {
        String res = dataSnapshot.getValue();
        System.out.println(res);
    }
});
```

##### Node.js

```javascript
var admin = require("firebase-admin");

// Fetch the service account key JSON file contents
var serviceAccount = require("path/to/serviceAccountKey.json");

// Initialize the app with a custom auth variable, limiting the server's access
admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  // The database URL depends on the https://firebase.google.com/docs/projects/locations#rtdb-locations
  databaseURL: "https://DATABASE_NAME.firebaseio.com",
  databaseAuthVariableOverride: {
    uid: "my-service-worker"
  }
});

// The app only has access as defined in the Security Rules
var db = admin.database();
var ref = db.ref("/some_resource");
ref.once("value", function(snapshot) {
  console.log(snapshot.val());
});
```

##### Python

```python
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('path/to/serviceAccountKey.json')

# Initialize the app with a custom auth variable, limiting the server's access
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://databaseName.firebaseio.com',
    'databaseAuthVariableOverride': {
        'uid': 'my-service-worker'
    }
})

# The app only has access as defined in the Security Rules
ref = db.reference('/some_resource')
print(ref.get())
```

##### Go

```go
ctx := context.Background()
// Initialize the app with a custom auth variable, limiting the server's access
ao := map[string]interface{}{"uid": "my-service-worker"}
conf := &firebase.Config{
	DatabaseURL:  "https://databaseName.firebaseio.com",
	AuthOverride: &ao,
}

// Fetch the service account key JSON file contents
opt := option.WithCredentialsFile("path/to/serviceAccountKey.json")

app, err := firebase.NewApp(ctx, conf, opt)
if err != nil {
	log.Fatalln("Error initializing app:", err)
}

client, err := app.Database(ctx)
if err != nil {
	log.Fatalln("Error initializing database client:", err)
}

// The app only has access as defined in the Security Rules
ref := client.NewRef("/some_resource")
var data map[string]interface{}
if err := ref.Get(ctx, &data); err != nil {
	log.Fatalln("Error reading from database:", err)
}
fmt.Println(data)
```

In some cases, you may want to downscope the Admin SDKs to act as an
unauthenticated client. You can do this by providing a value of
`null` for the database auth variable override.

##### Java

```java
// Fetch the service account key JSON file contents
FileInputStream serviceAccount = new FileInputStream("path/to/serviceAccountCredentials.json");

FirebaseOptions options = new FirebaseOptions.Builder()
    .setCredential(FirebaseCredentials.fromCertificate(serviceAccount))
    // The database URL depends on the https://firebase.google.com/docs/projects/locations#rtdb-locations
    .setDatabaseUrl("https://DATABASE_NAME.firebaseio.com")
    .setDatabaseAuthVariableOverride(null)
    .build();
FirebaseApp.initializeApp(options);

// The app only has access to public data as defined in the Security Rules
DatabaseReference ref = FirebaseDatabase
    .getInstance()
    .getReference("/public_resource");
ref.addListenerForSingleValueEvent(new ValueEventListener() {
    @Override
    public void onDataChange(DataSnapshot dataSnapshot) {
        String res = dataSnapshot.getValue();
        System.out.println(res);
    }
});
```

##### Node.js

```javascript
var admin = require("firebase-admin");

// Fetch the service account key JSON file contents
var serviceAccount = require("path/to/serviceAccountKey.json");

// Initialize the app with a null auth variable, limiting the server's access
admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  // The database URL depends on the https://firebase.google.com/docs/projects/locations#rtdb-locations
  databaseURL: "https://DATABASE_NAME.firebaseio.com",
  databaseAuthVariableOverride: null
});

// The app only has access to public data as defined in the Security Rules
var db = admin.database();
var ref = db.ref("/public_resource");
ref.once("value", function(snapshot) {
  console.log(snapshot.val());
});
```

##### Python

```python
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('path/to/serviceAccountKey.json')

# Initialize the app with a None auth variable, limiting the server's access
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://databaseName.firebaseio.com',
    'databaseAuthVariableOverride': None
})

# The app only has access to public data as defined in the Security Rules
ref = db.reference('/public_resource')
print(ref.get())
```

##### Go

```go
ctx := context.Background()
// Initialize the app with a nil auth variable, limiting the server's access
var nilMap map[string]interface{}
conf := &firebase.Config{
	DatabaseURL:  "https://databaseName.firebaseio.com",
	AuthOverride: &nilMap,
}

// Fetch the service account key JSON file contents
opt := option.WithCredentialsFile("path/to/serviceAccountKey.json")

app, err := firebase.NewApp(ctx, conf, opt)
if err != nil {
	log.Fatalln("Error initializing app:", err)
}

client, err := app.Database(ctx)
if err != nil {
	log.Fatalln("Error initializing database client:", err)
}

// The app only has access to public data as defined in the Security Rules
ref := client.NewRef("/some_resource")
var data map[string]interface{}
if err := ref.Get(ctx, &data); err != nil {
	log.Fatalln("Error reading from database:", err)
}
fmt.Println(data)
```

## Next Steps

- Learn how to [structure data](https://firebase.google.com/docs/database/admin/structure-data) for Realtime Database.
- [Scale data across multiple database instances](https://firebase.google.com/docs/database/usage/sharding).
- [Save data.](https://firebase.google.com/docs/database/admin/save-data)
- [Retrieve data.](https://firebase.google.com/docs/database/admin/retrieve-data)
- [View your database in
  the Firebase console.](https://console.firebase.google.com/project/_/database/data)