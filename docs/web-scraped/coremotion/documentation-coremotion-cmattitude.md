# Source: https://developer.apple.com/documentation/coremotion/cmattitude

Title: CMAttitude | Apple Developer Documentation

URL Source: https://developer.apple.com/documentation/coremotion/cmattitude

Markdown Content:
[Overview](https://developer.apple.com/documentation/coremotion/cmattitude#overview)
------------------------------------------------------------------------------------

The `CMAttitude` class offers three different mathematical representations of attitude: a rotation matrix, a quaternion, and Euler angles (roll, pitch, and yaw values). You access `CMAttitude` objects through the attitude property of each [`CMDeviceMotion`](https://developer.apple.com/documentation/coremotion/cmdevicemotion) objects passed to an application. An application starts receiving these device-motion objects as a result of calling the [`startDeviceMotionUpdates(using:to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(using:to:withhandler:)) method, the [`startDeviceMotionUpdates(to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(to:withhandler:)) method, the [`startDeviceMotionUpdates(using:)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(using:)) method, or the [`startDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates()) method of the [`CMMotionManager`](https://developer.apple.com/documentation/coremotion/cmmotionmanager) class.

[Topics](https://developer.apple.com/documentation/coremotion/cmattitude#topics)
--------------------------------------------------------------------------------

### [Getting a Mathematical Representation of Attitude as Euler Angles](https://developer.apple.com/documentation/coremotion/cmattitude#Getting-a-Mathematical-Representation-of-Attitude-as-Euler-Angles)

[`var roll: Double`](https://developer.apple.com/documentation/coremotion/cmattitude/roll)

The roll of the device, in radians.

[`var pitch: Double`](https://developer.apple.com/documentation/coremotion/cmattitude/pitch)

The pitch of the device, in radians.

[`var yaw: Double`](https://developer.apple.com/documentation/coremotion/cmattitude/yaw)

The yaw of the device, in radians.

### [Getting a Mathematical Representation of Attitude as a Rotation Matrix](https://developer.apple.com/documentation/coremotion/cmattitude#Getting-a-Mathematical-Representation-of-Attitude-as-a-Rotation-Matrix)

[`var rotationMatrix: CMRotationMatrix`](https://developer.apple.com/documentation/coremotion/cmattitude/rotationmatrix)

Returns a rotation matrix representing the device’s attitude.

[`struct CMRotationMatrix`](https://developer.apple.com/documentation/coremotion/cmrotationmatrix)

The type of a structure representing a rotation matrix.

### [Getting a Mathematical Representation of Attitude as a Quaternion](https://developer.apple.com/documentation/coremotion/cmattitude#Getting-a-Mathematical-Representation-of-Attitude-as-a-Quaternion)

[`var quaternion: CMQuaternion`](https://developer.apple.com/documentation/coremotion/cmattitude/quaternion)

Returns a quaternion representing the device’s attitude.

[`struct CMQuaternion`](https://developer.apple.com/documentation/coremotion/cmquaternion)

The type for a quaternion representing a measurement of attitude.

### [Obtaining the Change in Attitude](https://developer.apple.com/documentation/coremotion/cmattitude#Obtaining-the-Change-in-Attitude)

[`func multiply(byInverseOf: CMAttitude)`](https://developer.apple.com/documentation/coremotion/cmattitude/multiply(byinverseof:))

Yields the change in attitude given a specific attitude.

[Relationships](https://developer.apple.com/documentation/coremotion/cmattitude#relationships)
----------------------------------------------------------------------------------------------

### [Inherits From](https://developer.apple.com/documentation/coremotion/cmattitude#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)

### [Conforms To](https://developer.apple.com/documentation/coremotion/cmattitude#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
*   [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding)
*   [`NSCopying`](https://developer.apple.com/documentation/Foundation/NSCopying)
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
*   [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding)

[See Also](https://developer.apple.com/documentation/coremotion/cmattitude#see-also)
------------------------------------------------------------------------------------

### [Device motion](https://developer.apple.com/documentation/coremotion/cmattitude#Device-motion)

[Getting processed device-motion data](https://developer.apple.com/documentation/coremotion/getting-processed-device-motion-data)

Retrieve motion data that the system processed to remove environmental bias, such as the effects of gravity.

[`class CMDeviceMotion`](https://developer.apple.com/documentation/coremotion/cmdevicemotion)

Encapsulated measurements of the attitude, rotation rate, and acceleration of a device.

[`struct CMAttitudeReferenceFrame`](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe)

Constants that indicate the frame of reference for attitude-related motion data.

[`class CMHeadphoneMotionManager`](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager)

An object that starts and manages headphone motion services.
