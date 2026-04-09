Search
      
    
  

  
    
    
  

  

    
      
Instruments
      
      **
        v2.11.0
      **
    
    

      
- Pages

        
- Modules

    

  

  
  

  
  
    

# 

  API Reference Instruments v2.11.0

  
    
## 
  **
  

modules
  
  Modules

    

  
    Instruments

  

    

Instruments allows you to easily create and emit metrics from your application.

  
    Instruments.CustomFunctions

  

    

Creates custom prefixed functions

  
    Instruments.Probe

  

    

A behavior for a Probe.

  
    Instruments.Probe.Errors.ProbeNameTakenError

  

  
    Instruments.Probes.Schedulers

  

    

A probe that reports erlang's internal CPU usage

  
    Instruments.RateTracker

  

    

RateTracker will track how often you are reporting metrics that are not backed 
by a "fast" implementation.

  
    Instruments.Statix

  

    

The default stats reporter. Uses the `Statix` library.

  
    Instruments.StatsReporter

  

    

A behavoiur for reporters.

  
    Instruments.StatsReporter.Logger

  

    

A StatsReporter that logs to the `Logger` module.

  
    Instruments.StatsReporter.Null

  

    

A StatsReporter module that throws out all logging messages.

  
    Instruments.Sysmon.Emitter

  

    

The Emitter is a simple module that subscribes to the Reporter and will invoke
the corresponding handler on the Receiver.

  
    Instruments.Sysmon.Receiver

  

    

The Receiver behavior defines callbacks that are invoked by the Emitter in
response to system monitor events.

  
    Instruments.Sysmon.Receiver.Log

  

    

This module emits system monitor events

  
    Instruments.Sysmon.Receiver.Metrics

  

    

This module emits system monitor events

  
    Instruments.Sysmon.Reporter

  

    

Since only one process can subscribe to system monitor events, the Reporter
acts as a relay for system monitor events, allowing multiple subscribers to
receive system monitor events.

  
    Instruments.Sysmon.Supervisor

  

    

The system monitor is broken into three concepts: the Reporter, the Emitter,
and the Receiver.