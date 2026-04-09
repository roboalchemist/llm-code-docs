# Class: Brakeman::CheckModelAttrAccessible
  
  
  

  
  
    Inherits:
    
      BaseCheck
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- Brakeman::CheckModelAttrAccessible
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_model_attr_accessible.rb
  
  

## Overview

  
    

Author: Paul Deardorff (themetric) Checks models to see if important foreign keys or attributes are exposed as attr_accessible when they probably shouldn’t be.

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        SUSP_ATTRS =
          
        
        

```
[
  [:admin, :high], # Very dangerous unless some Rails authorization used
  [:role, :medium],
  [:banned, :medium],
  [:account_id, :high],
  [/\S*_id(s?)\z/, :weak] # All other foreign keys have weak/low confidence
]
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
  
    
      #**check_models**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**role_limited?**(model, attribute)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
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
  
    #**check_models**  ⇒ Object 
  

  

  

  
    
      

```

50
51
52
53
54
55
56
```

    
    
      

```
# File 'lib/brakeman/checks/check_model_attr_accessible.rb', line 50

def check_models
  tracker.models.each do |name, model|
    if !model.attr_accessible.nil?
      yield name, model
    end
  end
end
```

    
  

    
      
  
### 
  
    #**role_limited?**(model, attribute)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

44
45
46
47
48
```

    
    
      

```
# File 'lib/brakeman/checks/check_model_attr_accessible.rb', line 44

def role_limited? model, attribute
  role_accessible = model.role_accessible
  return if role_accessible.nil?
  role_accessible.include? attribute
end
```

    
  

    
      
  
### 
  
    #**run_check**  ⇒ Object 
  

  

  

  
    
      

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
34
35
36
37
38
39
40
41
42
```

    
    
      

```
# File 'lib/brakeman/checks/check_model_attr_accessible.rb', line 21

def run_check
  check_models do |name, model|
    model.attr_accessible.each do |attribute|
      next if role_limited? model, attribute

      SUSP_ATTRS.each do |susp_attr, confidence|
        if susp_attr.is_a?(Regexp) and susp_attr =~ attribute.to_s or susp_attr == attribute
          warn :model => model,
            :file => model.file,
            :warning_type => "Mass Assignment",
            :warning_code => :dangerous_attr_accessible,
            :message => "Potentially dangerous attribute available for mass assignment",
            :confidence => confidence,
            :code => Sexp.new(:lit, attribute),
            :cwe_id => [915]

          break # Prevent from matching single attr multiple times
        end
      end
    end
  end
end
```