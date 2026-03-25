# Class: SimpleForm::Tags::CollectionCheckBoxes
  
  
  

  
  
    Inherits:
    
      ActionView::Helpers::Tags::CollectionCheckBoxes
      
        

          
- Object
          
            
- ActionView::Helpers::Tags::CollectionCheckBoxes
          
            
- SimpleForm::Tags::CollectionCheckBoxes
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      CollectionExtensions
  
  
  

  

  
  
    Defined in:
    lib/simple_form/tags.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**render**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**render**  ⇒ Object 
  

  

  

  
    
      

```

60
61
62
```

    
    
      

```
# File 'lib/simple_form/tags.rb', line 60

def render
  wrap_rendered_collection(super)
end
```