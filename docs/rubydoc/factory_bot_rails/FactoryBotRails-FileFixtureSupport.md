# Module: FactoryBotRails::FileFixtureSupport
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/factory_bot_rails/file_fixture_support.rb
  
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**included**(klass)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**included**(klass)  ⇒ Object 
  

  

  

  
    
      

```

3
4
5
6
7
```

    
    
      

```
# File 'lib/factory_bot_rails/file_fixture_support.rb', line 3

def self.included(klass)
  klass.cattr_accessor :file_fixture_support

  klass.delegate :file_fixture, to: "self.class.file_fixture_support"
end
```