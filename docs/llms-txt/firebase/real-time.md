# Source: https://firebase.google.com/docs/remote-config/real-time.md.txt

<br />

iOS+AndroidWebFlutterUnityC++  

<br />

Real-timeRemote Configlets you receive updated[parameter keys and values](https://firebase.google.com/docs/remote-config/parameters)as soon as they're published on the server. This lets you quickly update any type of app attribute controlled using aRemote Configparameter value. With real-timeRemote Configupdates, you can:

- Reduce risk by rolling out features incrementally to targeted users, and performing an emergency rollback if needed.
- Increase user engagement by quickly customizing user experiences as they use the app. For example, you could update banners and offer incentives for users who match specificGoogle Analyticsuser properties or dynamically adjust game difficulty for cohorts of players.
- Reduce build dependencies and increase developer productivity: UseRemote Configparameters as feature flags to expose functionality for your development and test teams, while keeping it hidden to users in production.

To learn more about ways you can useRemote Config, see[What can you do withRemote Config?](https://firebase.google.com/docs/remote-config/use-cases)

In this guide, you'll:

- Learn more about the client-server relationship that supports real-time updates.
- Understand how the real-time functionality in the SDK works.
- Learn how to use real-time updates to keep your app configuration up-to-date.

| Real-time updates are available for the following versions of theRemote ConfigSDK:
|
| - iOS: v10.7.0+
| - Android: v21.3.0+ (Firebase BoMv31.3.0+)
| - Web: v12.3.0+
| - C++: v11.0.0+
| - Unity: v11.0.0+ (Android and Apple platforms)
| - Flutter: v4.0.0+ (Android and Apple platforms)

## The real-time client-server connection

When you implement real-timeRemote Configin your app, you create a real-time listener that opens an HTTP connection to theRemote Configbackend. The request includes the config version that's cached on the device. The real-timeRemote Configserver uses an*invalidation message*to signal to the app when a newer version of a server-side config should be fetched.

If the server has a newer version, it sends the invalidation signal immediately. If it doesn't have a newer version, it keeps the connection open and waits until one is published on the server. When the client SDK receives an invalidation signal, it automatically fetches it, then calls the listener callback registered when you opened the listener connection. This fetch is similar to the fetch call you can make with the SDK, but bypasses any caching or`minimumFetchInterval`setting. The client-server connection is maintained while the app is in the foreground.
![Real-time Remote Config client-server workflow](https://firebase.google.com/static/docs/remote-config/images/real-time-client-server.png)Real-timeRemote Configclient-server workflow

Since the client-server connection is made over HTTP, it doesn't require any dependencies on other libraries.

## Listen for updates

Real-time updates complementRemote Config`fetch`calls. We recommend calling fetch when your app starts (or sometime during your app's lifecycle) and listening for real-timeRemote Configupdates during the user session to ensure that you have the latest values as soon as they're published on the server.

To listen for updates, call[`addOnConfigUpdateListener`](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/ConfigUpdateListenerRegistration), implementing a callback that is invoked whenever aRemote Configupdate is available in the app. Behind the scenes, this call starts listening for updates from theRemote Configserver. To learn more about the client-server relationship, see[the previous section](https://firebase.google.com/docs/remote-config/real-time#real-time-client-server-connection).

The callback is often a good place to use`activate`to make the updated config parameters available to your app. See[FirebaseRemote ConfigLoading Strategies](https://firebase.google.com/docs/remote-config/loading)for additional strategies to activate parameter values when you're using real-timeRemote Config.

## Selectively activate parameter values

When you call[`addOnConfigUpdateListener`](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/ConfigUpdateListenerRegistration), you can await the change and activate it.
The`onUpdate`callback is called when both a new version of the template has been automatically fetched and when that new version has changes to the active parameter values in the app.

<br />

These callbacks are invoked with a parameter`configUpdate`.`configUpdate`contains`updatedKeys`, which is the set of changed parameter keys that initiated the real-time update and includes the following:

- Parameter keys that were added or removed
- Parameter keys whose values have changed
- Parameter keys whose metadata has changed (for example,Remote Configpersonalization information)
- Parameter keys whose value source has changed (for example, an in-app default value updating to a server-side value)

If you're using a real-time listener in a particular view within your app, you can check if the parameters relevant to that view have changed before activating.

Occasionally, a fetch (either initiated when you call the`fetch`method, or by real-timeRemote Config) does not result in an update for the client. In these cases, the`onUpdate`method or completion won't be called.

## Add and remove listeners

[`addOnConfigUpdateListener`](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/ConfigUpdateListenerRegistration)is the main entrypoint for real-timeRemote Config. Calling this listener for the first time in your app's lifecycle opens the connection to the backend. Subsequent calls reuse the same connection, multiplexing the invalidation message described in[the real-time client-server connection](https://firebase.google.com/docs/remote-config/real-time#real-time-client-server-connection).

<br />

The call returns a "listener registration," which has a method called[`remove`](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/ConfigUpdateListenerRegistration). To stop listening, store the reference to the listener registration. Call`remove`to stop listening at this registration. If it's the only registered listener, calling`remove`closes the real-time connection to the server.

Although you*can* manually stop listening for updates, it's often not necessary. Real-timeRemote Configautomatically stops listening for updates when the app enters the background and restarts when the app is foregrounded.
| **Note:** Effective January 1, 2026, real-time Remote Config will limit projects to 20 million concurrent open connections. If a project exceeds this limit, incremental real-time connection requests may be rejected, and the client SDK will automatically fall back to the standard fetch mechanism. To ensure all clients receive configuration updates when a new template is published, the service will provide exceptional handling for clients on a stale config version. When such a client initiates a real-time connection, the service will respond with the new update and then terminate the connection if the 20 million connection limit is breached. This allows stale clients to receive their update immediately, even if the general connection limit has been reached. This limit will be applicable from Android SDK v23.0.0+ (Firebase BOM v34.1.0+) and iOS SDK v12.0.0+.

## Next steps

Check out[Get started with FirebaseRemote Config](https://firebase.google.com/docs/remote-config/get-started)to configureRemote Configand start listening for updates in real-time.