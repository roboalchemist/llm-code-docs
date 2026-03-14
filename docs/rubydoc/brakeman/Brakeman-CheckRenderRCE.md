# Class: Brakeman::CheckRenderRCE
  
  
  

  
  
    Inherits:
    
      CheckRender
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- CheckRender
          
            
- Brakeman::CheckRenderRCE
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_render_rce.rb
  
  

  
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
  
    
      #**check_for_rce**(result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**process_render_result**(result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**run_check**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from CheckRender

  

#check_for_dynamic_path, #known_renderable_class?, #renderable?, #safe_param?

  
  
  
  
  
  
  
  
  
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
  
    #**check_for_rce**(result)  ⇒ Object 
  

  

  

  
    
      

```

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
# File 'lib/brakeman/checks/check_render_rce.rb', line 23

def check_for_rce result
  return unless version_between? "0.0.0", "3.2.22" or
                version_between? "4.0.0", "4.1.14" or
                version_between? "4.2.0", "4.2.5"

  view = result[:call][2]
  if sexp? view and not duplicate? result
    if params? view and not safe_param? view
      add_result result

      warn :result => result,
        :warning_type => "Remote Code Execution",
        :warning_code => :dynamic_render_path_rce,
        :message => msg("Passing query parameters to ", msg_code("render"), " is vulnerable in ", msg_version(rails_version), " ", msg_cve("CVE-2016-0752")),
        :user_input => view,
        :confidence => :high,
        :cwe_id => [22]
    end
  end
end
```

    
  

    
      
  
### 
  
    #**process_render_result**(result)  ⇒ Object 
  

  

  

  
    
      

```

14
15
16
17
18
19
20
21
```

    
    
      

```
# File 'lib/brakeman/checks/check_render_rce.rb', line 14

def process_render_result result
  return unless node_type? result[:call], :render

  case result[:call].render_type
  when :partial, :template, :action, :file
    check_for_rce(result)
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
```

    
    
      

```
# File 'lib/brakeman/checks/check_render_rce.rb', line 8

def run_check
  tracker.find_call(:target => nil, :method => :render).each do |result|
    process_render_result result
  end
end
```