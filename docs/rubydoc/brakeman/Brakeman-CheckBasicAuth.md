# Class: Brakeman::CheckBasicAuth
  
  
  

  
  
    Inherits:
    
      BaseCheck
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- Brakeman::CheckBasicAuth
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_basic_auth.rb
  
  

## Overview

  
    

Checks if password is stored in controller when using http_basic_authenticate_with

Only for Rails >= 3.1

  

  

  
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
  
    
      #**check_basic_auth_filter**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_basic_auth_request**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Look for  authenticate_or_request_with_http_basic do |username, password|    username == “foo” && password == “bar”  end.

  

      
        
- 
  
    
      #**get_password**(call)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**include_password_literal?**(result)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Check if the block of a result contains a comparison of password to string.

  

      
        
- 
  
    
      #**process_call**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Looks for :== calls on password var.

  

      
        
- 
  
    
      #**run_check**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from BaseCheck

  

#add_result, description, inherited, #initialize, #process_array, #process_cookies, #process_default, #process_dstr, #process_if, #process_params

  
  
  
  
  
  
  
  
  
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
  
    #**check_basic_auth_filter**  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_basic_auth.rb', line 19

def check_basic_auth_filter
  controllers = tracker.controllers.select do |_name, c|
    c.options[:http_basic_authenticate_with]
  end

  Hash[controllers].each do |name, controller|
    controller.options[:http_basic_authenticate_with].each do |call|

      if pass = get_password(call) and string? pass
        warn :controller => name,
            :warning_type => "Basic Auth",
            :warning_code => :basic_auth_password,
            :message => "Basic authentication password stored in source code",
            :code => call,
            :confidence => :high,
            :file => controller.file,
            :cwe_id => [259]
        break
      end
    end
  end
end
```

    
  

    
      
  
### 
  
    #**check_basic_auth_request**  ⇒ Object 
  

  

  

  
    

Look for

```
authenticate_or_request_with_http_basic do |username, password|
  username == "foo" && password == "bar"
end

```

  

  

  
    
      

```

46
47
48
49
50
51
52
53
54
55
56
57
58
```

    
    
      

```
# File 'lib/brakeman/checks/check_basic_auth.rb', line 46

def check_basic_auth_request
  tracker.find_call(:target => nil, :method => :authenticate_or_request_with_http_basic).each do |result|
    if include_password_literal? result
        warn :result => result,
            :code => @include_password,
            :warning_type => "Basic Auth",
            :warning_code => :basic_auth_password,
            :message => "Basic authentication password stored in source code",
            :confidence => :high,
            :cwe_id => [259]
    end
  end
end
```

    
  

    
      
  
### 
  
    #**get_password**(call)  ⇒ Object 
  

  

  

  
    
      

```

85
86
87
88
89
90
91
```

    
    
      

```
# File 'lib/brakeman/checks/check_basic_auth.rb', line 85

def get_password call
  arg = call.first_arg

  return false if arg.nil? or not hash? arg

  hash_access(arg, :password)
end
```

    
  

    
      
  
### 
  
    #**include_password_literal?**(result)  ⇒ Boolean 
  

  

  

  
    

Check if the block of a result contains a comparison of password to string

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

61
62
63
64
65
66
67
68
```

    
    
      

```
# File 'lib/brakeman/checks/check_basic_auth.rb', line 61

def include_password_literal? result
  return false if result[:block_args].nil?

  @password_var = result[:block_args].last
  @include_password = false
  process result[:block]
  @include_password
end
```

    
  

    
      
  
### 
  
    #**process_call**(exp)  ⇒ Object 
  

  

  

  
    

Looks for :== calls on password var

  

  

  
    
      

```

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
83
```

    
    
      

```
# File 'lib/brakeman/checks/check_basic_auth.rb', line 71

def process_call exp
  target = exp.target

  if node_type?(target, :lvar) and
    target.value == @password_var and
    exp.method == :== and
    string? exp.first_arg

    @include_password = exp
  end

  exp
end
```

    
  

    
      
  
### 
  
    #**run_check**  ⇒ Object 
  

  

  

  
    
      

```

12
13
14
15
16
17
```

    
    
      

```
# File 'lib/brakeman/checks/check_basic_auth.rb', line 12

def run_check
  return if version_between? "0.0.0", "3.0.99"

  check_basic_auth_filter
  check_basic_auth_request
end
```