# Source: https://docs.crewai.com/en/enterprise/guides/update-crew.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.crewai.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Crew

> Updating a Crew on CrewAI AMP

<Note>
  After deploying your crew to CrewAI AMP, you may need to make updates to the
  code, security settings, or configuration. This guide explains how to perform
  these common update operations.
</Note>

## Why Update Your Crew?

CrewAI won't automatically pick up GitHub updates by default, so you'll need to manually trigger updates, unless you checked the `Auto-update` option when deploying your crew.

There are several reasons you might want to update your crew deployment:

* You want to update the code with a latest commit you pushed to GitHub
* You want to reset the bearer token for security reasons
* You want to update environment variables

## 1. Updating Your Crew Code for a Latest Commit

When you've pushed new commits to your GitHub repository and want to update your deployment:

1. Navigate to your crew in the CrewAI AMP platform
2. Click on the `Re-deploy` button on your crew details page

<Frame><img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/redeploy-button.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=1dc96ae0dd8f0dc2f5f62f58ebd6e5d0" alt="Re-deploy Button" data-og-width="980" width="980" data-og-height="852" height="852" data-path="images/enterprise/redeploy-button.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/redeploy-button.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=8d240851abcc6a015002a129ac12274b 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/redeploy-button.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=2655800484e20180df0d3bc88e563ef8 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/redeploy-button.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f8d7850c288577c99242ada871e5eb7c 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/redeploy-button.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=d5c4dd51e512466df9209fa6218bbb9e 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/redeploy-button.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=15e03da40d3e92fe0c9615b28f4efce8 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/redeploy-button.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=8d29aa1f4ac64a30a01c449b2f31aead 2500w" /></Frame>

This will trigger an update that you can track using the progress bar. The system will pull the latest code from your repository and rebuild your deployment.

## 2. Resetting Bearer Token

If you need to generate a new bearer token (for example, if you suspect the current token might have been compromised):

1. Navigate to your crew in the CrewAI AMP platform
2. Find the `Bearer Token` section
3. Click the `Reset` button next to your current token

<Frame><img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/reset-token.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c38b0a22de7a192a1962b4b371e03119" alt="Reset Token" data-og-width="980" width="980" data-og-height="840" height="840" data-path="images/enterprise/reset-token.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/reset-token.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=759453ab874cffd228bbbc91db2cbe3c 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/reset-token.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=365f3075be71ad8ed85e1a9ba7cbe9b5 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/reset-token.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=7b689e67e67abb1e39cd6e98efa1e562 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/reset-token.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=7dfbd9d08e16bb16de00d6e7fde00a6d 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/reset-token.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=900c92322f9cd90732ccdfa1f8d9ea42 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/reset-token.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=000718aaaa645b109514bc72c2f0b70e 2500w" /></Frame>

<Warning>
  Resetting your bearer token will invalidate the previous token immediately.
  Make sure to update any applications or scripts that are using the old token.
</Warning>

## 3. Updating Environment Variables

To update the environment variables for your crew:

1. First access the deployment page by clicking on your crew's name

<Frame>
    <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/env-vars-button.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=740ad7bcf5b860f35fe9fddd7a707271" alt="Environment Variables Button" data-og-width="1216" width="1216" data-og-height="598" height="598" data-path="images/enterprise/env-vars-button.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/env-vars-button.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=a4bdc54aee3c54cedc4c25f0b0e28aaa 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/env-vars-button.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f3012e2c4257313f080afeb2ab0c690b 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/env-vars-button.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=9532e4a7281391aacacc1faaf14e6f74 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/env-vars-button.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=ea0aaee0f92be7b9ef4b62cc64e12877 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/env-vars-button.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=ca4a47c02e4761b05b83af8fb118e915 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/env-vars-button.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=542188110b78b31121abba738a28019d 2500w" />
</Frame>

2. Locate the `Environment Variables` section (you will need to click the `Settings` icon to access it)
3. Edit the existing variables or add new ones in the fields provided
4. Click the `Update` button next to each variable you modify

<Frame>
    <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/update-env-vars.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=461ca7ce61dd14a4344f6237c584b891" alt="Update Environment Variables" data-og-width="2888" width="2888" data-og-height="1914" height="1914" data-path="images/enterprise/update-env-vars.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/update-env-vars.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=9afc7b7e194a371365d7b69edc0ddac6 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/update-env-vars.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=8ccb5b296eab23dd57cc241f7f445589 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/update-env-vars.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=374a4a1f02dd73e7eb7e30e4de59b0ac 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/update-env-vars.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=23357a7c2e61f08b456e20450eaa255f 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/update-env-vars.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=bb82e60664a74c99ae0fa88dae8366a8 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/update-env-vars.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=1d764223f3032607fd6d2577452c021a 2500w" />
</Frame>

5. Finally, click the `Update Deployment` button at the bottom of the page to apply the changes

<Note>
  Updating environment variables will trigger a new deployment, but this will
  only update the environment configuration and not the code itself.
</Note>

## After Updating

After performing any update:

1. The system will rebuild and redeploy your crew
2. You can monitor the deployment progress in real-time
3. Once complete, test your crew to ensure the changes are working as expected

<Tip>
  If you encounter any issues after updating, you can view deployment logs in
  the platform or contact support for assistance.
</Tip>

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with updating your crew or
  troubleshooting deployment issues.
</Card>
