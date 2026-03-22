# 

      
        **
        View Source
      

    ExMachina.Strategy 
    (ex_machina v2.8.0)

  

    

Module for making new strategies for working with factories
## 
  
    **
  
  Example

```
defmodule MyApp.JsonEncodeStrategy do
  # The function_name will be used to generate functions in your factory
  # This example adds json_encode/1, json_encode/2, json_encode/3,
  # json_encode_pair/2 and json_encode_list/3
  use ExMachina.Strategy, function_name: :json_encode

  # Define a function for handling the records.
  # Takes the form of "handle_#{function_name}"
  def handle_json_encode(record, %{encoder: encoder}) do
    encoder.encode!(record)
  end

  # Optionally, define a function for handling records and taking in
  # options at the function level
  def handle_json_encode(record, %{encoder: encoder}, encoding_opts) do
    encoder.encode!(record, encoding_opts)
  end
end

defmodule MyApp.JsonFactory do
  use ExMachina
  use MyApp.JsonEncodeStrategy, encoder: Poison

  def user_factory do
    %User{name: "John"}
  end
end

# Will build and then return a JSON encoded version of the user.
MyApp.JsonFactories.json_encode(:user)
```

The arguments sent to the handling function are

- The built record
- The options passed to the strategy
- The options passed to the function as a third argument

The options sent as the second argument are always converted to a map. The
options are anything you passed when you `use` your strategy in your factory,
merged together with `%{factory_module: FactoryItWasCalledFrom}`.

This allows for customizing the strategy, and for calling other functions on
the factory if needed.

See `ExMachina.EctoStrategy` in the ExMachina repo, and the docs for
`name_from_struct/1` for more examples.

The options sent as the third argument come directly from the options passed
to the function being called. These could be function-level overrides of the
options passed when you `use` the strategy, or they could be other
customizations needed at the level of the function.

See `ExMachina.Ecto.insert/3` for an example.
    

Module for making new strategies for working with factories
## 
  
    **
  
  Example

```
defmodule MyApp.JsonEncodeStrategy do
  # The function_name will be used to generate functions in your factory
  # This example adds json_encode/1, json_encode/2, json_encode/3,
  # json_encode_pair/2 and json_encode_list/3
  use ExMachina.Strategy, function_name: :json_encode

  # Define a function for handling the records.
  # Takes the form of "handle_#{function_name}"
  def handle_json_encode(record, %{encoder: encoder}) do
    encoder.encode!(record)
  end

  # Optionally, define a function for handling records and taking in
  # options at the function level
  def handle_json_encode(record, %{encoder: encoder}, encoding_opts) do
    encoder.encode!(record, encoding_opts)
  end
end

defmodule MyApp.JsonFactory do
  use ExMachina
  use MyApp.JsonEncodeStrategy, encoder: Poison

  def user_factory do
    %User{name: "John"}
  end
end

# Will build and then return a JSON encoded version of the user.
MyApp.JsonFactories.json_encode(:user)
```

The arguments sent to the handling function are

- The built record
- The options passed to the strategy
- The options passed to the function as a third argument

The options sent as the second argument are always converted to a map. The
options are anything you passed when you `use` your strategy in your factory,
merged together with `%{factory_module: FactoryItWasCalledFrom}`.

This allows for customizing the strategy, and for calling other functions on
the factory if needed.

See `ExMachina.EctoStrategy` in the ExMachina repo, and the docs for
`name_from_struct/1` for more examples.

The options sent as the third argument come directly from the options passed
to the function being called. These could be function-level overrides of the
options passed when you `use` the strategy, or they could be other
customizations needed at the level of the function.

See `ExMachina.Ecto.insert/3` for an example.
    

    
# 
      
        **
      
      Summary
    

  
## 
    Functions
  

    
      
        name_from_struct(struct)

      

        

Returns the factory name from a struct. Useful for strategies with callbacks.

    

  

    
# 
      
        **
      
      Functions
    

    

  
    
      **
      Link to this function
    
    
# name_from_struct(struct)

      
       **
       View Source
     

  

  

      

          

```
@spec name_from_struct(struct()) :: atom()
```

      

Returns the factory name from a struct. Useful for strategies with callbacks.

This function can be useful when you want to call other functions based on the
type of struct passed in. For example, if you wanted to call a function on the
factory module before JSON encoding.
## 
  
    **
  
  Examples

```
ExMachina.Strategy.name_from_struct(%User{}) # Returns :user
ExMachina.Strategy.name_from_struct(%MyUser{}) # Returns :my_user
ExMachina.Strategy.name_from_struct(%MyApp.MyTask{}) # Returns :my_task
```

## 
  
    **
  
  Implementing callback functions with name_from_struct/1

```
defmodule MyApp.JsonEncodeStrategy do
  use ExMachina.Strategy, function_name: :json_encode

  def handle_json_encode(record, %{factory_module: factory_module}) do
    # If the record was a %User{} this would return :before_encode_user
    callback_func_name = :"before_encode_#{ExMachina.Strategy.name_from_struct(record)}"

    if callback_defined?(factory_module, callback_func_name) do
      # First call the callback function
      apply(factory_module, callback_func_name, [record])
      # Then encode it
      |> Poison.encode!
    else
      # Otherwise, encode it without calling any callback
      Poison.encode!(record)
    end
  end

  defp callback_defined?(module, func_name) do
    Code.ensure_loaded?(module) && function_exported?(module, func_name, 1)
  end
end
```