# Source: https://firebase.google.com/docs/admin/migrate-java-v7.md.txt

<br />

Version 7.0.0 of the Firebase Admin SDK for Java introduces some important changes in the API. Primarily, the API changes in this release are additions and improvements in error handling forAuthenticationamdFCM.

## General error handling changes

`FirebaseException`base class now exposes several new attributes:

- `ErrorCode getErrorCode()`: Returns the platform error code associated with the exception. Every instance of`FirebaseException`is guaranteed to have a non-null platform error code. Possible platform error codes are defined as a new enum type`ErrorCode`.
- `IncomingHttpResponse getHttpResponse()`: Returns the HTTP response associated with the exception. May be null if the exception was caused by a reason other than a backend HTTP response.

Like before, most other exception types defined in the SDK (for example,`FirebaseAuthException`,`FirebaseMessagingException`) are derived from the`FirebaseException`base class.

## Auth error handling changes

All APIs in the`FirebaseAuth`class may throw instances of`FirebaseAuthException`. Async APIs (for instance, methods that return an`ApiFuture`) may fail with an`ExecutionException`that wraps a`FirebaseAuthException`. The Auth-specific error codes are publicly defined in the new enum type`AuthErrorCode`.

**Before (\<= v6.15.0)**  

    try {
      FirebaseAuth.getInstance().verifyIdToken(idToken, true);
    } catch (FirebaseAuthException ex) {
      if (ex.getErrorCode().equals("id-token-revoked")) {
        System.err.println("ID token has been revoked");
      } else {
        System.err.println("ID token is invalid");
      }
    }

**Now (\>= v7.0.0)**  

    try {
      FirebaseAuth.getInstance().verifyIdToken(idToken, true);
    } catch (FirebaseAuthException ex) {
      if (ex.getAuthErrorCode() == AuthErrorCode.REVOKED_ID_TOKEN) {
        System.err.println("ID token has been revoked");
      } else {
        System.err.println("ID token is invalid");
      }
    }

The`AuthErrorCode`is in addition to the`ErrorCode`inherited from the base`FirebaseException`type. You can implement error handling logic that inspects both error codes if necessary.

## FCMerror handling changes

All APIs in`FirebaseMessaging`class may throw instances of`FirebaseMessagingException`. Async APIs (for instance, methods that return an`ApiFuture`) may fail with an`ExecutionException`that wraps a`FirebaseMessagingException`. TheAuthentication-specific error codes are publicly defined in the new enum type`MessagingErrorCode`.

**Before (\<= v6.15.0)**  

    try {
      FirebaseMessaging.getInstance().send(message);
    } catch (FirebaseMessagingException ex) {
      if (ex.getErrorCode().equals("registration-token-not-registered")) {
        System.err.println("Device token has been unregistered");
      } else {
        System.err.println("Failed to send the notification");
      }
    }

**Now (\>= v7.0.0)**  

    try {
      FirebaseMessaging.getInstance().send(message);
    } catch (FirebaseMessagingException ex) {
      if (ex.getMessagingErrorCode() == MessagingErrorCode.UNREGISTERED) {
        System.err.println("Device token has been unregistered");
      } else {
        System.err.println("Failed to send the notification");
      }
    }

The`MessagingErrorCode`is in addition to the`ErrorCode`inherited from the base`FirebaseException`type. You can implement error handling logic that inspects both error codes if necessary.

## Authenticationcustom claims

The deprecated`FirebaseAuth.setCustomClaims()`method has been removed. Use the`FirebaseAuth.setCustomUserClaims()`instead.

**Before (\<= v6.15.0)**  

    FirebaseAuth.getInstance().setCustomClaims(uid, claims);

**Now (\>= v7.0.0)**  

    FirebaseAuth.getInstance().setCustomUserClaims(uid, claims);

## FCMnotification constructors

The deprecated constructors of the`Notification`class have been removed. Use the`Notification.Builder`class to create new instances.

**Before (\<= v6.15.0)**  

    Notification notification = new Notification(title, body, url);

**Now (\>= v7.0.0)**  

    Notification notification = Notification.builder()
      .setTitle(title)
      .setBody(body)
      .setImage(url)
      .build();