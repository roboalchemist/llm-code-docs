# Source: https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Classes/FIRTrace.md.txt

# FirebasePerformance Framework Reference

# FIRTrace


    @interface FIRTrace : NSObject <https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Protocols/FIRPerformanceAttributable.html>

FIRTrace objects contain information about a "Trace", which is a sequence of steps. Traces can be
used to measure the time taken for a sequence of steps.
Traces also include "Counters". Counters are used to track information which is cumulative in
nature (e.g., Bytes downloaded). Counters are scoped to an FIRTrace object.
- `
  ``
  ``
  `

  ### [name](https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Classes/FIRTrace#/c:objc(cs)FIRTrace(py)name)

  `
  `  
  @brief Name of the trace.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nonnull) NSString *name;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Classes/FIRTrace#/c:objc(cs)FIRTrace(im)init)

  `
  `  
  Unavailable  
  @brief Not a valid initializer.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;

- `
  ``
  ``
  `

  ### [-start](https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Classes/FIRTrace#/c:objc(cs)FIRTrace(im)start)

  `
  `  
  Starts the trace.  

  #### Declaration

  Objective-C  

      - (void)start;

- `
  ``
  ``
  `

  ### [-stop](https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Classes/FIRTrace#/c:objc(cs)FIRTrace(im)stop)

  `
  `  
  Stops the trace if the trace is active.  

  #### Declaration

  Objective-C  

      - (void)stop;

[## Metrics API](https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Classes/FIRTrace#/Metrics-API)

- `
  ``
  ``
  `

  ### [-incrementMetric:byInt:](https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Classes/FIRTrace#/c:objc(cs)FIRTrace(im)incrementMetric:byInt:)

  `
  `  
  Atomically increments the metric for the provided metric name with the provided value. If it is a
  new metric name, the metric value will be initialized to the value. Does nothing if the trace
  has not been started or has already been stopped.  

  #### Declaration

  Objective-C  

      - (void)incrementMetric:(nonnull NSString *)metricName
                        byInt:(int64_t)incrementValue;

  #### Parameters

  |------------------------|---------------------------------------|
  | ` `*metricName*` `     | The name of the metric to increment.  |
  | ` `*incrementValue*` ` | The value to increment the metric by. |

- `
  ``
  ``
  `

  ### [-valueForIntMetric:](https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Classes/FIRTrace#/c:objc(cs)FIRTrace(im)valueForIntMetric:)

  `
  `  
  Gets the value of the metric for the provided metric name. If the metric doesn't exist, a 0 is
  returned.  

  #### Declaration

  Objective-C  

      - (int64_t)valueForIntMetric:(nonnull NSString *)metricName;

  #### Parameters

  |--------------------|----------------------------------------|
  | ` `*metricName*` ` | The name of metric whose value to get. |

  #### Return Value

  The value of the given metric or 0 if it hasn't yet been set.
- `
  ``
  ``
  `

  ### [-setIntValue:forMetric:](https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Classes/FIRTrace#/c:objc(cs)FIRTrace(im)setIntValue:forMetric:)

  `
  `  
  Sets the value of the metric for the provided metric name to the provided value. Does nothing if
  the trace has not been started or has already been stopped.  

  #### Declaration

  Objective-C  

      - (void)setIntValue:(int64_t)value forMetric:(nonnull NSString *)metricName;

  #### Parameters

  |--------------------|---------------------------------|
  | ` `*metricName*` ` | The name of the metric to set.  |
  | ` `*value*` `      | The value to set the metric to. |