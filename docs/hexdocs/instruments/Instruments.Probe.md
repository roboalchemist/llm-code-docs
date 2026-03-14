Search
      
    
  

  
    
    
  

  

    
      
Instruments
      
      **
        v2.11.0
      **
    
    

      
- Pages

        
- Modules

    

  

  
  

  
  
    

# 

  Instruments.Probe behaviour
  (Instruments v2.11.0)

  

A behavior for a Probe.

Modules that define probes are expected to implement all of the functions in
this behaviour.

A probe is created via the call to `Instruments.Probe.probe_init/3`, and is
then called every `sample_interval` milliseconds via the
`Instruments.Probe.probe_sample/1` function. The probe can then update its
internal state and do any processing it requires.

Every `report_interval` milliseconds, the probe is expected to emit its metric
value.
  

    
# 
      
        **
        Link to this section
      
      Summary
    

  
    
## 
      Types
    

      
        
          datapoint()

        

      

      
        
          probe_options()

        

      

      
        
          probe_type()

        

      

      
        
          probe_value()

        

      

      
        
          state()

        

      

  

  
    
## 
      Callbacks
    

      
        
          probe_get_value(state)

        

          

Called at least every `report_interval` milliseconds. This call reads the
value of the probe, which is reported to the underlying statistics system.

      

      
        
          probe_handle_message(any, state)

        

          

Called when the probe's runner process receives an unknown message.

      

      
        
          probe_init(t, probe_type, probe_options)

        

          

Called when the probe is created. The callback is passed
the name of the probe, what kind of metric it's producing and the options
the probe was created with.

      

      
        
          probe_reset(state)

        

          

Resets the probe's state.

      

      
        
          probe_sample(state)

        

          

Called every `sample_interval` milliseconds. When called, the probe should
perform its measurement and update its internal state.

      

  

  
    
## 
      Functions
    

      
        
          define!(name, type, options)

        

          

See `Instruments.Probe.Definitions.define!/3`.

      

      
        
          define(name, type, options)

        

          

See `Instruments.Probe.Definitions.define/3`.

      

  

  

    
# 
      
        **
        Link to this section
      
Types
    

    

  
    
      **
      Link to this type
    
    
# datapoint()

  

  

      

          

```
@type datapoint() :: String.t()
```

      

  

  
    
      **
      Link to this type
    
    
# probe_options()

  

  

      

          

```
@type probe_options() :: [
  sample_rate: pos_integer(),
  tags: [String.t(), ...],
  report_interval: pos_integer(),
  sample_interval: pos_integer(),
  function: (-> {:ok, state()}),
  mfa: {module(), atom(), [term()]},
  module: module(),
  keys: [atom()]
]
```

      

  

  
    
      **
      Link to this type
    
    
# probe_type()

  

  

      

          

```
@type probe_type() :: :counter | :spiral | :gauge | :histogram | :timing | :set
```

      

  

  
    
      **
      Link to this type
    
    
# probe_value()

  

  

      

          

```
@type probe_value() :: number() | keyword()
```

      

  

  
    
      **
      Link to this type
    
    
# state()

  

  

      

          

```
@type state() :: any()
```

      

  

    
# 
      
        **
        Link to this section
      
Callbacks
    

    

  
    
      **
      Link to this callback
    
    
# probe_get_value(state)

  

  

      

          

```
@callback probe_get_value(state()) :: {:ok, probe_value()}
```

      

Called at least every `report_interval` milliseconds. This call reads the
value of the probe, which is reported to the underlying statistics system.

Return values can either take the form of a single numeric value, or a
keyword list keys -> numeric values. Nil values won't be reported to the
statistics system.
  

  
    
      **
      Link to this callback
    
    
# probe_handle_message(any, state)

  

  

      

          

```
@callback probe_handle_message(any(), state()) :: {:ok, state()}
```

      

Called when the probe's runner process receives an unknown message.

You must return `{:ok, state}`. Any other return values will cancel further
execution of the probe.
  

  
    
      **
      Link to this callback
    
    
# probe_init(t, probe_type, probe_options)

  

  

      

          

```
@callback probe_init(String.t(), probe_type(), probe_options()) :: {:ok, state()}
```

      

Called when the probe is created. The callback is passed
the name of the probe, what kind of metric it's producing and the options
the probe was created with.

You must return `{:ok, state}`. The state will be passed back to you on
subsequent callbacks. Any other return values will cancel further
execution of the probe.
  

  
    
      **
      Link to this callback
    
    
# probe_reset(state)

  

  

      

          

```
@callback probe_reset(state()) :: {:ok, state()}
```

      

Resets the probe's state.

You must return `{:ok, state}`. Any other return values will cancel further
execution of the probe.
  

  
    
      **
      Link to this callback
    
    
# probe_sample(state)

  

  

      

          

```
@callback probe_sample(state()) :: {:ok, state()}
```

      

Called every `sample_interval` milliseconds. When called, the probe should
perform its measurement and update its internal state.

You must return `{:ok, state}`. Any other return values will cancel further
execution of the probe.
  

    
# 
      
        **
        Link to this section
      
Functions
    

    

  
    
      **
      Link to this function
    
    
# define!(name, type, options)

  

  

See `Instruments.Probe.Definitions.define!/3`.
  

  
    
      **
      Link to this function
    
    
# define(name, type, options)

  

  

See `Instruments.Probe.Definitions.define/3`.