# Source: https://docs.statsig.com/guides/config-history.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Config History

## Entity Change History

Change history for entities like Feature Gates, Experiments, Dynamic Configs, and Segments can be accessed by clicking the "History" button on the top right of their respective page.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/W8Ofi9vALiNXCKIR/images/config_history.png?fit=max&auto=format&n=W8Ofi9vALiNXCKIR&q=85&s=4ffc7d98c07c6692a968b408c9849918" alt="Config History" width="730" height="290" data-path="images/config_history.png" />
</Frame>

This page shows each change to a given config and the time that change was published.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/n7aLPkvQ3ml2MAiO/images/guides/config-history/169888219-6dd20bb4-2d22-4396-b9cb-ebe3a7307b90.png?fit=max&auto=format&n=n7aLPkvQ3ml2MAiO&q=85&s=32dd9cc0be730e953a82dc8e6ce334dd" alt="History timeline listing published config changes" width="834" height="742" data-path="images/guides/config-history/169888219-6dd20bb4-2d22-4396-b9cb-ebe3a7307b90.png" />
</Frame>

For Feature Gates and Dynamic Configs, there is also a "Preview" and "Restore" option. These are meant to make it easy to revert to a previous state, particularly if you start rolling something out that is causing issues in production.
The "preview" action will show a diff view between the current state of the gate and the previous state you selected, so you can make sure you are reverting to the correct state.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/n7aLPkvQ3ml2MAiO/images/guides/config-history/169888598-df6f94ee-0194-4f09-906e-d85ed89cd554.png?fit=max&auto=format&n=n7aLPkvQ3ml2MAiO&q=85&s=36943d7955cc171947184bc1b1321d20" alt="Preview and restore dialog comparing config versions" width="853" height="717" data-path="images/guides/config-history/169888598-df6f94ee-0194-4f09-906e-d85ed89cd554.png" />
</Frame>

For Gates, Dynamic Configs, and Segments, you can also select two different versions, and compare the differences between the states of the entity between the two versions.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/F_V_VJJ-2qC3MQMI/images/config_history_compare_changes.png?fit=max&auto=format&n=F_V_VJJ-2qC3MQMI&q=85&s=56b937f6ca098a0408b5412bc82f3dcf" alt="Compare Configs" width="2512" height="1476" data-path="images/config_history_compare_changes.png" />
</Frame>

<Info>
  Note that changes in nested configs are not listed (e.g. if this gate references another gate or segment via a "Passes Target Gate" or "User in Segment" condition, changes to the other gate or segment will not show in the history view).
</Info>

## Audit Logs

Audit logs will show you the change history for all available entities across the entire project. These audit logs are stored indefinitely and you can filter by entity type or name, tag, target app, environment, action, and user who triggered the action.
Audit logs can be accessed programmatically or though the Statsig Console UI in **Settings** > [Audit Logs](https://console.statsig.com/audit_logs).


Built with [Mintlify](https://mintlify.com).