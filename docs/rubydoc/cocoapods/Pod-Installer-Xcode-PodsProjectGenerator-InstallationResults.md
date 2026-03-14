# Class: Pod::Installer::Xcode::PodsProjectGenerator::InstallationResults
  
  
  

  
  
    Inherits:
    
      Struct
      
        

          
- Object
          
            
- Struct
          
            
- Pod::Installer::Xcode::PodsProjectGenerator::InstallationResults
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/cocoapods/installer/xcode/pods_project_generator.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**aggregate_target_installation_results**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      #**pod_target_installation_results**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    
  

    
  

  
  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**aggregate_target_installation_results**  ⇒ Object  (readonly)
  

  

  

  
    
      

```

95
```

    
    
      

```
# File 'lib/cocoapods/installer/xcode/pods_project_generator.rb', line 95

InstallationResults = Struct.new(:pod_target_installation_results, :aggregate_target_installation_results)
```

    
  

    
      
      
      
  
### 
  
    #**pod_target_installation_results**  ⇒ Object  (readonly)
  

  

  

  
    
      

```

95
```

    
    
      

```
# File 'lib/cocoapods/installer/xcode/pods_project_generator.rb', line 95

InstallationResults = Struct.new(:pod_target_installation_results, :aggregate_target_installation_results)
```