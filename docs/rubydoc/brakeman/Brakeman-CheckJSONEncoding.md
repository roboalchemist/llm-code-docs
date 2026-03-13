# Class: Brakeman::CheckJSONEncoding
  
  
  

  
  
    Inherits:
    
      BaseCheck
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- Brakeman::CheckJSONEncoding
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_json_encoding.rb
  
  

  
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
  
    
      #**has_workaround?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
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
  
    #**has_workaround?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

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
# File 'lib/brakeman/checks/check_json_encoding.rb', line 34

def has_workaround?
  workaround = s(:module, :ActiveSupport,
                 s(:module, :JSON,
                   s(:module, :Encoding,
                     s(:call, nil, :private),
                     s(:class, :EscapedString, nil,
                       s(:defn, :to_s,
                         s(:args),
                         s(:self))))))

  tracker.initializers.any? do |_name, initializer|
    initializer == workaround
  end
end
```

    
  

    
      
  
### 
  
    #**run_check**  ⇒ Object 
  

  

  

  
    
      

```

8
9
10
11
12
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
```

    
    
      

```
# File 'lib/brakeman/checks/check_json_encoding.rb', line 8

def run_check
  if (version_between? "4.1.0", "4.1.10" or version_between? "4.2.0", "4.2.1") and not has_workaround?
    message = msg(msg_version(rails_version), " does not encode JSON keys ", msg_cve("CVE-2015-3226"), ". Upgrade to ")

    if version_between? "4.1.0", "4.1.10"
      message << msg_version("4.1.11")
    else
      message << msg_version("4.2.2")
    end

    if tracker.find_call(:methods => [:to_json, :encode]).any?
      confidence = :high
    else
      confidence = :medium
    end

    warn :warning_type => "Cross-Site Scripting",
      :warning_code => :CVE_2015_3226,
      :message => message,
      :confidence => confidence,
      :gem_info => gemfile_or_environment,
      :link_path => "https://groups.google.com/d/msg/rubyonrails-security/7VlB_pck3hU/3QZrGIaQW6cJ",
      :cwe_id => [79]
  end
end
```