# Source: https://docs.statsig.com/guides/customer-io-email-abtest.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Email AB Testing with Customer.io

Email campaigns are a critical tool for any Marketing team.  Finding the best performing Email template is a perfect use-case for an A/B test.  Statsig allows you to run simple but powerful A/B tests on different parts of your email content.  Since Statsig can integrate seamlessly with product analytics, you can run email experiments and understand deeper business level impact on product metrics easily.

<Info>
  This guide assumes you have an existing Statsig account.  Please go here to create a new free account if you don't already have one: [https://statsig.com/signup](https://statsig.com/signup)
</Info>

### Step 1: Create an experiment

Start by creating a new Experiment on Statsig console. Put in a name and leave the rest of the fields empty/default.  For the purposes of this walkthrough, that should do.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/JoVpINC5Q0MyHWkm/images/guides/sendgrid-email-abtest/210731384-8bbfc1e1-076c-4ae3-959a-ef1507801e71.png?fit=max&auto=format&n=JoVpINC5Q0MyHWkm&q=85&s=0b0fa3839402d83ecb0866ed82582385" alt="Experiment creation interface" width="526" height="671" data-path="images/guides/sendgrid-email-abtest/210731384-8bbfc1e1-076c-4ae3-959a-ef1507801e71.png" />
</Frame>

### Step 2: Start the experiment

Since you can't start an experiment without a parameter, let's go ahead and add a dummy parameter.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/JoVpINC5Q0MyHWkm/images/guides/sendgrid-email-abtest/210316935-99f13616-c412-47c1-b9ab-99b90462805e.png?fit=max&auto=format&n=JoVpINC5Q0MyHWkm&q=85&s=9f0f1ae3daf84d279a175fad3e2bd756" alt="Experiment parameter configuration" width="374" height="142" data-path="images/guides/sendgrid-email-abtest/210316935-99f13616-c412-47c1-b9ab-99b90462805e.png" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/JoVpINC5Q0MyHWkm/images/guides/sendgrid-email-abtest/210731687-0883c356-5cef-458d-a6aa-bfde9ad36f8b.png?fit=max&auto=format&n=JoVpINC5Q0MyHWkm&q=85&s=0bff9e24eabac9ed58a4709c713c4934" alt="Experiment setup completion" width="510" height="385" data-path="images/guides/sendgrid-email-abtest/210731687-0883c356-5cef-458d-a6aa-bfde9ad36f8b.png" />
</Frame>

Save the experiment setup and **Start** it.  We're all set with the experiment set up.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/JoVpINC5Q0MyHWkm/images/guides/sendgrid-email-abtest/210731969-decf481a-b6a2-41ee-b1c1-6b917bb18fab.png?fit=max&auto=format&n=JoVpINC5Q0MyHWkm&q=85&s=0edc141bf8921b0c84b345c212e2e1c4" alt="Experiment start confirmation" width="845" height="188" data-path="images/guides/sendgrid-email-abtest/210731969-decf481a-b6a2-41ee-b1c1-6b917bb18fab.png" />
</Frame>

While you're at it, copy the **Experiment Name**.  We'll use this in a bit.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/JoVpINC5Q0MyHWkm/images/guides/sendgrid-email-abtest/210732298-34c0e1f4-6485-425b-af07-fa535ad86396.png?fit=max&auto=format&n=JoVpINC5Q0MyHWkm&q=85&s=ca9263b46ec199d074eeb256c2f911ec" alt="Experiment name copy interface" width="450" height="101" data-path="images/guides/sendgrid-email-abtest/210732298-34c0e1f4-6485-425b-af07-fa535ad86396.png" />
</Frame>

### Step 3: Set up Exposure Webhooks

In your Customer.io campaign, create a **Random Cohort Branch** which a flow similar to the following:

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/n7aLPkvQ3ml2MAiO/images/guides/customer-io-email-abtest/211873572-0966ae02-4a41-40a1-b55d-19378f1d0b98.png?fit=max&auto=format&n=n7aLPkvQ3ml2MAiO&q=85&s=e7918343647f3ce87d15f2b516408731" alt="Customer.io random cohort branch setup" width="1632" height="1338" data-path="images/guides/customer-io-email-abtest/211873572-0966ae02-4a41-40a1-b55d-19378f1d0b98.png" />
</Frame>

In the Webhook actions, put in a post request similar to the following, with your api key and experiment name filled in:

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/n7aLPkvQ3ml2MAiO/images/guides/customer-io-email-abtest/211873593-d48ed161-2a55-4099-8f06-7835ee82d011.png?fit=max&auto=format&n=n7aLPkvQ3ml2MAiO&q=85&s=21e7f2824d1869aa17bcbd4d434e98b7" alt="Webhook configuration for experiment exposure" width="1914" height="1168" data-path="images/guides/customer-io-email-abtest/211873593-d48ed161-2a55-4099-8f06-7835ee82d011.png" />
</Frame>

Pass in any other custom IDs and user attributes inside the post body.

For each webhook, make sure to expose the correct group that you'd like to attribute your branch to. In the above webhook, we are exposing the "Control" group.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/n7aLPkvQ3ml2MAiO/images/guides/customer-io-email-abtest/211873585-1b2da267-cd72-4c29-acde-d1888500ac36.png?fit=max&auto=format&n=n7aLPkvQ3ml2MAiO&q=85&s=f45e9ef9f1b8b90ee8697948cdec96c6" alt="Experiment group exposure configuration" width="2258" height="1382" data-path="images/guides/customer-io-email-abtest/211873585-1b2da267-cd72-4c29-acde-d1888500ac36.png" />
</Frame>

In Statsig, you'll now have exposures for each of your experiment groups.

## Holdouts

To use Statsig Holdouts with Customer.io, it's recommended to identify users that are part of a holdout via customer.io's identify function: [https://customer.io/docs/sdk/ios/identify/](https://customer.io/docs/sdk/ios/identify/)

Where you call Customer.io's identify method, you could check a Statsig holdout gate, and add an attribute to the user to mark that user as being in a holdout.

In your campaign, you'll be able to create a True/False branch to check whether a user is in the holdout.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/n7aLPkvQ3ml2MAiO/images/guides/customer-io-email-abtest/211888584-a164d8bf-0d78-4a6b-86ab-ea336fd2bc3a.png?fit=max&auto=format&n=n7aLPkvQ3ml2MAiO&q=85&s=3cd18a5812f1caab97f496ce8c51527c" alt="Customer.io holdout branch configuration" width="1590" height="1142" data-path="images/guides/customer-io-email-abtest/211888584-a164d8bf-0d78-4a6b-86ab-ea336fd2bc3a.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).