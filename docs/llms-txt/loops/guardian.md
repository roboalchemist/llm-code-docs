# Source: https://loops.so/docs/creating-emails/guardian.md

> ## Documentation Index
> Fetch the complete documentation index at: https://loops.so/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Guardian

> Sending emails protected by Guardian

Guardian checks your emails in real time and flags issues *before* you hit send. It catches misconfigured or missing elements in campaigns, loops, and transactional emails so you ship with confidence.

<img src="https://mintcdn.com/loops/zdY_6OBc_NXTb9Vu/images/guardian.png?fit=max&auto=format&n=zdY_6OBc_NXTb9Vu&q=85&s=d792baa1a0372f7100cc28b6b3e5f9b5" alt="Guardian" data-og-width="2280" width="2280" data-og-height="1700" height="1700" data-path="images/guardian.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/zdY_6OBc_NXTb9Vu/images/guardian.png?w=280&fit=max&auto=format&n=zdY_6OBc_NXTb9Vu&q=85&s=0e28529ab260f53f575d571900b5fb36 280w, https://mintcdn.com/loops/zdY_6OBc_NXTb9Vu/images/guardian.png?w=560&fit=max&auto=format&n=zdY_6OBc_NXTb9Vu&q=85&s=824b277dc349d34658e8620882fee684 560w, https://mintcdn.com/loops/zdY_6OBc_NXTb9Vu/images/guardian.png?w=840&fit=max&auto=format&n=zdY_6OBc_NXTb9Vu&q=85&s=7c6063003bc13396de69579e928a0655 840w, https://mintcdn.com/loops/zdY_6OBc_NXTb9Vu/images/guardian.png?w=1100&fit=max&auto=format&n=zdY_6OBc_NXTb9Vu&q=85&s=a91b78e65b80dd5a74f718b596122152 1100w, https://mintcdn.com/loops/zdY_6OBc_NXTb9Vu/images/guardian.png?w=1650&fit=max&auto=format&n=zdY_6OBc_NXTb9Vu&q=85&s=22241d06e8ef881fff97546b3e0986e3 1650w, https://mintcdn.com/loops/zdY_6OBc_NXTb9Vu/images/guardian.png?w=2500&fit=max&auto=format&n=zdY_6OBc_NXTb9Vu&q=85&s=70f62c448cc1af1646fd66c1aa064151 2500w" />

## Guardian checks

### Misplaced variables

Occasionally, content will be copied between email types (campaign \<> loops \<> transactional) and certain types of dynamic content may not be supported. Instead of stripping the variables or blocking the paste, Guardian flags the errors so you can make sure the content is adjusted and formatted properly for the email type.

## Save states

We transparently poll for the last saved checkpoint and keep you updated. This is especially helpful in poor network conditions such as hotspots on the go or on a plane. If local changes fall out of sync we'll let you know.

## Missing button links

If you add a button, we assume you would like a link (href) attached. Now we'll flag that for you to block any accidental sends.

## Missing fallback variables

When using contact and event properties in campaigns and loops, emails will not be sent if the values are missing from the contact or event.

For example, if you have inserted "Hello `First Name`" in your email, and the contact doesn't have a first name value, the loop or campaign email will not be sent. In some cases, that can be desired behavior but we've found most of the time a fallback should be added. We've added it as a warning and now Guardian will alert you when there are missing fallbacks and emails will send as expected.

<CardGroup cols={2}>
  <Card title="Fallback values" icon="crystal-ball" href="/creating-emails/personalizing-emails#fallback-values">
    Learn about using fallback values for your dynamic content.
  </Card>
</CardGroup>

## Future improvements

* Content checks
* Boosted spellcheck
* Adhering to design/brand guidelines

<Info>
  Should we add something else? Send [chris@loops.so](mailto:chris@loops.so) an email and let him know :)
</Info>
