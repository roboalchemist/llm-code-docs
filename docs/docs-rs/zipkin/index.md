# Crate zipkin 
Source 
## Modules§
annotationAnnotations.endpointEndpoints.reportSpan reporters.sampleSpan samplers.sampling_flagsSampling flags.spanSpans.span_idSpan IDs.trace_contextTrace contexts.trace_idTrace IDs.
## Structs§
AnnotationAssociates an event that explains latency with a timestamp.AttachedA type indicating that an `OpenSpan` is “attached” to the current thread.BindA type which wraps a future, associating it with an `OpenSpan`.CurrentGuardA guard object for the thread-local current trace context.DetachedA type indicating that an `OpenSpan` is “detached” from the current thread.EndpointThe network context of a node in the service graph.OpenSpanAn open span.SamplingFlagsFlags used to control sampling.SetTracerErrorThe error returned when attempting to set a tracer when one is already installed.SpanA `Span` represents a single operation over some range of time.SpanIdThe ID of a span.TraceContextA `TraceContext` represents a distributed trace request.TraceIdThe ID of a trace.
## Enums§
KindThe “kind” of a span.
## Traits§
ReportA reporter consumes Zipkin spans and reports them.SampleA sampler decides whether or not a span should be recorded based on its
trace ID.
## Functions§
currentReturns this thread’s current trace context.join_traceJoins an existing trace.new_childStats a new span with the specified parent.new_traceStarts a new trace.new_trace_fromStats a new trace with specific sampling flags.next_spanCreates a new span parented to the current one if it exists, or starting a new trace otherwise.set_currentSets this thread’s current trace context.set_tracerInitializes the global tracer.
## Attribute Macros§
spannedWraps the execution of a function or method in a span.