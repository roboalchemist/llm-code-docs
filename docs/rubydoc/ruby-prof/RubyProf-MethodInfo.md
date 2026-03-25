# Class: RubyProf::MethodInfo
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- RubyProf::MethodInfo
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Comparable
  
  
  

  

  
  
    Defined in:
    lib/ruby-prof/method_info.rb,

  ext/ruby_prof/rp_method.c,
 ext/ruby_prof/rp_method.c

  
  

## Overview

  
    

The RubyProf::MethodInfo class stores profiling data for a method. One instance of the RubyProf::MethodInfo class is created per method called per thread.  Thus, if a method is called in two different thread then there will be two RubyProf::MethodInfo objects created.  RubyProf::MethodInfo objects can be accessed via the RubyProf::Profile object.

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        MODULE_INCLUDEE =
          
        
        

```
INT2NUM(kModuleIncludee)
```

      
        CLASS_SINGLETON =
          
        
        

```
INT2NUM(kClassSingleton)
```

      
        MODULE_SINGLETON =
          
        
        

```
INT2NUM(kModuleSingleton)
```

      
        OBJECT_SINGLETON =
          
        
        

```
INT2NUM(kObjectSingleton)
```

      
        OTHER_SINGLETON =
          
        
        

```
INT2NUM(kOtherSingleton)
```

      
    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**<=>**(other)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**==**(other)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_dump_data**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      #**_load_data**(data)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      #**allocations**  ⇒ Array 
    

    
  
  
  
  
  
  
  
  

  
    

Returns an array of allocation information.

  

      
        
- 
  
    
      #**call_trees**  ⇒ CallTrees 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the CallTrees associated with this method.

  

      
        
- 
  
    
      #**called**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The number of times this method was called.

  

      
        
- 
  
    
      #**children_time**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The time this method’s children took to execute.

  

      
        
- 
  
    
      #**eql?**(other)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**full_name**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the full name of a class.

  

      
        
- 
  
    
      #**hash**  ⇒ Hash 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the hash key for this method info.

  

      
        
- 
  
    
      #**new**(klass, method_name)  ⇒ Object 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Creates a new MethodInfo instance.

  

      
        
- 
  
    
      #**klass_flags**  ⇒ Integer 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the klass flags.

  

      
        
- 
  
    
      #**klass_name**  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the name of this method’s class.

  

      
        
- 
  
    
      #**line_no**  ⇒ Integer 
    

    
  
  
  
  
  
  
  
  

  
    

returns the line number of the method.

  

      
        
- 
  
    
      #**called**  ⇒ Measurement 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the measurement associated with this method.

  

      
        
- 
  
    
      #**method_name**  ⇒ Symbol 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the name of this method in the format Object#method.

  

      
        
- 
  
    
      #**recursive?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the true if this method is recursively invoked.

  

      
        
- 
  
    
      #**self_time**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The time this method took to execute.

  

      
        
- 
  
    
      #**source_file**  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the source file of the method.

  

      
        
- 
  
    
      #**to_s**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**total_time**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The total time this method took - includes self time + wait time + child time.

  

      
        
- 
  
    
      #**wait_time**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The time this method waited for other fibers/threads to execute.

  

      
    

  

  
  
## Constructor Details

  
    
  
### 
  
    #**new**(klass, method_name)  ⇒ Object 
  

  

  

  
    

Creates a new MethodInfo instance. `Klass` should be a reference to a Ruby class and `method_name` a symbol identifying one of its instance methods.

  

  
  

  
    
      

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
356
357
358
359
360
361
362
```

    
    
      

```
# File 'ext/ruby_prof/rp_method.c', line 341

static VALUE prof_method_initialize(VALUE self, VALUE klass, VALUE method_name)
{
  prof_method_t* method_ptr = prof_get_method(self);
  method_ptr->klass = klass;
  method_ptr->method_name = method_name;

  // Setup method key
  method_ptr->key = method_key(klass, method_name);

  // Get method object
  VALUE ruby_method = rb_funcall(klass, rb_intern("instance_method"), 1, method_name);

  // Get source file and line number
  VALUE location_array = rb_funcall(ruby_method, rb_intern("source_location"), 0);
  if (location_array != Qnil && RARRAY_LEN(location_array) == 2)
  {
    method_ptr->source_file = rb_ary_entry(location_array, 0);
    method_ptr->source_line = NUM2INT(rb_ary_entry(location_array, 1));
  }

  return self;
}
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**<=>**(other)  ⇒ Object 
  

  

  

  
    
      

```

63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
```

    
    
      

```
# File 'lib/ruby-prof/method_info.rb', line 63

def <=>(other)
  sort_delta = 0.0001

  if other.nil?
    -1
  elsif self.full_name == other.full_name
    0
  elsif self.total_time < other.total_time && (self.total_time - other.total_time).abs > sort_delta
    -1
  elsif self.total_time > other.total_time && (self.total_time - other.total_time).abs > sort_delta
    1
  elsif self.call_trees.min_depth < other.call_trees.min_depth
    1
  elsif self.call_trees.min_depth > other.call_trees.min_depth
    -1
  else
    self.full_name <=> other.full_name
  end
end
```

    
  

    
      
  
### 
  
    #**==**(other)  ⇒ Object 
  

  

  

  
    
      

```

59
60
61
```

    
    
      

```
# File 'lib/ruby-prof/method_info.rb', line 59

def ==(other)
  self.eql?(other)
end
```

    
  

    
      
  
### 
  
    #**_dump_data**  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

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
491
492
493
494
```

    
    
      

```
# File 'ext/ruby_prof/rp_method.c', line 475

static VALUE prof_method_dump(VALUE self)
{
    prof_method_t* method_data = prof_get_method(self);
    VALUE result = rb_hash_new();

    rb_hash_aset(result, ID2SYM(rb_intern("klass_name")), prof_method_klass_name(self));
    rb_hash_aset(result, ID2SYM(rb_intern("klass_flags")), INT2FIX(method_data->klass_flags));
    rb_hash_aset(result, ID2SYM(rb_intern("method_name")), method_data->method_name);

    rb_hash_aset(result, ID2SYM(rb_intern("key")), ULL2NUM(method_data->key));
    rb_hash_aset(result, ID2SYM(rb_intern("recursive")), prof_method_recursive(self));
    rb_hash_aset(result, ID2SYM(rb_intern("source_file")), method_data->source_file);
    rb_hash_aset(result, ID2SYM(rb_intern("source_line")), INT2FIX(method_data->source_line));

    rb_hash_aset(result, ID2SYM(rb_intern("call_trees")), prof_call_trees_wrap(method_data->call_trees));
    rb_hash_aset(result, ID2SYM(rb_intern("measurement")), prof_measurement_wrap(method_data->measurement));
    rb_hash_aset(result, ID2SYM(rb_intern("allocations")), prof_method_allocations(self));

    return result;
}
```

    
  

    
      
  
### 
  
    #**_load_data**(data)  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

497
498
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
510
511
512
513
514
515
516
517
518
519
520
521
```

    
    
      

```
# File 'ext/ruby_prof/rp_method.c', line 497

static VALUE prof_method_load(VALUE self, VALUE data)
{
    prof_method_t* method_data = prof_get_method(self);
    method_data->object = self;

    method_data->klass_name = rb_hash_aref(data, ID2SYM(rb_intern("klass_name")));
    method_data->klass_flags = FIX2INT(rb_hash_aref(data, ID2SYM(rb_intern("klass_flags"))));
    method_data->method_name = rb_hash_aref(data, ID2SYM(rb_intern("method_name")));
    method_data->key = RB_NUM2ULL(rb_hash_aref(data, ID2SYM(rb_intern("key"))));

    method_data->recursive = rb_hash_aref(data, ID2SYM(rb_intern("recursive"))) == Qtrue ? true : false;

    method_data->source_file = rb_hash_aref(data, ID2SYM(rb_intern("source_file")));
    method_data->source_line = FIX2INT(rb_hash_aref(data, ID2SYM(rb_intern("source_line"))));

    VALUE call_trees = rb_hash_aref(data, ID2SYM(rb_intern("call_trees")));
    method_data->call_trees = prof_get_call_trees(call_trees);

    VALUE measurement = rb_hash_aref(data, ID2SYM(rb_intern("measurement")));
    method_data->measurement = prof_get_measurement(measurement);

    VALUE allocations = rb_hash_aref(data, ID2SYM(rb_intern("allocations")));
    prof_allocations_unwrap(method_data->allocations_table, allocations);
    return data;
}
```

    
  

    
      
  
### 
  
    #**allocations**  ⇒ Array 
  

  

  

  
    

Returns an array of allocation information.

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (Array)
      
      
      
    
  

  
    
      

```

379
380
381
382
383
```

    
    
      

```
# File 'ext/ruby_prof/rp_method.c', line 379

static VALUE prof_method_allocations(VALUE self)
{
    prof_method_t* method = prof_get_method(self);
    return prof_allocations_wrap(method->allocations_table);
}
```

    
  

    
      
  
### 
  
    #**call_trees**  ⇒ CallTrees 
  

  

  

  
    

Returns the CallTrees associated with this method.

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (CallTrees)
      
      
      
    
  

  
    
      

```

468
469
470
471
472
```

    
    
      

```
# File 'ext/ruby_prof/rp_method.c', line 468

static VALUE prof_method_call_trees(VALUE self)
{
    prof_method_t* method = prof_get_method(self);
    return prof_call_trees_wrap(method->call_trees);
}
```

    
  

    
      
  
### 
  
    #**called**  ⇒ Object 
  

  

  

  
    

The number of times this method was called

  

  

  
    
      

```

31
32
33
```

    
    
      

```
# File 'lib/ruby-prof/method_info.rb', line 31

def called
  self.measurement.called
end
```

    
  

    
      
  
### 
  
    #**children_time**  ⇒ Object 
  

  

  

  
    

The time this method’s children took to execute

  

  

  
    
      

```

51
52
53
```

    
    
      

```
# File 'lib/ruby-prof/method_info.rb', line 51

def children_time
  self.total_time - self.self_time - self.wait_time
end
```

    
  

    
      
  
### 
  
    #**eql?**(other)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

55
56
57
```

    
    
      

```
# File 'lib/ruby-prof/method_info.rb', line 55

def eql?(other)
  self.hash == other.hash
end
```

    
  

    
      
  
### 
  
    #**full_name**  ⇒ Object 
  

  

  

  
    

Returns the full name of a class. The interpretation of method names is:

- 

MyObject#test - An method defined in a class

- 

<Class:MyObject>#test - A method defined in a singleton class.

- 

<Module:MyObject>#test - A method defined in a singleton module.

- 

<Object:MyObject>#test - A method defined in a singleton object.

  

  

  
    
      

```

15
16
17
18
19
20
21
22
23
24
25
26
27
28
```

    
    
      

```
# File 'lib/ruby-prof/method_info.rb', line 15

def full_name
  decorated_class_name = case self.klass_flags
                         when 0x2
                           "<Class::#{klass_name}>"
                         when 0x4
                           "<Module::#{klass_name}>"
                         when 0x8
                           "<Object::#{klass_name}>"
                         else
                           klass_name
                         end

  "#{decorated_class_name}##{method_name}"
end
```

    
  

    
      
  
### 
  
    #**hash**  ⇒ Hash 
  

  

  

  
    

Returns the hash key for this method info. The hash key is calculated based on the klass name and method name

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (Hash)
      
      
      
    
  

  
    
      

```

369
370
371
372
373
```

    
    
      

```
# File 'ext/ruby_prof/rp_method.c', line 369

static VALUE prof_method_hash(VALUE self)
{
  prof_method_t* method_ptr = prof_get_method(self);
  return ULL2NUM(method_ptr->key);
}
```

    
  

    
      
  
### 
  
    #**klass_flags**  ⇒ Integer 
  

  

  

  
    

Returns the klass flags

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (Integer)
      
      
      
    
  

  
    
      

```

436
437
438
439
440
```

    
    
      

```
# File 'ext/ruby_prof/rp_method.c', line 436

static VALUE prof_method_klass_flags(VALUE self)
{
    prof_method_t* method = prof_get_method(self);
    return INT2FIX(method->klass_flags);
}
```

    
  

    
      
  
### 
  
    #**klass_name**  ⇒ String 
  

  

  

  
    

Returns the name of this method’s class.  Singleton classes will have the form <Object::Object>.

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
    
  

  
    
      

```

422
423
424
425
426
427
428
429
```

    
    
      

```
# File 'ext/ruby_prof/rp_method.c', line 422

static VALUE prof_method_klass_name(VALUE self)
{
    prof_method_t* method = prof_get_method(self);
    if (method->klass_name == Qnil)
        method->klass_name = resolve_klass_name(method->klass, &method->klass_flags);

    return method->klass_name;
}
```

    
  

    
      
  
### 
  
    #**line_no**  ⇒ Integer 
  

  

  

  
    

returns the line number of the method

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (Integer)
      
      
      
    
  

  
    
      

```

410
411
412
413
414
```

    
    
      

```
# File 'ext/ruby_prof/rp_method.c', line 410

static VALUE prof_method_line(VALUE self)
{
    prof_method_t* method = prof_get_method(self);
    return INT2FIX(method->source_line);
}
```

    
  

    
      
  
### 
  
    #**called**  ⇒ Measurement 
  

  

  

  
    

Returns the measurement associated with this method.

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (Measurement)
      
      
      
    
  

  
    
      

```

389
390
391
392
393
```

    
    
      

```
# File 'ext/ruby_prof/rp_method.c', line 389

static VALUE prof_method_measurement(VALUE self)
{
    prof_method_t* method = prof_get_method(self);
    return prof_measurement_wrap(method->measurement);
}
```

    
  

    
      
  
### 
  
    #**method_name**  ⇒ Symbol 
  

  

  

  
    

Returns the name of this method in the format Object#method. Singletons methods will be returned in the format <Object::Object>#method.

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (Symbol)
      
      
      
    
  

  
    
      

```

448
449
450
451
452
```

    
    
      

```
# File 'ext/ruby_prof/rp_method.c', line 448

static VALUE prof_method_name(VALUE self)
{
    prof_method_t* method = prof_get_method(self);
    return method->method_name;
}
```

    
  

    
      
  
### 
  
    #**recursive?**  ⇒ Boolean 
  

  

  

  
    

Returns the true if this method is recursively invoked

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

458
459
460
461
462
```

    
    
      

```
# File 'ext/ruby_prof/rp_method.c', line 458

static VALUE prof_method_recursive(VALUE self)
{
    prof_method_t* method = prof_get_method(self);
    return method->recursive ? Qtrue : Qfalse;
}
```

    
  

    
      
  
### 
  
    #**self_time**  ⇒ Object 
  

  

  

  
    

The time this method took to execute

  

  

  
    
      

```

41
42
43
```

    
    
      

```
# File 'lib/ruby-prof/method_info.rb', line 41

def self_time
  self.measurement.self_time
end
```

    
  

    
      
  
### 
  
    #**source_file**  ⇒ String 
  

  

  

  
    

Returns the source file of the method

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
    
  

  
    
      

```

400
401
402
403
404
```

    
    
      

```
# File 'ext/ruby_prof/rp_method.c', line 400

static VALUE prof_method_source_file(VALUE self)
{
    prof_method_t* method = prof_get_method(self);
    return method->source_file;
}
```

    
  

    
      
  
### 
  
    #**to_s**  ⇒ Object 
  

  

  

  
    
      

```

83
84
85
```

    
    
      

```
# File 'lib/ruby-prof/method_info.rb', line 83

def to_s
  "#{self.full_name} (c: #{self.called}, tt: #{self.total_time}, st: #{self.self_time}, wt: #{wait_time}, ct: #{self.children_time})"
end
```

    
  

    
      
  
### 
  
    #**total_time**  ⇒ Object 
  

  

  

  
    

The total time this method took - includes self time + wait time + child time

  

  

  
    
      

```

36
37
38
```

    
    
      

```
# File 'lib/ruby-prof/method_info.rb', line 36

def total_time
  self.measurement.total_time
end
```

    
  

    
      
  
### 
  
    #**wait_time**  ⇒ Object 
  

  

  

  
    

The time this method waited for other fibers/threads to execute

  

  

  
    
      

```

46
47
48
```

    
    
      

```
# File 'lib/ruby-prof/method_info.rb', line 46

def wait_time
  self.measurement.wait_time
end
```