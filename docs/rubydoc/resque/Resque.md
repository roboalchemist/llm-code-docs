# Module: Resque
  
  
  

  

  
  
  
      Extended by:
      Forwardable, Resque
  
  
  
  
  
      Includes:
      Helpers
  
  
  

  
  
    Included in:
    Resque
  
  

  
  
    Defined in:
    lib/resque/web_runner.rb,

  lib/resque.rb,
 lib/resque/job.rb,
 lib/resque/stat.rb,
 lib/resque/errors.rb,
 lib/resque/plugin.rb,
 lib/resque/server.rb,
 lib/resque/worker.rb,
 lib/resque/failure.rb,
 lib/resque/helpers.rb,
 lib/resque/logging.rb,
 lib/resque/railtie.rb,
 lib/resque/version.rb,
 lib/resque/data_store.rb,
 lib/resque/failure/base.rb,
 lib/resque/failure/redis.rb,
 lib/resque/server_helper.rb,
 lib/resque/failure/airbrake.rb,
 lib/resque/failure/multiple.rb,
 lib/resque/failure/redis_multi_queue.rb,
 lib/resque/log_formatters/quiet_formatter.rb,
 lib/resque/log_formatters/verbose_formatter.rb,
 lib/resque/log_formatters/very_verbose_formatter.rb

  
  

## Overview

  
    

only used with `bin/resque-web` github.com/resque/resque/pull/1780

  

  

## Defined Under Namespace

  
    
      **Modules:** Failure, Helpers, Logging, Plugin, ServerHelper, Stat
    
  
    
      **Classes:** DataStore, DirtyExit, Job, NoClassError, NoQueueError, PruneDeadWorkerDirtyExit, QuietFormatter, Railtie, Server, TermException, ThreadSignal, VerboseFormatter, VeryVerboseFormatter, WebRunner, Worker
    
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        DEFAULT_HEARTBEAT_INTERVAL =
          
        
        

```
60
```

      
        DEFAULT_PRUNE_INTERVAL =
          
        
        

```
DEFAULT_HEARTBEAT_INTERVAL * 5
```

      
        VERSION =
          
        
        

```
'3.0.0'
```

      
        WINDOWS =
          
        
        

```
!!(RUBY_PLATFORM =~ /(mingw|bccwin|wince|mswin32)/i)
```

      
        JRUBY =
          
        
        

```
!!(RbConfig::CONFIG["RUBY_INSTALL_NAME"] =~ /^jruby/i)
```

      
    
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**enqueue_front**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      #**heartbeat_interval**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      #**inline**  ⇒ Object 
    

    
      (also: #inline?)
    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute inline.

  

    
      
- 
  
    
      #**logger**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Set or retrieve the current logger object.

  

    
      
- 
  
    
      #**prune_interval**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**after_fork**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The `after_fork` hook will be run in the child process and is passed the current job.

  

      
        
- 
  
    
      #**after_fork=**(block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Register an after_fork proc.

  

      
        
- 
  
    
      #**after_pause**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The `after_pause` hook will be run in the parent process after the worker has paused (via SIGCONT).

  

      
        
- 
  
    
      #**after_pause=**(block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Register an after_pause proc.

  

      
        
- 
  
    
      #**before_first_fork**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The `before_first_fork` hook will be run in the **parent** process only once, before forking to run the first job.

  

      
        
- 
  
    
      #**before_first_fork=**(block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Register a before_first_fork proc.

  

      
        
- 
  
    
      #**before_fork**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The `before_fork` hook will be run in the **parent** process before every job, so be careful- any changes you make will be permanent for the lifespan of the worker.

  

      
        
- 
  
    
      #**before_fork=**(block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Register a before_fork proc.

  

      
        
- 
  
    
      #**before_pause**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The `before_pause` hook will be run in the parent process before the worker has paused processing (via #pause_processing or SIGUSR2).

  

      
        
- 
  
    
      #**before_pause=**(block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Register a before_pause proc.

  

      
        
- 
  
    
      #**classify**(dashed_word)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Given a word with dashes, returns a camel cased version of it.

  

      
        
- 
  
    
      #**constantize**(camel_cased_word)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Tries to find a constant with the name specified in the argument string:.

  

      
        
- 
  
    
      #**decode**(object)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Given a string, returns a Ruby object.

  

      
        
- 
  
    
      #**dequeue**(klass, *args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

This method can be used to conveniently remove a job from a queue.

  

      
        
- 
  
    
      #**encode**(object)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Given a Ruby object, returns a string suitable for storage in a queue.

  

      
        
- 
  
    
      #**enqueue**(klass, *args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

This method can be used to conveniently add a job to a queue.

  

      
        
- 
  
    
      #**enqueue_to**(queue, klass, *args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Just like `enqueue` but allows you to specify the queue you want to use.

  

      
        
- 
  
    
      #**info**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns a hash, similar to redis-rb’s #info, of interesting stats.

  

      
        
- 
  
    
      #**keys**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns an array of all known Resque keys in Redis.

  

      
        
- 
  
    
      #**list_range**(key, start = 0, count = 1)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Does the dirty work of fetching a range of items from a Redis list and converting them into Ruby objects.

  

      
        
- 
  
    
      #**peek**(queue, start = 0, count = 1)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns an array of items currently queued, or the item itself if count = 1.

  

      
        
- 
  
    
      #**pop**(queue)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Pops a job off a queue.

  

      
        
- 
  
    
      #**push**(queue, item)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Pushes a job onto a queue.

  

      
        
- 
  
    
      #**queue_empty**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The `queue_empty` hook will be run in the **parent** process when the worker finds no more jobs in the queue and becomes idle.

  

      
        
- 
  
    
      #**queue_empty=**(block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Register a queue_empty proc.

  

      
        
- 
  
    
      #**queue_from_class**(klass)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Given a class, try to extrapolate an appropriate queue based on a class instance variable or `queue` method.

  

      
        
- 
  
    
      #**queue_sizes**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns a hash, mapping queue names to queue sizes.

  

      
        
- 
  
    
      #**queues**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns an array of all known Resque queues as strings.

  

      
        
- 
  
    
      #**redis**  ⇒ Object 
    

    
      (also: #data_store)
    
  
  
  
  
  
  
  
  

  
    

Returns the current Redis connection.

  

      
        
- 
  
    
      #**redis=**(server)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Accepts:   1.

  

      
        
- 
  
    
      #**redis_id**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**remove_queue**(queue)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Given a queue name, completely deletes the queue.

  

      
        
- 
  
    
      #**remove_worker**(worker_id)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

A shortcut to unregister_worker useful for command line tool.

  

      
        
- 
  
    
      #**reserve**(queue)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

This method will return a `Resque::Job` object or a non-true value depending on whether a job can be obtained.

  

      
        
- 
  
    
      #**sample_queues**(sample_size = 1000)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns a hash, mapping queue names to (up to `sample_size`) samples of jobs in that queue.

  

      
        
- 
  
    
      #**shutdown**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The `shutdown` hook will be run in the **child** process when the worker has received a signal to stop processing.

  

      
        
- 
  
    
      #**shutdown=**(block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Register a shutdown proc.

  

      
        
- 
  
    
      #**size**(queue)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns an integer representing the size of a queue.

  

      
        
- 
  
    
      #**stat_data_store**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the data store for the statistics module.

  

      
        
- 
  
    
      #**stat_data_store=**(stat_data_store)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Set the data store for the processed and failed statistics.

  

      
        
- 
  
    
      #**to_s**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**validate**(klass, queue = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Validates if the given klass could be a valid Resque job.

  

      
        
- 
  
    
      #**watch_queue**(queue)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Used internally to keep track of which queues we’ve created.

  

      
        
- 
  
    
      #**worker_exit**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The `worker_exit` hook will be run in the **parent** process after the worker has existed (via SIGQUIT, SIGTERM, SIGINT, etc.).

  

      
        
- 
  
    
      #**worker_exit=**(block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Register a worker_exit proc.

  

      
        
- 
  
    
      #**workers**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

A shortcut to Worker.all.

  

      
        
- 
  
    
      #**working**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

A shortcut to Worker.working.

  

      
    

  

  
  
  
  
  
  
  
  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**enqueue_front**  ⇒ Object 
  

  

  

  
    
      

```

215
216
217
218
219
220
221
```

    
    
      

```
# File 'lib/resque.rb', line 215

def enqueue_front
  if defined? @enqueue_front
    @enqueue_front
  else
    @enqueue_front = false
  end
end
```

    
  

    
      
      
      
  
### 
  
    #**heartbeat_interval**  ⇒ Object 
  

  

  

  
    
      

```

192
193
194
195
196
197
198
```

    
    
      

```
# File 'lib/resque.rb', line 192

def heartbeat_interval
  if defined? @heartbeat_interval
    @heartbeat_interval
  else
    DEFAULT_HEARTBEAT_INTERVAL
  end
end
```

    
  

    
      
      
      
  
### 
  
    #**inline**  ⇒ Object 
  

  
    Also known as:
    inline?
    
  

  

  
    

Returns the value of attribute inline.

  

  

  
    
      

```

337
338
339
```

    
    
      

```
# File 'lib/resque.rb', line 337

def inline
  @inline
end
```

    
  

    
      
      
      
  
### 
  
    #**logger**  ⇒ Object 
  

  

  

  
    

Set or retrieve the current logger object

  

  

  
    
      

```

184
185
186
```

    
    
      

```
# File 'lib/resque.rb', line 184

def logger
  @logger
end
```

    
  

    
      
      
      
  
### 
  
    #**prune_interval**  ⇒ Object 
  

  

  

  
    
      

```

202
203
204
205
206
207
208
```

    
    
      

```
# File 'lib/resque.rb', line 202

def prune_interval
  if defined? @prune_interval
    @prune_interval
  else
    DEFAULT_PRUNE_INTERVAL
  end
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**after_fork**(&block)  ⇒ Object 
  

  

  

  
    

The `after_fork` hook will be run in the child process and is passed the current job. Any changes you make, therefore, will only live as long as the job currently being processed.

Call with a block to register a hook. Call with no arguments to return all registered hooks.

  

  

  
    
      

```

260
261
262
```

    
    
      

```
# File 'lib/resque.rb', line 260

def after_fork(&block)
  block ? register_hook(:after_fork, block) : hooks(:after_fork)
end
```

    
  

    
      
  
### 
  
    #**after_fork=**(block)  ⇒ Object 
  

  

  

  
    

Register an after_fork proc.

  

  

  
    
      

```

265
266
267
```

    
    
      

```
# File 'lib/resque.rb', line 265

def after_fork=(block)
  register_hook(:after_fork, block)
end
```

    
  

    
      
  
### 
  
    #**after_pause**(&block)  ⇒ Object 
  

  

  

  
    

The `after_pause` hook will be run in the parent process after the worker has paused (via SIGCONT).

  

  

  
    
      

```

282
283
284
```

    
    
      

```
# File 'lib/resque.rb', line 282

def after_pause(&block)
  block ? register_hook(:after_pause, block) : hooks(:after_pause)
end
```

    
  

    
      
  
### 
  
    #**after_pause=**(block)  ⇒ Object 
  

  

  

  
    

Register an after_pause proc.

  

  

  
    
      

```

287
288
289
```

    
    
      

```
# File 'lib/resque.rb', line 287

def after_pause=(block)
  register_hook(:after_pause, block)
end
```

    
  

    
      
  
### 
  
    #**before_first_fork**(&block)  ⇒ Object 
  

  

  

  
    

The `before_first_fork` hook will be run in the **parent** process only once, before forking to run the first job. Be careful- any changes you make will be permanent for the lifespan of the worker.

Call with a block to register a hook. Call with no arguments to return all registered hooks.

  

  

  
    
      

```

230
231
232
```

    
    
      

```
# File 'lib/resque.rb', line 230

def before_first_fork(&block)
  block ? register_hook(:before_first_fork, block) : hooks(:before_first_fork)
end
```

    
  

    
      
  
### 
  
    #**before_first_fork=**(block)  ⇒ Object 
  

  

  

  
    

Register a before_first_fork proc.

  

  

  
    
      

```

235
236
237
```

    
    
      

```
# File 'lib/resque.rb', line 235

def before_first_fork=(block)
  register_hook(:before_first_fork, block)
end
```

    
  

    
      
  
### 
  
    #**before_fork**(&block)  ⇒ Object 
  

  

  

  
    

The `before_fork` hook will be run in the **parent** process before every job, so be careful- any changes you make will be permanent for the lifespan of the worker.

Call with a block to register a hook. Call with no arguments to return all registered hooks.

  

  

  
    
      

```

245
246
247
```

    
    
      

```
# File 'lib/resque.rb', line 245

def before_fork(&block)
  block ? register_hook(:before_fork, block) : hooks(:before_fork)
end
```

    
  

    
      
  
### 
  
    #**before_fork=**(block)  ⇒ Object 
  

  

  

  
    

Register a before_fork proc.

  

  

  
    
      

```

250
251
252
```

    
    
      

```
# File 'lib/resque.rb', line 250

def before_fork=(block)
  register_hook(:before_fork, block)
end
```

    
  

    
      
  
### 
  
    #**before_pause**(&block)  ⇒ Object 
  

  

  

  
    

The `before_pause` hook will be run in the parent process before the worker has paused processing (via #pause_processing or SIGUSR2).

  

  

  
    
      

```

271
272
273
```

    
    
      

```
# File 'lib/resque.rb', line 271

def before_pause(&block)
  block ? register_hook(:before_pause, block) : hooks(:before_pause)
end
```

    
  

    
      
  
### 
  
    #**before_pause=**(block)  ⇒ Object 
  

  

  

  
    

Register a before_pause proc.

  

  

  
    
      

```

276
277
278
```

    
    
      

```
# File 'lib/resque.rb', line 276

def before_pause=(block)
  register_hook(:before_pause, block)
end
```

    
  

    
      
  
### 
  
    #**classify**(dashed_word)  ⇒ Object 
  

  

  

  
    

Given a word with dashes, returns a camel cased version of it.

classify(‘job-name’) # => ‘JobName’

  

  

  
    
      

```

60
61
62
```

    
    
      

```
# File 'lib/resque.rb', line 60

def classify(dashed_word)
  dashed_word.split('-').map(&:capitalize).join
end
```

    
  

    
      
  
### 
  
    #**constantize**(camel_cased_word)  ⇒ Object 
  

  

  

  
    

Tries to find a constant with the name specified in the argument string:

constantize(“Module”) # => Module constantize(“Test::Unit”) # => Test::Unit

The name is assumed to be the one of a top-level constant, no matter whether it starts with “::” or not. No lexical context is taken into account:

C = ‘outside’ module M

```
C = 'inside'
C # => 'inside'
constantize("C") # => 'outside', same as ::C

```

end

NameError is raised when the constant is unknown.

  

  

  
    
      

```

81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
```

    
    
      

```
# File 'lib/resque.rb', line 81

def constantize(camel_cased_word)
  camel_cased_word = camel_cased_word.to_s

  if camel_cased_word.include?('-')
    camel_cased_word = classify(camel_cased_word)
  end

  names = camel_cased_word.split('::')
  names.shift if names.empty? || names.first.empty?

  constant = Object
  names.each do |name|
    args = Module.method(:const_get).arity != 1 ? [false] : []

    if constant.const_defined?(name, *args)
      constant = constant.const_get(name)
    else
      constant = constant.const_missing(name)
    end
  end
  constant
end
```

    
  

    
      
  
### 
  
    #**decode**(object)  ⇒ Object 
  

  

  

  
    

Given a string, returns a Ruby object.

  

  

  
    
      

```

43
44
45
46
47
48
49
50
51
52
53
54
55
```

    
    
      

```
# File 'lib/resque.rb', line 43

def decode(object)
  return unless object

  begin
    if MultiJson.respond_to?(:dump) && MultiJson.respond_to?(:load)
      MultiJson.load object
    else
      MultiJson.decode object
    end
  rescue ::MultiJson::DecodeError => e
    raise Helpers::DecodeException, e.message, e.backtrace
  end
end
```

    
  

    
      
  
### 
  
    #**dequeue**(klass, *args)  ⇒ Object 
  

  

  

  
    

This method can be used to conveniently remove a job from a queue. It assumes the class you’re passing it is a real Ruby class (not a string or reference) which either:

```
a) has a @queue ivar set
b) responds to `queue`

```

If either of those conditions are met, it will use the value obtained from performing one of the above operations to determine the queue.

If no queue can be inferred this method will raise a `Resque::NoQueueError`

If no args are given, this method will dequeue **all** jobs matching the provided class. See `Resque::Job.destroy` for more information.

Returns the number of jobs destroyed.

Example:

```
# Removes all jobs of class `UpdateNetworkGraph`
Resque.dequeue(GitHub::Jobs::UpdateNetworkGraph)

# Removes all jobs of class `UpdateNetworkGraph` with matching args.
Resque.dequeue(GitHub::Jobs::UpdateNetworkGraph, 'repo:135325')

```

This method is considered part of the `stable` API.

  

  

  
    
      

```

501
502
503
504
505
506
507
508
509
510
511
512
513
514
515
```

    
    
      

```
# File 'lib/resque.rb', line 501

def dequeue(klass, *args)
  # Perform before_dequeue hooks. Don't perform dequeue if any hook returns false
  before_hooks = Plugin.before_dequeue_hooks(klass).collect do |hook|
    klass.send(hook, *args)
  end
  return if before_hooks.any? { |result| result == false }

  destroyed = Job.destroy(queue_from_class(klass), klass, *args)

  Plugin.after_dequeue_hooks(klass).each do |hook|
    klass.send(hook, *args)
  end

  destroyed
end
```

    
  

    
      
  
### 
  
    #**encode**(object)  ⇒ Object 
  

  

  

  
    

Given a Ruby object, returns a string suitable for storage in a queue.

  

  

  
    
      

```

34
35
36
37
38
39
40
```

    
    
      

```
# File 'lib/resque.rb', line 34

def encode(object)
  if MultiJson.respond_to?(:dump) && MultiJson.respond_to?(:load)
    MultiJson.dump object
  else
    MultiJson.encode object
  end
end
```

    
  

    
      
  
### 
  
    #**enqueue**(klass, *args)  ⇒ Object 
  

  

  

  
    

This method can be used to conveniently add a job to a queue. It assumes the class you’re passing it is a real Ruby class (not a string or reference) which either:

```
a) has a @queue ivar set
b) responds to `queue`

```

If either of those conditions are met, it will use the value obtained from performing one of the above operations to determine the queue.

If no queue can be inferred this method will raise a `Resque::NoQueueError`

Returns true if the job was queued, nil if the job was rejected by a before_enqueue hook.

This method is considered part of the `stable` API.

  

  

  
    
      

```

445
446
447
```

    
    
      

```
# File 'lib/resque.rb', line 445

def enqueue(klass, *args)
  enqueue_to(queue_from_class(klass), klass, *args)
end
```

    
  

    
      
  
### 
  
    #**enqueue_to**(queue, klass, *args)  ⇒ Object 
  

  

  

  
    

Just like `enqueue` but allows you to specify the queue you want to use. Runs hooks.

`queue` should be the String name of the queue you’re targeting.

Returns true if the job was queued, nil if the job was rejected by a before_enqueue hook.

This method is considered part of the `stable` API.

  

  

  
    
      

```

458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
```

    
    
      

```
# File 'lib/resque.rb', line 458

def enqueue_to(queue, klass, *args)
  # Perform before_enqueue hooks. Don't perform enqueue if any hook returns false
  before_hooks = Plugin.before_enqueue_hooks(klass).collect do |hook|
    klass.send(hook, *args)
  end
  return nil if before_hooks.any? { |result| result == false }

  Job.create(queue, klass, *args)

  Plugin.after_enqueue_hooks(klass).each do |hook|
    klass.send(hook, *args)
  end

  return true
end
```

    
  

    
      
  
### 
  
    #**info**  ⇒ Object 
  

  

  

  
    

Returns a hash, similar to redis-rb’s #info, of interesting stats.

  

  

  
    
      

```

577
578
579
580
581
582
583
584
585
586
587
588
```

    
    
      

```
# File 'lib/resque.rb', line 577

def info
  return {
    :pending   => queue_sizes.inject(0) { |sum, (_queue_name, queue_size)| sum + queue_size },
    :processed => Stat[:processed],
    :queues    => queues.size,
    :workers   => workers.size.to_i,
    :working   => working.size,
    :failed    => data_store.num_failed,
    :servers   => [redis_id],
    :environment  => ENV['RAILS_ENV'] || ENV['RACK_ENV'] || 'development'
  }
end
```

    
  

    
      
  
### 
  
    #**keys**  ⇒ Object 
  

  

  

  
    

Returns an array of all known Resque keys in Redis. Redis’ KEYS operation is O(N) for the keyspace, so be careful - this can be slow for big databases.

  

  

  
    
      

```

592
593
594
```

    
    
      

```
# File 'lib/resque.rb', line 592

def keys
  data_store.all_resque_keys
end
```

    
  

    
      
  
### 
  
    #**list_range**(key, start = 0, count = 1)  ⇒ Object 
  

  

  

  
    

Does the dirty work of fetching a range of items from a Redis list and converting them into Ruby objects.

  

  

  
    
      

```

399
400
401
402
403
404
405
406
```

    
    
      

```
# File 'lib/resque.rb', line 399

def list_range(key, start = 0, count = 1)
  results = data_store.list_range(key, start, count)
  if count == 1
    decode(results)
  else
    results.map { |result| decode(result) }
  end
end
```

    
  

    
      
  
### 
  
    #**peek**(queue, start = 0, count = 1)  ⇒ Object 
  

  

  

  
    

Returns an array of items currently queued, or the item itself if count = 1. Queue name should be a string.

start and count should be integer and can be used for pagination. start is the item to begin, count is how many items to return.

To get the 3rd page of a 30 item, paginatied list one would use:

```
Resque.peek('my_list', 59, 30)

```

  

  

  
    
      

```

388
389
390
391
392
393
394
395
```

    
    
      

```
# File 'lib/resque.rb', line 388

def peek(queue, start = 0, count = 1)
  results = data_store.peek_in_queue(queue,start,count)
  if count == 1
    decode(results)
  else
    results.map { |result| decode(result) }
  end
end
```

    
  

    
      
  
### 
  
    #**pop**(queue)  ⇒ Object 
  

  

  

  
    

Pops a job off a queue. Queue name should be a string.

Returns a Ruby object.

  

  

  
    
      

```

370
371
372
```

    
    
      

```
# File 'lib/resque.rb', line 370

def pop(queue)
  decode(data_store.pop_from_queue(queue))
end
```

    
  

    
      
  
### 
  
    #**push**(queue, item)  ⇒ Object 
  

  

  

  
    

Pushes a job onto a queue. Queue name should be a string and the item should be any JSON-able Ruby object.

Resque works generally expect the `item` to be a hash with the following keys:

```
class - The String name of the job to run.
 args - An Array of arguments to pass the job. Usually passed
        via `class.to_class.perform(*args)`.

```

Example

```
Resque.push('archive', :class => 'Archive', :args => [ 35, 'tar' ])

```

Returns nothing

  

  

  
    
      

```

363
364
365
```

    
    
      

```
# File 'lib/resque.rb', line 363

def push(queue, item)
  data_store.push_to_queue(queue,encode(item))
end
```

    
  

    
      
  
### 
  
    #**queue_empty**(&block)  ⇒ Object 
  

  

  

  
    

The `queue_empty` hook will be run in the **parent** process when the worker finds no more jobs in the queue and becomes idle.

Call with a block to register a hook. Call with no arguments to return all registered hooks.

  

  

  
    
      

```

296
297
298
```

    
    
      

```
# File 'lib/resque.rb', line 296

def queue_empty(&block)
  block ? register_hook(:queue_empty, block) : hooks(:queue_empty)
end
```

    
  

    
      
  
### 
  
    #**queue_empty=**(block)  ⇒ Object 
  

  

  

  
    

Register a queue_empty proc.

  

  

  
    
      

```

301
302
303
```

    
    
      

```
# File 'lib/resque.rb', line 301

def queue_empty=(block)
  register_hook(:queue_empty, block)
end
```

    
  

    
      
  
### 
  
    #**queue_from_class**(klass)  ⇒ Object 
  

  

  

  
    

Given a class, try to extrapolate an appropriate queue based on a class instance variable or `queue` method.

  

  

  
    
      

```

519
520
521
522
```

    
    
      

```
# File 'lib/resque.rb', line 519

def queue_from_class(klass)
  (klass.instance_variable_defined?(:@queue) && klass.instance_variable_get(:@queue)) ||
    (klass.respond_to?(:queue) and klass.queue)
end
```

    
  

    
      
  
### 
  
    #**queue_sizes**  ⇒ Object 
  

  

  

  
    

Returns a hash, mapping queue names to queue sizes

  

  

  
    
      

```

597
598
599
600
601
602
603
604
605
606
607
```

    
    
      

```
# File 'lib/resque.rb', line 597

def queue_sizes
  queue_names = queues

  sizes = redis.pipelined do |piped|
    queue_names.each do |name|
      piped.llen("queue:#{name}")
    end
  end

  Hash[queue_names.zip(sizes)]
end
```

    
  

    
      
  
### 
  
    #**queues**  ⇒ Object 
  

  

  

  
    

Returns an array of all known Resque queues as strings.

  

  

  
    
      

```

409
410
411
```

    
    
      

```
# File 'lib/resque.rb', line 409

def queues
  data_store.queue_names
end
```

    
  

    
      
  
### 
  
    #**redis**  ⇒ Object 
  

  
    Also known as:
    data_store
    
  

  

  
    

Returns the current Redis connection. If none has been created, will create a new one.

  

  

  
    
      

```

140
141
142
143
144
```

    
    
      

```
# File 'lib/resque.rb', line 140

def redis
  return @data_store if @data_store
  self.redis = Redis.respond_to?(:connect) ? Redis.connect : "localhost:6379"
  self.redis
end
```

    
  

    
      
  
### 
  
    #**redis=**(server)  ⇒ Object 
  

  

  

  
    

Accepts:

```
1. A 'hostname:port' String
2. A 'hostname:port:db' String (to select the Redis db)
3. A 'hostname:port/namespace' String (to set the Redis namespace)
4. A Redis URL String 'redis://host:port'
5. An instance of `Redis`, `Redis::Client`, `Redis::DistRedis`,
   or `Redis::Namespace`.
6. An Hash of a redis connection {:host => 'localhost', :port => 6379, :db => 0}

```

  

  

  
    
      

```

114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
```

    
    
      

```
# File 'lib/resque.rb', line 114

def redis=(server)
  case server
  when String
    if server =~ /rediss?\:\/\//
      redis = Redis.new(:url => server)
    else
      server, namespace = server.split('/', 2)
      host, port, db = server.split(':')
      redis = Redis.new(:host => host, :port => port, :db => db)
    end
    namespace ||= :resque

    @data_store = Resque::DataStore.new(Redis::Namespace.new(namespace, :redis => redis))
  when Redis::Namespace
    @data_store = Resque::DataStore.new(server)
  when Resque::DataStore
    @data_store = server
  when Hash
    @data_store = Resque::DataStore.new(Redis::Namespace.new(:resque, :redis => Redis.new(server)))
  else
    @data_store = Resque::DataStore.new(Redis::Namespace.new(:resque, :redis => server))
  end
end
```

    
  

    
      
  
### 
  
    #**redis_id**  ⇒ Object 
  

  

  

  
    
      

```

147
148
149
```

    
    
      

```
# File 'lib/resque.rb', line 147

def redis_id
  data_store.identifier
end
```

    
  

    
      
  
### 
  
    #**remove_queue**(queue)  ⇒ Object 
  

  

  

  
    

Given a queue name, completely deletes the queue.

  

  

  
    
      

```

414
415
416
```

    
    
      

```
# File 'lib/resque.rb', line 414

def remove_queue(queue)
  data_store.remove_queue(queue)
end
```

    
  

    
      
  
### 
  
    #**remove_worker**(worker_id)  ⇒ Object 
  

  

  

  
    

A shortcut to unregister_worker useful for command line tool

  

  

  
    
      

```

567
568
569
570
```

    
    
      

```
# File 'lib/resque.rb', line 567

def remove_worker(worker_id)
  worker = Resque::Worker.find(worker_id)
  worker.unregister_worker
end
```

    
  

    
      
  
### 
  
    #**reserve**(queue)  ⇒ Object 
  

  

  

  
    

This method will return a `Resque::Job` object or a non-true value depending on whether a job can be obtained. You should pass it the precise name of a queue: case matters.

This method is considered part of the `stable` API.

  

  

  
    
      

```

529
530
531
```

    
    
      

```
# File 'lib/resque.rb', line 529

def reserve(queue)
  Job.reserve(queue)
end
```

    
  

    
      
  
### 
  
    #**sample_queues**(sample_size = 1000)  ⇒ Object 
  

  

  

  
    

Returns a hash, mapping queue names to (up to `sample_size`) samples of jobs in that queue

  

  

  
    
      

```

610
611
612
613
614
615
616
617
618
619
620
621
622
623
624
625
626
627
628
629
630
631
632
633
634
635
```

    
    
      

```
# File 'lib/resque.rb', line 610

def sample_queues(sample_size = 1000)
  queue_names = queues

  samples = redis.pipelined do |piped|
    queue_names.each do |name|
      key = "queue:#{name}"
      piped.llen(key)
      piped.lrange(key, 0, sample_size - 1)
    end
  end

  hash = {}

  queue_names.zip(samples.each_slice(2).to_a) do |queue_name, (queue_size, serialized_samples)|
    samples = serialized_samples.map do |serialized_sample|
      Job.decode(serialized_sample)
    end

    hash[queue_name] = {
      :size => queue_size,
      :samples => samples
    }
  end

  hash
end
```

    
  

    
      
  
### 
  
    #**shutdown**(&block)  ⇒ Object 
  

  

  

  
    

The `shutdown` hook will be run in the **child** process when the worker has received a signal to stop processing

Call with a block to register a hook. Call with no arguments to return all registered hooks.

  

  

  
    
      

```

324
325
326
```

    
    
      

```
# File 'lib/resque.rb', line 324

def shutdown(&block)
  block ? register_hook(:shutdown, block) : hooks(:shutdown)
end
```

    
  

    
      
  
### 
  
    #**shutdown=**(block)  ⇒ Object 
  

  

  

  
    

Register a shutdown proc.

  

  

  
    
      

```

329
330
331
```

    
    
      

```
# File 'lib/resque.rb', line 329

def shutdown=(block)
  register_hook(:shutdown, block)
end
```

    
  

    
      
  
### 
  
    #**size**(queue)  ⇒ Object 
  

  

  

  
    

Returns an integer representing the size of a queue. Queue name should be a string.

  

  

  
    
      

```

376
377
378
```

    
    
      

```
# File 'lib/resque.rb', line 376

def size(queue)
  data_store.queue_size(queue)
end
```

    
  

    
      
  
### 
  
    #**stat_data_store**  ⇒ Object 
  

  

  

  
    

Returns the data store for the statistics module.

  

  

  
    
      

```

179
180
181
```

    
    
      

```
# File 'lib/resque.rb', line 179

def stat_data_store
  Resque::Stat.data_store
end
```

    
  

    
      
  
### 
  
    #**stat_data_store=**(stat_data_store)  ⇒ Object 
  

  

  

  
    

Set the data store for the processed and failed statistics.

By default it uses the same as `Resque.redis`, but different stores can be used.

A custom store needs to obey the following API to work correctly

class NullDataStore

```
# Returns the current value for the given stat.
def stat(stat)
end

# Increments the stat by the given value.
def increment_stat(stat, by)
end

# Decrements the stat by the given value.
def decrement_stat(stat, by)
end

# Clear the values for the given stat.
def clear_stat(stat)
end

```

end

  

  

  
    
      

```

174
175
176
```

    
    
      

```
# File 'lib/resque.rb', line 174

def stat_data_store=(stat_data_store)
  Resque::Stat.data_store = stat_data_store
end
```

    
  

    
      
  
### 
  
    #**to_s**  ⇒ Object 
  

  

  

  
    
      

```

333
334
335
```

    
    
      

```
# File 'lib/resque.rb', line 333

def to_s
  "Resque Client connected to #{redis_id}"
end
```

    
  

    
      
  
### 
  
    #**validate**(klass, queue = nil)  ⇒ Object 
  

  

  

  
    

Validates if the given klass could be a valid Resque job

If no queue can be inferred this method will raise a `Resque::NoQueueError`

If given klass is nil this method will raise a `Resque::NoClassError`

  

  

  
    
      

```

538
539
540
541
542
543
544
545
546
547
548
```

    
    
      

```
# File 'lib/resque.rb', line 538

def validate(klass, queue = nil)
  queue ||= queue_from_class(klass)

  if !queue
    raise NoQueueError.new("Jobs must be placed onto a queue. No queue could be inferred for class #{klass}")
  end

  if klass.to_s.empty?
    raise NoClassError.new("Jobs must be given a class.")
  end
end
```

    
  

    
      
  
### 
  
    #**watch_queue**(queue)  ⇒ Object 
  

  

  

  
    

Used internally to keep track of which queues we’ve created. Don’t call this directly.

  

  

  
    
      

```

420
421
422
```

    
    
      

```
# File 'lib/resque.rb', line 420

def watch_queue(queue)
  data_store.watch_queue(queue)
end
```

    
  

    
      
  
### 
  
    #**worker_exit**(&block)  ⇒ Object 
  

  

  

  
    

The `worker_exit` hook will be run in the **parent** process after the worker has existed (via SIGQUIT, SIGTERM, SIGINT, etc.).

Call with a block to register a hook. Call with no arguments to return all registered hooks.

  

  

  
    
      

```

310
311
312
```

    
    
      

```
# File 'lib/resque.rb', line 310

def worker_exit(&block)
  block ? register_hook(:worker_exit, block) : hooks(:worker_exit)
end
```

    
  

    
      
  
### 
  
    #**worker_exit=**(block)  ⇒ Object 
  

  

  

  
    

Register a worker_exit proc.

  

  

  
    
      

```

315
316
317
```

    
    
      

```
# File 'lib/resque.rb', line 315

def worker_exit=(block)
  register_hook(:worker_exit, block)
end
```

    
  

    
      
  
### 
  
    #**workers**  ⇒ Object 
  

  

  

  
    

A shortcut to Worker.all

  

  

  
    
      

```

556
557
558
```

    
    
      

```
# File 'lib/resque.rb', line 556

def workers
  Worker.all
end
```

    
  

    
      
  
### 
  
    #**working**  ⇒ Object 
  

  

  

  
    

A shortcut to Worker.working

  

  

  
    
      

```

561
562
563
```

    
    
      

```
# File 'lib/resque.rb', line 561

def working
  Worker.working
end
```