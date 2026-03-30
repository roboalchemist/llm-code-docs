# Source: https://docs.base44.com/Integrations/AI-integrations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# AI Integrations in Base44

> Connect your Base44 app to popular AI services like OpenAI, Claude, Groq, Mistral or any other AI platform that uses an API key. 

<Info>
  <u>Note</u>: AI integrations are available on Builder tier and above. If you're on the Free tier, you'll need to upgrade your app to use backend functions and payment features.
</Info>

# Step-by-step setup

## Part 1: The AI provider's side

If you already have your secrets or API keys, you can skip ahead to "The Base44 side" setup

<Steps>
  <Step title="Visit your AI provider’s developer portal">
    1. Open your provider’s developer portal in a new browser tab 

       <img src="https://mintcdn.com/base44/oUaRpzSyJvMVshj9/images/OpenAI-APIkeys.png?fit=max&auto=format&n=oUaRpzSyJvMVshj9&q=85&s=1a25b7103ea07de0048ab5e0bbba8721" alt="Open AI AP Ikeys Pn" width="2780" height="1338" data-path="images/OpenAI-APIkeys.png" />

       <Info>
         We're using OpenAI for this example and their developer portal is at: [https://platform.openai.com](https://platform.openai.com)
       </Info>
    2. Log in or create a new account
    3. Go to the **API keys** section
  </Step>

  <Step title="New Enable API access if needed">
    1. Go to your provider’s **billing** or \*\*payment \*\*section.

       <img src="https://mintcdn.com/base44/oUaRpzSyJvMVshj9/images/OpenAI-billing.png?fit=max&auto=format&n=oUaRpzSyJvMVshj9&q=85&s=61ecfca5a6bc9179076bc82e5e9d688f" alt="Open AI Billing Pn" width="2796" height="1336" data-path="images/OpenAI-billing.png" />

       <Warning>
         To obtain and utilize an OpenAI API key, a paid account is required. While creating an OpenAI account is free, using the API necessitates funding the account with a credit balance or having a billing method on file. OpenAI operates on a pay-per-use model for its API services, where charges are incurred based on the actual usage of the models.
       </Warning>
    2. Add a valid payment method such as a credit card or PayPal.
    3. (Optional) Set up a spending limit to control costs.

       <img src="https://mintcdn.com/base44/oUaRpzSyJvMVshj9/images/OpenAI-usage.png?fit=max&auto=format&n=oUaRpzSyJvMVshj9&q=85&s=e887dcc59aebda2141cd454b28047467" alt="Open AI Usage Pn" width="2808" height="1348" data-path="images/OpenAI-usage.png" />
    4. Make sure your account has active credits if your provider requires it.
  </Step>

  <Step title="Create a new API key">
    1. In your provider’s API keys section, click **Create new API key** 

       <img src="https://mintcdn.com/base44/oUaRpzSyJvMVshj9/images/OpenAI-createsecretkey.png?fit=max&auto=format&n=oUaRpzSyJvMVshj9&q=85&s=0b30844f4622e85c9ef1388d634eb009" alt="Open AI Createsecretkey Pn" width="2788" height="1332" data-path="images/OpenAI-createsecretkey.png" />

       <Info>
         <u>Note</u>: The button text may be different across providers. Sometimes it may be called "Create new secret"
       </Info>
    2. Copy the generated key immediately because you may not be able to see it again.
  </Step>
</Steps>

## Part 2: The Base44 Side

<Steps>
  <Step title="Go to the Base44 integration catalog">
    Head to Base44 and click on **Integrations**

        <img src="https://mintcdn.com/base44/oUaRpzSyJvMVshj9/images/Integrations.png?fit=max&auto=format&n=oUaRpzSyJvMVshj9&q=85&s=16ac71b185167177ef260be7c92b0339" alt="Integrations Pn" width="1570" height="652" data-path="images/Integrations.png" />

    <Info>
      Make sure you're logged into Base44 to view the [Integrations catalog page](https://app.base44.com/integrations-catalog)
    </Info>

    2. Use the search bar or scroll to find your **AI provider**
    3. Select your **AI provider** and click **“Use this integration**” \
       (in this example we are using OpenAI)

       <img src="https://mintcdn.com/base44/UsrMcs9B3MEl2R91/images/Base44-OpenAI-integration.png?fit=max&auto=format&n=UsrMcs9B3MEl2R91&q=85&s=8520105d22c0414d2fa69905b8b8e4b4" alt="Base44 Open AI Integration Pn" width="2768" height="1326" data-path="images/Base44-OpenAI-integration.png" />
  </Step>

  <Step title="Add your API key to Base44">
    1. Type out your app idea inside the AI chat box 
    2. Paste the key when prompted

       <img src="https://mintcdn.com/base44/oUaRpzSyJvMVshj9/images/Integrations-pasteAPIkey.png?fit=max&auto=format&n=oUaRpzSyJvMVshj9&q=85&s=d26fd8ef2d13ba31923157049b9b4249" alt="Integrations Paste AP Ikey Pn" width="1501" height="738" data-path="images/Integrations-pasteAPIkey.png" />

       Example: For OpenAI you might see: OPENAI\_API\_KEY

    <Tip>
      Optional: You can save your key securely in **Dashboard → Secrets** so you can reuse it later.
    </Tip>

    <Warning>
      Important: Never paste API keys into public code, visible components, or prompts.
    </Warning>
  </Step>

  <Step title="Tell the AI what to do">
    1. Once your app has been created, in the Base44 chat, describe the task you want the AI to perform

       <img src="https://mintcdn.com/base44/oUaRpzSyJvMVshj9/images/Integrations-imagegen1.png?fit=max&auto=format&n=oUaRpzSyJvMVshj9&q=85&s=06229c9da7abb8460c5b93771c066258" alt="Integrations Imagegen1 Pn" width="2824" height="1378" data-path="images/Integrations-imagegen1.png" />
    2. Base44 will create the backend and frontend components for you.
    3. You can improve the AI’s behavior with follow-up prompts.
  </Step>

  <Step title="Test your AI integration">
    1. Try your AI feature with test inputs or example prompts.

       <img src="https://mintcdn.com/base44/-Vklow6W-uVvNnvR/images/learnlink-imagegen.png?fit=max&auto=format&n=-Vklow6W-uVvNnvR&q=85&s=63ffd932e9812443ea118aa13f6f92a6" alt="Learnlink Imagegen Pn" width="1000" height="494" data-path="images/learnlink-imagegen.png" />
    2. Check the AI’s output.
    3. Experiment with different styles, tones, or examples until it works the way you want.

    <Info>
       When running tests, do not paste real customer data. Use sample or dummy content.
    </Info>
  </Step>

  <Step title="Go live">
    Once everything works:

    * Preview your app on different devices
    * Deploy it and share with others
    * Monitor your **API usage** in your provider’s dashboard
  </Step>
</Steps>

## **Recap**

What you did (no coding required)

* Selected an AI provider for your use case.
* Connected it securely with an API key.
* Let Base44 handle the backend setup.
* Used prompts to design your AI’s behavior.
* Tested and launched your AI-powered app.

You now have a working AI integration. You can repeat these steps for any provider that uses API keys, not just OpenAI. 

## FAQ

<AccordionGroup>
  <Accordion title="What if my provider is not listed in the catalog">
    You can still connect it with help from the Base44 AI. The process is a little more manual, but the AI will guide you step by step.

    Say: `"Use the provider “[provider name]”. I have an api key. Help me connect it and create a simple test. Ask me for the details you need."`

    Keep your API key somewhere safe until the AI asks for it. You will also need a few details from your provider’s documentation.

    <Info>
      **Some important requirements for manual setup**\
      Your provider needs to offer a standard online API that works over https (often called a “REST API”). This means:

      * A web address (URL) where Base44 can send requests.
      * An API key for authentication.\
        Instructions from the provider on what information to send and how it should be formatted.
      * Details on how the provider will send responses back, ideally in a format like JSON (a common way to send structured text).
    </Info>
  </Accordion>

  <Accordion title="How do I keep my API key safe?">
    Store it in Base44’s **Secrets** section or a password manager. Never share it in public code, screenshots, or chat messages.
  </Accordion>

  <Accordion title="What happens if I run out of credits with my provider?">
    Your AI integration will stop working until you add more credits or update your billing settings with the provider.
  </Accordion>

  <Accordion title="Do I need to know how to code to use AI in Base44?">
    No. You can set everything up by following the steps in the guide and writing prompts in plain language.
  </Accordion>

  <Accordion title="Can I change my AI provider later?">
    Yes. You can connect to a different provider at any time. You will need to add the new API key in Base44 and may need to update your prompts or components so they work with the new provider’s API.
  </Accordion>

  <Accordion title="How can I limit costs?">
    Most AI providers let you set spending limits or usage caps in your account’s billing settings. You can also monitor your usage in their dashboard. For testing, try shorter prompts or smaller requests to keep costs low. Keep in mind that each provider’s cost controls work a little differently, so it’s a good idea to check their help docs.
  </Accordion>

  <Accordion title="Why is my AI giving unexpected answers?">
    Make your prompt more specific. Include clear instructions, important context, and examples of what you want. If possible, tell the AI what *not* to include. You can also try switching to a different model if your provider offers one that is more focused on accuracy. If the problem continues, share the prompt and response with the Base44 AI and ask it to help troubleshoot step by step.

    “If you get stuck, paste your prompt and the AI’s response into the Base44 chat and say ‘help me troubleshoot this step by step.’”
  </Accordion>

  <Accordion title="Can I use more than one AI provider at the same time?">
    Yes. You can add multiple integrations in Base44, you would just need to make sure you specify which provider will be used for which function
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).