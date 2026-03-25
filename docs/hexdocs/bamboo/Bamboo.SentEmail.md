# 
      Bamboo.SentEmail 
      (bamboo v2.5.0)

    

      
        **
        View Source
      

  

Used for storing and retrieving sent emails when used with `Bamboo.LocalAdapter`.

When emails are sent with the `Bamboo.LocalAdapter`, they are stored in
`Bamboo.SentEmail`. Use the functions in this module to store and retrieve the emails.

Remember to start the Bamboo app by adding it to the app list in `mix.exs` or
starting it with `Application.ensure_all_started(:bamboo)`
    

    
# 
      
        **
      
      Summary
    

  
## 
    Functions
  

    
      
        all()

      

        

Returns a list of all sent emails

    

    
      
        child_spec(arg)

      

        

Returns a specification to start this module under a supervisor.

    

    
      
        get(id)

      

        

Gets an email by id. Returns nil if it can't find a matching email.

    

    
      
        get!(id)

      

        

Gets an email by id. Raises if it can't find one.

    

    
      
        get_id(email)

      

        

Gets the email's id.

    

    
      
        one()

      

        

Returns exactly one sent email. Raises if none, or more than one are found

    

    
      
        push(email)

      

        

Adds an email to the list of sent emails.

    

    
      
        reset()

      

        

Clears all sent emails

    

    
      
        start_link(opts)

      

        

Starts the SentEmail Agent

    

  

    
# 
      
        **
      
      Functions
    

    

  
    
      **
    
    
      
# all()

        
          **
        

    
  

  

Returns a list of all sent emails
  

  
    
      **
    
    
      
# child_spec(arg)

        
          **
        

    
  

  

Returns a specification to start this module under a supervisor.

See `Supervisor`.
  

  
    
      **
    
    
      
# get(id)

        
          **
        

    
  

  

Gets an email by id. Returns nil if it can't find a matching email.
  

  
    
      **
    
    
      
# get!(id)

        
          **
        

    
  

  

Gets an email by id. Raises if it can't find one.
  

  
    
      **
    
    
      
# get_id(email)

        
          **
        

    
  

  

Gets the email's id.

The email must be an email that was sent with `Bamboo.LocalAdapter` or added
via `Bamboo.SentEmail.push/1`, otherwise the id will not have been set.
  

  
    
      **
    
    
      
# one()

        
          **
        

    
  

  

Returns exactly one sent email. Raises if none, or more than one are found

Raises `NoDeliveriesError` if there are no emails. Raises `DeliveriesError` if
there are 2 or more emails.
  

  
    
      **
    
    
      
# push(email)

        
          **
        

    
  

  

Adds an email to the list of sent emails.

Adds an email to the beginning of the sent emails list. Also gives the email
an id that can be fetched with `Bamboo.SentEmail.get_id/1`.
  

  
    
      **
    
    
      
# reset()

        
          **
        

    
  

  

Clears all sent emails
  

  
    
      **
    
    
      
# start_link(opts)

        
          **
        

    
  

  

Starts the SentEmail Agent