Search
      
    
  

  
    
    
  

  

    
      
Instruments
      
      **
        v2.11.0
      **
    
    

      
- Pages

        
- Modules

    

  

  
  

  
  
    

# 

  Instruments.Sysmon.Supervisor 
  (Instruments v2.11.0)

  

The system monitor is broken into three concepts: the Reporter, the Emitter,
and the Receiver.

The Reporter subscribes to `:erlang.system_monitor` and will forward system
monitor events it receives to subscribers.

The Emitter is responsible for receiving events from the Reporter and invoking
the appropriate handler on the Receiver.

Since only one process can subscribe to system monitor events, this is opt-in
and must be enabled by setting `:enable_sysmon` to `true` in the
`:instruments` application environment.
  

    
# 
      
        **
        Link to this section
      
      Summary
    

  
    
## 
      Functions
    

      
        
          child_spec(init_arg)

        

          

Returns a specification to start this module under a supervisor.

      

      
        
          init(list)

        

          

Callback implementation for `Supervisor.init/1`.

      

      
        
          start_link(_)

        

      

  

  

    
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
    
    
# init(list)

  

  

Callback implementation for `Supervisor.init/1`.
  

  
    
      **
      Link to this function
    
    
# start_link(_)