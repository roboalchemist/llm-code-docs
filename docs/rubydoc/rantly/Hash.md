# Class: Hash
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Hash
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/rantly/shrinks.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**retry?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**shrink**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**shrinkable?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**retry?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

189
190
191
```

    
    
      

```
# File 'lib/rantly/shrinks.rb', line 189

def retry?
  false
end

```

    
  

    
      
  
### 
  
    #**shrink**  ⇒ Object 
  

  

  

  
    
      

```

168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
```

    
    
      

```
# File 'lib/rantly/shrinks.rb', line 168

def shrink
  if any? { |_, v| v.respond_to?(:shrinkable?) && v.shrinkable? }
    key, = detect { |_, v| v.respond_to?(:shrinkable?) && v.shrinkable? }
    clone = dup
    clone[key] = clone[key].shrink
    clone
  elsif !empty?
    key = keys.first
    h2 = dup
    h2.delete(key)
    h2
  else
    self
  end
end

```

    
  

    
      
  
### 
  
    #**shrinkable?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

184
185
186
187
```

    
    
      

```
# File 'lib/rantly/shrinks.rb', line 184

def shrinkable?
  any? { |_, v| v.respond_to?(:shrinkable?) && v.shrinkable? } ||
    !empty?
end

```