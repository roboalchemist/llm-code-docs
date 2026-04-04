# Source: https://firebase.google.com/docs/projects/learn-more.md.txt

# Source: https://firebase.google.com/docs/ios/learn-more.md.txt

# Source: https://firebase.google.com/docs/web/learn-more.md.txt

# Source: https://firebase.google.com/docs/cpp/learn-more.md.txt

# Source: https://firebase.google.com/docs/android/learn-more.md.txt

# Source: https://firebase.google.com/docs/unity/learn-more.md.txt

# Source: https://firebase.google.com/docs/cpp/learn-more.md.txt

# Source: https://firebase.google.com/docs/android/learn-more.md.txt

# Source: https://firebase.google.com/docs/unity/learn-more.md.txt

<br />

As you're developing your Unity project using Firebase, you might discover concepts that are unfamiliar or specific to Firebase. This page aims to answer those questions or point you to resources to learn more.

Feel free to visit one of our online communities if you have questions about a topic not covered on this page. We'll also update this page with new topics periodically, so check back to see if we've added the topic you want to learn about!
| **Looking for how to get started with Firebase in your Unity projects? Check out our[Getting Started Guide](https://firebase.google.com/docs/unity/setup).**

## Firebase library support by platform

The following table describes which Firebase libraries are compatible with which platforms. Currently, desktop platforms are only officially supported in the Unity Editor to facilitate development workflows.

|     Platform      | Android | iOS |   tvOS   | macOS *(beta)* | Windows *(beta)* | Linux *(beta)* |
|-------------------|---------|-----|----------|----------------|------------------|----------------|
| A/B Testing       |         |     | v10.4.0+ |                |                  |                |
| Firebase AI Logic |         |     | v10.4.0+ |                |                  |                |
| Analytics         |         |     | v10.4.0+ |                |                  |                |
| App Distribution  |         |     | v10.4.0+ |                |                  |                |
| Authentication    |         |     | v10.4.0+ |                |                  |                |
| Cloud Firestore   |         |     | v10.4.0+ |                |                  |                |
| Cloud Functions   |         |     | v10.4.0+ |                |                  |                |
| Cloud Messaging   |         |     | v10.4.0+ |                |                  |                |
| Cloud Storage     |         |     | v10.4.0+ |                |                  |                |
| Crashlytics       |         |     | v10.4.0+ |                |                  |                |
| Dynamic Links     |         |     |          |                |                  |                |
| Realtime Database |         |     | v10.4.0+ |                |                  |                |
| Remote Config     |         |     | v10.4.0+ |                |                  |                |

## Google services -- config files

As part of adding Firebase to your Unity project, you need to add a Firebase configuration file:

- For Apple platforms: add`GoogleService-Info.plist`.
- For Android: add`google-services.json`.
- For desktop: add one or both of these config files, depending on the platforms you're developing for.

If you want to use multiple Firebase projects in a single app, visit the documentation for[configuring multiple projects](https://firebase.google.com/docs/projects/multiprojects#use_multiple_projects_in_your_application).
| **Note:** The Firebase configuration files contain unique, but non-secret identifiers for your project. To learn more about these config files, visit[Understand Firebase Projects](https://firebase.google.com/docs/projects/learn-more#config-files-objects).

## Open source resources for the Firebase Unity SDK

Firebase supports open source development, and we encourage contributions and feedback.

### Firebase SDKs

The open source Unity SDKs are available in our[GitHub repository](https://github.com/firebase/firebase-unity-sdk).

Note the following about how we build the Unity SDKs for Firebase:

- The Unity SDKs are built on top of the open source[C++ SDKs](https://github.com/firebase/firebase-cpp-sdk).
- The C++ SDKs are in-turn built on top of the open source[iOS SDKs](https://github.com/firebase/firebase-ios-sdk)and[Android SDKs](https://github.com/firebase/firebase-android-sdk).

### Quickstart samples

Firebase maintains a collection of quickstart samples for Firebase APIs on Unity. Find these quickstarts in our public Firebase GitHub[quickstart repository](https://github.com/firebase/quickstart-unity/).

You can open each quickstart in Unity, then run them on a mobile device or in the Unity editor. Or you can use these quickstarts as example code for using Firebase SDKs.

### MechaHamster

MechaHamster is an open source game built in Unity that demonstrates a number of Firebase features in a released game, includingGoogle Analytics,Authentication,Realtime Database,Cloud Messaging,Crashlytics,Remote Config,Cloud Storage,Cloud Functions, andTest Lab. It's available in our[Firebase GitHub repository](https://github.com/google/mechahamster).

### Firebase Unity Solutions

Firebase Unity Solutions is a repository containing a number of open source utilities to help Unity developers achieve common tasks with Firebase. Current solutions include a leaderboard implementation and a utility to create and syncFirebase Remote Configconfigurations directly from the Unity editor. It's available in our[Firebase GitHub repository](https://github.com/FirebaseExtended/unity-solutions).