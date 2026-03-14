# Class: Brakeman::CheckRegexDoS
  
  
  

  
  
    Inherits:
    
      BaseCheck
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- Brakeman::CheckRegexDoS
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_regex_dos.rb
  
  

## Overview

  
    

This check looks for regexes that include user input.

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        ESCAPES =
          
        
        

```
{
  s(:const, :Regexp) => [
    :escape,
    :quote
  ]
}
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
  
    
      #**process_call**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**process_result**(result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Warns if regex includes user input.

  

      
        
- 
  
    
      #**run_check**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Process calls.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from BaseCheck

  

#add_result, description, inherited, #initialize, #process_array, #process_cookies, #process_default, #process_dstr, #process_if, #process_params

  
  
  
  
  
  
  
  
  
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
  
    #**process_call**(exp)  ⇒ Object 
  

  

  

  
    
      

```

60
61
62
63
64
65
66
67
68
```

    
    
      

```
# File 'lib/brakeman/checks/check_regex_dos.rb', line 60

def process_call(exp)
  if escape_methods = ESCAPES[exp.target]
    if escape_methods.include? exp.method
      return exp
    end
  end

  super
end
```

    
  

    
      
  
### 
  
    #**process_result**(result)  ⇒ Object 
  

  

  

  
    

Warns if regex includes user input

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_regex_dos.rb', line 28

def process_result result
  return unless original? result

  call = result[:call]
  components = call.sexp_body

  components.any? do |component|
    next unless sexp? component

    if match = has_immediate_user_input?(component)
      confidence = :high
    elsif match = has_immediate_model?(component)
      match = Match.new(:model, match)
      confidence = :medium
    elsif match = include_user_input?(component)
      confidence = :weak
    end

    if match
      message = msg(msg_input(match), " used in regular expression")

      warn :result => result,
        :warning_type => "Denial of Service",
        :warning_code => :regex_dos,
        :message => message,
        :confidence => confidence,
        :user_input => match,
        :cwe_id => [20, 185]
    end
  end
end
```

    
  

    
      
  
### 
  
    #**run_check**  ⇒ Object 
  

  

  

  
    

Process calls

  

  

  
    
      

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_regex_dos.rb', line 17

def run_check
  Brakeman.debug "Finding dynamic regexes"
  calls = tracker.find_call :method => [:brakeman_regex_interp]

  Brakeman.debug "Processing dynamic regexes"
  calls.each do |call|
    process_result call
  end
end
```