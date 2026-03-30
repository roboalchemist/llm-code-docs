# Module: Nokogiri::XML::PP::CharacterData
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    CharacterData
  
  

  
  
    Defined in:
    lib/nokogiri/xml/pp/character_data.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**inspect**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**pretty_print**(pp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**inspect**  ⇒ Object 
  

  

  

  
    
      

```

15
16
17
```

    
    
      

```
# File 'lib/nokogiri/xml/pp/character_data.rb', line 15

def inspect
  "#<#{self.class.name}:#{format("0x%x", object_id)} #{text.inspect}>"
end

```

    
  

    
      
  
### 
  
    #**pretty_print**(pp)  ⇒ Object 
  

  

  

  
    
      

```

8
9
10
11
12
13
```

    
    
      

```
# File 'lib/nokogiri/xml/pp/character_data.rb', line 8

def pretty_print(pp)
  nice_name = self.class.name.split("::").last
  pp.group(2, "#(#{nice_name} ", ")") do
    pp.pp(text)
  end
end

```