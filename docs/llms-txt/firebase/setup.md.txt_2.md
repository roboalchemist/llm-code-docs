# Source: https://firebase.google.com/docs/games/setup.md.txt

[Video](https://www.youtube.com/watch?v=rAcWLPQIL38)

With Firebase, it's easy to add backend services and analytics to your mobile
games on iOS and Android. Using our SDKs for C++ and Unity, you can
access Firebase services directly in your C++ and Unity code, without having to
write any Swift/Objective-C or Java/Kotlin code.

<br />

Ready to get started? Choose your platform:

[Unity](https://firebase.google.com/docs/unity/setup)
[C++](https://firebase.google.com/docs/cpp/setup)

<br />

**Find out more information about powering up your games with Firebase at our
[Firebase games page](https://firebase.google.com/games).**

## Example use cases for Firebase in your games

- [AdMob](https://firebase.google.com/docs/admob) --- Earn revenue in your games with banner ads,
  interstitials, even rewarded video. Track your ads performance with
  Google Analytics.

- [Firebase AI Logic](https://firebase.google.com/docs/ai-logic) --- Build AI features using
  Gemini models, like new forms of player interaction
  (both voice and image input), responsive and evolving game worlds, and
  personalized experiences.

- [Analytics](https://firebase.google.com/docs/analytics) --- Learn how players interact with your game,
  how much time they spend playing, how long they take to complete levels, how
  much and how frequently they make in-app purchases, how often they return to
  the game, and much more.

- [App Check](https://firebase.google.com/docs/app-check) - Protect your API resources from abuse by
  preventing unauthorized clients from accessing your backend resources.

- [Authentication](https://firebase.google.com/docs/auth) --- Give players a frictionless sign-in experience that
  also ensures safe and secure account management.

- [Realtime Database](https://firebase.google.com/docs/database) --- Read and write game content using this
  realtime, scalable database. Realtime Database allows you to keep track of player
  presence in- or out-of-game.

- [Cloud Firestore](https://firebase.google.com/docs/firestore) --- Read and write game content using
  this realtime, scalable database. Cloud Firestore has outstanding uptime
  guarantees and allows you to serve data from your choice of locations
  worldwide.

- [Cloud Storage](https://firebase.google.com/docs/storage) --- Store and serve player-generated
  content reliably and securely, such as avatars, game playthroughs, and
  screenshots.

- [Cloud Messaging](https://firebase.google.com/docs/cloud-messaging) --- Inform players about new
  content or levels or send push notifications to players who have completed
  your available content.

- [Crashlytics](https://firebase.google.com/docs/crashlytics) --- Spend less time finding and more time
  fixing crashes. Build more stable games by providing deep and actionable
  insights into crashes.

- [Dynamic Links](https://firebase.google.com/docs/dynamic-links) --- Share content, such as custom levels,
  in-game items, and game invitations between players.

- [Remote Config](https://firebase.google.com/docs/remote-config) --- Change elements of your game
  without deploying code, including settings like enemy density or power-up
  frequency.

- [Cloud Functions](https://firebase.google.com/docs/functions) --- Run backend code in a secure
  environment in response to events triggered by other Firebase products and
  client requests.

## Supported Firebase products

The Firebase SDKs for C++ and for Unity directly support the following Firebase
products. Firebase also supports a subset of the available libraries for a
desktop workflow (**beta**) implementation.

| Firebase product | C++ | Unity | Desktop (beta) |
|---|---|---|---|
| [AdMob](https://firebase.google.com/docs/admob) | Yes | Yes | No |
| [Firebase AI Logic](https://firebase.google.com/docs/ai-logic) | No | Yes | Yes |
| [Analytics](https://firebase.google.com/docs/analytics) | Yes | Yes | No |
| [App Check](https://firebase.google.com/docs/app-check) | Yes | Yes | Yes |
| [Authentication](https://firebase.google.com/docs/auth) | Yes | Yes | Yes |
| [Cloud Firestore](https://firebase.google.com/docs/firestore) | Yes | Yes | Yes |
| [Cloud Functions](https://firebase.google.com/docs/functions) | Yes | Yes | Yes |
| [Cloud Messaging](https://firebase.google.com/docs/cloud-messaging) | Yes | Yes | No |
| [Cloud Storage](https://firebase.google.com/docs/storage) | Yes | Yes | Yes |
| [Crashlytics](https://firebase.google.com/docs/crashlytics) | No | Yes | No |
| [Dynamic Links](https://firebase.google.com/docs/dynamic-links) | Yes | Yes | No |
| [Realtime Database](https://firebase.google.com/docs/database) | Yes | Yes | Yes |
| [Remote Config](https://firebase.google.com/docs/remote-config) | Yes | Yes | Yes |

> [!NOTE]
> **Note:** For the desktop workflow, Firebase provides stub (non-functional) implementations of all unsupported Firebase products for convenience.