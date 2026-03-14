### Index ¶

- Variables

### Constants ¶

  

This section is empty.

  
### Variables ¶

  
    
      View Source
      

```
var (
	ColdStarts = prometheus.NewCounterVec(
		prometheus.CounterOpts{
			Name: "fission_function_cold_starts_total",
			Help: "How many cold starts are made by function_name, function_namespace.",
		},
		functionLabels,
	)
	FuncRunningSummary = prometheus.NewSummaryVec(
		prometheus.SummaryOpts{
			Name:       "fission_function_running_seconds",
			Help:       "The running time (last access - create) in seconds of the function.",
			Objectives: map[float64]float64{0.5: 0.05, 0.9: 0.01, 0.99: 0.001},
		},
		functionLabels,
	)
	ColdStartsError = prometheus.NewCounterVec(
		prometheus.CounterOpts{
			Name: "fission_function_cold_start_errors_total",
			Help: "Count of fission cold start errors",
		},
		functionLabels,
	)
)
```

    
  

  
### Functions ¶

  

This section is empty.

  
### Types ¶

  

This section is empty.