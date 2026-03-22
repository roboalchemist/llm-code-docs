# Class: PDF::Core::Reference
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- PDF::Core::Reference
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/prawn/security.rb
  
  

  
    
## 
      Experimental API
      collapse
    

    

      
        
- 
  
    
      #**encrypted_object**(key)  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the object definition for the object this references, keyed from `key`.

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**encrypted_object**(key)  ⇒ String 
  

  

  

  
    

Returns the object definition for the object this references, keyed from `key`.

  

  

Parameters:

  
    
- 
      
      
      
      
    
  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
```

    
    
      

```
# File 'lib/prawn/security.rb', line 290

def encrypted_object(key)
  @on_encode&.call(self)

  output = +"#{@identifier} #{gen} obj\n"
  if @stream.empty?
    output <<
      PDF::Core.encrypted_pdf_object(data, key, @identifier, gen) << "\n"
  else
    output << PDF::Core.encrypted_pdf_object(
      data.merge(@stream.data), key, @identifier, gen,
    ) << "\n" <<
      @stream.encrypted_object(key, @identifier, gen)
  end

  output << "endobj\n"
end

```