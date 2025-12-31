# Source: https://docs.crewai.com/en/observability/neatlogs.md

# Neatlogs Integration

> Understand, debug, and share your CrewAI agent runs

# Introduction

Neatlogs helps you **see what your agent did**, **why**, and **share it**.

It captures every step: thoughts, tool calls, responses, evaluations. No raw logs. Just clear, structured traces. Great for debugging and collaboration.

## Why use Neatlogs?

CrewAI agents use multiple tools and reasoning steps. When something goes wrong, you need context — not just errors.

Neatlogs lets you:

* Follow the full decision path
* Add feedback directly on steps
* Chat with the trace using AI assistant
* Share runs publicly for feedback
* Turn insights into tasks

All in one place.

Manage your traces effortlessly

<img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/neatlogs-1.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=d01a5ce64066c6c7387b238068e71369" alt="Traces" data-og-width="1999" width="1999" data-og-height="763" height="763" data-path="images/neatlogs-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/neatlogs-1.png?w=280&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=ee62fda86fa566c25c133bcab4749395 280w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/neatlogs-1.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=5cb6eaca0429f7e70bb5c8d98a489a97 560w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/neatlogs-1.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=cb664845151f8e54c0e0b9fba753f383 840w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/neatlogs-1.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=fb471833d13ba8718ebd37cc6f557697 1100w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/neatlogs-1.png?w=1650&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=e470693ab78a2cce5b34570b328c6939 1650w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/neatlogs-1.png?w=2500&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=2211c7cdbf87f4e96de3aa5a51927b1d 2500w" />
<img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/neatlogs-2.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=5b737699468781be25098c33040d2125" alt="Trace Response" data-og-width="1999" width="1999" data-og-height="1128" height="1128" data-path="images/neatlogs-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/neatlogs-2.png?w=280&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=020336c536f38ce54dfc04854acac7d4 280w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/neatlogs-2.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=8a40138ff848d453607b8e4cf6d0af31 560w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/neatlogs-2.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=411d496952511260f03dcf703cf40402 840w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/neatlogs-2.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=ce7a99a7d6752ae77706cde411104694 1100w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/neatlogs-2.png?w=1650&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=e943a0308341c59d6b4d17e29e17126c 1650w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/neatlogs-2.png?w=2500&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=61b95cdb68c4c5cbdd349e802db3f2cb 2500w" />

The best UX to view a CrewAI trace. Post comments anywhere you want. Use AI to debug.

<img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/neatlogs-3.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=43cda9bcd83376dda4523ff0596b2043" alt="Trace Details" data-og-width="1999" width="1999" data-og-height="1125" height="1125" data-path="images/neatlogs-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/neatlogs-3.png?w=280&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=b412fc1111d110fba24398449f86c8a6 280w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/neatlogs-3.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=bc9a8210c617335893a0b9e94b9dcede 560w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/neatlogs-3.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=bca4c7758110744a457e3e635ba86e1c 840w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/neatlogs-3.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=c259898ac4cbe4835a0df33f161c7840 1100w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/neatlogs-3.png?w=1650&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=74f03053e7cc5b98b3e568417de3a319 1650w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/neatlogs-3.png?w=2500&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=b90e2b8fcadb097c82a60e6522533386 2500w" />
<img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/neatlogs-4.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=c9e7ad0653cae7bfaad2dd448d90eda0" alt="Ai Chat Bot With A Trace" data-og-width="1999" width="1999" data-og-height="751" height="751" data-path="images/neatlogs-4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/neatlogs-4.png?w=280&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=eb0debf5272db5db3729d8b4b4634d94 280w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/neatlogs-4.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=9ebccf5654ad590f1d231118b4a29037 560w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/neatlogs-4.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=a7987df251bd7085c86535c31c3bc8fe 840w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/neatlogs-4.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=113e589438936a55df794a60faec5ff7 1100w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/neatlogs-4.png?w=1650&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=469f0ab2f09cdd65c18e925ebd88be11 1650w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/neatlogs-4.png?w=2500&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=55115f959b3f2e49231e9ed273e6d11c 2500w" />
<img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/neatlogs-5.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=a977655abb8cd26d9ed4cef5fdd7d859" alt="Comments Drawer" data-og-width="1999" width="1999" data-og-height="1388" height="1388" data-path="images/neatlogs-5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/neatlogs-5.png?w=280&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=51ad567b077e31082ed8f2a1c53be446 280w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/neatlogs-5.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=b4c663fe1527dc74a13e8c7a7ae955d2 560w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/neatlogs-5.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=fdddfe615d4098db90f694707d70ec87 840w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/neatlogs-5.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=15cefd5838432e622844dced45f2f6b6 1100w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/neatlogs-5.png?w=1650&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=18b726e6b4bf38ee419f2a50be1e748a 1650w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/neatlogs-5.png?w=2500&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=52fcf26f16e0d4177dbcb9c0da5d1bb9 2500w" />

## Core Features

* **Trace Viewer**: Track thoughts, tools, and decisions in sequence
* **Inline Comments**: Tag teammates on any trace step
* **Feedback & Evaluation**: Mark outputs as correct or incorrect
* **Error Highlighting**: Automatic flagging of API/tool failures
* **Task Conversion**: Convert comments into assigned tasks
* **Ask the Trace (AI)**: Chat with your trace using Neatlogs AI bot
* **Public Sharing**: Publish trace links to your community

## Quick Setup with CrewAI

<Steps>
  <Step title="Sign Up & Get API Key">
    Visit [neatlogs.com](https://neatlogs.com/?utm_source=crewAI-docs), create a project, copy the API key.
  </Step>

  <Step title="Install SDK">
    ```bash  theme={null}
    pip install neatlogs
    ```

    (Latest version 0.8.0, Python 3.8+; MIT license)
  </Step>

  <Step title="Initialize Neatlogs">
    Before starting Crew agents, add:

    ```python  theme={null}
    import neatlogs
    neatlogs.init("YOUR_PROJECT_API_KEY")
    ```

    Agents run as usual. Neatlogs captures everything automatically.
  </Step>
</Steps>

## Under the Hood

According to GitHub, Neatlogs:

* Captures thoughts, tool calls, responses, errors, and token stats
* Supports AI-powered task generation and robust evaluation workflows

All with just two lines of code.

## Watch It Work

### 🔍 Full Demo (4 min)

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/8KDme9T2I7Q?si=b8oHteaBwFNs_Duk" title="NeatLogs overview" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

### ⚙️ CrewAI Integration (30 s)

<iframe className="w-full aspect-video rounded-xl" src="https://www.loom.com/embed/9c78b552af43452bb3e4783cb8d91230?sid=e9d7d370-a91a-49b0-809e-2f375d9e801d" title="Loom video player" frameBorder="0" allowFullScreen />

## Links & Support

* 📘 [Neatlogs Docs](https://docs.neatlogs.com/)
* 🔐 [Dashboard & API Key](https://app.neatlogs.com/)
* 🐦 [Follow on Twitter](https://twitter.com/neatlogs)
* 📧 Contact: [hello@neatlogs.com](mailto:hello@neatlogs.com)
* 🛠 [GitHub SDK](https://github.com/NeatLogs/neatlogs)

## TL;DR

With just:

```bash  theme={null}
pip install neatlogs

import neatlogs
neatlogs.init("YOUR_API_KEY")

You can now capture, understand, share, and act on your CrewAI agent runs in seconds.
No setup overhead. Full trace transparency. Full team collaboration.
```
