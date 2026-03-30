# Class: ActionCable::Connection::TestCase
  
  
  

  
  
    Inherits:
    
      ActiveSupport::TestCase
      
        

          
- Object
          
            
- ActiveSupport::TestCase
          
            
- ActionCable::Connection::TestCase
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Behavior
  
  
  

  

  
  
    Defined in:
    lib/action_cable/connection/test_case.rb
  
  

## Overview

  
    

# Action Cable Connection TestCase

Unit test Action Cable connections.

Useful to check whether a connection’s `identified_by` gets assigned properly and that any improper connection requests are rejected.

## Basic example

Unit tests are written by first simulating a connection attempt by calling `connect` and then asserting state, e.g. identifiers, have been assigned.

```
class ApplicationCable::ConnectionTest < ActionCable::Connection::TestCase
  def test_connects_with_proper_cookie
    # Simulate the connection request with a cookie.
    cookies["user_id"] = users(:john).id

    connect

    # Assert the connection identifier matches the fixture.
    assert_equal users(:john).id, connection.user.id
  end

  def test_rejects_connection_without_proper_cookie
    assert_reject_connection { connect }
  end
end

```

`connect` accepts additional information about the HTTP request with the `params`, `headers`, `session`, and Rack `env` options.

```
def test_connect_with_headers_and_query_string
  connect params: { user_id: 1 }, headers: { "X-API-TOKEN" => "secret-my" }

  assert_equal "1", connection.user.id
  assert_equal "secret-my", connection.token
end

def test_connect_with_params
  connect params: { user_id: 1 }

  assert_equal "1", connection.user.id
end

```

You can also set up the correct cookies before the connection request:

```
def test_connect_with_cookies
  # Plain cookies:
  cookies["user_id"] = 1

  # Or signed/encrypted:
  # cookies.signed["user_id"] = 1
  # cookies.encrypted["user_id"] = 1

  connect

  assert_equal "1", connection.user_id
end

```

## Connection is automatically inferred

ActionCable::Connection::TestCase will automatically infer the connection under test from the test class name. If the channel cannot be inferred from the test class name, you can explicitly set it with `tests`.

```
class ConnectionTest < ActionCable::Connection::TestCase
  tests ApplicationCable::Connection
end

```

  

  

## Defined Under Namespace

  
    
      **Modules:** Behavior
    
  
    
  

  
## Constant Summary

  
  
### Constants included
     from Behavior

  

Behavior::DEFAULT_PATH

  
  
  
  
  
  
  
## Method Summary

  
  
### Methods included from Behavior

  

#connect, #cookies, #disconnect

  
  
  
  
  
  
  
  
  
  
### Methods included from Assertions

  

#assert_reject_connection