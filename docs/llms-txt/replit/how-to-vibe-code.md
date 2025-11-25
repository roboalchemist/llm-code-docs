# Source: https://docs.replit.com/tutorials/how-to-vibe-code.md

# How to vibe code effectively

> Learn essential skills to effectively guide AI tools like Replit Agent and Assistant, turning your ideas into functional applications faster.

export const AgentModelV2 = 'Latest AI Model';

export const AgentModelV1 = 'Advanced AI Model';

export const TeamsCredits = '$40';

export const CoreCredits = '$25';

export const AssistantCheckpointCost = '$0.05';

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

<AuthorCard />

## How to think about vibe coding

AI tools like Replit Agent and Assistant are incredibly powerful, capable of generating code, configuring environments, and even building entire applications.

However, they work best when guided effectively. "Vibe coding" is about developing the intuition and skills to steer these AI partners efficiently.

Think about yourself like a manager, or rather, a *leader* your job is to guide your "team" to success—that's done by providing direction, resources, and feedback.

Replit is your team, and you're the leader.

<Frame>
  <iframe src="https://www.youtube.com/embed/2ctPkWNM2Ak" title="5 Skills for Vibe Coding" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />
</Frame>

Without vibe coding skills, you might find yourself:

* Stuck in unproductive loops with the AI.
* Building features that don't quite meet your vision.
* Unsure how to debug when things inevitably break.
* Overwhelmed by the possibilities and unsure where to start.

Mastering these five skills helps you provide the right guidance at the right time, enabling you to leverage AI to go from idea to app, fast.

## What is Vibe Coding?

Vibe coding is a practical approach to prompt engineering focused on application development. It involves a blend of technical understanding, clear communication, and iterative refinement.

It's less about knowing every programming language feature and more about understanding how to break down problems, ask the right questions, and guide an AI collaborator.

<Frame>
  <iframe src="https://www.youtube.com/embed/5OWurmg41tI" title="What is Vibe Coding?" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />
</Frame>

The five key skills are:

1. **Procedural Thinking**: Planning your app like a product manager and engineer combined.
2. **Leveraging Frameworks**: Knowing which tools to use and asking the AI for help.
3. **Building in Checkpoints**: Making incremental progress and using AI snapshots.
4. **Debugging Methodically**: Systematically finding and fixing errors with AI assistance.
5. **Mastering Context**: Giving the AI the right information (and only the right information).

## The Skills

Let's break down each skill with practical steps you can apply when building with Replit Agent or Assistant.

See our guide on [Effective Prompting](/tutorials/effective-prompting) for detailed tips and examples.

### Think Procedurally

<Frame>
  <img src="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/procedural_thinking.png?fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=9feb2941a6941d1b81bafc518a240407" alt="Procedural Thinking" style={{backgroundColor: 'white'}} data-og-width="955" width="955" data-og-height="499" height="499" data-path="images/tutorials/procedural_thinking.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/procedural_thinking.png?w=280&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=dd374e3540e5dde685005257f4bc5e37 280w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/procedural_thinking.png?w=560&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=8274cf2e8aeda8ed4d02aeeb880dbe04 560w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/procedural_thinking.png?w=840&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=2629810d8590a2cc24efad5b492a052a 840w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/procedural_thinking.png?w=1100&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=680f25b3aae0e57373142148c663776a 1100w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/procedural_thinking.png?w=1650&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=7bf2f9c6851b5344342d038b706b9c0b 1650w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/procedural_thinking.png?w=2500&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=43bccd28ded8743f69ed37a4e8c3d9b7 2500w" />
</Frame>

Before writing a single prompt, think through the entire application. This goes beyond basic logical thinking (like knowing the rules of chess) or even computational thinking (like programming a computer to enforce those rules).

Procedural thinking is about understanding how to *excel*—like programming an AI to play chess competitively. It means deeply understanding the problem space, the desired outcome, and the steps to get there.

* **Define the problem space**: What core problem does the app solve? What makes a *successful* app in this context?
* **Plan the MVP**: What are the absolute essential features for the first version? Start small.
* **Break it down**: Define the high-level goals, then break them into smaller, actionable steps or features. Think like both a product manager (defining requirements) and an engineer (planning implementation).
* **Anticipate edge cases**: What could go wrong? How should the app handle unexpected inputs or situations?
* **Consider the User Experience**: What makes a *good* app for this purpose? What data needs to be stored? How should users interact with it?
* **Example**: If building a tip-splitting app, don't just ask for "a tip splitter." Specify how users add friends, input the bill amount, handle taxes/discounts, and share the results. Procedural thinking defines these requirements clearly for the AI.

This might involve drawing a wireframe, writing a doc about the requirements of the app, or even just a list of features.

Use the screenshot from your wireframe to help Agent understand the app. Here's a sample screenshot and prompt from a question asking app.

<Frame>
  <img src="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/question_asking_app.png?fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=42ba1de606098f198d3cf3e4e1d9b407" alt="Question Asking App" data-og-width="1986" width="1986" data-og-height="1070" height="1070" data-path="images/tutorials/question_asking_app.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/question_asking_app.png?w=280&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=825e928f8564bedadbb0b3da0598545f 280w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/question_asking_app.png?w=560&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=e77463bd2da331eef04f264c58c37df7 560w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/question_asking_app.png?w=840&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=10b311d568a64248fdef3d7b7010d849 840w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/question_asking_app.png?w=1100&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=1d10c7f599c61989f9d734ab7aa9f380 1100w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/question_asking_app.png?w=1650&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=fe0fa5f9c625f5d8b3f2e46cec3d953c 1650w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/question_asking_app.png?w=2500&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=d79160963a68d5ddac5844dfcfe718d4 2500w" />
</Frame>

### Leverage Frameworks

You don't need to build everything from scratch, and often, you shouldn't. Countless frameworks and libraries exist to solve common problems (UI components, animations, data handling, etc.).

* **Ask the AI**: You don't know what you don't know. Ask Agent or Assistant: "What are good options for building a user interface with drag-and-drop features?" or "What's the best way to handle user authentication?"
* **Check Compatibility**: Newer frameworks might not be in the AI's training data. Ask the AI about compatibility or provide documentation links directly in your prompt. Replit Agent and Assistant can often scrape web content for context.
* **Provide Specifics**: If you find a relevant library or code snippet, include it in your prompt. Giving the AI concrete examples of *how* to use a framework is highly effective.

<Info>
  LLMs have training data cutoffs. Very recent frameworks might require you to provide documentation or examples as context for best results.
</Info>

### Build in Checkpoints

AI doesn't always get it right on the first try. Building large features in one go increases the risk of complex errors. Work incrementally.

* **Define Small Goals**: Prompt the AI to build one small piece of functionality at a time.
* **Test Each Step**: After the AI completes a task, run the code. Does it work as expected?
* **Use Checkpoints**: Replit Agent automatically creates **Checkpoints** that capture your complete development state—workspace contents, AI conversation context, and connected databases. If something breaks, don't keep prompting with the same request. Select **Rollback to here** on a previous checkpoint and try a different approach or prompt.
* **Version Control Principles**: Think of Checkpoints like comprehensive commits that preserve your entire development environment. They provide safe points to return to if you go down the wrong path.

<Frame>
  <iframe src="https://www.youtube.com/embed/iLOxO1FBZls" title="Checkpoints" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />
</Frame>

<Note>
  Using **Rollback** allows you to explore different implementation paths without losing progress on what already works. Rollbacks restore your entire development environment, including workspace contents and AI conversation context. Connected databases can also be restored when you select "Restore databases" under "Additional rollback options."
</Note>

<Info>
  Learn more about comprehensive checkpoint and rollback capabilities in [Checkpoints and Rollbacks](/replitai/checkpoints-and-rollbacks).
</Info>

### Debug Methodically

<Frame>
  <img src="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/debugging.png?fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=2623e4938023f35d1143cd7792aa18a9" alt="Debug Methodically" data-og-width="776" width="776" data-og-height="1012" height="1012" data-path="images/tutorials/debugging.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/debugging.png?w=280&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=87e03366a11b061da613a49b8812e8a2 280w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/debugging.png?w=560&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=272f7b3a418adb6df986fd7a4850e5f8 560w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/debugging.png?w=840&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=ff11b5c1392b6cb4306e27a3e0e2a5d8 840w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/debugging.png?w=1100&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=645549fc3f0056893cb8ea6afd8e60ed 1100w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/debugging.png?w=1650&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=468f78c59586ce3eea9363e3df969b34 1650w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/debugging.png?w=2500&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=b4c9fb117576ebe7fb8258d5a401b6f2 2500w" />
</Frame>

Errors are inevitable. Instead of just pasting the error message back to the AI, approach debugging systematically.

* **Understand the Error**: Read the error message carefully. Where did it occur (`Console`, browser, specific file)? What does it say?
* **Gather Clues**: Look at the code around the error. Check the `Console` for logs. Use the AI Assistant to explain parts of the code you don't understand.
* **Isolate the Problem**: Try to reproduce the error reliably. What specific action triggers it?
* **Provide Contextual Clues**: When asking the AI for help, provide:
  * The exact error message.
  * The relevant code snippet(s).
  * What you were trying to do.
  * What you've already tried.
* **Turn it into a Game**: Think of debugging as solving a puzzle. Each clue gets you closer to the solution.

### Master Context

The information (context) you provide the AI dramatically influences the quality of its response. More context isn't always better; *relevant* context is key.

* **Be Selective**: Include only information directly relevant to the current task. Exclude unrelated code, files, or previous instructions if they aren't needed. Think about the AI's limited attention span (context window).
* **Use Multimodal Inputs**: Provide code snippets, file attachments, error messages, URLs for documentation, or even screenshots if they help clarify the request.
* **Structure Prompts Clearly**: State the goal first, then provide supporting context.
* **Start Fresh for New Features**: When starting a significantly new feature, consider using **New chat** in Agent or Assistant to ensure the AI isn't confused by previous, unrelated context.

<Tip>
  Imagine explaining a task to a human expert. You wouldn't start by telling them your life story if you just need help fixing a specific bug. Give the AI the focused information it needs.
</Tip>

## Putting It All Together: The Vibe Coding Loop

Mastering these skills enables an effective iterative loop for building with AI:

<Frame>
  <img src="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/feedback_loop.png?fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=c619ea3a70d9ffceccd501fc6880b0ad" alt="Vibe Coding Loop" data-og-width="1796" width="1796" data-og-height="1546" height="1546" data-path="images/tutorials/feedback_loop.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/feedback_loop.png?w=280&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=a755fb3f1629e0c189b86c1221b31208 280w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/feedback_loop.png?w=560&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=60b998c850fee0978a92cddc68cbf92b 560w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/feedback_loop.png?w=840&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=b9ecd28eac15242b34ad062e781bb641 840w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/feedback_loop.png?w=1100&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=7fc25ab6e6a66d0491b7b98a697f801e 1100w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/feedback_loop.png?w=1650&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=310dc93387b74a348aa2e39430f386d3 1650w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/feedback_loop.png?w=2500&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=fcbb5027943e4da4237f15e06c4c5530 2500w" />
</Frame>

1. **Think**: Define the next small feature or fix (Procedural Thinking).
2. **Prompt**: Clearly ask the AI, providing relevant frameworks and context (Leveraging Frameworks, Mastering Context).
3. **Test**: Run the code. Does it work?
4. **Error?**:
   * **Yes**: Debug systematically, gather clues, and prompt the AI again with specific details. If stuck, consider rolling back to a previous **Checkpoint** and trying a different approach (Debugging Methodically, Building in Checkpoints).
   * **No**: Success! Save a **Checkpoint** (Building in Checkpoints).
5. **Repeat**: Move on to the next feature or refinement.

This loop turns AI from a magic black box into a powerful, steerable collaborator.

## What you've learned

Developing these skills transforms how you build software with AI:

* **Build Faster**: Go from idea to functional app more quickly and efficiently.
* **Overcome Roadblocks**: Systematically navigate errors and AI limitations.
* **Tackle Complexity**: Build more sophisticated applications by breaking them down effectively.
* **Improve Clarity**: Enhance your own understanding of the project by thinking procedurally.
* **Unlock Creativity**: Spend less time fighting the tools and more time bringing your vision to life.

<Note>
  Vibe coding isn't just about interacting with AI; it enhances your fundamental skills in problem-solving, planning, and critical thinking.
</Note>

## Next Steps: Practice Your Skills

The best way to improve is by building!

<AccordionGroup>
  <Accordion title="Try Building a Project">
    * Start a new project using [Replit Agent](https://replit.com/ai/agent) with a simple idea.
    * Practice breaking the idea down (Procedural Thinking).
    * Use Agent or Assistant to build it step-by-step, focusing on clear prompts and context (Mastering Context, Leveraging Frameworks).
    * Utilize **Checkpoints** frequently (Building in Checkpoints).
    * When errors occur, practice systematic debugging (Debugging Methodically).
  </Accordion>

  <Accordion title="Explore Replit AI Documentation">
    * Learn more about [Replit Agent](/replitai/agent) features like Checkpoints and Rollback.
    * Discover tips for writing effective prompts for Replit Assistant. (Link to Assistant docs when available)
  </Accordion>
</AccordionGroup>

Vibe coding is an evolving practice. By focusing on these core skills, you'll be well-equipped to navigate the exciting landscape of AI-assisted development and build amazing applications on Replit.
