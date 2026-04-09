# Class: Resque::Job
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Resque::Job
          
        

        show all
      
    
  
  

  
  
  
      Extended by:
      Helpers
  
  
  
  
  
      Includes:
      Helpers
  
  
  

  

  
  
    Defined in:
    lib/resque/job.rb
  
  

## Overview

  
    

A Resque::Job represents a unit of work. Each job lives on a single queue and has an associated payload object. The payload is a hash with two attributes: `class` and `args`. The `class` is the name of the Ruby class which should be used to run the job. The `args` are an array of arguments which should be passed to the Ruby class’s `perform` class-level method.

You can manually run a job using this code:

```
job = Resque::Job.reserve(:high)
klass = Resque::Job.constantize(job.payload['class'])
klass.perform(*job.payload['args'])

```

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        DontPerform =
          
  
    

Raise Resque::Job::DontPerform from a before_perform hook to abort the job.

  

  

        
        

```
Class.new(StandardError)
```

      
    
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**payload**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

This job’s associated payload object.

  

    
      
- 
  
    
      #**queue**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The name of the queue from which this job was pulled (or is to be placed).

  

    
      
- 
  
    
      #**worker**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

The worker object which is currently processing this job.

  

    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**create**(queue, klass, *args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Creates a job by placing it on a queue.

  

      
        
- 
  
    
      .**data_store**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**decode**(object)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Given a string, returns a Ruby object.

  

      
        
- 
  
    
      .**destroy**(queue, klass, *args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Removes a job from a queue.

  

      
        
- 
  
    
      .**encode**(object)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Given a Ruby object, returns a string suitable for storage in a queue.

  

      
        
- 
  
    
      .**redis**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**reserve**(queue)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Given a string queue name, returns an instance of Resque::Job if any jobs are available.

  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**==**(other)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Equality.

  

      
        
- 
  
    
      #**after_hooks**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**args**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns an array of args represented in this job’s payload.

  

      
        
- 
  
    
      #**around_hooks**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**before_hooks**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**classify**(dashed_word)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Given a word with dashes, returns a camel cased version of it.

  

      
        
- 
  
    
      #**constantize**(camel_cased_word)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Tries to find a constant with the name specified in the argument string.

  

      
        
- 
  
    
      #**data_store**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**decode**(object)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Given a string, returns a Ruby object.

  

      
        
- 
  
    
      #**encode**(object)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Given a Ruby object, returns a string suitable for storage in a queue.

  

      
        
- 
  
    
      #**fail**(exception)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Given an exception object, hands off the needed parameters to the Failure module.

  

      
        
- 
  
    
      #**failure_hooks**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**has_payload_class?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(queue, payload)  ⇒ Job 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Job.

  

      
        
- 
  
    
      #**inspect**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

String representation.

  

      
        
- 
  
    
      #**payload_class**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the actual class constant represented in this job’s payload.

  

      
        
- 
  
    
      #**payload_class_name**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the payload class as a string without raising NameError.

  

      
        
- 
  
    
      #**perform**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Attempts to perform the work represented by this job instance.

  

      
        
- 
  
    
      #**recreate**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Creates an identical job, essentially placing this job back on the queue.

  

      
        
- 
  
    
      #**redis**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**run_failure_hooks**(exception)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(queue, payload)  ⇒ Job 
  

  

  

  
    

Returns a new instance of Job.

  

  

  
    
      

```

76
77
78
79
80
```

    
    
      

```
# File 'lib/resque/job.rb', line 76

def initialize(queue, payload)
  @queue = queue
  @payload = payload
  @failure_hooks_ran = false
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**payload**  ⇒ Object  (readonly)
  

  

  

  
    

This job’s associated payload object.

  

  

  
    
      

```

74
75
76
```

    
    
      

```
# File 'lib/resque/job.rb', line 74

def payload
  @payload
end
```

    
  

    
      
      
      
  
### 
  
    #**queue**  ⇒ Object  (readonly)
  

  

  

  
    

The name of the queue from which this job was pulled (or is to be placed)

  

  

  
    
      

```

71
72
73
```

    
    
      

```
# File 'lib/resque/job.rb', line 71

def queue
  @queue
end
```

    
  

    
      
      
      
  
### 
  
    #**worker**  ⇒ Object 
  

  

  

  
    

The worker object which is currently processing this job.

  

  

  
    
      

```

67
68
69
```

    
    
      

```
# File 'lib/resque/job.rb', line 67

def worker
  @worker
end
```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**create**(queue, klass, *args)  ⇒ Object 
  

  

  

  
    

Creates a job by placing it on a queue. Expects a string queue name, a string class name, and an optional array of arguments to pass to the class’ `perform` method.

Raises an exception if no queue or class is given.

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/resque/job.rb', line 87

def self.create(queue, klass, *args)
  Resque.validate(klass, queue)

  if Resque.inline?
    # Instantiating a Resque::Job and calling perform on it so callbacks run
    # decode(encode(args)) to ensure that args are normalized in the same manner as a non-inline job
    new(:inline, {'class' => klass, 'args' => decode(encode(args))}).perform
  else
    Resque.push(queue, :class => klass.to_s, :args => args)
  end
end
```

    
  

    
      
  
### 
  
    .**data_store**  ⇒ Object 
  

  

  

  
    
      

```

26
27
28
```

    
    
      

```
# File 'lib/resque/job.rb', line 26

def self.data_store
  self.redis
end
```

    
  

    
      
  
### 
  
    .**decode**(object)  ⇒ Object 
  

  

  

  
    

Given a string, returns a Ruby object.

  

  

  
    
      

```

48
49
50
```

    
    
      

```
# File 'lib/resque/job.rb', line 48

def self.decode(object)
  Resque.decode(object)
end
```

    
  

    
      
  
### 
  
    .**destroy**(queue, klass, *args)  ⇒ Object 
  

  

  

  
    

Removes a job from a queue. Expects a string queue name, a string class name, and, optionally, args.

Returns the number of jobs destroyed.

If no args are provided, it will remove all jobs of the class provided.

That is, for these two jobs:

{ ‘class’ => ‘UpdateGraph’, ‘args’ => [‘defunkt’] } { ‘class’ => ‘UpdateGraph’, ‘args’ => [‘mojombo’] }

The following call will remove both:

```
Resque::Job.destroy(queue, 'UpdateGraph')

```

Whereas specifying args will only remove the 2nd job:

```
Resque::Job.destroy(queue, 'UpdateGraph', 'mojombo')

```

This method can be potentially very slow and memory intensive, depending on the size of your queue, as it loads all jobs into a Ruby array before processing.

  

  

  
    
      

```

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
137
138
```

    
    
      

```
# File 'lib/resque/job.rb', line 123

def self.destroy(queue, klass, *args)
  klass = klass.to_s
  destroyed = 0

  if args.empty?
    data_store.everything_in_queue(queue).each do |string|
      if decode(string)['class'] == klass
        destroyed += data_store.remove_from_queue(queue,string).to_i
      end
    end
  else
    destroyed += data_store.remove_from_queue(queue, encode(:class => klass, :args => args))
  end

  destroyed
end
```

    
  

    
      
  
### 
  
    .**encode**(object)  ⇒ Object 
  

  

  

  
    

Given a Ruby object, returns a string suitable for storage in a queue.

  

  

  
    
      

```

43
44
45
```

    
    
      

```
# File 'lib/resque/job.rb', line 43

def self.encode(object)
  Resque.encode(object)
end
```

    
  

    
      
  
### 
  
    .**redis**  ⇒ Object 
  

  

  

  
    
      

```

22
23
24
```

    
    
      

```
# File 'lib/resque/job.rb', line 22

def self.redis
  Resque.redis
end
```

    
  

    
      
  
### 
  
    .**reserve**(queue)  ⇒ Object 
  

  

  

  
    

Given a string queue name, returns an instance of Resque::Job if any jobs are available. If not, returns nil.

  

  

  
    
      

```

142
143
144
145
```

    
    
      

```
# File 'lib/resque/job.rb', line 142

def self.reserve(queue)
  return unless payload = Resque.pop(queue)
  new(queue, payload)
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**==**(other)  ⇒ Object 
  

  

  

  
    

Equality

  

  

  
    
      

```

259
260
261
262
263
```

    
    
      

```
# File 'lib/resque/job.rb', line 259

def ==(other)
  queue == other.queue &&
    payload_class == other.payload_class &&
    args == other.args
end
```

    
  

    
      
  
### 
  
    #**after_hooks**  ⇒ Object 
  

  

  

  
    
      

```

273
274
275
```

    
    
      

```
# File 'lib/resque/job.rb', line 273

def after_hooks
  @after_hooks ||= Plugin.after_hooks(payload_class)
end
```

    
  

    
      
  
### 
  
    #**args**  ⇒ Object 
  

  

  

  
    

Returns an array of args represented in this job’s payload.

  

  

  
    
      

```

226
227
228
```

    
    
      

```
# File 'lib/resque/job.rb', line 226

def args
  @payload['args']
end
```

    
  

    
      
  
### 
  
    #**around_hooks**  ⇒ Object 
  

  

  

  
    
      

```

269
270
271
```

    
    
      

```
# File 'lib/resque/job.rb', line 269

def around_hooks
  @around_hooks ||= Plugin.around_hooks(payload_class)
end
```

    
  

    
      
  
### 
  
    #**before_hooks**  ⇒ Object 
  

  

  

  
    
      

```

265
266
267
```

    
    
      

```
# File 'lib/resque/job.rb', line 265

def before_hooks
  @before_hooks ||= Plugin.before_hooks(payload_class)
end
```

    
  

    
      
  
### 
  
    #**classify**(dashed_word)  ⇒ Object 
  

  

  

  
    

Given a word with dashes, returns a camel cased version of it.

  

  

  
    
      

```

53
54
55
```

    
    
      

```
# File 'lib/resque/job.rb', line 53

def classify(dashed_word)
  Resque.classify(dashed_word)
end
```

    
  

    
      
  
### 
  
    #**constantize**(camel_cased_word)  ⇒ Object 
  

  

  

  
    

Tries to find a constant with the name specified in the argument string

  

  

  
    
      

```

58
59
60
```

    
    
      

```
# File 'lib/resque/job.rb', line 58

def constantize(camel_cased_word)
  Resque.constantize(camel_cased_word)
end
```

    
  

    
      
  
### 
  
    #**data_store**  ⇒ Object 
  

  

  

  
    
      

```

20
21
22
```

    
    
      

```
# File 'lib/resque/job.rb', line 20

def redis
  Resque.redis
end
```

    
  

    
      
  
### 
  
    #**decode**(object)  ⇒ Object 
  

  

  

  
    

Given a string, returns a Ruby object.

  

  

  
    
      

```

37
38
39
```

    
    
      

```
# File 'lib/resque/job.rb', line 37

def decode(object)
  Resque.decode(object)
end
```

    
  

    
      
  
### 
  
    #**encode**(object)  ⇒ Object 
  

  

  

  
    

Given a Ruby object, returns a string suitable for storage in a queue.

  

  

  
    
      

```

32
33
34
```

    
    
      

```
# File 'lib/resque/job.rb', line 32

def encode(object)
  Resque.encode(object)
end
```

    
  

    
      
  
### 
  
    #**fail**(exception)  ⇒ Object 
  

  

  

  
    

Given an exception object, hands off the needed parameters to the Failure module.

  

  

  
    
      

```

232
233
234
235
236
237
238
239
240
241
242
243
244
```

    
    
      

```
# File 'lib/resque/job.rb', line 232

def fail(exception)
  begin
    run_failure_hooks(exception)
  rescue Exception => e
    raise e
  ensure
    Failure.create \
      :payload   => payload,
      :exception => exception,
      :worker    => worker,
      :queue     => queue
  end
end
```

    
  

    
      
  
### 
  
    #**failure_hooks**  ⇒ Object 
  

  

  

  
    
      

```

277
278
279
```

    
    
      

```
# File 'lib/resque/job.rb', line 277

def failure_hooks
  @failure_hooks ||= Plugin.failure_hooks(payload_class)
end
```

    
  

    
      
  
### 
  
    #**has_payload_class?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

219
220
221
222
223
```

    
    
      

```
# File 'lib/resque/job.rb', line 219

def has_payload_class?
  payload_class != Object
rescue NameError
  false
end
```

    
  

    
      
  
### 
  
    #**inspect**  ⇒ Object 
  

  

  

  
    

String representation

  

  

  
    
      

```

253
254
255
256
```

    
    
      

```
# File 'lib/resque/job.rb', line 253

def inspect
  obj = @payload
  "(Job{%s} | %s | %s)" % [ @queue, obj['class'], obj['args'].inspect ]
end
```

    
  

    
      
  
### 
  
    #**payload_class**  ⇒ Object 
  

  

  

  
    

Returns the actual class constant represented in this job’s payload.

  

  

  
    
      

```

208
209
210
```

    
    
      

```
# File 'lib/resque/job.rb', line 208

def payload_class
  @payload_class ||= constantize(@payload['class'])
end
```

    
  

    
      
  
### 
  
    #**payload_class_name**  ⇒ Object 
  

  

  

  
    

Returns the payload class as a string without raising NameError

  

  

  
    
      

```

213
214
215
216
217
```

    
    
      

```
# File 'lib/resque/job.rb', line 213

def payload_class_name
  payload_class.to_s
rescue NameError
  'No Name'
end
```

    
  

    
      
  
### 
  
    #**perform**  ⇒ Object 
  

  

  

  
    

Attempts to perform the work represented by this job instance. Calls #perform on the class given in the payload with the arguments given in the payload.

  

  

  
    
      

```

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
165
166
167
168
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
180
181
182
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
197
198
199
200
201
202
203
204
205
```

    
    
      

```
# File 'lib/resque/job.rb', line 150

def perform
  job = payload_class
  job_args = args || []
  job_was_performed = false

  begin
    # Execute before_perform hook. Abort the job gracefully if
    # Resque::Job::DontPerform is raised.
    begin
      before_hooks.each do |hook|
        job.send(hook, *job_args)
      end
    rescue DontPerform
      return false
    end

    # Execute the job. Do it in an around_perform hook if available.
    if around_hooks.empty?
      job.perform(*job_args)
      job_was_performed = true
    else
      # We want to nest all around_perform plugins, with the last one
      # finally calling perform
      stack = around_hooks.reverse.inject(nil) do |last_hook, hook|
        if last_hook
          lambda do
            job.send(hook, *job_args) { last_hook.call }
          end
        else
          lambda do
            job.send(hook, *job_args) do
              result = job.perform(*job_args)
              job_was_performed = true
              result
            end
          end
        end
      end
      stack.call
    end

    # Execute after_perform hook
    after_hooks.each do |hook|
      job.send(hook, *job_args)
    end

    # Return true if the job was performed
    return job_was_performed

  # If an exception occurs during the job execution, look for an
  # on_failure hook then re-raise.
  rescue Object => e
    run_failure_hooks(e)
    raise e
  end
end
```

    
  

    
      
  
### 
  
    #**recreate**  ⇒ Object 
  

  

  

  
    

Creates an identical job, essentially placing this job back on the queue.

  

  

  
    
      

```

248
249
250
```

    
    
      

```
# File 'lib/resque/job.rb', line 248

def recreate
  self.class.create(queue, payload_class, *args)
end
```

    
  

    
      
  
### 
  
    #**redis**  ⇒ Object 
  

  

  

  
    
      

```

17
18
19
```

    
    
      

```
# File 'lib/resque/job.rb', line 17

def redis
  Resque.redis
end
```

    
  

    
      
  
### 
  
    #**run_failure_hooks**(exception)  ⇒ Object 
  

  

  

  
    
      

```

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
291
292
293
294
```

    
    
      

```
# File 'lib/resque/job.rb', line 281

def run_failure_hooks(exception)
  begin
    job_args = args || []
    if has_payload_class?
      failure_hooks.each { |hook| payload_class.send(hook, exception, *job_args) } unless @failure_hooks_ran
    end
  rescue Exception => e
    error_message = "Additional error (#{e.class}: #{e}) occurred in running failure hooks for job #{inspect}\n" \
                    "Original error that caused job failure was #{e.class}: #{exception.class}: #{exception.message}"
    raise RuntimeError.new(error_message)
  ensure
    @failure_hooks_ran = true
  end
end
```