# Source: https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfigValue.md.txt

# FirebaseRemoteConfig Framework Reference

# RemoteConfigValue

    class RemoteConfigValue : NSObject, NSCopying

This class provides a wrapper for Remote Config parameter values, with methods to get parameter
values as different data types.
- `


  ### [stringValue](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfigValue#/c:objc(cs)FIRRemoteConfigValue(py)stringValue)


  ` Gets the value as a string.

  #### Declaration

  Swift

      var stringValue: String { get }

- `


  ### [numberValue](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfigValue#/c:objc(cs)FIRRemoteConfigValue(py)numberValue)


  ` Gets the value as a number value.

  #### Declaration

  Swift

      var numberValue: NSNumber { get }

- `


  ### [dataValue](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfigValue#/c:objc(cs)FIRRemoteConfigValue(py)dataValue)


  ` Gets the value as a NSData object.

  #### Declaration

  Swift

      var dataValue: Data { get }

- `


  ### [boolValue](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfigValue#/c:objc(cs)FIRRemoteConfigValue(py)boolValue)


  ` Gets the value as a boolean.

  #### Declaration

  Swift

      var boolValue: Bool { get }

- `


  ### [jsonValue](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfigValue#/c:objc(cs)FIRRemoteConfigValue(py)JSONValue)


  ` Gets a foundation object (NSDictionary / NSArray) by parsing the value as JSON. This method uses
  NSJSONSerialization's JSONObjectWithData method with an options value of 0.

  #### Declaration

  Swift

      var jsonValue: Any? { get }

- `


  ### [source](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfigValue#/c:objc(cs)FIRRemoteConfigValue(py)source)


  ` Identifies the source of the fetched value.

  #### Declaration

  Swift

      var source: https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Enums/RemoteConfigSource.html { get }

- `


  ### [decoded(asType:)](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfigValue#/s:So20FIRRemoteConfigValueC014FirebaseRemoteB0E7decoded6asTypexxm_tKSeRzlF)


  ` Extracts a RemoteConfigValue JSON-encoded object and decodes it to the requested type.

  #### Declaration

  Swift

      func decoded<Value>(asType: Value.Type = Value.self) throws -> Value where Value : Decodable

  #### Parameters

  |---|---|
  | ` asType ` | The type to decode the JSON-object to |