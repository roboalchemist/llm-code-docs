# Source: https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfigValue.md.txt

# FirebaseRemoteConfig Framework Reference

# FIRRemoteConfigValue


    @interface FIRRemoteConfigValue : NSObject <NSCopying>

This class provides a wrapper for Remote Config parameter values, with methods to get parameter
values as different data types.
- `
  ``
  ``
  `

  ### [stringValue](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfigValue#/c:objc(cs)FIRRemoteConfigValue(py)stringValue)

  `
  `  
  Gets the value as a string.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nonnull) NSString *stringValue;

- `
  ``
  ``
  `

  ### [numberValue](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfigValue#/c:objc(cs)FIRRemoteConfigValue(py)numberValue)

  `
  `  
  Gets the value as a number value.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nonnull) NSNumber *numberValue;

- `
  ``
  ``
  `

  ### [dataValue](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfigValue#/c:objc(cs)FIRRemoteConfigValue(py)dataValue)

  `
  `  
  Gets the value as a NSData object.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nonnull) NSData *dataValue;

- `
  ``
  ``
  `

  ### [boolValue](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfigValue#/c:objc(cs)FIRRemoteConfigValue(py)boolValue)

  `
  `  
  Gets the value as a boolean.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) BOOL boolValue;

- `
  ``
  ``
  `

  ### [JSONValue](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfigValue#/c:objc(cs)FIRRemoteConfigValue(py)JSONValue)

  `
  `  
  Gets a foundation object (NSDictionary / NSArray) by parsing the value as JSON. This method uses
  NSJSONSerialization's JSONObjectWithData method with an options value of 0.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) id JSONValue;

- `
  ``
  ``
  `

  ### [source](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfigValue#/c:objc(cs)FIRRemoteConfigValue(py)source)

  `
  `  
  Identifies the source of the fetched value.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Enums/FIRRemoteConfigSource.html source;