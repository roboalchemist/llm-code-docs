# Source: https://docs.fireworks.ai/fine-tuning/using-secret-in-evaluator.md

# Using Secrets

> Learn how to create secrets that can be utilized within your reward function.

# Creating Secrets

<Steps>
  <Step title="Navigate to the secrets page on your dashboard">
        <img src="https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/new.png?fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=5a5a1f8a626c6e678d22a44addde7fc5" alt="new.png" data-og-width="1540" width="1540" data-og-height="1106" height="1106" data-path="images/new.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/new.png?w=280&fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=fad25753520447ffdbb63182fc92d194 280w, https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/new.png?w=560&fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=ed05cd99096aa33925c989fc19157402 560w, https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/new.png?w=840&fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=bcc4928202a856b5a0d8593dfce2d5e8 840w, https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/new.png?w=1100&fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=bc5a42177b80825f9d73531180c34088 1100w, https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/new.png?w=1650&fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=7e78b4e3c90000837e7967da461cd13a 1650w, https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/new.png?w=2500&fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=d279764c7f5a0b7c4f94bc853fb19950 2500w" />
  </Step>

  <Step title="Create a new secret">
        <img src="https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/test.png?fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=5b398ccbb320787377d235b9114bdc8d" alt="test.png" data-og-width="1826" width="1826" data-og-height="964" height="964" data-path="images/test.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/test.png?w=280&fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=23ec9e053dfaccbac993cf5554db0c5e 280w, https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/test.png?w=560&fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=87d4aa204ceee34d9b2bb7826a7786b8 560w, https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/test.png?w=840&fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=98ed857288a080843053ecc42d52b809 840w, https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/test.png?w=1100&fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=2342b7078b857409fa37724cd0e9ac92 1100w, https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/test.png?w=1650&fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=b8653468aa02bb04f0c7621ec1d13f40 1650w, https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/test.png?w=2500&fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=f47a1dd88880fa5976571540f91478d0 2500w" />

    All secrets created here will be injected as environment variables for your Evaluator to access.
  </Step>

  <Step title="Update the Evaluator to access the new secret">
        <img src="https://mintcdn.com/fireworksai/htXrlzmlFtUdajJX/fine-tuning/openai_secret.png?fit=max&auto=format&n=htXrlzmlFtUdajJX&q=85&s=d51579ef3f497ab478898f7b8f2529f8" alt="openai_secret.png" data-og-width="1462" width="1462" data-og-height="1420" height="1420" data-path="fine-tuning/openai_secret.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/htXrlzmlFtUdajJX/fine-tuning/openai_secret.png?w=280&fit=max&auto=format&n=htXrlzmlFtUdajJX&q=85&s=42b2741a2fb733e99c72220821b7e942 280w, https://mintcdn.com/fireworksai/htXrlzmlFtUdajJX/fine-tuning/openai_secret.png?w=560&fit=max&auto=format&n=htXrlzmlFtUdajJX&q=85&s=5faf69b15ad549b960368eb194f02dd1 560w, https://mintcdn.com/fireworksai/htXrlzmlFtUdajJX/fine-tuning/openai_secret.png?w=840&fit=max&auto=format&n=htXrlzmlFtUdajJX&q=85&s=85680748efbd1d720bb2dbc294bda527 840w, https://mintcdn.com/fireworksai/htXrlzmlFtUdajJX/fine-tuning/openai_secret.png?w=1100&fit=max&auto=format&n=htXrlzmlFtUdajJX&q=85&s=579e56dbe4bb417a693622ad5548c2ac 1100w, https://mintcdn.com/fireworksai/htXrlzmlFtUdajJX/fine-tuning/openai_secret.png?w=1650&fit=max&auto=format&n=htXrlzmlFtUdajJX&q=85&s=af3a279689dba12c84861b29b44c0a9a 1650w, https://mintcdn.com/fireworksai/htXrlzmlFtUdajJX/fine-tuning/openai_secret.png?w=2500&fit=max&auto=format&n=htXrlzmlFtUdajJX&q=85&s=4dba4f485e37101de7143f21dc2578cc 2500w" />
  </Step>
</Steps>

And that's it! If you want to learn more about creating evaluators, see:

1. Learn about [Evaluation](/fine-tuning/evaluators) and [Eval Protocol](https://evalprotocol.io/introduction) for evaluator authoring
