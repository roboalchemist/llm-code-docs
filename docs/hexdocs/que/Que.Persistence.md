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
    

  Que.Persistence behaviour
  (Que v0.10.1)

  

Provides a high-level API to interact with Jobs in Database

This module is a behaviour that delegates calls to the specified
adapter. It has been designed in a way that it's easy to write
custom adapters for other databases or stores like Redis, even
though there are no current plans on supporting anything other
than `Mnesia`.
  

    
# 
      
        **
        Link to this section
      
      Summary
    

  
    
## 
      Callbacks
    

      
        
          all()

        

          

Returns all `Que.Job`s in the database.

      

      
        
          all(worker)

        

          

Returns all `Que.Job`s for the given worker.

      

      
        
          completed()

        

          

Returns completed `Que.Job`s from the database.

      

      
        
          completed(worker)

        

          

Returns completed `Que.Job`s for the given worker.

      

      
        
          destroy(id)

        

          

Deletes a `Que.Job` from the database.

      

      
        
          failed()

        

          

Returns failed `Que.Job`s from the database.

      

      
        
          failed(worker)

        

          

Returns failed `Que.Job`s for the given worker.

      

      
        
          find(id)

        

          

Finds a `Que.Job` from the database.

      

      
        
          incomplete()

        

          

Returns incomplete `Que.Job`s from the database.

      

      
        
          incomplete(worker)

        

          

Returns incomplete `Que.Job`s for the given worker.

      

      
        
          initialize()

        

          

Makes sure that the Database is ready to be used.

      

      
        
          insert(job)

        

          

Inserts a `Que.Job` into the database.

      

      
        
          update(job)

        

          

Updates an existing `Que.Job` in the database.

      

  

  
    
## 
      Functions
    

      
        
          all()

        

          

See `Que.Persistence.Mnesia.all/0`.

      

      
        
          all(worker)

        

          

See `Que.Persistence.Mnesia.all/1`.

      

      
        
          completed()

        

          

See `Que.Persistence.Mnesia.completed/0`.

      

      
        
          completed(worker)

        

          

See `Que.Persistence.Mnesia.completed/1`.

      

      
        
          destroy(id)

        

          

See `Que.Persistence.Mnesia.destroy/1`.

      

      
        
          failed()

        

          

See `Que.Persistence.Mnesia.failed/0`.

      

      
        
          failed(worker)

        

          

See `Que.Persistence.Mnesia.failed/1`.

      

      
        
          find(id)

        

          

See `Que.Persistence.Mnesia.find/1`.

      

      
        
          incomplete()

        

          

See `Que.Persistence.Mnesia.incomplete/0`.

      

      
        
          incomplete(worker)

        

          

See `Que.Persistence.Mnesia.incomplete/1`.

      

      
        
          initialize()

        

          

See `Que.Persistence.Mnesia.initialize/0`.

      

      
        
          insert(job)

        

          

See `Que.Persistence.Mnesia.insert/1`.

      

      
        
          update(job)

        

          

See `Que.Persistence.Mnesia.update/1`.

      

  

  

    
# 
      
        **
        Link to this section
      
Callbacks
    

    

  
    
      **
      Link to this callback
    
    
# all()

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
all() :: [Que.Job.t()]
```

      

Returns all `Que.Job`s in the database.
  

  
    
      **
      Link to this callback
    
    
# all(worker)

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
all(worker :: Que.Worker.t()) :: [Que.Job.t()]
```

      

Returns all `Que.Job`s for the given worker.
  

  
    
      **
      Link to this callback
    
    
# completed()

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
completed() :: [Que.Job.t()]
```

      

Returns completed `Que.Job`s from the database.
  

  
    
      **
      Link to this callback
    
    
# completed(worker)

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
completed(worker :: Que.Worker.t()) :: [Que.Job.t()]
```

      

Returns completed `Que.Job`s for the given worker.
  

  
    
      **
      Link to this callback
    
    
# destroy(id)

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
destroy(id :: integer()) :: :ok | no_return()
```

      

Deletes a `Que.Job` from the database.
  

  
    
      **
      Link to this callback
    
    
# failed()

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
failed() :: [Que.Job.t()]
```

      

Returns failed `Que.Job`s from the database.
  

  
    
      **
      Link to this callback
    
    
# failed(worker)

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
failed(worker :: Que.Worker.t()) :: [Que.Job.t()]
```

      

Returns failed `Que.Job`s for the given worker.
  

  
    
      **
      Link to this callback
    
    
# find(id)

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
find(id :: integer()) :: Que.Job.t() | nil
```

      

Finds a `Que.Job` from the database.

Returns the a Job struct if it's found, otherwise `nil`.
  

  
    
      **
      Link to this callback
    
    
# incomplete()

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
incomplete() :: [Que.Job.t()]
```

      

Returns incomplete `Que.Job`s from the database.

This includes all Jobs whose status is either
`:queued` or `:started` but not `:failed`.
  

  
    
      **
      Link to this callback
    
    
# incomplete(worker)

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
incomplete(worker :: Que.Worker.t()) :: [Que.Job.t()]
```

      

Returns incomplete `Que.Job`s for the given worker.
  

  
    
      **
      Link to this callback
    
    
# initialize()

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
initialize() :: :ok | :error
```

      

Makes sure that the Database is ready to be used.

This is called when the Que application, specifically
`Que.Server`, starts to make sure that a database exists
and is ready to be used.
  

  
    
      **
      Link to this callback
    
    
# insert(job)

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
insert(job :: Que.Job.t()) :: Que.Job.t()
```

      

Inserts a `Que.Job` into the database.

Returns the same Job struct with the `id` value set
  

  
    
      **
      Link to this callback
    
    
# update(job)

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
update(job :: Que.Job.t()) :: Que.Job.t()
```

      

Updates an existing `Que.Job` in the database.

This methods finds the job to update by the given
job's id. If no job with the given id exists, it is
inserted as-is. If the id of the given job is nil,
it's still inserted and a valid id is assigned.

Returns the updated job.
  

    
# 
      
        **
        Link to this section
      
Functions
    

    

  
    
      **
      Link to this function
    
    
# all()

      
       **
       View Source
     

  

  

See `Que.Persistence.Mnesia.all/0`.
  

  
    
      **
      Link to this function
    
    
# all(worker)

      
       **
       View Source
     

  

  

See `Que.Persistence.Mnesia.all/1`.
  

  
    
      **
      Link to this function
    
    
# completed()

      
       **
       View Source
     

  

  

See `Que.Persistence.Mnesia.completed/0`.
  

  
    
      **
      Link to this function
    
    
# completed(worker)

      
       **
       View Source
     

  

  

See `Que.Persistence.Mnesia.completed/1`.
  

  
    
      **
      Link to this function
    
    
# destroy(id)

      
       **
       View Source
     

  

  

See `Que.Persistence.Mnesia.destroy/1`.
  

  
    
      **
      Link to this function
    
    
# failed()

      
       **
       View Source
     

  

  

See `Que.Persistence.Mnesia.failed/0`.
  

  
    
      **
      Link to this function
    
    
# failed(worker)

      
       **
       View Source
     

  

  

See `Que.Persistence.Mnesia.failed/1`.
  

  
    
      **
      Link to this function
    
    
# find(id)

      
       **
       View Source
     

  

  

See `Que.Persistence.Mnesia.find/1`.
  

  
    
      **
      Link to this function
    
    
# incomplete()

      
       **
       View Source
     

  

  

See `Que.Persistence.Mnesia.incomplete/0`.
  

  
    
      **
      Link to this function
    
    
# incomplete(worker)

      
       **
       View Source
     

  

  

See `Que.Persistence.Mnesia.incomplete/1`.
  

  
    
      **
      Link to this function
    
    
# initialize()

      
       **
       View Source
     

  

  

See `Que.Persistence.Mnesia.initialize/0`.
  

  
    
      **
      Link to this function
    
    
# insert(job)

      
       **
       View Source
     

  

  

See `Que.Persistence.Mnesia.insert/1`.
  

  
    
      **
      Link to this function
    
    
# update(job)

      
       **
       View Source
     

  

  

See `Que.Persistence.Mnesia.update/1`.