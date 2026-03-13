# Class: Brakeman::CheckDynamicFinders
  
  
  

  
  
    Inherits:
    
      BaseCheck
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- Brakeman::CheckDynamicFinders
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_dynamic_finders.rb
  
  

## Overview

  
    

This check looks for regexes that include user input.

  

  

  
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
  
    
      #**potentially_dangerous?**(method_name)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**process_result**(result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**run_check**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**safe_call?**(arg)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
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
  
    #**potentially_dangerous?**(method_name)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

46
47
48
```

    
    
      

```
# File 'lib/brakeman/checks/check_dynamic_finders.rb', line 46

def potentially_dangerous? method_name
  method_name.match(/^find_by_.*(token|guid|password|api_key|activation|code|private|reset)/)
end
```

    
  

    
      
  
### 
  
    #**process_result**(result)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_dynamic_finders.rb', line 17

def process_result result
  return unless original? result

  call = result[:call]

  if potentially_dangerous? call.method
    call.each_arg do |arg|
      if params? arg and not safe_call? arg
        warn :result => result,
          :warning_type => "SQL Injection",
          :warning_code => :sql_injection_dynamic_finder,
          :message => "MySQL integer conversion may cause 0 to match any string",
          :confidence => :medium,
          :user_input => arg,
          :cwe_id => [89]

        break
      end
    end
  end
end
```

    
  

    
      
  
### 
  
    #**run_check**  ⇒ Object 
  

  

  

  
    
      

```

9
10
11
12
13
14
15
```

    
    
      

```
# File 'lib/brakeman/checks/check_dynamic_finders.rb', line 9

def run_check
  if tracker.config.has_gem? :mysql and version_between? '2.0.0', '4.1.99'
    tracker.find_call(:method => /^find_by_/).each do |result|
      process_result result
    end
  end
end
```

    
  

    
      
  
### 
  
    #**safe_call?**(arg)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

39
40
41
42
43
44
```

    
    
      

```
# File 'lib/brakeman/checks/check_dynamic_finders.rb', line 39

def safe_call? arg
  return false unless call? arg

  meth = arg.method
  meth == :to_s or meth == :to_i
end
```