# Source: https://resend.com/docs/knowledge-base/lovable-integration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://resend.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send emails with Lovable and Resend

> Learn how to add the Resend integration to your Lovable project.

export const YouTube = ({id}) => {
  return <iframe className="w-full aspect-video rounded-xl" src={`https://www.youtube.com/embed/${id}`} title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen></iframe>;
};

[Lovable](https://lovable.dev) is a platform for building web sites, tools, apps, and projects via chat. You can add Resend in a Lovable project by asking the chat to add email sending with Resend.

If you prefer to watch a video, check out our video walkthrough below.

<YouTube id="0gw693uZt0w" />

## 1. Add your Resend API key

To use Resend with Lovable, you'll need to add a Resend API key, which you can create in the [Resend Dashboard](https://resend.com/api-keys). Do not share your API key with others or expose it in the browser or other client-side code.

Lovable may integrate Resend in a few different ways:

* Use the Supabase integration to store the API key **(highly recommended)**
* Ask users to provide their own API key
* Add the API key directly in the code

You may need to prompt Lovable to store the API key for Resend using Supabase. Clicking **Add API key** will open a modal where you can add the API key.

<img src="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/lovable-integration.png?fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=c071ba3ae671bc6cafd8dfd43e12772d" alt="adding the Resend integration to a Lovable chat" data-og-width="2992" width="2992" data-og-height="1868" height="1868" data-path="images/lovable-integration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/lovable-integration.png?w=280&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=71dba7b6bc78c7bb2530fd3b6cdfec36 280w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/lovable-integration.png?w=560&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=03cf46a9c1d8291d9074ed5027d3c6f4 560w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/lovable-integration.png?w=840&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=39dcccf2658d43ee8c04dff4a98ff817 840w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/lovable-integration.png?w=1100&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=c934b77a84ec24d74875389fdc7595e3 1100w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/lovable-integration.png?w=1650&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=339b019e6e9c0ffb2407193def0236b8 1650w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/lovable-integration.png?w=2500&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=9cc37decca471f7322714d1df6a06123 2500w" />

<Info>
  At the time of writing, Lovable does not securely handle API keys
  independently. Instead, it uses the [Supabase integration to store
  secrets](https://docs.lovable.dev/integrations/supabase#storing-secrets-api-keys-%26-config).
</Info>

## 2. Add a custom domain to your Resend account

By default, you can only send emails to your own email address.

To send emails to other email addresses:

1. Add a [custom domain to your Resend account](https://resend.com/domains).
2. Add the custom domain to the `from` field in the `resend` function in Lovable (or ask the chat to update these fields).

Get more help adding a custom domain in [Resend's documentation](/dashboard/domains/introduction).
