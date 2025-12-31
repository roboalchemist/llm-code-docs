# Source: https://firebase.google.com/docs/reference/ios/firebasecore/api/reference/Classes/FIROptions.md.txt

# FIROptions


    @interface FIROptions : NSObject <NSCopying>

This class provides constant fields of Google APIs.
- `
  ``
  ``
  `

  ### [+defaultOptions](https://firebase.google.com/docs/reference/ios/firebasecore/api/reference/Classes/FIROptions#/c:objc(cs)FIROptions(cm)defaultOptions)

  `
  `  
  Returns the default options. The first time this is called it synchronously reads GoogleService-Info.plist from disk.  

  #### Declaration

  Objective-C  

      + (nullable FIROptions *)defaultOptions;

- `
  ``
  ``
  `

  ### [APIKey](https://firebase.google.com/docs/reference/ios/firebasecore/api/reference/Classes/FIROptions#/c:objc(cs)FIROptions(py)APIKey)

  `
  `  
  An API key used for authenticating requests from your Apple app, e.g. The key must begin with "A" and contain exactly 39 alphanumeric characters, used to identify your app to Google servers.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, nullable) NSString *APIKey;

- `
  ``
  ``
  `

  ### [bundleID](https://firebase.google.com/docs/reference/ios/firebasecore/api/reference/Classes/FIROptions#/c:objc(cs)FIROptions(py)bundleID)

  `
  `  
  The bundle ID for the application. Defaults to`Bundle.main.bundleIdentifier`when not set manually or in a plist.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy) NSString *_Nonnull bundleID;

- `
  ``
  ``
  `

  ### [clientID](https://firebase.google.com/docs/reference/ios/firebasecore/api/reference/Classes/FIROptions#/c:objc(cs)FIROptions(py)clientID)

  `
  `  
  The OAuth2 client ID for Apple applications used to authenticate Google users, for example @"12345.apps.googleusercontent.com", used for signing in with Google.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, nullable) NSString *clientID;

- `
  ``
  ``
  `

  ### [GCMSenderID](https://firebase.google.com/docs/reference/ios/firebasecore/api/reference/Classes/FIROptions#/c:objc(cs)FIROptions(py)GCMSenderID)

  `
  `  
  The Project Number from the Google Developer's console, for example @"012345678901", used to configure Firebase Cloud Messaging.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy) NS_SWIFT_NAME NSString *GCMSenderID;

- `
  ``
  ``
  `

  ### [projectID](https://firebase.google.com/docs/reference/ios/firebasecore/api/reference/Classes/FIROptions#/c:objc(cs)FIROptions(py)projectID)

  `
  `  
  The Project ID from the Firebase console, for example @"abc-xyz-123".  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, nullable) NSString *projectID;

- `
  ``
  ``
  `

  ### [googleAppID](https://firebase.google.com/docs/reference/ios/firebasecore/api/reference/Classes/FIROptions#/c:objc(cs)FIROptions(py)googleAppID)

  `
  `  
  The Google App ID that is used to uniquely identify an instance of an app.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy) NSString *_Nonnull googleAppID;

- `
  ``
  ``
  `

  ### [databaseURL](https://firebase.google.com/docs/reference/ios/firebasecore/api/reference/Classes/FIROptions#/c:objc(cs)FIROptions(py)databaseURL)

  `
  `  
  The database root URL, e.g. @"<http://abc-xyz-123.firebaseio.com>".  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, nullable) NSString *databaseURL;

- `
  ``
  ``
  `

  ### [storageBucket](https://firebase.google.com/docs/reference/ios/firebasecore/api/reference/Classes/FIROptions#/c:objc(cs)FIROptions(py)storageBucket)

  `
  `  
  The Google Cloud Storage bucket name, e.g. @"abc-xyz-123.storage.firebase.com".  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, nullable) NSString *storageBucket;

- `
  ``
  ``
  `

  ### [appGroupID](https://firebase.google.com/docs/reference/ios/firebasecore/api/reference/Classes/FIROptions#/c:objc(cs)FIROptions(py)appGroupID)

  `
  `  
  The App Group identifier to share data between the application and the application extensions. The App Group must be configured in the application and on the Apple Developer Portal. Default value`nil`.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, nullable) NSString *appGroupID;

- `
  ``
  ``
  `

  ### [-initWithContentsOfFile:](https://firebase.google.com/docs/reference/ios/firebasecore/api/reference/Classes/FIROptions#/c:objc(cs)FIROptions(im)initWithContentsOfFile:)

  `
  `  
  Initializes a customized instance of FirebaseOptions from the file at the given plist file path. This will read the file synchronously from disk. For example:  

        if let path = Bundle.main.path(forResource:"GoogleService-Info", ofType:"plist") {
            let options = FirebaseOptions(contentsOfFile: path)
        }

  Note that it is not possible to customize`FirebaseOptions`for Firebase Analytics which expects a static file named`GoogleService-Info.plist`-<https://github.com/firebase/firebase-ios-sdk/issues/230>. Returns`nil`if the plist file does not exist or is invalid.  

  #### Declaration

  Objective-C  

      - (nullable instancetype)initWithContentsOfFile:(nonnull NSString *)plistPath;

- `
  ``
  ``
  `

  ### [-initWithGoogleAppID:GCMSenderID:](https://firebase.google.com/docs/reference/ios/firebasecore/api/reference/Classes/FIROptions#/c:objc(cs)FIROptions(im)initWithGoogleAppID:GCMSenderID:)

  `
  `  
  Initializes a customized instance of`FirebaseOptions`with required fields. Use the mutable properties to modify fields for configuring specific services. Note that it is not possible to customize`FirebaseOptions`for Firebase Analytics which expects a static file named`GoogleServices-Info.plist`-<https://github.com/firebase/firebase-ios-sdk/issues/230>.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)initWithGoogleAppID:(nonnull NSString *)googleAppID
                                      GCMSenderID:(nonnull NSString *)GCMSenderID;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasecore/api/reference/Classes/FIROptions#/c:objc(cs)FIROptions(im)init)

  `
  `  
  Unavailable  
  Unavailable. Please use`init(contentsOfFile:)`or`init(googleAppID:gcmSenderID:)`instead.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;