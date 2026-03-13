# Source: https://docs.logrocket.com/docs/why-have-my-sessions-stopped-recording.md

# Why have my sessions stopped recording?

Common reasons why new sessions aren't recording

## You've hit your monthly session quota

* Part of your LogRocket subscription is the number of sessions you can record each month, called your "session quota".
* You will see a red warning on your LogRocket dashboard if your session quota has been met.
* This quota resets on the same day each month
* You can view your session quota and reset data on the <Anchor label="Plans page here" target="_blank" href="https://app.logrocket.com/r/settings/plans">Plans page here</Anchor>

<Image align="center" border={true} width="600px" src="https://files.readme.io/05a36956897730c4119971e92ccc4a050a611e6ae54397c202cd2e5a9e72f491-Sessions_by_Day.png" className="border" />

<Image align="left" border={true} width="550px" src="https://files.readme.io/ac4c8bc55c41881869b998a98ca6e3491232e9c54b31f0346ac63841eff2a5a6-Session_Quota_Reached.png" className="border" />

<Image align="center" border={true} src="https://files.readme.io/549e6c3894bc943bee08623e0f0c5116e11df3cbdcc208f7a25e08f9a63fcfee-Session_Quota_Warning.png" className="border" />

## Recording Settings

* Have you paused recording for this project?
* Have you set a session limit that has been reached?
* check your <Anchor label="Recording Settings here " target="_blank" href="https://app.logrocket.com/r/settings/plans">Recording Settings here </Anchor>

<br />

<Image align="center" border={true} src="https://files.readme.io/525f8b42d17028d13136b27a421b07107d328693f74e99bee9310183b5b73f8d-Recording_Settings.png" className="border" />

<br />

## You've removed LogRocket.init from your app

* LogRocket.init is what triggers a session to be captured
* If you've removed LogRocket.init from your app, then new LogRocket sessions will not be recorded

<br />

## Conditional Recording (if you have this add-on)

* <Anchor label="Conditional Recording is an add-on" target="_blank" href="https://docs.logrocket.com/docs/conditional-recording">Conditional Recording is an add-on</Anchor> feature that allows you to set conditions for when to capture sessions
* If you've set conditions that are too strict, then you'll stop seeing sessions captured as frequently