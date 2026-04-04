# Source: https://docs.sonarsource.com/sonarqube-server/8.9/user-guide/sonarlint-smart-notifications.md

# SonarLint smart notifications

Smart notifications allow developers using Connected Mode in SonarLint to receive in-IDE notifications from SonarQube when:

* the Quality Gate status (failed / success) of a project /solution *open in the IDE* changes
* a SonarQube analysis raises new issues *introduced by this developer in a project /solution open in the IDE*

### Activate/deactivate notifications <a href="#activate-deactivate-notifications" id="activate-deactivate-notifications"></a>

The activation or deactivation of notifications must be done individually, by each developer directly in SonarLint (on the IDE side).

Receiving notifications is configurable on the SonarLint side on a SonarQube server-by-server basis.
