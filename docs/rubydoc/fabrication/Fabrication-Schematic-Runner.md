# Class: Fabrication::Schematic::Runner
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Fabrication::Schematic::Runner
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/fabrication/schematic/runner.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**klass**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute klass.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(klass)  ⇒ Runner 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Runner.

  

      
        
- 
  
    
      #**sequence**(name = Fabrication::Sequencer::DEFAULT, start = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(klass)  ⇒ Runner 
  

  

  

  
    

Returns a new instance of Runner.

  

  

  
    
      

```

6
7
8
```

    
    
      

```
# File 'lib/fabrication/schematic/runner.rb', line 6

def initialize(klass)
  self.klass = klass
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**klass**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute klass.

  

  

  
    
      

```

4
5
6
```

    
    
      

```
# File 'lib/fabrication/schematic/runner.rb', line 4

def klass
  @klass
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**sequence**(name = Fabrication::Sequencer::DEFAULT, start = nil)  ⇒ Object 
  

  

  

  
    
      

```

10
11
12
13
```

    
    
      

```
# File 'lib/fabrication/schematic/runner.rb', line 10

def sequence(name = Fabrication::Sequencer::DEFAULT, start = nil, &)
  name = "#{klass.to_s.downcase.gsub('::', '_')}_#{name}"
  Fabrication::Sequencer.sequence(name, start, &)
end
```