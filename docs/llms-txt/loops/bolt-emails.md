# Source: https://loops.so/docs/guides/bolt-emails.md

# Send emails from Bolt.new

> How to integrate Loops transactional emails into a Bolt application.

<Info>
  This guide is for Bolt but this kind of approach will work with many AI web
  builders, and also for different kinds of Loops integrations, like adding
  newsletter signup forms or sending events with the API instead of
  transactional emails.
</Info>

[Bolt](https://bolt.new) is an in-browser AI web development tool. This guide shows how you can integrate Loops into your Bolt project.

In this guide we will build a simple to-do application in Bolt, with a daily email digest sent with Loops. It uses Supabase for authentication and database.

Adding Loops sending to Bolt can be boiled down to four steps:

1. Prompt Bolt to add a Loops integration
2. Set up emails in Loops
3. Add your Loops credentials and IDs
4. Check the code for mistakes

<img src="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-new.png?fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=7d3d535fcc138f3646aff6603dcfc9c7" alt="Bolt.new" data-og-width="2280" width="2280" data-og-height="1632" height="1632" data-path="images/bolt-new.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-new.png?w=280&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=4f3b64d3340b4efee3bfdc611b9a2e1a 280w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-new.png?w=560&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=c5a53fd6fef63f20cf5a2a9fa2d92543 560w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-new.png?w=840&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=31ee5713ab0fdca60178b143854f2c21 840w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-new.png?w=1100&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=f3dcad10532807f94df42fe90097d545 1100w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-new.png?w=1650&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=8795277f8135c7afe3300c5b26670ca2 1650w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-new.png?w=2500&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=b1dcc1f4659c8418bea0efd3cd19b16f 2500w" />

## 1. Create the app with a prompt

I wrote a prompt to create the app. In this prompt I included information about using the Loops API.

In Bolt you can choose to add Loops to your original prompt or ask it to add Loops in a later prompt.

For example:

> I want to add daily reminder emails that should be sent at 6am every morning showing the new day's list of tasks. I will send these emails as transactional emails using the Loops API (loops.so)

Using this prompt, Bolt added code to my app that spoke to Loops and had everything ready for me to add my Loops credentials, including a Supabase [Edge Function](https://supabase.com/docs/guides/functions) that could be run on a cron job.

<img src="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-app.png?fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=d29c16aa47e4a4f94804691528b23853" alt="Example Bolt application" data-og-width="2280" width="2280" data-og-height="1797" height="1797" data-path="images/bolt-app.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-app.png?w=280&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=82074d19920f7141b28ae0965f1192dc 280w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-app.png?w=560&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=86565a435eb25541435af58e3478225d 560w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-app.png?w=840&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=40e637149c8981acc5ef3e09eb08a9f1 840w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-app.png?w=1100&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=1e7fb33af8d3c15124301bea9c1b0b45 1100w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-app.png?w=1650&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=e5558883cbec5e537f09b11d7c145196 1650w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-app.png?w=2500&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=5c5ace89aeac9432df3c75c7c189b156 2500w" />

<Info>
  To improve the code that Bolt produces, you can upload our full LLM text
  [available here](https://loops.so/docs/llms-full.txt) and append it to the
  message.
</Info>

## 2. Create transactional email in Loops

Once you have the basics of the app working, you can move over to Loops to set up the digest email.

This will be a [transactional email](/transactional) (a 1:1 email for a single recipient), sent to each user every morning.

With Loops' transactional sending, you create the email body in the Loops editor and any dynamic content is added using [data variables](/creating-emails/personalizing-emails). Then, when it comes to sending the email via the API, you include the dynamic content in the API payload.

<img src="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-api-call.png?fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=ddc2bb992658455b58a5675a4a08185c" alt="API call to Loops" data-og-width="2280" width="2280" data-og-height="1797" height="1797" data-path="images/bolt-api-call.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-api-call.png?w=280&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=c28782acedcec7df7ca75b50cc373b5e 280w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-api-call.png?w=560&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=ba32c3734debac1277b741fd528c315d 560w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-api-call.png?w=840&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=400fa2a31281aac29286b7b280f6d8f4 840w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-api-call.png?w=1100&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=45333b00babf70519714175145449781 1100w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-api-call.png?w=1650&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=2157e9f0ef6faf16d1a7319ad0849f61 1650w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-api-call.png?w=2500&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=ec129f9af6d374a2c35cf1e4a8123ed8 2500w" />

In Loops, you'll need to create a new transactional email and write your content. Bolt added two data variables `tasks` and `date` to the code, so in my example I added those data variables to the email.

<img src="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-transactional.png?fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=5f0e196ab2fd5c17afbad87d63aa63e7" alt="Creating a transactional email in Loops" data-og-width="2280" width="2280" data-og-height="1257" height="1257" data-path="images/bolt-transactional.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-transactional.png?w=280&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=c226263fc715908b97daa51841311d9b 280w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-transactional.png?w=560&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=0cb122d0e76a868e8e7e40157349659f 560w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-transactional.png?w=840&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=751761a940555815485ce4b6a3d8b44e 840w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-transactional.png?w=1100&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=8175c2c682de5082c876ba7d11f5d053 1100w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-transactional.png?w=1650&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=242184faa11fea68dc23b782ba7ef892 1650w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-transactional.png?w=2500&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=500bde8d6dee3e44ce1f642a2ca343f3 2500w" />

## 3. Add Loops credentials

As part of the integration with Loops, you will need to add a Loops API key to your code. This tells Loops which account is sending data as well as making sure the correct apps have access to the correct data.

To do this, get an API key from your Loops [API Settings](https://app.loops.so/settings/?page=api) page.

For my example app I needed to add my Loops API key into the Edge Function's secrets in Supabase (**Edge functions -> Secrets**). I called mine `LOOPS_API_KEY` to match the name Bolt used in the code.

<img src="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-api-key.png?fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=6309173eeca21413ca03c25198ae53bb" alt="Loops API key" data-og-width="2280" width="2280" data-og-height="1365" height="1365" data-path="images/bolt-api-key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-api-key.png?w=280&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=bedd74b1029ba33ae3b22d64d4af01b9 280w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-api-key.png?w=560&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=3ed7045c05e220b468fdfdffacaa94f3 560w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-api-key.png?w=840&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=dfa3e887addf2d5279855852a5be8b8c 840w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-api-key.png?w=1100&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=f399809caad4b9cc1acb3dfd3069bbbf 1100w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-api-key.png?w=1650&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=e58be655770e340417bb3b5a39d3e5f3 1650w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-api-key.png?w=2500&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=07c17eeaef95b6cb0eae9d125723fcb8 2500w" />

<img src="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-supabase-secret.png?fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=6c6ede96f1623f1b07f774f23a6997ab" alt="Supabase secret" data-og-width="2280" width="2280" data-og-height="1797" height="1797" data-path="images/bolt-supabase-secret.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-supabase-secret.png?w=280&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=820798596d8192710cf68312d6770103 280w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-supabase-secret.png?w=560&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=05eb3711b2380a1b95d4ee4ab0abd004 560w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-supabase-secret.png?w=840&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=95bd54f46f91f1532052fa271f6bb04a 840w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-supabase-secret.png?w=1100&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=596ffaad71817424158bf36ce8cd4e24 1100w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-supabase-secret.png?w=1650&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=8d99b4513284ee0f5fa0539c46eb7b92 1650w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-supabase-secret.png?w=2500&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=138b6f6fd08a5b4eca76a14ef7f8987a 2500w" />

You will also need the ID of the transactional email so that the correct email is sent from your application.

In Loops, from the **Preview** page if your transactional email, copy the transactional ID and paste it into your app's code. This completes the Loops integration in the app.

<img src="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-transactional-id.png?fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=d58866ad63317e11987ad199ead403b0" alt="Transactional ID" data-og-width="2280" width="2280" data-og-height="2100" height="2100" data-path="images/bolt-transactional-id.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-transactional-id.png?w=280&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=4f02aa6f3b3531a2226f20e92dd7908a 280w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-transactional-id.png?w=560&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=b4992a27b6a223bff2aa358bd4904674 560w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-transactional-id.png?w=840&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=49552d20e17c24cc7fa77d725da488a5 840w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-transactional-id.png?w=1100&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=5824ebba95c18efe5505a9c6dc6ee372 1100w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-transactional-id.png?w=1650&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=c9f3af47247fd35cf7778fc7e18044a8 1650w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-transactional-id.png?w=2500&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=651666b1c5c1ac29044916620159f011 2500w" />

## 4. Fix bugs

Now that the app is set up, it's time to see if things are working correctly.

For me, I discovered a few bugs. For example, the original Google sign in that Bolt had added didn't work so I asked Bolt to change to email and password authentication. Overall the app worked as I had prompted. I could sign up and create tasks and the delay feature worked great.

<img src="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-tasks-app.png?fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=b0cb1614422b7bc73cf998a78bfe3226" alt="My new to-do app" data-og-width="2280" width="2280" data-og-height="2072" height="2072" data-path="images/bolt-tasks-app.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-tasks-app.png?w=280&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=61da0888e20f5c3efc1f1d9d0df9e9ff 280w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-tasks-app.png?w=560&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=bf23a4b0baeaceea70318c8b892f8be9 560w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-tasks-app.png?w=840&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=2fa1e6267eab65c86471b44f5fb51077 840w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-tasks-app.png?w=1100&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=4af42a298f1a5b3495fd9214f8b7bf08 1100w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-tasks-app.png?w=1650&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=003260f6c165541963e49e59fce4c6ac 1650w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-tasks-app.png?w=2500&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=ba5b510f1851732dc78f3503b976b592 2500w" />

Next I wanted to make sure the email sending was working. Because this was tied up in an edge function that is to be called with a scheduled cron job, I needed to find a way to test it on demand. Luckily, Supabase offers a simple API call to trigger functions. This can be run in the **Terminal** tab in Bolt.

<img src="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-function-invocation.png?fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=753df2573dff1cd0a284b62d81a3669c" alt="Invocation call" data-og-width="2280" width="2280" data-og-height="1430" height="1430" data-path="images/bolt-function-invocation.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-function-invocation.png?w=280&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=4a425e58c895acf67a3c6147210061e4 280w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-function-invocation.png?w=560&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=44f21ac14242e16b7df92e510a6e67a4 560w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-function-invocation.png?w=840&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=f94ff3c86f0a9ae3f7ddbcf782693ee2 840w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-function-invocation.png?w=1100&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=931a9b7462c619c48c52f7e816021a96 1100w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-function-invocation.png?w=1650&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=acfadff4b81a8945372764d4543e728d 1650w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-function-invocation.png?w=2500&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=18931f5fd78453727778663295f9e14d 2500w" />

<img src="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-terminal.png?fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=7ec3a16aeb3f0f143a8726a4354cf417" alt="Running a command in Bolt's terminal" data-og-width="2280" width="2280" data-og-height="956" height="956" data-path="images/bolt-terminal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-terminal.png?w=280&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=52e7b22583d78c3dd7027531e7c9fac9 280w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-terminal.png?w=560&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=b3585d56a17e7f919a7f179164b64624 560w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-terminal.png?w=840&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=f03c89effa7c269bce53d3bc0462eadd 840w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-terminal.png?w=1100&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=78d7c1bf7883f198d1d2d9ad7ff4de05 1100w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-terminal.png?w=1650&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=8bf687909a89ff4d27fa389fb8b99b92 1650w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-terminal.png?w=2500&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=04c117ecdd3ec76c062c5fc8398b89ba 2500w" />

Initially, I was seeing errors in the terminal.

```
{"success":true,"sent":0,"failed":1}
```

I realised that Bolt had incorrectly guessed the Loops API endpoint URL. This is a good example of AI-generated code needing sanity checking. I changed the URL to the [correct one](/api-reference/send-transactional-email).

<Note>
  To help with this kind of AI hallucination you can upload or link to our
  [LLM-friendly docs file](https://loops.so/docs/llms-full.txt) within your
  prompts or chats.
</Note>

<img src="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-api-url.png?fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=0d5ab11a36c59092c7e9ca7cd6033bef" alt="API URL" data-og-width="2280" width="2280" data-og-height="1470" height="1470" data-path="images/bolt-api-url.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-api-url.png?w=280&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=0ecd67bacf522bd261e80c52f2671e9b 280w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-api-url.png?w=560&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=326490ef7c258eacc377e2c2f2b9c351 560w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-api-url.png?w=840&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=e8d3db0714d72aa971595b35e979e034 840w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-api-url.png?w=1100&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=f4e47d96ac320e54a36b0b9fd44bc824 1100w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-api-url.png?w=1650&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=13c1226165163cef3aa0909443b8ac7e 1650w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-api-url.png?w=2500&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=eb9a01ecbea67ec21f7efc53ade77ef3 2500w" />

Supabase has great visibility of edge function invocations and error messages, which can help figure out when there's a problem.

<img src="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-supabase-logs.png?fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=88067f8d070b36da0670e473427b95d1" alt="Supabase logs" data-og-width="2280" width="2280" data-og-height="1499" height="1499" data-path="images/bolt-supabase-logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-supabase-logs.png?w=280&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=62af6d1279f91b1c058d19739525871d 280w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-supabase-logs.png?w=560&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=3d16c1b755b690a0eebca96d0a1b4921 560w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-supabase-logs.png?w=840&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=d5003f902b2272d82c27c452ecb98b70 840w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-supabase-logs.png?w=1100&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=5ccf0b9d102969f854e7731b6eed1d4b 1100w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-supabase-logs.png?w=1650&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=884b2e89ff575af5f7ed69e5c7b9ba5a 1650w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-supabase-logs.png?w=2500&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=c0670932d2c38357957a3ec60af81246 2500w" />

After a few tries, I started seeing succesful invocations of the edge function, and email digests in my inbox!

<img src="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-email.png?fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=2f50b1bc28a8d9281276fd3ebf16e77a" alt="Example email in my inbox" data-og-width="2280" width="2280" data-og-height="1499" height="1499" data-path="images/bolt-email.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-email.png?w=280&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=0d1bec6a39da8498a303a9ece4a7e57a 280w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-email.png?w=560&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=07a072b0be54eb8c0f3c7076365d00c9 560w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-email.png?w=840&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=2501a3566c783de80add301de54a5e4b 840w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-email.png?w=1100&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=736b282844aa7fd16eb930e9904ce8e4 1100w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-email.png?w=1650&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=93a31fa927374ac58979366a0bd25c65 1650w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bolt-email.png?w=2500&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=086cb444515ec832d9d4b35975df96f8 2500w" />

Here you can see that the current date and the task I had scheduled for the same day have been passed into the email body, which was handled by the data variables in the API call to Loops.

That's the end of this guide. Make sure to check out the rest of the Loops API to see what is possible when integrating to a Bolt-powered application.

<CardGroup>
  <Card title="Loops API" icon="rectangle-terminal" href="/api-reference">
    View all of our API endpoints.
  </Card>

  <Card title="Creating emails in the editor" icon="keyboard" href="/creating-emails/editor">
    Learn how to create stylized emails and add personalization.
  </Card>

  <Card title="Transactional guide" icon="file-code" href="/transactional">
    Read our detailed guide for sending transactional emails.
  </Card>
</CardGroup>
