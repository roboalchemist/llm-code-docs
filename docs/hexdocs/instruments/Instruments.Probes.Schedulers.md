Search
      
    
  

  
    
    
  

  

    
      
Instruments
      
      **
        v2.11.0
      **
    
    

      
- Pages

        
- Modules

    

  

  
  

  
  
    

# 

  Instruments.Probes.Schedulers 
  (Instruments v2.11.0)

  

A probe that reports erlang's internal CPU usage

Any good system monitoring needs to understand how hard the CPU is working. In
an Erlang ecosystem, this can be somewhat challenging becase when an Erlang
system isn't busy, the BEAM vm keeps its schedulers in tight loops so they don't get
descheduled by the operating system. This can make external CPU metrics like `top`
report that the system is actually much busier than it is.

This module reports Erlang's internal view of its scheduler utilization and is
a better gauge of how loaded your system is. It reports two values, the total
utilization, and a weighted
utilization,
which can be used as a proxy for CPU usage. Weighted utilization is calculated
based on the number of logical CPUs available, but in containerized
environments, the number of CPUs available may differ from what erlang
reports. In these cases, you can override the count by configuring
`num_logical_processors_override` on the `instruments` application.

To use this probe, add the following function somewhwere in your application's
initialization:

```
alias Instruments
Probe.define!("erlang.scheduler_utilization", :gauge, module: Probes.Schedulers, keys: ~w(weighted total))
```

The probe will now report two metrics, `erlang.scheduler_utilization.total` and `erlang.scheduler_utilization.total`.