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
    

  <img src='https://i.imgur.com/Eec71eh.png' alt='Que' width='200px' />

[

Simple Background Job Processing in Elixir :zap:

Que is a job processing library backed by `Mnesia`, a distributed
real-time database that comes with Erlang / Elixir. That means it doesn't
depend on any external services like `Redis` for persisting job state. This
makes it really easy to use since you don't need to install anything other
than Que itself.

See the Documentation.

## 
  **
  

installation
  
  Installation

Add `que` to your project dependencies in `mix.exs`:

```
def deps do
  [{:que, "~> 0.10.1"}]
end
```

and then add it to your list of `applications`:

```
def application do
  [applications: [:que]]
end
```

### 
  **
  

mnesia-setup
  
  Mnesia Setup

Que runs out of the box, but by default all jobs are stored in-memory.
To persist jobs across application restarts, specify the DB path in
your `config.exs`:

```
config :mnesia, dir: 'mnesia/#{Mix.env}/#{node()}'        # Notice the single quotes
```

And run the following mix task:

```
$ mix que.setup

```

This will create the Mnesia schema and job database for you. For a
detailed guide, see the Mix Task Documentation. For
compiled releases where `Mix` is not available
see this.

## 
  **
  

usage
  
  Usage

Que is very similar to other job processing libraries such as Ku and
Toniq. Start by defining a `Worker` with a `perform/1`
callback to process your jobs:

```
defmodule App.Workers.ImageConverter do
  use Que.Worker

  def perform(image) do
    ImageTool.save_resized_copy!(image, :thumbnail)
    ImageTool.save_resized_copy!(image, :medium)
  end
end
```

You can now add jobs to be processed by the worker:

```
Que.add(App.Workers.ImageConverter, some_image)
#=> {:ok, %Que.Job{...}}
```

### 
  **
  

pattern-matching
  
  Pattern Matching

The argument here can be any term from a Tuple to a Keyword List
or a Struct. You can also pattern match and use guard clauses like
any other method:

```
defmodule App.Workers.NotificationSender do
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

### 
  **
  

concurrency
  
  Concurrency

By default, all workers process one Job at a time, but you can
customize that by passing the `concurrency` option:

```
defmodule App.Workers.SignupMailer do
  use Que.Worker, concurrency: 4

  def perform(email) do
    Mailer.send_email(to: email, message: "Thank you for signing up!")
  end
end
```

### 
  **
  

job-success-failure-callbacks
  
  Job Success / Failure Callbacks

The worker can also export optional `on_success/1` and `on_failure/2`
callbacks that handle appropriate cases.

```
defmodule App.Workers.ReportBuilder do
  use Que.Worker

  def perform({user, report}) do
    report.data
    |> PDFGenerator.generate!
    |> File.write!("reports/#{user.id}/report-#{report.id}.pdf")
  end

  def on_success({user, _}) do
    Mailer.send_email(to: user.email, subject: "Your Report is ready!")
  end

  def on_failure({user, report}, error) do
    Mailer.send_email(to: user.email, subject: "There was a problem generating your report")
    Logger.error("Could not generate report #{report.id}. Reason: #{inspect(error)}")
  end
end
```

### 
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

Head over to Hexdocs for detailed `Worker` documentation.

## 
  **
  

roadmap
  
  Roadmap

- [x] Write Documentation
- [x] Write Tests
- [x] Persist Job State to Disk

  - [x] Provide an API to interact with Jobs

- [x] Add Concurrency Support

  - [x] Make jobs work in Parallel
  - [x] Allow customizing the number of concurrent jobs

- [x] Success/Failure Callbacks
- [x] Find a more reliable replacement for Amnesia
- [ ] Delayed Jobs
- [ ] Allow job cancellation
- [ ] Job Priority
- [ ] Support running in a multi-node enviroment

  - [ ] Recover from node failures

- [ ] Support for more Persistence Adapters

  - [ ] Redis
  - [ ] Postgres

- [x] Mix Task for creating Mnesia Database
- [ ] Better Job Failures

  - [ ] Option to set timeout on workers
  - [ ] Add strategies to automatically retry failed jobs

- [ ] Web UI

## 
  **
  

contributing
  
  Contributing

- Fork, Enhance, Send PR
- Lock issues with any bugs or feature requests
- Implement something from Roadmap
- Spread the word :heart:

## 
  **
  

license
  
  License

This package is available as open source under the terms of the MIT License.

  

      
        
          â Previous Page
        
        
API Reference
        
      

  
  

  

      

          

            On Hex.pm:

            
              Package
              Preview

                (current file)

            

            
          

        

          Built using
          ExDoc (v0.28.2) for the
          Elixir programming language