# Class: RubyProf::CallTrees
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- RubyProf::CallTrees
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    ext/ruby_prof/rp_call_trees.c,

  ext/ruby_prof/rp_call_trees.c

  
  

## Overview

  
    

The RubyProf::MethodInfo class stores profiling data for a method. One instance of the RubyProf::MethodInfo class is created per method called per thread.  Thus, if a method is called in two different thread then there will be two RubyProf::MethodInfo objects created.  RubyProf::MethodInfo objects can be accessed via the RubyProf::Profile object.

  

  

  
    
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
  
    
      #**callers**  ⇒ Array 
    

    
  
  
  
  
  
  
  
  

  
    

Returns an array of all CallTree objects that called this method.

  

      
        
- 
  
    
      #**callees**  ⇒ Array 
    

    
  
  
  
  
  
  
  
  

  
    

Returns an array of aggregated CallTree objects that this method called (ie, children).

  

      
        
- 
  
    
      #**callers**  ⇒ Array 
    

    
  
  
  
  
  
  
  
  

  
    

Returns an array of aggregated CallTree objects that called this method (ie, parents).

  

      
        
- 
  
    
      #**min_depth**  ⇒ Integer 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the minimum depth of this method in any call tree.

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**_dump_data**  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

257
258
259
260
261
262
263
```

    
    
      

```
# File 'ext/ruby_prof/rp_call_trees.c', line 257

VALUE prof_call_trees_dump(VALUE self)
{
    VALUE result = rb_hash_new();
    rb_hash_aset(result, ID2SYM(rb_intern("call_trees")), prof_call_trees_call_trees(self));

    return result;
}
```

    
  

    
      
  
### 
  
    #**_load_data**(data)  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

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
```

    
    
      

```
# File 'ext/ruby_prof/rp_call_trees.c', line 266

VALUE prof_call_trees_load(VALUE self, VALUE data)
{
    prof_call_trees_t* call_trees_data = prof_get_call_trees(self);
    call_trees_data->object = self;

    VALUE call_trees = rb_hash_aref(data, ID2SYM(rb_intern("call_trees")));
    for (int i = 0; i < rb_array_len(call_trees); i++)
    {
        VALUE call_tree = rb_ary_entry(call_trees, i);
        prof_call_tree_t* call_tree_data = prof_get_call_tree(call_tree);
        prof_add_call_tree(call_trees_data, call_tree_data);
    }

    return data;
}
```

    
  

    
      
  
### 
  
    #**callers**  ⇒ Array 
  

  

  

  
    

Returns an array of all CallTree objects that called this method.

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (Array)
      
      
      
    
  

  
    
      

```

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
# File 'ext/ruby_prof/rp_call_trees.c', line 185

VALUE prof_call_trees_call_trees(VALUE self)
{
    VALUE result = rb_ary_new();

    prof_call_trees_t* call_trees = prof_get_call_trees(self);
    for (prof_call_tree_t** p_call_tree = call_trees->start; p_call_tree < call_trees->ptr; p_call_tree++)
    {
        VALUE call_tree = prof_call_tree_wrap(*p_call_tree);
        rb_ary_push(result, call_tree);
    }
    return result;
}
```

    
  

    
      
  
### 
  
    #**callees**  ⇒ Array 
  

  

  

  
    

Returns an array of aggregated CallTree objects that this method called (ie, children).

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (Array)
      
      
      
    
  

  
    
      

```

240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
```

    
    
      

```
# File 'ext/ruby_prof/rp_call_trees.c', line 240

VALUE prof_call_trees_callees(VALUE self)
{
    st_table* callees = rb_st_init_numtable();

    prof_call_trees_t* call_trees = prof_get_call_trees(self);
    for (prof_call_tree_t** call_tree = call_trees->start; call_tree < call_trees->ptr; call_tree++)
    {
        rb_st_foreach((*call_tree)->children, prof_call_trees_collect_callees, (st_data_t)callees);
    }

    VALUE result = rb_ary_new_capa((long)callees->num_entries);
    rb_st_foreach(callees, prof_call_trees_collect, result);
    rb_st_free_table(callees);
    return result;
}
```

    
  

    
      
  
### 
  
    #**callers**  ⇒ Array 
  

  

  

  
    

Returns an array of aggregated CallTree objects that called this method (ie, parents).

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (Array)
      
      
      
    
  

  
    
      

```

202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
```

    
    
      

```
# File 'ext/ruby_prof/rp_call_trees.c', line 202

VALUE prof_call_trees_callers(VALUE self)
{
    st_table* callers = rb_st_init_numtable();

    prof_call_trees_t* call_trees = prof_get_call_trees(self);
    for (prof_call_tree_t** p_call_tree = call_trees->start; p_call_tree < call_trees->ptr; p_call_tree++)
    {
        prof_call_tree_t* parent = (*p_call_tree)->parent;
        if (parent == NULL)
            continue;

        prof_call_tree_t* aggregate_call_tree_data = NULL;

        if (rb_st_lookup(callers, parent->method->key, (st_data_t*)&aggregate_call_tree_data))
        {
          prof_measurement_merge_internal(aggregate_call_tree_data->measurement, (*p_call_tree)->measurement);
        }
        else
        {
            // Copy the call tree so we don't touch the original and give Ruby ownerhip 
            // of it so that it is freed on GC
            aggregate_call_tree_data = prof_call_tree_copy(*p_call_tree);
            aggregate_call_tree_data->owner = OWNER_RUBY;

            rb_st_insert(callers, parent->method->key, (st_data_t)aggregate_call_tree_data);
        }
    }

    VALUE result = rb_ary_new_capa((long)callers->num_entries);
    rb_st_foreach(callers, prof_call_trees_collect, result);
    rb_st_free_table(callers);
    return result;
}
```

    
  

    
      
  
### 
  
    #**min_depth**  ⇒ Integer 
  

  

  

  
    

Returns the minimum depth of this method in any call tree

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (Integer)
      
      
      
    
  

  
    
      

```

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
```

    
    
      

```
# File 'ext/ruby_prof/rp_call_trees.c', line 166

VALUE prof_call_trees_min_depth(VALUE self)
{
    unsigned int depth = INT_MAX;

    prof_call_trees_t* call_trees = prof_get_call_trees(self);
    for (prof_call_tree_t** p_call_tree = call_trees->start; p_call_tree < call_trees->ptr; p_call_tree++)
    {
        unsigned int call_tree_depth = prof_call_tree_figure_depth(*p_call_tree);
        if (call_tree_depth < depth)
            depth = call_tree_depth;
    }

    return UINT2NUM(depth);
}
```