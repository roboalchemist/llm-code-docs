# Class: Rails::Generators::ChannelGenerator
  
  
  

  
  
    Inherits:
    
      NamedBase
      
        

          
- Object
          
            
- NamedBase
          
            
- Rails::Generators::ChannelGenerator
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/rails/generators/channel/channel_generator.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**create_channel_files**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**create_channel_files**  ⇒ Object 
  

  

  

  
    
      

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
31
32
33
34
35
36
37
```

    
    
      

```
# File 'lib/rails/generators/channel/channel_generator.rb', line 18

def create_channel_files
  create_shared_channel_files
  create_channel_file

  if using_javascript?
    if first_setup_required?
      create_shared_channel_javascript_files
      import_channels_in_javascript_entrypoint

      if using_importmap?
        pin_javascript_dependencies
      elsif using_js_runtime?
        install_javascript_dependencies
      end
    end

    create_channel_javascript_file
    import_channel_in_javascript_entrypoint
  end
end
```