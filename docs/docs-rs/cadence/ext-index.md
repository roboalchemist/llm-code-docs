cadence
# Module ext 
Source 
## Structs§
MultiLineWriterBuffered implementation of the `Write` trait that appends a
trailing line ending string to every input written and only
writes the complete input in a single call to the underlying
writer.SocketStatsThread-safe collection of stats updated by network sinks.
## Enums§
MetricValueHolder for primitive metric values that knows how to display itself
## Traits§
MetricBackendTypically internal client methods for sending metrics and handling errors.ToCounterValueConversion trait for valid values for countersToDistributionValueConversion trait for valid values for distributionsToGaugeValueConversion trait for valid values for gaugesToHistogramValueConversion trait for valid values for histogramsToMeterValueConversion trait for valid values for metersToSetValueConversion trait for valid values for setsToTimerValueConversion trait for valid values for timers