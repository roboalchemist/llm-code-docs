# Source: https://firebase.google.com/docs/reference/js/firestore_lite.timestamp.md.txt

# Timestamp class

A `Timestamp` represents a point in time independent of any time zone or calendar, represented as seconds and fractions of seconds at nanosecond resolution in UTC Epoch time.

It is encoded using the Proleptic Gregorian Calendar which extends the Gregorian calendar backwards to year one. It is encoded assuming all minutes are 60 seconds long, i.e. leap seconds are "smeared" so that no leap second table is needed for interpretation. Range is from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59.999999999Z.

For examples and further specifications, refer to the [Timestamp definition](https://github.com/google/protobuf/blob/master/src/google/protobuf/timestamp.proto).

**Signature:**  

    export declare class Timestamp 

## Constructors

|                                                              Constructor                                                              | Modifiers |       Description        |
|---------------------------------------------------------------------------------------------------------------------------------------|-----------|--------------------------|
| [(constructor)(seconds, nanoseconds)](https://firebase.google.com/docs/reference/js/firestore_lite.timestamp.md#timestampconstructor) |           | Creates a new timestamp. |

## Properties

|                                                   Property                                                    | Modifiers |  Type  |                               Description                                |
|---------------------------------------------------------------------------------------------------------------|-----------|--------|--------------------------------------------------------------------------|
| [nanoseconds](https://firebase.google.com/docs/reference/js/firestore_lite.timestamp.md#timestampnanoseconds) |           | number | The fractions of a second at nanosecond resolution.\*                    |
| [seconds](https://firebase.google.com/docs/reference/js/firestore_lite.timestamp.md#timestampseconds)         |           | number | The number of seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. |

## Methods

|                                                          Method                                                           | Modifiers |                                                                               Description                                                                                |
|---------------------------------------------------------------------------------------------------------------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [fromDate(date)](https://firebase.google.com/docs/reference/js/firestore_lite.timestamp.md#timestampfromdate)             | `static`  | Creates a new timestamp from the given date.                                                                                                                             |
| [fromJSON(json)](https://firebase.google.com/docs/reference/js/firestore_lite.timestamp.md#timestampfromjson)             | `static`  | Builds a `Timestamp` instance from a JSON object created by [Timestamp.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.timestamp.md#timestamptojson). |
| [fromMillis(milliseconds)](https://firebase.google.com/docs/reference/js/firestore_lite.timestamp.md#timestampfrommillis) | `static`  | Creates a new timestamp from the given number of milliseconds.                                                                                                           |
| [isEqual(other)](https://firebase.google.com/docs/reference/js/firestore_lite.timestamp.md#timestampisequal)              |           | Returns true if this `Timestamp` is equal to the provided one.                                                                                                           |
| [now()](https://firebase.google.com/docs/reference/js/firestore_lite.timestamp.md#timestampnow)                           | `static`  | Creates a new timestamp with the current date, with millisecond precision.                                                                                               |
| [toDate()](https://firebase.google.com/docs/reference/js/firestore_lite.timestamp.md#timestamptodate)                     |           | Converts a `Timestamp` to a JavaScript `Date` object. This conversion causes a loss of precision since `Date` objects only support millisecond precision.                |
| [toJSON()](https://firebase.google.com/docs/reference/js/firestore_lite.timestamp.md#timestamptojson)                     |           | Returns a JSON-serializable representation of this `Timestamp`.                                                                                                          |
| [toMillis()](https://firebase.google.com/docs/reference/js/firestore_lite.timestamp.md#timestamptomillis)                 |           | Converts a `Timestamp` to a numeric timestamp (in milliseconds since epoch). This operation causes a loss of precision.                                                  |
| [toString()](https://firebase.google.com/docs/reference/js/firestore_lite.timestamp.md#timestamptostring)                 |           | Returns a textual representation of this `Timestamp`.                                                                                                                    |
| [valueOf()](https://firebase.google.com/docs/reference/js/firestore_lite.timestamp.md#timestampvalueof)                   |           | Converts this object to a primitive string, which allows `Timestamp` objects to be compared using the `>`, `<=`, `>=` and `>` operators.                                 |

## Timestamp.(constructor)

Creates a new timestamp.

**Signature:**  

    constructor(
        seconds: number, 
        nanoseconds: number);

#### Parameters

|  Parameter  |  Type  |                                                                                                         Description                                                                                                         |
|-------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| seconds     | number | The number of seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive.                                                                               |
| nanoseconds | number | The non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanoseconds values that count forward in time. Must be from 0 to 999,999,999 inclusive. |

## Timestamp.nanoseconds

The fractions of a second at nanosecond resolution.\*

**Signature:**  

    readonly nanoseconds: number;

## Timestamp.seconds

The number of seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z.

**Signature:**  

    readonly seconds: number;

## Timestamp.fromDate()

Creates a new timestamp from the given date.

**Signature:**  

    static fromDate(date: Date): Timestamp;

#### Parameters

| Parameter | Type |                 Description                  |
|-----------|------|----------------------------------------------|
| date      | Date | The date to initialize the `Timestamp` from. |

**Returns:**

[Timestamp](https://firebase.google.com/docs/reference/js/firestore_lite.timestamp.md#timestamp_class)

A new `Timestamp` representing the same point in time as the given date.

## Timestamp.fromJSON()

Builds a `Timestamp` instance from a JSON object created by [Timestamp.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.timestamp.md#timestamptojson).

**Signature:**  

    static fromJSON(json: object): Timestamp;

#### Parameters

| Parameter |  Type  | Description |
|-----------|--------|-------------|
| json      | object |             |

**Returns:**

[Timestamp](https://firebase.google.com/docs/reference/js/firestore_lite.timestamp.md#timestamp_class)

## Timestamp.fromMillis()

Creates a new timestamp from the given number of milliseconds.

**Signature:**  

    static fromMillis(milliseconds: number): Timestamp;

#### Parameters

|  Parameter   |  Type  |                          Description                          |
|--------------|--------|---------------------------------------------------------------|
| milliseconds | number | Number of milliseconds since Unix epoch 1970-01-01T00:00:00Z. |

**Returns:**

[Timestamp](https://firebase.google.com/docs/reference/js/firestore_lite.timestamp.md#timestamp_class)

A new `Timestamp` representing the same point in time as the given number of milliseconds.

## Timestamp.isEqual()

Returns true if this `Timestamp` is equal to the provided one.

**Signature:**  

    isEqual(other: Timestamp): boolean;

#### Parameters

| Parameter |                                                  Type                                                  |             Description             |
|-----------|--------------------------------------------------------------------------------------------------------|-------------------------------------|
| other     | [Timestamp](https://firebase.google.com/docs/reference/js/firestore_lite.timestamp.md#timestamp_class) | The `Timestamp` to compare against. |

**Returns:**

boolean

true if this `Timestamp` is equal to the provided one.

## Timestamp.now()

Creates a new timestamp with the current date, with millisecond precision.

**Signature:**  

    static now(): Timestamp;

**Returns:**

[Timestamp](https://firebase.google.com/docs/reference/js/firestore_lite.timestamp.md#timestamp_class)

a new timestamp representing the current date.

## Timestamp.toDate()

Converts a `Timestamp` to a JavaScript `Date` object. This conversion causes a loss of precision since `Date` objects only support millisecond precision.

**Signature:**  

    toDate(): Date;

**Returns:**

Date

JavaScript `Date` object representing the same point in time as this `Timestamp`, with millisecond precision.

## Timestamp.toJSON()

Returns a JSON-serializable representation of this `Timestamp`.

**Signature:**  

    toJSON(): {
            seconds: number;
            nanoseconds: number;
            type: string;
        };

**Returns:**

{ seconds: number; nanoseconds: number; type: string; }

## Timestamp.toMillis()

Converts a `Timestamp` to a numeric timestamp (in milliseconds since epoch). This operation causes a loss of precision.

**Signature:**  

    toMillis(): number;

**Returns:**

number

The point in time corresponding to this timestamp, represented as the number of milliseconds since Unix epoch 1970-01-01T00:00:00Z.

## Timestamp.toString()

Returns a textual representation of this `Timestamp`.

**Signature:**  

    toString(): string;

**Returns:**

string

## Timestamp.valueOf()

Converts this object to a primitive string, which allows `Timestamp` objects to be compared using the `>`, `<=`, `>=` and `>` operators.

**Signature:**  

    valueOf(): string;

**Returns:**

string