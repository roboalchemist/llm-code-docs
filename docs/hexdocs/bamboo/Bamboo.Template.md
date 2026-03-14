# 
      Bamboo.Template 
      (bamboo v2.5.0)

    

      
        **
        View Source
      

  

Render emails with layouts, view modules, and templates.

This module allows rendering emails with layouts and views. Pass an
atom (e.g. `:welcome_email`) as the template name to render both HTML and
plain text emails. Use a string if you only want to render one type, e.g.
`"welcome_email.text"` or `"welcome_email.html"`.
## **Examples

*Set the text and HTML layout for an email.*

```
defmodule MyApp.Email do
  use Bamboo.Template, view: MyApp.Email.AccountView

  def welcome_email do
    new_email()
    |> put_text_layout({MyApp.Email.LayoutView, "email.text"})
    |> put_html_layout({MyApp.Email.LayoutView, "email.html"})
    |> render(:welcome) # Pass atom to render html AND plain text templates
  end
end
```

*You can optionally pass the html and text layouts when calling `use Bamboo.Template`*

```
defmodule MyApp.Email do
  use Bamboo.Template,
    view: MyApp.Email.AccountView
    text_layout: {MyApp.Email.LayoutView, "email.text"},
    html_layout: {MyApp.Email.LayoutView, "email.html"}

  def welcome_email do
    new_email()
    |> render(:welcome) # Pass atom to render html AND plain text templates
  end
end
```

*Set both the text and HTML layout at the same time for an email.*

```
defmodule MyApp.Email do
  use Bamboo.Template, view: MyApp.Email.AccountView

  def welcome_email do
    new_email()
    |> put_layout({MyApp.Email.LayoutView, :email})
    |> render(:welcome)
  end
end
```

*Render both text and html emails without layouts.*

```
defmodule MyApp.Email do
  use Bamboo.Template, view: MyApp.Email.AccountView

  def welcome_email do
    new_email()
    |> render(:welcome)
  end
end
```

*Make assigns available to a template.*

```
defmodule MyApp.Email do
  use Bamboo.Template, view: MyApp.Email.AccountView

  def welcome_email(user) do
    new_email()
    |> assign(:user, user)
    |> render(:welcome)
  end
end
```

*Make assigns available to a template during render call.*

```
defmodule MyApp.Email do
  use Bamboo.Template, view: MyApp.Email.AccountView

  def welcome_email(user) do
    new_email()
    |> render(:welcome, user: user)
  end
end
```

*Render an email by passing the template string to render.*

```
defmodule MyApp.Email do
  use Bamboo.Template, view: MyApp.Email.AccountView

  def html_email do
    new_email()
    |> render("html_email.html")
  end

  def text_email do
    new_email
    |> render("text_email.text")
  end
end
```

## **HTML Layout Example

```
# lib/my_app/email.ex
defmodule MyApp.Email do
  use Bamboo.Template, view: MyApp.Email.AccountView

  def welcome_email(person) do
    base_email()
    |> to(person)
    |> subject("Welcome to MyApp")
    |> assign(:person, person)
    |> render(:welcome_email)
  end

  defp base_email do
    new_email()
    |> from("Rob Ot<robot@changelog.com>")
    |> put_header("Reply-To", "editors@changelog.com")
    # This will use the "email.html.eex" file as a layout when rendering html emails.
    # Plain text emails will not use a layout unless you use `put_text_layout`
    |> put_html_layout({MyApp.Email.LayoutView, "email.html"})
  end
end

# lib/my_app/email/views/layout_view.ex
defmodule MyApp.Email.LayoutView do
  use Bamboo.View, path: "lib/my_app/email/templates/layout"
end

# lib/my_app/email/templates/layout/email.html.eex
<html>
  <body>
    <%= @inner_content %>
  </body>
</html>

# lib/my_app/email/views/account_view.ex
defmodule MyApp.Email.AccountView do
  use Bamboo.View, path: "lib/my_app/email/templates/account"
end

# lib/my_app/email/templates/account/welcome_email.html.eex
# This will be rendered within a layout because `put_html_layout` was used.
<p>Welcome <%= @person.name %></p>

# lib/my_app/email/templates/account/welcome_email.text.eex
# This will not be rendered within a layout because `put_text_layout` was not used.
Welcome <%= @person.name %>
```

    

    
# 
      
        **
      
      Summary
    

  
## 
    Functions
  

    
      
        assign(email, attrs)

      

        

Sets many assigns for an email. Accepts a map or a keyword list. See
`assign/3` for more.

    

    
      
        assign(email, key, value)

      

        

Sets an assign for the email. These will be available when rendering the email.

    

    
      
        put_html_layout(email, layout)

      

        

Sets the layout when rendering HTML templates.

    

    
      
        put_layout(email, arg)

      

        

Sets the layout for rendering plain text and HTML templates.

    

    
      
        put_text_layout(email, layout)

      

        

Sets the layout when rendering plain text templates.

    

    
      
        put_view(email, view)

      

        

Overrides the view for rendering templates

    

    
      
        render(email, template_name, assigns)

      

        

Render a template and set the body on the email.

    

  

    
# 
      
        **
      
      Functions
    

    

  
    
      **
    
    
      
# assign(email, attrs)

        
          **
        

    
  

  

      

          

```
@spec assign(
  %{:assigns => any(), optional(any()) => any()},
  maybe_improper_list() | map()
) :: %{
  :assigns => any(),
  optional(any()) => any()
}
```

      

Sets many assigns for an email. Accepts a map or a keyword list. See
`assign/3` for more.
## **Example

```
new_email()
|> assign(%{user: user})
|> render(:template_name)

new_email()
|> assign(user: user)
|> render(:template_name)
```

  

  
    
      **
    
    
      
# assign(email, key, value)

        
          **
        

    
  

  

Sets an assign for the email. These will be available when rendering the email.
## **Example

```
new_email()
# assigns user to be accessed as `@user` in template
|> assign(:user, user)
|> render(:template_name)
```

  

  
    
      **
    
    
      
# put_html_layout(email, layout)

        
          **
        

    
  

  

Sets the layout when rendering HTML templates.
## **Example

```
def html_email_layout do
  new_email
  # Will use the email.html template of MyApp.LayoutView when rendering html emails
  |> put_html_layout({MyApp.LayoutView, "email.html"})
end
```

  

  
    
      **
    
    
      
# put_layout(email, arg)

        
          **
        

    
  

  

Sets the layout for rendering plain text and HTML templates.
## **Example

```
def text_and_html_email_layout do
  new_email
  # Will use email.html and email.text templates of MyApp.LayoutView
  # when rendering HTML and text emails
  |> put_layout({MyAppWeb.LayoutView, :email})
end
```

  

  
    
      **
    
    
      
# put_text_layout(email, layout)

        
          **
        

    
  

  

Sets the layout when rendering plain text templates.
## **Example

```
def text_email_layout do
  new_email
  # Will use the email.text template of MyApp.LayoutView when rendering text emails
  |> put_text_layout({MyApp.LayoutView, "email.text"})
end
```

  

  
    
      **
    
    
      
# put_view(email, view)

        
          **
        

    
  

  

Overrides the view for rendering templates
## **Example

```
defmodule MyApp.Email do
  use Bamboo.Template, view: MyApp.EmailView

  def different_view_template do
    new_email
    # Will use welcome.html template of MyApp.AccountView
    |> put_view(MyApp.AccountView)
    |> render("welcome.html")
  end
end
```

  

  
    
      **
    
    
      
# render(email, template_name, assigns)

        
          **
        

    
  

  

Render a template and set the body on the email.

Pass an atom as the template name to render HTML *and* plain text emails,
e.g. `:welcome_email`. Use a string if you only want to render one type, e.g.
`"welcome_email.text"` or `"welcome_email.html"`.

You can also optionally pass assigns.
## **Example

```
# renders both HTML and text emails
render(new_email(), :template_name)

# renders HTML template
render(new_email(), "template_name.html")

# renders text template
render(new_email(), "template_name.text")

# renders with assigns
render(new_email(), :template_name, user: user)
```