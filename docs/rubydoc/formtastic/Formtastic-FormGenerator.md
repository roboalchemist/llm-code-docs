# Class: Formtastic::FormGenerator
  
  
  

  
  
    Inherits:
    
      Rails::Generators::NamedBase
      
        

          
- Object
          
            
- Rails::Generators::NamedBase
          
            
- Formtastic::FormGenerator
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/generators/formtastic/form/form_generator.rb
  
  

## Overview

  
    

Generates a Formtastic form partial based on an existing model. It will not overwrite existing
files without confirmation.

!!!shell
  $ rails generate formtastic:form Post
!!!shell
  $ rails generate formtastic:form Post --copy
!!!shell
  $ rails generate formtastic:form Post --template-engine haml
  $ rails generate formtastic:form Post --template-engine slim
!!!shell
  $ rails generate formtastic:form Post title:string body:text
!!!shell
  $ rails generate formtastic:form Post --controller admin/posts

  

  
  
    
#### Examples:

    
      
        
##### 

Copy the partial code to the pasteboard rather than generating a partial

      
      

```

```

    
      
        
##### 

Return HAML or Slim output instead of default ERB

      
      

```

```

    
      
        
##### 

Generate a form for specific model attributes

      
      

```

```

    
      
        
##### 

Generate a form for a specific controller

      
      

```

```

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**create_or_show**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**create_or_show**  ⇒ Object 
  

  

  

  
    
      

```

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
51
52
53
```

    
    
      

```
# File 'lib/generators/formtastic/form/form_generator.rb', line 38

def create_or_show
  @attributes = reflected_attributes if @attributes.empty?

  engine = options[:template_engine]

  if options[:copy]
    template = File.read("#{self.class.source_root}/_form.html.#{engine}")
    erb = ERB.new(template, trim_mode: '-')
    generated_code = erb.result(binding).strip rescue nil
    puts "The following code has been copied to the clipboard, just paste it in your views:" if save_to_clipboard(generated_code)
    puts generated_code || "Error: Nothing generated. Does the model exist?"
  else
    empty_directory "app/views/#{controller_path}"
    template "_form.html.#{engine}", "app/views/#{controller_path}/_form.html.#{engine}"
  end
end
```