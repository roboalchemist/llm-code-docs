# Class: Brakeman::CheckModelAttributes
  
  
  

  
  
    Inherits:
    
      BaseCheck
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- Brakeman::CheckModelAttributes
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_model_attributes.rb
  
  

## Overview

  
    

Check if mass assignment is used with models which inherit from ActiveRecord::Base.

  

  

  
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
  
    
      #**check_for_attr_protected_bypass**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_models**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
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
  
    #**check_for_attr_protected_bypass**  ⇒ Object 
  

  

  

  
    
      

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
82
```

    
    
      

```
# File 'lib/brakeman/checks/check_model_attributes.rb', line 57

def check_for_attr_protected_bypass
  upgrade_version = case
                    when version_between?("2.0.0", "2.3.16")
                      "2.3.17"
                    when version_between?("3.0.0", "3.0.99")
                      "3.2.11"
                    when version_between?("3.1.0", "3.1.10")
                      "3.1.11"
                    when version_between?("3.2.0", "3.2.11")
                      "3.2.12"
                    else
                      nil
                    end

  if upgrade_version
    message = msg(msg_code("attr_protected"), " is bypassable in ", msg_version(rails_version), ". Use ", msg_code("attr_accessible"), " or upgrade to ", msg_version(upgrade_version))
    confidence = :high
    link = "https://groups.google.com/d/topic/rubyonrails-security/AFBKNY7VSH8/discussion"
  else
    message = msg(msg_code("attr_accessible"), " is recommended over ", msg_code("attr_protected"))
    confidence = :medium
    link = nil
  end

  return message, confidence, link
end
```

    
  

    
      
  
### 
  
    #**check_models**  ⇒ Object 
  

  

  

  
    
      

```

49
50
51
52
53
54
55
```

    
    
      

```
# File 'lib/brakeman/checks/check_model_attributes.rb', line 49

def check_models
  tracker.models.each do |name, model|
    if model.unprotected_model?
      yield name, model
    end
  end
end
```

    
  

    
      
  
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
# File 'lib/brakeman/checks/check_model_attributes.rb', line 10

def run_check
  return if mass_assign_disabled? or tracker.config.has_gem?(:protected_attributes)

  #Roll warnings into one warning for all models
  if tracker.options[:collapse_mass_assignment]
    Brakeman.alert "The `collapse_mass_assignment` option has been removed."
  end

  check_models do |name, model|
    if model.attr_protected.nil?
      warn :model => model,
        :file => model.file,
        :line => model.top_line,
        :warning_type => "Attribute Restriction",
        :warning_code => :no_attr_accessible,
        :message => msg("Mass assignment is not restricted using ", msg_code("attr_accessible")),
        :confidence => :high,
        :cwe_id => [915] # TODO: Should this be mass assignment?
    elsif not tracker.options[:ignore_attr_protected]
      message, confidence, link = check_for_attr_protected_bypass

      if link
        warning_code = :CVE_2013_0276
      else
        warning_code = :attr_protected_used
      end

      warn :model => model,
        :file => model.file,
        :line => model.attr_protected.first.line,
        :warning_type => "Attribute Restriction",
        :warning_code => warning_code,
        :message => message,
        :confidence => confidence,
        :cwe_id => [915] # TODO: Should this be mass assignment?
    end
  end
end
```