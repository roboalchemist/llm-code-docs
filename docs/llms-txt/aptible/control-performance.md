# Source: https://www.aptible.com/docs/core-concepts/security-compliance/security-compliance-dashboard/control-performance.md

# Control Performance

Security controls in-place check for the implementation of a specific safeguard. If you have not implemented a particular control , appropriate notifications are provided in the Aprible Dashboard to indicate the same, with relevant recommendations to remediate.

You can choose to ignore a control implementation, thereby no longer seeing the notification in the Aptible Dashboard and ensuring it does not affect your overall compliance readiness score.

In the example below, [container logging](/core-concepts/observability/logs/overview) was not implemented in the *aptible-misc* environment.

<img src="https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/73a2f64-compliance-visibility-container-logging.png?fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=42cc9d3246da9ad2e03f907309b8b44f" alt="Image" data-og-width="3580" width="3580" data-og-height="1828" height="1828" data-path="images/73a2f64-compliance-visibility-container-logging.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/73a2f64-compliance-visibility-container-logging.png?w=280&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=f8732e006f44c454518898c9260fb40c 280w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/73a2f64-compliance-visibility-container-logging.png?w=560&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=d3374c456d67beea9931a64c67befb88 560w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/73a2f64-compliance-visibility-container-logging.png?w=840&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=d27f1bf42ff93432b33a49c9f16d642c 840w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/73a2f64-compliance-visibility-container-logging.png?w=1100&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=b8d678e2819172040b6724d2dfa02811 1100w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/73a2f64-compliance-visibility-container-logging.png?w=1650&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=cd5ada5d5b2a90cb8b83c6bc71ca2f30 1650w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/73a2f64-compliance-visibility-container-logging.png?w=2500&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=11851166df515180cd0f52c2cb47c793 2500w" />

In such a scenario, you have two options:

## Option 1: Remediate and Implement Control

Based on the remediation recommendations provided in the platform for a control you haven’t implemented, you could follow the appropriate instructions to implement the control in question. Coming to the example provided above, the user with `write` access to the aptible-misc environment can configure a log drain collecting and aggregating their container logs in a destination of choice. Doing this would be an acceptable implementation of the specific control, thereby remediating the issue of non-compliance.

## Option 2: Ignore Implementation

You could also ignore the control implementation based on your organization’s judgment for the specific resource. Choosing to ignore the control implementation will signal to Aptible to also ignore the implementation of the particular control, which in the example above, was the *aptible-misc* environment. Doing so would no longer show you a warning in the UI indicating that you have not implemented the control  and would ensure it does not affect your compliance readiness score.

You can see control implementations you’ve ignored in the expanded view of each control. You can also unignore the control implementation if needed.

<img src="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/cff01f0-compliance-visibility-ignore.gif?s=db9ad75665118f31f183f2542c074b17" alt="Image" data-og-width="640" width="640" data-og-height="318" height="318" data-path="images/cff01f0-compliance-visibility-ignore.gif" data-optimize="true" data-opv="3" />
