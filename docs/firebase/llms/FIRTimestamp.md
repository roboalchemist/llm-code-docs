# Source: https://firebase.google.com/docs/reference/ios/firebasecore/api/reference/Classes/FIRTimestamp.md.txt

# FirebaseCore Framework Reference

# FIRTimestamp


    @interface FIRTimestamp : NSObject <NSCopying>

A Timestamp represents a point in time independent of any time zone or calendar, represented as
seconds and fractions of seconds at nanosecond resolution in UTC Epoch time. It is encoded using
the Proleptic Gregorian Calendar which extends the Gregorian calendar backwards to year one. It
is encoded assuming all minutes are 60 seconds long, i.e. leap seconds are "smeared" so that no
leap second table is needed for interpretation. Range is from 0001-01-01T00:00:00Z to
9999-12-31T23:59:59.999999999Z. By restricting to that range, we ensure that we can convert to
and from RFC 3339 date strings.  
See
<https://github.com/google/protobuf/blob/main/src/google/protobuf/timestamp.proto> for the reference timestamp definition.
- `
  ``
  ``
  `

  ### [-initWithSeconds:nanoseconds:](https://firebase.google.com/docs/reference/ios/firebasecore/api/reference/Classes/FIRTimestamp#/c:objc(cs)FIRTimestamp(im)initWithSeconds:nanoseconds:)

  `
  `  
  Creates a new timestamp.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)initWithSeconds:(int64_t)seconds
                                  nanoseconds:(int32_t)nanoseconds;

  #### Parameters

  |---------------------|----------------------------------------------|
  | ` `*seconds*` `     | the number of seconds since epoch.           |
  | ` `*nanoseconds*` ` | the number of nanoseconds after the seconds. |

- `
  ``
  ``
  `

  ### [+timestampWithSeconds:nanoseconds:](https://firebase.google.com/docs/reference/ios/firebasecore/api/reference/Classes/FIRTimestamp#/c:objc(cs)FIRTimestamp(cm)timestampWithSeconds:nanoseconds:)

  `
  `  
  Creates a new timestamp.  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)timestampWithSeconds:(int64_t)seconds
                                       nanoseconds:(int32_t)nanoseconds;

  #### Parameters

  |---------------------|----------------------------------------------|
  | ` `*seconds*` `     | the number of seconds since epoch.           |
  | ` `*nanoseconds*` ` | the number of nanoseconds after the seconds. |

- `
  ``
  ``
  `

  ### [+timestampWithDate:](https://firebase.google.com/docs/reference/ios/firebasecore/api/reference/Classes/FIRTimestamp#/c:objc(cs)FIRTimestamp(cm)timestampWithDate:)

  `
  `  
  Creates a new timestamp from the given date.  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)timestampWithDate:(nonnull NSDate *)date;

- `
  ``
  ``
  `

  ### [+timestamp](https://firebase.google.com/docs/reference/ios/firebasecore/api/reference/Classes/FIRTimestamp#/c:objc(cs)FIRTimestamp(cm)timestamp)

  `
  `  
  Creates a new timestamp with the current date / time.  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)timestamp;

- `
  ``
  ``
  `

  ### [-dateValue](https://firebase.google.com/docs/reference/ios/firebasecore/api/reference/Classes/FIRTimestamp#/c:objc(cs)FIRTimestamp(im)dateValue)

  `
  `  
  Returns a new `Date` corresponding to this timestamp. This may lose precision.  

  #### Declaration

  Objective-C  

      - (nonnull NSDate *)dateValue;

- `
  ``
  ``
  `

  ### [-compare:](https://firebase.google.com/docs/reference/ios/firebasecore/api/reference/Classes/FIRTimestamp#/c:objc(cs)FIRTimestamp(im)compare:)

  `
  `  
  Returns the result of comparing the receiver with another timestamp.  

  #### Declaration

  Objective-C  

      - (NSComparisonResult)compare:(nonnull FIRTimestamp *)other;

  #### Parameters

  |---------------|---------------------------------|
  | ` `*other*` ` | the other timestamp to compare. |

  #### Return Value

  `orderedAscending` if `other` is chronologically following self,
  `orderedDescending` if `other` is chronologically preceding self,
  `orderedSame` otherwise.
- `
  ``
  ``
  `

  ### [seconds](https://firebase.google.com/docs/reference/ios/firebasecore/api/reference/Classes/FIRTimestamp#/c:objc(cs)FIRTimestamp(py)seconds)

  `
  `  
  Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z.
  Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) int64_t seconds;

- `
  ``
  ``
  `

  ### [nanoseconds](https://firebase.google.com/docs/reference/ios/firebasecore/api/reference/Classes/FIRTimestamp#/c:objc(cs)FIRTimestamp(py)nanoseconds)

  `
  `  
  Non-negative fractions of a second at nanosecond resolution. Negative second values with
  fractions must still have non-negative nanos values that count forward in time.
  Must be from 0 to 999,999,999 inclusive.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) int32_t nanoseconds;