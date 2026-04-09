Search
      
    
  

  
    
    
  

  

    
      
Instruments
      
      **
        v2.11.0
      **
    
    

      
- Pages

        
- Modules

    

  

  
  

  
  
    

# 

  Probes

A probe is a persistent system metric that's updated at a
consistent rate.

Probes can be either functions, or a module that implements the
`Instruments.Probe` behaviour. If it's a module, its state is controlled by
another process, all implementers need to worry about is the
state transitions.
## 
  **
  

defining-probes
  
  Defining probes

First of all, probes must have unique names so their stats won't conflict
with one another. This is enforced at runtime, since it's possible to
define probes progammatically.
### 
  **
  

functions
  
  Functions

The simplest way to define a probe is to specify a function:

```
Probe.define("erlang.process_count", :gauge,
  function: fn -> :erlang.system_info(:process_count) end,
  report_interval: 60_000)
```

Since the above definiton doesn't pass in the sample_interval options,
the sample interval is the same as the report interval. The metric will
be sampled and reported every 60 seconds.
### 
  **
  

mfa
  
  MFA

A simplification of the above example uses the `:mfa` option to specify
a module, function and arguments to be called.
For example,

```
Probe.define("erlang.process_count", :gauge, mfa: {:erlang, :system_info, [:process_count]})
```

You can also have a function that returns a keyword list of stats and
select which keys you want to report. The keys are added to the stat name

```
Probe.define("erlang.memory", :gauge,
  function: fn -> :erlang.memory() end,
  keys: [:total, :atom, :processes],
  report_interval: 60_000)
```

While the `:erlang.memory()` returns a keyword list with 9 entries,
the above call will only produce three metrics, `erlang.memory.total`,
`erlang.memory.atom` and `erlang.memory.processes`.
## 
  **
  

module-based-probes
  
  Module based Probes

If more control is desired, you can implement a probe module yourself.

```
defmodule MyProbe do
  @behaviour Instruments.Probe
  # callback implementations...
end

# and then define the probe:
Probe.define("system.my_probe", :counter, module: MyProbe)
```

Your module is now a registered probe, and will receive all of the `Probe`
callbacks.

  

      
        
          â Previous Page
        
        
Configuration
        
      

  
  

      
        
          Next Page â
        
        
Performance
        
      

  

      

          

            On Hex.pm:

            
              Package
              Preview

                (current file)

            

            
          

        

          Built using
          ExDoc (v0.28.4) for the

            Elixir programming language