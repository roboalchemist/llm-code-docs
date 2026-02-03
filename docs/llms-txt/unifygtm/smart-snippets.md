# Source: https://docs.unifygtm.com/reference/sequences/smart-snippets.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unifygtm.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Smart Snippets

> Personalize your outreach with AI-powered email copy generation.

## Overview

Smart snippets allow you to personalize messages with AI-generated copy that's
unique to each recipient. You can use smart snippets to enhance your messaging,
improve deliverability, and increase engagement.

Smart snippets are concise, self-contained pieces of text that serve a clear
communicative purpose. Each snippet should be laser-focused on the parts of your
outbound message that change the most to fit each recipient differently.

## Creating a smart snippet

Navigate to the [Snippets](https://app.unifygtm.com/dashboard/snippets) tab in
the sidebar, select **New Snippet** in the top right corner, and choose
**Smart Snippet**. You will see the smart snippet creation screen.

<Frame caption="This is where you enter the prompt for your smart snippet.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/smart-snippet-create.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=95c886816ee1ef78ea46bc17216f5ae4" data-og-width="2864" width="2864" data-og-height="2048" height="2048" data-path="images/reference/sequences/smart-snippet-create.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/smart-snippet-create.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=a3a6d195abb412416a3bc1388f3fc045 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/smart-snippet-create.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=68faebcf57e2e15ee576f4d638c839c0 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/smart-snippet-create.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=9de1184c52edb5b38cf00a53b89d2e52 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/smart-snippet-create.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=2977cac1cb67953f5edd0ed667ecf924 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/smart-snippet-create.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=258075fcf7ec5f96946d75f417cf73cb 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/smart-snippet-create.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=baa72f675a2928b50bdd4b0277615972 2500w" />
</Frame>

To define a smart snippet, you provide a prompt that describes the content you
want to generate. The prompt should include template variables for any data you
want the model to use when writing the snippet. You can click on the quick
prompts to see example prompts for inspiration.

After you've entered your prompt, click **Generate examples** to see what the
smart snippet will generate for a sample of real people from your data. You can
edit the prompt and regenerate examples to iteratively refine your snippet.

<Frame caption="Example snippet generations appear on the left.">
  <img src="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/sequences/smart-snippet-previews.png?fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=82661918e2a2402dba1597add9a60c13" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/sequences/smart-snippet-previews.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/sequences/smart-snippet-previews.png?w=280&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=1a639f51d52fa02accdd149ccd267357 280w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/sequences/smart-snippet-previews.png?w=560&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=33e8219401a70e5926bc450811baaec6 560w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/sequences/smart-snippet-previews.png?w=840&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=f7694a795e29b2784f352b6e16ae89ad 840w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/sequences/smart-snippet-previews.png?w=1100&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=a1562993bd6d44a3cff43a4488852ee0 1100w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/sequences/smart-snippet-previews.png?w=1650&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=58a2b3b5cc317895828edceef0889c77 1650w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/sequences/smart-snippet-previews.png?w=2500&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=b46c2396a9101681f2cd0f0f7d400369 2500w" />
</Frame>

Just like regular snippets, you should also define a fallback value for the case
where some of the template variables in the prompt are missing data. This will
prevent enrollments from being blocked by the missing data.

When you're satisfied with your prompt, click **Create** to save it. You will
now be able to use the snippet in your sequences.

## Recommendations

Here are a few practices we recommend to get the most out of smart snippets:

1. Always include at least one template variable for the model to use to
   personalize the snippet. For example, include some details about the sender,
   the recipient, or their company. This helps the model write more precise and
   personalized copy.
2. Include 2-3 example outputs to guide the model. Examples help the model
   understand the tone and structure you're trying to achieve. The model will
   often pick up on vocabulary and stylistic choices from your examples.
3. Start small. Pick a specific part of the email—such as the salutation or
   hook—and focus on personalizing that part. Smart snippets are most effective
   when they're used to personalize small sections of your email. Remember that
   you can use as many snippets in an email as you want!
