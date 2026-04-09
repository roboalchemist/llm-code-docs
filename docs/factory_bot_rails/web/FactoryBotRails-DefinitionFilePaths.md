# Class: FactoryBotRails::DefinitionFilePaths
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- FactoryBotRails::DefinitionFilePaths
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/factory_bot_rails/definition_file_paths.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**any?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**directories**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**files**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(definition_file_paths)  ⇒ DefinitionFilePaths 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of DefinitionFilePaths.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(definition_file_paths)  ⇒ DefinitionFilePaths 
  

  

  

  
    

Returns a new instance of DefinitionFilePaths.

  

  

  
    
      

```

5
6
7
8
9
10
11
12
13
```

    
    
      

```
# File 'lib/factory_bot_rails/definition_file_paths.rb', line 5

def initialize(definition_file_paths)
  @files = []
  @directories = {}

  definition_file_paths.each do |path|
    @files << "#{path}.rb"
    @directories[path.to_s] = [:rb]
  end
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**any?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

23
24
25
```

    
    
      

```
# File 'lib/factory_bot_rails/definition_file_paths.rb', line 23

def any?
  directories.any? || files.any?
end
```

    
  

    
      
  
### 
  
    #**directories**  ⇒ Object 
  

  

  

  
    
      

```

15
16
17
```

    
    
      

```
# File 'lib/factory_bot_rails/definition_file_paths.rb', line 15

def directories
  @directories.select { |path| Dir.exist?(path) }
end
```

    
  

    
      
  
### 
  
    #**files**  ⇒ Object 
  

  

  

  
    
      

```

19
20
21
```

    
    
      

```
# File 'lib/factory_bot_rails/definition_file_paths.rb', line 19

def files
  @files.select { |file| File.exist?(file) }
end
```