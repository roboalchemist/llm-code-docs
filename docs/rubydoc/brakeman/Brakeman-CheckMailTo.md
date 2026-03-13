# Class: Brakeman::CheckMailTo
  
  
  

  
  
    Inherits:
    
      BaseCheck
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- Brakeman::CheckMailTo
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_mail_to.rb
  
  

## Overview

  
    

Check for cross-site scripting vulnerability in mail_to :encode => :javascript with certain versions of Rails (< 2.3.11 or < 3.0.4).

groups.google.com/group/rubyonrails-security/browse_thread/thread/f02a48ede8315f81

  

  

  
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
  
    
      #**mail_to_javascript?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Check for javascript encoding of mail_to address    mail_to email, name, :encode => :javascript.

  

      
        
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
  
    #**mail_to_javascript?**  ⇒ Boolean 
  

  

  

  
    

Check for javascript encoding of mail_to address

```
mail_to email, name, :encode => :javascript

```

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_mail_to.rb', line 35

def mail_to_javascript?
  Brakeman.debug "Checking calls to mail_to for javascript encoding"

  tracker.find_call(:target => false, :method => :mail_to).each do |result|
    result[:call].each_arg do |arg|
      if hash? arg
        if option = hash_access(arg, :encode)
          return result if symbol? option and option.value == :javascript
        end
      end
    end
  end

  false
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
```

    
    
      

```
# File 'lib/brakeman/checks/check_mail_to.rb', line 12

def run_check
  if (version_between? "2.3.0", "2.3.10" or version_between? "3.0.0", "3.0.3") and result = mail_to_javascript?
    message = msg("Vulnerability in ", msg_code("mail_to"), " using javascript encoding ", msg_cve("CVE-2011-0446"), ". Upgrade to ")

    if version_between? "2.3.0", "2.3.10"
      message << msg_version("2.3.11")
    else
      message << msg_version("3.0.4")
    end

    warn :result => result,
      :warning_type => "Mail Link",
      :warning_code => :CVE_2011_0446,
      :message => message,
      :confidence => :high,
      :gem_info => gemfile_or_environment, # Probably ignored now
      :link_path => "https://groups.google.com/d/topic/rubyonrails-security/8CpI7egxX4E/discussion",
      :cwe_id => [79]
  end
end
```