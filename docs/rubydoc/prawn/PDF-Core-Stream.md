# Class: PDF::Core::Stream
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- PDF::Core::Stream
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/prawn/security.rb
  
  

  
    
## 
      Experimental API
      collapse
    

    

      
        
- 
  
    
      #**encrypted_object**(key, id, gen)  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Encrypt stream.

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**encrypted_object**(key, id, gen)  ⇒ String 
  

  

  

  
    

Encrypt stream.

  

  

Parameters:

  
    
- 
      
      
      
      
    
  
    
- 
      
      
      
      
    
  
    
- 
      
      
      
      
    
  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

270
271
272
273
274
275
276
277
278
279
280
```

    
    
      

```
# File 'lib/prawn/security.rb', line 270

def encrypted_object(key, id, gen)
  if filtered_stream
    "stream\n#{
      Prawn::Document::Security.encrypt_string(
        filtered_stream, key, id, gen,
      )
    }\nendstream\n"
  else
    ''
  end
end

```