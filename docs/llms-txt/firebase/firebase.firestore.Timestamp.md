# Source: https://firebase.google.com/docs/reference/node/firebase.firestore.Timestamp.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Timestamp.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.firestore.Timestamp.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Timestamp.md.txt

# Timestamp | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [firestore](https://firebase.google.com/docs/reference/js/v8/firebase.firestore).
- Timestamp

A Timestamp represents a point in time independent of any time zone or
calendar, represented as seconds and fractions of seconds at nanosecond
resolution in UTC Epoch time.

It is encoded using the Proleptic Gregorian
Calendar which extends the Gregorian calendar backwards to year one. It is
encoded assuming all minutes are 60 seconds long, i.e. leap seconds are
"smeared" so that no leap second table is needed for interpretation. Range is
from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59.999999999Z.

see

:   <https://github.com/google/protobuf/blob/master/src/google/protobuf/timestamp.proto>

## Index

### Constructors

- [constructor](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Timestamp#constructor)

### Properties

- [nanoseconds](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Timestamp#nanoseconds)
- [seconds](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Timestamp#seconds)

### Methods

- [isEqual](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Timestamp#isequal)
- [toDate](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Timestamp#todate)
- [toMillis](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Timestamp#tomillis)
- [valueOf](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Timestamp#valueof)
- [fromDate](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Timestamp#fromdate)
- [fromMillis](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Timestamp#frommillis)
- [now](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Timestamp#now)

## Constructors

### constructor

- new Timestamp ( seconds : number , nanoseconds : number ) : [Timestamp](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Timestamp)
- Creates a new timestamp.

  #### Parameters

  -

    ##### seconds: number

    The number of seconds of UTC time since Unix epoch
    1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to
    9999-12-31T23:59:59Z inclusive.
  -

    ##### nanoseconds: number

    The non-negative fractions of a second at nanosecond
    resolution. Negative second values with fractions must still have
    non-negative nanoseconds values that count forward in time. Must be
    from 0 to 999,999,999 inclusive.

  #### Returns [Timestamp](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Timestamp)

## Properties

### nanoseconds

nanoseconds: number

### seconds

seconds: number

## Methods

### isEqual

- isEqual ( other : [Timestamp](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Timestamp) ) : boolean
- Returns true if this `Timestamp` is equal to the provided one.

  #### Parameters

  -

    ##### other: [Timestamp](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Timestamp)

    The `Timestamp` to compare against.

  #### Returns boolean

  true if this `Timestamp` is equal to the provided one.

### toDate

- toDate ( ) : Date
- Convert a Timestamp to a JavaScript `Date` object. This conversion causes
  a loss of precision since `Date` objects only support millisecond precision.

  #### Returns Date

  JavaScript `Date` object representing the same point in time as
  this `Timestamp`, with millisecond precision.

### toMillis

- toMillis ( ) : number
- Convert a timestamp to a numeric timestamp (in milliseconds since epoch).
  This operation causes a loss of precision.

  #### Returns number

  The point in time corresponding to this timestamp, represented as
  the number of milliseconds since Unix epoch 1970-01-01T00:00:00Z.

### valueOf

- valueOf ( ) : string
- Converts this object to a primitive string, which allows Timestamp objects to be compared
  using the `>`, `<=`, `>=` and `>` operators.

  #### Returns string

### Static fromDate

- fromDate ( date : Date ) : [Timestamp](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Timestamp)
- Creates a new timestamp from the given date.

  #### Parameters

  -

    ##### date: Date

    The date to initialize the `Timestamp` from.

  #### Returns [Timestamp](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Timestamp)

  A new `Timestamp` representing the same point in time as the given
  date.

### Static fromMillis

- fromMillis ( milliseconds : number ) : [Timestamp](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Timestamp)
- Creates a new timestamp from the given number of milliseconds.

  #### Parameters

  -

    ##### milliseconds: number

    Number of milliseconds since Unix epoch
    1970-01-01T00:00:00Z.

  #### Returns [Timestamp](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Timestamp)

  A new `Timestamp` representing the same point in time as the given
  number of milliseconds.

### Static now

- now ( ) : [Timestamp](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Timestamp)
- Creates a new timestamp with the current date, with millisecond precision.

  #### Returns [Timestamp](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Timestamp)

a new timestamp representing the current date.