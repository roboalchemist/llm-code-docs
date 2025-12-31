# Source: https://firebase.google.com/docs/reference/js/performance.performancetrace.md.txt

# PerformanceTrace interface

The interface representing a `Trace`.

**Signature:**  

    export interface PerformanceTrace 

## Methods

|                                                                      Method                                                                       |                                                                                                                           Description                                                                                                                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [getAttribute(attr)](https://firebase.google.com/docs/reference/js/performance.performancetrace.md#performancetracegetattribute)                  | Retrieves the value which a custom attribute is set to.                                                                                                                                                                                                         |
| [getAttributes()](https://firebase.google.com/docs/reference/js/performance.performancetrace.md#performancetracegetattributes)                    | Returns a map of all custom attributes of a trace instance.                                                                                                                                                                                                     |
| [getMetric(metricName)](https://firebase.google.com/docs/reference/js/performance.performancetrace.md#performancetracegetmetric)                  | Returns the value of the custom metric by that name. If a custom metric with that name does not exist will return zero.                                                                                                                                         |
| [incrementMetric(metricName, num)](https://firebase.google.com/docs/reference/js/performance.performancetrace.md#performancetraceincrementmetric) | Adds to the value of a custom metric. If a custom metric with the provided name does not exist, it creates one with that name and the value equal to the given number. The value will be floored down to an integer.                                            |
| [putAttribute(attr, value)](https://firebase.google.com/docs/reference/js/performance.performancetrace.md#performancetraceputattribute)           | Set a custom attribute of a trace to a certain value.                                                                                                                                                                                                           |
| [putMetric(metricName, num)](https://firebase.google.com/docs/reference/js/performance.performancetrace.md#performancetraceputmetric)             | Sets the value of the specified custom metric to the given number regardless of whether a metric with that name already exists on the trace instance or not. The value will be floored down to an integer.                                                      |
| [record(startTime, duration, options)](https://firebase.google.com/docs/reference/js/performance.performancetrace.md#performancetracerecord)      | Records a trace from given parameters. This provides a direct way to use trace without a need to start/stop. This is useful for use cases in which the trace cannot directly be used (e.g. if the duration was captured before the Performance SDK was loaded). |
| [removeAttribute(attr)](https://firebase.google.com/docs/reference/js/performance.performancetrace.md#performancetraceremoveattribute)            | Removes the specified custom attribute from a trace instance.                                                                                                                                                                                                   |
| [start()](https://firebase.google.com/docs/reference/js/performance.performancetrace.md#performancetracestart)                                    | Starts the timing for the trace instance.                                                                                                                                                                                                                       |
| [stop()](https://firebase.google.com/docs/reference/js/performance.performancetrace.md#performancetracestop)                                      | Stops the timing of the trace instance and logs the data of the instance.                                                                                                                                                                                       |

## PerformanceTrace.getAttribute()

Retrieves the value which a custom attribute is set to.

**Signature:**  

    getAttribute(attr: string): string | undefined;

#### Parameters

| Parameter |  Type  |          Description          |
|-----------|--------|-------------------------------|
| attr      | string | Name of the custom attribute. |

**Returns:**

string \| undefined

## PerformanceTrace.getAttributes()

Returns a map of all custom attributes of a trace instance.

**Signature:**  

    getAttributes(): {
            [key: string]: string;
        };

**Returns:**

{ \[key: string\]: string; }

## PerformanceTrace.getMetric()

Returns the value of the custom metric by that name. If a custom metric with that name does not exist will return zero.

**Signature:**  

    getMetric(metricName: string): number;

#### Parameters

| Parameter  |  Type  |        Description         |
|------------|--------|----------------------------|
| metricName | string | Name of the custom metric. |

**Returns:**

number

## PerformanceTrace.incrementMetric()

Adds to the value of a custom metric. If a custom metric with the provided name does not exist, it creates one with that name and the value equal to the given number. The value will be floored down to an integer.

**Signature:**  

    incrementMetric(metricName: string, num?: number): void;

#### Parameters

| Parameter  |  Type  |                                                Description                                                 |
|------------|--------|------------------------------------------------------------------------------------------------------------|
| metricName | string | The name of the custom metric.                                                                             |
| num        | number | The number to be added to the value of the custom metric. If not provided, it uses a default value of one. |

**Returns:**

void

## PerformanceTrace.putAttribute()

Set a custom attribute of a trace to a certain value.

**Signature:**  

    putAttribute(attr: string, value: string): void;

#### Parameters

| Parameter |  Type  |          Description           |
|-----------|--------|--------------------------------|
| attr      | string | Name of the custom attribute.  |
| value     | string | Value of the custom attribute. |

**Returns:**

void

## PerformanceTrace.putMetric()

Sets the value of the specified custom metric to the given number regardless of whether a metric with that name already exists on the trace instance or not. The value will be floored down to an integer.

**Signature:**  

    putMetric(metricName: string, num: number): void;

#### Parameters

| Parameter  |  Type  |          Description           |
|------------|--------|--------------------------------|
| metricName | string | Name of the custom metric.     |
| num        | number | Value to of the custom metric. |

**Returns:**

void

## PerformanceTrace.record()

Records a trace from given parameters. This provides a direct way to use trace without a need to start/stop. This is useful for use cases in which the trace cannot directly be used (e.g. if the duration was captured before the Performance SDK was loaded).

**Signature:**  

    record(startTime: number, duration: number, options?: {
            metrics?: {
                [key: string]: number;
            };
            attributes?: {
                [key: string]: string;
            };
        }): void;

#### Parameters

| Parameter |                                          Type                                          |                                    Description                                    |
|-----------|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| startTime | number                                                                                 | trace start time since epoch in millisec.                                         |
| duration  | number                                                                                 | The duration of the trace in millisec.                                            |
| options   | { metrics?: { \[key: string\]: number; }; attributes?: { \[key: string\]: string; }; } | An object which can optionally hold maps of custom metrics and custom attributes. |

**Returns:**

void

## PerformanceTrace.removeAttribute()

Removes the specified custom attribute from a trace instance.

**Signature:**  

    removeAttribute(attr: string): void;

#### Parameters

| Parameter |  Type  |          Description          |
|-----------|--------|-------------------------------|
| attr      | string | Name of the custom attribute. |

**Returns:**

void

## PerformanceTrace.start()

Starts the timing for the trace instance.

**Signature:**  

    start(): void;

**Returns:**

void

## PerformanceTrace.stop()

Stops the timing of the trace instance and logs the data of the instance.

**Signature:**  

    stop(): void;

**Returns:**

void