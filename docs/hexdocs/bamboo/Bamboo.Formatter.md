# 
      Bamboo.Formatter protocol
      (bamboo v2.5.0)

    

      
        **
        View Source
      

  

Converts data to email addresses.

Implementations of the `Bamboo.Formatter` protocol convert a given data
structure to a two item tuple of `{name, address}` or an address string. The
`opts` argument is a map with the key `:type` and a value of `:from`, `:to`,
`:cc`, or `:bcc`. The options argument allows functions to pattern match an
address type and format a given data structure differently for different
types of addresses.
## **Simple example

Let's say you have a user struct like this.

```
defmodule MyApp.User do
  defstruct first_name: nil, last_name: nil, email: nil
end
```

Bamboo can automatically format this struct if you implement the `Bamboo.Formatter`
protocol.

```
defimpl Bamboo.Formatter, for: MyApp.User do
  # Used by `to`, `bcc`, `cc` and `from`
  def format_email_address(user, _opts) do
    fullname = "#{user.first_name} #{user.last_name}"
    {fullname, user.email}
  end
end
```

Now you can create emails like this, and the user will be formatted correctly

```
user = %User{first_name: "John", last_name: "Doe", email: "me@example.com"}
Bamboo.Email.new_email(from: user)
```

## **Customize formatting based on from, to, cc or bcc

By pattern matching the `opts` argument, you can format a given data
structure differently for different types of addresses. For example, if you
want to provide the name of the app when sending email on behalf of a user,
you can format the name for all `type: :from` addresses.

```
defimpl Bamboo.Formatter, for: MyApp.User do
  # Include the app name when used in a from address
  def format_email_address(user, %{type: :from}) do
    fullname = "#{user.first_name} #{user.last_name}"
    {fullname <> " (Sent from MyApp)", user.email}
  end

  # Just use the name for all other types
  def format_email_address(user, _opts) do
    fullname = "#{user.first_name} #{user.last_name}"
    {fullname, user.email}
  end
end
```

    

    
# 
      
        **
      
      Summary
    

  
## 
    Types
  

    
      
        opts()

      

    

    
      
        t()

      

        

All the types that implement this protocol.

    

  
## 
    Functions
  

    
      
        format_email_address(data, opts)

      

        

Receives data and opts and returns a string, a two item tuple `{name, address}`, or a list of either.

    

  

    
# 
      
        **
      
      Types
    

    

  
    
      **
    
    
      
# opts()

        
          **
        

    
  

  

      

          

```
@type opts() :: %{optional(:type) => :from | :to | :cc | :bcc}
```

      

  

  
    
      **
    
    
      
# t()

        
          **
        

    
  

  

      

          

```
@type t() :: term()
```

      

All the types that implement this protocol.
  

    
# 
      
        **
      
      Functions
    

    

  
    
      **
    
    
      
# format_email_address(data, opts)

        
          **
        

    
  

  

      

          

```
@spec format_email_address(any(), opts()) :: Bamboo.Email.address_list()
```

      

Receives data and opts and returns a string, a two item tuple `{name, address}`, or a list of either.

opts is a map with the key `:type` and a value of
`:from`, `:to`, `:cc` or `:bcc`. You can pattern match on this to customize
the address.