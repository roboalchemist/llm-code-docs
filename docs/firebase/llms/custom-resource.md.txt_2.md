# Source: https://firebase.google.com/docs/app-check/ios/custom-resource.md.txt

You can use App Check to protect non-Google custom backend resources for
your app, like your own self-hosted backend. To do so, you'll need to do both of
the following:

- Modify your app client to send an App Check token along with each request to your backend, as described on this page.
- Modify your backend to require a valid App Check token with every request, as described in [Verify App Check tokens from a custom backend](https://firebase.google.com/docs/app-check/custom-resource-backend).

## Before you begin

Add App Check to your app, using either [App Attest](https://firebase.google.com/docs/app-check/ios/app-attest-provider),
[DeviceCheck](https://firebase.google.com/docs/app-check/ios/devicecheck-provider), or a [custom provider](https://firebase.google.com/docs/app-check/ios/custom-provider).

## Send App Check tokens with backend requests

To ensure your backend requests include a valid, unexpired, App Check token,
wrap each request in a call to `AppCheck.token()`. The App Check library
will refresh the token if necessary, and you can access the token in the
method's completion block.

Once you have a valid token, send it along with the request to your backend. The
specifics of how you accomplish this are up to you, but *don't send
App Check tokens as part of URLs*, including in query parameters, as this
makes them vulnerable to accidental leakage and interception. The following
example sends the token in a custom HTTP header, which is the recommended
approach.

### Swift

```swift
do {
  let token = try await AppCheck.appCheck().token(forcingRefresh: false)

  // Get the raw App Check token string.
  let tokenString = token.token

  // Include the App Check token with requests to your server.
  let url = URL(string: "https://yourbackend.example.com/yourApiEndpoint")!
  var request = URLRequest(url: url)
  request.httpMethod = "GET"
  request.setValue(tokenString, forHTTPHeaderField: "X-Firebase-AppCheck")

  let task = URLSession.shared.dataTask(with: request) { data, response, error in
      // Handle response from your backend.
  }
  task.resume()
} catch(let error) {
  print("Unable to retrieve App Check token: \(error)")
  return
}
```

### Objective-C

```objective-c
[[FIRAppCheck appCheck] tokenForcingRefresh:NO
                                 completion:^(FIRAppCheckToken * _Nullable token,
                                              NSError * _Nullable error) {
    if (error != nil) {
        // Handle any errors if the token was not retrieved.
        NSLog(@"Unable to retrieve App Check token: %@", error);
        return;
    }
    if (token == nil) {
        NSLog(@"Unable to retrieve App Check token.");
        return;
    }

    // Get the raw App Check token string.
    NSString *tokenString = token.token;

    // Include the App Check token with requests to your server.
    NSURL *url = [[NSURL alloc] initWithString:@"https://yourbackend.example.com/yourApiEndpoint"];
    NSMutableURLRequest *request = [[NSMutableURLRequest alloc] initWithURL:url];
    [request setHTTPMethod:@"GET"];
    [request setValue:tokenString forHTTPHeaderField:@"X-Firebase-AppCheck"];

    NSURLSessionDataTask *task =
        [[NSURLSession sharedSession] dataTaskWithRequest:request
                                        completionHandler:^(NSData * _Nullable data,
                                                            NSURLResponse * _Nullable response,
                                                            NSError * _Nullable error) {
        // Handle response from your backend.
    }];
    [task resume];
}];
```

### Replay protection (beta)

When making a request to an endpoint for which you've enabled
[replay protection](https://firebase.google.com/docs/app-check/custom-resource-backend#replay-protection),
wrap the request in a call to `limitedUseToken()` instead of `token()`:

### Swift

    AppCheck.appCheck().limitedUseToken() { token, error in
      // ...
    }

### Objective-C

    [[FIRAppCheck appCheck] limitedUseTokenWithCompletion:^(FIRAppCheckToken * _Nullable token,
                                                            NSError * _Nullable error) {
        // ...
    }];