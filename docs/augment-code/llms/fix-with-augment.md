# Source: https://docs.augmentcode.com/codereview/fix-with-augment.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Fix in Augment

> Automatically address issues found during code review directly using the agent in your IDE or paste the details into your preferred environment to address it yourself.

When Augment Code Review identifies issues in your pull request, you can use the "Fix in Augment" button inside the comment to automatically address the issue.

<img src="https://mintcdn.com/augment-mtje7p526w/NsS6pjzbr2jAhbIL/images/codereview-fixwithaugment-inline.png?fit=max&auto=format&n=NsS6pjzbr2jAhbIL&q=85&s=979f17210ac453068daa2332e60ed8dd" alt="Fix in Augment button" data-og-width="1570" width="1570" data-og-height="554" height="554" data-path="images/codereview-fixwithaugment-inline.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/NsS6pjzbr2jAhbIL/images/codereview-fixwithaugment-inline.png?w=280&fit=max&auto=format&n=NsS6pjzbr2jAhbIL&q=85&s=91f668b1a9f22725f7a32868c5b849ac 280w, https://mintcdn.com/augment-mtje7p526w/NsS6pjzbr2jAhbIL/images/codereview-fixwithaugment-inline.png?w=560&fit=max&auto=format&n=NsS6pjzbr2jAhbIL&q=85&s=e178ccaed840ecf48db751205b31463e 560w, https://mintcdn.com/augment-mtje7p526w/NsS6pjzbr2jAhbIL/images/codereview-fixwithaugment-inline.png?w=840&fit=max&auto=format&n=NsS6pjzbr2jAhbIL&q=85&s=4450646c7ab27be059697280a170824a 840w, https://mintcdn.com/augment-mtje7p526w/NsS6pjzbr2jAhbIL/images/codereview-fixwithaugment-inline.png?w=1100&fit=max&auto=format&n=NsS6pjzbr2jAhbIL&q=85&s=9524360c3daee87cbc2990ffd9fedce0 1100w, https://mintcdn.com/augment-mtje7p526w/NsS6pjzbr2jAhbIL/images/codereview-fixwithaugment-inline.png?w=1650&fit=max&auto=format&n=NsS6pjzbr2jAhbIL&q=85&s=0fd5516a322baad996d62e2e1ce7233b 1650w, https://mintcdn.com/augment-mtje7p526w/NsS6pjzbr2jAhbIL/images/codereview-fixwithaugment-inline.png?w=2500&fit=max&auto=format&n=NsS6pjzbr2jAhbIL&q=85&s=be985ffd7412fe5f97f4ef00c91850f6 2500w" />

Options include:

* **Open in Agent Session**: For VS Code only, allows you to copy the prompt and start a new thread inside the Augment Code extension
* **Copy to Clipboard**: Allows you to paste the prompt into your preferred environment, e.g. Auggie CLI, Augment Code for JetBrains, etc.

<img src="https://mintcdn.com/augment-mtje7p526w/NsS6pjzbr2jAhbIL/images/codereview-fixwithaugment.png?fit=max&auto=format&n=NsS6pjzbr2jAhbIL&q=85&s=bf9f109456c5843cdbbd60d0ac699de5" alt="Fix in Augment options" data-og-width="817" width="817" data-og-height="616" height="616" data-path="images/codereview-fixwithaugment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/NsS6pjzbr2jAhbIL/images/codereview-fixwithaugment.png?w=280&fit=max&auto=format&n=NsS6pjzbr2jAhbIL&q=85&s=88eb4b484801992db97f770568e67f8b 280w, https://mintcdn.com/augment-mtje7p526w/NsS6pjzbr2jAhbIL/images/codereview-fixwithaugment.png?w=560&fit=max&auto=format&n=NsS6pjzbr2jAhbIL&q=85&s=bf7debc22a1bcf575cb9624e61c8f4dc 560w, https://mintcdn.com/augment-mtje7p526w/NsS6pjzbr2jAhbIL/images/codereview-fixwithaugment.png?w=840&fit=max&auto=format&n=NsS6pjzbr2jAhbIL&q=85&s=9b2e3fffbc70208b1a059730500208aa 840w, https://mintcdn.com/augment-mtje7p526w/NsS6pjzbr2jAhbIL/images/codereview-fixwithaugment.png?w=1100&fit=max&auto=format&n=NsS6pjzbr2jAhbIL&q=85&s=ee81e06468c5c7f7622547e39605457e 1100w, https://mintcdn.com/augment-mtje7p526w/NsS6pjzbr2jAhbIL/images/codereview-fixwithaugment.png?w=1650&fit=max&auto=format&n=NsS6pjzbr2jAhbIL&q=85&s=de84ddd1e76ebe3eab42368076aafe41 1650w, https://mintcdn.com/augment-mtje7p526w/NsS6pjzbr2jAhbIL/images/codereview-fixwithaugment.png?w=2500&fit=max&auto=format&n=NsS6pjzbr2jAhbIL&q=85&s=46f72497d83fa42297b001455e201b08 2500w" />

***

## Best Practices

**Review the Fix**: Always review the changes proposed by Agent before accepting them. While Agent has full context, you should verify the fix aligns with your intent.

**Test the Changes**: Run your tests after applying the fix to ensure the issue is resolved and no new issues are introduced.

**Update the PR**: After pushing your fix, you can reply to the Code Review comment to indicate you've addressed the issue.

**Request Follow-up Review**: If you make significant changes, consider requesting another review by commenting `auggie review` on your PR.
