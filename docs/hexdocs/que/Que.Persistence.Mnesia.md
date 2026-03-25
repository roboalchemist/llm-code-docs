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
    

  Que.Persistence.Mnesia 
  (Que v0.10.1)

  

Mnesia adapter to persist `Que.Job`s

This module defines a Database and a Job Table in Mnesia to keep
track of all Jobs, along with Mnesia transaction methods that
provide an easy way to find, insert, update or destroy Jobs from
the Database.

It implements all callbacks defined in `Que.Persistence`, along
with some `Mnesia` specific ones. You should read the
`Que.Persistence` documentation if you just want to interact
with the Jobs in database.
## 
  **
  

persisting-to-disk
  
  Persisting to Disk

`Que` works out of the box without any configuration needed, but
initially all Jobs are not persisted to disk, and are only in
memory. You'll need to create the Mnesia Schema on disk and create
the Job Database for this to work.

Que provides ways that automatically do this for you. First,
specify the location where you want your Mnesia database to be
created in your `config.exs` file. It's highly recommended that you
specify your `Mix.env` in the path to keep development, test and
production databases separate.

```
config :mnesia, dir: 'mnesia/#{Mix.env}/#{node()}'
# Notice the single quotes
```

You can now either run the `Mix.Tasks.Que.Setup` mix task or call
`Que.Persistence.Mnesia.setup!/0` to create the Schema, Database
and Tables.
  

    
# 
      
        **
        Link to this section
      
      Summary
    

  
    
## 
      Functions
    

      
        
          __config__()

        

          

Returns the Mnesia configuration for Que

      

      
        
          setup!(nodes \\ [node()])

        

          

Creates the Mnesia Database for `Que` on disk

      

  

  

    
# 
      
        **
        Link to this section
      
Functions
    

    

  
    
      **
      Link to this function
    
    
# __config__()

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
__config__() :: Keyword.t()
```

      

Returns the Mnesia configuration for Que
  

    

  
    
      **
      Link to this function
    
    
# setup!(nodes \\ [node()])

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
setup!(nodes :: [node()]) :: :ok
```

      

Creates the Mnesia Database for `Que` on disk

This creates the Schema, Database and Tables for
Que Jobs on disk for the specified erlang nodes so
Jobs are persisted across application restarts.
Calling this momentarily stops the `:mnesia`
application so you should make sure it's not being
used when you do.

If no argument is provided, the database is created
for the current node.
## 
  **
  

on-production
  
  On Production

For a compiled release (`Distillery` or `Exrm`),
start the application in console mode or connect a
shell to the running release and simply call the
method:

```
$ bin/my_app remote_console

iex(my_app@127.0.0.1)1> Que.Persistence.Mnesia.setup!
:ok

```

You can alternatively provide a list of nodes for
which you would like to create the schema:

```
iex(my_app@host_x)1> nodes = [node() | Node.list]
[:my_app@host_x, :my_app@host_y, :my_app@host_z]

iex(my_app@node_x)2> Que.Persistence.Mnesia.setup!(nodes)
:ok
```