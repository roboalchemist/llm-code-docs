# 
      Bamboo.Attachment 
      (bamboo v2.5.0)

    

      
        **
        View Source
      

  

    

    
# 
      
        **
      
      Summary
    

  
## 
    Types
  

    
      
        t()

      

    

  
## 
    Functions
  

    
      
        new(path, opts \\ [])

      

        

Creates a new Attachment

    

  

    
# 
      
        **
      
      Types
    

    

  
    
      **
    
    
      
# t()

        
          **
        

    
  

  

      

          

```
@type t() :: %Bamboo.Attachment{
  content_id: nil | String.t(),
  content_type: nil | String.t(),
  data: nil | binary(),
  filename: nil | String.t(),
  path: nil | String.t()
}
```

      

  

    
# 
      
        **
      
      Functions
    

    

    

  
    
      **
    
    
      
# new(path, opts \\ [])

        
          **
        

    
  

  

Creates a new Attachment

`content_id` can be used to embed an image, attach it and reference it in the message body by
setting its CID (Content-ID) and using a standard HTML tag:

```
<img src="cid:some-image-cid" alt="img" />
```

within an HTML email message.

Examples:

```
Bamboo.Attachment.new("/path/to/attachment.png")
Bamboo.Attachment.new("/path/to/attachment.png", filename: "image.png")
Bamboo.Attachment.new("/path/to/attachment.png", filename: "image.png", content_type: "image/png", content_id: "12387432")
Bamboo.Attachment.new(params["file"]) # Where params["file"] is a %Plug.Upload

email
|> put_html_layout({LayoutView, "email.html"})
|> put_attachment(%Bamboo.Attachment{content_type: "image/png", filename: "logo.png", data: "content", content_id: "2343333333"})
```