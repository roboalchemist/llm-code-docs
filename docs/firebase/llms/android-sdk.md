# Source: https://firebase.google.com/docs/data-connect/android-sdk.md.txt

<br />

Firebase Data Connectclient SDKs let you call your server-side queries and mutations directly from a Firebase app. You generate a custom client SDK in parallel as you design the schemas, queries and mutations you deploy to yourData Connectservice. Then, you integrate methods from this SDK into your client logic.

As we've mentioned elsewhere, it's important to note thatData Connectqueries and mutations are not submitted by client code and executed on the server. Instead, when deployed,Data Connectoperations are stored on the server like Cloud Functions. This means you need to deploy corresponding client-side changes to avoid breaking existing users (for example, on older app versions).

That's whyData Connectprovides you with a developer environment and tooling that lets you prototype your server-deployed schemas, queries and mutations. It also generates client-side SDKs automatically, while you prototype.

When you've iterated updates to your service and client apps, both server- and client-side updates are ready to deploy.

## What is the client development workflow?

If you followed the[Get started](https://firebase.google.com/docs/data-connect/quickstart), you were introduced to the overall development flow forData Connect. In this guide, you'll find more detailed information about generating Android SDKs from your schema and working with client queries and mutations.
| You can learn client development with a quickstart app repository and build a fully-featuredData Connectapp by following our[codelab for Android](https://firebase.google.com/codelabs/firebase-dataconnect-android).

To summarize, to use generated Android SDKs in your client apps, you'll follow these prerequisite steps:

1. Add Firebase to your[Android](https://firebase.google.com/docs/android/setup)app.
2. ConfigureData Connectas a dependency in Gradle.
3. Add the Kotlin Serialization Gradle plugin and Gradle dependency.

Then:

1. Develop your app schema.
2. Set up SDK generation:

   - With the**Add SDK to app**button in our Data Connect VS Code extension
   - By[updating your`connector.yaml`](https://firebase.google.com/docs/data-connect/android-sdk#generate-kotlin)
3. [Initialize your client code and import libraries](https://firebase.google.com/docs/data-connect/android-sdk#set-client).

4. [Implement calls to queries and mutations](https://firebase.google.com/docs/data-connect/android-sdk#queries-mutations).

5. [Set up and use theData Connectemulator](https://firebase.google.com/docs/data-connect/android-sdk#prototype-and)and iterate.

## Generate your Kotlin SDK

Use theFirebaseCLI to set upData Connectgenerated SDKs in your apps. The`init`command should detect all apps in the current folder and install generated SDKs automatically.  

    firebase init dataconnect:sdk

### Update SDKs while prototyping

If you have Data Connect VS Code extension installed, it will always keep generated SDKs up to date.

If you don't use Data Connect VS Code extension, you can use Firebase CLI to keep generated SDKs up to date.  

    firebase dataconnect:sdk:generate --watch

### Generate SDKs in build pipelines

You can use the Firebase CLI to generate Data Connect SDKs in CI/CD build processes.  

    firebase dataconnect:sdk:generate

## Set up client code

### IncorporateData Connectinto your client code

To set up your client code to useData Connectand your generated SDK, first follow the[standard Firebase setup instructions](https://firebase.google.com/docs/android/setup).

Then, add the following into the`plugins`section in`app/build.gradle.kts`:  

    // The Firebase team tests with version 1.8.22; however, other 1.8 versions,
    // and all newer versions are expected work too.
    kotlin("plugin.serialization") version "1.8.22" // MUST match the version of the Kotlin compiler

Then, add the following into the`dependencies`section in`app/build.gradle.kts`:  

    implementation(platform("com.google.firebase:firebase-bom:34.7.0"))
    implementation("com.google.firebase:firebase-dataconnect")
    implementation("com.google.firebase:firebase-auth") // Optional
    implementation("com.google.firebase:firebase-appcheck") // Optional
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.7.3") // Newer versions should work too
    implementation("org.jetbrains.kotlinx:kotlinx-serialization-core:1.5.1") // Newer versions should work too

### Initialize theData ConnectAndroid SDK

Initialize yourData Connectinstance using the information you used to set up Data Connect (all available in theFirebaseconsole Data Connect tab).

#### The ConnectorConfig object

The SDK requires a connector configuration object.

This object is automatically generated from`serviceId`and`location`in`dataconnect.yaml`, and`connectorId`in`connector.yaml`.

#### Getting a connector instance

Now that you've set up a configuration object, get aData Connectconnector instance. The code for your connector will be generated by theData Connectemulator. If your connector name is`movies`and the Kotlin package is`com.myapplication`, as specified in`connector.yaml`, then retrieve the connector object by calling:  

    val connector = com.myapplication.MoviesConnector.instance

## Use queries and mutations from your Android SDK

With the connector object, you can run queries and mutations as defined in the GraphQL source code. Suppose your connector has these operations defined:  

    mutation createMovie($title: String!, $releaseYear: Int!, $genre: String!, $rating: Int!) {
      movie_insert(data: {
        title: $title
        releaseYear: $releaseYear
        genre: $genre
        rating: $rating
      })
    }

    query getMovieByKey($key: Movie_Key!) {
      movie(key: $key) { id title }
    }

    query listMoviesByGenre($genre: String!) {
      movies(where: {genre: {eq: $genre}}) {
        id
        title
      }
    }

then you could create and retrieve a movie as follows:  

    val connector = MoviesConnector.instance

    val addMovieResult1 = connector.createMovie.execute(
      title = "Empire Strikes Back",
      releaseYear = 1980,
      genre = "Sci-Fi",
      rating = 5
    )

    val movie1 = connector.getMovieByKey.execute(addMovieResult1.data.key)

    println("Empire Strikes Back: ${movie1.data.movie}")

You can also retrieve multiple movies:  

    val connector = MoviesConnector.instance

    val addMovieResult2 = connector.createMovie.execute(
      title="Attack of the Clones",
      releaseYear = 2002,
      genre = "Sci-Fi",
      rating = 5
    )

    val listMoviesResult = connector.listMoviesByGenre.execute(genre = "Sci-Fi")

    println(listMoviesResult.data.movies)

You can also collect a`Flow`that will only produce a result when a new query result is retrieved using a call to the query's`execute()`method.
**Note:** This Flow is not updated in realtime.  

    val connector = MoviesConnector.instance

    connector.listMoviesByGenre.flow(genre = "Sci-Fi").collect { data ->
      println(data.movies)
    }

    connector.createMovie.execute(
      title="A New Hope",
      releaseYear = 1977,
      genre = "Sci-Fi",
      rating = 5
    )

    connector.listMoviesByGenre.execute(genre = "Sci-Fi") // will cause the Flow to get notified

### Handle changes to enumeration fields

An app's schema can[contain enumerations](https://firebase.google.com/docs/data-connect/schemas-guide#enumeration-fields), which can be accessed by your[GraphQL queries](https://firebase.google.com/docs/data-connect/queries-guide#query-enumerations).

As an app's design changes, you may add new enum supported values. For example, imagine that later in your application's lifecycle you decide to add a FULLSCREEN value to the`AspectRatio`enum.

In theData Connectworkflow, you can use local development tooling to update your queries and SDKs.

However, before you release an updated version of your clients, older deployed clients may break.

#### Example resilient implementation

The generated SDK forces handling of unknown values as the customer's code must unwrap the`EnumValue`object, which is either`EnumValue.Known`for known enum values or`EnumValue.Unknown`for unknown values.  

    val result = connector.listMoviesByAspectRatio.execute(AspectRatio.WIDESCREEN)
    val encounteredAspectRatios = mutableSetOf<String>()

    result.data.movies
      .mapNotNull { it.otherAspectRatios }
      .forEach { otherAspectRatios ->
        otherAspectRatios
          .filterNot { it.value == AspectRatio.WIDESCREEN }
          .forEach {
            when (it) {
              is EnumValue.Known -> encounteredAspectRatios.add(it.value.name)
              is EnumValue.Unknown ->
                encounteredAspectRatios.add("[unknown ratio: ${it.stringValue}]")
            }
          }
      }

    println(
      "Widescreen movies also include additional aspect ratios: " +
        encounteredAspectRatios.sorted().joinToString()
    )

## Prototype and test your Android application

### Instrument clients to use a local emulator

You can use theData Connectemulator, whether from the Data Connect VS Code extension or from the CLI.

Instrumenting the app to connect to the emulator is the same for both scenarios.  

    val connector = MoviesConnector.instance

    // Connect to the emulator on "10.0.2.2:9399"
    connector.dataConnect.useEmulator()

    // (alternatively) if you're running your emulator on non-default port:
    connector.dataConnect.useEmulator(port = 9999)

    // Make calls from your app

To switch to production resources, comment out lines for connecting to the emulator.

## Data types inData ConnectSDKs

TheData Connectserver represents common and custom GraphQL data types. These are represented in the SDK as follows.

| Data Connect Type |                                       Kotlin                                       |
|-------------------|------------------------------------------------------------------------------------|
| String            | String                                                                             |
| Int               | Int (32-bit integer)                                                               |
| Float             | Double (64-bit float)                                                              |
| Boolean           | Boolean                                                                            |
| UUID              | java.util.UUID                                                                     |
| Date              | com.google.firebase.dataconnect.LocalDate (was java.util.Date until 16.0.0-beta03) |
| Timestamp         | com.google.firebase.Timestamp                                                      |
| Int64             | Long                                                                               |
| Any               | com.google.firebase.dataconnect.AnyValue                                           |