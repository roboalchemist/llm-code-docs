Search
      
    
  

  
    
    
  

  

    
      
Instruments
      
      **
        v2.11.0
      **
    
    

      
- Pages

        
- Modules

    

  

  
  

  
  
    

# 

  Instruments.Sysmon.Emitter 
  (Instruments v2.11.0)

  

The Emitter is a simple module that subscribes to the Reporter and will invoke
the corresponding handler on the Receiver.
  

    
# 
      
        **
        Link to this section
      
      Summary
    

  
    
## 
      Functions
    

      
        
          child_spec(init_arg)

        

          

Returns a specification to start this module under a supervisor.

      

      
        
          set_receiver(receiver_module)

        

          

Sets the receiver module to handle system monitor events. Receiver modules must implement the `Instruments.Sysmon.Receiver` behaviour.

      

      
        
          start_link(opts \\ [])

        

      

  

  

    
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
    
    
# set_receiver(receiver_module)

  

  

      

          

```
@spec set_receiver(term()) :: :ok
```

      

Sets the receiver module to handle system monitor events. Receiver modules must implement the `Instruments.Sysmon.Receiver` behaviour.
  

    

  
    
      **
      Link to this function
    
    
# start_link(opts \\ [])