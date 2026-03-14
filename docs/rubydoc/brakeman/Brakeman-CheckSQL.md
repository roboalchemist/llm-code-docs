# Class: Brakeman::CheckSQL
  
  
  

  
  
    Inherits:
    
      BaseCheck
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- Brakeman::CheckSQL
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_sql.rb
  
  

## Overview

  
    

This check tests for find calls which do not use Rails’ auto SQL escaping

For example: Project.find(:all, :conditions => “name = ‘” + params + “’”)

Project.find(:all, :conditions => “name = ‘#:name’”)

User.find_by_sql(“SELECT * FROM projects WHERE name = ‘#:name’”)

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        TO_STRING_METHODS =
          
        
        

```
[:chomp, :chop, :lstrip, :rstrip, :scrub, :squish, :strip,
:strip_heredoc, :to_s, :tr]
```

      
        IGNORE_METHODS_IN_SQL =
          
        
        

```

```

      
        QUOTE_METHODS =
          
        
        

```
[:quote, :quote_column_name, :quoted_date, :quote_string, :quote_table_name]
```

      
        AREL_METHODS =
          
        
        

```
[:all, :and, :arel_table, :as, :eq, :eq_any, :exists, :group,
:gt, :gteq, :having, :in, :join_sources, :limit, :lt, :lteq, :not,
:not_eq, :on, :or, :order, :project, :skip, :take, :where, :with]
```

      
        SELF_CLASS =
          
        
        

```
s(:call, s(:self), :class)
```

      
        DATE_CLASS =
          
        
        

```
s(:const, :Date)
```

      
    
  

  
  
  
### Constants inherited
     from BaseCheck

  

BaseCheck::CONFIDENCE

  
  
  
### Constants included
     from Util

  

Util::ALL_COOKIES, Util::ALL_PARAMETERS, Util::COOKIES, Util::COOKIES_SEXP, Util::DIR_CONST, Util::LITERALS, Util::PARAMETERS, Util::PARAMS_SEXP, Util::PATH_PARAMETERS, Util::QUERY_PARAMETERS, Util::REQUEST_COOKIES, Util::REQUEST_ENV, Util::REQUEST_PARAMETERS, Util::REQUEST_PARAMS, Util::REQUEST_REQUEST_PARAMETERS, Util::SAFE_LITERAL, Util::SESSION, Util::SESSION_SEXP, Util::SIMPLE_LITERALS

  
  
  
### Constants inherited
     from SexpProcessor

  

SexpProcessor::VERSION

  
## Instance Attribute Summary

  
  
### Attributes inherited from BaseCheck

  

#tracker, #warnings

  
  
  
### Attributes inherited from SexpProcessor

  

#context, #env, #expected

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**ar_scope_calls**(symbol_name, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**arel?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_by_sql_arguments**(arg)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

find_by_sql and count_by_sql can take either a straight SQL string or an array with values to bind.

  

      
        
- 
  
    
      #**check_call**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Check call for string building.

  

      
        
- 
  
    
      #**check_exists**(arg)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_find_arguments**(arg)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The ‘find’ methods accept a number of different types of parameters:.

  

      
        
- 
  
    
      #**check_for_limit_or_offset_vulnerability**(options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Prior to Rails 2.1.1, the :offset and :limit parameters were not escaping input properly.

  

      
        
- 
  
    
      #**check_for_string_building**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_hash_keys**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Check hash keys for user input.

  

      
        
- 
  
    
      #**check_hash_values**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Checks hash values associated with these keys:.

  

      
        
- 
  
    
      #**check_interp_target_or_arg**(target, arg)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_joins_arguments**(arg)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

joins can take a string, hash of associations, or an array of both(?) We only care about the possible string values.

  

      
        
- 
  
    
      #**check_lock_arguments**(arg)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Model#lock essentially only cares about strings.

  

      
        
- 
  
    
      #**check_order_arguments**(args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Checks each argument to order/reorder/group for possible SQL.

  

      
        
- 
  
    
      #**check_query_arguments**(arg)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_scope_arguments**(call)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_str_target_or_arg**(target, arg)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_string_arg**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_string_interp**(arg)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Check an interpolated string for dangerous values.

  

      
        
- 
  
    
      #**check_update_all_arguments**(args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**connect_call?**(result)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**constantize_call?**(result)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Look for something like this:.

  

      
        
- 
  
    
      #**date_target?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**find_dangerous_value**(exp, ignore_hash)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Check *exp* for dangerous values.

  

      
        
- 
  
    
      #**find_scope_calls**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Find calls to named_scope() or scope() in models RP 3 TODO.

  

      
        
- 
  
    
      #**ignore_call?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**ignore_methods_in_sql**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**number_target?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**process_result**(result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Process possible SQL injection sites:.

  

      
        
- 
  
    
      #**process_scope_with_block**(model, args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**quote_call?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**run_check**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**safe_value?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**scope_call_hash**(call, model, method)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**unsafe_sql?**(exp, ignore_hash = false)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Checks the given expression for unsafe SQL values.

  

      
        
- 
  
    
      #**unsafe_string_interp?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Returns value if interpolated value is not something safe.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from BaseCheck

  

#add_result, description, inherited, #initialize, #process_array, #process_call, #process_cookies, #process_default, #process_dstr, #process_if, #process_params

  
  
  
  
  
  
  
  
  
### Methods included from Messages

  

#msg, #msg_code, #msg_cve, #msg_file, #msg_input, #msg_lit, #msg_plain, #msg_version

  
  
  
  
  
  
  
  
  
### Methods included from Util

  

#all_literals?, #array?, #block?, #call?, #camelize, #class_name, #constant?, #contains_class?, #cookies?, #dir_glob?, #false?, #hash?, #hash_access, #hash_insert, #hash_iterate, #hash_values, #integer?, #kwsplat?, #literal?, #make_call, #node_type?, #number?, #params?, #pluralize, #rails_version, #recurse_check?, #regexp?, #remove_kwsplat, #request_headers?, #request_value?, #result?, #safe_literal, #safe_literal?, #safe_literal_target?, #set_env_defaults, #sexp?, #simple_literal?, #string?, #string_interp?, #symbol?, #template_path_to_name, #true?, #underscore

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
### Methods included from ProcessorHelper

  

#current_file, #process_all, #process_all!, #process_call_args, #process_call_defn?, #process_class, #process_module

  
  
  
  
  
  
  
  
  
### Methods inherited from SexpProcessor

  

#in_context, #initialize, #process, processors, #scope

  
## Constructor Details

  
    

This class inherits a constructor from Brakeman::BaseCheck
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**ar_scope_calls**(symbol_name, &block)  ⇒ Object 
  

  

  

  
    
      

```

111
112
113
114
115
116
117
118
119
120
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql.rb', line 111

def ar_scope_calls(symbol_name, &block)
  active_record_models.each do |name, model|
    model_args = model.options[symbol_name]
    if model_args
      model_args.each do |args|
        yield model, args
      end
    end
  end
end
```

    
  

    
      
  
### 
  
    #**arel?**(exp)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

662
663
664
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql.rb', line 662

def arel? exp
  call? exp and (AREL_METHODS.include? exp.method or arel? exp.target)
end
```

    
  

    
      
  
### 
  
    #**check_by_sql_arguments**(arg)  ⇒ Object 
  

  

  

  
    

find_by_sql and count_by_sql can take either a straight SQL string or an array with values to bind.

  

  

  
    
      

```

347
348
349
350
351
352
353
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql.rb', line 347

def check_by_sql_arguments arg
  return unless sexp? arg

  #This is kind of unnecessary, because unsafe_sql? will handle an array
  #correctly, but might be better to be explicit.
  array?(arg) ? unsafe_sql?(arg[1]) : unsafe_sql?(arg)
end
```

    
  

    
      
  
### 
  
    #**check_call**(exp)  ⇒ Object 
  

  

  

  
    

Check call for string building

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql.rb', line 667

def check_call exp
  return unless call? exp
  unsafe = check_for_string_building exp

  if unsafe
    unsafe
  elsif call? exp.target
    check_call exp.target
  else
    nil
  end
end
```

    
  

    
      
  
### 
  
    #**check_exists**(arg)  ⇒ Object 
  

  

  

  
    
      

```

680
681
682
683
684
685
686
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql.rb', line 680

def check_exists arg
  if call? arg and arg.method == :to_s
    false
  else
    check_find_arguments arg
  end
end
```

    
  

    
      
  
### 
  
    #**check_find_arguments**(arg)  ⇒ Object 
  

  

  

  
    

The ‘find’ methods accept a number of different types of parameters:

- 

The first argument might be :all, :first, or :last

- 

The first argument might be an integer ID or an array of IDs

- 

The second argument might be a hash of options, some of which are dangerous and some of which are not

- 

The second argument might contain SQL fragments as values

- 

The second argument might contain properly parameterized SQL fragments in arrays

- 

The second argument might contain improperly parameterized SQL fragments in arrays

This method should only be passed the second argument.

  

  

  
    
      

```

288
289
290
291
292
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql.rb', line 288

def check_find_arguments arg
  return nil if not sexp? arg or node_type? arg, :lit, :string, :str, :true, :false, :nil

  unsafe_sql? arg
end
```

    
  

    
      
  
### 
  
    #**check_for_limit_or_offset_vulnerability**(options)  ⇒ Object 
  

  

  

  
    

Prior to Rails 2.1.1, the :offset and :limit parameters were not escaping input properly.

www.rorsecurity.info/2008/09/08/sql-injection-issue-in-limit-and-offset-parameter/

  

  

  
    
      

```

692
693
694
695
696
697
698
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql.rb', line 692

def check_for_limit_or_offset_vulnerability options
  return false if rails_version.nil? or rails_version >= "2.1.1" or not hash?(options)

  return true if hash_access(options, :limit) or hash_access(options, :offset)

  false
end
```

    
  

    
      
  
### 
  
    #**check_for_string_building**(exp)  ⇒ Object 
  

  

  

  
    
      

```

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
564
565
566
567
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql.rb', line 552

def check_for_string_building exp
  return unless call? exp

  target = exp.target
  method = exp.method
  arg = exp.first_arg

  if STRING_METHODS.include? method
    check_str_target_or_arg(target, arg) or
    check_interp_target_or_arg(target, arg) or
    check_for_string_building(target) or
    check_for_string_building(arg)
  else
    nil
  end
end
```

    
  

    
      
  
### 
  
    #**check_hash_keys**(exp)  ⇒ Object 
  

  

  

  
    

Check hash keys for user input. (Seems unlikely, but if a user can control the column names queried, that could be bad)

  

  

  
    
      

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql.rb', line 394

def check_hash_keys exp
  hash_iterate(exp) do |key, _value|
    unless symbol?(key)
      unsafe_key = unsafe_sql? key
      return unsafe_key if unsafe_key
    end
  end

  false
end
```

    
  

    
      
  
### 
  
    #**check_hash_values**(exp)  ⇒ Object 
  

  

  

  
    

Checks hash values associated with these keys:

- 

conditions

- 

order

- 

having

- 

joins

- 

select

- 

from

- 

lock

  

  

  
    
      

```

527
528
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
548
549
550
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql.rb', line 527

def check_hash_values exp
  hash_iterate(exp) do |key, value|
    if symbol? key
      unsafe = case key.value
               when :conditions, :having, :select
                 check_query_arguments value
               when :order, :group
                 check_order_arguments value
               when :joins
                 check_joins_arguments value
               when :lock
                 check_lock_arguments value
               when :from
                 unsafe_sql? value
               else
                 nil
               end

      return unsafe if unsafe
    end
  end

  false
end
```

    
  

    
      
  
### 
  
    #**check_interp_target_or_arg**(target, arg)  ⇒ Object 
  

  

  

  
    
      

```

577
578
579
580
581
582
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql.rb', line 577

def check_interp_target_or_arg target, arg
  if string_interp? target or string_interp? arg
    check_string_arg target and
    check_string_arg arg
  end
end
```

    
  

    
      
  
### 
  
    #**check_joins_arguments**(arg)  ⇒ Object 
  

  

  

  
    

joins can take a string, hash of associations, or an array of both(?) We only care about the possible string values.

  

  

  
    
      

```

357
358
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
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql.rb', line 357

def check_joins_arguments arg
  return unless sexp? arg and not node_type? arg, :hash, :string, :str

  if array? arg
    arg.each do |a|
      unsafe_arg = check_joins_arguments a
      return unsafe_arg if unsafe_arg
    end

    nil
  else
    unsafe_sql? arg
  end
end
```

    
  

    
      
  
### 
  
    #**check_lock_arguments**(arg)  ⇒ Object 
  

  

  

  
    

Model#lock essentially only cares about strings. But those strings can be any SQL fragment. This does not apply to all databases. (For those who do not support it, the lock method does nothing).

  

  

  
    
      

```

384
385
386
387
388
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql.rb', line 384

def check_lock_arguments arg
  return unless sexp? arg and not node_type? arg, :hash, :array, :string, :str

  unsafe_sql?(arg, :ignore_hash)
end
```

    
  

    
      
  
### 
  
    #**check_order_arguments**(args)  ⇒ Object 
  

  

  

  
    

Checks each argument to order/reorder/group for possible SQL. Anything used with these methods is passed in verbatim.

  

  

  
    
      

```

335
336
337
338
339
340
341
342
343
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql.rb', line 335

def check_order_arguments args
  return unless sexp? args

  if node_type? args, :arglist
    check_update_all_arguments(args)
  else
    unsafe_sql? args
  end
end
```

    
  

    
      
  
### 
  
    #**check_query_arguments**(arg)  ⇒ Object 
  

  

  

  
    
      

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
323
324
325
326
327
328
329
330
331
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql.rb', line 300

def check_query_arguments arg
  return unless sexp? arg
  first_arg = arg[1]

  if node_type? arg, :arglist
    if arg.length > 2 and string_interp? first_arg
      # Model.where("blah = ?", blah)
      return check_string_interp first_arg
    else
      arg = first_arg
    end
  end

  if request_value? arg
    unless call? arg and params? arg.target and [:permit, :slice, :to_h, :to_hash, :symbolize_keys].include? arg.method
      # Model.where(params[:where])
      arg
    end
  elsif hash? arg and not kwsplat? arg
    #This is generally going to be a hash of column names and values, which
    #would escape the values. But the keys _could_ be user input.
    check_hash_keys arg
  elsif node_type? arg, :lit, :str
    nil
  elsif node_type? arg, :or
    check_query_arguments(arg.lhs) or
      check_query_arguments(arg.rhs)
  else
    #Hashes are safe...but we check above for hash, so...?
    unsafe_sql? arg, :ignore_hash
  end
end
```

    
  

    
      
  
### 
  
    #**check_scope_arguments**(call)  ⇒ Object 
  

  

  

  
    
      

```

294
295
296
297
298
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql.rb', line 294

def check_scope_arguments call
  scope_arg = call.second_arg #first arg is name of scope

  node_type?(scope_arg, :iter) ? unsafe_sql?(scope_arg.block) : unsafe_sql?(scope_arg)
end
```

    
  

    
      
  
### 
  
    #**check_str_target_or_arg**(target, arg)  ⇒ Object 
  

  

  

  
    
      

```

569
570
571
572
573
574
575
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql.rb', line 569

def check_str_target_or_arg target, arg
  if string? target
    check_string_arg arg
  elsif string? arg
    check_string_arg target
  end
end
```

    
  

    
      
  
### 
  
    #**check_string_arg**(exp)  ⇒ Object 
  

  

  

  
    
      

```

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
594
595
596
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql.rb', line 584

def check_string_arg exp
  if safe_value? exp
    nil
  elsif string_building? exp
    check_for_string_building exp
  elsif string_interp? exp
    check_string_interp exp
  elsif call? exp and exp.method == :to_s
    check_string_arg exp.target
  else
    exp
  end
end
```

    
  

    
      
  
### 
  
    #**check_string_interp**(arg)  ⇒ Object 
  

  

  

  
    

Check an interpolated string for dangerous values.

This method assumes values interpolated into strings are unsafe by default, unless safe_value? explicitly returns true.

  

  

  
    
      

```

409
410
411
412
413
414
415
416
417
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql.rb', line 409

def check_string_interp arg
  arg.each do |exp|
    if dangerous = unsafe_string_interp?(exp)
      return dangerous
    end
  end

  nil
end
```

    
  

    
      
  
### 
  
    #**check_update_all_arguments**(args)  ⇒ Object 
  

  

  

  
    
      

```

372
373
374
375
376
377
378
379
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql.rb', line 372

def check_update_all_arguments args
  args.each do |arg|
    unsafe_arg = unsafe_sql? arg
    return unsafe_arg if unsafe_arg
  end

  nil
end
```

    
  

    
      
  
### 
  
    #**connect_call?**(result)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql.rb', line 721

def connect_call? result
  call = result[:call]
  target = call.target

  if call? target and target.method == :connection
    target = target.target
    klass = class_name(target)

    target.nil? or
    target == SELF_CLASS or
    node_type? target, :self or
    klass == :"ActiveRecord::Base" or
    active_record_models.include? klass
  end
end
```

    
  

    
      
  
### 
  
    #**constantize_call?**(result)  ⇒ Boolean 
  

  

  

  
    

Look for something like this:

params.constantize.find(‘something’)

s(:call,

```
s(:call,
  s(:call,
    s(:call, nil, :params, s(:arglist)),
    :[],
    s(:arglist, s(:lit, :x))),
  :constantize,
  s(:arglist)),
:find,
s(:arglist, s(:str, "something")))

```

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

714
715
716
717
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql.rb', line 714

def constantize_call? result
  call = result[:call]
  call? call.target and call.target.method == :constantize
end
```

    
  

    
      
  
### 
  
    #**date_target?**(exp)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

751
752
753
754
755
756
757
758
759
760
761
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql.rb', line 751

def date_target? exp
  return unless call? exp

  if exp.target == DATE_CLASS
    true
  elsif call? exp.target
    date_target? exp.target
  else
   false
  end
end
```

    
  

    
      
  
### 
  
    #**find_dangerous_value**(exp, ignore_hash)  ⇒ Object 
  

  

  

  
    

Check *exp* for dangerous values. Used by unsafe_sql?

  

  

  
    
      

```

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
495
496
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
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql.rb', line 468

def find_dangerous_value exp, ignore_hash
  case exp.node_type
  when :lit, :str, :const, :colon2, :true, :false, :nil
    nil
  when :array
    #Assume this is an array like
    #
    #  ["blah = ? AND thing = ?", ...]
    #
    #and check first value
    unsafe_sql? exp[1]
  when :dstr
    check_string_interp exp
  when :hash
    if kwsplat? exp and has_immediate_user_input? exp
      exp
    elsif not ignore_hash
      check_hash_values exp
    else
      nil
    end
  when :if
    unsafe_sql? exp.then_clause or unsafe_sql? exp.else_clause
  when :call
    unless IGNORE_METHODS_IN_SQL.include? exp.method
      if has_immediate_user_input? exp
        exp
      elsif TO_STRING_METHODS.include? exp.method
        find_dangerous_value exp.target, ignore_hash
      else
        check_call exp
      end
    end
  when :or
    if unsafe = (unsafe_sql?(exp.lhs) || unsafe_sql?(exp.rhs))
      unsafe
    else
      nil
    end
  when :block, :rlist
    unsafe_sql? exp.last
  else
    if has_immediate_user_input? exp
      exp
    else
      nil
    end
  end
end
```

    
  

    
      
  
### 
  
    #**find_scope_calls**  ⇒ Object 
  

  

  

  
    

Find calls to named_scope() or scope() in models RP 3 TODO

  

  

  
    
      

```

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
103
104
105
106
107
108
109
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql.rb', line 83

def find_scope_calls
  scope_calls = []

  # Used in pre-3.1.0 versions of Rails
  ar_scope_calls(:named_scope) do |model, args|
    call = make_call(nil, :named_scope, args).line(args.line)
    scope_calls << scope_call_hash(call, model, :named_scope)
  end

  # Use in 3.1.0 and later
  ar_scope_calls(:scope) do |model, args|
    second_arg = args[2]
    next unless sexp? second_arg

    if second_arg.node_type == :iter and node_type? second_arg.block, :block, :call, :safe_call
      process_scope_with_block(model, args)
    elsif call? second_arg
      call = second_arg
      scope_calls << scope_call_hash(call, model, call.method)
    else
      call = make_call(nil, :scope, args).line(args.line)
      scope_calls << scope_call_hash(call, model, :scope)
    end
  end

  scope_calls
end
```

    
  

    
      
  
### 
  
    #**ignore_call?**(exp)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

636
637
638
639
640
641
642
643
644
645
646
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql.rb', line 636

def ignore_call? exp
  return unless call? exp

  ignore_methods_in_sql.include? exp.method or
    quote_call? exp or
    arel? exp or
    exp.method.to_s.end_with? "_id" or
    number_target? exp or
    date_target? exp or
    locale_call? exp
end
```

    
  

    
      
  
### 
  
    #**ignore_methods_in_sql**  ⇒ Object 
  

  

  

  
    
      

```

607
608
609
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql.rb', line 607

def ignore_methods_in_sql
  @ignore_methods_in_sql ||= IGNORE_METHODS_IN_SQL + (tracker.options[:sql_safe_methods] || [])
end
```

    
  

    
      
  
### 
  
    #**number_target?**(exp)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

737
738
739
740
741
742
743
744
745
746
747
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql.rb', line 737

def number_target? exp
  return unless call? exp

  if number? exp.target
    true
  elsif call? exp.target
    number_target? exp.target
  else
    false
  end
end
```

    
  

    
      
  
### 
  
    #**process_result**(result)  ⇒ Object 
  

  

  

  
    

Process possible SQL injection sites:

Model#find

Model#(named_)scope

Model#(find|count)_by_sql

Model#all

Rails 3

Model#(where|having) Model#(order|group)

Find Options Hash

Dangerous keys that accept SQL:

- 

conditions

- 

order

- 

having

- 

joins

- 

select

- 

from

- 

lock

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql.rb', line 173

def process_result result
  return if duplicate?(result) or result[:call].original_line

  call = result[:call]
  method = call.method

  dangerous_value = case method
                    when :find
                      check_find_arguments call.second_arg
                    when :exists?
                      check_exists call.first_arg
                    when :delete_all, :destroy_all
                      check_find_arguments call.first_arg
                    when :named_scope, :scope
                      check_scope_arguments call
                    when :find_by_sql, :count_by_sql
                      check_by_sql_arguments call.first_arg
                    when :calculate
                      if call.num_args > 2
                        unsafe_sql?(call.second_arg) or check_find_arguments(call.third_arg)
                      elsif call.num_args > 1
                        unsafe_sql?(call.second_arg)
                      end
                    when :last, :first, :all
                      check_find_arguments call.first_arg
                    when :average, :count, :maximum, :minimum, :sum
                      if call.num_args > 1
                        if version_between?("0.0.0", "4.9.9") # In Rails 5+ these do not accept multiple arguments
                          check_find_arguments(call.first_arg) or check_find_arguments(call.second_arg)
                        end
                      else
                        check_find_arguments call.first_arg
                      end
                    when :where, :rewhere, :having, :find_by, :find_by!, :find_or_create_by, :find_or_create_by!, :find_or_initialize_by,:not, :delete_by, :destroy_by
                      check_query_arguments call.arglist
                    when :order, :group, :reorder
                      check_order_arguments call.arglist
                    when :joins
                      check_joins_arguments call.first_arg
                    when :from
                      unsafe_sql? call.first_arg
                    when :lock
                      check_lock_arguments call.first_arg
                    when :pluck
                      unsafe_sql? call.first_arg
                    when :sql
                      unsafe_sql? call.first_arg
                    when :update_all, :select, :reselect
                      check_update_all_arguments call.args
                    when *@connection_calls
                      check_by_sql_arguments call.first_arg
                    else
                      Brakeman.debug "Unhandled SQL method: #{method}"
                    end

  if dangerous_value
    add_result result

    input = include_user_input? dangerous_value
    if input
      confidence = :high
      user_input = input
    else
      confidence = :medium
      user_input = dangerous_value
    end

    if result[:call].target and result[:chain] and not @expected_targets.include? result[:chain].first
      confidence = case confidence
                   when :high
                     :medium
                   when :medium
                     :weak
                   else
                     confidence
                   end
    end

    warn :result => result,
      :warning_type => "SQL Injection",
      :warning_code => :sql_injection,
      :message => "Possible SQL injection",
      :user_input => user_input,
      :confidence => confidence,
      :cwe_id => [89]
  end

  if check_for_limit_or_offset_vulnerability call.last_arg
    if include_user_input? call.last_arg
      confidence = :high
    else
      confidence = :weak
    end

    warn :result => result,
      :warning_type => "SQL Injection",
      :warning_code => :sql_injection_limit_offset,
      :message => msg("Upgrade to Rails >= 2.1.2 to escape ", msg_code(":limit"), " and ", msg_code("offset"), ". Possible SQL injection"),
      :confidence => confidence,
      :cwe_id => [89]
  end
end
```

    
  

    
      
  
### 
  
    #**process_scope_with_block**(model, args)  ⇒ Object 
  

  

  

  
    
      

```

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
139
140
141
142
143
144
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql.rb', line 127

def process_scope_with_block model, args
  scope_name = args[1][1]
  block = args[-1][-1]

  # Search lambda for calls to query methods
  if block.node_type == :block
    find_calls = Brakeman::FindAllCalls.new(tracker)
    find_calls.process_source(block, :class => model.name, :method => scope_name, :file => model.file)
    find_calls.calls.each { |call| process_result(call) if @sql_targets.include?(call[:method]) }
  elsif call? block
    while call? block
      process_result :target => block.target, :method => block.method, :call => block,
        :location => { :type => :class, :class => model.name, :method => scope_name, :file => model.file }

      block = block.target
    end
  end
end
```

    
  

    
      
  
### 
  
    #**quote_call?**(exp)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

650
651
652
653
654
655
656
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql.rb', line 650

def quote_call? exp
  if call? exp.target
    exp.target.method == :connection and QUOTE_METHODS.include? exp.method
  elsif exp.target.nil?
    exp.method == :quote_value
  end
end
```

    
  

    
      
  
### 
  
    #**run_check**  ⇒ Object 
  

  

  

  
    
      

```

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
29
30
31
32
33
34
35
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
47
48
49
50
51
52
53
54
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
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql.rb', line 16

def run_check
  # Avoid reporting `user_input` on silly values when generating warning.
  # Note that we retroactively find `user_input` inside the "dangerous" value.
  @safe_input_attributes.merge IGNORE_METHODS_IN_SQL

  @sql_targets = [:average, :calculate, :count, :count_by_sql, :delete_all, :destroy_all,
                  :find_by_sql, :maximum, :minimum, :pluck, :sum, :update_all]
  @sql_targets.concat [:from, :group, :having, :joins, :lock, :order, :reorder, :where] if tracker.options[:rails3]
  @sql_targets.concat [:find_by, :find_by!, :find_or_create_by, :find_or_create_by!, :find_or_initialize_by, :not] if tracker.options[:rails4]

  if tracker.options[:rails6]
    @sql_targets.concat [:delete_by, :destroy_by, :rewhere, :reselect]

    @sql_targets.delete :delete_all
    @sql_targets.delete :destroy_all
  end

  if version_between?("6.1.0", "9.9.9")
    @sql_targets.delete :order
    @sql_targets.delete :reorder
    @sql_targets.delete :pluck
  end

  if version_between?("2.0.0", "3.9.9") or tracker.config.rails_version.nil?
    @sql_targets << :first << :last << :all
  end

  if version_between?("2.0.0", "4.0.99") or tracker.config.rails_version.nil?
    @sql_targets << :find
  end

  @connection_calls = [:delete, :execute, :insert, :select_all, :select_one,
    :select_rows, :select_value, :select_values]

  if tracker.options[:rails3]
    @connection_calls.concat [:exec_delete, :exec_insert, :exec_query, :exec_update]
  else
    @connection_calls.concat [:add_limit!, :add_offset_limit!, :add_lock!]
  end

  @expected_targets = active_record_models.keys + [:connection, :"ActiveRecord::Base", :Arel]

  Brakeman.debug "Finding possible SQL calls on models"
  calls = tracker.find_call(:methods => @sql_targets, :nested => true)

  narrow_targets = [:exists?, :select]
  calls.concat tracker.find_call(:targets => active_record_models.keys, :methods => narrow_targets, :chained => true)

  Brakeman.debug "Finding possible SQL calls with no target"
  calls.concat tracker.find_call(:target => nil, :methods => @sql_targets)

  Brakeman.debug "Finding possible SQL calls using constantized()"
  calls.concat tracker.find_call(:methods => @sql_targets).select { |result| constantize_call? result }

  calls.concat tracker.find_call(:targets => @expected_targets, :methods => @connection_calls, :chained => true).select { |result| connect_call? result }

  calls.concat tracker.find_call(:target => :Arel, :method => :sql)

  Brakeman.debug "Finding calls to named_scope or scope"
  calls.concat find_scope_calls

  Brakeman.debug "Processing possible SQL calls"
  calls.each { |call| process_result call }
end
```

    
  

    
      
  
### 
  
    #**safe_value?**(exp)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql.rb', line 611

def safe_value? exp
  return true unless sexp? exp

  case exp.node_type
  when :str, :lit, :const, :colon2, :nil, :true, :false
    true
  when :call
    if exp.method == :to_s or exp.method == :to_sym
      safe_value? exp.target
    else
      ignore_call? exp
    end
  when :if
    safe_value? exp.then_clause and safe_value? exp.else_clause
  when :block, :rlist
    safe_value? exp.last
  when :or
    safe_value? exp.lhs and safe_value? exp.rhs
  when :dstr
    not unsafe_string_interp? exp
  else
    false
  end
end
```

    
  

    
      
  
### 
  
    #**scope_call_hash**(call, model, method)  ⇒ Object 
  

  

  

  
    
      

```

122
123
124
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql.rb', line 122

def scope_call_hash(call, model, method)
  { :call => call, :location => { :type => :class, :class => model.name, :file => model.file }, :method => :named_scope }
end
```

    
  

    
      
  
### 
  
    #**unsafe_sql?**(exp, ignore_hash = false)  ⇒ Boolean 
  

  

  

  
    

Checks the given expression for unsafe SQL values. If an unsafe value is found, returns that value (may be the given *exp* or a subexpression).

Otherwise, returns false/nil.

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

460
461
462
463
464
465
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql.rb', line 460

def unsafe_sql? exp, ignore_hash = false
  return unless sexp?(exp)

  dangerous_value = find_dangerous_value exp, ignore_hash
  safe_value?(dangerous_value) ? false : dangerous_value
end
```

    
  

    
      
  
### 
  
    #**unsafe_string_interp?**(exp)  ⇒ Boolean 
  

  

  

  
    

Returns value if interpolated value is not something safe

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

423
424
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
444
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
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql.rb', line 423

def unsafe_string_interp? exp
  if node_type? exp, :evstr
    value = exp.value
  else
    value = exp
  end

  if not sexp? value
    nil
  elsif call? value and TO_STRING_METHODS.include? value.method
    unsafe_string_interp? value.target
  elsif call? value and safe_literal_target? value
    nil
  else
    case value.node_type
    when :or
      unsafe_string_interp?(value.lhs) || unsafe_string_interp?(value.rhs)
    when :dstr
      if dangerous = check_string_interp(value)
        return dangerous
      end
    else
      if safe_value? value
        nil
      elsif string_building? value
        check_for_string_building value
      else
        value
      end
    end
  end
end
```