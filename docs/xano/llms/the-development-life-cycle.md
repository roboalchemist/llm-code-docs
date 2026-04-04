# Source: https://docs.xano.com/before-you-begin/the-development-life-cycle.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# The Development Life Cycle

> Learn more about the fundamentals of application development and the software development life cycle.

<Info>
  Before you start building, we wanted to share some best practices around how to think about creating your product or service. If you don't need to learn this, you can go straight to [setting up your Database](/the-database/designing-your-database).
</Info>

<Frame caption="A visual representation of the Software Development Life Cycle">
  <img src="https://mintcdn.com/xano-997cb9ee/kUGpIho8LJSMl5Gv/images/3bb3202d-image.jpeg?fit=max&auto=format&n=kUGpIho8LJSMl5Gv&q=85&s=a7fb3fb5fd243421f3eda920f111da70" width="600" height="575" data-path="images/3bb3202d-image.jpeg" />
</Frame>

When you have an idea for an app or a project that you'd like to build, it's easy to feel overwhelmed and not even know where to begin. Regardless of whether you're on your own or with a team, it's important to have a framework around how you approach designing, launching, and maintaining your application. Luckily, when building in Xano, you can leverage a tried and tested methodology called the **Software Development Life Cycle (SDLC)**.

**There are** **six phases **to the Software Development Life cycle**,** and Xano was designed to support you and your team through each one.

<Frame caption="A visual representation of the Software Development Life Cycle">
  <img src="https://mintcdn.com/xano-997cb9ee/pz6e9Ndbn8i3u8Zz/images/6cc5afac-image.jpeg?fit=max&auto=format&n=pz6e9Ndbn8i3u8Zz&q=85&s=4cbbecb72dfba3fb1b56e3c7ef077768" width="1200" height="199" data-path="images/6cc5afac-image.jpeg" />
</Frame>

<AccordionGroup>
  <Accordion title="Planning / Analysis">
    The first stage of the SLDC usually consists of two parts: **planning** and **analysis**. Gather requirements passively or actively from potential customers or other relevant stakeholders, and ensure you are solving a real problem. You would then be able to analyze the feasibility of creating the product, revenue potential, cost, and more.

    Once you decide what you're building is in line with stakeholder goals, addresses user needs, and is feasible to create, you can move to the second stage.
  </Accordion>

  <Accordion title="Design">
    The design phase is where you start to put your ideas to paper. This might include creating actual designs in a tool like [Figma](https://www.figma.com/), or going higher level and using a tool like [Miro](https://miro.com/) to create a wireframe or flowchart. From a Xano perspective, this is where you would start designing a data model.
  </Accordion>

  <Accordion title="Development">
    With a solid foundation to work with, this phase is where the actual development happens and where you turn specifications and designs into an actual product. This phase usually takes the most time, so setting expectations with yourself and the stakeholders you are working with is important.

    Xano helps accelerate this stage with features like:

    * [Generation of API CRUD Operations](/the-function-stack/building-with-visual-development/apis)

    * [Auto-Documentation](/the-function-stack/building-with-visual-development/apis/swagger-openapi-documentation)

    * [Real-time Collaboration](/team-collaboration/realtime-collaboration)

    If you're working with a team, you can leverage Xano features like [real-time collaboration](/team-collaboration/realtime-collaboration) to seamlessly work within the same workspace, or create [Branches and Merge](/team-collaboration/branching-and-merging) them in when you're ready to move to the testing phase.
  </Accordion>

  <Accordion title="Testing">
    Before launching any product or service, it's important to have everything tested. At this phase, you would have a quality assurance (QA) team step in to run tests, but if you're on your own, you'll need to think through every part of testing your product which is more than just fixing critical bugs.

    This might sound easier than it seems, but it's essential to test all the different permutations and ways that your users might interact with your application. Here are some different types of testing that you can do in this phase.

    * **Performance testing** Is your product ready to handle the traffic/storage requirements?

    * **Functional testing** Does your application meet the requirements set for in the Planning/Analysis phase?

    * **Security testing** Is your data in a secure place, and do you meet the appropriate compliance certifications within your country, or if you're dealing with sensitive data?

    * **Unit testing** Does every part of your app work the way it's supposed to?

    * **Usability testing** Do your users actually understand how to use your app?

    **Xano provides a few features to help you in this phase**. Using [Unit Tests](/testing-debugging/unit-tests), [Test Suites](/testing-debugging/test-suites) and [Data Sources](/the-database/database-basics/data-sources) can help you use dummy data without affecting what will be live in production. We support drafts to help you and your team get things right before Publishing. [Branches](/api/branches-and-merging) can be used to create separate testing environments (Development, Staging, Production). For more complex use cases, Xano also supports [Xano Link](/enterprise-plan/xano-link), which allows you to keep all of your Workspaces and Instances in sync with a master so your customers have a consistent experience.
  </Accordion>

  <Accordion title="Deployment">
    The Deployment stage is where your product or service is shipped to its intended user(s). This process can depend on the nature of what is being released; however, it's best practice to launch to a small set of users (typically called a canary release).
  </Accordion>

  <Accordion title="Maintenance">
    Maintenance is typically the last stage of the SDLC; however, in today's world, people are moving toward a more [Agile software development](https://monday.com/blog/rnd/agile-sdlc/) approach where the product or service is continually improved, and sometimes the feedback from users makes it necessary to go back to the first step of the SDLC. This is why most images of the SDLC that you find are circular because it is a process that keeps repeating itself once you find something that's working.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).