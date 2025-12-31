# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/controlling-skill-flow.md

# Control skill flow

You can use functions such as goto\_node, goto\_intent, execute\_intent, or goto\_output in the JS while building a skill flow for navigating to different nodes in the flow, based on your business requirements. See [Flow control](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/flow-control), for more information.

Consider that at the end of placing a pizza order, you wish to navigate to another node that provides options to place order starters in the Order skill of the MacPizza agent. At the end of taking the order details,&#x20;

* You can add a JS node with **return goto\_node('<\<skill\_key>>.<\<intent\_key>>')** and navigate to the required node. See [Flow control](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/flow-control), for more information.
* You can also specify the same suing **Goto Skill Message** in the **Advanced Settings** of the response node. See [Advanced Settings](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/advanced-settings), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Mah1bSVgrzMksXemDH4%2F-Mah1h5rBCpLmDyM7saZ%2F5.7.-js-flow-control-example-1.png?alt=media\&token=052c1a55-acad-443b-8242-0441bb7033b2)

In the agent, the navigation is displayed as follows:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FZ87VA9ItbgloXfjrdY9A%2Fimage.png?alt=media\&token=2a6d8e01-47a7-4f22-9067-a701cc8e3674)

Similarly, you can use JS in post-processing for navigating to different nodes in the flow based on your business requirements. See [Add user intent](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-user-intent), for more information on post-processing.
