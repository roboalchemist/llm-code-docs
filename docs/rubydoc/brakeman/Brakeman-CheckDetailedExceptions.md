# Class: Brakeman::CheckDetailedExceptions
  
  
  

  
  
    Inherits:
    
      BaseCheck
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- Brakeman::CheckDetailedExceptions
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_detailed_exceptions.rb
  
  

## Overview

  
    

Check for detailed exceptions enabled for production

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        LOCAL_REQUEST =
          
        
        

```
s(:call, s(:call, nil, :request), :local?)
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
  
    
      #**check_detailed_exceptions**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_local_request_config**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**run_check**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**safe?**(body)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
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
  
    #**check_detailed_exceptions**  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_detailed_exceptions.rb', line 27

def check_detailed_exceptions
  tracker.controllers.each do |_name, controller|
    controller.methods_public.each do |method_name, definition|
      src = definition.src
      body = src.body.last
      next unless body

      if method_name == :show_detailed_exceptions? and not safe? body
        if true? body
          confidence = :high
        else
          confidence = :medium
        end

        warn :warning_type => "Information Disclosure",
             :warning_code => :detailed_exceptions,
             :message => msg("Detailed exceptions may be enabled in ", msg_code("show_detailed_exceptions?")),
             :confidence => confidence,
             :code => src,
             :file => definition[:file],
             :cwe_id => [200]
      end
    end
  end
end
```

    
  

    
      
  
### 
  
    #**check_local_request_config**  ⇒ Object 
  

  

  

  
    
      

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_detailed_exceptions.rb', line 16

def check_local_request_config
  if true? tracker.config.rails[:consider_all_requests_local]
    warn :warning_type => "Information Disclosure",
         :warning_code => :local_request_config,
         :message => "Detailed exceptions are enabled in production",
         :confidence => :high,
         :file => "config/environments/production.rb",
         :cwe_id => [200]
  end
end
```

    
  

    
      
  
### 
  
    #**run_check**  ⇒ Object 
  

  

  

  
    
      

```

11
12
13
14
```

    
    
      

```
# File 'lib/brakeman/checks/check_detailed_exceptions.rb', line 11

def run_check
  check_local_request_config
  check_detailed_exceptions
end
```

    
  

    
      
  
### 
  
    #**safe?**(body)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

53
54
55
56
```

    
    
      

```
# File 'lib/brakeman/checks/check_detailed_exceptions.rb', line 53

def safe? body
  false? body or
  body == LOCAL_REQUEST
end
```