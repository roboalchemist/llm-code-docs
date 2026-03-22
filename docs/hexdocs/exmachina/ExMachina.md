# 

      
        **
        View Source
      

    ExMachina behaviour
    (ex_machina v2.8.0)

  

    

Defines functions for generating data

In depth examples are in the README
    

Defines functions for generating data

In depth examples are in the README
    

    
# 
      
        **
      
      Summary
    

  
## 
    Callbacks
  

    
      
        build(factory_name)

      

    

    
      
        build(factory_name, attrs)

      

    

    
      
        build_list(number_of_records, factory_name)

      

    

    
      
        build_list(number_of_records, factory_name, attrs)

      

    

    
      
        build_pair(factory_name)

      

    

    
      
        build_pair(factory_name, attrs)

      

    

  
## 
    Functions
  

    
      
        build(module, factory_name, attrs \\ %{})

      

        

Builds a single factory.

    

    
      
        build_list(module, number_of_records, factory_name, attrs \\ %{})

      

        

Builds any number of factories.

    

    
      
        build_pair(module, factory_name, attrs \\ %{})

      

        

Builds two factories.

    

    
      
        evaluate_lazy_attributes(factory)

      

        

Helper function to evaluate lazy attributes that are passed into a factory.

    

    
      
        merge_attributes(record, attrs)

      

        

Helper function to merge attributes into a factory that could be either a map
or a struct.

    

    
      
        sequence(name)

      

        

Shortcut for creating unique string values.

    

    
      
        sequence(name, formatter)

      

        

Create sequences for generating unique values.

    

    
      
        sequence(name, formatter, opts)

      

        

Similar to `sequence/2` but it allows for passing a `start_at` option
to the sequence generation.

    

  

    
# 
      
        **
      
      Callbacks
    

    

  
    
      **
      Link to this callback
    
    
# build(factory_name)

      
       **
       View Source
     

  

  

      

          

```
@callback build(factory_name :: atom()) :: any()
```

      

  

  
    
      **
      Link to this callback
    
    
# build(factory_name, attrs)

      
       **
       View Source
     

  

  

      

          

```
@callback build(factory_name :: atom(), attrs :: keyword() | map()) :: any()
```

      

  

  
    
      **
      Link to this callback
    
    
# build_list(number_of_records, factory_name)

      
       **
       View Source
     

  

  

      

          

```
@callback build_list(number_of_records :: integer(), factory_name :: atom()) :: list()
```

      

  

  
    
      **
      Link to this callback
    
    
# build_list(number_of_records, factory_name, attrs)

      
       **
       View Source
     

  

  

      

          

```
@callback build_list(
  number_of_records :: integer(),
  factory_name :: atom(),
  attrs :: keyword() | map()
) ::
  list()
```

      

  

  
    
      **
      Link to this callback
    
    
# build_pair(factory_name)

      
       **
       View Source
     

  

  

      

          

```
@callback build_pair(factory_name :: atom()) :: list()
```

      

  

  
    
      **
      Link to this callback
    
    
# build_pair(factory_name, attrs)

      
       **
       View Source
     

  

  

      

          

```
@callback build_pair(factory_name :: atom(), attrs :: keyword() | map()) :: list()
```

      

  

    
# 
      
        **
      
      Functions
    

    

    

  
    
      **
      Link to this function
    
    
# build(module, factory_name, attrs \\ %{})

      
       **
       View Source
     

  

  

Builds a single factory.

This will defer to the `[factory_name]_factory/0` callback defined in the
factory module in which it is `use`d.
### 
  
    **
  
  Example

```
def user_factory do
  %{name: "John Doe", admin: false}
end

# Returns %{name: "John Doe", admin: false}
build(:user)

# Returns %{name: "John Doe", admin: true}
build(:user, admin: true)
```

## 
  
    **
  
  Full control of a factory's attributes

If you want full control over the factory attributes, you can define the
factory with `[factory_name]_factory/1`, taking in the attributes as the first
argument.

Caveats:

- 

ExMachina will no longer merge the attributes for your factory. If you want
to do that, you can merge the attributes with the `merge_attributes/2` helper.
- 

ExMachina will no longer evaluate lazy attributes. If you want to do that,
you can evaluate the lazy attributes with the `evaluate_lazy_attributes/1`
helper.

### 
  
    **
  
  Example

```
def article_factory(attrs) do
  title = Map.get(attrs, :title, "default title")
  slug = Article.title_to_slug(title)

  article = %Article{title: title, slug: slug}

  article
  # merge attributes on your own
  |> merge_attributes(attrs)
  # evaluate any lazy attributes
  |> evaluate_lazy_attributes()
end

# Returns %Article{title: "default title", slug: "default-title"}
build(:article)

# Returns %Article{title: "hello world", slug: "hello-world"}
build(:article, title: "hello world")
```

  

    

  
    
      **
      Link to this function
    
    
# build_list(module, number_of_records, factory_name, attrs \\ %{})

      
       **
       View Source
     

  

  

Builds any number of factories.
## 
  
    **
  
  Example

```
# Returns a list of 3 users
build_list(3, :user)
```

  

    

  
    
      **
      Link to this function
    
    
# build_pair(module, factory_name, attrs \\ %{})

      
       **
       View Source
     

  

  

Builds two factories.

This is just an alias for `build_list(2, factory_name, attrs)`.
## 
  
    **
  
  Example

```
# Returns a list of 2 users
build_pair(:user)
```

  

  
    
      **
      Link to this function
    
    
# evaluate_lazy_attributes(factory)

      
       **
       View Source
     

  

  

      

          

```
@spec evaluate_lazy_attributes(struct() | map()) :: struct() | map()
```

      

Helper function to evaluate lazy attributes that are passed into a factory.
## 
  
    **
  
  Example

```
# custom factory
def article_factory(attrs) do
  %{title: "title"}
  |> merge_attributes(attrs)
  |> evaluate_lazy_attributes()
end

def author_factory do
  %{name: sequence("gandalf")}
end

# => returns [
#  %{title: "title", author: %{name: "gandalf0"},
#  %{title: "title", author: %{name: "gandalf0"}
# ]
build_pair(:article, author: build(:author))

# => returns [
#  %{title: "title", author: %{name: "gandalf0"},
#  %{title: "title", author: %{name: "gandalf1"}
# ]
build_pair(:article, author: fn -> build(:author) end)
```

  

  
    
      **
      Link to this function
    
    
# merge_attributes(record, attrs)

      
       **
       View Source
     

  

  

      

          

```
@spec merge_attributes(struct() | map(), map()) :: struct() | map() | no_return()
```

      

Helper function to merge attributes into a factory that could be either a map
or a struct.
## 
  
    **
  
  Example

```
# custom factory
def article_factory(attrs) do
  title = Map.get(attrs, :title, "default title")

  article = %Article{
    title: title
  }

  merge_attributes(article, attrs)
end
```

Note that when trying to merge attributes into a struct, this function will
raise if one of the attributes is not defined in the struct.
  

  
    
      **
      Link to this function
    
    
# sequence(name)

      
       **
       View Source
     

  

  

      

          

```
@spec sequence(String.t()) :: String.t()
```

      

Shortcut for creating unique string values.

This is automatically imported into a model factory when you `use ExMachina`.

This is equivalent to `sequence(name, &"#{name}#{&1}")`. If you need to
customize the returned string, see `sequence/2`.

Note that sequences keep growing and are *not* reset by ExMachina. Most of the
time you won't need to reset the sequence, but when you do need to reset them,
you can use `ExMachina.Sequence.reset/0`.
## 
  
    **
  
  Examples

```
def user_factory do
  %User{
    # Will generate "username0" then "username1", etc.
    username: sequence("username")
  }
end

def article_factory do
  %Article{
    # Will generate "Article Title0" then "Article Title1", etc.
    title: sequence("Article Title")
  }
end
```

  

  
    
      **
      Link to this function
    
    
# sequence(name, formatter)

      
       **
       View Source
     

  

  

      

          

```
@spec sequence(any(), (integer() -> any()) | [...]) :: any()
```

      

Create sequences for generating unique values.

This is automatically imported into a model factory when you `use ExMachina`.

The `name` can be any term, although it is typically an atom describing the
sequence. Each time a sequence is called with the same `name`, its number is
incremented by one.

The `formatter` function takes the sequence number, and returns a sequential
representation of that number â typically a formatted string.
## 
  
    **
  
  Examples

```
def user_factory do
  %{
    # Will generate "me-0@foo.com" then "me-1@foo.com", etc.
    email: sequence(:email, &"me-#{&1}@foo.com"),
    # Will generate "admin" then "user", "other", "admin" etc.
    role: sequence(:role, ["admin", "user", "other"])
  }
end
```

  

  
    
      **
      Link to this function
    
    
# sequence(name, formatter, opts)

      
       **
       View Source
     

  

  

      

          

```
@spec sequence(any(), (integer() -> any()) | [...], [{:start_at, non_neg_integer()}]) ::
  any()
```

      

Similar to `sequence/2` but it allows for passing a `start_at` option
to the sequence generation.
## 
  
    **
  
  Examples

```
def user_factory do
  %{
    # Will generate "me-100@foo.com" then "me-101@foo.com", etc.
    email: sequence(:email, &"me-#{&1}@foo.com", start_at: 100),
  }
end
```