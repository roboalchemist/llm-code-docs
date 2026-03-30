# 
      Bamboo.Email 
      (bamboo v2.5.0)

    

      
        **
        View Source
      

  

Contains functions for composing emails.

Bamboo separates composing emails from delivering them. This separation makes
emails easy to test and makes things like using a default layout or a default
from address easy to do. This module is for creating emails. To actually send
them, use Bamboo.Mailer.
## **Handling email addresses

The from, to, cc, and bcc addresses of a `Bamboo.Email` can be set to any
data structure for which there is an implementation of the
Bamboo.Formatter protocol or a list of such data
structures. Bamboo includes implementations for some common data structures
or you can create your own. All from, to, cc, and bcc addresses are
normalized internally to a two item tuple of `{name, address}`. See
Bamboo.Formatter for more info.
## **Simplest way to create a new email

```
defmodule MyApp.Email do
  import Bamboo.Email

  def welcome_email(user) do
    new_email(
      from: "me@app.com",
      to: user,
      subject: "Welcome!",
      text_body: "Welcome to the app",
      html_body: "<strong>Welcome to the app</strong>"
    )
  end
end
```

## **Extracting common parts (default layout, default from address, etc.)

Let's say you want all emails to have the same from address. Here's how you
could do that

```
defmodule MyApp.Email do
  import Bamboo.Email

  def welcome_email(user) do
    # Since new_email/1 returns a struct you can update it with Kernel.struct!/2
    struct!(base_email(),
      to: user,
      subject: "Welcome!",
      text_body: "Welcome to the app",
      html_body: "<strong>Welcome to the app</strong>"
    )
  end

  def base_email do
    new_email(from: "me@app.com")
  end
end
```

In addition to keyword lists, `Bamboo.Email`s can also be built using function pipelines.

```
defmodule MyApp.Email do
  import Bamboo.Email

  def welcome_email(user) do
    base_email()
    |> to(user)
    |> subject("Welcome!")
    |> text_body("Welcome to the app")
    |> html_body("<strong>Welcome to the app</strong>")
  end
end
```

    

    
# 
      
        **
      
      Summary
    

  
## 
    Types
  

    
      
        address()

      

    

    
      
        address_list()

      

    

    
      
        t()

      

    

  
## 
    Functions
  

    
      
        all_recipients(email)

      

        

Returns a list of all recipients (to, cc and bcc).

    

    
      
        bcc(email, attr)

      

        

Sets the `bcc` on the email.

    

    
      
        block(email)

      

        

Marks an email as blocked to prevent it from being sent out. This is meant to
be used from an interceptor. To learn more about interceptors, see the
`Bamboo.Interceptor` behaviour.

    

    
      
        cc(email, attr)

      

        

Sets the `cc` on the email.

    

    
      
        from(email, attr)

      

        

Sets the `from` on the email.

    

    
      
        get_address(invalid_address)

      

        

Gets just the email address from a normalized email address

    

    
      
        html_body(email, attr)

      

        

Sets the html_body on the email

    

    
      
        new_email(attrs \\ [])

      

        

Used to create a new email

    

    
      
        put_attachment(email, attachment)

      

        

Adds a data attachment to the email

    

    
      
        put_attachment(email, path, opts \\ [])

      

        

Adds a file attachment to the email

    

    
      
        put_header(email, header_name, value)

      

        

Adds a header to the email

    

    
      
        put_private(email, key, value)

      

        

Adds a key/value to the private key of the email

    

    
      
        subject(email, attr)

      

        

Sets the subject on the email

    

    
      
        text_body(email, attr)

      

        

Sets the text_body on the email

    

    
      
        to(email, attr)

      

        

Sets the `to` on the email.

    

  

    
# 
      
        **
      
      Types
    

    

  
    
      **
    
    
      
# address()

        
          **
        

    
  

  

      

          

```
@type address() :: {String.t(), String.t()}
```

      

  

  
    
      **
    
    
      
# address_list()

        
          **
        

    
  

  

      

          

```
@type address_list() :: nil | address() | [address()] | any()
```

      

  

  
    
      **
    
    
      
# t()

        
          **
        

    
  

  

      

          

```
@type t() :: %Bamboo.Email{
  assigns: %{required(atom()) => any()},
  attachments: term(),
  bcc: address_list(),
  blocked: boolean(),
  cc: address_list(),
  from: term(),
  headers: %{required(String.t()) => String.t()},
  html_body: nil | String.t(),
  private: %{required(atom()) => any()},
  subject: nil | String.t(),
  text_body: nil | String.t(),
  to: address_list()
}
```

      

  

    
# 
      
        **
      
      Functions
    

    

  
    
      **
    
    
      
# all_recipients(email)

        
          **
        

    
  

  

      

          

```
@spec all_recipients(t()) :: [address()] | no_return()
```

      

Returns a list of all recipients (to, cc and bcc).
  

  
    
      **
    
    
      
# bcc(email, attr)

        
          **
        

    
  

  

      

          

```
@spec bcc(t(), address_list()) :: t()
```

      

Sets the `bcc` on the email.

`bcc` receives as an argument any data structure for which
there is an implementation of the `Bamboo.Formatter` protocol.

```
new_email()
|> bcc(["sally@example.com", "james@example.com"])
```

  

  
    
      **
    
    
      
# block(email)

        
          **
        

    
  

  

Marks an email as blocked to prevent it from being sent out. This is meant to
be used from an interceptor. To learn more about interceptors, see the
`Bamboo.Interceptor` behaviour.
## **Example

```
iex> Bamboo.Email.block(%Bamboo.Email{blocked: false})
%Bamboo.Email{blocked: true}
```

  

  
    
      **
    
    
      
# cc(email, attr)

        
          **
        

    
  

  

      

          

```
@spec cc(t(), address_list()) :: t()
```

      

Sets the `cc` on the email.

`cc` receives as an argument any data structure for which
there is an implementation of the `Bamboo.Formatter` protocol.

```
new_email()
|> cc(["sally@example.com", "james@example.com"])
```

  

  
    
      **
    
    
      
# from(email, attr)

        
          **
        

    
  

  

      

          

```
@spec from(t(), address_list()) :: t()
```

      

Sets the `from` on the email.

`from` receives as an argument any data structure for which
there is an implementation of the `Bamboo.Formatter` protocol.

```
new_email()
|> from(["sally@example.com", "james@example.com"])
```

  

  
    
      **
    
    
      
# get_address(invalid_address)

        
          **
        

    
  

  

      

          

```
@spec get_address(address()) :: String.t() | no_return()
```

      

Gets just the email address from a normalized email address

Normalized email addresses are 2 item tuples {name, address}. This gets the
address part of the tuple. Use this instead of calling `elem(address, 1)`
so that if Bamboo changes how email addresses are represented your code will
still work
## **Examples

```
Bamboo.Email.get_address({"Paul", "paul@thoughtbot.com"}) # "paul@thoughtbot.com"
```

  

  
    
      **
    
    
      
# html_body(email, attr)

        
          **
        

    
  

  

Sets the html_body on the email
  

    

  
    
      **
    
    
      
# new_email(attrs \\ [])

        
          **
        

    
  

  

      

          

```
@spec new_email(Enum.t()) :: t()
```

      

Used to create a new email

If called without arguments it is the same as creating an empty
`%Bamboo.Email{}` struct. If called with arguments it will populate the struct
with given attributes.
## **Example

```
# Same as %Bamboo.Email{from: "support@myapp.com"}
new_email(from: "support@myapp.com")
```

  

  
    
      **
    
    
      
# put_attachment(email, attachment)

        
          **
        

    
  

  

Adds a data attachment to the email
## **Example

```
put_attachment(email, %Bamboo.Attachment{})
```

Requires the fields filename and data of the `%Bamboo.Attachment{}` struct to be set.
## **Example

```
def create(conn, params) do
  #...
  email
  |> put_attachment(%Bamboo.Attachment{filename: "event.ics", data: "BEGIN:VCALENDAR..."})
  #...
end
```

  

  
    
      **
    
    
      
# put_attachment(email, path, opts \\ [])

        
          **
        

    
  

  

Adds a file attachment to the email
## **Example

```
put_attachment(email, path, opts \\ [])
```

Accepts `filename: <name>` and `content_type: <type>` options.

If you are using Plug, it accepts a Plug.Upload struct
## **Example

```
def create(conn, params) do
  #...
  email
  |> put_attachment(params["file"])
  #...
end
```

  

  
    
      **
    
    
      
# put_header(email, header_name, value)

        
          **
        

    
  

  

      

          

```
@spec put_header(t(), String.t(), String.t()) :: t()
```

      

Adds a header to the email
## **Example

```
put_header(email, "Reply-To", "support@myapp.com")
```

  

  
    
      **
    
    
      
# put_private(email, key, value)

        
          **
        

    
  

  

      

          

```
@spec put_private(t(), atom(), any()) :: t()
```

      

Adds a key/value to the private key of the email

This is mostly used to implement specific functionality for a particular
adapter. It will rarely be used directly from your code. Internally this is
used to set Mandrill specific params for the MandrillAdapter and it's also
used to store the view module, template and layout when using Bamboo.Phoenix.
## **Example

```
put_private(email, :tags, "welcome-email")
```

  

  
    
      **
    
    
      
# subject(email, attr)

        
          **
        

    
  

  

Sets the subject on the email
  

  
    
      **
    
    
      
# text_body(email, attr)

        
          **
        

    
  

  

Sets the text_body on the email
  

  
    
      **
    
    
      
# to(email, attr)

        
          **
        

    
  

  

      

          

```
@spec to(t(), address_list()) :: t()
```

      

Sets the `to` on the email.

`to` receives as an argument any data structure for which
there is an implementation of the `Bamboo.Formatter` protocol.

```
new_email()
|> to(["sally@example.com", "james@example.com"])
```