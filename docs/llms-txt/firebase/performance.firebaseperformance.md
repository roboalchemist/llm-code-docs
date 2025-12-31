# Source: https://firebase.google.com/docs/reference/js/performance.firebaseperformance.md.txt

# FirebasePerformance interface

The Firebase Performance Monitoring service interface.

**Signature:**  

    export interface FirebasePerformance 

## Properties

|                                                                       Property                                                                       |                                                 Type                                                  |                                                                            Description                                                                            |
|------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [app](https://firebase.google.com/docs/reference/js/performance.firebaseperformance.md#firebaseperformanceapp)                                       | [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) | The [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) this `FirebasePerformance` instance is associated with. |
| [dataCollectionEnabled](https://firebase.google.com/docs/reference/js/performance.firebaseperformance.md#firebaseperformancedatacollectionenabled)   | boolean                                                                                               | Controls the logging of custom traces.                                                                                                                            |
| [instrumentationEnabled](https://firebase.google.com/docs/reference/js/performance.firebaseperformance.md#firebaseperformanceinstrumentationenabled) | boolean                                                                                               | Controls the logging of automatic traces and HTTP/S network monitoring.                                                                                           |

## FirebasePerformance.app

The [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) this `FirebasePerformance` instance is associated with.

**Signature:**  

    app: FirebaseApp;

## FirebasePerformance.dataCollectionEnabled

Controls the logging of custom traces.

**Signature:**  

    dataCollectionEnabled: boolean;

## FirebasePerformance.instrumentationEnabled

Controls the logging of automatic traces and HTTP/S network monitoring.

**Signature:**  

    instrumentationEnabled: boolean;