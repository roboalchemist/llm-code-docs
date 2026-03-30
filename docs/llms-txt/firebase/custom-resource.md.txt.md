# Source: https://firebase.google.com/docs/app-check/android/custom-resource.md.txt

You can use App Check to protect non-Google custom backend resources for
your app, like your own self-hosted backend. To do so, you'll need to do both of
the following:

- Modify your app client to send an App Check token along with each request to your backend, as described on this page.
- Modify your backend to require a valid App Check token with every request, as described in [Verify App Check tokens from a custom backend](https://firebase.google.com/docs/app-check/custom-resource-backend).

## Before you begin

Add App Check to your app, using either the default
[Play Integrity provider](https://firebase.google.com/docs/app-check/android/play-integrity-provider), or a
[custom provider](https://firebase.google.com/docs/app-check/android/custom-provider).

## Send App Check tokens with backend requests

To ensure your backend requests include a valid, unexpired, App Check token,
wrap each request in a call to `getAppCheckToken()`. The App Check library
will refresh the token if necessary, and you can access the token in the
method's success listener.

Once you have a valid token, send it along with the request to your backend. The
specifics of how you accomplish this are up to you, but *don't send
App Check tokens as part of URLs*, including in query parameters, as this
makes them vulnerable to accidental leakage and interception. The recommended
approach is to send the token in a custom HTTP header.

For example, if you use Retrofit:

### Kotlin

```kotlin
class ApiWithAppCheckExample {
    interface YourExampleBackendService {
        @GET("yourExampleEndpoint")
        fun exampleData(
            @Header("X-Firebase-AppCheck") appCheckToken: String,
        ): Call<List<String>>
    }

    var yourExampleBackendService: YourExampleBackendService = Retrofit.Builder()
        .baseUrl("https://yourbackend.example.com/")
        .build()
        .create(YourExampleBackendService::class.java)

    fun callApiExample() {
        Firebase.appCheck.getAppCheckToken(false).addOnSuccessListener { appCheckToken ->
            val token = appCheckToken.token
            val apiCall = yourExampleBackendService.exampleData(token)
            // ...
        }
    }
}
```

### Java

```java
public class ApiWithAppCheckExample {
    private interface YourExampleBackendService {
        @GET("yourExampleEndpoint")
        Call<List<String>> exampleData(
                @Header("X-Firebase-AppCheck") String appCheckToken);
    }

    YourExampleBackendService yourExampleBackendService = new Retrofit.Builder()
            .baseUrl("https://yourbackend.example.com/")
            .build()
            .create(YourExampleBackendService.class);

    public void callApiExample() {
        FirebaseAppCheck.getInstance()
                .getAppCheckToken(false)
                .addOnSuccessListener(new OnSuccessListener<AppCheckToken>() {
                    @Override
                    public void onSuccess(@NonNull AppCheckToken appCheckToken) {
                        String token = appCheckToken.getToken();
                        Call<List<String>> apiCall =
                                yourExampleBackendService.exampleData(token);
                        // ...
                    }
                });
    }
}
```

### Replay protection (beta)

When making a request to an endpoint for which you've enabled
[replay protection](https://firebase.google.com/docs/app-check/custom-resource-backend#replay-protection),
wrap the request in a call to `getLimitedUseAppCheckToken()` instead of
`getAppCheckToken()`:

### Kotlin

```kotlin
Firebase.appCheck.limitedUseAppCheckToken.addOnSuccessListener {
    // ...
}
```

### Java

```java
FirebaseAppCheck.getInstance()
        .getLimitedUseAppCheckToken().addOnSuccessListener(
                new OnSuccessListener<AppCheckToken>() {
                    @Override
                    public void onSuccess(AppCheckToken appCheckToken) {
                        String token = appCheckToken.getToken();
                        // ...
                    }
                }
        );
```