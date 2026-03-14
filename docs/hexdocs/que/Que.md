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
    

  Que 
  (Que v0.10.1)

  

`Que` is a simple background job processing library backed by `Mnesia`.

Que doesn't depend on any external services like Redis for persisting job
state, instead uses the built-in erlang application
`mnesia`. This makes it extremely
easy to use as you don't need to install anything other than Que itself.
## 
  **
  

installation
  
  Installation

First add it as a dependency in your `mix.exs` and run `mix deps.get`:

```
defp deps do
  [{:que, "~> 0.10.1"}]
end
```

Then run `$ mix deps.get` and add it to your list of applications:

```
def application do
  [applications: [:que]]
end
```

## 
  **
  

usage
  
  Usage

Define a `Worker` to process your jobs:

```
defmodule App.Workers.ImageConverter do
  use Que.Worker

  def perform(image) do
    ImageTool.save_resized_copy!(image, :thumbnail)
    ImageTool.save_resized_copy!(image, :medium)
    ImageTool.save_resized_copy!(image, :large)
  end
end
```

You can now add jobs to be processed by the worker:

```
Que.add(App.Workers.ImageConverter, some_image)
#=> :ok
```

Read the `Que.Worker` documentation for other callbacks and
concurrency options.
## 
  **
  

persist-to-disk
  
  Persist to Disk

By default, `Que` uses an in-memory `Mnesia` database so jobs are NOT
persisted across application restarts. To do that, you first need to
specify a path for your mnesia database in you `config.exs`.

```
config :mnesia, dir: 'mnesia/#{Mix.env}/#{node()}'
# Notice the single quotes
```

You can now call the `que.setup` mix task to create the job database:

```
$ mix que.setup

```

For compiled releases, see the `Que.Persistence.Mnesia` documentation.
  

    
# 
      
        **
        Link to this section
      
      Summary
    

  
    
## 
      Functions
    

      
        
          add(worker, arguments)

        

          

Enqueues a Job to be processed by Que.

      

      
        
          start(type, args)

        

          

Starts the Que Application (and its Supervision Tree)

      

  

  

    
# 
      
        **
        Link to this section
      
Functions
    

    

  
    
      **
      Link to this function
    
    
# add(worker, arguments)

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
add(worker :: module(), arguments :: term()) ::
  {:ok,
   %Que.Job{
     arguments: term(),
     created_at: term(),
     id: term(),
     pid: term(),
     ref: term(),
     status: term(),
     updated_at: term(),
     worker: term()
   }}
```

      

Enqueues a Job to be processed by Que.

Accepts the worker module name and a term to be passed to
the worker as arguments.
## 
  **
  

example
  
  Example

```
Que.add(App.Workers.FileDownloader, {"http://example.com/file/path.zip", "/some/local/path.zip"})
#=> :ok

Que.add(App.Workers.SignupMailer, to: "some@email.com", message: "Thank you for Signing up!")
#=> :ok
```

  

  
    
      **
      Link to this function
    
    
# start(type, args)

      
       **
       View Source
     

  

  

Starts the Que Application (and its Supervision Tree)