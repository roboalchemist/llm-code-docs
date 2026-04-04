# Source: https://docs.frigade.com/guides/custom/js-sdk.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.frigade.com/llms.txt
> Use this file to discover all available pages before exploring further.

# JavaScript SDK

You can build components entirely headless using the [Frigade JS SDK](/sdk/js). For instance, to build a simple Checklist component, you can use the `Flow` and `Step` classes to get the data and build the UI. Here's an example of how to do just that:

<CodeGroup>
  ```js app.js theme={"system"}
  import { Flow, Step } from '@frigade/js';

  const flowId = 'flow_RgilNasCrSBQmrVM'; // Replace this with the Flow ID found in the Frigade dashboard
  const frigade = new Frigade('FRIGADE_API_KEY');
  const flow = await frigade.getFlow(flowId);

  const checklist = document.getElementById('checklist');

  const steps = flow.getSteps();
  const stepsCompleted = flow.getNumberOfCompletedSteps();
  const totalSteps = flow.getNumberOfAvailableSteps();

  const progress = document.createElement('div');

  progress.innerHTML = `
    <div>
      <h2>Getting started</h2>
      <p>${stepsCompleted}/${totalSteps}</p>
    </div>
    <div>
      ${steps.map((step, index) => {
        const isCompleted = index < stepsCompleted;
        return `<div style="background-color: ${isCompleted ? 'blue' : 'grey'}; height: 9px; width: 100%;"></div>`;
      }).join('')}
    </div>
  `;

  checklist.appendChild(progress);

  const stepsList = document.createElement('ul');
  stepsList.innerHTML = steps.map((step, index) => {
    const isCompleted = index < stepsCompleted;
    let html = `<li style="color: ${isCompleted ? 'blue' : 'grey'};">`
    html += `<p>${step.name}</p>`;
    html += `<button id="step-${step.id}">Mark Complete</button>`;
    html += `</li>`;
  }).join('');

  checklist.appendChild(stepsList);

  steps.forEach((step, index) => {
    const isCompleted = index < stepsCompleted;
    const button = document.getElementById(`step-${step.id}`);
    button.addEventListener('click', () => {
      if (!isCompleted) {
        step.complete();
        button.style.color = 'blue';
      }
    });
  });
  ```

  ```html index.html theme={"system"}
  <div id="checklist"></div>
  ```
</CodeGroup>
