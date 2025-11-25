# Source: https://docs.replit.com/tutorials/advanced-ai-features.md

# Advanced AI features

> Learn when and how to use Dynamic Intelligence (High Power) and Web Search to maximize Agent's capabilities for complex builds and accessing current information.

export const AuthorCard = ({img = "https://replit.com/cdn-cgi/image/width=256,quality=80,format=auto/https://storage.googleapis.com/replit/images/1730840970400_e885f16578bbbb227adbfeb7b979be34.jpeg", href = "https://youtube.com/@mattpalmer", name = "Matt Palmer", role = "Head of Developer Relations"}) => {
  return <a href={href} target="_blank" className="card block not-prose font-normal group relative my-2 ring-2 ring-transparent rounded-xl bg-white/50 dark:bg-codeblock/50 border border-gray-100 shadow-md dark:shadow-none shadow-gray-300/10 dark:border-gray-800/50 overflow-hidden cursor-pointer hover:!border-primary dark:hover:!border-primary-light">
      <div className="flex items-center gap-2 p-4">
        <div className="flex-shrink-0">
          <img src={img} alt={name} className="w-12 h-12 rounded-full object-cover" />
        </div>
        <div className="flex-grow">
          <h3 className="text-base font-semibold mb-0.5 text-inherit">{name}</h3>
          <p className="text-sm text-gray-600 dark:text-gray-400 m-0">{role}</p>
        </div>
      </div>
    </a>;
};

export const AiPrompt = ({children}) => {
  return <CodeBlock className="relative block font-sans whitespace-pre-wrap break-words">
      <div className="pr-7">
        {children}
      </div>
    </CodeBlock>;
};

export const HighPowerCostMultiple = '5x';

export const AdvancedModelOutputPrice = '$75';

export const AdvancedModelInputPrice = '$15';

export const AgentCheckpointCost = '$0.25';

<AuthorCard />

Agent has two advanced features that can significantly improve your development workflow: High Power mode (part of Dynamic Intelligence) and Web Search. While High Power upgrades Agent's AI model for complex tasks, Web Search lets Agent access current information from the internet. Use them independently or together for the best results.

Here's how to use them strategically while managing costs.

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/replit/images/replitai/advanced-features.png" alt="Agent performing web search to gather current information for app development" />
</Frame>

## What each feature does

**High Power mode** - Upgrades Agent to our most advanced AI model for maximum capability through Dynamic Intelligence.

**Web Search** lets Agent access current information from the internet, overcoming knowledge cutoffs.

## When to use what

| Feature             | Perfect for                                                  | Skip for                        | Cost                             |
| :------------------ | :----------------------------------------------------------- | :------------------------------ | :------------------------------- |
| **High Power mode** | Large codebases, critical business logic, complex algorithms | Basic features, quick fixes     | {HighPowerCostMultiple} the cost |
| **Web Search**      | Latest packages, current docs, real-time data                | Well-known tech, static content | Standard pricing                 |

## High Power mode

High Power upgrades Agent to our most advanced AI model. It costs about 5× more but handles complex tasks that standard Agent might struggle with.

**Reserve it for:**

* Analyzing large codebases (500+ files)
* Building complex recommendation engines
* Financial or healthcare apps requiring high accuracy
* Advanced data processing pipelines

The extra cost is usually worth it when precision matters more than speed.

## Web Search

Web Search lets Agent research current information while helping you build. It's particularly valuable for discovering the latest tools and best practices.

**Use it when you need:**

* The newest React animation libraries
* Current API documentation
* Latest security best practices
* Real-time market data for your app

**Example:**

<AiPrompt>
  Research the best animation libraries for smooth transitions. Implement the most practical one into my application.
</AiPrompt>

## Combining features

The real power comes from using these features together. For complex projects, try combining both:

<AiPrompt>
  Help me build an app that pixelates images and allows exporting them to vector graphics. Do research on the best libraries for image canvas manipulation, vectorization, and exporting. Create the app in a scalable, maintainable way.
</AiPrompt>

*Enable: High Power + Web Search*

This gives you:

1. **Web Search** finds the best current libraries
2. **High Power** ensures accurate implementation and solid architecture

## Smart cost management

* **Plan first**: Agent's initial planning is free, so review the approach before implementing
* **Be selective**: Use Web Search for research, High Power for critical tasks
* **Test and learn**: Try different combinations to see what works for your workflow
* **Monitor value**: Compare results with and without features

## Common scenarios

**Building an MVP?**
Web Search gives you current best practices with solid architecture.

**Modernizing legacy code?**\
High Power can analyze large codebases and plan migrations effectively.

**Learning new tech?**
Web Search finds current tutorials and helps you understand concepts.

**Mission-critical system?**
Use both features for research and maximum accuracy.

## Getting started

1. **Pick a moderately complex task** in your current project
2. **Try High Power** on something that stumped standard Agent
3. **Use Web Search** when you need current information
4. **Experiment with combinations** as you get comfortable

Start small, measure the value, and gradually use these features for your most challenging builds.

## Learn more

* [Dynamic Intelligence](/replitai/dynamic-intelligence) - Complete guide to High Power
* [Web Search](/replitai/web-search) - Full documentation on Web Search capabilities
* [Agent billing](/billing/ai-billing#agent-billing) - Pricing and cost management
