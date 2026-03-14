# Class: Resque::Worker
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Resque::Worker
          
        

        show all
      
    
  
  

  
  
  
      Extended by:
      Helpers
  
  
  
  
  
      Includes:
      Helpers, Logging
  
  
  

  

  
  
    Defined in:
    lib/resque/worker.rb
  
  

## Overview

  
    

A Resque Worker processes jobs. On platforms that support fork(2), the worker will fork off a child to process each job. This ensures a clean slate when beginning the next job and cuts down on gradual memory growth as well as low level failures.

It also ensures workers are always listening to signals from you, their master, and can react accordingly.

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        WILDCARDS =
          
        
        

```
['*', '?', '{', '}', '[', ']'].freeze

```

      
        @@all_heartbeat_threads =
          
        
        

```
[]

```

      
    
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**fork_per_job**  ⇒ Object 
    

    
  
  
  
  
    
    
      writeonly
    
  
  
  
  
  

  
    

Sets the attribute fork_per_job.

  

    
      
- 
  
    
      #**graceful_term**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

should term kill workers gracefully (vs. immediately) Makes SIGTERM work like SIGQUIT.

  

    
      
- 
  
    
      #**hostname**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

chomp’d hostname of this worker’s machine.

  

    
      
- 
  
    
      #**job**(reload = true)  ⇒ Object 
    

    
      (also: #processing)
    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns a hash explaining the Job we’re currently processing, if any.

  

    
      
- 
  
    
      #**pid**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns Integer PID of running worker.

  

    
      
- 
  
    
      #**pre_shutdown_timeout**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute pre_shutdown_timeout.

  

    
      
- 
  
    
      #**run_at_exit_hooks**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

When set to true, forked workers will exit with `exit`, calling any `at_exit` code handlers that have been registered in the application.

  

    
      
- 
  
    
      #**term_child**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

decide whether to use new_kill_child logic.

  

    
      
- 
  
    
      #**term_child_signal**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute term_child_signal.

  

    
      
- 
  
    
      #**term_timeout**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute term_timeout.

  

    
      
- 
  
    
      #**to_s**  ⇒ Object 
    

    
      (also: #id)
    
  
  
  
  
    
    
  
  
  
  
  

  
    

The string representation is the same as the id for this worker instance.

  

    
      
- 
  
    
      #**verbose**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute verbose.

  

    
      
- 
  
    
      #**very_verbose**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute very_verbose.

  

    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**all**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns an array of all worker objects.

  

      
        
- 
  
    
      .**all_heartbeats**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**all_workers_with_expired_heartbeats**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns a list of workers that have sent a heartbeat in the past, but which already expired (does NOT include workers that have never sent a heartbeat at all).

  

      
        
- 
  
    
      .**attach**(worker_id)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Alias of `find`.

  

      
        
- 
  
    
      .**data_store**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**exists?**(worker_id)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Given a string worker id, return a boolean indicating whether the worker exists.

  

      
        
- 
  
    
      .**find**(worker_id, options = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns a single worker object.

  

      
        
- 
  
    
      .**kill_all_heartbeat_threads**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**redis**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**working**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns an array of all worker objects currently processing jobs.

  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**==**(other)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Is this worker the same as another worker?.

  

      
        
- 
  
    
      #**child_already_exited?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**data_store**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**decode**(object)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Given a string, returns a Ruby object.

  

      
        
- 
  
    
      #**done_working**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Called when we are done working - clears our `working_on` state and tells Redis we processed a job.

  

      
        
- 
  
    
      #**enable_gc_optimizations**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Enables GC Optimizations if you’re running REE.

  

      
        
- 
  
    
      #**encode**(object)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Given a Ruby object, returns a string suitable for storage in a queue.

  

      
        
- 
  
    
      #**failed**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

How many failed jobs has this worker seen? Returns an int.

  

      
        
- 
  
    
      #**failed!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Tells Redis we’ve failed a job.

  

      
        
- 
  
    
      #**fork_per_job?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**glob_match**(list, pattern)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**heartbeat**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**heartbeat!**(time = data_store.server_time)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**idle?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Boolean - true if idle, false if not.

  

      
        
- 
  
    
      #**initialize**(*queues)  ⇒ Worker 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Workers should be initialized with an array of string queue names.

  

      
        
- 
  
    
      #**inspect**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**kill_background_threads**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**kill_child**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Kills the forked child immediately, without remorse.

  

      
        
- 
  
    
      #**linux_worker_pids**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Find Resque worker pids on Linux and OS X.

  

      
        
- 
  
    
      #**log**(message)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**log!**(message)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**new_kill_child**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Kills the forked child immediately with minimal remorse.

  

      
        
- 
  
    
      #**pause_processing**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Stop processing jobs after the current one has completed (if we’re currently running one).

  

      
        
- 
  
    
      #**paused?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

are we paused?.

  

      
        
- 
  
    
      #**perform**(job)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Processes a given job in the child.

  

      
        
- 
  
    
      #**prepare**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Daemonizes the worker if ENV is set and writes the process id to ENV if set.

  

      
        
- 
  
    
      #**process**(job = nil, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

DEPRECATED.

  

      
        
- 
  
    
      #**processed**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

How many jobs has this worker processed? Returns an int.

  

      
        
- 
  
    
      #**processed!**(**opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Tell Redis we’ve processed a job.

  

      
        
- 
  
    
      #**procline**(string)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Given a string, sets the procline ($0) and logs.

  

      
        
- 
  
    
      #**prune_dead_workers**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Looks for any workers which should be running on this server and, if they’re not, removes them from Redis.

  

      
        
- 
  
    
      #**queues**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns a list of queues to use when searching for a job.

  

      
        
- 
  
    
      #**queues=**(queues)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**reconnect**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Reconnect to Redis to avoid sharing a connection with the parent, retry up to 3 times with increasing delay before giving up.

  

      
        
- 
  
    
      #**redis**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**register_signal_handlers**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Registers the various signal handlers a worker responds to.

  

      
        
- 
  
    
      #**register_worker**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Registers ourself as a worker.

  

      
        
- 
  
    
      #**remove_heartbeat**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**report_failed_job**(job, exception)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Reports the exception and marks the job as failed.

  

      
        
- 
  
    
      #**reserve**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Attempts to grab a job off one of the provided queues.

  

      
        
- 
  
    
      #**run_hook**(name, *args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Runs a named hook, passing along any arguments.

  

      
        
- 
  
    
      #**shutdown**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Schedule this worker for shutdown.

  

      
        
- 
  
    
      #**shutdown!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Kill the child and shutdown immediately.

  

      
        
- 
  
    
      #**shutdown?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Should this worker shutdown as soon as current job is finished?.

  

      
        
- 
  
    
      #**solaris_worker_pids**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Find Resque worker pids on Solaris.

  

      
        
- 
  
    
      #**start_heartbeat**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**started**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

What time did this worker start? Returns an instance of `Time`.

  

      
        
- 
  
    
      #**started!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Tell Redis we’ve started.

  

      
        
- 
  
    
      #**startup**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Runs all the methods needed when a worker begins its lifecycle.

  

      
        
- 
  
    
      #**state**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns a symbol representing the current worker state, which can be either :working or :idle.

  

      
        
- 
  
    
      #**state_change**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**unpause_processing**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Start processing jobs again after a pause.

  

      
        
- 
  
    
      #**unregister_signal_handlers**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**unregister_worker**(exception = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Unregisters ourself as a worker.

  

      
        
- 
  
    
      #**validate_queues**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

A worker must be given a queue, otherwise it won’t know what to do with itself.

  

      
        
- 
  
    
      #**wait_for_child_exit**(timeout)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**windows_worker_pids**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns an Array of string pids of all the other workers on this machine.

  

      
        
- 
  
    
      #**work**(interval = 5.0, min_interval: nil, max_interval: nil, backoff_interval: nil, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

This is the main workhorse method.

  

      
        
- 
  
    
      #**work_one_job**(job = nil, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**worker_pids**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns an Array of string pids of all the other workers on this machine.

  

      
        
- 
  
    
      #**working?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Boolean - true if working, false if not.

  

      
        
- 
  
    
      #**working_on**(job)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Given a job, tells Redis we’re working on it.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Helpers

  

classify, constantize

  
  
  
  
  
  
  
  
  
### Methods included from Logging

  

debug, error, fatal, info, log, warn

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(*queues)  ⇒ Worker 
  

  

  

  
    

Workers should be initialized with an array of string queue names. The order is important: a Worker will check the first queue given for a job. If none is found, it will check the second queue name given. If a job is found, it will be processed. Upon completion, the Worker will again check the first queue given, and so forth. In this way the queue list passed to a Worker on startup defines the priorities of queues.

If passed a single “*”, this Worker will operate on all queues in alphabetical order. Queues can be dynamically added or removed without needing to restart workers using this method.

Workers should have `#prepare` called after they are initialized if you are running work on the worker.

  

  

  
    
      

```

143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
```

    
    
      

```
# File 'lib/resque/worker.rb', line 143

def initialize(*queues)
  @shutdown = nil
  @paused = nil
  @cached_pause_value = nil
  @before_first_fork_hook_ran = false

  @heartbeat_thread = nil
  @heartbeat_thread_signal = nil

  @last_state = :idle

  verbose_value = ENV['LOGGING'] || ENV['VERBOSE']
  self.verbose = verbose_value if verbose_value
  self.very_verbose = ENV['VVERBOSE'] if ENV['VVERBOSE']
  self.pre_shutdown_timeout = (ENV['RESQUE_PRE_SHUTDOWN_TIMEOUT'] || 0.0).to_f
  self.term_timeout = (ENV['RESQUE_TERM_TIMEOUT'] || 4.0).to_f
  self.term_child = ENV['TERM_CHILD']
  self.graceful_term = ENV['GRACEFUL_TERM']
  self.run_at_exit_hooks = ENV['RUN_AT_EXIT_HOOKS']

  self.queues = queues
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**fork_per_job=**(value)  ⇒ Object  (writeonly)
  

  

  

  
    

Sets the attribute fork_per_job

  

  

Parameters:

  
    
- 
      
      
      
      
        
        

the value to set the attribute fork_per_job to.

      
    
  

  
    
      

```

65
66
67
```

    
    
      

```
# File 'lib/resque/worker.rb', line 65

def fork_per_job=(value)
  @fork_per_job = value
end

```

    
  

    
      
      
      
  
### 
  
    #**graceful_term**  ⇒ Object 
  

  

  

  
    

should term kill workers gracefully (vs. immediately) Makes SIGTERM work like SIGQUIT

  

  

  
    
      

```

59
60
61
```

    
    
      

```
# File 'lib/resque/worker.rb', line 59

def graceful_term
  @graceful_term
end

```

    
  

    
      
      
      
  
### 
  
    #**hostname**  ⇒ Object 
  

  

  

  
    

chomp’d hostname of this worker’s machine

  

  

  
    
      

```

849
850
851
```

    
    
      

```
# File 'lib/resque/worker.rb', line 849

def hostname
  @hostname ||= Socket.gethostname
end

```

    
  

    
      
      
      
  
### 
  
    #**job**(reload = true)  ⇒ Object 
  

  
    Also known as:
    processing
    
  

  

  
    

Returns a hash explaining the Job we’re currently processing, if any.

  

  

  
    
      

```

804
805
806
807
```

    
    
      

```
# File 'lib/resque/worker.rb', line 804

def job(reload = true)
  @job = nil if reload
  @job ||= decode(data_store.get_worker_payload(self)) || {}
end

```

    
  

    
      
      
      
  
### 
  
    #**pid**  ⇒ Object 
  

  

  

  
    

Returns Integer PID of running worker

  

  

  
    
      

```

854
855
856
```

    
    
      

```
# File 'lib/resque/worker.rb', line 854

def pid
  @pid ||= Process.pid
end

```

    
  

    
      
      
      
  
### 
  
    #**pre_shutdown_timeout**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute pre_shutdown_timeout.

  

  

  
    
      

```

50
51
52
```

    
    
      

```
# File 'lib/resque/worker.rb', line 50

def pre_shutdown_timeout
  @pre_shutdown_timeout
end

```

    
  

    
      
      
      
  
### 
  
    #**run_at_exit_hooks**  ⇒ Object 
  

  

  

  
    

When set to true, forked workers will exit with `exit`, calling any `at_exit` code handlers that have been registered in the application. Otherwise, forked workers exit with `exit!`

  

  

  
    
      

```

63
64
65
```

    
    
      

```
# File 'lib/resque/worker.rb', line 63

def run_at_exit_hooks
  @run_at_exit_hooks
end

```

    
  

    
      
      
      
  
### 
  
    #**term_child**  ⇒ Object 
  

  

  

  
    

decide whether to use new_kill_child logic

  

  

  
    
      

```

55
56
57
```

    
    
      

```
# File 'lib/resque/worker.rb', line 55

def term_child
  @term_child
end

```

    
  

    
      
      
      
  
### 
  
    #**term_child_signal**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute term_child_signal.

  

  

  
    
      

```

52
53
54
```

    
    
      

```
# File 'lib/resque/worker.rb', line 52

def term_child_signal
  @term_child_signal
end

```

    
  

    
      
      
      
  
### 
  
    #**term_timeout**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute term_timeout.

  

  

  
    
      

```

48
49
50
```

    
    
      

```
# File 'lib/resque/worker.rb', line 48

def term_timeout
  @term_timeout
end

```

    
  

    
      
      
      
  
### 
  
    #**to_s**  ⇒ Object 
  

  
    Also known as:
    id
    
  

  

  
    

The string representation is the same as the id for this worker instance. Can be used with `Worker.find`.

  

  

  
    
      

```

843
844
845
```

    
    
      

```
# File 'lib/resque/worker.rb', line 843

def to_s
  @to_s ||= "#{hostname}:#{pid}:#{@queues.join(',')}"
end

```

    
  

    
      
      
      
  
### 
  
    #**verbose**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute verbose.

  

  

  
    
      

```

916
917
918
```

    
    
      

```
# File 'lib/resque/worker.rb', line 916

def verbose
  @verbose
end

```

    
  

    
      
      
      
  
### 
  
    #**very_verbose**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute very_verbose.

  

  

  
    
      

```

916
917
918
```

    
    
      

```
# File 'lib/resque/worker.rb', line 916

def very_verbose
  @very_verbose
end

```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**all**  ⇒ Object 
  

  

  

  
    

Returns an array of all worker objects.

  

  

  
    
      

```

71
72
73
```

    
    
      

```
# File 'lib/resque/worker.rb', line 71

def self.all
  data_store.worker_ids.map { |id| find(id, :skip_exists => true) }.compact
end

```

    
  

    
      
  
### 
  
    .**all_heartbeats**  ⇒ Object 
  

  

  

  
    
      

```

523
524
525
```

    
    
      

```
# File 'lib/resque/worker.rb', line 523

def self.all_heartbeats
  data_store.all_heartbeats
end

```

    
  

    
      
  
### 
  
    .**all_workers_with_expired_heartbeats**  ⇒ Object 
  

  

  

  
    

Returns a list of workers that have sent a heartbeat in the past, but which already expired (does NOT include workers that have never sent a heartbeat at all).

  

  

  
    
      

```

529
530
531
532
533
534
535
536
537
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
```

    
    
      

```
# File 'lib/resque/worker.rb', line 529

def self.all_workers_with_expired_heartbeats
  # Use `Worker.all_heartbeats` instead of `Worker.all`
  # to prune workers which haven't been registered but have set a heartbeat.
  # https://github.com/resque/resque/pull/1751
  heartbeats = Worker.all_heartbeats
  now = data_store.server_time

  heartbeats.select do |id, heartbeat|
    if heartbeat
      seconds_since_heartbeat = (now - Time.parse(heartbeat)).to_i
      seconds_since_heartbeat > Resque.prune_interval
    else
      false
    end
  end.each_key.map do |id|
    # skip_exists must be true to include not registered workers
    find(id, :skip_exists => true)
  end
end

```

    
  

    
      
  
### 
  
    .**attach**(worker_id)  ⇒ Object 
  

  

  

  
    

Alias of `find`

  

  

  
    
      

```

119
120
121
```

    
    
      

```
# File 'lib/resque/worker.rb', line 119

def self.attach(worker_id)
  find(worker_id)
end

```

    
  

    
      
  
### 
  
    .**data_store**  ⇒ Object 
  

  

  

  
    
      

```

33
34
35
```

    
    
      

```
# File 'lib/resque/worker.rb', line 33

def self.data_store
  self.redis
end

```

    
  

    
      
  
### 
  
    .**exists?**(worker_id)  ⇒ Boolean 
  

  

  

  
    

Given a string worker id, return a boolean indicating whether the worker exists

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

125
126
127
```

    
    
      

```
# File 'lib/resque/worker.rb', line 125

def self.exists?(worker_id)
  data_store.worker_exists?(worker_id)
end

```

    
  

    
      
  
### 
  
    .**find**(worker_id, options = {})  ⇒ Object 
  

  

  

  
    

Returns a single worker object. Accepts a string id.

  

  

  
    
      

```

102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
```

    
    
      

```
# File 'lib/resque/worker.rb', line 102

def self.find(worker_id, options = {})
  skip_exists = options[:skip_exists]

  if skip_exists || exists?(worker_id)
    host, pid, queues_raw = worker_id.split(':', 3)
    queues = queues_raw.split(',')
    worker = new(*queues)
    worker.hostname = host
    worker.to_s = worker_id
    worker.pid = pid.to_i
    worker
  else
    nil
  end
end

```

    
  

    
      
  
### 
  
    .**kill_all_heartbeat_threads**  ⇒ Object 
  

  

  

  
    
      

```

19
20
21
22
```

    
    
      

```
# File 'lib/resque/worker.rb', line 19

def self.kill_all_heartbeat_threads
  @@all_heartbeat_threads.each(&:kill).each(&:join)
  @@all_heartbeat_threads = []
end

```

    
  

    
      
  
### 
  
    .**redis**  ⇒ Object 
  

  

  

  
    
      

```

29
30
31
```

    
    
      

```
# File 'lib/resque/worker.rb', line 29

def self.redis
  Resque.redis
end

```

    
  

    
      
  
### 
  
    .**working**  ⇒ Object 
  

  

  

  
    

Returns an array of all worker objects currently processing jobs.

  

  

  
    
      

```

77
78
79
80
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
```

    
    
      

```
# File 'lib/resque/worker.rb', line 77

def self.working
  names = all
  return [] unless names.any?

  reportedly_working = {}

  begin
    reportedly_working = data_store.workers_map(names).reject do |key, value|
      value.nil? || value.empty?
    end
  rescue Redis::Distributed::CannotDistribute
    names.each do |name|
      value = data_store.get_worker_payload(name)
      reportedly_working[name] = value unless value.nil? || value.empty?
    end
  end

  reportedly_working.keys.map do |key|
    worker = find(key.sub("worker:", ''), :skip_exists => true)
    worker.job = worker.decode(reportedly_working[key])
    worker
  end.compact
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**==**(other)  ⇒ Object 
  

  

  

  
    

Is this worker the same as another worker?

  

  

  
    
      

```

833
834
835
```

    
    
      

```
# File 'lib/resque/worker.rb', line 833

def ==(other)
  to_s == other.to_s
end

```

    
  

    
      
  
### 
  
    #**child_already_exited?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

595
596
597
```

    
    
      

```
# File 'lib/resque/worker.rb', line 595

def child_already_exited?
  Process.waitpid(@child, Process::WNOHANG)
end

```

    
  

    
      
  
### 
  
    #**data_store**  ⇒ Object 
  

  

  

  
    
      

```

27
28
29
```

    
    
      

```
# File 'lib/resque/worker.rb', line 27

def redis
  Resque.redis
end

```

    
  

    
      
  
### 
  
    #**decode**(object)  ⇒ Object 
  

  

  

  
    

Given a string, returns a Ruby object.

  

  

  
    
      

```

44
45
46
```

    
    
      

```
# File 'lib/resque/worker.rb', line 44

def decode(object)
  Resque.decode(object)
end

```

    
  

    
      
  
### 
  
    #**done_working**  ⇒ Object 
  

  

  

  
    

Called when we are done working - clears our `working_on` state and tells Redis we processed a job.

  

  

  
    
      

```

757
758
759
760
761
```

    
    
      

```
# File 'lib/resque/worker.rb', line 757

def done_working
  data_store.worker_done_working(self) do |**opts|
    processed!(**opts)
  end
end

```

    
  

    
      
  
### 
  
    #**enable_gc_optimizations**  ⇒ Object 
  

  

  

  
    

Enables GC Optimizations if you’re running REE. www.rubyenterpriseedition.com/faq.html#adapt_apps_for_cow

  

  

  
    
      

```

411
412
413
414
415
```

    
    
      

```
# File 'lib/resque/worker.rb', line 411

def enable_gc_optimizations
  if GC.respond_to?(:copy_on_write_friendly=)
    GC.copy_on_write_friendly = true
  end
end

```

    
  

    
      
  
### 
  
    #**encode**(object)  ⇒ Object 
  

  

  

  
    

Given a Ruby object, returns a string suitable for storage in a queue.

  

  

  
    
      

```

39
40
41
```

    
    
      

```
# File 'lib/resque/worker.rb', line 39

def encode(object)
  Resque.encode(object)
end

```

    
  

    
      
  
### 
  
    #**failed**  ⇒ Object 
  

  

  

  
    

How many failed jobs has this worker seen? Returns an int.

  

  

  
    
      

```

783
784
785
```

    
    
      

```
# File 'lib/resque/worker.rb', line 783

def failed
  Stat["failed:#{self}"]
end

```

    
  

    
      
  
### 
  
    #**failed!**  ⇒ Object 
  

  

  

  
    

Tells Redis we’ve failed a job.

  

  

  
    
      

```

788
789
790
791
```

    
    
      

```
# File 'lib/resque/worker.rb', line 788

def failed!
  Stat << "failed"
  Stat << "failed:#{self}"
end

```

    
  

    
      
  
### 
  
    #**fork_per_job?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

821
822
823
824
```

    
    
      

```
# File 'lib/resque/worker.rb', line 821

def fork_per_job?
  return @fork_per_job if defined?(@fork_per_job)
  @fork_per_job = ENV["FORK_PER_JOB"] != 'false' && Kernel.respond_to?(:fork)
end

```

    
  

    
      
  
### 
  
    #**glob_match**(list, pattern)  ⇒ Object 
  

  

  

  
    
      

```

220
221
222
223
224
225
```

    
    
      

```
# File 'lib/resque/worker.rb', line 220

def glob_match(list, pattern)
  list.select do |queue|
    File.fnmatch?(pattern, queue) &&
      @skip_queues.none? { |skip_pattern| File.fnmatch?(skip_pattern, queue) }
  end.sort
end

```

    
  

    
      
  
### 
  
    #**heartbeat**  ⇒ Object 
  

  

  

  
    
      

```

511
512
513
```

    
    
      

```
# File 'lib/resque/worker.rb', line 511

def heartbeat
  data_store.heartbeat(self)
end

```

    
  

    
      
  
### 
  
    #**heartbeat!**(time = data_store.server_time)  ⇒ Object 
  

  

  

  
    
      

```

519
520
521
```

    
    
      

```
# File 'lib/resque/worker.rb', line 519

def heartbeat!(time = data_store.server_time)
  data_store.heartbeat!(self, time)
end

```

    
  

    
      
  
### 
  
    #**idle?**  ⇒ Boolean 
  

  

  

  
    

Boolean - true if idle, false if not

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

817
818
819
```

    
    
      

```
# File 'lib/resque/worker.rb', line 817

def idle?
  state == :idle
end

```

    
  

    
      
  
### 
  
    #**inspect**  ⇒ Object 
  

  

  

  
    
      

```

837
838
839
```

    
    
      

```
# File 'lib/resque/worker.rb', line 837

def inspect
  "#<Worker #{to_s}>"
end

```

    
  

    
      
  
### 
  
    #**kill_background_threads**  ⇒ Object 
  

  

  

  
    
      

```

704
705
706
707
708
709
```

    
    
      

```
# File 'lib/resque/worker.rb', line 704

def kill_background_threads
  if @heartbeat_thread
    @heartbeat_thread_signal.signal
    @heartbeat_thread.join
  end
end

```

    
  

    
      
  
### 
  
    #**kill_child**  ⇒ Object 
  

  

  

  
    

Kills the forked child immediately, without remorse. The job it is processing will not be completed.

  

  

  
    
      

```

499
500
501
502
503
504
505
506
507
508
509
```

    
    
      

```
# File 'lib/resque/worker.rb', line 499

def kill_child
  if @child
    log_with_severity :debug, "Killing child at #{@child}"
    if `ps -o pid,state -p #{@child}`
      Process.kill("KILL", @child) rescue nil
    else
      log_with_severity :debug, "Child #{@child} not found, restarting."
      shutdown
    end
  end
end

```

    
  

    
      
  
### 
  
    #**linux_worker_pids**  ⇒ Object 
  

  

  

  
    

Find Resque worker pids on Linux and OS X.

  

  

  
    
      

```

879
880
881
882
883
```

    
    
      

```
# File 'lib/resque/worker.rb', line 879

def linux_worker_pids
  `ps -A -o pid,command | grep -E "[r]esque:work|[r]esque:\sStarting|[r]esque-[0-9]" | grep -v "resque-web"`.split("\n").map do |line|
    line.split(' ')[0]
  end
end

```

    
  

    
      
  
### 
  
    #**log**(message)  ⇒ Object 
  

  

  

  
    
      

```

907
908
909
```

    
    
      

```
# File 'lib/resque/worker.rb', line 907

def log(message)
  info(message)
end

```

    
  

    
      
  
### 
  
    #**log!**(message)  ⇒ Object 
  

  

  

  
    
      

```

911
912
913
```

    
    
      

```
# File 'lib/resque/worker.rb', line 911

def log!(message)
  debug(message)
end

```

    
  

    
      
  
### 
  
    #**new_kill_child**  ⇒ Object 
  

  

  

  
    

Kills the forked child immediately with minimal remorse. The job it is processing will not be completed. Send the child a TERM signal, wait <term_timeout> seconds, and then a KILL signal if it has not quit If pre_shutdown_timeout has been set to a positive number, it will allow the child that many seconds before sending the aforementioned TERM and KILL.

  

  

  
    
      

```

570
571
572
573
574
575
576
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
589
590
591
592
593
```

    
    
      

```
# File 'lib/resque/worker.rb', line 570

def new_kill_child
  if @child
    unless child_already_exited?
      if pre_shutdown_timeout && pre_shutdown_timeout > 0.0
        log_with_severity :debug, "Waiting #{pre_shutdown_timeout.to_f}s for child process to exit"
        return if wait_for_child_exit(pre_shutdown_timeout)
      end

      log_with_severity :debug, "Sending TERM signal to child #{@child}"
      Process.kill("TERM", @child)

      if wait_for_child_exit(term_timeout)
        return
      else
        log_with_severity :debug, "Sending KILL signal to child #{@child}"
        Process.kill("KILL", @child)
      end
    else
      log_with_severity :debug, "Child #{@child} already quit."
    end
  end
rescue SystemCallError
  log_with_severity :error, "Child #{@child} already quit and reaped."
end

```

    
  

    
      
  
### 
  
    #**pause_processing**  ⇒ Object 
  

  

  

  
    

Stop processing jobs after the current one has completed (if we’re currently running one).

  

  

  
    
      

```

614
615
616
617
618
619
```

    
    
      

```
# File 'lib/resque/worker.rb', line 614

def pause_processing
  _, self_write = IO.pipe
  self_write.puts "USR2 received; pausing job processing"
  run_hook :before_pause, self
  @paused = true
end

```

    
  

    
      
  
### 
  
    #**paused?**  ⇒ Boolean 
  

  

  

  
    

are we paused?

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

608
609
610
```

    
    
      

```
# File 'lib/resque/worker.rb', line 608

def paused?
  @cached_pause_value = @paused || redis.get('pause-all-workers').to_s.strip.downcase == 'true'
end

```

    
  

    
      
  
### 
  
    #**perform**(job)  ⇒ Object 
  

  

  

  
    

Processes a given job in the child.

  

  

  
    
      

```

341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
```

    
    
      

```
# File 'lib/resque/worker.rb', line 341

def perform(job)
  begin
    if fork_per_job?
      reconnect
      run_hook :after_fork, job
    end
    job.perform
  rescue Object => e
    report_failed_job(job,e)
  else
    log_with_severity :info, "done: #{job.inspect}"
  ensure
    yield job if block_given?
  end
end

```

    
  

    
      
  
### 
  
    #**prepare**  ⇒ Object 
  

  

  

  
    

Daemonizes the worker if ENV is set and writes the process id to ENV if set. Should only be called once per worker.

  

  

  
    
      

```

169
170
171
172
173
174
175
176
177
178
179
```

    
    
      

```
# File 'lib/resque/worker.rb', line 169

def prepare
  if ENV['BACKGROUND']
    Process.daemon(true)
  end

  if ENV['PIDFILE']
    File.open(ENV['PIDFILE'], 'w') { |f| f << pid }
  end

  self.reconnect if ENV['BACKGROUND']
end

```

    
  

    
      
  
### 
  
    #**process**(job = nil, &block)  ⇒ Object 
  

  

  

  
    

DEPRECATED. Processes a single job. If none is given, it will try to produce one. Usually run in the child.

  

  

  
    
      

```

314
315
316
317
318
319
320
321
322
```

    
    
      

```
# File 'lib/resque/worker.rb', line 314

def process(job = nil, &block)
  return unless job ||= reserve

  job.worker = self
  working_on job
  perform(job, &block)
ensure
  done_working
end

```

    
  

    
      
  
### 
  
    #**processed**  ⇒ Object 
  

  

  

  
    

How many jobs has this worker processed? Returns an int.

  

  

  
    
      

```

772
773
774
```

    
    
      

```
# File 'lib/resque/worker.rb', line 772

def processed
  Stat["processed:#{self}"]
end

```

    
  

    
      
  
### 
  
    #**processed!**(**opts)  ⇒ Object 
  

  

  

  
    

Tell Redis we’ve processed a job.

  

  

  
    
      

```

777
778
779
780
```

    
    
      

```
# File 'lib/resque/worker.rb', line 777

def processed!(**opts)
  Stat.incr("processed",         1, **opts)
  Stat.incr("processed:#{self}", 1, **opts)
end

```

    
  

    
      
  
### 
  
    #**procline**(string)  ⇒ Object 
  

  

  

  
    

Given a string, sets the procline ($0) and logs. Procline is always in the format of:

```
RESQUE_PROCLINE_PREFIXresque-VERSION: STRING

```

  

  

  
    
      

```

902
903
904
905
```

    
    
      

```
# File 'lib/resque/worker.rb', line 902

def procline(string)
  $0 = "#{ENV['RESQUE_PROCLINE_PREFIX']}resque-#{Resque::VERSION}: #{string}"
  log_with_severity :debug, $0
end

```

    
  

    
      
  
### 
  
    #**prune_dead_workers**  ⇒ Object 
  

  

  

  
    

Looks for any workers which should be running on this server and, if they’re not, removes them from Redis.

This is a form of garbage collection. If a server is killed by a hard shutdown, power failure, or something else beyond our control, the Resque workers will not die gracefully and therefore will leave stale state information in Redis.

By checking the current Redis state against the actual environment, we can determine if Redis is old and clean it up a bit.

  

  

  
    
      

```

639
640
641
642
643
644
645
646
647
648
649
650
651
652
653
654
655
656
657
658
659
660
661
662
663
664
665
666
667
668
669
670
671
672
673
674
675
676
677
678
679
680
681
```

    
    
      

```
# File 'lib/resque/worker.rb', line 639

def prune_dead_workers
  return unless data_store.acquire_pruning_dead_worker_lock(self, Resque.heartbeat_interval)

  all_workers = Worker.all

  known_workers = worker_pids
  all_workers_with_expired_heartbeats = Worker.all_workers_with_expired_heartbeats
  all_workers_with_expired_heartbeats.each do |worker|
    # If the worker hasn't sent a heartbeat, remove it from the registry.
    #
    # If the worker hasn't ever sent a heartbeat, we won't remove it since
    # the first heartbeat is sent before the worker is registred it means
    # that this is a worker that doesn't support heartbeats, e.g., another
    # client library or an older version of Resque. We won't touch these.
    log_with_severity :info, "Pruning dead worker: #{worker}"

    job_class = worker.job(false)['payload']['class'] rescue nil
    worker.unregister_worker(PruneDeadWorkerDirtyExit.new(worker.to_s, job_class))
  end

  all_workers.each do |worker|
    if all_workers_with_expired_heartbeats.include?(worker)
      next
    end

    host, pid, worker_queues_raw = worker.id.split(':')
    worker_queues = worker_queues_raw.split(",")
    unless @queues.include?("*") || (worker_queues.to_set == @queues.to_set)
      # If the worker we are trying to prune does not belong to the queues
      # we are listening to, we should not touch it.
      # Attempt to prune a worker from different queues may easily result in
      # an unknown class exception, since that worker could easily be even
      # written in different language.
      next
    end

    next unless host == hostname
    next if known_workers.include?(pid)

    log_with_severity :debug, "Pruning dead worker: #{worker}"
    worker.unregister_worker
  end
end

```

    
  

    
      
  
### 
  
    #**queues**  ⇒ Object 
  

  

  

  
    

Returns a list of queues to use when searching for a job. A splat (“*”) means you want every queue (in alpha order) - this can be useful for dynamically adding new queues.

  

  

  
    
      

```

211
212
213
214
215
216
217
218
```

    
    
      

```
# File 'lib/resque/worker.rb', line 211

def queues
  if @has_dynamic_queues
    current_queues = Resque.queues
    @queues.map { |queue| glob_match(current_queues, queue) }.flatten.uniq
  else
    @queues
  end
end

```

    
  

    
      
  
### 
  
    #**queues=**(queues)  ⇒ Object 
  

  

  

  
    
      

```

183
184
185
186
187
188
189
190
191
192
193
194
195
196
```

    
    
      

```
# File 'lib/resque/worker.rb', line 183

def queues=(queues)
  queues = (ENV["QUEUES"] || ENV['QUEUE']).to_s.split(',') if queues.empty?
  queues = queues.map { |queue| queue.to_s.strip }

  @skip_queues, @queues = queues.partition { |queue| queue.start_with?('!') }
  @skip_queues.map! { |queue| queue[1..-1] }

  # The behavior of `queues` is dependent on the value of `@has_dynamic_queues: if it's true, the method returns the result of filtering @queues with `glob_match`
  # if it's false, the method returns @queues directly. Since `glob_match` will cause skipped queues to be filtered out, we want to make sure it's called if we have @skip_queues.any?
  @has_dynamic_queues =
    @skip_queues.any? || WILDCARDS.any? { |char| @queues.join.include?(char) }

  validate_queues
end

```

    
  

    
      
  
### 
  
    #**reconnect**  ⇒ Object 
  

  

  

  
    

Reconnect to Redis to avoid sharing a connection with the parent, retry up to 3 times with increasing delay before giving up.

  

  

  
    
      

```

377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
```

    
    
      

```
# File 'lib/resque/worker.rb', line 377

def reconnect
  tries = 0
  begin
    data_store.reconnect
  rescue Redis::BaseConnectionError
    if (tries += 1) <= 3
      log_with_severity :error, "Error reconnecting to Redis; retrying"
      sleep(tries)
      retry
    else
      log_with_severity :error, "Error reconnecting to Redis; quitting"
      raise
    end
  end
end

```

    
  

    
      
  
### 
  
    #**redis**  ⇒ Object 
  

  

  

  
    
      

```

24
25
26
```

    
    
      

```
# File 'lib/resque/worker.rb', line 24

def redis
  Resque.redis
end

```

    
  

    
      
  
### 
  
    #**register_signal_handlers**  ⇒ Object 
  

  

  

  
    

Registers the various signal handlers a worker responds to.

TERM: Shutdown immediately, stop processing jobs.

```
INT: Shutdown immediately, stop processing jobs.

```

QUIT: Shutdown after the current job has finished processing. USR1: Kill the forked child immediately, continue processing jobs. USR2: Don’t process any new jobs CONT: Start processing jobs again after a USR2

  

  

  
    
      

```

425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
```

    
    
      

```
# File 'lib/resque/worker.rb', line 425

def register_signal_handlers
  trap('TERM') { graceful_term ? shutdown : shutdown!  }
  trap('INT')  { shutdown!  }

  begin
    trap('QUIT') { shutdown   }
    if term_child
      trap('USR1') { new_kill_child }
    else
      trap('USR1') { kill_child }
    end
    trap('USR2') { pause_processing }
    trap('CONT') { unpause_processing }
  rescue ArgumentError
    log_with_severity :warn, "Signals QUIT, USR1, USR2, and/or CONT not supported."
  end

  log_with_severity :debug, "Registered signals"
end

```

    
  

    
      
  
### 
  
    #**register_worker**  ⇒ Object 
  

  

  

  
    

Registers ourself as a worker. Useful when entering the worker lifecycle on startup.

  

  

  
    
      

```

685
686
687
```

    
    
      

```
# File 'lib/resque/worker.rb', line 685

def register_worker
  data_store.register_worker(self)
end

```

    
  

    
      
  
### 
  
    #**remove_heartbeat**  ⇒ Object 
  

  

  

  
    
      

```

515
516
517
```

    
    
      

```
# File 'lib/resque/worker.rb', line 515

def remove_heartbeat
  data_store.remove_heartbeat(self)
end

```

    
  

    
      
  
### 
  
    #**report_failed_job**(job, exception)  ⇒ Object 
  

  

  

  
    

Reports the exception and marks the job as failed

  

  

  
    
      

```

325
326
327
328
329
330
331
332
333
334
335
336
337
```

    
    
      

```
# File 'lib/resque/worker.rb', line 325

def report_failed_job(job,exception)
  log_with_severity :error, "#{job.inspect} failed: #{exception.inspect}"
  begin
    job.fail(exception)
  rescue Object => exception
    log_with_severity :error, "Received exception when reporting failure: #{exception.inspect}"
  end
  begin
    failed!
  rescue Object => exception
    log_with_severity :error, "Received exception when increasing failed jobs counter (redis issue) : #{exception.inspect}"
  end
end

```

    
  

    
      
  
### 
  
    #**reserve**  ⇒ Object 
  

  

  

  
    

Attempts to grab a job off one of the provided queues. Returns nil if no job can be found.

  

  

  
    
      

```

359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
```

    
    
      

```
# File 'lib/resque/worker.rb', line 359

def reserve
  queues.each do |queue|
    log_with_severity :debug, "Checking #{queue}"
    if job = Resque.reserve(queue)
      log_with_severity :debug, "Found job on #{queue}"
      return job
    end
  end

  nil
rescue Exception => e
  log_with_severity :error, "Error reserving job: #{e.inspect}"
  log_with_severity :error, e.backtrace.join("\n")
  raise e
end

```

    
  

    
      
  
### 
  
    #**run_hook**(name, *args)  ⇒ Object 
  

  

  

  
    

Runs a named hook, passing along any arguments.

  

  

  
    
      

```

690
691
692
693
694
695
696
697
698
699
700
701
702
```

    
    
      

```
# File 'lib/resque/worker.rb', line 690

def run_hook(name, *args)
  hooks = Resque.send(name)
  return if hooks.empty?
  return if name == :before_first_fork && @before_first_fork_hook_ran
  msg = "Running #{name} hooks"
  msg << " with #{args.inspect}" if args.any?
  log_with_severity :info, msg

  hooks.each do |hook|
    args.any? ? hook.call(*args) : hook.call
    @before_first_fork_hook_ran = true if name == :before_first_fork
  end
end

```

    
  

    
      
  
### 
  
    #**shutdown**  ⇒ Object 
  

  

  

  
    

Schedule this worker for shutdown. Will finish processing the current job.

  

  

  
    
      

```

466
467
468
469
470
471
```

    
    
      

```
# File 'lib/resque/worker.rb', line 466

def shutdown
  log_with_severity :info, 'Exiting...'
  @shutdown = true
  run_hook :shutdown
  true
end

```

    
  

    
      
  
### 
  
    #**shutdown!**  ⇒ Object 
  

  

  

  
    

Kill the child and shutdown immediately. If not forking, abort this process.

  

  

  
    
      

```

475
476
477
478
479
480
481
482
483
484
485
486
487
488
489
490
```

    
    
      

```
# File 'lib/resque/worker.rb', line 475

def shutdown!
  shutdown
  if term_child
    if fork_per_job?
      new_kill_child
    else
      # Raise TermException in the same process
      trap('TERM') do
        # ignore subsequent terms
      end
      raise TermException.new("SIGTERM")
    end
  else
    kill_child
  end
end

```

    
  

    
      
  
### 
  
    #**shutdown?**  ⇒ Boolean 
  

  

  

  
    

Should this worker shutdown as soon as current job is finished?

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

493
494
495
```

    
    
      

```
# File 'lib/resque/worker.rb', line 493

def shutdown?
  @shutdown
end

```

    
  

    
      
  
### 
  
    #**solaris_worker_pids**  ⇒ Object 
  

  

  

  
    

Find Resque worker pids on Solaris.

Returns an Array of string pids of all the other workers on this machine. Useful when pruning dead workers on startup.

  

  

  
    
      

```

889
890
891
892
893
894
895
896
897
```

    
    
      

```
# File 'lib/resque/worker.rb', line 889

def solaris_worker_pids
  `ps -A -o pid,comm | grep "[r]uby" | grep -v "resque-web"`.split("\n").map do |line|
    real_pid = line.split(' ')[0]
    pargs_command = `pargs -a #{real_pid} 2>/dev/null | grep [r]esque | grep -v "resque-web"`
    if pargs_command.split(':')[1] == " resque-#{Resque::VERSION}"
      real_pid
    end
  end.compact
end

```

    
  

    
      
  
### 
  
    #**start_heartbeat**  ⇒ Object 
  

  

  

  
    
      

```

549
550
551
552
553
554
555
556
557
558
559
560
561
562
563
```

    
    
      

```
# File 'lib/resque/worker.rb', line 549

def start_heartbeat
  remove_heartbeat

  @heartbeat_thread_signal = Resque::ThreadSignal.new

  @heartbeat_thread = Thread.new do
    loop do
      heartbeat!
      signaled = @heartbeat_thread_signal.wait_for_signal(Resque.heartbeat_interval)
      break if signaled
    end
  end

  @@all_heartbeat_threads << @heartbeat_thread
end

```

    
  

    
      
  
### 
  
    #**started**  ⇒ Object 
  

  

  

  
    

What time did this worker start? Returns an instance of `Time`

  

  

  
    
      

```

794
795
796
```

    
    
      

```
# File 'lib/resque/worker.rb', line 794

def started
  data_store.worker_start_time(self)
end

```

    
  

    
      
  
### 
  
    #**started!**  ⇒ Object 
  

  

  

  
    

Tell Redis we’ve started

  

  

  
    
      

```

799
800
801
```

    
    
      

```
# File 'lib/resque/worker.rb', line 799

def started!
  data_store.worker_started(self)
end

```

    
  

    
      
  
### 
  
    #**startup**  ⇒ Object 
  

  

  

  
    

Runs all the methods needed when a worker begins its lifecycle.

  

  

  
    
      

```

394
395
396
397
398
399
400
401
402
403
404
405
406
407
```

    
    
      

```
# File 'lib/resque/worker.rb', line 394

def startup
  $0 = "resque: Starting"

  enable_gc_optimizations
  register_signal_handlers
  start_heartbeat
  prune_dead_workers
  run_hook :before_first_fork
  register_worker

  # Fix buffering so we can `rake resque:work > resque.log` and
  # get output from the child in there.
  $stdout.sync = true
end

```

    
  

    
      
  
### 
  
    #**state**  ⇒ Object 
  

  

  

  
    

Returns a symbol representing the current worker state, which can be either :working or :idle

  

  

  
    
      

```

828
829
830
```

    
    
      

```
# File 'lib/resque/worker.rb', line 828

def state
  data_store.get_worker_payload(self) ? :working : :idle
end

```

    
  

    
      
  
### 
  
    #**state_change**  ⇒ Object 
  

  

  

  
    
      

```

763
764
765
766
767
768
769
```

    
    
      

```
# File 'lib/resque/worker.rb', line 763

def state_change
  current_state = state
  if current_state != @last_state
    run_hook :queue_empty if current_state == :idle
    @last_state = current_state
  end
end

```

    
  

    
      
  
### 
  
    #**unpause_processing**  ⇒ Object 
  

  

  

  
    

Start processing jobs again after a pause

  

  

  
    
      

```

622
623
624
625
626
627
```

    
    
      

```
# File 'lib/resque/worker.rb', line 622

def unpause_processing
  _, self_write = IO.pipe
  self_write.puts "CONT received; resuming job processing"
  @paused = false
  run_hook :after_pause, self
end

```

    
  

    
      
  
### 
  
    #**unregister_signal_handlers**  ⇒ Object 
  

  

  

  
    
      

```

445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
```

    
    
      

```
# File 'lib/resque/worker.rb', line 445

def unregister_signal_handlers
  trap('TERM') do
    trap('TERM') do
      # Ignore subsequent term signals
    end

    raise TermException.new("SIGTERM")
  end

  trap('INT', 'DEFAULT')

  begin
    trap('QUIT', 'DEFAULT')
    trap('USR1', 'DEFAULT')
    trap('USR2', 'DEFAULT')
  rescue ArgumentError
  end
end

```

    
  

    
      
  
### 
  
    #**unregister_worker**(exception = nil)  ⇒ Object 
  

  

  

  
    

Unregisters ourself as a worker. Useful when shutting down.

  

  

  
    
      

```

712
713
714
715
716
717
718
719
720
721
722
723
724
725
726
727
728
729
730
731
732
733
734
735
736
737
738
739
740
741
742
```

    
    
      

```
# File 'lib/resque/worker.rb', line 712

def unregister_worker(exception = nil)
  # If we're still processing a job, make sure it gets logged as a
  # failure.
  if (hash = processing) && !hash.empty?
    job = Job.new(hash['queue'], hash['payload'])
    # Ensure the proper worker is attached to this job, even if
    # it's not the precise instance that died.
    job.worker = self
    begin
      job.fail(exception || DirtyExit.new("Job still being processed"))
    rescue RuntimeError => e
      log_with_severity :error, e.message
    end
  end

  kill_background_threads

  data_store.unregister_worker(self) do |**opts|
    Stat.clear("processed:#{self}", **opts)
    Stat.clear("failed:#{self}",    **opts)
  end
rescue Exception => exception_while_unregistering
  message = exception_while_unregistering.message
  if exception
    message += "\nOriginal Exception (#{exception.class}): #{exception.message}"
    message += "\n  #{exception.backtrace.join("  \n")}" if exception.backtrace
  end
  fail(exception_while_unregistering.class,
       message,
       exception_while_unregistering.backtrace)
end

```

    
  

    
      
  
### 
  
    #**validate_queues**  ⇒ Object 
  

  

  

  
    

A worker must be given a queue, otherwise it won’t know what to do with itself.

You probably never need to call this.

  

  

  
    
      

```

202
203
204
205
206
```

    
    
      

```
# File 'lib/resque/worker.rb', line 202

def validate_queues
  if @queues.nil? || @queues.empty?
    raise NoQueueError.new("Please give each worker at least one queue.")
  end
end

```

    
  

    
      
  
### 
  
    #**wait_for_child_exit**(timeout)  ⇒ Object 
  

  

  

  
    
      

```

599
600
601
602
603
604
605
```

    
    
      

```
# File 'lib/resque/worker.rb', line 599

def wait_for_child_exit(timeout)
  (timeout * 10).round.times do |i|
    sleep(0.1)
    return true if child_already_exited?
  end
  false
end

```

    
  

    
      
  
### 
  
    #**windows_worker_pids**  ⇒ Object 
  

  

  

  
    

Returns an Array of string pids of all the other workers on this machine. Useful when pruning dead workers on startup.

  

  

  
    
      

```

872
873
874
875
```

    
    
      

```
# File 'lib/resque/worker.rb', line 872

def windows_worker_pids
  tasklist_output = `tasklist /FI "IMAGENAME eq ruby.exe" /FO list`.encode("UTF-8", Encoding.locale_charmap)
  tasklist_output.split($/).select { |line| line =~ /^PID:/ }.collect { |line| line.gsub(/PID:\s+/, '') }
end

```

    
  

    
      
  
### 
  
    #**work**(interval = 5.0, min_interval: nil, max_interval: nil, backoff_interval: nil, &block)  ⇒ Object 
  

  

  

  
    

This is the main workhorse method. Called on a Worker instance, it begins the worker life cycle.

The following events occur during a worker’s life cycle:

- 

Startup:   Signals are registered, dead workers are pruned,

```
and this worker is registered.

```

- 

Work loop: Jobs are pulled from a queue and processed.

- 

Teardown:  This worker is unregistered.

Can be passed a float representing the polling frequency. The default is 5 seconds, but for a semi-active site you may want to use a smaller value.

Can also be passed 3 interval floats: max, min, backoff. The actual sleep amount will float between these min/max bounds.

If a job is picked up we sleep for the minimum amount of time, but as the queues empty we increase the backoff to the max interval. This prevents idle workers from hammering the redis server with lpop requests.

Also accepts a block which will be passed the job as soon as it has completed processing. Useful for testing.

  

  

  
    
      

```

252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
```

    
    
      

```
# File 'lib/resque/worker.rb', line 252

def work(interval = 5.0,
         min_interval: nil,     # defaults to interval
         max_interval: nil,     # defaults to interval
         backoff_interval: nil, # defaults to 0.1
         &block)
  interval = Float(interval || 5.0)
  max_interval = Float(max_interval || interval)
  min_interval = Float(min_interval || interval).clamp(nil, max_interval)
  backoff_interval = Float(backoff_interval || 0.1).clamp(nil, max_interval)
  interval = interval.clamp(min_interval, max_interval)
  startup

  loop do
    break if shutdown?

    if work_one_job(&block)
      interval = min_interval
    else
      state_change
      break if interval.zero?

      interval = (interval + backoff_interval)
        .clamp(nil, max_interval)

      log_with_severity :debug, "Sleeping for #{interval} seconds"
      procline @cached_pause_value ? "Paused" : "Waiting for #{queues.join(',')}"
      sleep interval
    end
  end

  unregister_worker
  run_hook :worker_exit
rescue Exception => exception
  return if exception.class == SystemExit && !@child && run_at_exit_hooks
  log_with_severity :error, "Failed to start worker : #{exception.inspect}"
  log_with_severity :error, exception.backtrace.join("\n")
  unregister_worker(exception)
  run_hook :worker_exit
end

```

    
  

    
      
  
### 
  
    #**work_one_job**(job = nil, &block)  ⇒ Object 
  

  

  

  
    
      

```

292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
```

    
    
      

```
# File 'lib/resque/worker.rb', line 292

def work_one_job(job = nil, &block)
  return false if paused?
  return false unless job ||= reserve

  working_on job
  procline "Processing #{job.queue} since #{Time.now.to_i} [#{job.payload_class_name}]"

  log_with_severity :info, "got: #{job.inspect}"
  job.worker = self

  if fork_per_job?
    perform_with_fork(job, &block)
  else
    perform(job, &block)
  end

  done_working
  true
end

```

    
  

    
      
  
### 
  
    #**worker_pids**  ⇒ Object 
  

  

  

  
    

Returns an Array of string pids of all the other workers on this machine. Useful when pruning dead workers on startup.

  

  

  
    
      

```

860
861
862
863
864
865
866
867
868
```

    
    
      

```
# File 'lib/resque/worker.rb', line 860

def worker_pids
  if RUBY_PLATFORM =~ /solaris/
    solaris_worker_pids
  elsif RUBY_PLATFORM =~ /mingw32/
    windows_worker_pids
  else
    linux_worker_pids
  end
end

```

    
  

    
      
  
### 
  
    #**working?**  ⇒ Boolean 
  

  

  

  
    

Boolean - true if working, false if not

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

812
813
814
```

    
    
      

```
# File 'lib/resque/worker.rb', line 812

def working?
  state == :working
end

```

    
  

    
      
  
### 
  
    #**working_on**(job)  ⇒ Object 
  

  

  

  
    

Given a job, tells Redis we’re working on it. Useful for seeing what workers are doing and when.

  

  

  
    
      

```

746
747
748
749
750
751
752
753
```

    
    
      

```
# File 'lib/resque/worker.rb', line 746

def working_on(job)
  data = encode \
    :queue   => job.queue,
    :run_at  => Time.now.utc.iso8601,
    :payload => job.payload
  data_store.set_worker_payload(self,data)
  state_change
end

```