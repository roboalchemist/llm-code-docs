Search
      
    
  

  
    
    
  

  

    
      
Instruments
      
      **
        v2.11.0
      **
    
    

      
- Pages

        
- Modules

    

  

  
  

  
  
    

# 

  Instruments.Sysmon.Receiver behaviour
  (Instruments v2.11.0)

  

The Receiver behavior defines callbacks that are invoked by the Emitter in
response to system monitor events.
  

    
# 
      
        **
        Link to this section
      
      Summary
    

  
    
## 
      Types
    

      
        
          info()

        

      

  

  
    
## 
      Callbacks
    

      
        
          handle_busy_dist_port(pid, port)

        

      

      
        
          handle_busy_port(pid, port)

        

      

      
        
          handle_large_heap(pid, info)

        

      

      
        
          handle_long_gc(pid, info)

        

      

      
        
          handle_long_message_queue(pid, boolean)

        

      

      
        
          handle_long_schedule(pid, info)

        

      

  

  

    
# 
      
        **
        Link to this section
      
Types
    

    

  
    
      **
      Link to this type
    
    
# info()

  

  

      

          

```
@type info() :: List.t({term(), term()})
```

      

  

    
# 
      
        **
        Link to this section
      
Callbacks
    

    

  
    
      **
      Link to this callback
    
    
# handle_busy_dist_port(pid, port)

  

  

      

          

```
@callback handle_busy_dist_port(pid(), port()) :: :ok
```

      

  

  
    
      **
      Link to this callback
    
    
# handle_busy_port(pid, port)

  

  

      

          

```
@callback handle_busy_port(pid(), port()) :: :ok
```

      

  

  
    
      **
      Link to this callback
    
    
# handle_large_heap(pid, info)

  

  

      

          

```
@callback handle_large_heap(pid(), info()) :: :ok
```

      

  

  
    
      **
      Link to this callback
    
    
# handle_long_gc(pid, info)

  

  

      

          

```
@callback handle_long_gc(pid(), info()) :: :ok
```

      

  

  
    
      **
      Link to this callback
    
    
# handle_long_message_queue(pid, boolean)

  

  

      

          

```
@callback handle_long_message_queue(pid(), boolean()) :: :ok
```

      

  

  
    
      **
      Link to this callback
    
    
# handle_long_schedule(pid, info)

  

  

      

          

```
@callback handle_long_schedule(pid(), info()) :: :ok
```