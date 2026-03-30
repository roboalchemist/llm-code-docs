# Class: Brakeman::CheckEvaluation
  
  
  

  
  
    Inherits:
    
      BaseCheck
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- Brakeman::CheckEvaluation
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_evaluation.rb
  
  

## Overview

  
    

This check looks for calls to `eval`, `instance_eval`, etc. which include user input.

  

  

  
## Constant Summary

  
  
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
  
    
      #**process_result**(result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Warns if eval includes user input.

  

      
        
- 
  
    
      #**run_check**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Process calls.

  

      
        
- 
  
    
      #**safe_value?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**string_evaluation?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
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
  
    #**process_result**(result)  ⇒ Object 
  

  

  

  
    

Warns if eval includes user input

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_evaluation.rb', line 22

def process_result result
  return unless original? result

  first_arg = result[:call].first_arg

  unless safe_value? first_arg
    if input = include_user_input?(first_arg)
      confidence = :high
      message = msg(msg_input(input), " evaluated as code")
    elsif string_evaluation? first_arg
      confidence = :low
      message = "Dynamic string evaluated as code"
    elsif result[:call].method == :eval
      confidence = :low
      message = "Dynamic code evaluation"
    end

    if confidence
      warn :result => result,
        :warning_type => "Dangerous Eval",
        :warning_code => :code_eval,
        :message => message,
        :user_input => input,
        :confidence => confidence,
        :cwe_id => [913, 95]
    end
  end
end
```

    
  

    
      
  
### 
  
    #**run_check**  ⇒ Object 
  

  

  

  
    

Process calls

  

  

  
    
      

```

11
12
13
14
15
16
17
18
19
```

    
    
      

```
# File 'lib/brakeman/checks/check_evaluation.rb', line 11

def run_check
  Brakeman.debug "Finding eval-like calls"
  calls = tracker.find_call methods: [:eval, :instance_eval, :class_eval, :module_eval], nested: true

  Brakeman.debug "Processing eval-like calls"
  calls.each do |call|
    process_result call
  end
end
```

    
  

    
      
  
### 
  
    #**safe_value?**(exp)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_evaluation.rb', line 56

def safe_value? exp
  return true unless sexp? exp

  case exp.sexp_type
  when :dstr
    exp.all? { |e| safe_value? e}
  when :evstr
    safe_value? exp.value
  when :str, :lit
    true
  when :call
    always_safe_method? exp.method
  else
    false
  end
end
```

    
  

    
      
  
### 
  
    #**string_evaluation?**(exp)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

51
52
53
54
```

    
    
      

```
# File 'lib/brakeman/checks/check_evaluation.rb', line 51

def string_evaluation? exp
  string_interp? exp or
    (call? exp and string? exp.target)
end
```