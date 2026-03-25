# 
      Bamboo.MailgunHelper 
      (bamboo v2.5.0)

    

      
        **
        View Source
      

  

Functions for using features specific to Mailgun
(e.g. tagging, templates).
    

    
# 
      
        **
      
      Summary
    

  
## 
    Functions
  

    
      
        deliverytime(email, deliverytime)

      

        

Schedule an email to be delivered in the future.

    

    
      
        option(email, key, value)

      

        

Set a Mailgun option (`o:` parameter) on the email in a safe, validated way.

    

    
      
        recipient_variables(email, value)

      

        

Adds Mailgun recipient variables to the outgoing email

    

    
      
        substitute_variables(email, variables)

      

        

This behaves like `Bamboo.MailgunHelper.substitute_variables/3`, but
accepts a `Map` rather than a key, value pair.

    

    
      
        substitute_variables(email, key, value)

      

        

When sending an email with `Bamboo.MailgunHelper.template/2` you can
replace a handlebars variables using this function.

    

    
      
        tag(email, tag)

      

        

Add a tag to outgoing email to help categorize traffic based on some
criteria, perhaps separate signup emails from password recovery emails
or from user comments.

    

    
      
        template(email, template_name)

      

        

Send an email using a template stored in Mailgun, rather than supplying
a `Bamboo.Email.text_body/2` or a `Bamboo.Email.html_body/2`.

    

    
      
        template_text(email, arg2)

      

        

Use it if you want to have rendered template in the text part of the
message in case of template sending.

    

    
      
        template_version(email, version)

      

        

Use it to send a message to specific version of a template.

    

  

    
# 
      
        **
      
      Functions
    

    

  
    
      **
    
    
      
# deliverytime(email, deliverytime)

        
          **
        

    
  

  

Schedule an email to be delivered in the future.

More details can be found in the
Mailgun documentation
## **Example

```
one_hour_from_now =
  DateTime.utc_now()
  |> DateTime.add(3600)

email
|> MailgunHelper.deliverytime(one_hour_from_now)
```

  

  
    
      **
    
    
      
# option(email, key, value)

        
          **
        

    
  

  

Set a Mailgun option (`o:` parameter) on the email in a safe, validated way.

Only the options allowed by the Mailgun API are supported. See:
https://mailgun-docs.redoc.ly/docs/mailgun/api-reference/openapi-final/tag/Messages/#tag/Messages/operation/POST-v3--domain-name--messages
## **Example

```
email
|> MailgunHelper.option(:"o:tracking", "yes")
|> MailgunHelper.option(:"o:tracking-clicks", "htmlonly")
```

If you try to set an unsupported option, an ArgumentError will be raised.
  

  
    
      **
    
    
      
# recipient_variables(email, value)

        
          **
        

    
  

  

Adds Mailgun recipient variables to the outgoing email

More details can be found in the
Mailgun documentation
## **Example

```
variables = %{
  "user1@example.com" => %{unique_id: "ABC123456789"},
  "user2@example.com" => %{unique_id: "ZXY987654321"}
}

email
|> MailgunHelper.recipient_variables(variables)
```

  

  
    
      **
    
    
      
# substitute_variables(email, variables)

        
          **
        

    
  

  

This behaves like `Bamboo.MailgunHelper.substitute_variables/3`, but
accepts a `Map` rather than a key, value pair.
## **Example

```
email
|> MailgunHelper.template("password-reset-email")
|> MailgunHelper.substitute_variables(%{ "greeting" => "Hello!", "password_reset_link" => "https://example.com/123" })
```

  

  
    
      **
    
    
      
# substitute_variables(email, key, value)

        
          **
        

    
  

  

When sending an email with `Bamboo.MailgunHelper.template/2` you can
replace a handlebars variables using this function.

More details about templates can be found in the
Templates section of the Mailgun documentation.
## **Example

```
email
|> MailgunHelper.template("password-reset-email")
|> MailgunHelper.substitute_variables("password_reset_link", "https://example.com/123")
```

  

  
    
      **
    
    
      
# tag(email, tag)

        
          **
        

    
  

  

Add a tag to outgoing email to help categorize traffic based on some
criteria, perhaps separate signup emails from password recovery emails
or from user comments.

More details can be found in the
Mailgun documentation
## **Example

```
email
|> MailgunHelper.tag("welcome-email")
```

  

  
    
      **
    
    
      
# template(email, template_name)

        
          **
        

    
  

  

Send an email using a template stored in Mailgun, rather than supplying
a `Bamboo.Email.text_body/2` or a `Bamboo.Email.html_body/2`.

More details about templates can be found in the
Templates section of the Mailgun documentation.
  

  
    
      **
    
    
      
# template_text(email, arg2)

        
          **
        

    
  

  

Use it if you want to have rendered template in the text part of the
message in case of template sending.

More details can be found in the
Mailgun documentation
## **Example

```
email
|> MailgunHelper.template_text(true)
```

  

  
    
      **
    
    
      
# template_version(email, version)

        
          **
        

    
  

  

Use it to send a message to specific version of a template.

More details can be found in the
Mailgun documentation
## **Example

```
email
|> MailgunHelper.template("my-template")
|> MailgunHelper.template_version("v2")
```