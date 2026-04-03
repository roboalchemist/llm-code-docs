# Source: https://firebase.google.com/docs/reference/js/firestore_lite.geopoint.md.txt

# GeoPoint class

An immutable object representing a geographic location in Firestore. The location is represented as latitude/longitude pair.

Latitude values are in the range of \[-90, 90\]. Longitude values are in the range of \[-180, 180\].

**Signature:**  

    export declare class GeoPoint 

## Constructors

|                                                            Constructor                                                             | Modifiers |                                        Description                                         |
|------------------------------------------------------------------------------------------------------------------------------------|-----------|--------------------------------------------------------------------------------------------|
| [(constructor)(latitude, longitude)](https://firebase.google.com/docs/reference/js/firestore_lite.geopoint.md#geopointconstructor) |           | Creates a new immutable `GeoPoint` object with the provided latitude and longitude values. |

## Properties

|                                                Property                                                 | Modifiers |  Type  |                Description                 |
|---------------------------------------------------------------------------------------------------------|-----------|--------|--------------------------------------------|
| [latitude](https://firebase.google.com/docs/reference/js/firestore_lite.geopoint.md#geopointlatitude)   |           | number | The latitude of this `GeoPoint` instance.  |
| [longitude](https://firebase.google.com/docs/reference/js/firestore_lite.geopoint.md#geopointlongitude) |           | number | The longitude of this `GeoPoint` instance. |

## Methods

|                                                   Method                                                    | Modifiers |                                                                             Description                                                                              |
|-------------------------------------------------------------------------------------------------------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [fromJSON(json)](https://firebase.google.com/docs/reference/js/firestore_lite.geopoint.md#geopointfromjson) | `static`  | Builds a `GeoPoint` instance from a JSON object created by [GeoPoint.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.geopoint.md#geopointtojson). |
| [isEqual(other)](https://firebase.google.com/docs/reference/js/firestore_lite.geopoint.md#geopointisequal)  |           | Returns true if this `GeoPoint` is equal to the provided one.                                                                                                        |
| [toJSON()](https://firebase.google.com/docs/reference/js/firestore_lite.geopoint.md#geopointtojson)         |           | Returns a JSON-serializable representation of this `GeoPoint` instance.                                                                                              |

## GeoPoint.(constructor)

Creates a new immutable `GeoPoint` object with the provided latitude and longitude values.

**Signature:**  

    constructor(latitude: number, longitude: number);

#### Parameters

| Parameter |  Type  |                  Description                  |
|-----------|--------|-----------------------------------------------|
| latitude  | number | The latitude as number between -90 and 90.    |
| longitude | number | The longitude as number between -180 and 180. |

## GeoPoint.latitude

The latitude of this `GeoPoint` instance.

**Signature:**  

    get latitude(): number;

## GeoPoint.longitude

The longitude of this `GeoPoint` instance.

**Signature:**  

    get longitude(): number;

## GeoPoint.fromJSON()

Builds a `GeoPoint` instance from a JSON object created by [GeoPoint.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.geopoint.md#geopointtojson).

**Signature:**  

    static fromJSON(json: object): GeoPoint;

#### Parameters

| Parameter |  Type  |                     Description                     |
|-----------|--------|-----------------------------------------------------|
| json      | object | a JSON object represention of a `GeoPoint` instance |

**Returns:**

[GeoPoint](https://firebase.google.com/docs/reference/js/firestore_lite.geopoint.md#geopoint_class)

an instance of [GeoPoint](https://firebase.google.com/docs/reference/js/firestore_.geopoint.md#geopoint_class) if the JSON object could be parsed. Throws a [FirestoreError](https://firebase.google.com/docs/reference/js/firestore_.firestoreerror.md#firestoreerror_class) if an error occurs.

## GeoPoint.isEqual()

Returns true if this `GeoPoint` is equal to the provided one.

**Signature:**  

    isEqual(other: GeoPoint): boolean;

#### Parameters

| Parameter |                                                Type                                                 |            Description             |
|-----------|-----------------------------------------------------------------------------------------------------|------------------------------------|
| other     | [GeoPoint](https://firebase.google.com/docs/reference/js/firestore_lite.geopoint.md#geopoint_class) | The `GeoPoint` to compare against. |

**Returns:**

boolean

true if this `GeoPoint` is equal to the provided one.

## GeoPoint.toJSON()

Returns a JSON-serializable representation of this `GeoPoint` instance.

**Signature:**  

    toJSON(): {
            latitude: number;
            longitude: number;
            type: string;
        };

**Returns:**

{ latitude: number; longitude: number; type: string; }

a JSON representation of this object.