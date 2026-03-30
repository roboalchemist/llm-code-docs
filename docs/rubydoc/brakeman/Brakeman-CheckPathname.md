# Class: Brakeman::CheckPathname
  
  
  

  
  
    Inherits:
    
      BaseCheck
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- Brakeman::CheckPathname
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_pathname.rb
  
  

  
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
  
    
      #**check_pathname_join**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_rails_root_join**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_result**(result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
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
  
    #**check_pathname_join**  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_pathname.rb', line 20

def check_pathname_join
  pathname_methods = [
    :'Pathname.new',
    :'Pathname.getwd',
    :'Pathname.glob',
    :'Pathname.pwd',
  ]

  tracker.find_call(targets: pathname_methods, method: :join, nested: true).each do |result|
    check_result result
  end
end
```

    
  

    
      
  
### 
  
    #**check_rails_root_join**  ⇒ Object 
  

  

  

  
    
      

```

14
15
16
17
18
```

    
    
      

```
# File 'lib/brakeman/checks/check_pathname.rb', line 14

def check_rails_root_join
  tracker.find_call(target: :'Rails.root', method: :join, nested: true).each do |result|
    check_result result
  end
end
```

    
  

    
      
  
### 
  
    #**check_result**(result)  ⇒ Object 
  

  

  

  
    
      

```

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
# File 'lib/brakeman/checks/check_pathname.rb', line 33

def check_result result
  return unless original? result

  result[:call].each_arg do |arg|
    if match = has_immediate_user_input?(arg)
      warn :result => result,
        :warning_type => "Path Traversal",
        :warning_code => :pathname_traversal,
        :message => "Absolute paths in `Pathname#join` cause the entire path to be relative to the absolute path, ignoring any prior values",
        :user_input => match,
        :confidence => :high,
        :cwe_id => [22]
    end
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
# File 'lib/brakeman/checks/check_pathname.rb', line 8

def run_check
  check_rails_root_join
  check_pathname_join

end
```