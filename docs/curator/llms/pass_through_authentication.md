# Source: https://docs.curator.interworks.com/setup/authentication/pass_through_authentication.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Pass-Through Authentication

> An overview of the Pass-Through Authentication method in Curator.

export const BackendNavPath = ({levelOne, levelTwo, levelThree, tab, section}) => {
  const levels = [levelOne, levelTwo, levelThree].filter(Boolean);
  const lastLevel = levels.length ? levels[levels.length - 1] : '';
  return <span>
      In the <a href="/setup/installation/linux_installation">backend of Curator</a> using the left-hand navigation,
      navigate to the
      {levelOne && <strong>{" " + levelOne}</strong>}
      {levelOne && levelTwo && " > "}
      {levelTwo && <strong>{levelTwo}</strong>}
      {levelTwo && levelThree && " > "}
      {levelThree && <strong>{levelThree}</strong>} page.
      {(tab || section) && <>
          {" "}On the {lastLevel} page
          {tab && <> click the <strong>{tab}</strong> tab</>}
          {tab && section && " and"}
          {section && <> expand the <strong>{section}</strong> section</>}.
        </>}
    </span>;
};

export const allEmbedTypes = ['Tableau', 'Power BI', 'Sigma', 'ThoughtSpot'];

"Pass-Through" authentication is the default security setting in Curator. This does not mean it's recommended though -
in fact typically it's *not* recommended as it's the lowest security setting available.  However, it allows you to
quickly get started with Curator and your analytics content, and is a good way to test out the platform before
committing to a more secure or complex authentication method, or it can be useful if you would like to use Curator
in a public-facing manner where you will have almost entirely anonymous users who may or may not have access to
<Tooltip tip={allEmbedTypes.join(', ')}>analytics content</Tooltip>.

## Changing Authentication Settings to Pass-Through

<BackendNavPath levelOne="Settings" levelTwo="Security" levelThree="Authentication Settings" tab="General" section="Authentication Type" />

Select the **Pass-Through (Security Disabled)** option and be sure to save your changes.

<img src="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/authentication/pass_through_authentication/enable_pass_through.png?fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=6df805f9d47b8df4ee8bbba937759321" alt="Authentication settings page with Pass-Through selected" data-og-width="2880" width="2880" data-og-height="1800" height="1800" data-path="assets/images/setup/authentication/pass_through_authentication/enable_pass_through.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/authentication/pass_through_authentication/enable_pass_through.png?w=280&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=c5f38ee2c725c064ad69b9aa0d7b448c 280w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/authentication/pass_through_authentication/enable_pass_through.png?w=560&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=529f76b501743acc4888814d84ae5b38 560w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/authentication/pass_through_authentication/enable_pass_through.png?w=840&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=e0960b0d7de273867f216e8be6dfff39 840w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/authentication/pass_through_authentication/enable_pass_through.png?w=1100&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=1cae4f074b26f5d59ac3dd7624fcf6d5 1100w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/authentication/pass_through_authentication/enable_pass_through.png?w=1650&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=b9f2ec80bd6e2c3f10983cc8da25bfb1 1650w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/authentication/pass_through_authentication/enable_pass_through.png?w=2500&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=918e11ff03e5881ee90097a50e3d6e13 2500w" />
