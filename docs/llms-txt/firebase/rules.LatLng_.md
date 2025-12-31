# Source: https://firebase.google.com/docs/reference/rules/rules.LatLng_.md.txt

# Interface: LatLng

# [rules](https://firebase.google.com/docs/reference/rules/rules).LatLng

interface static

Type representing a geopoint. Used in rules as `latlng`.

## Methods

### distance

distance(other) returns [rules.Float](https://firebase.google.com/docs/reference/rules/rules.Float)

Calculate distance between two LatLng points in distance (meters).

|                                                         #### Parameter                                                         ||
|-------|-------------------------------------------------------------------------------------------------------------------------|
| other | [rules.LatLng](https://firebase.google.com/docs/reference/rules/rules.LatLng_) The other point. Value must not be null. |

Returns

:   `non-null `[rules.Float](https://firebase.google.com/docs/reference/rules/rules.Float) distance in meters.

### latitude

latitude() returns [rules.Float](https://firebase.google.com/docs/reference/rules/rules.Float)

Get the latitude value in the range \[-90.0, 90.0\].

Returns

:   `non-null `[rules.Float](https://firebase.google.com/docs/reference/rules/rules.Float) latitude.

### longitude

longitude() returns [rules.Float](https://firebase.google.com/docs/reference/rules/rules.Float)

Get the longitude value in the range \[-180.0, 180.0\].

Returns

:   `non-null `[rules.Float](https://firebase.google.com/docs/reference/rules/rules.Float) longitude.