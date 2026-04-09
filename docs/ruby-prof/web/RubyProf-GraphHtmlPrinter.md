# Class: RubyProf::GraphHtmlPrinter
  
  
  

  
  
    Inherits:
    
      AbstractPrinter
      
        

          
- Object
          
            
- AbstractPrinter
          
            
- RubyProf::GraphHtmlPrinter
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      ERB::Util
  
  
  

  

  
  
    Defined in:
    lib/ruby-prof/printers/graph_html_printer.rb
  
  

## Overview

  
    

Generates graph profile reports as html. To use the graph html printer:

```
result = RubyProf.profile do
  [code to profile]
end

printer = RubyProf::GraphHtmlPrinter.new(result)
printer.print(STDOUT, min_percent: 0)

```

  

  

  
## Instance Attribute Summary

  
  
### Attributes inherited from AbstractPrinter

  

#filter_by, #max_percent, #min_percent, #sort_method

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**create_link**(thread, overall_time, method)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Creates a link to a method.

  

      
        
- 
  
    
      #**file_link**(path, linenum)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**method_href**(thread, method)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**print**(output = STDOUT, min_time: nil, nonzero: false, min_percent: 0, max_percent: 100, filter_by: :self_time, sort_method: nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**template**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
  
### Methods inherited from AbstractPrinter

  

#initialize, #method_location, needs_dir?, #open_asset, #print_column_headers, #print_footer, #print_header, #print_thread, #print_threads, #time_format

  
## Constructor Details

  
    

This class inherits a constructor from RubyProf::AbstractPrinter
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**create_link**(thread, overall_time, method)  ⇒ Object 
  

  

  

  
    

Creates a link to a method.  Note that we do not create links to methods which are under the min_percent specified by the user, since they will not be printed out.

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/ruby-prof/printers/graph_html_printer.rb', line 34

def create_link(thread, overall_time, method)
  total_percent = (method.total_time/overall_time) * 100
  if total_percent < min_percent
    # Just return name
    h method.full_name
  else
    href = '#' + method_href(thread, method)
    "<a href=\"#{href}\">#{h method.full_name}</a>"
  end
end
```

    
  

    
      
  
### 
  
    #**file_link**(path, linenum)  ⇒ Object 
  

  

  

  
    
      

```

49
50
51
52
53
54
55
56
```

    
    
      

```
# File 'lib/ruby-prof/printers/graph_html_printer.rb', line 49

def file_link(path, linenum)
  if path.nil?
    ""
  else
    srcfile = File.expand_path(path)
    "<a href=\"file://#{h srcfile}##{linenum}\" title=\"#{h srcfile}:#{linenum}\">#{linenum}</a>"
  end
end
```

    
  

    
      
  
### 
  
    #**method_href**(thread, method)  ⇒ Object 
  

  

  

  
    
      

```

45
46
47
```

    
    
      

```
# File 'lib/ruby-prof/printers/graph_html_printer.rb', line 45

def method_href(thread, method)
  h(method.full_name.gsub(/[><#\.\?=:]/,"_") + "_" + thread.fiber_id.to_s)
end
```

    
  

    
      
  
### 
  
    #**print**(output = STDOUT, min_time: nil, nonzero: false, min_percent: 0, max_percent: 100, filter_by: :self_time, sort_method: nil)  ⇒ Object 
  

  

  

  
    
      

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
```

    
    
      

```
# File 'lib/ruby-prof/printers/graph_html_printer.rb', line 19

def print(output = STDOUT, min_time: nil, nonzero: false,
          min_percent: 0, max_percent: 100, filter_by: :self_time, sort_method: nil, **)
  @min_percent = min_percent
  @max_percent = max_percent
  @filter_by = filter_by
  @sort_method = sort_method
  @min_time = min_time
  @nonzero = nonzero
  output << ERB.new(self.template).result(binding)
end
```

    
  

    
      
  
### 
  
    #**template**  ⇒ Object 
  

  

  

  
    
      

```

58
59
60
```

    
    
      

```
# File 'lib/ruby-prof/printers/graph_html_printer.rb', line 58

def template
  open_asset('graph_printer.html.erb')
end
```