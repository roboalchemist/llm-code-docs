# Source: https://www.traceloop.com/docs/evaluators/custom-evaluator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom Evaluators

> Define an evaluator for your specific needs 

Create your own evaluator to match your specific needs. You can start right away with custom criteria for full flexibility, or use one of our recommended formats as a starting point.

<Frame>
  <img className="block dark:hidden" src="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-custom-light.png?fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=875e3060f650ac2058742288d3b27e6b" data-og-width="2376" width="2376" data-og-height="1386" height="1386" data-path="img/evaluator/eval-custom-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-custom-light.png?w=280&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=46090a7c162198e95eedba1069a737a9 280w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-custom-light.png?w=560&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=4e724aaebbf402b3d4fddc0c0f5af7f8 560w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-custom-light.png?w=840&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=23a9193a3a12b71db60670ac5c41c50d 840w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-custom-light.png?w=1100&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=77c1bee4cfc3a5d79b0820078a47d118 1100w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-custom-light.png?w=1650&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=62a3082c072511bc4386e295325c0fc7 1650w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-custom-light.png?w=2500&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=fb22928102050d38984b1b6d193692fe 2500w" />

  <img className="hidden dark:block" src="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-custom-dark.png?fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=d272ae37ea8e3a2a7d9e057700fac28d" data-og-width="2378" width="2378" data-og-height="1388" height="1388" data-path="img/evaluator/eval-custom-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-custom-dark.png?w=280&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=cce8b473e983b6f5648f5ad7e028437f 280w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-custom-dark.png?w=560&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=bc8f1475d3199e7ddc3afc48711659d3 560w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-custom-dark.png?w=840&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=445f31e8076a38eb936011ebf96d3a1d 840w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-custom-dark.png?w=1100&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=c54626e6a201e59b9abe9cecfff9cfd6 1100w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-custom-dark.png?w=1650&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=321db37b71c27f1cc2c09d2bf4e2259c 1650w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-custom-dark.png?w=2500&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=e7b0312cc6d16dbcb7dc0fd41c226751 2500w" />
</Frame>

## Do It Yourself

This option lets you write the evaluator prompt from scratch by adding the desired messages (System, Assistant, User, or Developer) and configuring the model along with its settings.

<Frame>
  <img className="block dark:hidden" src="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-do-it-yourself-light.png?fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=61ec66544fab9316edd6f5031a327393" data-og-width="2698" width="2698" data-og-height="1390" height="1390" data-path="img/evaluator/eval-do-it-yourself-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-do-it-yourself-light.png?w=280&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=eed47bd859dfa451a4ec69aaf74f4fa6 280w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-do-it-yourself-light.png?w=560&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=31ff1c84b1b85cdb43799e26081113c6 560w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-do-it-yourself-light.png?w=840&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=e1f43faeff043c4bc4f58e907d2e1cf8 840w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-do-it-yourself-light.png?w=1100&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=2d4f4d3d282841e65b4efd3d7ed452ca 1100w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-do-it-yourself-light.png?w=1650&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=837498e1e7073434223e21d4d3c0cd25 1650w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-do-it-yourself-light.png?w=2500&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=b4cc117499e84a6597ba7ad8c7f5d77b 2500w" />

  <img className="hidden dark:block" src="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-do-it-yourself-dark.png?fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=23e2088c62a4e3d2d1a2c89ed051ef06" data-og-width="2392" width="2392" data-og-height="1384" height="1384" data-path="img/evaluator/eval-do-it-yourself-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-do-it-yourself-dark.png?w=280&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=e07c34b541ba43740ec577876eeecc8b 280w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-do-it-yourself-dark.png?w=560&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=429ff2171836d2f9d0895f9501c3fd23 560w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-do-it-yourself-dark.png?w=840&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=fc119e56adf5d34686fadd729f2c8d66 840w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-do-it-yourself-dark.png?w=1100&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=96434d7fc821fb8ef4d01380a5daaf89 1100w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-do-it-yourself-dark.png?w=1650&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=5546b6489ea72cbcfd18ffcec9d2837f 1650w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-do-it-yourself-dark.png?w=2500&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=b990e54c88d44a9449292381d1285cd4 2500w" />
</Frame>

## Generate Evaluator

The evaluator prompt can be automatically configured by Traceloop by clicking on the **Generate Evaluator** button.
To enable the button, map the column you want to evaluate (such as an LLM response) and add any additional data columns required for prompt creation.
Describe the evaluator’s purpose and reference the relevant data columns in the description.

The system generates a prompt template that you can edit and customize as needed.

## Test Evaluator

Before creating an evaluator, you can test it on existing Playground data.
This allows you to refine and correct the evaluator prompt before saving the final version.

## Execute Evaluator

Evaluators can be executed in [playground columns](../playgrounds/columns/column-management) and in [experiments through the SDK](../experiments/running-from-code).
