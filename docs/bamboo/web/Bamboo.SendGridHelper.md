# 
      Bamboo.SendGridHelper 
      (bamboo v2.5.0)

    

      
        **
        View Source
      

  

Functions for using features specific to Sendgrid.
## **Example

```
email
|> with_template("80509523-83de-42b6-a2bf-54b7513bd2aa")
|> substitute("%name%", "Jon Snow")
|> substitute("%location%", "Westeros")
```

    

    
# 
      
        **
      
      Summary
    

  
## 
    Functions
  

    
      
        add_dynamic_field(email, field, value)

      

        

Add a property to the list of dynamic template data in the SendGrid template.

    

    
      
        add_personalizations(email, personalizations)

      

        

Add SendGrid personalizations.

    

    
      
        substitute(email, tag, value)

      

        

Add a tag to the list of substitutions in the SendGrid template.

    

    
      
        with_asm_group_id(email, asm_group_id)

      

        

Set the ASM (Advanced Suppression Manager) group that this email should belong to.

    

    
      
        with_bypass_list_management(email, enabled)

      

        

Instruct SendGrid to bypass list management for this email.

    

    
      
        with_bypass_unsubscribe_management(email, enabled)

      

        

Instruct SendGrid to bypass unsubscribe list management for this email.

    

    
      
        with_categories(email, categories)

      

        

Sets a list of categories for this email.

    

    
      
        with_click_tracking(email, enabled)

      

        

Instruct SendGrid to enable or disable Click Tracking for a particular email.

    

    
      
        with_custom_args(email, custom_args)

      

        

Set a map of custom arguments for this email.

    

    
      
        with_google_analytics(email, enabled, utm_params \\ %{})

      

        

Instruct SendGrid to enable or disable Google Analytics tracking, and
optionally set the UTM parameters for it.

    

    
      
        with_ip_pool_name(email, ip_pool_name)

      

        

Specify the ip pool name.

    

    
      
        with_send_at(email, time)

      

        

Schedule a time for SendGrid to deliver the email.

    

    
      
        with_subscription_tracking(email, enabled)

      

        

Instruct SendGrid to enable or disable Subscription Tracking for a particular email.

    

    
      
        with_template(email, template_id)

      

        

Specify the template for SendGrid to use for the context of the substitution
tags.

    

  

    
# 
      
        **
      
      Functions
    

    

  
    
      **
    
    
      
# add_dynamic_field(email, field, value)

        
          **
        

    
  

  

Add a property to the list of dynamic template data in the SendGrid template.

This will be added to the request as:

```
 "personalizations":[
    {
       "to":[
          {
             "email":"example@sendgrid.net"
          }
       ],
       "dynamic_template_data":{
          "total":"$ 239.85",
       }
    }
 ],
```

The tag can be of any type since SendGrid allows you to use Handlebars in its templates
## **Example

```
email
|> add_dynamic_field("name", "Jon Snow")
```

  

  
    
      **
    
    
      
# add_personalizations(email, personalizations)

        
          **
        

    
  

  

      

          

```
@spec add_personalizations(Bamboo.Email.t(), [map()]) :: Bamboo.Email.t()
```

      

Add SendGrid personalizations.

Each personalization can have the following fields: `to`, `cc`, `bcc`,
`subject`, `headers`, `substitutions`, `custom_args`, or `send_at`.

Settings from the top level of the email (e.g., `Email |> with_send_at`)
will not be applied to each personalization.  If you want multiple
personalizations with common properties, it is recommended to generate the
list from a common base value and simply do not set the corresponding
top-level fields.
## **Example:

```
base_personalization = %{
  bcc: [%{"email" => "bcc@bar.com", "name" => "BCC"}],
  subject: "Here is your email"
}

personalizations =
  Enum.map(
    [
      %{to: "one@test.com"},
      %{to: "two@test.com", send_at: 1_580_485_560}
    ],
    &Map.merge(base_personalization, &1)
  )

email =
  new_email()
  |> Email.put_header("Reply-To", "reply@foo.com")
  |> Bamboo.SendGridHelper.add_personalizations(personalizations)
```

  

  
    
      **
    
    
      
# substitute(email, tag, value)

        
          **
        

    
  

  

Add a tag to the list of substitutions in the SendGrid template.

The tag must be a `String.t` due to SendGrid using special characters to wrap
tags in the template.
## **Example

```
email
|> substitute("%name%", "Jon Snow")
```

  

  
    
      **
    
    
      
# with_asm_group_id(email, asm_group_id)

        
          **
        

    
  

  

Set the ASM (Advanced Suppression Manager) group that this email should belong to.

This can be used to let recipients unsubscribe from only a certain type of communication.
## **Example

```
email
|> with_asm_group_id(1234)
```

  

  
    
      **
    
    
      
# with_bypass_list_management(email, enabled)

        
          **
        

    
  

  

Instruct SendGrid to bypass list management for this email.

If enabled, SendGrid will ignore any email suppression (such as
unsubscriptions, bounces, spam filters) for this email. This is useful for
emails that all users must receive, such as Terms of Service updates, or
password resets.
## **Example

```
email
|> with_bypass_list_management(true)
```

  

  
    
      **
    
    
      
# with_bypass_unsubscribe_management(email, enabled)

        
          **
        

    
  

  

Instruct SendGrid to bypass unsubscribe list management for this email.

If enabled, SendGrid will ignore any email suppression (such as
unsubscriptions, bounces, spam filters) for this email. This is useful for
emails that all users must receive, such as Terms of Service updates, or
password resets.
## **Example

```
email
|> with_bypass_unsubscribe_management(true)
```

  

  
    
      **
    
    
      
# with_categories(email, categories)

        
          **
        

    
  

  

Sets a list of categories for this email.

A maximum of 10 categories can be assigned to an email. Duplicate categories will
be ignored and only unique entries will be sent.
## **Example

```
email
|> with_categories("campaign-12345")
```

  

  
    
      **
    
    
      
# with_click_tracking(email, enabled)

        
          **
        

    
  

  

Instruct SendGrid to enable or disable Click Tracking for a particular email.

Read more about SendGrid click tracking here
## **Example

```
email
|> with_click_tracking(true)

email
|> with_click_tracking(false)
```

  

  
    
      **
    
    
      
# with_custom_args(email, custom_args)

        
          **
        

    
  

  

Set a map of custom arguments for this email.

This will override any existing custom arguments.
## **Example

```
email
|> with_custom_args(%{new_arg_1: "new arg 1", new_arg_2: "new arg 2"})
```

  

    

  
    
      **
    
    
      
# with_google_analytics(email, enabled, utm_params \\ %{})

        
          **
        

    
  

  

Instruct SendGrid to enable or disable Google Analytics tracking, and
optionally set the UTM parameters for it.

This is useful if you need to control UTM tracking parameters on an individual email
basis.
## **Example

```
email
|> with_google_analytics(true, %{utm_source: "email", utm_campaign: "campaign"})

email
|> with_google_analytics(false)
```

  

  
    
      **
    
    
      
# with_ip_pool_name(email, ip_pool_name)

        
          **
        

    
  

  

Specify the ip pool name.
## **Example

```
email
|> with_ip_pool_name("my-ip-pool-name")
```

  

  
    
      **
    
    
      
# with_send_at(email, time)

        
          **
        

    
  

  

      

          

```
@spec with_send_at(Bamboo.Email.t(), DateTime.t() | integer()) :: Bamboo.Email.t()
```

      

Schedule a time for SendGrid to deliver the email.

Note that if the time is in the past, SendGrid will immediately deliver the
email.
## **Example

```
{:ok, delivery_time, _} = DateTime.from_iso8601("2020-01-01T00:00:00Z")

email
|> with_send_at(delivery_time)
```

  

  
    
      **
    
    
      
# with_subscription_tracking(email, enabled)

        
          **
        

    
  

  

Instruct SendGrid to enable or disable Subscription Tracking for a particular email.

Read more about SendGrid click tracking here
## **Example

```
email
|> with_subscription_tracking(true)

email
|> with_subscription_tracking(false)
```

  

  
    
      **
    
    
      
# with_template(email, template_id)

        
          **
        

    
  

  

Specify the template for SendGrid to use for the context of the substitution
tags.
## **Example

```
with_template(email, "80509523-83de-42b6-a2bf-54b7513bd2aa")
```