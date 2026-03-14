# Source: https://docs.gitguardian.com/secrets-detection/core-concepts/where-to-implement-secrets-detection.md

# Where should you scan for secrets in the SDLC?

> Recommends a layered approach to implementing secrets detection across all stages of the SDLC.

We recommend you add automated secrets scanning wherever you can, at every stage of the SDLC.
Throwing as many nets as possible builds a layered defense and removes the dangers of having one single point of failure. We believe this should be the pursued strategy by every organization looking to reduce the risk of exposure of its secrets. Counter-intuitively, this layered approach adds little friction and can help you achieve wide-scale adoption from your developers.

We recommend starting with continuous monitoring for your VCS instances (server-side). Results at this level are more informative and non-blocking. As you get used to handling these results, you can incrementally increase the level of restriction, up to the point where it feels more accurate and in line with your organization. With GitGuardian, you will be able to gradually move secrets scanning upstream until you reach developer environments (client-side).

1. Start with continuous scanning for your remote repositories using
   the available native VCS integrations. It is an easy setup and guarantees your security team(s) total visibility over an evolving perimeter
   since repositories get created and deleted every day.

2. Add automated scanning jobs in CI environments to test supporting branches such as feature, release, and hotfix; before merging into the main one.

3. Configure developer workstations to scan local changes thanks to the pre-commit git hook and ggshield CLI. It prevents secrets from leaving developer workstations in the first place.

4. If you run your own self-hosted VCS instances, you can leverage a globally configured pre-receive git hook to block secrets from entering centralized repositories.
