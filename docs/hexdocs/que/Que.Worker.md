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
    

  Que.Worker behaviour
  (Que v0.10.1)

  

Defines a Worker for processing Jobs.

The defined worker is responsible for processing passed jobs, and
handling the job's success and failure callbacks. The defined
worker must export a `perform/1` callback otherwise compilation
will fail.
## 
  **
  

basic-worker
  
  Basic Worker

```
defmodule MyApp.Workers.SignupMailer do
  use Que.Worker

  def perform(email) do
    Mailer.send_email(to: email, message: "Thank you for signing up!")
  end
end
```

You can also pattern match and use guard clauses like normal methods:

```
defmodule MyApp.Workers.NotificationSender do
  use Que.Worker

  def perform(type: :like, to: user, count: count) do
    User.notify(user, "You have #{count} new likes on your posts")
  end

  def perform(type: :message, to: user, from: sender) do
    User.notify(user, "You received a new message from #{sender.name}")
  end

  def perform(to: user) do
    User.notify(user, "New activity on your profile")
  end
end
```

## 
  **
  

concurrency
  
  Concurrency

By default, workers process one Job at a time. You can specify a custom
value by passing the `concurrency` option.

```
defmodule MyApp.Workers.PageScraper do
  use Que.Worker, concurrency: 4

  def perform(url), do: Scraper.scrape(url)
end
```

If you want all Jobs to be processed concurrently without any limit,
you can set the concurrency option to `:infinity`. The concurrency
option must either be a positive integer or `:infinity`, otherwise
it will raise an error during compilation.
## 
  **
  

handle-job-success-failure
  
  Handle Job Success & Failure

The worker can also export optional `on_success/1` and `on_failure/2`
callbacks that handle appropriate cases.

```
defmodule MyApp.Workers.CampaignMailer do
  use Que.Worker

  def perform({campaign, user}) do
    Mailer.send_campaign_email(campaign, user: user)
  end

  def on_success({campaign, user}) do
    CampaignReport.compile(campaign, status: :success, user: user)
  end

  def on_failure({campaign, user}, error) do
    CampaignReport.compile(campaign, status: :failed, user: user)
    Logger.debug("Campaign email to #{user.id} failed: #{inspect(error)}")
  end
end
```

## 
  **
  

setup-and-teardown
  
  Setup and Teardown

You can similarly export optional `on_setup/1` and `on_teardown/1` callbacks
that are respectively run before and after the job is performed (successfully
or not). But instead of the job arguments, they pass the job struct as an
argument which holds a lot more internal details that can be useful for custom
features such as logging, metrics, requeuing and more.

```
defmodule MyApp.Workers.VideoProcessor do
  use Que.Worker

  def on_setup(%Que.Job{} = job) do
    VideoMetrics.record(job.id, :start, process: job.pid, status: :starting)
  end

  def perform({user, video, options}) do
    User.notify(user, "Your video is processing, check back later.")
    FFMPEG.process(video.path, options)
  end

  def on_teardown(%Que.Job{} = job) do
    {user, video, _options} = job.arguments
    link = MyApp.Router.video_path(user.id, video.id)

    VideoMetrics.record(job.id, :end, status: job.status)
    User.notify(user, "We've finished processing your video. See the results.", link)
  end
end
```

## 
  **
  

failed-job-retries
  
  Failed Job Retries

Failed Jobs are NOT automatically retried. If you want a job to be
retried when it fails, you can simply enqueue it again.

To get a list of all failed jobs, you can call `Que.Persistence.failed/0`.
  

    
# 
      
        **
        Link to this section
      
      Summary
    

  
    
## 
      Types
    

      
        
          t()

        

          

A valid worker module

      

  

  
    
## 
      Callbacks
    

      
        
          on_failure(arguments, error)

        

          

Optional callback that is executed if an error is raised during
job is processed (in `perform` callback)

      

      
        
          on_setup(job)

        

          

Optional callback that is executed before the job is started.

      

      
        
          on_success(arguments)

        

          

Optional callback that is executed when the job is processed
successfully.

      

      
        
          on_teardown(job)

        

          

Optional callback that is executed after the job finishes,
both on success and failure.

      

      
        
          perform(arguments)

        

          

Main callback that processes the Job.

      

  

  
    
## 
      Functions
    

      
        
          valid?(module)

        

          

Checks if the specified module is a valid Que Worker

      

      
        
          validate!(module)

        

          

Raises an error if the passed module is not a valid `Que.Worker`

      

  

  

    
# 
      
        **
        Link to this section
      
Types
    

    

  
    
      **
      Link to this type
    
    
# t()

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
t() :: module()
```

      

A valid worker module
  

    
# 
      
        **
        Link to this section
      
Callbacks
    

    

  
    
      **
      Link to this callback
    
    
# on_failure(arguments, error)

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
on_failure(arguments :: term(), error :: tuple()) :: term()
```

      

Optional callback that is executed if an error is raised during
job is processed (in `perform` callback)
  

  
    
      **
      Link to this callback
    
    
# on_setup(job)

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
on_setup(job :: Que.Job.t()) :: term()
```

      

Optional callback that is executed before the job is started.
  

  
    
      **
      Link to this callback
    
    
# on_success(arguments)

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
on_success(arguments :: term()) :: term()
```

      

Optional callback that is executed when the job is processed
successfully.
  

  
    
      **
      Link to this callback
    
    
# on_teardown(job)

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
on_teardown(job :: Que.Job.t()) :: term()
```

      

Optional callback that is executed after the job finishes,
both on success and failure.
  

  
    
      **
      Link to this callback
    
    
# perform(arguments)

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
perform(arguments :: term()) :: term()
```

      

Main callback that processes the Job.

This is a required callback that must be implemented by the worker.
If the worker doesn't export `perform/1` method, compilation will
fail. It takes one argument which is whatever that's passed to
`Que.add`.

You can define it like any other method, use guard clauses and also
use pattern matching with multiple method definitions.
  

    
# 
      
        **
        Link to this section
      
Functions
    

    

  
    
      **
      Link to this function
    
    
# valid?(module)

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
valid?(module :: module()) :: boolean()
```

      

Checks if the specified module is a valid Que Worker
## 
  **
  

example
  
  Example

```
defmodule MyWorker do
  use Que.Worker

  def perform(_args), do: nil
end

Que.Worker.valid?(MyWorker)
# => true

Que.Worker.valid?(SomeOtherModule)
# => false
```

  

  
    
      **
      Link to this function
    
    
# validate!(module)

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
validate!(module :: module()) :: :ok | no_return()
```

      

Raises an error if the passed module is not a valid `Que.Worker`