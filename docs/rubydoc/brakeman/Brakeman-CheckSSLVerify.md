# Class: Brakeman::CheckSSLVerify
  
  
  

  
  
    Inherits:
    
      BaseCheck
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- Brakeman::CheckSSLVerify
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_ssl_verify.rb
  
  

## Overview

  
    

Checks if verify_mode= is called with OpenSSL::SSL::VERIFY_NONE

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        SSL_VERIFY_NONE =
          
        
        

```
s(:colon2, s(:colon2, s(:const, :OpenSSL), :SSL), :VERIFY_NONE)
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
  
    
      #**check_http_start**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_open_ssl_verify_none**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**process_http_start_result**(result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**process_verify_mode_result**(result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**run_check**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**warn_about_ssl_verification_bypass**(result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
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
  
    #**check_http_start**  ⇒ Object 
  

  

  

  
    
      

```

27
28
29
```

    
    
      

```
# File 'lib/brakeman/checks/check_ssl_verify.rb', line 27

def check_http_start
  tracker.find_call(:target => :'Net::HTTP', :method => :start).each { |call| process_http_start_result call }
end
```

    
  

    
      
  
### 
  
    #**check_open_ssl_verify_none**  ⇒ Object 
  

  

  

  
    
      

```

17
18
19
```

    
    
      

```
# File 'lib/brakeman/checks/check_ssl_verify.rb', line 17

def check_open_ssl_verify_none
  tracker.find_call(:method => :verify_mode=).each {|call| process_verify_mode_result(call) }
end
```

    
  

    
      
  
### 
  
    #**process_http_start_result**(result)  ⇒ Object 
  

  

  

  
    
      

```

31
32
33
34
35
36
37
```

    
    
      

```
# File 'lib/brakeman/checks/check_ssl_verify.rb', line 31

def process_http_start_result result
  arg = result[:call].last_arg

  if hash? arg and hash_access(arg, :verify_mode) == SSL_VERIFY_NONE
    warn_about_ssl_verification_bypass result
  end
end
```

    
  

    
      
  
### 
  
    #**process_verify_mode_result**(result)  ⇒ Object 
  

  

  

  
    
      

```

21
22
23
24
25
```

    
    
      

```
# File 'lib/brakeman/checks/check_ssl_verify.rb', line 21

def process_verify_mode_result result
  if result[:call].last_arg == SSL_VERIFY_NONE
    warn_about_ssl_verification_bypass result
  end
end
```

    
  

    
      
  
### 
  
    #**run_check**  ⇒ Object 
  

  

  

  
    
      

```

12
13
14
15
```

    
    
      

```
# File 'lib/brakeman/checks/check_ssl_verify.rb', line 12

def run_check
  check_open_ssl_verify_none
  check_http_start
end
```

    
  

    
      
  
### 
  
    #**warn_about_ssl_verification_bypass**(result)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_ssl_verify.rb', line 39

def warn_about_ssl_verification_bypass result
  return unless original? result

  warn :result => result,
    :warning_type => "SSL Verification Bypass",
    :warning_code => :ssl_verification_bypass,
    :message => "SSL certificate verification was bypassed",
    :confidence => :high,
    :cwe_id => [295]
end
```