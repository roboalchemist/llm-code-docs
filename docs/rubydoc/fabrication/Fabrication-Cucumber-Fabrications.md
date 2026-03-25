# Class: Fabrication::Cucumber::Fabrications
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Fabrication::Cucumber::Fabrications
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Singleton
  
  
  

  

  
  
    Defined in:
    lib/fabrication/cucumber/step_fabricator.rb
  
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**[]**(fabricator)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**[]=**(fabricator, fabrication)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**fabrications**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**fabrications**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  

  
    
## Class Method Details

    
      
  
### 
  
    .**[]**(fabricator)  ⇒ Object 
  

  

  

  
    
      

```

97
98
99
```

    
    
      

```
# File 'lib/fabrication/cucumber/step_fabricator.rb', line 97

def self.[](fabricator)
  instance.fabrications[fabricator.to_sym]
end

```

    
  

    
      
  
### 
  
    .**[]=**(fabricator, fabrication)  ⇒ Object 
  

  

  

  
    
      

```

101
102
103
```

    
    
      

```
# File 'lib/fabrication/cucumber/step_fabricator.rb', line 101

def self.[]=(fabricator, fabrication)
  instance.fabrications[fabricator.to_sym] = fabrication
end

```

    
  

    
      
  
### 
  
    .**fabrications**  ⇒ Object 
  

  

  

  
    
      

```

93
94
95
```

    
    
      

```
# File 'lib/fabrication/cucumber/step_fabricator.rb', line 93

def self.fabrications
  instance.fabrications
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**fabrications**  ⇒ Object 
  

  

  

  
    
      

```

105
106
107
```

    
    
      

```
# File 'lib/fabrication/cucumber/step_fabricator.rb', line 105

def fabrications
  @fabrications ||= {}
end

```