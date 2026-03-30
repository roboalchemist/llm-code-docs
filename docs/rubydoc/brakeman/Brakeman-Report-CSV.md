# Class: Brakeman::Report::CSV
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- Brakeman::Report::CSV
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/report/report_csv.rb
  
  

  
## Constant Summary

  
  
### Constants included
     from Util

  

Util::ALL_COOKIES, Util::ALL_PARAMETERS, Util::COOKIES, Util::COOKIES_SEXP, Util::DIR_CONST, Util::LITERALS, Util::PARAMETERS, Util::PARAMS_SEXP, Util::PATH_PARAMETERS, Util::QUERY_PARAMETERS, Util::REQUEST_COOKIES, Util::REQUEST_ENV, Util::REQUEST_PARAMETERS, Util::REQUEST_PARAMS, Util::REQUEST_REQUEST_PARAMETERS, Util::SAFE_LITERAL, Util::SESSION, Util::SESSION_SEXP, Util::SIMPLE_LITERALS

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#checks, #tracker

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**generate_report**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**generate_row**(headers, warning)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**warning_row**(warning)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#absolute_paths?, #all_warnings, #context_for, #controller_information, #controller_warnings, #filter_warnings, #generic_warnings, #github_url, #ignored_warnings, #initialize, #model_warnings, #number_of_templates, #rails_version, #template_warnings, #warning_file, #warnings_summary

  
  
  
  
  
  
  
  
  
### Methods included from Util

  

#all_literals?, #array?, #block?, #call?, #camelize, #class_name, #constant?, #contains_class?, #cookies?, #dir_glob?, #false?, #hash?, #hash_access, #hash_insert, #hash_iterate, #hash_values, #integer?, #kwsplat?, #literal?, #make_call, #node_type?, #number?, #params?, #pluralize, #rails_version, #recurse_check?, #regexp?, #remove_kwsplat, #request_headers?, #request_value?, #result?, #safe_literal, #safe_literal?, #safe_literal_target?, #set_env_defaults, #sexp?, #simple_literal?, #string?, #string_interp?, #symbol?, #template_path_to_name, #true?, #underscore

  
## Constructor Details

  
    

This class inherits a constructor from Brakeman::Report::Base
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**generate_report**  ⇒ Object 
  

  

  

  
    
      

```

4
5
6
7
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
# File 'lib/brakeman/report/report_csv.rb', line 4

def generate_report
  headers = [
    "Confidence",
    "Warning Type",
    "CWE",
    "File",
    "Line",
    "Message",
    "Code",
    "User Input",
    "Check Name",
    "Warning Code",
    "Fingerprint",
    "Link"
  ]

  rows = tracker.filtered_warnings.sort_by do |w|
    [w.confidence, w.warning_type, w.file, w.line || 0, w.fingerprint]
  end.map do |warning|
    generate_row(headers, warning)
  end

  table = CSV::Table.new(rows)

  table.to_csv
end
```

    
  

    
      
  
### 
  
    #**generate_row**(headers, warning)  ⇒ Object 
  

  

  

  
    
      

```

31
32
33
```

    
    
      

```
# File 'lib/brakeman/report/report_csv.rb', line 31

def generate_row headers, warning
  CSV::Row.new headers, warning_row(warning)
end
```

    
  

    
      
  
### 
  
    #**warning_row**(warning)  ⇒ Object 
  

  

  

  
    
      

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
50
```

    
    
      

```
# File 'lib/brakeman/report/report_csv.rb', line 35

def warning_row warning
  [
    warning.confidence_name,
    warning.warning_type,
    warning.cwe_id.first,
    warning_file(warning),
    warning.line,
    warning.message,
    warning.code && warning.format_code(false),
    warning.user_input && warning.format_user_input(false),
    warning.check_name,
    warning.warning_code,
    warning.fingerprint,
    warning.link,
  ]
end
```