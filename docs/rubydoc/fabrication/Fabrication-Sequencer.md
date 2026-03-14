# Class: Fabrication::Sequencer
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Fabrication::Sequencer
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Singleton
  
  
  

  

  
  
    Defined in:
    lib/fabrication/sequencer.rb
  
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        DEFAULT =
          
        
        

```
:_default
```

      
    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**clear**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**sequence**(name = DEFAULT, start = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**reset**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**sequence**(name = DEFAULT, start = nil, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**sequence_blocks**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**sequences**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  

  
    
## Class Method Details

    
      
  
### 
  
    .**clear**  ⇒ Object 
  

  

  

  
    
      

```

13
14
15
16
```

    
    
      

```
# File 'lib/fabrication/sequencer.rb', line 13

def self.clear
  instance.sequences.clear
  instance.sequence_blocks.clear
end
```

    
  

    
      
  
### 
  
    .**sequence**(name = DEFAULT, start = nil)  ⇒ Object 
  

  

  

  
    
      

```

9
10
11
```

    
    
      

```
# File 'lib/fabrication/sequencer.rb', line 9

def self.sequence(name = DEFAULT, start = nil, &)
  instance.sequence(name, start, &)
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**reset**  ⇒ Object 
  

  

  

  
    
      

```

37
38
39
40
41
```

    
    
      

```
# File 'lib/fabrication/sequencer.rb', line 37

def reset
  Fabrication::Config.sequence_start = nil
  @sequences = nil
  @sequence_blocks = nil
end
```

    
  

    
      
  
### 
  
    #**sequence**(name = DEFAULT, start = nil, &block)  ⇒ Object 
  

  

  

  
    
      

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
```

    
    
      

```
# File 'lib/fabrication/sequencer.rb', line 18

def sequence(name = DEFAULT, start = nil, &block)
  idx = sequences[name] ||= start || Fabrication::Config.sequence_start
  if block
    sequence_blocks[name] = block.to_proc
  else
    sequence_blocks[name] ||= ->(i) { i }
  end.call(idx).tap do
    sequences[name] = idx.succ
  end
end
```

    
  

    
      
  
### 
  
    #**sequence_blocks**  ⇒ Object 
  

  

  

  
    
      

```

33
34
35
```

    
    
      

```
# File 'lib/fabrication/sequencer.rb', line 33

def sequence_blocks
  @sequence_blocks ||= {}
end
```

    
  

    
      
  
### 
  
    #**sequences**  ⇒ Object 
  

  

  

  
    
      

```

29
30
31
```

    
    
      

```
# File 'lib/fabrication/sequencer.rb', line 29

def sequences
  @sequences ||= {}
end
```