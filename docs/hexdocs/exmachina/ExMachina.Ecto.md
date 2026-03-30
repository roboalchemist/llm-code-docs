# 

      
        **
        View Source
      

    ExMachina.Ecto behaviour
    (ex_machina v2.8.0)

  

    

Module for building and inserting factories with Ecto

This module works much like the regular `ExMachina` module, but adds a few
nice things that make working with Ecto easier.

- It uses `ExMachina.EctoStrategy`, which adds `insert/1`, `insert/2`,
`insert/3` `insert_pair/2`, `insert_list/3`.
- Adds a `params_for` function that is useful for working with changesets or
sending params to API endpoints.

More in-depth examples are in the README.
    

Module for building and inserting factories with Ecto

This module works much like the regular `ExMachina` module, but adds a few
nice things that make working with Ecto easier.

- It uses `ExMachina.EctoStrategy`, which adds `insert/1`, `insert/2`,
`insert/3` `insert_pair/2`, `insert_list/3`.
- Adds a `params_for` function that is useful for working with changesets or
sending params to API endpoints.

More in-depth examples are in the README.
    

    
# 
      
        **
      
      Summary
    

  
## 
    Callbacks
  

    
      
        insert(factory_name)

      

    

    
      
        insert(factory_name, attrs)

      

    

    
      
        insert(factory_name, attrs, opts)

      

        

Builds a factory and inserts it into the database.

    

    
      
        insert_list(number_of_records, factory_name)

      

        

Builds many factories and inserts them into the database.

    

    
      
        insert_list(number_of_records, factory_name, attrs)

      

    

    
      
        insert_pair(factory_name)

      

        

Builds two factories and inserts them into the database.

    

    
      
        insert_pair(factory_name, attrs)

      

    

    
      
        params_for(factory_name)

      

        

Builds a factory and returns only its fields.

    

    
      
        params_for(factory_name, attrs)

      

    

    
      
        params_with_assocs(factory_name)

      

        

Similar to `params_for/2` but inserts all `belongs_to` associations and
sets the foreign keys.

    

    
      
        params_with_assocs(factory_name, attrs)

      

    

    
      
        string_params_for(factory_name)

      

        

Similar to `params_for/2` but converts atom keys to strings in returned map.

    

    
      
        string_params_for(factory_name, attrs)

      

    

    
      
        string_params_with_assocs(factory_name)

      

        

Similar to `params_with_assocs/2` but converts atom keys to strings in
returned map.

    

    
      
        string_params_with_assocs(factory_name, attrs)

      

    

  

    
# 
      
        **
      
      Callbacks
    

    

  
    
      **
      Link to this callback
    
    
# insert(factory_name)

      
       **
       View Source
     

  

  

      

          

```
@callback insert(factory_name :: atom()) :: any()
```

      

  

  
    
      **
      Link to this callback
    
    
# insert(factory_name, attrs)

      
       **
       View Source
     

  

  

      

          

```
@callback insert(factory_name :: atom(), attrs :: keyword() | map()) :: any()
```

      

  

  
    
      **
      Link to this callback
    
    
# insert(factory_name, attrs, opts)

      
       **
       View Source
     

  

  

      

          

```
@callback insert(
  factory_name :: atom(),
  attrs :: keyword() | map(),
  opts :: keyword() | map()
) :: any()
```

      

Builds a factory and inserts it into the database.

The first two arguments are the same as `ExMachina.build/2`. The last
argument is a set of options that will be passed to Ecto's
`Repo.insert!/2`.
## 
  
    **
  
  Examples

```
# return all values from the database
insert(:user, [name: "Jane"], returning: true)
build(:user, name: "Jane") |> insert(returning: true)

# use a different prefix
insert(:user, [name: "Jane"], prefix: "other_tenant")
build(:user, name: "Jane") |> insert(prefix: "other_tenant")
```

  

  
    
      **
      Link to this callback
    
    
# insert_list(number_of_records, factory_name)

      
       **
       View Source
     

  

  

      

          

```
@callback insert_list(number_of_records :: integer(), factory_name :: atom()) :: list()
```

      

Builds many factories and inserts them into the database.

The arguments are the same as `ExMachina.build_list/3`.
  

  
    
      **
      Link to this callback
    
    
# insert_list(number_of_records, factory_name, attrs)

      
       **
       View Source
     

  

  

      

          

```
@callback insert_list(
  number_of_records :: integer(),
  factory_name :: atom(),
  attrs :: keyword() | map()
) :: list()
```

      

  

  
    
      **
      Link to this callback
    
    
# insert_pair(factory_name)

      
       **
       View Source
     

  

  

      

          

```
@callback insert_pair(factory_name :: atom()) :: list()
```

      

Builds two factories and inserts them into the database.

The arguments are the same as `ExMachina.build_pair/2`.
  

  
    
      **
      Link to this callback
    
    
# insert_pair(factory_name, attrs)

      
       **
       View Source
     

  

  

      

          

```
@callback insert_pair(factory_name :: atom(), attrs :: keyword() | map()) :: list()
```

      

  

  
    
      **
      Link to this callback
    
    
# params_for(factory_name)

      
       **
       View Source
     

  

  

      

          

```
@callback params_for(factory_name :: atom()) :: %{optional(atom()) => any()}
```

      

Builds a factory and returns only its fields.

This is only for use with Ecto models.

Will return a map with the fields and virtual fields, but without the Ecto
metadata, the primary key, or any `belongs_to` associations. This will
recursively act on `has_one` associations and Ecto structs found in
`has_many` associations.

If you want `belongs_to` associations to be inserted, use
`params_with_assocs/2`.

If you want params with string keys use `string_params_for/2`.
## 
  
    **
  
  Example

```
def user_factory do
  %MyApp.User{name: "John Doe", admin: false}
end

# Returns %{name: "John Doe", admin: true}
params_for(:user, admin: true)

# Returns %{name: "John Doe", admin: false}
params_for(:user)
```

  

  
    
      **
      Link to this callback
    
    
# params_for(factory_name, attrs)

      
       **
       View Source
     

  

  

      

          

```
@callback params_for(factory_name :: atom(), attrs :: keyword() | map()) :: %{
  optional(atom()) => any()
}
```

      

  

  
    
      **
      Link to this callback
    
    
# params_with_assocs(factory_name)

      
       **
       View Source
     

  

  

      

          

```
@callback params_with_assocs(factory_name :: atom()) :: %{optional(atom()) => any()}
```

      

Similar to `params_for/2` but inserts all `belongs_to` associations and
sets the foreign keys.

If you want params with string keys use `string_params_with_assocs/2`.
## 
  
    **
  
  Example

```
def article_factory do
  %MyApp.Article{title: "An Awesome Article", author: build(:author)}
end

# Inserts an author and returns %{title: "An Awesome Article", author_id: 12}
params_with_assocs(:article)
```

  

  
    
      **
      Link to this callback
    
    
# params_with_assocs(factory_name, attrs)

      
       **
       View Source
     

  

  

      

          

```
@callback params_with_assocs(factory_name :: atom(), attrs :: keyword() | map()) :: %{
  optional(atom()) => any()
}
```

      

  

  
    
      **
      Link to this callback
    
    
# string_params_for(factory_name)

      
       **
       View Source
     

  

  

      

          

```
@callback string_params_for(factory_name :: atom()) :: %{optional(String.t()) => any()}
```

      

Similar to `params_for/2` but converts atom keys to strings in returned map.

The result of this function can be safely used in controller tests for Phoenix
web applications.
## 
  
    **
  
  Example

```
def user_factory do
  %MyApp.User{name: "John Doe", admin: false}
end

# Returns %{"name" => "John Doe", "admin" => true}
string_params_for(:user, admin: true)
```

  

  
    
      **
      Link to this callback
    
    
# string_params_for(factory_name, attrs)

      
       **
       View Source
     

  

  

      

          

```
@callback string_params_for(factory_name :: atom(), attrs :: keyword() | map()) :: %{
  optional(String.t()) => any()
}
```

      

  

  
    
      **
      Link to this callback
    
    
# string_params_with_assocs(factory_name)

      
       **
       View Source
     

  

  

      

          

```
@callback string_params_with_assocs(factory_name :: atom()) :: %{
  optional(String.t()) => any()
}
```

      

Similar to `params_with_assocs/2` but converts atom keys to strings in
returned map.

The result of this function can be safely used in controller tests for Phoenix
web applications.
## 
  
    **
  
  Example

```
def article_factory do
  %MyApp.Article{title: "An Awesome Article", author: build(:author)}
end

# Inserts an author and returns %{"title" => "An Awesome Article", "author_id" => 12}
string_params_with_assocs(:article)
```

  

  
    
      **
      Link to this callback
    
    
# string_params_with_assocs(factory_name, attrs)

      
       **
       View Source
     

  

  

      

          

```
@callback string_params_with_assocs(factory_name :: atom(), attrs :: keyword() | map()) ::
  %{
    optional(String.t()) => any()
  }
```