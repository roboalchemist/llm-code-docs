# Source: https://loops.so/docs/integrations/census.md

> ## Documentation Index
> Fetch the complete documentation index at: https://loops.so/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Census

> Send user data from your data warehouse to Loops.

<Info>
  Our Census integration lets you:

  * Create and update contacts
  * Trigger loops when contacts are created or updated
</Info>

Loops is a partnered destination for Census. We support syncing data via `userId` or `email`.

<Warning>
  New contacts cannot be created if no email is provided.
</Warning>

Within the Census app, go to **Destinations** and click **+ New Destination**.

Select the **Loops** destination.

<img src="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/census-loops-destination.png?fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=9f98daaada92cb75aa11a676002b5efa" alt="Add Loops destination" data-og-width="2280" width="2280" data-og-height="860" height="860" data-path="images/census-loops-destination.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/census-loops-destination.png?w=280&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=a59676545519fe0a7a1a999aec6dea49 280w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/census-loops-destination.png?w=560&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=b44cec4c0052d109176431829afb5f8e 560w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/census-loops-destination.png?w=840&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=1e0745e884deee56f3ee20db93e59358 840w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/census-loops-destination.png?w=1100&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=689a2086be096384bf8086bb29ecc0fd 1100w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/census-loops-destination.png?w=1650&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=4bf52de5116070beb4ccb05af6353fa6 1650w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/census-loops-destination.png?w=2500&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=0bfb9711f7b614483a95aa19e4872a58 2500w" />

You will be prompted to enter your Loops API Token, which you can find on your [API settings page](https://app.loops.so/settings?page=api), and to decide if you want to trigger loops when contacts are created or updated.

<img src="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/census-destination-modal.png?fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=f81896e9b3e936c44aabfef1bc28c001" alt="Create a destination" data-og-width="2280" width="2280" data-og-height="1248" height="1248" data-path="images/census-destination-modal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/census-destination-modal.png?w=280&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=4350d088df3b5e2a40b9ae37d1da854f 280w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/census-destination-modal.png?w=560&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=a7be431039777b5515ce41919778f17b 560w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/census-destination-modal.png?w=840&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=5b8b70720b44cf2b660667a1019a4e1b 840w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/census-destination-modal.png?w=1100&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=86b34a86caab09f8060e011281ea42ef 1100w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/census-destination-modal.png?w=1650&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=570eaee32287ad91f10a4c772e740e67 1650w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/census-destination-modal.png?w=2500&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=9cc200fc6008b20997e063724c142cfe 2500w" />

Click **Connect** and test out your destination.

Loops will now be available as a destination in Census.

<img src="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/census-destination-loops.png?fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=f53488c47f0b422bc599a0b4e464dc2f" alt="Use the Loops destination" data-og-width="2280" width="2280" data-og-height="1031" height="1031" data-path="images/census-destination-loops.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/census-destination-loops.png?w=280&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=4d4422acdad6d0c6747b41e50d42b828 280w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/census-destination-loops.png?w=560&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=cfe8db1ed01b64cdef717949eae8983f 560w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/census-destination-loops.png?w=840&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=0dedbfa67b97fcfc3d42a025c5ce5af5 840w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/census-destination-loops.png?w=1100&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=8c22653f5016d50e91e52dacd1319c06 1100w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/census-destination-loops.png?w=1650&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=124d389ea65e837e1c48408b5f69331b 1650w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/census-destination-loops.png?w=2500&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=25faedd85044b768c8f6349521e52ce3 2500w" />

When choosing a sync behavior, you can choose either **Update or Create** or **Mirror**.

<img src="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/census-sync-behavior.png?fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=57086c808ce26f993cbae4ff353c28e1" alt="Choose sync behavior" data-og-width="2280" width="2280" data-og-height="890" height="890" data-path="images/census-sync-behavior.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/census-sync-behavior.png?w=280&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=b8dc21dbd62a1f2162f5b9138be31e53 280w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/census-sync-behavior.png?w=560&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=dd2dcdeb98a881e907b8a759cfe36af0 560w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/census-sync-behavior.png?w=840&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=c0fe68cf00ab5dfb3726abed9a9c62c8 840w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/census-sync-behavior.png?w=1100&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=8917d6736d7becc3faa2f941744806c0 1100w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/census-sync-behavior.png?w=1650&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=e4ca7a5f9351a23d32e6af63d182cc54 1650w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/census-sync-behavior.png?w=2500&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=6b3d0a00db324a9c52d43e64a480a1d0 2500w" />
