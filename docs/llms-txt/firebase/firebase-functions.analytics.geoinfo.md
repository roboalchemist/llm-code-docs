# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.geoinfo.md.txt

# analytics.GeoInfo interface

Interface representing the geographic origin of the events.

**Signature:**  

    export interface GeoInfo 

## Properties

|                                                              Property                                                               |  Type  |                     Description                      |
|-------------------------------------------------------------------------------------------------------------------------------------|--------|------------------------------------------------------|
| [city](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.geoinfo.md#analyticsgeoinfocity)           | string | The geographic city.Example: "Sao Paulo".            |
| [continent](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.geoinfo.md#analyticsgeoinfocontinent) | string | The geographic continent.Example: "South America".   |
| [country](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.geoinfo.md#analyticsgeoinfocountry)     | string | The geographic country.Example: "Brazil".            |
| [region](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.geoinfo.md#analyticsgeoinforegion)       | string | The geographic region.Example: "State of Sao Paulo". |

## analytics.GeoInfo.city

The geographic city.

Example: "Sao Paulo".

**Signature:**  

    city?: string;

## analytics.GeoInfo.continent

The geographic continent.

Example: "South America".

**Signature:**  

    continent?: string;

## analytics.GeoInfo.country

The geographic country.

Example: "Brazil".

**Signature:**  

    country?: string;

## analytics.GeoInfo.region

The geographic region.

Example: "State of Sao Paulo".

**Signature:**  

    region?: string;