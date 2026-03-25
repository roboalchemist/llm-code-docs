# Class: Brakeman::CheckExecute
  
  
  

  
  
    Inherits:
    
      BaseCheck
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- Brakeman::CheckExecute
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_execute.rb
  
  

## Overview

  
    

Checks for string interpolation and parameters in calls to Kernel#system, Kernel#exec, Kernel#syscall, and inside backticks.

Examples of command injection vulnerabilities:

system(“rf -rf #:file”) exec(params) ‘unlink #params[:something`

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        SAFE_VALUES =
          
        
        

```
[s(:const, :RAILS_ROOT),
s(:call, s(:const, :Rails), :root),
s(:call, s(:const, :Rails), :env),
s(:call, s(:const, :Process), :pid)]
```

      
        SHELL_ESCAPE_MODULE_METHODS =
          
        
        

```

```

      
        SHELL_ESCAPE_MIXIN_METHODS =
          
        
        

```

```

      
        KNOWN_SHELL_COMMANDS =
          
  
    

These are common shells that are known to allow the execution of commands via a -c flag. See dash_c_shell_command? for more info.

  

  

        
        

```

```

      
        SHELLWORDS =
          
        
        

```
s(:const, :Shellwords)
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
    

    
  
  
  
  
  
  
  
  

  
    

Check models, controllers, and views for command injection.

  

      
    

  

  
  
  
  
  
  
  
  
  
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
  

  

  

  
    

Check models, controllers, and views for command injection.

  

  

  
    
      

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
43
44
45
46
47
```

    
    
      

```
# File 'lib/brakeman/checks/check_execute.rb', line 31

def run_check
  Brakeman.debug "Finding system calls using ``"
  check_for_backticks tracker

  check_open_calls

  Brakeman.debug "Finding other system calls"
  calls = tracker.find_call :targets => [:IO, :Open3, :Kernel, :'POSIX::Spawn', :Process, nil],
    :methods => [:capture2, :capture2e, :capture3, :exec, :pipeline, :pipeline_r,
      :pipeline_rw, :pipeline_start, :pipeline_w, :popen, :popen2, :popen2e,
      :popen3, :spawn, :syscall, :system], :nested => true

  Brakeman.debug "Processing system calls"
  calls.each do |result|
    process_result result
  end
end
```