zipkin
# Module sample 
Source 
## Structs§
AlwaysSamplerA `Sample`r which always returns `true`.NeverSamplerA `Sample`r which always returns `false`.RandomSamplerA `Sample`r which randomly samples at a specific rate.
## Traits§
SampleA sampler decides whether or not a span should be recorded based on its
trace ID.