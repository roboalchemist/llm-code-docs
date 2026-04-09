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
    

  Que.Supervisor 
  (Que v0.10.1)

  

This is the `Supervisor` responsible for overseeing the entire
`Que` application. You shouldn't start this manually unless
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

        

          

Starts the Supervision Tree for `Que`

      

  

  

    
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

      

Starts the Supervision Tree for `Que`