# Source: https://firebase.google.com/docs/database/android/start.md.txt

If you haven't already,
[add Firebase to your Android project](https://firebase.google.com/docs/android/setup).

## Create a Database

1. Navigate to the **Realtime Database** section of the
   [Firebase console](https://console.firebase.google.com/project/_/database).
   You'll be prompted to select an existing Firebase project.
   Follow the database creation workflow.

2. Select a starting mode for your Firebase Security Rules:

   Test mode

   :   Good for getting started with the mobile and web client libraries,
       but allows anyone to read and overwrite your data. After testing, **make
       sure to review the [Understand Firebase Realtime Database Rules](https://firebase.google.com/docs/database/security)
       section.**

   :

       > [!NOTE]
       > **Note:** If you create a database in Test mode and make no changes to the default world-readable and world-writeable Security Rules within a trial period, you will be alerted by email, then your database rules will deny all requests. Note the expiration date during the Firebase console setup flow.

   :   To get started with the web, Apple, or Android SDK, select testmode.

   Locked mode

   :   Denies all reads and writes from mobile and web clients.
       Your authenticated application servers can still access your database.

3. Choose a location for the database.

   Depending on the
   [location of the database](https://firebase.google.com/docs/projects/locations#rtdb-locations), the
   URL for the new database will be in one of the following forms:
   - `DATABASE_NAME.firebaseio.com` (for
     databases in `us-central1`)

   - `DATABASE_NAME.REGION.firebasedatabase.app`
     (for databases in all other locations)

4. Click **Done**.

When you enable Realtime Database, it also enables the API in the
[Cloud API Manager](https://console.cloud.google.com/projectselector/apis/api/firebasedatabase.googleapis.com/overview).

## Add the Realtime Database SDK to your app

In your **module (app-level) Gradle file** (usually `<project>/<app-module>/build.gradle.kts` or `<project>/<app-module>/build.gradle`), add the dependency for the Realtime Database library for Android. We recommend using the [Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom) to control library versioning.

<br />

```
dependencies {
    // Import the BoM for the Firebase platform
    implementation(platform("com.google.firebase:firebase-bom:34.10.0"))

    // Add the dependency for the Realtime Database library
    // When using the BoM, you don't specify versions in Firebase library dependencies
    implementation("com.google.firebase:firebase-database")
}
```

By using the [Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom),
your app will always use compatible versions of Firebase Android libraries.
*(Alternative)*
Add Firebase library dependencies *without* using the BoM

If you choose not to use the Firebase BoM, you must specify each Firebase library version
in its dependency line.

**Note that if you use *multiple* Firebase libraries in your app, we strongly
recommend using the BoM to manage library versions, which ensures that all versions are
compatible.**

```groovy
dependencies {
    // Add the dependency for the Realtime Database library
    // When NOT using the BoM, you must specify versions in Firebase library dependencies
    implementation("com.google.firebase:firebase-database:22.0.1")
}
```

<br />

## Configure Realtime Database Security Rules

The Realtime Database provides a declarative rules language that allows
you to define how your data should be structured, how it should be
indexed, and when your data can be read from and written to.

> [!NOTE]
> **Note:** By default, read and write access to your database is restricted so only authenticated users can read or write data. To get started without setting up [Authentication](https://firebase.google.com/docs/auth), you can [configure your rules for public access](https://firebase.google.com/docs/rules/basics#default_rules_locked_mode). This does make your database open to anyone, even people not using your app, so be sure to restrict your database again when you set up authentication.

## Write to your database

Retrieve an instance of your database using `getInstance()` and
reference the location you want to write to.

> [!NOTE]
> **Important** : To get a reference to a database other than a `us-central1` default database, you must pass the database URL to `getInstance()` (or for Kotlin `database()`). For a `us-central1` default database, you can call `getInstance()` (or `database`) without arguments.
>
> You can find your Realtime Database URL in the *Realtime Database* section of the
> [Firebase console](https://console.firebase.google.com/). Depending on the
> [location of the database](https://firebase.google.com/docs/projects/locations#rtdb-locations),
> the database URL will be in one of the following forms:
>
> - `https://DATABASE_NAME.firebaseio.com` (for databases in `us-central1`)
> - `https://DATABASE_NAME.REGION.firebasedatabase.app` (for databases in all other locations)

### Kotlin

```kotlin
// Write a message to the database
val database = Firebase.database
val myRef = database.getReference("message")

myRef.setValue("Hello, World!")
```

### Java

```java
// Write a message to the database
FirebaseDatabase database = FirebaseDatabase.getInstance();
DatabaseReference myRef = database.getReference("message");

myRef.setValue("Hello, World!");
```

You can save a range of data types to the database this way, including Java
objects. When you save an object the responses from any getters will be saved as
children of this location.

## Read from your database

To make your app data update in realtime, you should add a
[`ValueEventListener`](https://firebase.google.com/docs/reference/android/com/google/firebase/database/ValueEventListener)
to the reference you just created.

The `onDataChange()` method in this class is triggered once when the listener is
attached and again every time the data changes, including the children.

### Kotlin

```kotlin
// Read from the database
myRef.addValueEventListener(object : ValueEventListener {
    override fun onDataChange(dataSnapshot: DataSnapshot) {
        // This method is called once with the initial value and again
        // whenever data at this location is updated.
        val value = dataSnapshot.getValue<String>()
        Log.d(TAG, "Value is: $value")
    }

    override fun onCancelled(error: DatabaseError) {
        // Failed to read value
        Log.w(TAG, "Failed to read value.", error.toException())
    }
})
```

### Java

```java
// Read from the database
myRef.addValueEventListener(new ValueEventListener() {
    @Override
    public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
        // This method is called once with the initial value and again
        // whenever data at this location is updated.
        String value = dataSnapshot.getValue(String.class);
        Log.d(TAG, "Value is: " + value);
    }

    @Override
    public void onCancelled(@NonNull DatabaseError error) {
        // Failed to read value
        Log.w(TAG, "Failed to read value.", error.toException());
    }
});
```

## Optional: Configure ProGuard

When using Firebase Realtime Database in your app along with ProGuard, you need to
consider how your model objects will be serialized and deserialized after
obfuscation. If you use `DataSnapshot.getValue(Class)` or
`DatabaseReference.setValue(Object)` to read and write data, you will need to
add rules to the `proguard-rules.pro` file:

        # Add this global rule
        -keepattributes Signature

        # This rule will properly ProGuard all the model classes in
        # the package com.yourcompany.models.
        # Modify this rule to fit the structure of your app.
        -keepclassmembers class com.yourcompany.models.** {
          *;
        }

To get help for questions or issues related to ProGuard, visit the
[Guardsquare Community forums](https://community.guardsquare.com/?utm_source=site&utm_medium=site-link&utm_campaign=firebase-install-community)
to get assistance from an expert.

## Prepare for Launch

Before launching your app, we recommend walking through our
[launch checklist](https://firebase.google.com/support/guides/launch-checklist) to make sure your app is
ready to go!

Be sure to enable [App Check](https://firebase.google.com/docs/app-check/android) to help ensure that
only your apps can access your databases.

## Next Steps

- Learn how to [structure data](https://firebase.google.com/docs/database/android/structure-data) for Realtime Database
- [Scale your data across multiple database instances](https://firebase.google.com/docs/database/usage/sharding).
- [Read and write data](https://firebase.google.com/docs/database/android/read-and-write).
- [View your database in the Firebase console](https://console.firebase.google.com/project/_/database/data).