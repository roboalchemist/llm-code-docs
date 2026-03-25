# Class: Brakeman::CheckPermitAttributes
  
  
  

  
  
    Inherits:
    
      BaseCheck
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- Brakeman::CheckPermitAttributes
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_permit_attributes.rb
  
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        SUSPICIOUS_KEYS =
          
        
        

```
{
  admin: :high,
  account_id: :high,
  role: :medium,
  banned: :medium,
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
  
    
      #**check_permit**(result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**run_check**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**warn_on_permit_key**(result, key, confidence = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
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
  
    #**check_permit**(result)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_permit_attributes.rb', line 21

def check_permit result
  return unless original? result

  call = result[:call]

  call.each_arg do |arg|
    if symbol? arg
      if SUSPICIOUS_KEYS.key? arg.value
        warn_on_permit_key result, arg
      end
    end
  end
end
```

    
  

    
      
  
### 
  
    #**run_check**  ⇒ Object 
  

  

  

  
    
      

```

15
16
17
18
19
```

    
    
      

```
# File 'lib/brakeman/checks/check_permit_attributes.rb', line 15

def run_check
  tracker.find_call(:method => :permit).each do |result|
    check_permit result
  end
end
```

    
  

    
      
  
### 
  
    #**warn_on_permit_key**(result, key, confidence = nil)  ⇒ Object 
  

  

  

  
    
      

```

35
36
37
38
39
40
41
42
43
```

    
    
      

```
# File 'lib/brakeman/checks/check_permit_attributes.rb', line 35

def warn_on_permit_key result, key, confidence = nil
  warn :result => result,
    :warning_type => "Mass Assignment",
    :warning_code => :dangerous_permit_key,
    :message => "Potentially dangerous key allowed for mass assignment",
    :confidence => (confidence || SUSPICIOUS_KEYS[key.value]),
    :user_input => key,
    :cwe_id => [915]
end
```