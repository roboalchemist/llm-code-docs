# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseperformance/api/reference/Classes/Trace.md.txt

# FirebasePerformance Framework Reference

# Trace

    class Trace : NSObject, https://firebase.google.com/docs/reference/swift/firebaseperformance/api/reference/Protocols/PerformanceAttributable.html

FIRTrace objects contain information about a "Trace", which is a sequence of steps. Traces can be
used to measure the time taken for a sequence of steps.
Traces also include "Counters". Counters are used to track information which is cumulative in
nature (e.g., Bytes downloaded). Counters are scoped to an FIRTrace object.
- `
  ``
  ``
  `

  ### [name](https://firebase.google.com/docs/reference/swift/firebaseperformance/api/reference/Classes/Trace#/c:objc(cs)FIRTrace(py)name)

  `
  `  
  @brief Name of the trace.  

  #### Declaration

  Swift  

      var name: String { get }

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebaseperformance/api/reference/Classes/Trace#/c:objc(cs)FIRTrace(im)init)

  `
  `  
  Unavailable  
  @brief Not a valid initializer.
- `
  ``
  ``
  `

  ### [start()](https://firebase.google.com/docs/reference/swift/firebaseperformance/api/reference/Classes/Trace#/c:objc(cs)FIRTrace(im)start)

  `
  `  
  Starts the trace.  

  #### Declaration

  Swift  

      func start()

- `
  ``
  ``
  `

  ### [stop()](https://firebase.google.com/docs/reference/swift/firebaseperformance/api/reference/Classes/Trace#/c:objc(cs)FIRTrace(im)stop)

  `
  `  
  Stops the trace if the trace is active.  

  #### Declaration

  Swift  

      func stop()

[## Metrics API](https://firebase.google.com/docs/reference/swift/firebaseperformance/api/reference/Classes/Trace#/Metrics-API)

- `
  ``
  ``
  `

  ### [incrementMetric(_:by:)](https://firebase.google.com/docs/reference/swift/firebaseperformance/api/reference/Classes/Trace#/c:objc(cs)FIRTrace(im)incrementMetric:byInt:)

  `
  `  
  Atomically increments the metric for the provided metric name with the provided value. If it is a
  new metric name, the metric value will be initialized to the value. Does nothing if the trace
  has not been started or has already been stopped.  

  #### Declaration

  Swift  

      func incrementMetric(_ metricName: String, by incrementValue: Int64)

  #### Parameters

  |------------------------|---------------------------------------|
  | ` `*metricName*` `     | The name of the metric to increment.  |
  | ` `*incrementValue*` ` | The value to increment the metric by. |

- `
  ``
  ``
  `

  ### [valueForMetric(_:)](https://firebase.google.com/docs/reference/swift/firebaseperformance/api/reference/Classes/Trace#/c:objc(cs)FIRTrace(im)valueForIntMetric:)

  `
  `  
  Gets the value of the metric for the provided metric name. If the metric doesn't exist, a 0 is
  returned.  

  #### Declaration

  Swift  

      func valueForMetric(_ metricName: String) -> Int64

  #### Parameters

  |--------------------|----------------------------------------|
  | ` `*metricName*` ` | The name of metric whose value to get. |

  #### Return Value

  The value of the given metric or 0 if it hasn't yet been set.
- `
  ``
  ``
  `

  ### [setValue(_:forMetric:)](https://firebase.google.com/docs/reference/swift/firebaseperformance/api/reference/Classes/Trace#/c:objc(cs)FIRTrace(im)setIntValue:forMetric:)

  `
  `  
  Sets the value of the metric for the provided metric name to the provided value. Does nothing if
  the trace has not been started or has already been stopped.  

  #### Declaration

  Swift  

      func setValue(_ value: Int64, forMetric metricName: String)

  #### Parameters

  |--------------------|---------------------------------|
  | ` `*metricName*` ` | The name of the metric to set.  |
  | ` `*value*` `      | The value to set the metric to. |