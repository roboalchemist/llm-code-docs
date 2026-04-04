# Source: https://docs.replit.com/replitai/dynamic-intelligence.md

# Dynamic Intelligence

> Enhance Agent with Dynamic Intelligence—High Power mode for advanced AI capabilities. Get first-try correct results on complex builds when precision matters most.

export const YouTubeEmbed = ({videoId, title = "YouTube video", startAt}) => {
  if (!videoId) {
    return null;
  }
  let url = "https://www.youtube.com/embed/" + videoId;
  if (startAt) {
    url = url + "?start=" + startAt;
  }
  return <Frame>
      <iframe src={url} title={title} allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowFullScreen></iframe>
    </Frame>;
};

export const HighPowerCostMultiple = '5x';

export const TeamsHighPowerSoftAlert = '500';

export const ProHighPowerRequests = '100';

export const FreeHighPowerRequests = '3';

export const StandardModelOutputPrice = '$15';

export const StandardModelInputPrice = '$3';

export const AdvancedModelOutputPrice = '$75';

export const AdvancedModelInputPrice = '$15';

export const AgentCheckpointCost = '$0.25';

<Frame>
  <img src="https://mintcdn.com/replit/tUURBnDCn-Er8ghT/images/replitai/dynamic-intelligence-opus-4-5.png?fit=max&auto=format&n=tUURBnDCn-Er8ghT&q=85&s=31a39425943e90036038ca36436b35d2" alt="Agent tools showing High Power model with no extra cost until December 8" data-og-width="1182" width="1182" data-og-height="1404" height="1404" data-path="images/replitai/dynamic-intelligence-opus-4-5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/tUURBnDCn-Er8ghT/images/replitai/dynamic-intelligence-opus-4-5.png?w=280&fit=max&auto=format&n=tUURBnDCn-Er8ghT&q=85&s=94594ba08391096d66493df39ec53de4 280w, https://mintcdn.com/replit/tUURBnDCn-Er8ghT/images/replitai/dynamic-intelligence-opus-4-5.png?w=560&fit=max&auto=format&n=tUURBnDCn-Er8ghT&q=85&s=f8a528423fad036422c8a6eeb4eb2075 560w, https://mintcdn.com/replit/tUURBnDCn-Er8ghT/images/replitai/dynamic-intelligence-opus-4-5.png?w=840&fit=max&auto=format&n=tUURBnDCn-Er8ghT&q=85&s=628799e80ae17ed6e859ea89d0bd468d 840w, https://mintcdn.com/replit/tUURBnDCn-Er8ghT/images/replitai/dynamic-intelligence-opus-4-5.png?w=1100&fit=max&auto=format&n=tUURBnDCn-Er8ghT&q=85&s=d07867fc086b078c347464355db7f4c4 1100w, https://mintcdn.com/replit/tUURBnDCn-Er8ghT/images/replitai/dynamic-intelligence-opus-4-5.png?w=1650&fit=max&auto=format&n=tUURBnDCn-Er8ghT&q=85&s=0ed52d0f6ca6658a24d05147ad115593 1650w, https://mintcdn.com/replit/tUURBnDCn-Er8ghT/images/replitai/dynamic-intelligence-opus-4-5.png?w=2500&fit=max&auto=format&n=tUURBnDCn-Er8ghT&q=85&s=3799bbb9c88ffa51ae1c20efaa96b3ba 2500w" />
</Frame>

Dynamic Intelligence enhances Agent's reasoning capabilities through High Power <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/high-power.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=50de2faf7fd4ae77202602d8057d74a9" alt="High Power icon" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/high-power.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/high-power.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=bad43d8457268c5e26afd38f98249510 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/high-power.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=edf6986c697d797c36178860f2ad9a06 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/high-power.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=1cfd0914f8d9eaa2df99048c8f751cb9 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/high-power.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=d33fe8bc9a0ba261fab8ad54a418da3f 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/high-power.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=1b2496a6fa2234a019b1da29cf76aa39 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/high-power.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=0e9c7073932248103a2dc9996d226d71 2500w" /> mode that upgrades Agent to our most advanced AI model. This feature helps you get first-try correct results on complex builds.

<Note>
  **Free until December 8th**: From November 24 to December 8, 2025, High Power mode is available at no additional cost and is the default for both free and paid users. Experience our most advanced AI capabilities during this promotional period.
</Note>

<Info>
  Dynamic Intelligence is designed for builders who value quality over speed. High Power increases costs but delivers better results for complex tasks. This means that you'll get better results *and* it may take fewer turns to get there, though the cost of those turns will be higher.
</Info>

## What is Dynamic Intelligence?

Dynamic Intelligence enhances Agent's capabilities by upgrading to our most advanced AI model for maximum capability.

Use this feature to tackle demanding development tasks with higher accuracy and better outcomes.

<YouTubeEmbed videoId="K-vu88GHqEk" />

## High Power mode

High Power <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/high-power.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=50de2faf7fd4ae77202602d8057d74a9" alt="High Power icon" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/high-power.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/high-power.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=bad43d8457268c5e26afd38f98249510 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/high-power.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=edf6986c697d797c36178860f2ad9a06 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/high-power.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=1cfd0914f8d9eaa2df99048c8f751cb9 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/high-power.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=d33fe8bc9a0ba261fab8ad54a418da3f 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/high-power.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=1b2496a6fa2234a019b1da29cf76aa39 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/high-power.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=0e9c7073932248103a2dc9996d226d71 2500w" /> upgrades Agent to our most advanced AI model. This provides superior performance for complex reasoning, large context processing, and sophisticated problem-solving.

**Use High Power for:**

* **Maximum accuracy**: Critical business logic or security implementations
* **Large context processing**: Working with entire codebases or extensive documentation
* **Complex algorithms**: Multi-step processes or sophisticated data processing
* **Advanced integrations**: Complex API interactions or third-party service integrations

## How to use Dynamic Intelligence

1. Open Agent in your Replit App.
2. Locate the Dynamic Intelligence controls in the chat toolbar. <img class="icon-svg" src="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/agent-settings.svg?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=23a035924bb3c8c61e7ca996c76a90a1" alt="Agent settings icon" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/agent-settings.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/agent-settings.svg?w=280&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=08dd975be952b60db564bcfedfc6f7fd 280w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/agent-settings.svg?w=560&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=4c35dd49157af177d8e2ea495eb6fb51 560w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/agent-settings.svg?w=840&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=5d87fc1ea8d58c3105dadceb194b4edb 840w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/agent-settings.svg?w=1100&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=6d68bbc6b654bd433f2260669ddbf03b 1100w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/agent-settings.svg?w=1650&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=889488d8482ad86f6bdbe4194eb648ce 1650w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/agent-settings.svg?w=2500&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=ce1af7526c6290400507c309b091e5f4 2500w" />
3. Toggle <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/high-power.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=50de2faf7fd4ae77202602d8057d74a9" alt="High Power icon" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/high-power.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/high-power.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=bad43d8457268c5e26afd38f98249510 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/high-power.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=edf6986c697d797c36178860f2ad9a06 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/high-power.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=1cfd0914f8d9eaa2df99048c8f751cb9 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/high-power.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=d33fe8bc9a0ba261fab8ad54a418da3f 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/high-power.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=1b2496a6fa2234a019b1da29cf76aa39 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/high-power.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=0e9c7073932248103a2dc9996d226d71 2500w" /> **High Power** to upgrade to our most advanced AI model.
4. Send your prompt. The settings will apply to your next request.

### Cost transparency

Dynamic Intelligence provides clear cost information. Monitor your spending with detailed breakdowns per request, and view current token costs in the sidebar history.

**To manage costs effectively:**

* **Start selective**: Use Dynamic Intelligence for complex tasks where quality matters most
* **Monitor usage**: Check the usage icon to track spending on enhanced requests <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/usage-icon.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=afedaf18cbe1d4549be6e7833c88c269" alt="Usage cost icon" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/usage-icon.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/usage-icon.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=d5746213e15396325c7772f33084a4b5 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/usage-icon.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=31e3306f672210e2d9d4c1a0284be5fb 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/usage-icon.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=971452a359f72a20a7170f4c07bb6ea0 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/usage-icon.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=5e04ff80266d49ad695d29d09a05a106 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/usage-icon.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=cc48eb084ae86bff8f1a5beefdc0d332 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/usage-icon.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=4c7f0bfca699d607e695cc4439b52de1 2500w" />
* **Mix approaches**: Use standard Agent for simple tasks and Dynamic Intelligence for complex ones

## When to use Dynamic Intelligence

### Use High Power when you need:

* **Maximum accuracy**: Critical business logic or security implementations
* **Large context processing**: Working with entire codebases or extensive documentation
* **Complex problem solving**: Multi-step algorithms or sophisticated data processing
* **Advanced integrations**: Complex API interactions or third-party service integrations

### Use standard Agent for:

* Simple bug fixes and basic feature additions
* Straightforward UI changes and file organization tasks
* Quick modifications that don't require deep analysis

## Best practices

### Optimizing prompts for Dynamic Intelligence

* **Provide comprehensive context**: Upload related files, documentation, or examples
* **Describe constraints**: Mention performance requirements, compatibility needs, or business rules
* **Ask for analysis**: Request that Agent explain trade-offs and consider alternatives
* **Specify quality requirements**: Mention if you need production-ready, testable, or maintainable code

### Getting the most value

* **Start simple**: Try High Power on a moderately complex task to see the difference
* **Compare results**: Use both standard and Dynamic Intelligence modes on similar tasks to understand the value
* **Monitor usage patterns**: Track when you use this feature to optimize your workflow
* **Scale gradually**: Once comfortable, apply Dynamic Intelligence to your most challenging builds

## Next steps

Ready to enhance your development workflow with Dynamic Intelligence? Start by enabling this feature for your next complex build and experience the difference in quality and accuracy.

**Learn about other Agent features:**

* Explore [Web Search](/replitai/web-search) to access current information and latest documentation
* See [Advanced AI features](/tutorials/advanced-ai-features) for strategies on combining Dynamic Intelligence with Web Search

**For more information about pricing:**

* [Agent billing](/billing/ai-billing#agent-billing) and [managing spend](/billing/managing-spend)
