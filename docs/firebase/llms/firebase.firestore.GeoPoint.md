# Source: https://firebase.google.com/docs/reference/node/firebase.firestore.GeoPoint.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.firestore.GeoPoint.md.txt

# GeoPoint | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [firestore](https://firebase.google.com/docs/reference/js/v8/firebase.firestore).
- GeoPoint

An immutable object representing a geo point in Firestore. The geo point
is represented as latitude/longitude pair.

Latitude values are in the range of \[-90, 90\].
Longitude values are in the range of \[-180, 180\].

## Index

### Constructors

- [constructor](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.GeoPoint#constructor)

### Properties

- [latitude](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.GeoPoint#latitude)
- [longitude](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.GeoPoint#longitude)

### Methods

- [isEqual](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.GeoPoint#isequal)

## Constructors

### constructor

- new GeoPoint ( latitude : number , longitude : number ) : [GeoPoint](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.GeoPoint)
- Creates a new immutable GeoPoint object with the provided latitude and
  longitude values.

  #### Parameters

  -

    ##### latitude: number

    The latitude as number between -90 and 90.
  -

    ##### longitude: number

    The longitude as number between -180 and 180.

  #### Returns [GeoPoint](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.GeoPoint)

## Properties

### latitude

latitude: number  
The latitude of this GeoPoint instance.

### longitude

longitude: number  
The longitude of this GeoPoint instance.

## Methods

### isEqual

- isEqual ( other : [GeoPoint](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.GeoPoint) ) : boolean
- Returns true if this `GeoPoint` is equal to the provided one.

  #### Parameters

  -

    ##### other: [GeoPoint](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.GeoPoint)

    The `GeoPoint` to compare against.

  #### Returns boolean

true if this `GeoPoint` is equal to the provided one.