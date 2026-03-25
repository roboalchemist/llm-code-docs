# Class: Brakeman::CheckI18nXSS
  
  
  

  
  
    Inherits:
    
      BaseCheck
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- Brakeman::CheckI18nXSS
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_i18n_xss.rb
  
  

  
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
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**version_before**(gem_version, target)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
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

44
45
46
47
48
```

    
    
      

```
# File 'lib/brakeman/checks/check_i18n_xss.rb', line 44

def has_workaround?
  tracker.find_call(target: :I18n, method: :const_defined?, chained: true).any? do |match|
    match[:call].first_arg == s(:lit, :MissingTranslation)
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
```

    
    
      

```
# File 'lib/brakeman/checks/check_i18n_xss.rb', line 8

def run_check
  if (version_between? "3.0.6", "3.2.15" or version_between? "4.0.0", "4.0.1") and not has_workaround?
    i18n_gem = tracker.config.gem_version :i18n
    message = msg(msg_version(rails_version), " has an XSS vulnerability in ", msg_version(i18n_gem, "i18n"), " ", msg_cve("CVE-2013-4491"), ". Upgrade to ")

    if version_between? "3.0.6", "3.1.99" and version_before i18n_gem, "0.5.1"
      message << msg_version("3.2.16 or i18n 0.5.1")
    elsif version_between? "3.2.0", "4.0.1" and version_before i18n_gem, "0.6.6"
      message << msg_version("4.0.2 or i18n 0.6.6")
    else
      return
    end

    warn :warning_type => "Cross-Site Scripting",
      :warning_code => :CVE_2013_4491,
      :message => message,
      :confidence => :medium,
      :gem_info => gemfile_or_environment(:i18n),
      :link_path => "https://groups.google.com/d/msg/ruby-security-ann/pLrh6DUw998/bLFEyIO4k_EJ",
      :cwe_id => [79]
  end
end
```

    
  

    
      
  
### 
  
    #**version_before**(gem_version, target)  ⇒ Object 
  

  

  

  
    
      

```

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
# File 'lib/brakeman/checks/check_i18n_xss.rb', line 31

def version_before gem_version, target
  return true unless gem_version
  gem_version.split('.').map(&:to_i).zip(target.split('.').map(&:to_i)).each do |gv, t|
    if gv < t
      return true
    elsif gv > t
      return false
    end
  end

  false
end
```