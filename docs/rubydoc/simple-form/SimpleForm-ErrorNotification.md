# Class: SimpleForm::ErrorNotification
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- SimpleForm::ErrorNotification
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/simple_form/error_notification.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(builder, options)  ⇒ ErrorNotification 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of ErrorNotification.

  

      
        
- 
  
    
      #**render**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(builder, options)  ⇒ ErrorNotification 
  

  

  

  
    

Returns a new instance of ErrorNotification.

  

  

  
    
      

```

6
7
8
9
10
```

    
    
      

```
# File 'lib/simple_form/error_notification.rb', line 6

def initialize(builder, options)
  @builder = builder
  @message = options.delete(:message)
  @options = options
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**render**  ⇒ Object 
  

  

  

  
    
      

```

12
13
14
15
16
```

    
    
      

```
# File 'lib/simple_form/error_notification.rb', line 12

def render
  if has_errors?
    template.content_tag(error_notification_tag, error_message, html_options)
  end
end
```