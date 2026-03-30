# Class: Brakeman::CheckEOLRails
  
  
  

  
  
    Inherits:
    
      EOLCheck
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- EOLCheck
          
            
- Brakeman::CheckEOLRails
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_eol_rails.rb
  
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        RAILS_EOL_DATES =
          
  
    

rubyonrails.org/maintenance endoflife.date/rails

  

  

        
        

```
{
  ['2.0.0', '2.3.99'] => Date.new(2013, 6, 25),
  ['3.0.0', '3.2.99'] => Date.new(2016, 6, 30),
  ['4.0.0', '4.2.99'] => Date.new(2017, 4, 27),
  ['5.0.0', '5.0.99'] => Date.new(2018, 5, 9),
  ['5.1.0', '5.1.99'] => Date.new(2019, 8, 25),
  ['5.2.0', '5.2.99'] => Date.new(2022, 6, 1),
  ['6.0.0', '6.0.99'] => Date.new(2023, 6, 1),
  ['6.1.0', '6.1.99'] => Date.new(2024, 10, 1),
  ['7.0.0', '7.0.99'] => Date.new(2025, 4, 1),
  ['7.1.0', '7.1.99'] => Date.new(2025, 10, 1),
  ['7.2.0', '7.2.99'] => Date.new(2026, 8, 9),
  ['8.0.0', '8.0.99'] => Date.new(2026, 10, 7),
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
  
    
      #**run_check**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from EOLCheck

  

#check_eol_version, #warn_about_soon_unsupported_version, #warn_about_unsupported_version

  
  
  
  
  
  
  
  
  
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

8
9
10
11
12
```

    
    
      

```
# File 'lib/brakeman/checks/check_eol_rails.rb', line 8

def run_check
  return unless tracker.config.rails_version

  check_eol_version :rails, RAILS_EOL_DATES
end
```