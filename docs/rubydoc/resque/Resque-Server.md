# Class: Resque::Server
  
  
  

  
  
    Inherits:
    
      Sinatra::Base
      
        

          
- Object
          
            
- Sinatra::Base
          
            
- Resque::Server
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/resque/server.rb
  
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**tabs**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**url_prefix**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**url_prefix=**(url_prefix)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**resque**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**show**(page, layout = true)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**show_for_polling**(page)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  

  
    
## Class Method Details

    
      
  
### 
  
    .**tabs**  ⇒ Object 
  

  

  

  
    
      

```

179
180
181
```

    
    
      

```
# File 'lib/resque/server.rb', line 179

def self.tabs
  @tabs ||= ["Overview", "Working", "Failed", "Queues", "Workers", "Stats"]
end
```

    
  

    
      
  
### 
  
    .**url_prefix**  ⇒ Object 
  

  

  

  
    
      

```

187
188
189
```

    
    
      

```
# File 'lib/resque/server.rb', line 187

def self.url_prefix
  (@url_prefix.nil? || @url_prefix.empty?) ? '' : @url_prefix + '/'
end
```

    
  

    
      
  
### 
  
    .**url_prefix=**(url_prefix)  ⇒ Object 
  

  

  

  
    
      

```

183
184
185
```

    
    
      

```
# File 'lib/resque/server.rb', line 183

def self.url_prefix=(url_prefix)
  @url_prefix = url_prefix
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**resque**  ⇒ Object 
  

  

  

  
    
      

```

175
176
177
```

    
    
      

```
# File 'lib/resque/server.rb', line 175

def resque
  Resque
end
```

    
  

    
      
  
### 
  
    #**show**(page, layout = true)  ⇒ Object 
  

  

  

  
    
      

```

31
32
33
34
35
36
37
38
```

    
    
      

```
# File 'lib/resque/server.rb', line 31

def show(page, layout = true)
  response["Cache-Control"] = "max-age=0, private, must-revalidate"
  begin
    erb page.to_sym, {:layout => layout}, :resque => Resque
  rescue Errno::ECONNREFUSED
    erb :error, {:layout => false}, :error => "Can't connect to Redis! (#{Resque.redis_id})"
  end
end
```

    
  

    
      
  
### 
  
    #**show_for_polling**(page)  ⇒ Object 
  

  

  

  
    
      

```

40
41
42
43
44
```

    
    
      

```
# File 'lib/resque/server.rb', line 40

def show_for_polling(page)
  content_type "text/html"
  @polling = true
  show(page.to_sym, false).gsub(/\s{1,}/, ' ')
end
```