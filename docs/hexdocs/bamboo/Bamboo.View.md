# 
      Bamboo.View 
      (bamboo v2.5.0)

    

      
        **
        View Source
      

  

Compiles and renders templates defined in a given path.

Functions defined in the view are available to use in its templates.
## **Example

```
defmodule MyApp.EmailView do
  use Bamboo.View, path: "lib/my_app/email/templates"

  def app_title do
    "My Super App"
  end
end

# lib/my_app/email_templates/welcome.html
<h1>Welcome to <%= app_title() %></h1>
```