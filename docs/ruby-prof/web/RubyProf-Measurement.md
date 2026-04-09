# Class: RubyProf::Measurement
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- RubyProf::Measurement
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/ruby-prof/measurement.rb,

  ext/ruby_prof/rp_measurement.c

  
  

## Overview

  
    

The Measurement class is a helper class used by RubyProf::MethodInfo to store information about the method. You cannot create a CallTree object directly, they are generated while running a profile.

  

  

  
    
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
  
    
      #**called**  ⇒ Integer 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the total amount of times this method was called.

  

      
        
- 
  
    
      #**called=**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Sets the call count to value.

  

      
        
- 
  
    
      #**children_time**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**new**(total_time, self_time, wait_time, called)  ⇒ Measurement 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Creates a new measuremen instance.

  

      
        
- 
  
    
      #**initialize_copy**(other)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**inspect**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**merge**(other)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Adds the content of other measurement to this measurement.

  

      
        
- 
  
    
      #**self_time**  ⇒ Float 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the total amount of time spent in this method.

  

      
        
- 
  
    
      #**self_time=**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Sets the call count to value.

  

      
        
- 
  
    
      #**to_s**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**total_time**  ⇒ Float 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the total amount of time spent in this method and its children.

  

      
        
- 
  
    
      #**total_time=**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Sets the call count to n.

  

      
        
- 
  
    
      #**wait_time**  ⇒ Float 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the total amount of time this method waited for other threads.

  

      
        
- 
  
    
      #**wait_time=**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Sets the wait time to value.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**new**(total_time, self_time, wait_time, called)  ⇒ Measurement 
  

  

  

  
    

Creates a new measuremen instance.

  

  
  
  
    

  

  

  
    
      

```

55
56
57
58
59
60
61
62
63
64
65
```

    
    
      

```
# File 'ext/ruby_prof/rp_measurement.c', line 55

static VALUE prof_measurement_initialize(VALUE self, VALUE total_time, VALUE self_time, VALUE wait_time, VALUE called)
{
  prof_measurement_t* result = prof_get_measurement(self);

  result->total_time = NUM2DBL(total_time);
  result->self_time = NUM2DBL(self_time);
  result->wait_time = NUM2DBL(wait_time);
  result->called = NUM2INT(called);
  result->object = self;
  return self;
}
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**_dump_data**  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

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
```

    
    
      

```
# File 'ext/ruby_prof/rp_measurement.c', line 305

static VALUE prof_measurement_dump(VALUE self)
{
    prof_measurement_t* measurement_data = prof_get_measurement(self);
    VALUE result = rb_hash_new();

    rb_hash_aset(result, ID2SYM(rb_intern("owner")), INT2FIX(measurement_data->owner));
    rb_hash_aset(result, ID2SYM(rb_intern("total_time")), rb_float_new(measurement_data->total_time));
    rb_hash_aset(result, ID2SYM(rb_intern("self_time")), rb_float_new(measurement_data->self_time));
    rb_hash_aset(result, ID2SYM(rb_intern("wait_time")), rb_float_new(measurement_data->wait_time));
    rb_hash_aset(result, ID2SYM(rb_intern("called")), INT2FIX(measurement_data->called));

    return result;
}
```

    
  

    
      
  
### 
  
    #**_load_data**(data)  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

320
321
322
323
324
325
326
327
328
329
330
331
332
333
```

    
    
      

```
# File 'ext/ruby_prof/rp_measurement.c', line 320

static VALUE
prof_measurement_load(VALUE self, VALUE data)
{
    prof_measurement_t* measurement = prof_get_measurement(self);
    measurement->object = self;

    measurement->owner = FIX2INT(rb_hash_aref(data, ID2SYM(rb_intern("owner"))));
    measurement->total_time = rb_num2dbl(rb_hash_aref(data, ID2SYM(rb_intern("total_time"))));
    measurement->self_time = rb_num2dbl(rb_hash_aref(data, ID2SYM(rb_intern("self_time"))));
    measurement->wait_time = rb_num2dbl(rb_hash_aref(data, ID2SYM(rb_intern("wait_time"))));
    measurement->called = FIX2INT(rb_hash_aref(data, ID2SYM(rb_intern("called"))));

    return data;
}
```

    
  

    
      
  
### 
  
    #**called**  ⇒ Integer 
  

  

  

  
    

Returns the total amount of times this method was called.

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (Integer)
      
      
      
    
  

  
    
      

```

266
267
268
269
270
```

    
    
      

```
# File 'ext/ruby_prof/rp_measurement.c', line 266

static VALUE prof_measurement_called(VALUE self)
{
    prof_measurement_t* result = prof_get_measurement(self);
    return INT2NUM(result->called);
}
```

    
  

    
      
  
### 
  
    #**called=**  ⇒ Object 
  

  

  

  
    

Sets the call count to value.

  

  
  

  
    
      

```

276
277
278
279
280
281
```

    
    
      

```
# File 'ext/ruby_prof/rp_measurement.c', line 276

static VALUE prof_measurement_set_called(VALUE self, VALUE value)
{
  prof_measurement_t* result = prof_get_measurement(self);
  result->called = NUM2INT(value);
  return value;
}
```

    
  

    
      
  
### 
  
    #**children_time**  ⇒ Object 
  

  

  

  
    
      

```

5
6
7
```

    
    
      

```
# File 'lib/ruby-prof/measurement.rb', line 5

def children_time
  self.total_time - self.self_time - self.wait_time
end
```

    
  

    
      
  
### 
  
    #**initialize_copy**(other)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'ext/ruby_prof/rp_measurement.c', line 78

static VALUE prof_measurement_initialize_copy(VALUE self, VALUE other)
{
  // This object was created by Ruby either via Measurment#clone or Measurement#dup 
  // and thus prof_measurement_allocate was called so the object is owned by Ruby

  if (self == other)
    return self;

  prof_measurement_t* self_ptr = prof_get_measurement(self);
  prof_measurement_t* other_ptr = prof_get_measurement(other);

  self_ptr->called = other_ptr->called;
  self_ptr->total_time = other_ptr->total_time;
  self_ptr->self_time = other_ptr->self_time;
  self_ptr->wait_time = other_ptr->wait_time;

  return self;
}
```

    
  

    
      
  
### 
  
    #**inspect**  ⇒ Object 
  

  

  

  
    
      

```

13
14
15
```

    
    
      

```
# File 'lib/ruby-prof/measurement.rb', line 13

def inspect
  super + "(#{self.to_s})"
end
```

    
  

    
      
  
### 
  
    #**merge**(other)  ⇒ Object 
  

  

  

  
    

Adds the content of other measurement to this measurement

  

  
  

  
    
      

```

296
297
298
299
300
301
302
```

    
    
      

```
# File 'ext/ruby_prof/rp_measurement.c', line 296

VALUE prof_measurement_merge(VALUE self, VALUE other)
{
  prof_measurement_t* self_ptr = prof_get_measurement(self);
  prof_measurement_t* other_ptr = prof_get_measurement(other);
  prof_measurement_merge_internal(self_ptr, other_ptr);
  return self;
}
```

    
  

    
      
  
### 
  
    #**self_time**  ⇒ Float 
  

  

  

  
    

Returns the total amount of time spent in this method.

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (Float)
      
      
      
    
  

  
    
      

```

221
222
223
224
225
226
227
```

    
    
      

```
# File 'ext/ruby_prof/rp_measurement.c', line 221

static VALUE
prof_measurement_self_time(VALUE self)
{
    prof_measurement_t* result = prof_get_measurement(self);

    return rb_float_new(result->self_time);
}
```

    
  

    
      
  
### 
  
    #**self_time=**  ⇒ Object 
  

  

  

  
    

Sets the call count to value.

  

  
  

  
    
      

```

233
234
235
236
237
238
```

    
    
      

```
# File 'ext/ruby_prof/rp_measurement.c', line 233

static VALUE prof_measurement_set_self_time(VALUE self, VALUE value)
{
  prof_measurement_t* result = prof_get_measurement(self);
  result->self_time = NUM2DBL(value);
  return value;
}
```

    
  

    
      
  
### 
  
    #**to_s**  ⇒ Object 
  

  

  

  
    
      

```

9
10
11
```

    
    
      

```
# File 'lib/ruby-prof/measurement.rb', line 9

def to_s
  "c: #{called}, tt: #{total_time}, st: #{self_time}"
end
```

    
  

    
      
  
### 
  
    #**total_time**  ⇒ Float 
  

  

  

  
    

Returns the total amount of time spent in this method and its children.

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (Float)
      
      
      
    
  

  
    
      

```

200
201
202
203
204
```

    
    
      

```
# File 'ext/ruby_prof/rp_measurement.c', line 200

static VALUE prof_measurement_total_time(VALUE self)
{
    prof_measurement_t* result = prof_get_measurement(self);
    return rb_float_new(result->total_time);
}
```

    
  

    
      
  
### 
  
    #**total_time=**  ⇒ Object 
  

  

  

  
    

Sets the call count to n.

  

  
  

  
    
      

```

210
211
212
213
214
215
```

    
    
      

```
# File 'ext/ruby_prof/rp_measurement.c', line 210

static VALUE prof_measurement_set_total_time(VALUE self, VALUE value)
{
  prof_measurement_t* result = prof_get_measurement(self);
  result->total_time = NUM2DBL(value);
  return value;
}
```

    
  

    
      
  
### 
  
    #**wait_time**  ⇒ Float 
  

  

  

  
    

Returns the total amount of time this method waited for other threads.

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (Float)
      
      
      
    
  

  
    
      

```

244
245
246
247
248
249
```

    
    
      

```
# File 'ext/ruby_prof/rp_measurement.c', line 244

static VALUE prof_measurement_wait_time(VALUE self)
{
    prof_measurement_t* result = prof_get_measurement(self);

    return rb_float_new(result->wait_time);
}
```

    
  

    
      
  
### 
  
    #**wait_time=**  ⇒ Object 
  

  

  

  
    

Sets the wait time to value.

  

  
  

  
    
      

```

255
256
257
258
259
260
```

    
    
      

```
# File 'ext/ruby_prof/rp_measurement.c', line 255

static VALUE prof_measurement_set_wait_time(VALUE self, VALUE value)
{
  prof_measurement_t* result = prof_get_measurement(self);
  result->wait_time = NUM2DBL(value);
  return value;
}
```