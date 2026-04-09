Search
      
    
  

  
    
    
  

  

    
      
Instruments
      
      **
        v2.11.0
      **
    
    

      
- Pages

        
- Modules

    

  

  
  

  
  
    

# 

  Instruments.RateTracker 
  (Instruments v2.11.0)

  

RateTracker will track how often you are reporting metrics that are not backed 
by a "fast" implementation.

RateTracker is designed to catch cases where you have inadvertently reported 
a metric "too" frequently, as some metrics require hitting statsd directly for 
every reported value. Doing so in hot loops can result in your 
application slowing significantly.
  

    
# 
      
        **
        Link to this section
      
      Summary
    

  
    
## 
      Types
    

      
        
          callback()

        

      

      
        
          t()

        

      

  

  
    
## 
      Functions
    

      
        
          child_spec(init_arg)

        

          

Returns a specification to start this module under a supervisor.

      

      
        
          dump_rates()

        

          

Dump the currently tracked rates

      

      
        
          init(atom)

        

          

Callback implementation for `GenServer.init/1`.

      

      
        
          start_link(_ \\ [])

        

      

      
        
          subscribe(callback)

        

          

Add a callback to be notified that you are reporting a metric "too" frequently.

      

  

  

    
# 
      
        **
        Link to this section
      
Types
    

    

  
    
      **
      Link to this type
    
    
# callback()

  

  

      

          

```
@type callback() :: ({String.t(), Statix.options()}, non_neg_integer() -> term())
```

      

  

  
    
      **
      Link to this type
    
    
# t()

  

  

      

          

```
@type t() :: %Instruments.RateTracker{
  callbacks: [callback()],
  last_update_time: integer(),
  table_count: non_neg_integer()
}
```

      

  

    
# 
      
        **
        Link to this section
      
Functions
    

    

  
    
      **
      Link to this function
    
    
# child_spec(init_arg)

  

  

Returns a specification to start this module under a supervisor.

See `Supervisor`.
  

  
    
      **
      Link to this function
    
    
# dump_rates()

  

  

      

          

```
@spec dump_rates() :: [{{String.t(), Keyword.t()}, non_neg_integer()}]
```

      

Dump the currently tracked rates
  

  
    
      **
      Link to this function
    
    
# init(atom)

  

  

Callback implementation for `GenServer.init/1`.
  

    

  
    
      **
      Link to this function
    
    
# start_link(_ \\ [])

  

  

  

  
    
      **
      Link to this function
    
    
# subscribe(callback)

  

  

      

          

```
@spec subscribe(callback()) :: :ok
```

      

Add a callback to be notified that you are reporting a metric "too" frequently.

In order to receive notifications, you must set `:instruments` -> 
`:rate_tracker_callback_threshold` to the per-second rate that you want to be 
notified at. This value will be different for every system, and will require
experimentation to determine. You can use `dump_rates()` in a remote console
to see what values are currently tracked for your metrics.

This callback should be short-lived.