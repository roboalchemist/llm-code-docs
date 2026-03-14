# Class: RubyProf::CallTree
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- RubyProf::CallTree
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/ruby-prof/call_tree.rb,

  ext/ruby_prof/rp_call_tree.c

  
  

## Overview

  
    

The CallTree class is used to track the relationships between methods. It is a helper class used by RubyProf::MethodInfo to keep track of which methods called a given method and which methods a given method called. Each CallTree has a parent and target method. You cannot create a CallTree object directly, they are generated while running a profile.

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**<=>**(other)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Compares two CallTree instances.

  

      
        
- 
  
    
      #**_dump_data**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      #**_load_data**(data)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      #**add_child**(call_tree)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Adds the specified call_tree as a child.

  

      
        
- 
  
    
      #**called**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The number of times the parent method called the target method.

  

      
        
- 
  
    
      #**callees**  ⇒ Array 
    

    
  
  
  
  
  
  
  
  

  
    

Returns an array of call info objects that this method called (ie, children).

  

      
        
- 
  
    
      #**children_time**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The time spent in child methods resulting from the parent method calling the target method.

  

      
        
- 
  
    
      #**depth**  ⇒ Integer 
    

    
  
  
  
  
  
  
  
  

  
    

returns the depth of this call info in the call graph.

  

      
        
- 
  
    
      #**new**(method_info)  ⇒ Object 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Creates a new CallTree instance.

  

      
        
- 
  
    
      #**inspect**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**line_no**  ⇒ Integer 
    

    
  
  
  
  
  
  
  
  

  
    

returns the line number of the method.

  

      
        
- 
  
    
      #**called**  ⇒ Measurement 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the measurement associated with this call_tree.

  

      
        
- 
  
    
      #**parent**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the CallTree parent call_tree object (the method that called this method).

  

      
        
- 
  
    
      #**self_time**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The self time (of the parent) resulting from the parent method calling the target method.

  

      
        
- 
  
    
      #**source_file**  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

return the source file of the method.

  

      
        
- 
  
    
      #**called**  ⇒ MethodInfo 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the target method.

  

      
        
- 
  
    
      #**to_s**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      #**total_time**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The total time resulting from the parent method calling the target method.

  

      
        
- 
  
    
      #**wait_time**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The wait time (of the parent) resulting from the parent method calling the target method.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**new**(method_info)  ⇒ Object 
  

  

  

  
    

Creates a new CallTree instance. `Klass` should be a reference to a Ruby class and `method_name` a symbol identifying one of its instance methods.

  

  
  

  
    
      

```

253
254
255
256
257
258
259
```

    
    
      

```
# File 'ext/ruby_prof/rp_call_tree.c', line 253

static VALUE prof_call_tree_initialize(VALUE self, VALUE method_info)
{
  prof_call_tree_t* call_tree_ptr = prof_get_call_tree(self);
  call_tree_ptr->method = prof_get_method(method_info);

  return self;
}
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**<=>**(other)  ⇒ Object 
  

  

  

  
    

Compares two CallTree instances. The comparison is based on the CallTree#parent, CallTree#target, and total time.

  

  

  
    
      

```

36
37
38
39
40
41
42
43
44
45
46
```

    
    
      

```
# File 'lib/ruby-prof/call_tree.rb', line 36

def <=>(other)
  if self.target == other.target && self.parent == other.parent
    0
  elsif self.total_time < other.total_time
    -1
  elsif self.total_time > other.total_time
    1
  else
    self.target.full_name <=> other.target.full_name
  end
end
```

    
  

    
      
  
### 
  
    #**_dump_data**  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

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
444
445
446
447
448
```

    
    
      

```
# File 'ext/ruby_prof/rp_call_tree.c', line 431

static VALUE prof_call_tree_dump(VALUE self)
{
    prof_call_tree_t* call_tree_data = prof_get_call_tree(self);
    VALUE result = rb_hash_new();

    rb_hash_aset(result, ID2SYM(rb_intern("owner")), INT2FIX(call_tree_data->owner));

    rb_hash_aset(result, ID2SYM(rb_intern("measurement")), prof_measurement_wrap(call_tree_data->measurement));

    rb_hash_aset(result, ID2SYM(rb_intern("source_file")), call_tree_data->source_file);
    rb_hash_aset(result, ID2SYM(rb_intern("source_line")), INT2FIX(call_tree_data->source_line));

    rb_hash_aset(result, ID2SYM(rb_intern("parent")), prof_call_tree_parent(self));
    rb_hash_aset(result, ID2SYM(rb_intern("children")), prof_call_tree_children(self));
    rb_hash_aset(result, ID2SYM(rb_intern("target")), prof_call_tree_target(self));

    return result;
}
```

    
  

    
      
  
### 
  
    #**_load_data**(data)  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

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
473
474
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
```

    
    
      

```
# File 'ext/ruby_prof/rp_call_tree.c', line 451

static VALUE prof_call_tree_load(VALUE self, VALUE data)
{
    VALUE target = Qnil;
    VALUE parent = Qnil;
    prof_call_tree_t* call_tree = prof_get_call_tree(self);
    call_tree->object = self;

    call_tree->owner = FIX2INT(rb_hash_aref(data, ID2SYM(rb_intern("owner"))));

    VALUE measurement = rb_hash_aref(data, ID2SYM(rb_intern("measurement")));
    call_tree->measurement = prof_get_measurement(measurement);

    call_tree->source_file = rb_hash_aref(data, ID2SYM(rb_intern("source_file")));
    call_tree->source_line = FIX2INT(rb_hash_aref(data, ID2SYM(rb_intern("source_line"))));

    parent = rb_hash_aref(data, ID2SYM(rb_intern("parent")));
    if (parent != Qnil)
        call_tree->parent = prof_get_call_tree(parent);

    VALUE callees = rb_hash_aref(data, ID2SYM(rb_intern("children")));
    for (int i = 0; i < rb_array_len(callees); i++)
    {
        VALUE call_tree_object = rb_ary_entry(callees, i);
        prof_call_tree_t* call_tree_data = prof_get_call_tree(call_tree_object);

        st_data_t key = call_tree_data->method ? call_tree_data->method->key : method_key(Qnil, 0);
        call_tree_table_insert(call_tree->children, key, call_tree_data);
    }

    target = rb_hash_aref(data, ID2SYM(rb_intern("target")));
    call_tree->method = prof_get_method(target);

    return data;
}
```

    
  

    
      
  
### 
  
    #**add_child**(call_tree)  ⇒ Object 
  

  

  

  
    

Adds the specified call_tree as a child. If the method represented by the call tree is already a child than a IndexError is thrown.

The returned value is the added child

  

  
  

  
    
      

```

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
```

    
    
      

```
# File 'ext/ruby_prof/rp_call_tree.c', line 293

static VALUE prof_call_tree_add_child_ruby(VALUE self, VALUE child)
{
  prof_call_tree_t* parent_ptr = prof_get_call_tree(self);
  prof_call_tree_t* child_ptr = prof_get_call_tree(child);

  prof_call_tree_t* existing_ptr = call_tree_table_lookup(parent_ptr->children, child_ptr->method->key);
  if (existing_ptr)
  {
    rb_raise(rb_eIndexError, "Child call tree already exists");
  }

  prof_call_tree_add_parent(child_ptr, parent_ptr);

  return child;
}
```

    
  

    
      
  
### 
  
    #**called**  ⇒ Object 
  

  

  

  
    

The number of times the parent method called the target method

  

  

  
    
      

```

10
11
12
```

    
    
      

```
# File 'lib/ruby-prof/call_tree.rb', line 10

def called
  self.measurement.called
end
```

    
  

    
      
  
### 
  
    #**callees**  ⇒ Array 
  

  

  

  
    

Returns an array of call info objects that this method called (ie, children).

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (Array)
      
      
      
    
  

  
    
      

```

278
279
280
281
282
283
284
```

    
    
      

```
# File 'ext/ruby_prof/rp_call_tree.c', line 278

static VALUE prof_call_tree_children(VALUE self)
{
    prof_call_tree_t* call_tree = prof_get_call_tree(self);
    VALUE result = rb_ary_new();
    rb_st_foreach(call_tree->children, prof_call_tree_collect_children, result);
    return result;
}
```

    
  

    
      
  
### 
  
    #**children_time**  ⇒ Object 
  

  

  

  
    

The time spent in child methods resulting from the parent method calling the target method

  

  

  
    
      

```

30
31
32
```

    
    
      

```
# File 'lib/ruby-prof/call_tree.rb', line 30

def children_time
  self.total_time - self.self_time - self.wait_time
end
```

    
  

    
      
  
### 
  
    #**depth**  ⇒ Integer 
  

  

  

  
    

returns the depth of this call info in the call graph

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (Integer)
      
      
      
    
  

  
    
      

```

333
334
335
336
337
338
```

    
    
      

```
# File 'ext/ruby_prof/rp_call_tree.c', line 333

static VALUE prof_call_tree_depth(VALUE self)
{
    prof_call_tree_t* call_tree_data = prof_get_call_tree(self);
    uint32_t depth = prof_call_tree_figure_depth(call_tree_data);
    return rb_int_new(depth);
}
```

    
  

    
      
  
### 
  
    #**inspect**  ⇒ Object 
  

  

  

  
    
      

```

53
54
55
```

    
    
      

```
# File 'lib/ruby-prof/call_tree.rb', line 53

def inspect
  self.to_s
end
```

    
  

    
      
  
### 
  
    #**line_no**  ⇒ Integer 
  

  

  

  
    

returns the line number of the method

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (Integer)
      
      
      
    
  

  
    
      

```

355
356
357
358
359
```

    
    
      

```
# File 'ext/ruby_prof/rp_call_tree.c', line 355

static VALUE prof_call_tree_line(VALUE self)
{
    prof_call_tree_t* result = prof_get_call_tree(self);
    return INT2FIX(result->source_line);
}
```

    
  

    
      
  
### 
  
    #**called**  ⇒ Measurement 
  

  

  

  
    

Returns the measurement associated with this call_tree.

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (Measurement)
      
      
      
    
  

  
    
      

```

323
324
325
326
327
```

    
    
      

```
# File 'ext/ruby_prof/rp_call_tree.c', line 323

static VALUE prof_call_tree_measurement(VALUE self)
{
    prof_call_tree_t* call_tree = prof_get_call_tree(self);
    return prof_measurement_wrap(call_tree->measurement);
}
```

    
  

    
      
  
### 
  
    #**parent**  ⇒ Object 
  

  

  

  
    

Returns the CallTree parent call_tree object (the method that called this method).

  

  
  

  
    
      

```

265
266
267
268
269
270
271
272
```

    
    
      

```
# File 'ext/ruby_prof/rp_call_tree.c', line 265

static VALUE prof_call_tree_parent(VALUE self)
{
    prof_call_tree_t* call_tree = prof_get_call_tree(self);
    if (call_tree->parent)
        return prof_call_tree_wrap(call_tree->parent);
    else
        return Qnil;
}
```

    
  

    
      
  
### 
  
    #**self_time**  ⇒ Object 
  

  

  

  
    

The self time (of the parent) resulting from the parent method calling the target method

  

  

  
    
      

```

20
21
22
```

    
    
      

```
# File 'lib/ruby-prof/call_tree.rb', line 20

def self_time
  self.measurement.self_time
end
```

    
  

    
      
  
### 
  
    #**source_file**  ⇒ String 
  

  

  

  
    

return the source file of the method

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
    
  

  
    
      

```

345
346
347
348
349
```

    
    
      

```
# File 'ext/ruby_prof/rp_call_tree.c', line 345

static VALUE prof_call_tree_source_file(VALUE self)
{
    prof_call_tree_t* result = prof_get_call_tree(self);
    return result->source_file;
}
```

    
  

    
      
  
### 
  
    #**called**  ⇒ MethodInfo 
  

  

  

  
    

Returns the target method.

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (MethodInfo)
      
      
      
    
  

  
    
      

```

313
314
315
316
317
```

    
    
      

```
# File 'ext/ruby_prof/rp_call_tree.c', line 313

static VALUE prof_call_tree_target(VALUE self)
{
    prof_call_tree_t* call_tree = prof_get_call_tree(self);
    return prof_method_wrap(call_tree->method);
}
```

    
  

    
      
  
### 
  
    #**to_s**  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

49
50
51
```

    
    
      

```
# File 'lib/ruby-prof/call_tree.rb', line 49

def to_s
  "<#{self.class.name} - #{self.target.full_name}>"
end
```

    
  

    
      
  
### 
  
    #**total_time**  ⇒ Object 
  

  

  

  
    

The total time resulting from the parent method calling the target method

  

  

  
    
      

```

15
16
17
```

    
    
      

```
# File 'lib/ruby-prof/call_tree.rb', line 15

def total_time
  self.measurement.total_time
end
```

    
  

    
      
  
### 
  
    #**wait_time**  ⇒ Object 
  

  

  

  
    

The wait time (of the parent) resulting from the parent method calling the target method

  

  

  
    
      

```

25
26
27
```

    
    
      

```
# File 'lib/ruby-prof/call_tree.rb', line 25

def wait_time
  self.measurement.wait_time
end
```