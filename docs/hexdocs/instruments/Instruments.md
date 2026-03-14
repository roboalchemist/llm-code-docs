Search
      
    
  

  
    
    
  

  

    
      
Instruments
      
      **
        v2.11.0
      **
    
    

      
- Pages

        
- Modules

    

  

  
  

  
  
    

# 

  Instruments 
  (Instruments v2.11.0)

  

Instruments allows you to easily create and emit metrics from your application.

Getting started with instruments is simple, all you do is `use` this module, and
you're off to the races.

```
defmodule MyModule do
  use Instruments

  def compute_something() do
    Instruments.increment("computations")
  end
end
```

You can also create functions that are custom prefixed to avoide duplication in your code.
See `Instruments.CustomFunctions` for more details.
## 
  **
  

metric-options
  
  Metric Options

All the functions in this module can be given an options keyword list, with one
or both of the following keys:

- `sample_rate`: A float, determining the percentage chance this metric will be emitted.
- `tags`: A list of String tags that will be applied to this metric. Tags are useful for post-hoc grouping.

```
    For example, you could add instance type as a tag and visualize the difference between timing
    metrics of the same statistic across instance types to see which are the fastest.
```

Here's an example of using options:

```
@type user_type :: :administrator | :employee | :normal
@spec my_function(user_type, [User]) :: :ok
def my_function(user_type, users) do
  Instruments.histogram("user_counts", Enum.count(users), sample_rate: 0.5, tags: ["#{user_type}"])
end
```

Now you can aggregate user counts by user type without emitting new stats
## 
  **
  

performance-notes
  
  Performance notes

If a metric key has interpolation (such as `"my_metric.#{Mix.env}"`), the interpolation is removed and the metric name is converted to
IOdata. This will prevent garbage being created in your process.
  

    
# 
      
        **
        Link to this section
      
      Summary
    

  
    
## 
      Functions
    

      
        
          decrement(key, value \\ 1, options \\ [])

        

          

Decrements a counter

      

      
        
          gauge(key, value, options \\ [])

        

          

Sets a gauge value

      

      
        
          histogram(key, value, options \\ [])

        

          

Adds a value to a histogram

      

      
        
          increment(key, value \\ 1, options \\ [])

        

          

Increments a counter

      

      
        
          measure(key, options \\ [], function)

        

          

Times the function `function` and returns its result

      

      
        
          register_vm_metrics(report_interval \\ 10000)

        

          

Registers the following probes

      

      
        
          send_event(title_ast, text, opts \\ [])

        

          

Sends an event to DataDog

      

      
        
          set(key, value, options \\ [])

        

          

Adds `value` to a set

      

      
        
          timing(key, value, options \\ [])

        

          

Reports a timed value

      

  

  

    
# 
      
        **
        Link to this section
      
Functions
    

    

    

    

  
    
      **
      Link to this macro
    
    
# decrement(key, value \\ 1, options \\ [])

      (macro)

  

  

Decrements a counter

Decrements the counter with the key `key` by `value`.
  

    

  
    
      **
      Link to this macro
    
    
# gauge(key, value, options \\ [])

      (macro)

  

  

Sets a gauge value

Sets the Gauge with key `key` to `value`, overwriting the previous value. Gauges are useful
for system metrics that have a specific value at a specific time.
  

    

  
    
      **
      Link to this macro
    
    
# histogram(key, value, options \\ [])

      (macro)

  

  

Adds a value to a histogram

Reports `value` to a histogram with key `key`. A Histogram is useful if you want to see
aggregated percentages, and are often used when recording timings.
  

    

    

  
    
      **
      Link to this macro
    
    
# increment(key, value \\ 1, options \\ [])

      (macro)

  

  

Increments a counter

Increments the counter with name `key` by `value`.
  

    

  
    
      **
      Link to this macro
    
    
# measure(key, options \\ [], function)

      (macro)

  

  

Times the function `function` and returns its result

This function allows you to time a function and send a metric in one call, and can often be
easier to use than the `Instruments.timing/3` function.

For example this:

```
def timed_internals() do
  {run_time_micros, result} = :timer.tc(&other_fn/0)
  Instruments.timing("my.metric", run_time_micros)
  result
end
```

Can be converted to:

```
def timed_internals() do
  Instruments.measure("my.metric", &other_fn/0)
end
```

  

    

  
    
      **
      Link to this function
    
    
# register_vm_metrics(report_interval \\ 10000)

  

  

      

          

```
@spec register_vm_metrics(pos_integer()) :: :ok
```

      

Registers the following probes:

- `erlang.memory`: Reports how much memory is being used by the `process`, `system`, `atom`, `binary` and `ets` carriers.
- `erlang.supercarrier`: Reports the total size of the super carrier, and how much of it is used.
- `recon.alloc`: Reports how much memory is being actively used by the VM.
- `erlang.system.process_count`: A gauge reporting the number of processes in the VM.
- `erlang.system.port_count`: A gauge reporting the number of ports in the VM.
- `erlang.statistics.run_queue`: A gauge reporting the VM's run queue. This number should be 0 or very low. A high run queue indicates your system is overloaded.
- `erlang.scheduler_utilization`: A gauge that reports the actual utilization of every scheduler in the system. See `Instruments.Probes.Schedulers` for more information

  If some memory allocators are disabled, then the erlang.memory and recon.alloc probes will not be registered as these statistics are unavailable.
  

    

  
    
      **
      Link to this macro
    
    
# send_event(title_ast, text, opts \\ [])

      (macro)

  

  

Sends an event to DataDog

This macro is useful if you want to record one-off events like deploys or metrics values changing.
  

    

  
    
      **
      Link to this macro
    
    
# set(key, value, options \\ [])

      (macro)

  

  

Adds `value` to a set

Statsd supports the notion of sets,
which are unique values in a given flush. This adds `value`
to a set with key `key`.
  

    

  
    
      **
      Link to this macro
    
    
# timing(key, value, options \\ [])

      (macro)

  

  

Reports a timed value

If you're manually timing something, you can use this function to report its value. Timings
are usually added to a histogram and reported as percentages. If you're interested in timing
a function, you should also see `Instruments.measure/3`.