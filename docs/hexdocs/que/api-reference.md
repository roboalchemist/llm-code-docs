Search
      
    
  

  
    
    
  

  

    
      
Que
      
      **
        v0.10.1
      **
    
    

      
- Pages

        
- Modules

        
- Mix Tasks

    

  

  
  

  
    

# 

  API Reference Que v0.10.1

  
    
## 
  **
  

modules
  
  Modules

    

  
    Que

  

    

`Que` is a simple background job processing library backed by `Mnesia`.

  
    Que.Job

  

    

Module to manage a Job's state and execute the worker's callbacks.

  
    Que.Persistence

  

    

Provides a high-level API to interact with Jobs in Database

  
    Que.Persistence.Mnesia

  

    

Mnesia adapter to persist `Que.Job`s

  
    Que.Queue

  

    

Module to manage a Queue comprising of multiple jobs.

  
    Que.Server

  

    

`Que.Server` is the `GenServer` responsible for processing all Jobs.

  
    Que.ServerSupervisor

  

    

This Supervisor is responsible for spawning a `Que.Server`
for each worker. You shouldn't start this manually unless
you absolutely know what you're doing.

  
    Que.Supervisor

  

    

This is the `Supervisor` responsible for overseeing the entire
`Que` application. You shouldn't start this manually unless
you absolutely know what you're doing.

  
    Que.Worker

  

    

Defines a Worker for processing Jobs.

    
  

    
## 
  **
  

mix-tasks
  
  Mix Tasks

    

  
    mix que.setup

  

    

Creates an Mnesia DB on disk for Que