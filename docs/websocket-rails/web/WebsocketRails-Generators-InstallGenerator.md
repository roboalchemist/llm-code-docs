# Class: WebsocketRails::Generators::InstallGenerator
  
  
  

  
  
    Inherits:
    
      Rails::Generators::Base
      
        

          
- Object
          
            
- Rails::Generators::Base
          
            
- WebsocketRails::Generators::InstallGenerator
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/generators/websocket_rails/install/install_generator.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**create_events_initializer_file**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**inject_websocket_rails_client**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**create_events_initializer_file**  ⇒ Object 
  

  

  

  
    
      

```

13
14
15
16
```

    
    
      

```
# File 'lib/generators/websocket_rails/install/install_generator.rb', line 13

def create_events_initializer_file
  template 'events.rb', File.join('config', 'events.rb')
  template 'websocket_rails.rb', File.join('config', 'initializers', 'websocket_rails.rb')
end
```

    
  

    
      
  
### 
  
    #**inject_websocket_rails_client**  ⇒ Object 
  

  

  

  
    
      

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
29
30
```

    
    
      

```
# File 'lib/generators/websocket_rails/install/install_generator.rb', line 18

def inject_websocket_rails_client
  manifest = options[:manifest]
  js_path  = "app/assets/javascripts"

  create_file("#{js_path}/#{manifest}") unless File.exists?("#{js_path}/#{manifest}")

  append_to_file "#{js_path}/#{manifest}" do
    out = ""
    out << "//= require websocket_rails/main"
    out << "\n"
    out << "\n"
  end
end
```