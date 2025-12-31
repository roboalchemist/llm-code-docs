# Source: https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Classes/FIRFunctions.md.txt

# FirebaseFunctions Framework Reference

# FIRFunctions


    @interface FIRFunctions : NSObject

`Functions` is the client for Cloud Functions for a Firebase project.
- `
  ``
  ``
  `

  ### [+functions](https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Classes/FIRFunctions#/c:@M@FirebaseFunctions@objc(cs)FIRFunctions(cm)functions)

  `
  `  
  Creates a Cloud Functions client using the default or returns a pre-existing instance if it already exists.

  returns:
  A shared Functions instance initialized with the default `FirebaseApp`.  

  #### Declaration

  Objective-C  

      + (FIRFunctions *_Nonnull)functions;

- `
  ``
  ``
  `

  ### [+functionsForApp:](https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Classes/FIRFunctions#/c:@M@FirebaseFunctions@objc(cs)FIRFunctions(cm)functionsForApp:)

  `
  `  
  Creates a Cloud Functions client with the given app, or returns a pre-existing
  instance if one already exists.
  \\param app The app for the Firebase project.

  returns:
  A shared Functions instance initialized with the specified `FirebaseApp`.  

  #### Declaration

  Objective-C  

      + (FIRFunctions *_Nonnull)functionsForApp:(FIRApp *_Nonnull)app;

- `
  ``
  ``
  `

  ### [+functionsForRegion:](https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Classes/FIRFunctions#/c:@M@FirebaseFunctions@objc(cs)FIRFunctions(cm)functionsForRegion:)

  `
  `  
  Creates a Cloud Functions client with the default app and given region.
  \\param region The region for the HTTP trigger, such as `us-central1`.

  returns:
  A shared Functions instance initialized with the default `FirebaseApp` and a custom region.  

  #### Declaration

  Objective-C  

      + (FIRFunctions *_Nonnull)functionsForRegion:(NSString *_Nonnull)region;

- `
  ``
  ``
  `

  ### [+functionsForCustomDomain:](https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Classes/FIRFunctions#/c:@M@FirebaseFunctions@objc(cs)FIRFunctions(cm)functionsForCustomDomain:)

  `
  `  
  Creates a Cloud Functions client with the given app and region, or returns a pre-existing
  instance if one already exists.
  \\param customDomain A custom domain for the HTTP trigger, such as "https //mydomain.com".

  returns:
  A shared Functions instance initialized with the default `FirebaseApp` and a custom HTTP trigger domain.  

  #### Declaration

  Objective-C  

      + (FIRFunctions *_Nonnull)functionsForCustomDomain:
          (NSString *_Nonnull)customDomain;

- `
  ``
  ``
  `

  ### [+functionsForApp:region:](https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Classes/FIRFunctions#/c:@M@FirebaseFunctions@objc(cs)FIRFunctions(cm)functionsForApp:region:)

  `
  `  
  Creates a Cloud Functions client with the given app and region, or returns a pre-existing
  instance if one already exists.
  \\param app The app for the Firebase project.

  \\param region The region for the HTTP trigger, such as `us-central1`.

  returns:
  An instance of `Functions` with a custom app and region.  

  #### Declaration

  Objective-C  

      + (FIRFunctions *_Nonnull)functionsForApp:(FIRApp *_Nonnull)app
                                         region:(NSString *_Nonnull)region;

- `
  ``
  ``
  `

  ### [+functionsForApp:customDomain:](https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Classes/FIRFunctions#/c:@M@FirebaseFunctions@objc(cs)FIRFunctions(cm)functionsForApp:customDomain:)

  `
  `  
  Creates a Cloud Functions client with the given app and region, or returns a pre-existing
  instance if one already exists.
  \\param app The app for the Firebase project.

  \\param customDomain A custom domain for the HTTP trigger, such as <https://mydomain.com>.

  returns:
  An instance of `Functions` with a custom app and HTTP trigger domain.  

  #### Declaration

  Objective-C  

      + (FIRFunctions *_Nonnull)functionsForApp:(FIRApp *_Nonnull)app
                                   customDomain:(NSString *_Nonnull)customDomain;

- `
  ``
  ``
  `

  ### [-HTTPSCallableWithName:](https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Classes/FIRFunctions#/c:@M@FirebaseFunctions@objc(cs)FIRFunctions(im)HTTPSCallableWithName:)

  `
  `  
  Creates a reference to the Callable HTTPS trigger with the given name.
  \\param name The name of the Callable HTTPS trigger.  

  #### Declaration

  Objective-C  

      - (https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Classes/FIRHTTPSCallable.html *_Nonnull)HTTPSCallableWithName:(NSString *_Nonnull)name;

- `
  ``
  ``
  `

  ### [-HTTPSCallableWithURL:](https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Classes/FIRFunctions#/c:@M@FirebaseFunctions@objc(cs)FIRFunctions(im)HTTPSCallableWithURL:)

  `
  `  
  Undocumented  

  #### Declaration

  Objective-C  

      - (https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Classes/FIRHTTPSCallable.html * _Nonnull)HTTPSCallableWithURL:(NSURL * _Nonnull)url SWIFT_WARN_UNUSED_RESULT;

- `
  ``
  ``
  `

  ### [-useEmulatorWithHost:port:](https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Classes/FIRFunctions#/c:@M@FirebaseFunctions@objc(cs)FIRFunctions(im)useEmulatorWithHost:port:)

  `
  `  
  Changes this instance to point to a Cloud Functions emulator running locally.
  See <https://firebase.google.com/docs/functions/local-emulator>
  \\param host The host of the local emulator, such as "localhost".

  \\param port The port of the local emulator, for example 5005.  

  #### Declaration

  Objective-C  

      - (void)useEmulatorWithHost:(NSString *_Nonnull)host port:(NSInteger)port;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Classes/FIRFunctions#/c:@M@FirebaseFunctions@objc(cs)FIRFunctions(im)init)

  `
  `  
  Undocumented  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init SWIFT_UNAVAILABLE;

- `
  ``
  ``
  `

  ### [+new](https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Classes/FIRFunctions#/c:@M@FirebaseFunctions@objc(cs)FIRFunctions(cm)new)

  `
  `  
  Undocumented  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)new SWIFT_UNAVAILABLE_MSG("-init is unavailable");