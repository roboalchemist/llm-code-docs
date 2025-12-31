# Source: https://firebase.google.com/docs/reference/rules/rules.latlng.md.txt

# Namespace: latlng

# [rules](https://firebase.google.com/docs/reference/rules/rules).latlng

namespace static

Globally available latitude-longitude functions. These functions are accessed using the `latlng.` prefix.

## Method

### value

static

value(lat, lng) returns [rules.LatLng](https://firebase.google.com/docs/reference/rules/rules.LatLng_)

Create a LatLng from floating point coordinates.

|                                                     #### Parameter                                                      ||
|-----|--------------------------------------------------------------------------------------------------------------------|
| lat | [rules.Float](https://firebase.google.com/docs/reference/rules/rules.Float) The latitude. Value must not be null.  |
| lng | [rules.Float](https://firebase.google.com/docs/reference/rules/rules.Float) The longitude. Value must not be null. |

Returns

:   `non-null `[rules.LatLng](https://firebase.google.com/docs/reference/rules/rules.LatLng_) a LatLng.

#### Example

    latlng.value(45.0, 90.0)