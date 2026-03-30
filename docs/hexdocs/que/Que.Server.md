Search
      
    
  

  
    
    
  

  

    
      
Que
      
      **
        v0.10.1
      **
    
    

      
- Pages

        
- Modules

        
- Mix Tasks

    

  

  
  

  
    

# 

    
      **
      View Source
    

  Que.Server 
  (Que v0.10.1)

  

`Que.Server` is the `GenServer` responsible for processing all Jobs.

This `GenServer` oversees the Workers performing their Jobs and handles
their success and failure callbacks. You shouldn't call any of this
module's methods directly. Instead use the methods exported by the
base `Que` module.
  

    
# 
      
        **
        Link to this section
      
      Summary
    

  
    
## 
      Functions
    

      
        
          child_spec(init_arg)

        

          

Returns a specification to start this module under a supervisor.

      

      
        
          start_link(worker)

        

          

Starts the Job Server

      

      
        
          stop(worker)

        

          

Stops the Job Server

      

  

  

    
# 
      
        **
        Link to this section
      
Functions
    

    

  
    
      **
      Link to this function
    
    
# child_spec(init_arg)

      
       **
       View Source
     

  

  

Returns a specification to start this module under a supervisor.

See `Supervisor`.
  

  
    
      **
      Link to this function
    
    
# start_link(worker)

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
start_link(worker :: Que.Worker.t()) :: GenServer.on_start()
```

      

Starts the Job Server
  

  
    
      **
      Link to this function
    
    
# stop(worker)

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
stop(worker :: Que.Worker.t()) :: :ok
```

      

Stops the Job Server