# Source: https://docs.asapp.com/agent-desk/virtual-agent/links.md

# Links

> Learn how to manage external links and URLs that direct customers to web pages.

ASAPP provides a powerful mechanism to manage external links and URLs that direct customers to web pages. Links are predominantly used in flows, core dialogs, and customer profiles.

## Links List

The Links list page displays a list of all links available to use in AI-Console. When a link is created, it can be attached to content in a node in Flow Tooling, included in the Customer Profile panels, assigned to a View, etc.

Here, you'll find the **Link name & URL**. When adding a link to a flow or other feature, you will be required to add it from a list of all link names.

<Frame>
  <img src="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/messaging-platform/LinksPage.png?fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=d2d96077ffd90f9c1ecca8705275f856" data-og-width="2066" width="2066" data-og-height="462" height="462" data-path="images/messaging-platform/LinksPage.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/messaging-platform/LinksPage.png?w=280&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=b023e92384d7c58f057d3ba0514a9608 280w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/messaging-platform/LinksPage.png?w=560&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=6c43d5da4e151bb07ab45fb8d6eac920 560w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/messaging-platform/LinksPage.png?w=840&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=90b633fb63f5befb95d8f296b227d69d 840w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/messaging-platform/LinksPage.png?w=1100&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=3aff100f6277cc00373c995791d1df2a 1100w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/messaging-platform/LinksPage.png?w=1650&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=54f14a378417ed1ac65a0f857b32b4f6 1650w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/messaging-platform/LinksPage.png?w=2500&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=3968779da09c9d567b05b66f24c3c4d2 2500w" />
</Frame>

## Create a Link

To create a link:

1. From the **Links** landing page, click the **+** button at the bottom right.
2. A modal window will open.
3. **Link name:** Provide a name for the link. Make the name descriptive so that other users can recognize its purpose.
4. **URL:** Include the full external URL, including **http\://** (e.g., `http://example.com/about`).
5. **Channel Targets:** This feature is optional. It allows users to create a link variant that targets customers using a specific channel. See details below.

<Frame>
  <img src="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-39985f99-da5e-8997-87ba-dda6b9156a76.png?fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=20e20c97008aee4f85516847d2b52478" data-og-width="1306" width="1306" data-og-height="1068" height="1068" data-path="image/uuid-39985f99-da5e-8997-87ba-dda6b9156a76.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-39985f99-da5e-8997-87ba-dda6b9156a76.png?w=280&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=10e759a3e7419d15d07c24db007d8c80 280w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-39985f99-da5e-8997-87ba-dda6b9156a76.png?w=560&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=40041cd437135814d38dcda9e36923b0 560w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-39985f99-da5e-8997-87ba-dda6b9156a76.png?w=840&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=d636e569b0b1c69a4f90f28e80402c64 840w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-39985f99-da5e-8997-87ba-dda6b9156a76.png?w=1100&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=9dbd5c394a1f655f12a46eac07434fdc 1100w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-39985f99-da5e-8997-87ba-dda6b9156a76.png?w=1650&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=1371ba02193cf37006f2d9f5f6e16bce 1650w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-39985f99-da5e-8997-87ba-dda6b9156a76.png?w=2500&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=6ebe0a3fb16faa305c3958b27c5f8648 2500w" />
</Frame>

### Add a Channel Target Variant

1. Click **Add Channel Target** to add a URL variant. A new input field will be added.
   a. **URL Override:** Include the URL variant for the targeted channel. Please follow the same URL syntax as described under **Create a Link**.
   b. **Channel Target:** From the drop-down menu, select which channel to target. Bear in mind that a single variant per channel is currently supported.
2. **Delete targets:** To remove a target, click the **Delete** icon.
3. **Save:** To save the link, click the **Save** button. The link will not be active until it is assigned to a flow, customer profile or any other feature that supports **Links**.
4. **Cancel:** On click, all changes will be cleared.

<Frame>
  <img src="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-86cb8d7f-ba8f-6c01-8926-4f0cae6d3b80.png?fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=1e53e8ba29d7c31f883cad3bf2d9dc33" data-og-width="1090" width="1090" data-og-height="522" height="522" data-path="image/uuid-86cb8d7f-ba8f-6c01-8926-4f0cae6d3b80.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-86cb8d7f-ba8f-6c01-8926-4f0cae6d3b80.png?w=280&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=0079be88d7d7b9b2f139b653fdf634c5 280w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-86cb8d7f-ba8f-6c01-8926-4f0cae6d3b80.png?w=560&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=808e10e53564e0ad8911dd18862c2db5 560w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-86cb8d7f-ba8f-6c01-8926-4f0cae6d3b80.png?w=840&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=c6cf42b09ff0c340a97fa285300d7c8f 840w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-86cb8d7f-ba8f-6c01-8926-4f0cae6d3b80.png?w=1100&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=4ae354f7320c8b6238487d2300d8384c 1100w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-86cb8d7f-ba8f-6c01-8926-4f0cae6d3b80.png?w=1650&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=9a5fbf62c2596848f4db0356550e5c02 1650w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-86cb8d7f-ba8f-6c01-8926-4f0cae6d3b80.png?w=2500&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=abfd194f63b7d6ed6e09bde9a888f989 2500w" />
</Frame>

### Link Assignments

Once a link has been created, it can be sent to customers in flows. The **Links** feature will keep tabs on where each link has been assigned and provide quick access to those feature areas.

When viewing a specific link, the Usage section indicates which flows are currently using the respective link. On click, you can navigate directly to the flow. When a link is not assigned in any flow, 'Not yet assigned' will be displayed.

<Frame>
  <img src="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-80058a33-eb5c-5c76-3e89-8e7a35b2a5af.png?fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=dec88d376965339adb327ffb50196179" data-og-width="1072" width="1072" data-og-height="278" height="278" data-path="image/uuid-80058a33-eb5c-5c76-3e89-8e7a35b2a5af.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-80058a33-eb5c-5c76-3e89-8e7a35b2a5af.png?w=280&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=430a1302a16997188ced38a976d41694 280w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-80058a33-eb5c-5c76-3e89-8e7a35b2a5af.png?w=560&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=f06bc69754bab02a65f9eb5201441cc5 560w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-80058a33-eb5c-5c76-3e89-8e7a35b2a5af.png?w=840&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=dcafb5bc82d499e9c334ac110e1f6622 840w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-80058a33-eb5c-5c76-3e89-8e7a35b2a5af.png?w=1100&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=0e66ec885573204498269c44718f5244 1100w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-80058a33-eb5c-5c76-3e89-8e7a35b2a5af.png?w=1650&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=2c47cc2503360e462d6100cab88a5dc4 1650w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-80058a33-eb5c-5c76-3e89-8e7a35b2a5af.png?w=2500&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=6c8340fc8789d05b2cb4ce59508c1a3d 2500w" />
</Frame>

## Edit a Link

Link changes are global, which means that saved changes are immediately pushed to all features that reference the link.

1. From the **Links** landing page, click the **link name** you want to edit.
2. **Link ID:** After a link is saved for the first time, a unique identifier is automatically assigned to the link. This identifier does not change over time, including when the link is edited.
   a. The **Link ID** can be referenced in **Historical Reporting** for your reporting needs.
3. Assign changes to the configurations.
4. **Save:** When changes are complete, click **Save** to automatically apply the changes.

## Delete a Link

Links can be deleted, but only if they are not currently assigned. To delete a link that is assigned, remove the assignments first.

<Frame>
  <img src="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-bdf4a69c-fadd-918a-e277-aa4f7c3826eb.png?fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=f63b44776de7d924f11f7da28d3b4038" data-og-width="1999" width="1999" data-og-height="1121" height="1121" data-path="image/uuid-bdf4a69c-fadd-918a-e277-aa4f7c3826eb.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-bdf4a69c-fadd-918a-e277-aa4f7c3826eb.png?w=280&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=bac32572ca604bb4f8a485b4a5ff7fb2 280w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-bdf4a69c-fadd-918a-e277-aa4f7c3826eb.png?w=560&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=9001b966277c37058f258dc0c6c5117f 560w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-bdf4a69c-fadd-918a-e277-aa4f7c3826eb.png?w=840&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=935beaeac037bb9106255dfb0e99b3f9 840w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-bdf4a69c-fadd-918a-e277-aa4f7c3826eb.png?w=1100&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=84535d0140b07040bfdf0cf90b464da9 1100w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-bdf4a69c-fadd-918a-e277-aa4f7c3826eb.png?w=1650&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=041dc30a5c85c7223431ce07057d2048 1650w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-bdf4a69c-fadd-918a-e277-aa4f7c3826eb.png?w=2500&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=75debf5a2cbf00c6742d2463c7b8bdbb 2500w" />
</Frame>

1. If the link is assigned: When opening the Link modal, the **Delete** button will be disabled. The delete function will remain disabled until all link assignments have been removed.
2. If the link is not assigned: The link can be deleted by clicking on the **Delete** button on the bottom-left area of the link modal.
