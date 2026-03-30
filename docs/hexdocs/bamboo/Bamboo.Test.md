# 
      Bamboo.Test 
      (bamboo v2.5.0)

    

      
        **
        View Source
      

  

Helpers for testing email delivery.

Use these helpers with `Bamboo.TestAdapter` to test email delivery. Typically
you'll want to **unit test emails first**. Then, in integration tests, use
helpers from this module to test whether that email was delivered.
## **Note on sending from other processes

If you are sending emails from another process (for example, from inside a
Task or GenServer) you may need to use shared mode when using
`Bamboo.Test`. See the docs `__using__/1` for an example.

For most scenarios you will not need shared mode.
## **In your config

```
# Typically in config/test.exs
config :my_app, MyApp.Mailer,
  adapter: Bamboo.TestAdapter
```

## **Unit test

You don't need any special functions to unit test emails.

```
defmodule MyApp.EmailTest do
  use ExUnit.Case

  test "welcome email" do
    user = %User{name: "John", email: "person@example.com"}

    email = MyApp.Email.welcome_email(user)

    assert email.to == user
    assert email.subject == "This is your welcome email"
    assert email.html_body =~ "Welcome to the app"
  end
end
```

## **Integration test

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

defmodule MyApp.EmailDeliveryTest do
  use ExUnit.Case
  use Bamboo.Test

  test "sends welcome email" do
    user = %User{...}
    email = MyApp.Email.welcome_email(user)

    email |> MyApp.Mailer.deliver_now

    # Works with deliver_now and deliver_later
    assert_delivered_email email
  end
end
```

    

    
# 
      
        **
      
      Summary
    

  
## 
    Functions
  

    
      
        __using__(arg1)

      

        

Imports `Bamboo.Test` and `Bamboo.Formatter.format_email_address/2`

    

    
      
        assert_delivered_email(email, opts \\ [])

      

        

Checks whether an email was delivered.

    

    
      
        assert_delivered_email_matches(email_pattern, opts \\ [])

      

        

Checks whether an email was delivered matching the given pattern.

    

    
      
        assert_email_delivered_with(email_params, opts \\ [])

      

        

Check whether an email's params are equal to the ones provided.

    

    
      
        assert_no_emails_delivered(opts \\ [])

      

        

Checks that no emails were sent.

    

    
      
        refute_delivered_email(email, opts \\ [])

      

        

Ensures a particular email was not sent

    

    
      
        refute_email_delivered_with(email_params, opts \\ [])

      

        

Check that no email was sent with the given parameters.

    

  

    
# 
      
        **
      
      Functions
    

    

  
    
      **
    
    
      
# __using__(arg1)

        (macro)

        
          **
        

    
  

  

Imports `Bamboo.Test` and `Bamboo.Formatter.format_email_address/2`

`Bamboo.Test` and the `Bamboo.TestAdapter` work by sending a message to the
current process when an email is delivered. The process mailbox is then
checked when using the assertion helpers like `assert_delivered_email/1`.

Sometimes emails don't show up when asserting because you may deliver an email
from a *different* process than the test process. When that happens, turn on
shared mode. This will tell `Bamboo.TestAdapter` to always send to the test process.
This means that you cannot use shared mode with async tests.
## **Try to use this version first

```
use Bamboo.Test
```

## **And if you are delivering from another process, set `shared: true`

```
use Bamboo.Test, shared: true
```

Common scenarios for delivering mail from a different process are when you
send from inside of a Task, GenServer, or are running acceptance tests with a
headless browser like phantomjs.
  

    

  
    
      **
    
    
      
# assert_delivered_email(email, opts \\ [])

        
          **
        

    
  

  

Checks whether an email was delivered.

Must be used with the `Bamboo.TestAdapter` or this will never pass. In case you
are delivering from another process, the assertion waits up to 100ms before
failing. Typically if an email is successfully delivered the assertion will
pass instantly, so test suites will remain fast.
## **Examples

```
email = Bamboo.Email.new_email(subject: "something")
email |> MyApp.Mailer.deliver
assert_delivered_email(email) # Will pass

unsent_email = Bamboo.Email.new_email(subject: "something else")
assert_delivered_email(unsent_email) # Will fail
```

  

    

  
    
      **
    
    
      
# assert_delivered_email_matches(email_pattern, opts \\ [])

        (macro)

        
          **
        

    
  

  

Checks whether an email was delivered matching the given pattern.

Must be used with the `Bamboo.TestAdapter` or this will never pass. This
allows the user to use their configured `assert_receive_timeout` for ExUnit,
and also to match any variables in their given pattern for use in further
assertions.
## **Examples

```
%{email: user_email, name: user_name} = user
MyApp.deliver_welcome_email(user)
assert_delivered_email_matches(%{to: [{_, ^user_email}], text_body: text_body})
assert text_body =~ "Welcome to MyApp, #{user_name}"
assert text_body =~ "You can sign up at https://my_app.com/users/#{user_name}"
```

  

    

  
    
      **
    
    
      
# assert_email_delivered_with(email_params, opts \\ [])

        
          **
        

    
  

  

Check whether an email's params are equal to the ones provided.

Must be used with the `Bamboo.TestAdapter` or this will never pass. In case you
are delivering from another process, the assertion waits up to 100ms before
failing. Typically if an email is successfully delivered the assertion will
pass instantly, so test suites will remain fast.
## **Examples

```
email = Bamboo.Email.new_email(subject: "something")
email |> MyApp.Mailer.deliver
assert_email_delivered_with(subject: "something") # Will pass

unsent_email = Bamboo.Email.new_email(subject: "something else")
assert_email_delivered_with(subject: "something else") # Will fail
```

The function will use the Bamboo Formatter when checking email addresses.

```
email = Bamboo.Email.new_email(to: "someone@example.com")
email |> MyApp.Mailer.deliver
assert_email_delivered_with(to: "someone@example.com") # Will pass
```

You can also pass a regex to match portions of an email.
## **Example

```
email = new_email(text_body: "I love coffee")
email |> MyApp.Mailer.deliver
assert_email_delivered_with(text_body: ~r/love/) # Will pass
assert_email_delivered_with(text_body: ~r/like/) # Will fail
```

  

    

  
    
      **
    
    
      
# assert_no_emails_delivered(opts \\ [])

        
          **
        

    
  

  

Checks that no emails were sent.

If `Bamboo.Test` is used with shared mode, you must also configure a timeout
in your test config.

```
# Set this in your config, typically in config/test.exs
config :bamboo, :refute_timeout, 10
```

The value you set is up to you. Lower values will result in faster tests,
but may incorrectly pass if an email is delivered *after* the timeout. Often
times 1ms is enough.
  

    

  
    
      **
    
    
      
# refute_delivered_email(email, opts \\ [])

        
          **
        

    
  

  

Ensures a particular email was not sent

Same as `assert_delivered_email/0`, except it checks that a particular email
was not sent.

If `Bamboo.Test` is used with shared mode, you must also configure a timeout
in your test config.

```
# Set this in your config, typically in config/test.exs
config :bamboo, :refute_timeout, 10
```

The value you set is up to you. Lower values will result in faster tests,
but may incorrectly pass if an email is delivered *after* the timeout. Often
times 1ms is enough.
  

    

  
    
      **
    
    
      
# refute_email_delivered_with(email_params, opts \\ [])

        
          **
        

    
  

  

Check that no email was sent with the given parameters.

Similar to `assert_email_delivered_with/1`, but it checks that an email with
those parameters wasn't sent.

Note that this assertion helper will grab the email out of the process
mailbox. So if you want to make other assertions about the same email after
this assertion, you need to send the email again.
## **Examples

```
Bamboo.Email.new_email(subject: "something") |> MyApp.Mailer.deliver()
refute_email_delivered_with(subject: "something else") # Will pass

Bamboo.Email.new_email(subject: "something") |> MyApp.Mailer.deliver()
refute_email_delivered_with(subject: ~r/some/) # Will fail
```

If `Bamboo.Test` is used with shared mode, you must also configure a timeout
in your test config.

```
# Set this in your config, typically in config/test.exs
config :bamboo, :refute_timeout, 10
```

The value you set is up to you. Lower values may result in faster tests, but
your tests may incorrectly pass if an email is delivered *after* the timeout.

You can also pass a timeout for a given refutation:
## **Examples

```
Bamboo.Email.new_email(subject: "something") |> MyApp.Mailer.deliver()
refute_email_delivered_with([subject: "something else"], timeout: 100)
```