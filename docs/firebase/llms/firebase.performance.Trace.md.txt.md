# Source: https://firebase.google.com/docs/reference/js/v8/firebase.performance.Trace.md.txt

# Trace | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [performance](https://firebase.google.com/docs/reference/js/v8/firebase.performance).
- Trace

## Index

### Methods

- [getAttribute](https://firebase.google.com/docs/reference/js/v8/firebase.performance.Trace#getattribute)
- [getAttributes](https://firebase.google.com/docs/reference/js/v8/firebase.performance.Trace#getattributes)
- [getMetric](https://firebase.google.com/docs/reference/js/v8/firebase.performance.Trace#getmetric)
- [incrementMetric](https://firebase.google.com/docs/reference/js/v8/firebase.performance.Trace#incrementmetric)
- [putAttribute](https://firebase.google.com/docs/reference/js/v8/firebase.performance.Trace#putattribute)
- [putMetric](https://firebase.google.com/docs/reference/js/v8/firebase.performance.Trace#putmetric)
- [record](https://firebase.google.com/docs/reference/js/v8/firebase.performance.Trace#record)
- [removeAttribute](https://firebase.google.com/docs/reference/js/v8/firebase.performance.Trace#removeattribute)
- [start](https://firebase.google.com/docs/reference/js/v8/firebase.performance.Trace#start)
- [stop](https://firebase.google.com/docs/reference/js/v8/firebase.performance.Trace#stop)

## Methods

### getAttribute

- getAttribute ( attr : string ) : string \| undefined
- Retrieves the value that the custom attribute is set to.

  #### Parameters

  -

    ##### attr: string

    Name of the custom attribute.

  #### Returns string \| undefined

### getAttributes

- getAttributes ( ) : {}
- Returns a map of all custom attributes of a [`trace`](https://firebase.google.com/docs/reference/js/v8/firebase.performance.Trace)
  instance.

  #### Returns {}

  -

    ##### \[key: string\]: string

### getMetric

- getMetric ( metricName : string ) : number
- Returns the value of the custom metric by that name. If a custom metric with that name does
  not exist returns zero.

  #### Parameters

  -

    ##### metricName: string

    Name of the custom metric.

  #### Returns number

### incrementMetric

- incrementMetric ( metricName : string , num ? : number ) : void
- Adds to the value of a custom metric. If a custom metric with the provided name does not
  exist, it creates one with that name and the value equal to the given number.

  #### Parameters

  -

    ##### metricName: string

    The name of the custom metric.
  -

    ##### Optional num: number

    The number to be added to the value of the custom metric. If not provided, it
    uses a default value of one.

  #### Returns void

### putAttribute

- putAttribute ( attr : string , value : string ) : void
- Set a custom attribute of a [`trace`](https://firebase.google.com/docs/reference/js/v8/firebase.performance.Trace) to a certain value.

  #### Parameters

  -

    ##### attr: string

    Name of the custom attribute.
  -

    ##### value: string

    Value of the custom attribute.

  #### Returns void

### putMetric

- putMetric ( metricName : string , num : number ) : void
- Sets the value of the specified custom metric to the given number regardless of whether
  a metric with that name already exists on the [`trace`](https://firebase.google.com/docs/reference/js/v8/firebase.performance.Trace)
  instance or not.

  #### Parameters

  -

    ##### metricName: string

    Name of the custom metric.
  -

    ##### num: number

    Value to of the custom metric.

  #### Returns void

### record

- record ( startTime : number , duration : number , options ? : { attributes ?: {} ; metrics ?: {} } ) : void
- Records a [`trace`](https://firebase.google.com/docs/reference/js/v8/firebase.performance.Trace) from given parameters. This provides a
  direct way to use [`trace`](https://firebase.google.com/docs/reference/js/v8/firebase.performance.Trace) without a need to start/stop.
  This is useful for use cases in which the [`trace`](https://firebase.google.com/docs/reference/js/v8/firebase.performance.Trace) cannot
  directly be used (e.g. if the duration was captured before the Performance SDK was loaded).

  #### Parameters

  -

    ##### startTime: number

    Trace start time since epoch in millisec.
  -

    ##### duration: number

    The duraction of the trace in millisec.
  -

    ##### Optional options: { attributes?: {}; metrics?: {} }

    An object which can optionally hold maps of custom metrics and
    custom attributes.
    -

      ##### Optional attributes?: {}

      -

        ##### \[key: string\]: string

    -

      ##### Optional metrics?: {}

      -

        ##### \[key: string\]: number

  #### Returns void

### removeAttribute

- removeAttribute ( attr : string ) : void
- Removes the specified custom attribute from a [`trace`](https://firebase.google.com/docs/reference/js/v8/firebase.performance.Trace)
  instance.

  #### Parameters

  -

    ##### attr: string

    Name of the custom attribute.

  #### Returns void

### start

- start ( ) : void
- Starts the timing for the [`trace`](https://firebase.google.com/docs/reference/js/v8/firebase.performance.Trace) instance.

  #### Returns void

### stop

- stop ( ) : void
- Stops the timing of the [`trace`](https://firebase.google.com/docs/reference/js/v8/firebase.performance.Trace) instance and logs the
  data of the instance.

  #### Returns void