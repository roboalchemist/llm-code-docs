# Class: RubyProf::Allocation
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- RubyProf::Allocation
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    ext/ruby_prof/rp_allocation.c
  
  

  
    
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
  
    
      #**count**  ⇒ Numeric 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the number of times this class has been allocated.

  

      
        
- 
  
    
      #**klass_flags**  ⇒ Integer 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the klass flags.

  

      
        
- 
  
    
      #**klass**  ⇒ Class 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the type of Class being allocated.

  

      
        
- 
  
    
      #**line**  ⇒ Numeric 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the the line number where objects were allocated.

  

      
        
- 
  
    
      #**source_file**  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the the line number where objects were allocated.

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**_dump_data**  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

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
295
296
```

    
    
      

```
# File 'ext/ruby_prof/rp_allocation.c', line 282

static VALUE prof_allocation_dump(VALUE self)
{
    prof_allocation_t* allocation = prof_allocation_get(self);

    VALUE result = rb_hash_new();

    rb_hash_aset(result, ID2SYM(rb_intern("key")), ULL2NUM(allocation->key));
    rb_hash_aset(result, ID2SYM(rb_intern("klass_name")), prof_allocation_klass_name(self));
    rb_hash_aset(result, ID2SYM(rb_intern("klass_flags")), INT2FIX(allocation->klass_flags));
    rb_hash_aset(result, ID2SYM(rb_intern("source_file")), allocation->source_file);
    rb_hash_aset(result, ID2SYM(rb_intern("source_line")), INT2FIX(allocation->source_line));
    rb_hash_aset(result, ID2SYM(rb_intern("count")), INT2FIX(allocation->count));

    return result;
}
```

    
  

    
      
  
### 
  
    #**_load_data**(data)  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

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
311
312
```

    
    
      

```
# File 'ext/ruby_prof/rp_allocation.c', line 299

static VALUE prof_allocation_load(VALUE self, VALUE data)
{
    prof_allocation_t* allocation = prof_allocation_get(self);
    allocation->object = self;

    allocation->key = RB_NUM2ULL(rb_hash_aref(data, ID2SYM(rb_intern("key"))));
    allocation->klass_name = rb_hash_aref(data, ID2SYM(rb_intern("klass_name")));
    allocation->klass_flags = FIX2INT(rb_hash_aref(data, ID2SYM(rb_intern("klass_flags"))));
    allocation->source_file = rb_hash_aref(data, ID2SYM(rb_intern("source_file")));
    allocation->source_line = FIX2INT(rb_hash_aref(data, ID2SYM(rb_intern("source_line"))));
    allocation->count = FIX2INT(rb_hash_aref(data, ID2SYM(rb_intern("count"))));

    return data;
}
```

    
  

    
      
  
### 
  
    #**count**  ⇒ Numeric 
  

  

  

  
    

Returns the number of times this class has been allocated.

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (Numeric)
      
      
      
    
  

  
    
      

```

275
276
277
278
279
```

    
    
      

```
# File 'ext/ruby_prof/rp_allocation.c', line 275

static VALUE prof_allocation_count(VALUE self)
{
    prof_allocation_t* allocation = prof_allocation_get(self);
    return INT2FIX(allocation->count);
}
```

    
  

    
      
  
### 
  
    #**klass_flags**  ⇒ Integer 
  

  

  

  
    

Returns the klass flags

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (Integer)
      
      
      
    
  

  
    
      

```

245
246
247
248
249
```

    
    
      

```
# File 'ext/ruby_prof/rp_allocation.c', line 245

static VALUE prof_allocation_klass_flags(VALUE self)
{
    prof_allocation_t* allocation = prof_allocation_get(self);
    return INT2FIX(allocation->klass_flags);
}
```

    
  

    
      
  
### 
  
    #**klass**  ⇒ Class 
  

  

  

  
    

Returns the type of Class being allocated.

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (Class)
      
      
      
    
  

  
    
      

```

230
231
232
233
234
235
236
237
238
```

    
    
      

```
# File 'ext/ruby_prof/rp_allocation.c', line 230

static VALUE prof_allocation_klass_name(VALUE self)
{
    prof_allocation_t* allocation = prof_allocation_get(self);

    if (allocation->klass_name == Qnil)
        allocation->klass_name = resolve_klass_name(allocation->klass, &allocation->klass_flags);

    return allocation->klass_name;
}
```

    
  

    
      
  
### 
  
    #**line**  ⇒ Numeric 
  

  

  

  
    

Returns the the line number where objects were allocated.

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (Numeric)
      
      
      
    
  

  
    
      

```

265
266
267
268
269
```

    
    
      

```
# File 'ext/ruby_prof/rp_allocation.c', line 265

static VALUE prof_allocation_source_line(VALUE self)
{
    prof_allocation_t* allocation = prof_allocation_get(self);
    return INT2FIX(allocation->source_line);
}
```

    
  

    
      
  
### 
  
    #**source_file**  ⇒ String 
  

  

  

  
    

Returns the the line number where objects were allocated.

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
    
  

  
    
      

```

255
256
257
258
259
```

    
    
      

```
# File 'ext/ruby_prof/rp_allocation.c', line 255

static VALUE prof_allocation_source_file(VALUE self)
{
    prof_allocation_t* allocation = prof_allocation_get(self);
    return allocation->source_file;
}
```