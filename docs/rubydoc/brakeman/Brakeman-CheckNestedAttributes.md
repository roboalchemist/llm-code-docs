# Class: Brakeman::CheckNestedAttributes
  
  
  

  
  
    Inherits:
    
      BaseCheck
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- Brakeman::CheckNestedAttributes
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_nested_attributes.rb
  
  

## Overview

  
    

Check for vulnerability in nested attributes in Rails 2.3.9 and 3.0.0 groups.google.com/group/rubyonrails-security/browse_thread/thread/f9f913d328dafe0c

  

  

  
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
  
    
      #**run_check**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**uses_nested_attributes?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
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
  
    #**run_check**  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_nested_attributes.rb', line 10

def run_check
  version = rails_version

  if (version == "2.3.9" or version == "3.0.0") and uses_nested_attributes?
    message = msg("Vulnerability in nested attributes ", msg_cve("CVE-2010-3933"), ". Upgrade to ")

    if version == "2.3.9"
      message << msg_version("2.3.10")
    else
      message << msg_version("3.0.1")
    end

    warn :warning_type => "Nested Attributes",
      :warning_code => :CVE_2010_3933,
      :message => message,
      :confidence => :high,
      :gem_info => gemfile_or_environment,
      :link_path => "https://groups.google.com/d/topic/rubyonrails-security/-fkT0yja_gw/discussion",
      :cwe_id => [20]
  end
end
```

    
  

    
      
  
### 
  
    #**uses_nested_attributes?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

32
33
34
35
36
37
38
```

    
    
      

```
# File 'lib/brakeman/checks/check_nested_attributes.rb', line 32

def uses_nested_attributes?
  active_record_models.each do |_name, model|
    return true if model.options[:accepts_nested_attributes_for]
  end

  false
end
```