Search
      
    
  

  
    
    
  

  

    
      
Instruments
      
      **
        v2.11.0
      **
    
    

      
- Pages

        
- Modules

    

  

  
  

  
  
    

# 

  Instruments.Sysmon.Reporter 
  (Instruments v2.11.0)

  

Since only one process can subscribe to system monitor events, the Reporter
acts as a relay for system monitor events, allowing multiple subscribers to
receive system monitor events.

On startup, the Reporter will subscribe to the system monitor events
configured in `:sysmon_events` in the `:instruments` application environment.
If no events are configured, the Reporter will not subscribe to any events.
  

    
# 
      
        **
        Link to this section
      
      Summary
    

  
    
## 
      Types
    

      
        
          sysmon_event()

        

      

      
        
          t()

        

      

  

  
    
## 
      Functions
    

      
        
          child_spec(init_arg)

        

          

Returns a specification to start this module under a supervisor.

      

      
        
          get_events()

        

          

Returns the system monitor events the Reporter is subscribed to.

      

      
        
          set_events(events)

        

          

Sets the system monitor events to subscribe to. If no events are provided, the Reporter will not register itself as the system monitor process.

      

      
        
          start_link(opts \\ [])

        

      

      
        
          subscribe(pid \\ self())

        

          

Subscribes the provided pid to configured system monitor events.

      

      
        
          unsubscribe(pid \\ self())

        

          

Unsubscribes the provided pid from system monitor events.

      

  

  

    
# 
      
        **
        Link to this section
      
Types
    

    

  
    
      **
      Link to this type
    
    
# sysmon_event()

  

  

      

          

```
@type sysmon_event() ::
  {:long_gc, pos_integer()}
  | {:long_schedule, pos_integer()}
  | {:large_heap, pos_integer()}
  | :busy_port
  | :busy_dist_port
```

      

  

  
    
      **
      Link to this type
    
    
# t()

  

  

      

          

```
@type t() :: %Instruments.Sysmon.Reporter{
  events: [sysmon_event()],
  subscribers: %{required(reference()) => pid()}
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
    
    
# get_events()

  

  

      

          

```
@spec get_events() :: [sysmon_event()]
```

      

Returns the system monitor events the Reporter is subscribed to.
  

  
    
      **
      Link to this function
    
    
# set_events(events)

  

  

      

          

```
@spec set_events([sysmon_event()]) :: :ok
```

      

Sets the system monitor events to subscribe to. If no events are provided, the Reporter will not register itself as the system monitor process.
  

    

  
    
      **
      Link to this function
    
    
# start_link(opts \\ [])

  

  

  

    

  
    
      **
      Link to this function
    
    
# subscribe(pid \\ self())

  

  

      

          

```
@spec subscribe(pid()) :: :ok
```

      

Subscribes the provided pid to configured system monitor events.
  

    

  
    
      **
      Link to this function
    
    
# unsubscribe(pid \\ self())

  

  

      

          

```
@spec unsubscribe(pid()) :: :ok
```

      

Unsubscribes the provided pid from system monitor events.