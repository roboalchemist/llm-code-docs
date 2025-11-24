# Source: https://mintlify.com/docs/ai/assistant.md

# Assistant

> Add AI-powered chat to your docs that answers questions, cites sources, and generates code examples.

<Info>
  The assistant is automatically enabled on [Pro and Custom plans](https://mintlify.com/pricing?ref=assistant).
</Info>

## About the assistant

The assistant answers questions about your documentation through natural language queries. It is embedded directly in your documentation site, so users can find answers quickly and succeed with your product.

The assistant uses agentic RAG (retrieval-augmented generation) with tool calling powered by Claude Sonnet 4.5. When users ask questions, the assistant:

* **Searches and retrieves** relevant content from your documentation to provide accurate answers.
* **Cites sources** and provides navigable links to take users directly to referenced pages.
* **Generates copyable code examples** to help users implement solutions from your documentation.

Each message sent to the assistant counts toward your plan's message allowance. If you exceed your allowance, additional messages incur overage charges. You can set spending limits or disable the assistant if you reach your message allowance.

You can view assistant usage through your dashboard to understand user behavior and documentation effectiveness. Export and analyze query data to help identify:

* Frequently asked questions that might need better coverage.
* Content gaps where users struggle to find answers.
* Popular topics that could benefit from additional content.

## Configuring the assistant

The assistant is enabled by default for Pro and Custom plans.

Manage the assistant from your [dashboard](https://dashboard.mintlify.com/products/assistant/settings). Click **Configuration** to enable or disable the assistant, configure response handling, add default questions, and set a spend limit.

<Frame>
  <img src="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/configuration-light.png?fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=fe584b4ff97e6e8c5d29793b49bfc1f1" alt="The assistant toolbar in the dashboard. The Configuration button is emphasized with an orange rectangle." className="block dark:hidden" data-og-width="2036" width="2036" data-og-height="426" height="426" data-path="images/assistant/configuration-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/configuration-light.png?w=280&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=64a1fef5c36972c68d8638c732e1869e 280w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/configuration-light.png?w=560&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=3e923099c726ebc87b023d10acc2b7f0 560w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/configuration-light.png?w=840&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=012442bafc2da6adff66feb70d96ea92 840w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/configuration-light.png?w=1100&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=abad747c9a14d3207cb52cf48b74372d 1100w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/configuration-light.png?w=1650&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=e335a318cb8238e84e4692a85a394bdd 1650w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/configuration-light.png?w=2500&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=2abec94076616987fd205ae8d2894419 2500w" />

  <img src="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/configuration-dark.png?fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=10cacb17b4649fa239e5ca5bac3adbd7" alt="The assistant toolbar in the dashboard. The Configuration button is emphasized with an orange rectangle." className="hidden dark:block" data-og-width="2038" width="2038" data-og-height="428" height="428" data-path="images/assistant/configuration-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/configuration-dark.png?w=280&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=22ff0b697f2ab609de6786f938ba300b 280w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/configuration-dark.png?w=560&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=01619d849b3f10589ea8c8a93fa7e664 560w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/configuration-dark.png?w=840&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=e432bcc0a82e8ea9c4f9393e5c7da7cf 840w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/configuration-dark.png?w=1100&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=304186a00cd68dbe155670b61ca42eca 1100w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/configuration-dark.png?w=1650&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=28ce427dc69d5af9fda882f639de4b8a 1650w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/configuration-dark.png?w=2500&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=87062d8fda02cad8d0a4b604da7c7555 2500w" />
</Frame>

### Enable or disable the assistant

Toggle the assistant status to enable or disable the assistant for your documentation site.

<Frame>
  <img src="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-light.png?fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=723881f19ac3ad665a774eeb6f3b8652" alt="The assistant status toggle in the dashboard." className="block dark:hidden" data-og-width="2038" width="2038" data-og-height="338" height="338" data-path="images/assistant/status-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-light.png?w=280&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=324018ab573007ce00dea0256aec2789 280w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-light.png?w=560&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=08fa6f1070c0dfc73518d184244fab09 560w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-light.png?w=840&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=9396ddf191ca4433612550f1a6d8aa74 840w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-light.png?w=1100&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=08b1fcdd73408ae3aa2d441a1ad7b370 1100w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-light.png?w=1650&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=210932e2ffa0ed0f37e67cee7f9f5991 1650w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-light.png?w=2500&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=8a9373c2ccd834e7d146b06164874a8d 2500w" />

  <img src="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-dark.png?fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=8c7ae23c57d3db8f67a649b0f09d45c4" alt="The assistant status toggle in the dashboard." className="hidden dark:block" data-og-width="2040" width="2040" data-og-height="338" height="338" data-path="images/assistant/status-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-dark.png?w=280&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=0989add1e16e03d0f516c2d0e3271cc7 280w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-dark.png?w=560&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=af084192f28f689c1506a15750e50167 560w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-dark.png?w=840&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=7b36249ad898762cae73b78c8bc97477 840w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-dark.png?w=1100&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=a224b83ac59895b6ce7884c90a24842d 1100w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-dark.png?w=1650&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=161b1e9ac9cbf2c1b678fa59240d99cb 1650w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-dark.png?w=2500&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=8d5763ab56eba1c7d97c987b60b3148b 2500w" />
</Frame>

### Control placement

Select where the assistant appears on your documentation site. Choose between a floating chat bubble at the bottom of the page or a button next to the search bar.

<Frame>
  <img src="https://mintcdn.com/mintlify/Xfe-YlAgjAXFlRiK/images/assistant/placement-light.png?fit=max&auto=format&n=Xfe-YlAgjAXFlRiK&q=85&s=1c9096e678af41a9e955a005de432610" alt="The assistant placement panel in the dashboard with the bottom of page option selected." className="block dark:hidden" data-og-width="1286" width="1286" data-og-height="722" height="722" data-path="images/assistant/placement-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Xfe-YlAgjAXFlRiK/images/assistant/placement-light.png?w=280&fit=max&auto=format&n=Xfe-YlAgjAXFlRiK&q=85&s=41f444f20d85904cbe203244f65f63ed 280w, https://mintcdn.com/mintlify/Xfe-YlAgjAXFlRiK/images/assistant/placement-light.png?w=560&fit=max&auto=format&n=Xfe-YlAgjAXFlRiK&q=85&s=d3cc4a83d63f1cfc34fa719d703be619 560w, https://mintcdn.com/mintlify/Xfe-YlAgjAXFlRiK/images/assistant/placement-light.png?w=840&fit=max&auto=format&n=Xfe-YlAgjAXFlRiK&q=85&s=8b61ff7672f6b7c0624ac556c64191d5 840w, https://mintcdn.com/mintlify/Xfe-YlAgjAXFlRiK/images/assistant/placement-light.png?w=1100&fit=max&auto=format&n=Xfe-YlAgjAXFlRiK&q=85&s=25e1a3e918859b10856c70874577d028 1100w, https://mintcdn.com/mintlify/Xfe-YlAgjAXFlRiK/images/assistant/placement-light.png?w=1650&fit=max&auto=format&n=Xfe-YlAgjAXFlRiK&q=85&s=0b6e531c88eaa99700734f14baa35a68 1650w, https://mintcdn.com/mintlify/Xfe-YlAgjAXFlRiK/images/assistant/placement-light.png?w=2500&fit=max&auto=format&n=Xfe-YlAgjAXFlRiK&q=85&s=d7afd18f3ae82099a339e951d94d3208 2500w" />

  <img src="https://mintcdn.com/mintlify/Xfe-YlAgjAXFlRiK/images/assistant/placement-dark.png?fit=max&auto=format&n=Xfe-YlAgjAXFlRiK&q=85&s=d66a9422dad7e5cdd2a8d39f353b262e" alt="The assistant placement panel in the dashboard with the bottom of page option selected." className="hidden dark:block" data-og-width="1288" width="1288" data-og-height="722" height="722" data-path="images/assistant/placement-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Xfe-YlAgjAXFlRiK/images/assistant/placement-dark.png?w=280&fit=max&auto=format&n=Xfe-YlAgjAXFlRiK&q=85&s=419dca222b2be1a25e188cbf0d5ce3e7 280w, https://mintcdn.com/mintlify/Xfe-YlAgjAXFlRiK/images/assistant/placement-dark.png?w=560&fit=max&auto=format&n=Xfe-YlAgjAXFlRiK&q=85&s=40f493ded5f71918498f27342f4d8508 560w, https://mintcdn.com/mintlify/Xfe-YlAgjAXFlRiK/images/assistant/placement-dark.png?w=840&fit=max&auto=format&n=Xfe-YlAgjAXFlRiK&q=85&s=6c1adcee499867eabc004a5b47c6f7bf 840w, https://mintcdn.com/mintlify/Xfe-YlAgjAXFlRiK/images/assistant/placement-dark.png?w=1100&fit=max&auto=format&n=Xfe-YlAgjAXFlRiK&q=85&s=4ebd42037adba51fec88ed7b6694c77d 1100w, https://mintcdn.com/mintlify/Xfe-YlAgjAXFlRiK/images/assistant/placement-dark.png?w=1650&fit=max&auto=format&n=Xfe-YlAgjAXFlRiK&q=85&s=6bdb464911d7993b31eeeaff18f494b6 1650w, https://mintcdn.com/mintlify/Xfe-YlAgjAXFlRiK/images/assistant/placement-dark.png?w=2500&fit=max&auto=format&n=Xfe-YlAgjAXFlRiK&q=85&s=bfa3fd381854b86706e541d47fda8e35 2500w" />
</Frame>

### Set deflection email

In the response handling section, enable the assistant to redirect unanswered questions to your support team. Specify an email address that the assistant provides to users who ask questions that it cannot answer.

<Frame>
  <img src="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/deflection-light.png?fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=f55e6cb6a0121034aa40b18decab3d80" alt="The assistant deflection panel in the dashboard. Assistant deflection is toggled on and support@mintlify.com is set as the deflection email." className="block dark:hidden" data-og-width="2040" width="2040" data-og-height="580" height="580" data-path="images/assistant/deflection-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/deflection-light.png?w=280&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=16915ff0e1fee36dd5280a50700c0679 280w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/deflection-light.png?w=560&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=1bf4fb91773e61288d13102b59f7967c 560w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/deflection-light.png?w=840&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=363811453870d3ed3f8621c31db10680 840w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/deflection-light.png?w=1100&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=dc8d8edc71f47b92673a1958b2c26c94 1100w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/deflection-light.png?w=1650&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=99f71ff3e72bdb8b3cc1048aa5d1eaad 1650w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/deflection-light.png?w=2500&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=73ee21cc525db1e1db44eff5fcda10e3 2500w" />

  <img src="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/deflection-dark.png?fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=43b9454cd12cef2e9a0581306415de29" alt="The assistant deflection panel in the dashboard. Assistant deflection is toggled on and support@mintlify.com is set as the deflection email." className="hidden dark:block" data-og-width="2040" width="2040" data-og-height="580" height="580" data-path="images/assistant/deflection-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/deflection-dark.png?w=280&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=0b3ad456946f37175d208d0ff6e42ff4 280w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/deflection-dark.png?w=560&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=27e4cd4f334cddf9eb607f7582c3d71f 560w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/deflection-dark.png?w=840&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=83f3dc3c9eeeeb6045bcdfb3f669b8f8 840w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/deflection-dark.png?w=1100&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=fcd34d090c6be6872d07eb9bdc336f38 1100w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/deflection-dark.png?w=1650&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=eeefd70e7b15cba074bc8ea1cc57ddf3 1650w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/deflection-dark.png?w=2500&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=a0b6a7547f58a0f536cbc6b5bc64eefc 2500w" />
</Frame>

### Search sites

<Note>
  Site search is in beta. To enable it for your documentation site, [contact our sales team](mailto:gtm@mintlify.com).
</Note>

In the response handling section, configure sites that the assistant can search for additional context when answering questions.

* Sites must be publicly available.
* Sites that require JavaScript to load are not supported.

<Frame>
  <img src="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-sites-light.png?fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=ac5e9756055300a5409375f139458525" alt="The assistant search sites panel in the dashboard. The assistant is configured to search the mintlify.com and mintlify.com/blog domains." className="block dark:hidden" data-og-width="1306" width="1306" data-og-height="646" height="646" data-path="images/assistant/search-sites-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-sites-light.png?w=280&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=d4a04fac8b69e372fe398b3f6de4f595 280w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-sites-light.png?w=560&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=60f6a18fe56c08e4c474eaf9ed667755 560w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-sites-light.png?w=840&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=616231ed12d03848e0e278573841a642 840w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-sites-light.png?w=1100&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=388d2e030b23d297e137eead642e9df4 1100w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-sites-light.png?w=1650&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=b0f0050e3b5b82aaf9949ada105ead8c 1650w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-sites-light.png?w=2500&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=ea5cbac86b8af316f17e270cb87ab1a6 2500w" />

  <img src="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-sites-dark.png?fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=ba632460371199a921559e788f8cecc4" alt="The assistant search sites panel in the dashboard. The assistant is configured to search the mintlify.com and mintlify.com/blog domains." className="hidden dark:block" data-og-width="1306" width="1306" data-og-height="646" height="646" data-path="images/assistant/search-sites-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-sites-dark.png?w=280&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=017ae9b79e87eb9b74253fb9e074f65e 280w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-sites-dark.png?w=560&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=e3035bbdaeea85ce53a94c1c094bcb63 560w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-sites-dark.png?w=840&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=5893bbc5043684fe247a48b4bb25bf8b 840w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-sites-dark.png?w=1100&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=b211a9def9b162d07a0343466558a57d 1100w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-sites-dark.png?w=1650&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=3573cee1735cd9fcdbac882bcf2d3358 1650w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-sites-dark.png?w=2500&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=a66b9bfac0de24128fac9d09cee97169 2500w" />
</Frame>

Use the following filtering syntax for more precise control over what the assistant can search:

* **Domain-level filtering**
  * `example.com`: Search only the `example.com` domain
  * `docs.example.com`: Search only the `docs.example.com` subdomain
  * `*.example.com`: Search all subdomains of `example.com`
* **Path-level filtering**
  * `docs.example.com/api`: Search all pages under the `/api` subpath
* **Multiple patterns**
  * Add multiple entries to target different sections of sites

### Add sample questions

Help your users start questions with the assistant by adding sample questions. In the search suggestions section, add up to three sample questions.

<Frame>
  <img src="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-suggestions-light.png?fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=041635b9ca52f5ba9d8d455bac8ab6a2" alt="The search suggestions panel in the dashboard. What is an OpenAPI spec? is configured as a sample question." className="block dark:hidden" data-og-width="2124" width="2124" data-og-height="590" height="590" data-path="images/assistant/search-suggestions-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-suggestions-light.png?w=280&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=f0635e2a6b66cd6c3efffba22d4fe7ab 280w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-suggestions-light.png?w=560&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=d66d8295a95de0438c498b8be9da8c35 560w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-suggestions-light.png?w=840&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=08405d14a248ab8120d80d0ef9d08cc2 840w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-suggestions-light.png?w=1100&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=500e195bfb0521fe75ad53c39dae2173 1100w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-suggestions-light.png?w=1650&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=03afbb9113290cf83279e93097a8b206 1650w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-suggestions-light.png?w=2500&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=06ceb1f0c6cfbedc2f3a1aff52c44ca9 2500w" />

  <img src="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-suggestions-dark.png?fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=2fd18a1f2903ee2c5fa7303da0de20ca" alt="The search suggestions panel in the dashboard. What is an OpenAPI spec? is configured as a sample question." className="hidden dark:block" data-og-width="2124" width="2124" data-og-height="590" height="590" data-path="images/assistant/search-suggestions-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-suggestions-dark.png?w=280&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=837a22d5297e8207d200a48b1e2a8a37 280w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-suggestions-dark.png?w=560&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=a4bbf62a48aa3fce5535b111f238a11e 560w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-suggestions-dark.png?w=840&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=cb17a1ba40c2314ffb0f8b04078096e1 840w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-suggestions-dark.png?w=1100&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=dd01fd42636530007d9a59c98d511888 1100w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-suggestions-dark.png?w=1650&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=59405cd8603fec23bce2c0a1ef1c0271 1650w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/search-suggestions-dark.png?w=2500&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=8d4c755afa8cf0309be2dcacf73a4b6e 2500w" />
</Frame>

### Set a spend limit

Set a spend limit to control what happens if you reach your message allowance. By default, the assistant continues to answer user questions after you reach your message allowance, which incurs overages.

When you reach your spend limit, the assistant is disabled until your message allowance resets.

1. Select the **Billing** tab.

<Frame>
  <img src="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/billing-light.png?fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=0dc4a1790633a9030a591a8e0d161be1" alt="The billing tab on the Assistant Configurations page. The Billing tab is emphasized with an orange rectangle." className="block dark:hidden" style={{ width: '268px', height: 'auto' }} data-og-width="582" width="582" data-og-height="328" height="328" data-path="images/assistant/billing-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/billing-light.png?w=280&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=e8b29e941cc3a88f382936f7747d5427 280w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/billing-light.png?w=560&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=2e6dc3b3c7326f0ea044d8069644fc83 560w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/billing-light.png?w=840&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=cd487a27d9513131d97db962234c8037 840w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/billing-light.png?w=1100&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=872a48286f46c43c610a3f8ed0ba3a2c 1100w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/billing-light.png?w=1650&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=b9d40bbe961b268ad82a605d58f3437b 1650w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/billing-light.png?w=2500&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=5901c45abeb2b040c4f5e7c3cfece8cf 2500w" />

  <img src="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/billing-dark.png?fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=2a349bae7a1ee7b77cbbc74ee1c196e8" alt="The billing tab on the Assistant Configurations page. The Billing tab is emphasized with an orange rectangle." className="hidden dark:block" style={{ width: '268px', height: 'auto' }} data-og-width="584" width="584" data-og-height="328" height="328" data-path="images/assistant/billing-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/billing-dark.png?w=280&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=acd35de0eb0b3fef80ab437b491c8130 280w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/billing-dark.png?w=560&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=ac38d561c95a35fc09dbe85cc93e594a 560w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/billing-dark.png?w=840&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=dbff6409b9ea72020b78d29f077b8e16 840w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/billing-dark.png?w=1100&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=beb9ced921d14262a7c0c39515d51c90 1100w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/billing-dark.png?w=1650&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=b63243de39c13727b3c68961cb05cf49 1650w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/billing-dark.png?w=2500&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=59cf70b9e8a37bf8b8d87c00e98b3809 2500w" />
</Frame>

2. Set a spend limit for assistant messages beyond your allowance.
3. Set usage alerts to receive an email when you reach a certain percentage of your spend limit.

## Using the assistant

Users can access the assistant in three ways:

* **Keyboard shortcut**: <kbd>Command</kbd> + <kbd>I</kbd> (<kbd>Ctrl</kbd> + <kbd>I</kbd> on Windows)
* **Assistant button** next to the search bar
  <img
    src="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-light.png?fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=716582bc54eaea73cb53d26b36a74fb4"
    className="block dark:hidden rounded-2xl border border-gray-100 shadow-lg"
    style={{
    width: '268px',
    height: 'auto',
  }}
    alt="Search bar and assistant button in light mode."
    data-og-width="1806"
    width="1806"
    data-og-height="322"
    height="322"
    data-path="images/assistant/assistant-button-light.png"
    data-optimize="true"
    data-opv="3"
    srcset="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-light.png?w=280&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=9ae2bace996e8301def4d07a3151764b 280w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-light.png?w=560&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=70cde876f7f7ee59c07594108203c93c 560w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-light.png?w=840&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=95f1633b5e41b8b279a8923f7a1fa075 840w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-light.png?w=1100&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=11b8f8f14bdeb252e9ba07d622834146 1100w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-light.png?w=1650&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=b2c08d4d0573c75a3493e6dfd282dd56 1650w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-light.png?w=2500&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=fc092ff8b664ce5842067bca8bd531c7 2500w"
  />
  <img
    src="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-dark.png?fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=34096a771f492853e59eef654567b081"
    className="hidden dark:block rounded-2xl border border-white/10 shadow-lg"
    style={{
    width: '268px',
    height: 'auto',
  }}
    alt="Search bar and assistant button in dark mode."
    data-og-width="1806"
    width="1806"
    data-og-height="324"
    height="324"
    data-path="images/assistant/assistant-button-dark.png"
    data-optimize="true"
    data-opv="3"
    srcset="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-dark.png?w=280&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=1b8226b14933399c53d7975e02ad7d9d 280w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-dark.png?w=560&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=400dff40f5e394fd2d85a52066592e26 560w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-dark.png?w=840&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=00d387ddc8a0336bbac7e21b1130dfa1 840w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-dark.png?w=1100&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=860463b82aa2db420d87af6138c61e66 1100w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-dark.png?w=1650&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=0c15a237b868f23fad34f7838bdc3579 1650w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-dark.png?w=2500&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=1e88586f53b4f6f07b8336a77f0f940f 2500w"
  />
* **URLs** with `?assistant=open` appended open the assistant when the page loads. For example, [https://mintlify.com/docs?assistant=open](https://mintlify.com/docs?assistant=open).

Each method opens a chat panel on the right side of your docs. Users can ask any question and the assistant searches your documentation for an answer. If no relevant information is found, the assistant responds that it cannot answer the question.

## Making content AI ingestible

Structure your documentation to help the assistant provide accurate, relevant answers. Clear organization and comprehensive context benefit both human readers and AI understanding.

<Card title="Structure and organization">
  * Use semantic markup.
  * Write descriptive headings for sections.
  * Create a logical information hierarchy.
  * Use consistent formatting across your docs.
  * Include comprehensive metadata in page frontmatter.
  * Break up long blocks of text into shorter paragraphs.
</Card>

<Card title="Context">
  * Define specific terms and acronyms when first introduced.
  * Provide sufficient conceptual content about features and procedures.
  * Include examples and use cases.
  * Cross-reference related topics.
  * Add [hidden pages](/organize/hidden-pages) with additional context that users don't need, but the assistant can reference.
</Card>

## Exporting and analyzing queries

Review and export queries from your dashboard to understand how people interact with your documentation and identify improvement opportunities. Some ways that analyzing queries can help you improve your documentation:

* Identify content gaps where frequent queries receive insufficient answers.
* Discover user behavior patterns and common information needs from themes and patterns in queries.
* Prioritize high-traffic pages for accuracy and quality improvements.

You can explore queries from your [dashboard](https://dashboard.mintlify.com/products/assistant), but to get more powerful insights we recommend exporting a `CSV` file of your queries, responses, and sources to analyze with your preferred AI tool.

1. Navigate to the [assistant page](https://dashboard.mintlify.com/products/assistant) in your dashboard.
2. Select **Export to CSV**.
3. Analyze the exported data using your preferred tool.

<Card title="Sample analysis prompts">
  * Summarize the most common themes of the queries.
  * List any queries that had no sources cited.
  * Find patterns in unsuccessful interactions.
</Card>

## Assistant insights

Use assistant insights to understand how users interact with your documentation through two views: categories and chat history.

### Categories

The categories tab uses LLMs to automatically categorize conversations by question topic and theme. Conversations are organized by the most common groupings, helping you quickly identify:

* Which topics generate the most questions
* Patterns in user needs and behavior
* Areas where documentation might need expansion or clarification

Review categories to see what areas of your documentation people frequently ask about and check that you have sufficient coverage of those topics.

### Chat history

The chat history tab displays chronological records of all assistant conversations. Select any message to view the complete chat thread, including the user's question, the assistant's response, and any sources cited.

## Troubleshooting

<Accordion title="Assistant chat bar not visible">
  If the assistant UI is not visible in specific browsers, you may need to submit a false positive report to [EasyList](https://easylist.to). Browsers that use the EasyList Cookies List like Brave and Comet sometimes block the assistant or other UI elements. The EasyList Cookies List includes a domain-specific rule that hides fixed elements on certain domains to block cookie banners. This rule inadvertently affects legitimate UI components.

  Submit a false positive report to [EasyList](https://github.com/easylist/easylist) to request removal of the rule. This resolves the issue for all users once the filter list is updated.
</Accordion>
