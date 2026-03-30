# Class: Brakeman::AliasProcessor
  
  
  

  
  
    Inherits:
    
      SexpProcessor
      
        

          
- Object
          
            
- SexpProcessor
          
            
- Brakeman::AliasProcessor
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      CallConversionHelper, ProcessorHelper, SafeCallHelper, Util
  
  
  

  

  
  
    Defined in:
    lib/brakeman/processors/alias_processor.rb
  
  

## Overview

  
    

Returns an s-expression with aliases replaced with their value. This does not preserve semantics (due to side effects, etc.), but it makes processing easier when searching for various things.

  

  

  
## Direct Known Subclasses

  

ConfigAliasProcessor, ControllerAliasProcessor, RouteAliasProcessor, TemplateAliasProcessor

  
    
## 
      Constant Summary
      collapse
    

    
      
        ARRAY_CONST =
          
        
        

```
s(:const, :Array)
```

      
        HASH_CONST =
          
        
        

```
s(:const, :Hash)
```

      
        RAILS_TEST =
          
        
        

```
s(:call, s(:call, s(:const, :Rails), :env), :test?)
```

      
        RAILS_DEV =
          
        
        

```
s(:call, s(:call, s(:const, :Rails), :env), :development?)
```

      
        TEMP_FILE_CLASS =
          
        
        

```
s(:const, :Tempfile)
```

      
        STRING_NEW =
          
        
        

```
s(:call, s(:const, :String), :new)
```

      
    
  

  
  
  
### Constants included
     from CallConversionHelper

  

CallConversionHelper::STRING_LENGTH_LIMIT

  
  
  
### Constants included
     from Util

  

Util::ALL_COOKIES, Util::ALL_PARAMETERS, Util::COOKIES, Util::COOKIES_SEXP, Util::DIR_CONST, Util::LITERALS, Util::PARAMETERS, Util::PARAMS_SEXP, Util::PATH_PARAMETERS, Util::QUERY_PARAMETERS, Util::REQUEST_COOKIES, Util::REQUEST_ENV, Util::REQUEST_PARAMETERS, Util::REQUEST_PARAMS, Util::REQUEST_REQUEST_PARAMETERS, Util::SAFE_LITERAL, Util::SESSION, Util::SESSION_SEXP, Util::SIMPLE_LITERALS

  
  
  
### Constants inherited
     from SexpProcessor

  

SexpProcessor::VERSION

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**result**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute result.

  

    
      
- 
  
    
      #**tracker**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute tracker.

  

    
  

  
  
  
### Attributes inherited from SexpProcessor

  

#context, #env, #expected

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**all_literals_when?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

A list of literal values.

  

      
        
- 
  
    
      #**array_detect_all_literals?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**array_include_all_literals?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Check if exp is a call to Array#include? on an array literal that contains all literal values.

  

      
        
- 
  
    
      #**assign_args**(method_exp, args, meth_env = SexpProcessor::Environment.new)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**collapse_send_call**(exp, first_arg)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Change x.send(:y, 1) to x.y(1).

  

      
        
- 
  
    
      #**duplicate?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**early_return?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**equality_check?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**find_method**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**find_push_target**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Finds the inner most call target which is not the target of a call to <<.

  

      
        
- 
  
    
      #**get_call_value**(call)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**get_rhs**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Handles x = y = z = 1.

  

      
        
- 
  
    
      #**hash_include_all_literals?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Check if exp is a call to Hash#include? on a hash literal that contains all literal values.

  

      
        
- 
  
    
      #**hash_or_array_include_all_literals?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**in_array_all_literals?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Check if exp is a call to Array#include? on an array literal that contains all literal values.

  

      
        
- 
  
    
      #**initialize**(tracker = nil, current_file = nil)  ⇒ AliasProcessor 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Returns a new AliasProcessor with an empty environment.

  

      
        
- 
  
    
      #**join_item**(item, join_value)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**merge_if_branch**(branch_env)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**meth_env**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**new_string?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

String.new ?.

  

      
        
- 
  
    
      #**only_ivars**(include_request_vars = false, lenv = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns a new SexpProcessor::Environment containing only instance variables.

  

      
        
- 
  
    
      #**only_request_vars**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**process_array_join**(array, join_str)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Painful conversion of Array#join into string interpolation.

  

      
        
- 
  
    
      #**process_attrasgn**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

‘Attribute’ assignment x.y = 1 or x = 1.

  

      
        
- 
  
    
      #**process_block**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Start new scope for block.

  

      
        
- 
  
    
      #**process_bracket_call**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**process_branch_with_value**(var, value, branch, branch_index)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**process_call**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Process a method call.

  

      
        
- 
  
    
      #**process_case**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**process_cdecl**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Constant assignments like BIG_CONSTANT = 234810983.

  

      
        
- 
  
    
      #**process_cvdecl**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Class variable assignment @@x = 1.

  

      
        
- 
  
    
      #**process_default**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Process a Sexp.

  

      
        
- 
  
    
      #**process_defn**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Process a method definition.

  

      
        
- 
  
    
      #**process_defs**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Process a method definition on self.

  

      
        
- 
  
    
      #**process_gasgn**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Global assignment $x = 1.

  

      
        
- 
  
    
      #**process_hash**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**process_hash_merge**(hash, args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Return a new hash Sexp with the given values merged into it.

  

      
        
- 
  
    
      #**process_hash_merge!**(hash, args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Merge values into hash when processing.

  

      
        
- 
  
    
      #**process_helper_method**(method_exp, args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**process_iasgn**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Instance variable assignment.

  

      
        
- 
  
    
      #**process_if**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Sets @inside_if = true.

  

      
        
- 
  
    
      #**process_if_branch**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**process_iter**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**process_lasgn**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Local assignment x = 1.

  

      
        
- 
  
    
      #**process_masgn**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Multiple/parallel assignment:.

  

      
        
- 
  
    
      #**process_op_asgn1**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Assignments like this x ||= 1.

  

      
        
- 
  
    
      #**process_op_asgn2**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Assignments like this x.y ||= 1.

  

      
        
- 
  
    
      #**process_or_simple_operation**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

If possible, distribute operation over both sides of an or.

  

      
        
- 
  
    
      #**process_or_target**(value, copy)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**process_safely**(src, set_env = nil, current_file = @current_file)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

This method processes the given Sexp, but copies it first so the original argument will not be modified.

  

      
        
- 
  
    
      #**process_scope**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Process a new scope.

  

      
        
- 
  
    
      #**process_svalue**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

This is the right hand side value of a multiple assignment, like ‘x = y, z`.

  

      
        
- 
  
    
      #**raise?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**replace**(exp, int = 0)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**same_value?**(lhs, rhs)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Return true if lhs == rhs or lhs is an or expression and rhs is one of its values.

  

      
        
- 
  
    
      #**self_assign?**(var, value)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**self_assign_target?**(var, value)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Return true for x = x.blah.

  

      
        
- 
  
    
      #**self_assign_var?**(var, value)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Return true if for x = blah or @x = blah.

  

      
        
- 
  
    
      #**set_value**(var, value)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Set variable to given value.

  

      
        
- 
  
    
      #**simple_when?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Not a list of values   when :example.

  

      
        
- 
  
    
      #**splat_array?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**temp_file_create?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**temp_file_new**(line)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**temp_file_open?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**too_deep?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**top_target**(exp, last = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns last non-nil target in a call chain.

  

      
        
- 
  
    
      #**value_from_case**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**value_from_if**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from CallConversionHelper

  

#hash_values_at, #join_arrays, #join_strings, #math_op, #process_array_access, #process_hash_access

  
  
  
  
  
  
  
  
  
### Methods included from Util

  

#all_literals?, #array?, #block?, #call?, #camelize, #class_name, #constant?, #contains_class?, #cookies?, #dir_glob?, #false?, #hash?, #hash_access, #hash_insert, #hash_iterate, #hash_values, #integer?, #kwsplat?, #literal?, #make_call, #node_type?, #number?, #params?, #pluralize, #rails_version, #recurse_check?, #regexp?, #remove_kwsplat, #request_headers?, #request_value?, #result?, #safe_literal, #safe_literal?, #safe_literal_target?, #set_env_defaults, #sexp?, #simple_literal?, #string?, #string_interp?, #symbol?, #template_path_to_name, #true?, #underscore

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
### Methods included from ProcessorHelper

  

#current_file, #process_all, #process_all!, #process_call_args, #process_call_defn?, #process_class, #process_module

  
  
  
  
  
  
  
  
  
### Methods inherited from SexpProcessor

  

#in_context, #process, processors, #scope

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(tracker = nil, current_file = nil)  ⇒ AliasProcessor 
  

  

  

  
    

Returns a new AliasProcessor with an empty environment.

The recommended usage is:

AliasProcessor.new.process_safely src

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 23

def initialize tracker = nil, current_file = nil
  super()
  @env = SexpProcessor::Environment.new
  @inside_if = false
  @ignore_ifs = nil
  @exp_context = []
  @tracker = tracker #set in subclass as necessary
  @helper_method_cache = {}
  @helper_method_info = Hash.new({})
  @or_depth_limit = (tracker && tracker.options[:branch_limit]) || 5 #arbitrary default
  @meth_env = nil
  @current_file = current_file
  @mass_limit = (tracker && tracker.options[:mass_limit]) || 1000 # arbitrary default
  set_env_defaults
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**result**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute result.

  

  

  
    
      

```

16
17
18
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 16

def result
  @result
end
```

    
  

    
      
      
      
  
### 
  
    #**tracker**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute tracker.

  

  

  
    
      

```

16
17
18
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 16

def tracker
  @tracker
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**all_literals_when?**(exp)  ⇒ Boolean 
  

  

  

  
    

A list of literal values

```
when 1,2,3

```

or

```
when *[:a, :b]

```

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

1055
1056
1057
1058
1059
1060
1061
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 1055

def all_literals_when? exp
  if array? exp[1] # pretty sure this is always true
    all_literals? exp[1] or # simple list, not actually array
      (splat_array? exp[1][1] and
       all_literals? exp[1][1][1])
  end
end
```

    
  

    
      
  
### 
  
    #**array_detect_all_literals?**(exp)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

904
905
906
907
908
909
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 904

def array_detect_all_literals? exp
  call? exp and
  [:detect, :find].include? exp.method and
  exp.first_arg.nil? and
  (all_literals? exp.target or dir_glob? exp.target)
end
```

    
  

    
      
  
### 
  
    #**array_include_all_literals?**(exp)  ⇒ Boolean 
  

  

  

  
    

Check if exp is a call to Array#include? on an array literal that contains all literal values. For example:

```
[1, 2, "a"].include? x

```

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

898
899
900
901
902
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 898

def array_include_all_literals? exp
  call? exp and
  exp.method == :include? and
  (all_literals? exp.target or dir_glob? exp.target)
end
```

    
  

    
      
  
### 
  
    #**assign_args**(method_exp, args, meth_env = SexpProcessor::Environment.new)  ⇒ Object 
  

  

  

  
    
      

```

1311
1312
1313
1314
1315
1316
1317
1318
1319
1320
1321
1322
1323
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 1311

def assign_args method_exp, args, meth_env = SexpProcessor::Environment.new
  formal_args = method_exp.formal_args

  formal_args.each_with_index do |arg, index|
    next if index == 0

    if arg.is_a? Symbol and sexp? args[index - 1]
      meth_env[Sexp.new(:lvar, arg)] = args[index - 1]
    end
  end

  meth_env
end
```

    
  

    
      
  
### 
  
    #**collapse_send_call**(exp, first_arg)  ⇒ Object 
  

  

  

  
    

Change x.send(:y, 1) to x.y(1)

  

  

  
    
      

```

1174
1175
1176
1177
1178
1179
1180
1181
1182
1183
1184
1185
1186
1187
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 1174

def collapse_send_call exp, first_arg
  # Handle try(&:id)
  if node_type? first_arg, :block_pass
    first_arg = first_arg[1]
  end

  return unless symbol? first_arg or string? first_arg
  exp.method = first_arg.value.to_sym
  args = exp.args
  exp.pop # remove last arg
  if args.length > 1
    exp.arglist = args.sexp_body
  end
end
```

    
  

    
      
  
### 
  
    #**duplicate?**(exp)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

1334
1335
1336
1337
1338
1339
1340
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 1334

def duplicate? exp
  @exp_context[0..-2].reverse_each do |e|
    return true if exp == e
  end

  false
end
```

    
  

    
      
  
### 
  
    #**early_return?**(exp)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

1023
1024
1025
1026
1027
1028
1029
1030
1031
1032
1033
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 1023

def early_return? exp
  return true if node_type? exp, :return
  return true if call? exp and [:fail, :raise].include? exp.method

  if node_type? exp, :block, :rlist
    node_type? exp.last, :return or
      (call? exp and [:fail, :raise].include? exp.method)
  else
    false
  end
end
```

    
  

    
      
  
### 
  
    #**equality_check?**(exp)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

1035
1036
1037
1038
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 1035

def equality_check? exp
  call? exp and
    exp.method == :==
end
```

    
  

    
      
  
### 
  
    #**find_method**(*args)  ⇒ Object 
  

  

  

  
    
      

```

1342
1343
1344
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 1342

def find_method *args
  nil
end
```

    
  

    
      
  
### 
  
    #**find_push_target**(exp)  ⇒ Object 
  

  

  

  
    

Finds the inner most call target which is not the target of a call to <<

  

  

  
    
      

```

1326
1327
1328
1329
1330
1331
1332
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 1326

def find_push_target exp
  if call? exp and exp.method == :<<
    find_push_target exp.target
  else
    exp
  end
end
```

    
  

    
      
  
### 
  
    #**get_call_value**(call)  ⇒ Object 
  

  

  

  
    
      

```

1226
1227
1228
1229
1230
1231
1232
1233
1234
1235
1236
1237
1238
1239
1240
1241
1242
1243
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 1226

def get_call_value call
  method_name = call.method

  #Look for helper methods and see if we can get a return value
  if found_method = tracker.find_method(method_name, @current_class)
    helper = found_method.src

    if sexp? helper
      value = process_helper_method helper, call.args
      value.line(call.line)
      return value
    else
      raise "Unexpected value for method: #{found_method}"
    end
  else
    call
  end
end
```

    
  

    
      
  
### 
  
    #**get_rhs**(exp)  ⇒ Object 
  

  

  

  
    

Handles x = y = z = 1

  

  

  
    
      

```

556
557
558
559
560
561
562
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 556

def get_rhs exp
  if node_type? exp, :lasgn, :iasgn, :gasgn, :attrasgn, :safe_attrasgn, :cvdecl, :cdecl
    get_rhs(exp.rhs)
  else
    exp
  end
end
```

    
  

    
      
  
### 
  
    #**hash_include_all_literals?**(exp)  ⇒ Boolean 
  

  

  

  
    

Check if exp is a call to Hash#include? on a hash literal that contains all literal values. For example:

```
{x: 1}.include? x

```

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

926
927
928
929
930
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 926

def hash_include_all_literals? exp
  call? exp and
  exp.method == :include? and
  all_literals? exp.target, :hash
end
```

    
  

    
      
  
### 
  
    #**hash_or_array_include_all_literals?**(exp)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

881
882
883
884
885
886
887
888
889
890
891
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 881

def hash_or_array_include_all_literals? exp
  return unless call? exp and sexp? exp.target
  target = exp.target

  case target.node_type
  when :hash
    hash_include_all_literals? exp
  else
    array_include_all_literals? exp
  end
end
```

    
  

    
      
  
### 
  
    #**in_array_all_literals?**(exp)  ⇒ Boolean 
  

  

  

  
    

Check if exp is a call to Array#include? on an array literal that contains all literal values. For example:

```
x.in? [1, 2, "a"]

```

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

916
917
918
919
920
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 916

def in_array_all_literals? exp
  call? exp and
    exp.method == :in? and
    all_literals? exp.first_arg
end
```

    
  

    
      
  
### 
  
    #**join_item**(item, join_value)  ⇒ Object 
  

  

  

  
    
      

```

421
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
# File 'lib/brakeman/processors/alias_processor.rb', line 421

def join_item item, join_value
  if item.nil? || item.is_a?(String)
    "#{item}#{join_value}"
  elsif string? item or symbol? item or number? item
    s(:str, "#{item.value}#{join_value}").line(item.line)
  else
    s(:evstr, item).line(item.line)
  end
end
```

    
  

    
      
  
### 
  
    #**merge_if_branch**(branch_env)  ⇒ Object 
  

  

  

  
    
      

```

1145
1146
1147
1148
1149
1150
1151
1152
1153
1154
1155
1156
1157
1158
1159
1160
1161
1162
1163
1164
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 1145

def merge_if_branch branch_env
  branch_env.each do |k, v|
    next if v.nil?

    current_val = env[k]

    if current_val
      unless same_value?(current_val, v)
        if too_deep? current_val
          # Give up branching, start over with latest value
          env[k] = v
        else
          env[k] = current_val.combine(v, k.line)
        end
      end
    else
      env[k] = v
    end
  end
end
```

    
  

    
      
  
### 
  
    #**meth_env**  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 535

def meth_env
  begin
    env.scope do
      set_env_defaults
      @meth_env = env.current
      yield
    end
  ensure
    @meth_env = nil
  end
end
```

    
  

    
      
  
### 
  
    #**new_string?**(exp)  ⇒ Boolean 
  

  

  

  
    

String.new ?

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

1447
1448
1449
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 1447

def new_string? exp
  exp == STRING_NEW
end
```

    
  

    
      
  
### 
  
    #**only_ivars**(include_request_vars = false, lenv = nil)  ⇒ Object 
  

  

  

  
    

Returns a new SexpProcessor::Environment containing only instance variables. This is useful, for example, when processing views.

  

  

  
    
      

```

1191
1192
1193
1194
1195
1196
1197
1198
1199
1200
1201
1202
1203
1204
1205
1206
1207
1208
1209
1210
1211
1212
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 1191

def only_ivars include_request_vars = false, lenv = nil
  lenv ||= env
  res = SexpProcessor::Environment.new

  if include_request_vars
    lenv.all.each do |k, v|
      #TODO Why would this have nil values?
      if (k.node_type == :ivar or request_value? k) and not v.nil?
        res[k] = v.dup
      end
    end
  else
    lenv.all.each do |k, v|
      #TODO Why would this have nil values?
      if k.node_type == :ivar and not v.nil?
        res[k] = v.dup
      end
    end
  end

  res
end
```

    
  

    
      
  
### 
  
    #**only_request_vars**  ⇒ Object 
  

  

  

  
    
      

```

1214
1215
1216
1217
1218
1219
1220
1221
1222
1223
1224
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 1214

def only_request_vars
  res = SexpProcessor::Environment.new

  env.all.each do |k, v|
    if request_value? k and not v.nil?
      res[k] = v.dup
    end
  end

  res
end
```

    
  

    
      
  
### 
  
    #**process_array_join**(array, join_str)  ⇒ Object 
  

  

  

  
    

Painful conversion of Array#join into string interpolation

  

  

  
    
      

```

356
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
392
393
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
419
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 356

def process_array_join array, join_str
  # Empty array
  if array.length == 1
    return s(:str, '').line(array.line)
  end

  result = s().line(array.line)

  join_value = if string? join_str
                 join_str.value
               else
                 nil
               end

  if array.length > 2
    array[1..-2].each do |e|
      result << join_item(e, join_value)
    end
  end

  result << join_item(array.last, nil)

  # Combine the strings at the beginning because that's what RubyParser does
  combined_first = +""
  result.each do |e|
    if string? e
      combined_first << e.value
    elsif e.is_a? String
      combined_first << e
    else
      break
    end
  end

  # Remove the strings at the beginning
  result.reject! do |e|
    if e.is_a? String or string? e
      true
    else
      break
    end
  end

  result.unshift combined_first

  # Have to fix up strings that follow interpolation
  string = result.reduce(s(:dstr).line(array.line)) do |memo, e|
    if string? e and node_type? memo.last, :evstr
      e.value = "#{join_value}#{e.value}"
    elsif join_value and node_type? memo.last, :evstr and node_type? e, :evstr
      memo << s(:str, join_value).line(e.line)
    end

    memo << e
  end

  # Convert (:dstr, "hello world")
  # to (:str, "hello world")
  if string.length == 2 and string.last.is_a? String
    string[0] = :str
  end

  string
end
```

    
  

    
      
  
### 
  
    #**process_attrasgn**(exp)  ⇒ Object 
  

  

  

  
    

‘Attribute’ assignment x.y = 1 or x = 1

  

  

  
    
      

```

635
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
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 635

def process_attrasgn exp
  tar_variable = exp.target
  target = process(exp.target)
  method = exp.method
  index_arg = exp.first_arg
  value_arg = exp.second_arg

  if method == :[]=
    index = exp.first_arg = process(index_arg)
    value = exp.second_arg = process(value_arg)
    match = Sexp.new(:call, target, :[], index)

    set_value match, value

    if hash? target
      env[tar_variable] = hash_insert target.deep_clone, index, value
    end

    unless node_type? target, :hash
      exp.target = target
    end
  elsif method.to_s[-1,1] == "="
    exp.first_arg = process(index_arg)
    value = get_rhs(exp)
    #This is what we'll replace with the value
    match = Sexp.new(:call, target, method.to_s[0..-2].to_sym)

    set_value match, value
    exp.target = target
  else
    raise "Unrecognized assignment: #{exp}"
  end
  exp
end
```

    
  

    
      
  
### 
  
    #**process_block**(exp)  ⇒ Object 
  

  

  

  
    

Start new scope for block.

  

  

  
    
      

```

521
522
523
524
525
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 521

def process_block exp
  env.scope do
    process_default exp
  end
end
```

    
  

    
      
  
### 
  
    #**process_bracket_call**(exp)  ⇒ Object 
  

  

  

  
    
      

```

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
110
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
137
138
139
140
141
142
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
165
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 99

def process_bracket_call exp
  # TODO: What is even happening in this method?
  r = replace(exp)

  if r != exp
    return r
  end

  exp.arglist = process_default(exp.arglist)

  r = replace(exp)

  if r != exp
    return r
  end

  t = process(exp.target.deep_clone)

  # sometimes t[blah] has a match in the env
  # but we don't want to actually set the target
  # in case the target is big...which is what this
  # whole method is trying to avoid
  if t != exp.target
    e = exp.deep_clone
    e.target = t

    r = replace(e)

    if r != e
      return r
    end
  else
    t = exp.target # put it back?
  end

  if hash? t
    if v = process_hash_access(t, exp.first_arg)
      v.deep_clone(exp.line)
    else
      case t.node_type
      when :params
        exp.target = PARAMS_SEXP.deep_clone(exp.target.line)
      when :session
        exp.target = SESSION_SEXP.deep_clone(exp.target.line)
      when :cookies
        exp.target = COOKIES_SEXP.deep_clone(exp.target.line)
      end

      exp
    end
  elsif array? t
    if v = process_array_access(t, exp.args)
      v.deep_clone(exp.line)
    else
      exp
    end
  elsif t
    exp.target = t
    exp
  else
    if exp.target # `self` target is reported as `nil` https://github.com/seattlerb/ruby_parser/issues/250
      exp.target = process_default exp.target
    end

    exp
  end
end
```

    
  

    
      
  
### 
  
    #**process_branch_with_value**(var, value, branch, branch_index)  ⇒ Object 
  

  

  

  
    
      

```

1015
1016
1017
1018
1019
1020
1021
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 1015

def process_branch_with_value var, value, branch, branch_index
  previous_value = env.current[var]
  env.current[var] = value
  result = process_if_branch branch
  env.current[var] = previous_value
  result
end
```

    
  

    
      
  
### 
  
    #**process_call**(exp)  ⇒ Object 
  

  

  

  
    

Process a method call.

  

  

  
    
      

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
291
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
332
333
334
335
336
337
338
339
340
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
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 173

def process_call exp
  return exp if process_call_defn? exp
  target_var = exp.target
  target_var &&= target_var.deep_clone
  if exp.node_type == :safe_call
    exp.node_type = :call
  end

  if exp.method == :[]
    return process_bracket_call exp
  else
    exp = process_default exp
  end

  #In case it is replaced with something else
  unless call? exp
    return exp
  end

  # If x(*[1,2,3]) change to x(1,2,3)
  # if that's the only argument
  if splat_array? exp.first_arg and exp.second_arg.nil?
    exp.arglist = exp.first_arg[1].sexp_body
  end

  target = exp.target
  method = exp.method
  first_arg = exp.first_arg

  if method == :send or method == :__send__ or method == :try
    collapse_send_call exp, first_arg
  end

  if node_type? target, :or and [:+, :-, :*, :/].include? method
    res = process_or_simple_operation(exp)
    return res if res
  elsif target == ARRAY_CONST and method == :new
    return Sexp.new(:array, *exp.args).line(exp.line)
  elsif target == HASH_CONST and method == :new and first_arg.nil? and !node_type?(@exp_context.last, :iter)
    return Sexp.new(:hash).line(exp.line)
  elsif exp == RAILS_TEST or exp == RAILS_DEV
    return Sexp.new(:false).line(exp.line)
  end

  # For the simplest case of `Foo.thing`
  if node_type? target, :const and first_arg.nil?
    if tracker and (klass = tracker.find_class(class_name(target.value)))
      if return_value = klass.get_simple_method_return_value(:class, method)
        return return_value.deep_clone(exp.line)
      end
    end
  end

  #See if it is possible to simplify some basic cases
  #of addition/concatenation.
  case method
  when :+
    if array? target and array? first_arg
      exp = join_arrays(target, first_arg, exp)
    elsif string? first_arg
      exp = join_strings(target, first_arg, exp)
    elsif number? first_arg
      exp = math_op(:+, target, first_arg, exp)
    end
  when :-, :*, :/
    if method == :* and array? target
      if string? first_arg
        exp = process_array_join(target, first_arg)
      end
    else
      exp = math_op(method, target, first_arg, exp)
    end
  when :[]
    # TODO: This might never be used because of process_bracket_call above
    if array? target
      exp = process_array_access(target, exp.args, exp)
    elsif hash? target
      exp = process_hash_access(target, first_arg, exp)
    end
  when :fetch
    if array? target
      # Not dealing with default value
      # so just pass in first argument, but process_array_access expects
      # an array of arguments.
      exp = process_array_access(target, [first_arg], exp)
    elsif hash? target
      exp = process_hash_access(target, first_arg, exp)
    end
  when :merge!, :update
    if hash? target and hash? first_arg
       target = process_hash_merge! target, first_arg
       env[target_var] = target
       return target
    end
  when :merge
    if hash? target and hash? first_arg
      return process_hash_merge(target, first_arg)
    end
  when :<<
    if string? target and string? first_arg
      target.value += first_arg.value
      env[target_var] = target
      return target
    elsif string? target and string_interp? first_arg
      exp = Sexp.new(:dstr, target.value + first_arg[1]).concat(first_arg.sexp_body(2)).line(exp.line)
      env[target_var] = exp
    elsif string? first_arg and string_interp? target
      if string? target.last
        target.last.value += first_arg.value
      elsif target.last.is_a? String
        # TODO Use target.last += ?
        target.last << first_arg.value
      else
        target << first_arg
      end
      env[target_var] = target
      return first_arg
    elsif new_string? target
      env[target_var] = first_arg
      return first_arg
    elsif array? target
      target << first_arg
      env[target_var] = target
      return target
    else
      target = find_push_target(target_var)
      env[target] = exp unless target.nil? # Happens in TemplateAliasProcessor
    end
  when :push
    if array? target
      target << first_arg
      env[target_var] = target
      return target
    end
  when :first
    if array? target and first_arg.nil? and sexp? target[1]
      exp = target[1]
    end
  when :freeze, :dup, :presence
    unless target.nil?
      exp = target
    end
  when :join
    if array? target and (string? first_arg or first_arg.nil?)
      exp = process_array_join(target, first_arg)
    end
  when :!
    #  Convert `!!a` to boolean
    if call? target and target.method == :!
      exp = s(:or, s(:true).line(exp.line), s(:false).line(exp.line)).line(exp.line)
    end
  when :values
    # Hash literal
    if node_type? target, :hash
      exp = hash_values(target)
    end
  when :values_at
    if node_type? target, :hash
      res = hash_values_at target, exp.args

      # Only convert to array of values if _all_ keys
      # are present in the hash.
      unless res.any?(&:nil?)
        exp = res
      end
    end
  when :presence_in
    arg = exp.first_arg

    if node_type? arg, :array
      # 1.presence_in [1,2,3]
      if arg.include? target
        exp = target
      elsif all_literals? arg
        exp = safe_literal(exp.line)
      end
    end
  end

  exp
end
```

    
  

    
      
  
### 
  
    #**process_case**(exp)  ⇒ Object 
  

  

  

  
    
      

```

1063
1064
1065
1066
1067
1068
1069
1070
1071
1072
1073
1074
1075
1076
1077
1078
1079
1080
1081
1082
1083
1084
1085
1086
1087
1088
1089
1090
1091
1092
1093
1094
1095
1096
1097
1098
1099
1100
1101
1102
1103
1104
1105
1106
1107
1108
1109
1110
1111
1112
1113
1114
1115
1116
1117
1118
1119
1120
1121
1122
1123
1124
1125
1126
1127
1128
1129
1130
1131
1132
1133
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 1063

def process_case exp
  if @ignore_ifs.nil?
    @ignore_ifs = @tracker && @tracker.options[:ignore_ifs]
  end

  if @ignore_ifs
    process_default exp
    return exp
  end

  branch_scopes = []
  was_inside = @inside_if
  @inside_if = true

  exp[1] = process exp[1] if exp[1]

  case_value = if node_type? exp[1], :lvar, :ivar, :call
    exp[1].deep_clone
  end

  exp.each_sexp do |e|
    if node_type? e, :when
      scope do
        # Process the when value for matching
        process_default e[1]

        # Moved here to avoid @branch_env being cleared out
        # in process_default
        # Maybe in the future don't set it to nil?
        @branch_env = env.current

        # set value of case var if possible
        if case_value
          if simple_when? e
            @branch_env[case_value] = e[1][1]
          elsif all_literals_when? e
            @branch_env[case_value] = safe_literal(e.line + 1)
          end
        end

        # when blocks aren't blocks, they are lists of expressions
        process_default e

        branch_scopes << env.current

        @branch_env = nil
      end
    end
  end

  # else clause
  if sexp? exp.last
    scope do
      @branch_env = env.current

      process_default exp[-1]

      branch_scopes << env.current

      @branch_env = nil
    end
  end

  @inside_if = was_inside

  branch_scopes.each do |s|
    merge_if_branch s
  end

  exp
end
```

    
  

    
      
  
### 
  
    #**process_cdecl**(exp)  ⇒ Object 
  

  

  

  
    

Constant assignments like BIG_CONSTANT = 234810983

  

  

  
    
      

```

856
857
858
859
860
861
862
863
864
865
866
867
868
869
870
871
872
873
874
875
876
877
878
879
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 856

def process_cdecl exp
  if sexp? exp.rhs
    exp.rhs = process exp.rhs
  end

  if @tracker
    @tracker.add_constant exp.lhs,
      exp.rhs,
      :file => @current_file,
      :module => @current_module,
      :class => @current_class,
      :method => @current_method
  end

  if exp.lhs.is_a? Symbol
    match = Sexp.new(:const, exp.lhs)
  else
    match = exp.lhs
  end

  env[match] = get_rhs(exp)

  exp
end
```

    
  

    
      
  
### 
  
    #**process_cvdecl**(exp)  ⇒ Object 
  

  

  

  
    

Class variable assignment @@x = 1

  

  

  
    
      

```

621
622
623
624
625
626
627
628
629
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 621

def process_cvdecl exp
  match = Sexp.new(:cvar, exp.lhs)
  exp.rhs = process(exp.rhs)
  value = get_rhs(exp)

  set_value match, value

  exp
end
```

    
  

    
      
  
### 
  
    #**process_default**(exp)  ⇒ Object 
  

  

  

  
    

Process a Sexp. If the Sexp has a value associated with it in the environment, that value will be returned.

  

  

  
    
      

```

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
80
81
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 57

def process_default exp
  @exp_context.push exp

  begin
    exp.map! do |e|
      if sexp? e and not e.empty?
        process e
      else
        e
      end
    end
  rescue => err
    if @tracker
      @tracker.error err
    else
      raise err
    end
  end

  result = replace(exp)

  @exp_context.pop

  result
end
```

    
  

    
      
  
### 
  
    #**process_defn**(exp)  ⇒ Object 
  

  

  

  
    

Process a method definition.

  

  

  
    
      

```

528
529
530
531
532
533
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 528

def process_defn exp
  meth_env do
    exp.body = process_all! exp.body
  end
  exp
end
```

    
  

    
      
  
### 
  
    #**process_defs**(exp)  ⇒ Object 
  

  

  

  
    

Process a method definition on self.

  

  

  
    
      

```

548
549
550
551
552
553
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 548

def process_defs exp
  meth_env do
    exp.body = process_all! exp.body
  end
  exp
end
```

    
  

    
      
  
### 
  
    #**process_gasgn**(exp)  ⇒ Object 
  

  

  

  
    

Global assignment $x = 1

  

  

  
    
      

```

605
606
607
608
609
610
611
612
613
614
615
616
617
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 605

def process_gasgn exp
  match = Sexp.new(:gvar, exp.lhs)
  exp.rhs = process(exp.rhs)
  value = get_rhs(exp)

  if value
    value.line = exp.line

    set_value match, value
  end

  exp
end
```

    
  

    
      
  
### 
  
    #**process_hash**(exp)  ⇒ Object 
  

  

  

  
    
      

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
748
749
750
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
762
763
764
765
766
767
768
769
770
771
772
773
774
775
776
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 737

def process_hash exp
  exp = process_default(exp)

  # Handle { **kw }
  if node_type? exp, :hash
    if exp.any? { |e| node_type? e, :kwsplat and node_type? e.value, :hash }
      kwsplats, rest = exp.partition { |e| node_type? e, :kwsplat and node_type? e.value, :hash }
      exp = Sexp.new.concat(rest).line(exp.line)

      kwsplats.each do |e|
        exp = process_hash_merge! exp, e.value
      end
    end
  end

  # Return early unless there might be short-hand syntax,
  # since handling it is kind of expensive.
  return exp unless exp.any? { |e| e.nil? }

  # Need to handle short-hand hash syntax
  new_hash = [:hash]
  hash_iterate(exp) do |key, value|
    # e.g. { a: }
    if value.nil? and symbol? key
      # Only handling local variables for now, not calls
      lvar = s(:lvar, key.value)
      if var_value = env[lvar]
        new_hash << key << var_value.deep_clone(key.line || 0)
      else
        # If the value is unknown, assume it was a call
        # and set the value to a call
        new_hash.concat << key << s(:call, nil, key.value).line(key.line || 0)
      end
    else
      new_hash.concat << key << value
    end
  end

  Sexp.from_array(new_hash).line(exp.line || 0)
end
```

    
  

    
      
  
### 
  
    #**process_hash_merge**(hash, args)  ⇒ Object 
  

  

  

  
    

Return a new hash Sexp with the given values merged into it.

`args` should be a hash Sexp as well.

  

  

  
    
      

```

794
795
796
797
798
799
800
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 794

def process_hash_merge hash, args
  hash = hash.deep_clone
  hash_iterate args do |key, replacement|
    hash_insert hash, key, replacement
  end
  hash
end
```

    
  

    
      
  
### 
  
    #**process_hash_merge!**(hash, args)  ⇒ Object 
  

  

  

  
    

Merge values into hash when processing

h.merge! :something => “value”

  

  

  
    
      

```

781
782
783
784
785
786
787
788
789
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 781

def process_hash_merge! hash, args
  hash = hash.deep_clone
  hash_iterate args do |key, replacement|
    hash_insert hash, key, replacement
    match = Sexp.new(:call, hash, :[], key)
    env[match] = replacement
  end
  hash
end
```

    
  

    
      
  
### 
  
    #**process_helper_method**(method_exp, args)  ⇒ Object 
  

  

  

  
    
      

```

1245
1246
1247
1248
1249
1250
1251
1252
1253
1254
1255
1256
1257
1258
1259
1260
1261
1262
1263
1264
1265
1266
1267
1268
1269
1270
1271
1272
1273
1274
1275
1276
1277
1278
1279
1280
1281
1282
1283
1284
1285
1286
1287
1288
1289
1290
1291
1292
1293
1294
1295
1296
1297
1298
1299
1300
1301
1302
1303
1304
1305
1306
1307
1308
1309
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 1245

def process_helper_method method_exp, args
  method_name = method_exp.method_name
  Brakeman.debug "Processing method #{method_name}"

  info = @helper_method_info[method_name]

  #If method uses instance variables, then include those and request
  #variables (params, etc) in the method environment. Otherwise,
  #only include request variables.
  if info[:uses_ivars]
    meth_env = only_ivars(:include_request_vars)
  else
    meth_env = only_request_vars
  end

  #Add arguments to method environment
  assign_args method_exp, args, meth_env

  #Find return values if method does not depend on environment/args
  values = @helper_method_cache[method_name]

  unless values
    #Serialize environment for cache key
    meth_values = meth_env.instance_variable_get(:@env).to_a
    meth_values.sort!
    meth_values = meth_values.to_s

    digest = Digest::SHA1.new.update(meth_values << method_name.to_s).to_s.to_sym

    values = @helper_method_cache[digest]
  end

  if values
    #Use values from cache
    values[:ivar_values].each do |var, val|
      env[var] = val
    end

    values[:return_value]
  else
    #Find return value for method
    frv = Brakeman::FindReturnValue.new
    value = frv.get_return_value(method_exp.body_list, meth_env)

    ivars = {}

    only_ivars(false, meth_env).all.each do |var, val|
      env[var] = val
      ivars[var] = val
    end

    if not frv.uses_ivars? and args.length == 0
      #Store return value without ivars and args if they are not used
      @helper_method_cache[method_exp.method_name] = { :return_value => value, :ivar_values => ivars }
    else
      @helper_method_cache[digest] = { :return_value => value, :ivar_values => ivars }
    end

    #Store information about method, just ivar usage for now
    @helper_method_info[method_name] = { :uses_ivars => frv.uses_ivars? }

    value
  end
end
```

    
  

    
      
  
### 
  
    #**process_iasgn**(exp)  ⇒ Object 
  

  

  

  
    

Instance variable assignment

  

  

  
    
      

```

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
597
598
599
600
601
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 585

def process_iasgn exp
  self_assign = self_assign?(exp.lhs, exp.rhs)
  exp.rhs = process exp.rhs
  ivar = Sexp.new(:ivar, exp.lhs).line(exp.line)

  if self_assign
    if env[ivar].nil? and @meth_env
      @meth_env[ivar] = get_rhs(exp)
    else
      env[ivar] = get_rhs(exp)
    end
  else
    set_value ivar, get_rhs(exp)
  end

  exp
end
```

    
  

    
      
  
### 
  
    #**process_if**(exp)  ⇒ Object 
  

  

  

  
    

Sets @inside_if = true

  

  

  
    
      

```

933
934
935
936
937
938
939
940
941
942
943
944
945
946
947
948
949
950
951
952
953
954
955
956
957
958
959
960
961
962
963
964
965
966
967
968
969
970
971
972
973
974
975
976
977
978
979
980
981
982
983
984
985
986
987
988
989
990
991
992
993
994
995
996
997
998
999
1000
1001
1002
1003
1004
1005
1006
1007
1008
1009
1010
1011
1012
1013
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 933

def process_if exp
  if @ignore_ifs.nil?
    @ignore_ifs = @tracker && @tracker.options[:ignore_ifs]
  end

  condition = exp.condition = process exp.condition

  #Check if a branch is obviously going to be taken
  if true? condition
    no_branch = true
    exps = [exp.then_clause, nil]
  elsif false? condition
    no_branch = true
    exps = [nil, exp.else_clause]
  elsif equality_check? condition and condition.target == condition.first_arg
    no_branch = true
    exps = [exp.then_clause, nil]
  else
    no_branch = false
    exps = [exp.then_clause, exp.else_clause]
  end

  if @ignore_ifs or no_branch
    exps.each_with_index do |branch, i|
      exp[2 + i] = process_if_branch branch
    end
  else
    # Translate `if !...` into `unless ...`
    # Technically they are different but that's only if someone overrides `!`
    if call? condition and condition.method == :!
      condition = condition.target
      exps.reverse!
    end

    was_inside = @inside_if
    @inside_if = true

    branch_scopes = []
    exps.each_with_index do |branch, i|
      scope do
        @branch_env = env.current
        branch_index = 2 + i # s(:if, condition, then_branch, else_branch)
       exp[branch_index] = if i == 0 and hash_or_array_include_all_literals? condition
          # If the condition is ["a", "b"].include? x
          # set x to safe_literal inside the true branch
          var = condition.first_arg
          value = safe_literal(var.line)
          process_branch_with_value(var, value, branch, i)
        elsif i == 0 and in_array_all_literals? condition
          # If the condition is x.in? ["a", "b"]
          # set x to safe_literal inside the true branch
          var = condition.target
          value = safe_literal(var.line)
          process_branch_with_value(var, value, branch, i)
        elsif i == 0 and equality_check? condition
          # For conditions like a == b,
          # set a to b inside the true branch
          var = condition.target
          value = condition.first_arg
          process_branch_with_value(var, value, branch, i)
        elsif i == 1 and hash_or_array_include_all_literals? condition and early_return? branch
          var = condition.first_arg
          env.current[var] = safe_literal(var.line)
          process_if_branch branch
        else
          process_if_branch branch
        end
        branch_scopes << env.current
        @branch_env = nil
      end
    end

    @inside_if = was_inside

    branch_scopes.each do |s|
      merge_if_branch s
    end
  end

  exp
end
```

    
  

    
      
  
### 
  
    #**process_if_branch**(exp)  ⇒ Object 
  

  

  

  
    
      

```

1135
1136
1137
1138
1139
1140
1141
1142
1143
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 1135

def process_if_branch exp
  if sexp? exp
    if block? exp
      process_default exp
    else
      process exp
    end
  end
end
```

    
  

    
      
  
### 
  
    #**process_iter**(exp)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 454

def process_iter exp
  @exp_context.push exp
  exp[1] = process exp.block_call
  if array_detect_all_literals? exp[1]
    return safe_literal(exp.line)
  end

  @exp_context.pop

  env.scope do
    call = exp.block_call
    block_args = exp.block_args

    if call? call and [:each, :map].include? call.method and all_literals? call.target and block_args.length == 2 and block_args.last.is_a? Symbol
      # Iterating over an array of all literal values
      local = Sexp.new(:lvar, block_args.last)
      env.current[local] = safe_literal(exp.line)
    elsif temp_file_open? call
      local = Sexp.new(:lvar, block_args.last)
      env.current[local] = temp_file_new(exp.line)
    elsif temp_file_create? call
      local = Sexp.new(:lvar, block_args.last)
      env.current[local] = temp_file_new(exp.line)
    else
      block_args.each do |e|
        #Force block arg(s) to be local
        if node_type? e, :lasgn
          env.current[Sexp.new(:lvar, e.lhs)] = Sexp.new(:lvar, e.lhs)
        elsif node_type? e, :kwarg
          env.current[Sexp.new(:lvar, e[1])] = e[2]
        elsif node_type? e, :masgn, :shadow
          e[1..-1].each do |var|
            local = Sexp.new(:lvar, var)
            env.current[local] = local
          end
        elsif e.is_a? Symbol
          local = Sexp.new(:lvar, e)
          env.current[local] = local
        elsif e.nil? # trailing comma, argument destructuring
          next # Punt for now
        else
          raise "Unexpected value in block args: #{e.inspect}"
        end
      end
    end

    block = exp.block

    if block? block
      process_all! block
    else
      exp[3] = process block
    end
  end

  exp
end
```

    
  

    
      
  
### 
  
    #**process_lasgn**(exp)  ⇒ Object 
  

  

  

  
    

Local assignment x = 1

  

  

  
    
      

```

566
567
568
569
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
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 566

def process_lasgn exp
  self_assign = self_assign?(exp.lhs, exp.rhs)
  exp.rhs = process exp.rhs if sexp? exp.rhs
  return exp if exp.rhs.nil?

  local = Sexp.new(:lvar, exp.lhs).line(exp.line || -2)

  if self_assign
    # Skip branching
    env[local] = get_rhs(exp)
  else
    set_value local, get_rhs(exp)
  end

  exp
end
```

    
  

    
      
  
### 
  
    #**process_masgn**(exp)  ⇒ Object 
  

  

  

  
    

Multiple/parallel assignment:

x, y = z, w

  

  

  
    
      

```

673
674
675
676
677
678
679
680
681
682
683
684
685
686
687
688
689
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
703
704
705
706
707
708
709
710
711
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
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 673

def process_masgn exp
  exp[2] = process exp[2] if sexp? exp[2]

  if node_type? exp[2], :to_ary and array? exp[2][1]
    exp[2] = exp[2][1]
  end

  unless array? exp[1] and array? exp[2]
    # Already processed RHS, don't do it again
    # https://github.com/presidentbeef/brakeman/issues/1877
    return exp
  end

  vars = exp[1].dup
  vals = exp[2].dup

  vars.shift
  vals.shift

  # Call each assignment as if it is normal
  vars.each_with_index do |var, i|
    val = vals[i]
    next unless val # TODO: Break if there are no vals left?

    # This happens with nested destructuring like
    #   x, (a, b) = blah
    if node_type? var, :masgn
      # Need to add value to masgn exp
      m = var.dup
      m[2] = s(:to_ary, val)

      process_masgn m
    elsif node_type? var, :splat
      # Assign the rest of the values to the variable:
      #
      #   a, *b = 1, 2, 3
      #
      #   b == [2, 3]

      assign = var[1].dup # var is s(:splat, s(:lasgn, :b))

      if i == vars.length - 1 # Last variable being assigned, slurp up the rest
        assign.rhs = s(:array, *vals[i..]) # val is the "rest" of the values
      else
        # Calculate how many values to assign based on how many variables
        # there are.
        #
        # If there are more values than variables, the splat gets an empty array.

        assign.rhs = s(:array, *vals[i, (vals.length - vars.length + 1)]).line(vals.line)
      end

      process assign
    else
      assign = var.dup
      assign.rhs = val
      process assign
    end
  end

  exp
end
```

    
  

    
      
  
### 
  
    #**process_op_asgn1**(exp)  ⇒ Object 
  

  

  

  
    

Assignments like this x ||= 1

  

  

  
    
      

```

804
805
806
807
808
809
810
811
812
813
814
815
816
817
818
819
820
821
822
823
824
825
826
827
828
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 804

def process_op_asgn1 exp
  target_var = exp[1]
  target_var &&= target_var.deep_clone

  target = exp[1] = process(exp[1])
  index = exp[2][1] = process(exp[2][1])
  value = exp[4] = process(exp[4])
  match = Sexp.new(:call, target, :[], index)

  if exp[3] == :"||"
    unless env[match]
      if request_value? target
        env[match] = match.combine(value)
      else
        env[match] = value
      end
    end
  else
    new_value = process s(:call, s(:call, target_var, :[], index), exp[3], value).line(exp.line)

    env[match] = new_value
  end

  exp
end
```

    
  

    
      
  
### 
  
    #**process_op_asgn2**(exp)  ⇒ Object 
  

  

  

  
    

Assignments like this x.y ||= 1

  

  

  
    
      

```

832
833
834
835
836
837
838
839
840
841
842
843
844
845
846
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 832

def process_op_asgn2 exp
  return process_default(exp) if exp[3] != :"||"

  target = exp[1] = process(exp[1])
  value = exp[4] = process(exp[4])
  method = exp[2]

  match = Sexp.new(:call, target, method.to_s[0..-2].to_sym)

  unless env[match]
    env[match] = value
  end

  exp
end
```

    
  

    
      
  
### 
  
    #**process_or_simple_operation**(exp)  ⇒ Object 
  

  

  

  
    

If possible, distribute operation over both sides of an or. For example,

```
(1 or 2) * 5

```

Becomes

```
(5 or 10)

```

Only works for strings and numbers right now.

  

  

  
    
      

```

1489
1490
1491
1492
1493
1494
1495
1496
1497
1498
1499
1500
1501
1502
1503
1504
1505
1506
1507
1508
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 1489

def process_or_simple_operation exp
  arg = exp.first_arg
  return nil unless string? arg or number? arg

  target = exp.target
  lhs = process_or_target(target.lhs, exp.dup)
  rhs = process_or_target(target.rhs, exp.dup)

  if lhs and rhs
    if same_value? lhs, rhs
      lhs
    else
      exp.target.lhs = lhs
      exp.target.rhs = rhs
      exp.target
    end
  else
    nil
  end
end
```

    
  

    
      
  
### 
  
    #**process_or_target**(value, copy)  ⇒ Object 
  

  

  

  
    
      

```

1510
1511
1512
1513
1514
1515
1516
1517
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 1510

def process_or_target value, copy
  if string? value or number? value
    copy.target = value
    process copy
  else
    false
  end
end
```

    
  

    
      
  
### 
  
    #**process_safely**(src, set_env = nil, current_file = @current_file)  ⇒ Object 
  

  

  

  
    

This method processes the given Sexp, but copies it first so the original argument will not be modified.

*set_env* should be an instance of SexpProcessor::Environment. If provided, it will be used as the starting environment.

This method returns a new Sexp with variables replaced with their values, where possible.

  

  

  
    
      

```

47
48
49
50
51
52
53
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 47

def process_safely src, set_env = nil, current_file = @current_file
  @current_file = current_file
  @env = set_env || SexpProcessor::Environment.new
  @result = src.deep_clone
  process @result
  @result
end
```

    
  

    
      
  
### 
  
    #**process_scope**(exp)  ⇒ Object 
  

  

  

  
    

Process a new scope.

  

  

  
    
      

```

513
514
515
516
517
518
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 513

def process_scope exp
  env.scope do
    process exp.block
  end
  exp
end
```

    
  

    
      
  
### 
  
    #**process_svalue**(exp)  ⇒ Object 
  

  

  

  
    

This is the right hand side value of a multiple assignment, like ‘x = y, z`

  

  

  
    
      

```

850
851
852
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 850

def process_svalue exp
  exp.value
end
```

    
  

    
      
  
### 
  
    #**raise?**(exp)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

1440
1441
1442
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 1440

def raise? exp
  call? exp and exp.method == :raise
end
```

    
  

    
      
  
### 
  
    #**replace**(exp, int = 0)  ⇒ Object 
  

  

  

  
    
      

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
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 83

def replace exp, int = 0
  return exp if int > 3

  if replacement = env[exp]
    if not duplicate? replacement and replacement.mass < @mass_limit
      replace(replacement.deep_clone(exp.line), int + 1)
    else
      exp
    end
  elsif tracker and replacement = tracker.constant_lookup(exp) and not duplicate? replacement
    replace(replacement.deep_clone(exp.line), int + 1)
  else
    exp
  end
end
```

    
  

    
      
  
### 
  
    #**same_value?**(lhs, rhs)  ⇒ Boolean 
  

  

  

  
    

Return true if lhs == rhs or lhs is an or expression and rhs is one of its values

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

1348
1349
1350
1351
1352
1353
1354
1355
1356
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 1348

def same_value? lhs, rhs
  if lhs == rhs
    true
  elsif node_type? lhs, :or
    lhs.rhs == rhs or lhs.lhs == rhs
  else
    false
  end
end
```

    
  

    
      
  
### 
  
    #**self_assign?**(var, value)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

1358
1359
1360
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 1358

def self_assign? var, value
  self_assign_var?(var, value) or self_assign_target?(var, value)
end
```

    
  

    
      
  
### 
  
    #**self_assign_target?**(var, value)  ⇒ Boolean 
  

  

  

  
    

Return true for x = x.blah

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

1371
1372
1373
1374
1375
1376
1377
1378
1379
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 1371

def self_assign_target? var, value
  target = top_target(value)

  if node_type? target, :lvar, :ivar
    target = target.value
  end

  var == target
end
```

    
  

    
      
  
### 
  
    #**self_assign_var?**(var, value)  ⇒ Boolean 
  

  

  

  
    

Return true if for x = blah or @x = blah

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

1363
1364
1365
1366
1367
1368
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 1363

def self_assign_var? var, value
  call? value and
  value.method == :+ and
  node_type? value.target, :lvar, :ivar and
  value.target.value == var
end
```

    
  

    
      
  
### 
  
    #**set_value**(var, value)  ⇒ Object 
  

  

  

  
    

Set variable to given value. Creates “branched” versions of values when appropriate. Avoids creating multiple branched versions inside same if branch.

  

  

  
    
      

```

1455
1456
1457
1458
1459
1460
1461
1462
1463
1464
1465
1466
1467
1468
1469
1470
1471
1472
1473
1474
1475
1476
1477
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 1455

def set_value var, value
  if node_type? value, :if
    value = value_from_if(value)
  elsif node_type? value, :case
    value = value_from_case(value)
  end

  if @ignore_ifs or not @inside_if
    if @meth_env and node_type? var, :ivar and env[var].nil?
      @meth_env[var] = value
    else
      env[var] = value
    end
  elsif env.current[var]
    env.current[var] = value
  elsif @branch_env and @branch_env[var]
    @branch_env[var] = value
  elsif @branch_env and @meth_env and node_type? var, :ivar
    @branch_env[var] = value
  else
    env.current[var] = value
  end
end
```

    
  

    
      
  
### 
  
    #**simple_when?**(exp)  ⇒ Boolean 
  

  

  

  
    

Not a list of values

```
when :example

```

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

1042
1043
1044
1045
1046
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 1042

def simple_when? exp
  node_type? exp[1], :array and
    exp[1].length == 2 and # only one element in the array
    not node_type? exp[1][1], :splat, :array
end
```

    
  

    
      
  
### 
  
    #**splat_array?**(exp)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

449
450
451
452
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 449

def splat_array? exp
  node_type? exp, :splat and
    node_type? exp[1], :array
end
```

    
  

    
      
  
### 
  
    #**temp_file_create?**(exp)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

439
440
441
442
443
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 439

def temp_file_create? exp
  call? exp and
    exp.target == TEMP_FILE_CLASS and
    exp.method == :create
end
```

    
  

    
      
  
### 
  
    #**temp_file_new**(line)  ⇒ Object 
  

  

  

  
    
      

```

445
446
447
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 445

def temp_file_new line
  s(:call, TEMP_FILE_CLASS, :new).line(line)
end
```

    
  

    
      
  
### 
  
    #**temp_file_open?**(exp)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

433
434
435
436
437
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 433

def temp_file_open? exp
  call? exp and
    exp.target == TEMP_FILE_CLASS and
    exp.method == :open
end
```

    
  

    
      
  
### 
  
    #**too_deep?**(exp)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

1166
1167
1168
1169
1170
1171
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 1166

def too_deep? exp
  @or_depth_limit >= 0 and
  node_type? exp, :or and
  exp.or_depth and
  exp.or_depth >= @or_depth_limit
end
```

    
  

    
      
  
### 
  
    #**top_target**(exp, last = nil)  ⇒ Object 
  

  

  

  
    

Returns last non-nil target in a call chain

  

  

  
    
      

```

1382
1383
1384
1385
1386
1387
1388
1389
1390
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 1382

def top_target exp, last = nil
  if call? exp
    top_target exp.target, exp
  elsif node_type? exp, :iter
    top_target exp.block_call, last
  else
    exp || last
  end
end
```

    
  

    
      
  
### 
  
    #**value_from_case**(exp)  ⇒ Object 
  

  

  

  
    
      

```

1414
1415
1416
1417
1418
1419
1420
1421
1422
1423
1424
1425
1426
1427
1428
1429
1430
1431
1432
1433
1434
1435
1436
1437
1438
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 1414

def value_from_case exp
  result = []

  exp.each do |e|
    if node_type? e, :when
      result << e.last
    end
  end

  result << exp.last if exp.last # else

  result.reduce do |c, e|
    if c.nil?
      e
    elsif node_type? e, :if
      c.combine(value_from_if e)
    elsif raise? e
      c # ignore exceptions
    elsif e
      c.combine e
    else # when e is nil
      c
    end
  end
end
```

    
  

    
      
  
### 
  
    #**value_from_if**(exp)  ⇒ Object 
  

  

  

  
    
      

```

1392
1393
1394
1395
1396
1397
1398
1399
1400
1401
1402
1403
1404
1405
1406
1407
1408
1409
1410
1411
1412
```

    
    
      

```
# File 'lib/brakeman/processors/alias_processor.rb', line 1392

def value_from_if exp
  if block? exp.else_clause or block? exp.then_clause
    #If either clause is more than a single expression, just use entire
    #if expression for now
    exp
  elsif exp.else_clause.nil?
    exp.then_clause
  elsif exp.then_clause.nil?
    exp.else_clause
  else
    condition = exp.condition

    if true? condition
      exp.then_clause
    elsif false? condition
      exp.else_clause
    else
      exp.then_clause.combine(exp.else_clause, exp.line)
    end
  end
end
```