# Class: Brakeman::CheckRansack
  
  
  

  
  
    Inherits:
    
      BaseCheck
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- Brakeman::CheckRansack
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_ransack.rb
  
  

  
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
  
    
      #**check_ransack_calls**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**ransackable_allow_list?**(class_name)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**run_check**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
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
  
    #**check_ransack_calls**  ⇒ Object 
  

  

  

  
    
      

```

13
14
15
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
```

    
    
      

```
# File 'lib/brakeman/checks/check_ransack.rb', line 13

def check_ransack_calls
  tracker.find_call(method: :ransack, nested: true).each do |result|
    next unless original? result

    call = result[:call]
    arg = call.first_arg

    # If an allow list is defined anywhere in the
    # class or super classes, consider it safe
    class_name = result[:chain].first

    next if ransackable_allow_list?(class_name)

    if input = has_immediate_user_input?(arg)
      confidence = if tracker.find_class(class_name).nil?
                     confidence = :low
                   elsif result[:location][:file].relative.include? 'admin'
                     confidence = :medium
                   else
                     confidence = :high
                   end

      message = msg('Unrestricted search using ', msg_code('ransack'), ' library called with ', msg_input(input), '. Limit search by defining ', msg_code('ransackable_attributes'), ' and ', msg_code('ransackable_associations'), ' methods in class or upgrade Ransack to version 4.0.0 or newer')

      warn result: result,
        warning_type: 'Missing Authorization',
        warning_code: :ransack_search,
        message: message,
        user_input: input,
        confidence: confidence,
        cwe_id: [862],
        link: 'https://positive.security/blog/ransack-data-exfiltration'
    end
  end
end
```

    
  

    
      
  
### 
  
    #**ransackable_allow_list?**(class_name)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

49
50
51
52
```

    
    
      

```
# File 'lib/brakeman/checks/check_ransack.rb', line 49

def ransackable_allow_list? class_name
  tracker.find_method(:ransackable_attributes, class_name, :class) and
    tracker.find_method(:ransackable_associations, class_name, :class)
end
```

    
  

    
      
  
### 
  
    #**run_check**  ⇒ Object 
  

  

  

  
    
      

```

8
9
10
11
```

    
    
      

```
# File 'lib/brakeman/checks/check_ransack.rb', line 8

def run_check
  return unless version_between? "0.0.0", "3.99", tracker.config.gem_version(:ransack)
  check_ransack_calls
end
```