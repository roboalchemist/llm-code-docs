# Class: SimpleForm::Generators::InstallGenerator
  
  
  

  
  
    Inherits:
    
      Rails::Generators::Base
      
        

          
- Object
          
            
- Rails::Generators::Base
          
            
- SimpleForm::Generators::InstallGenerator
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/generators/simple_form/install_generator.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**copy_config**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**copy_scaffold_template**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**info_bootstrap**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**show_readme**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**copy_config**  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/generators/simple_form/install_generator.rb', line 18

def copy_config
  template "config/initializers/simple_form.rb"

  if options[:bootstrap]
    template "config/initializers/simple_form_bootstrap.rb"
  elsif options[:foundation]
    template "config/initializers/simple_form_foundation.rb"
  end

  directory 'config/locales'
end
```

    
  

    
      
  
### 
  
    #**copy_scaffold_template**  ⇒ Object 
  

  

  

  
    
      

```

30
31
32
33
```

    
    
      

```
# File 'lib/generators/simple_form/install_generator.rb', line 30

def copy_scaffold_template
  engine = options[:template_engine]
  copy_file "_form.html.#{engine}", "lib/templates/#{engine}/scaffold/_form.html.#{engine}"
end
```

    
  

    
      
  
### 
  
    #**info_bootstrap**  ⇒ Object 
  

  

  

  
    
      

```

11
12
13
14
15
16
```

    
    
      

```
# File 'lib/generators/simple_form/install_generator.rb', line 11

def info_bootstrap
  return if options.bootstrap? || options.foundation?
  puts "SimpleForm supports Bootstrap 5 and Zurb Foundation 5. If you want "\
    "a configuration that is compatible with one of these frameworks, then please " \
    "re-run this generator with --bootstrap or --foundation as an option."
end
```

    
  

    
      
  
### 
  
    #**show_readme**  ⇒ Object 
  

  

  

  
    
      

```

35
36
37
38
39
```

    
    
      

```
# File 'lib/generators/simple_form/install_generator.rb', line 35

def show_readme
  if behavior == :invoke && options.bootstrap?
    readme "README"
  end
end
```