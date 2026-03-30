# Class: RubyProf::Thread
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- RubyProf::Thread
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    ext/ruby_prof/rp_thread.c,

  lib/ruby-prof/thread.rb,
 ext/ruby_prof/rp_thread.c

  
  

## Overview

  
    

The Thread class contains profile results for a single fiber (note a Ruby thread can run multiple fibers). You cannot create an instance of RubyProf::Thread, instead you access it from a RubyProf::Profile object.

```
profile = RubyProf::Profile.profile do
            ...
          end

profile.threads.each do |thread|
  thread.root_methods.sort.each do |method|
    puts method.total_time
  end
end

```

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**_dump_data**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      #**_load_data**(data)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      #**call_tree**  ⇒ CallTree 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the root call tree.

  

      
        
- 
  
    
      #**fiber_id**  ⇒ Numeric 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the fiber id of this thread.

  

      
        
- 
  
    
      #**id**  ⇒ Numeric 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the thread id of this thread.

  

      
        
- 
  
    
      #**new**(call_tree, thread, fiber)  ⇒ Object 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Creates a new RubyProf thread instance.

  

      
        
- 
  
    
      #**merge!**(other)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**methods**  ⇒ Array 
    

    
  
  
  
  
  
  
  
  

  
    

Returns an array of methods that were called from this thread during program execution.

  

      
        
- 
  
    
      #**total_time**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the total time this thread was executed.

  

      
        
- 
  
    
      #**wait_time**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the amount of time this thread waited while other thread executed.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**new**(call_tree, thread, fiber)  ⇒ Object 
  

  

  

  
    

Creates a new RubyProf thread instance. `call_tree` is the root call_tree instance, `thread` is a reference to a Ruby thread and `fiber` is a reference to a Ruby fiber.

  

  
  

  
    
      

```

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
311
312
313
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
# File 'ext/ruby_prof/rp_thread.c', line 300

static VALUE prof_thread_initialize(VALUE self, VALUE call_tree, VALUE thread, VALUE fiber)
{
  thread_data_t* thread_ptr = prof_get_thread(self);

  // This call tree must now be managed by C
  thread_ptr->call_tree = prof_get_call_tree(call_tree);
  thread_ptr->call_tree->owner = OWNER_C;

  thread_ptr->fiber = fiber;
  thread_ptr->fiber_id = rb_obj_id(fiber);
  thread_ptr->thread_id = rb_obj_id(thread);

  // Add methods from call trees into thread methods table
  VALUE methods = prof_call_tree_methods(thread_ptr->call_tree);
  for (int i = 0; i < rb_array_len(methods); i++)
  {
      VALUE method = rb_ary_entry(methods, i);
      prof_method_t* method_ptr = prof_get_method(method);
      method_table_insert(thread_ptr->method_table, method_ptr->key, method_ptr);
  }

  return self;
}
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**_dump_data**  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

384
385
386
387
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
# File 'ext/ruby_prof/rp_thread.c', line 384

static VALUE prof_thread_dump(VALUE self)
{
    thread_data_t* thread_data = RTYPEDDATA_DATA(self);

    VALUE result = rb_hash_new();
    rb_hash_aset(result, ID2SYM(rb_intern("owner")), INT2FIX(thread_data->owner));
    rb_hash_aset(result, ID2SYM(rb_intern("fiber_id")), thread_data->fiber_id);
    rb_hash_aset(result, ID2SYM(rb_intern("methods")), prof_thread_methods(self));
    rb_hash_aset(result, ID2SYM(rb_intern("call_tree")), prof_call_tree(self));

    return result;
}
```

    
  

    
      
  
### 
  
    #**_load_data**(data)  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

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
408
409
410
411
412
413
414
415
416
417
418
```

    
    
      

```
# File 'ext/ruby_prof/rp_thread.c', line 398

static VALUE prof_thread_load(VALUE self, VALUE data)
{
    thread_data_t* thread_data = RTYPEDDATA_DATA(self);

    thread_data->owner = FIX2INT(rb_hash_aref(data, ID2SYM(rb_intern("owner"))));

    VALUE call_tree = rb_hash_aref(data, ID2SYM(rb_intern("call_tree")));
    thread_data->call_tree = prof_get_call_tree(call_tree);

    thread_data->fiber_id = rb_hash_aref(data, ID2SYM(rb_intern("fiber_id")));

    VALUE methods = rb_hash_aref(data, ID2SYM(rb_intern("methods")));
    for (int i = 0; i < rb_array_len(methods); i++)
    {
        VALUE method = rb_ary_entry(methods, i);
        prof_method_t* method_data = RTYPEDDATA_DATA(method);
        method_table_insert(thread_data->method_table, method_data->key, method_data);
    }

    return data;
}
```

    
  

    
      
  
### 
  
    #**call_tree**  ⇒ CallTree 
  

  

  

  
    

Returns the root call tree.

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (CallTree)
      
      
      
    
  

  
    
      

```

348
349
350
351
352
```

    
    
      

```
# File 'ext/ruby_prof/rp_thread.c', line 348

static VALUE prof_call_tree(VALUE self)
{
    thread_data_t* thread = prof_get_thread(self);
    return prof_call_tree_wrap(thread->call_tree);
}
```

    
  

    
      
  
### 
  
    #**fiber_id**  ⇒ Numeric 
  

  

  

  
    

Returns the fiber id of this thread.

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (Numeric)
      
      
      
    
  

  
    
      

```

338
339
340
341
342
```

    
    
      

```
# File 'ext/ruby_prof/rp_thread.c', line 338

static VALUE prof_fiber_id(VALUE self)
{
    thread_data_t* thread = prof_get_thread(self);
    return thread->fiber_id;
}
```

    
  

    
      
  
### 
  
    #**id**  ⇒ Numeric 
  

  

  

  
    

Returns the thread id of this thread.

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (Numeric)
      
      
      
    
  

  
    
      

```

328
329
330
331
332
```

    
    
      

```
# File 'ext/ruby_prof/rp_thread.c', line 328

static VALUE prof_thread_id(VALUE self)
{
    thread_data_t* thread = prof_get_thread(self);
    return thread->thread_id;
}
```

    
  

    
      
  
### 
  
    #**merge!**(other)  ⇒ Object 
  

  

  

  
    
      

```

370
371
372
373
374
375
376
377
378
379
380
381
```

    
    
      

```
# File 'ext/ruby_prof/rp_thread.c', line 370

static VALUE prof_thread_merge(VALUE self, VALUE other)
{
  thread_data_t* self_ptr = prof_get_thread(self);
  thread_data_t* other_ptr = prof_get_thread(other);
  prof_method_table_merge(self_ptr->method_table, other_ptr->method_table);
  prof_call_tree_merge_internal(self_ptr->call_tree, other_ptr->call_tree, self_ptr->method_table);

  // Reset method cache since it just changed
  self_ptr->methods = Qnil;

  return other;
}
```

    
  

    
      
  
### 
  
    #**methods**  ⇒ Array 
  

  

  

  
    

Returns an array of methods that were called from this thread during program execution.

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (Array)
      
      
      
    
  

  
    
      

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
```

    
    
      

```
# File 'ext/ruby_prof/rp_thread.c', line 359

static VALUE prof_thread_methods(VALUE self)
{
    thread_data_t* thread = prof_get_thread(self);
    if (thread->methods == Qnil)
    {
        thread->methods = rb_ary_new();
        rb_st_foreach(thread->method_table, collect_methods, thread->methods);
    }
    return thread->methods;
}
```

    
  

    
      
  
### 
  
    #**total_time**  ⇒ Object 
  

  

  

  
    

Returns the total time this thread was executed.

  

  

  
    
      

```

4
5
6
```

    
    
      

```
# File 'lib/ruby-prof/thread.rb', line 4

def total_time
  self.call_tree.total_time
end
```

    
  

    
      
  
### 
  
    #**wait_time**  ⇒ Object 
  

  

  

  
    

Returns the amount of time this thread waited while other thread executed.

  

  

  
    
      

```

9
10
11
12
13
14
15
16
17
18
```

    
    
      

```
# File 'lib/ruby-prof/thread.rb', line 9

def wait_time
  # wait_time, like self:time, is always method local
  # thus we need to sum over all methods and call infos
  self.methods.inject(0) do |sum, method_info|
    method_info.callers.each do |call_tree|
      sum += call_tree.wait_time
    end
    sum
  end
end
```