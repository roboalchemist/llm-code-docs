# Source: https://firebase.google.com/docs/functions/functions-and-firebase.md.txt

<br />

Google Cloud Run functions and Cloud Functions for Firebase together comprise an important part of Google's serverless compute solution for creating event-driven applications.

For**Google Cloud Platform developers** ,[Cloud Run functions](https://cloud.google.com/functions/)serve as a connective layer allowing you to weave logic between Google Cloud Platform (GCP) services by listening for and responding to events.

For**Firebase developers** ,[Cloud Functions for Firebase](https://firebase.google.com/docs/functions/)provides a way to extend the behavior of Firebase and integrate Firebase features through the addition of server-side code.

Both solutions provide fast and reliable execution of functions in a fully managed environment where there's no need for you to worry about managing any servers or provisioning any infrastructure.

## Cloud Functions for Firebase

You should use Cloud Functions for Firebase if you're a developer building a mobile app or mobile web app. Firebase gives mobile developers access to a complete range of fully managed mobile-centric services including analytics, authentication and Realtime Database. Cloud Functions rounds out the offering by providing a way to extend and connect the behavior of Firebase features through the addition of server-side code.

Firebase developers can easily integrate with external services for tasks like processing payments and sending SMS messages. Also, developers can include custom logic that is either too heavyweight for a mobile device, or which needs to be secured on a server.[Explore use cases](https://firebase.google.com/docs/functions/use-cases)to learn more about typical integrations. For developers that need a more full-featured backend, Cloud Run functions provides a gateway to the powerful capabilities in[Google Cloud Platform](https://cloud.google.com/docs/).

Cloud Functions for Firebase is optimized for Firebase developers:

- Firebase SDK to configure your functions through code
- Integrated with Firebase Console and Firebase CLI
- The same triggers as Google Cloud Functions, plus Firebase Realtime Database, Firebase Authentication, and Firebase Analytics triggers

## Cloud Run functions for Google Cloud Platform

Developers can connect and extend GCP services by writing code in the form of a function. Cloud Run functions serve as a connective layer allowing you to weave logic between GCP services by listening for and responding to events. With just a few lines of code, developers can enrich their use of GCP services to create higher level combinations without needing to provision or manage servers. See the[Google Cloud Run functions documentation](https://cloud.google.com/functions/docs/)for more information.