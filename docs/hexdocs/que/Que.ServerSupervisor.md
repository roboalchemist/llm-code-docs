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
    

  Que.ServerSupervisor 
  (Que v0.10.1)

  

This Supervisor is responsible for spawning a `Que.Server`
for each worker. You shouldn't start this manually unless
you absolutely know what you're doing.
  

    
# 
      
        **
        Link to this section
      
      Summary
    

  
    
## 
      Functions
    

      
        
          child_spec(init_arg)

        

          

Returns a specification to start this module under a supervisor.

      

      
        
          start_link()

        

          

Starts the Supervision Tree

      

      
        
          start_server(worker)

        

          

Starts a `Que.Server` for the given worker

      

  

  

    
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
    
    
# start_link()

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
start_link() :: Supervisor.on_start()
```

      

Starts the Supervision Tree
  

  
    
      **
      Link to this function
    
    
# start_server(worker)

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
start_server(worker :: Que.Worker.t()) ::
  Supervisor.on_start_child() | no_return()
```

      

Starts a `Que.Server` for the given worker