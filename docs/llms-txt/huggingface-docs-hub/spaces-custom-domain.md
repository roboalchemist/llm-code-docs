# Source: https://huggingface.co/docs/hub/spaces-custom-domain.md

# Spaces Custom Domain  

> [!WARNING]
> Spaces Custom Domain feature is part of PRO and Team or Enterprise subscriptions.

## Getting started with a Custom Domain

Spaces Custom Domain is a feature that allows you to host your space in a custom domain of your choosing: `yourdomain.example.com` 🚀 The custom domain must be a valid DNS name.

    
    

## Using a Custom Domain

You can submit a custom domain to host your space in the settings of your Space, under "Custom Domain". You'll need to add the CNAME Record Type: 

    
    

The request will move to 'pending' status after submission as seen below. 

    
    

Please make sure to point the domain to `hf.space`. Once set up, you'll see a 'ready' status to know the custom domain is active for your Space 🔥

If you've completed all the steps but aren't seeing a 'ready' status, you can enter your domain [here](https://toolbox.googleapps.com/apps/dig/#CNAME/) to verify it points to `hf.space`. If if doesn't, please check your domain host to ensure the CNAME record was added correctly.

## Removing a Custom Domain

Simply remove a custom domain by using the delete button to the right of “Custom Domain” in the settings of your Space. You can delete while the custom domain is pending or in ready state.

