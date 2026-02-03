# Source: https://docs.asapp.com/changelog/autosummary.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# AI Summary Updates

> New updates and improvements across AI Summary

<Update label="2024-12-18 - Intents Self Service Tooling">
  ## Intents Self Service Tooling

  The Intents Self Service tool in ASAPP's AI Console provides a streamlined interface for managing intent classification. This automated, self-serve UI allows customers to:

  * Upload, create and modify intent labels without support team intervention
  * Manage intent label hierarchies during onboarding or as business needs evolve
  * Consolidate or create more granular intents
  * Deploy changes to production within minutes

  The tool leverages GenAI (LLMs) to enable:

  * Zero-day customer onboarding
  * Self-service intent management through an intuitive frontend
  * Real-time intent classification deployment pipeline

  <Accordion title="How It Works">
    ## How It Works

    This service is built on a front-end interface, no separate API configuration is required from the customers.

    **Import Flow of Intents**

    1. Upload a csv/text file with the intent details, Refer to the provided links in the guidelines to familiarize yourself with the required file format and the necessary information for intents.
    2. Select the desired file and upload the file
       <Frame>
         <img src="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4c80b487-aa07-a23a-a020-a27ae2a93488.png?fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=14d3dd0522a17103a4733cd68715723c" data-og-width="1600" width="1600" data-og-height="1002" height="1002" data-path="image/uuid-4c80b487-aa07-a23a-a020-a27ae2a93488.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4c80b487-aa07-a23a-a020-a27ae2a93488.png?w=280&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=31fc0ebc5ea0428cbf6029f25f25e87a 280w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4c80b487-aa07-a23a-a020-a27ae2a93488.png?w=560&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=2496627057728e4e6feedc2901d1b574 560w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4c80b487-aa07-a23a-a020-a27ae2a93488.png?w=840&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=5e6be2c1cbca527612e2446f5a7ec566 840w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4c80b487-aa07-a23a-a020-a27ae2a93488.png?w=1100&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=0baf608df19af37e3a6ef2573b4032cb 1100w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4c80b487-aa07-a23a-a020-a27ae2a93488.png?w=1650&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=c8e1a0ce373b1ac0895a845b7a29376f 1650w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4c80b487-aa07-a23a-a020-a27ae2a93488.png?w=2500&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=5908f7963daa99774f99b30aa1ba74ee 2500w" />
       </Frame>
    3. Review selected file before deploying the intents
       <Frame>
         <img src="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-37078cc3-3b9b-bd41-7aac-9490a84ad726.png?fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=16f808b02de4ce4ceb06f9c7335ad67b" data-og-width="1600" width="1600" data-og-height="1002" height="1002" data-path="image/uuid-37078cc3-3b9b-bd41-7aac-9490a84ad726.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-37078cc3-3b9b-bd41-7aac-9490a84ad726.png?w=280&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=5ac1e0579eb33d1faae2bcea28b7f3e5 280w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-37078cc3-3b9b-bd41-7aac-9490a84ad726.png?w=560&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=702cd804a624fd0070a1ed3e9bda3d75 560w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-37078cc3-3b9b-bd41-7aac-9490a84ad726.png?w=840&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=267743772769a2080d028253032a93ad 840w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-37078cc3-3b9b-bd41-7aac-9490a84ad726.png?w=1100&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=03b319cfde88a4b7eca2ae83fa5b84e6 1100w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-37078cc3-3b9b-bd41-7aac-9490a84ad726.png?w=1650&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=8d6ef4495b4dfadd6a1f701993b05364 1650w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-37078cc3-3b9b-bd41-7aac-9490a84ad726.png?w=2500&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=182c58653e166d239de1bef2af80d06d 2500w" />
       </Frame>
    4. Review and verify your uploaded intents
       <Frame>
         <img src="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d63f6c9b-2abf-f13e-338e-eb2339ddf187.png?fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=af70a46a07d40d7ad8a4fea695313adc" data-og-width="1600" width="1600" data-og-height="1002" height="1002" data-path="image/uuid-d63f6c9b-2abf-f13e-338e-eb2339ddf187.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d63f6c9b-2abf-f13e-338e-eb2339ddf187.png?w=280&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=058275804fa16cebdeb98c54b4b3d1ca 280w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d63f6c9b-2abf-f13e-338e-eb2339ddf187.png?w=560&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=e3de401374baf7d17b37aed504848409 560w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d63f6c9b-2abf-f13e-338e-eb2339ddf187.png?w=840&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=6e25fb94f2aab84f12abd9ab30c472a4 840w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d63f6c9b-2abf-f13e-338e-eb2339ddf187.png?w=1100&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=92331415cc4e97fa303fc8b44af6a2a9 1100w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d63f6c9b-2abf-f13e-338e-eb2339ddf187.png?w=1650&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=61fad3e0a40c8cf44f497efd86dc9f46 1650w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d63f6c9b-2abf-f13e-338e-eb2339ddf187.png?w=2500&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=9f02ec816fe8fd9cb7e66ca5c7b9549d 2500w" />
       </Frame>

    **Adding a new Intent to the hierarchy**

    1. Review the existing Intent hierarchy and click 'New Intent' from the 'Add' button top right
       <Frame>
         <img src="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d63f6c9b-2abf-f13e-338e-eb2339ddf187.png?fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=af70a46a07d40d7ad8a4fea695313adc" data-og-width="1600" width="1600" data-og-height="1002" height="1002" data-path="image/uuid-d63f6c9b-2abf-f13e-338e-eb2339ddf187.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d63f6c9b-2abf-f13e-338e-eb2339ddf187.png?w=280&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=058275804fa16cebdeb98c54b4b3d1ca 280w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d63f6c9b-2abf-f13e-338e-eb2339ddf187.png?w=560&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=e3de401374baf7d17b37aed504848409 560w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d63f6c9b-2abf-f13e-338e-eb2339ddf187.png?w=840&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=6e25fb94f2aab84f12abd9ab30c472a4 840w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d63f6c9b-2abf-f13e-338e-eb2339ddf187.png?w=1100&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=92331415cc4e97fa303fc8b44af6a2a9 1100w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d63f6c9b-2abf-f13e-338e-eb2339ddf187.png?w=1650&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=61fad3e0a40c8cf44f497efd86dc9f46 1650w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d63f6c9b-2abf-f13e-338e-eb2339ddf187.png?w=2500&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=9f02ec816fe8fd9cb7e66ca5c7b9549d 2500w" />
       </Frame>
    2. Add intent details such as the intent label, parent intent, and description. Refer to sample file in case any further clarifications
       <Frame>
         <img src="https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-08197b0b-b683-317d-d378-c68c3110e42c.png?fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=15d64eb321b445336a5f1342370eae1c" data-og-width="1304" width="1304" data-og-height="818" height="818" data-path="image/uuid-08197b0b-b683-317d-d378-c68c3110e42c.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-08197b0b-b683-317d-d378-c68c3110e42c.png?w=280&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=b3ab5fe929051bba0c331d676d5710d6 280w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-08197b0b-b683-317d-d378-c68c3110e42c.png?w=560&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=a7c4d553a6a39c54d77e26ca88271a61 560w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-08197b0b-b683-317d-d378-c68c3110e42c.png?w=840&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=1ab15893a17d7ee2257d1180d2b60a68 840w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-08197b0b-b683-317d-d378-c68c3110e42c.png?w=1100&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=2ba56577ddd231936aa3485f37d56f4b 1100w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-08197b0b-b683-317d-d378-c68c3110e42c.png?w=1650&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=3a6e95e89909b04f49ad7408e3cfe620 1650w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-08197b0b-b683-317d-d378-c68c3110e42c.png?w=2500&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=4cd209be346d8446ea04e2f71ce169be 2500w" />
       </Frame>
    3. Click on create intent to add the intent to the hierarchy
       <Frame>
         <img src="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-25ed51d7-0442-1d32-2277-23d33bb97d1b.png?fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=a34a688adc320d1bf3fe9d1de8c91719" data-og-width="576" width="576" data-og-height="406" height="406" data-path="image/uuid-25ed51d7-0442-1d32-2277-23d33bb97d1b.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-25ed51d7-0442-1d32-2277-23d33bb97d1b.png?w=280&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=63bad85ad56765b18b62fc07848cbdbe 280w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-25ed51d7-0442-1d32-2277-23d33bb97d1b.png?w=560&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=a9766de807196f4f2ee2d772d3c30996 560w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-25ed51d7-0442-1d32-2277-23d33bb97d1b.png?w=840&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=884cc3735024b1242ce43b4207447755 840w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-25ed51d7-0442-1d32-2277-23d33bb97d1b.png?w=1100&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=9b167deb522f4bcbb640e6258ac1a297 1100w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-25ed51d7-0442-1d32-2277-23d33bb97d1b.png?w=1650&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=b728eca375a95b07e4f367fe98e63339 1650w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-25ed51d7-0442-1d32-2277-23d33bb97d1b.png?w=2500&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=dee67adb2811461f9fab775891bdc23e 2500w" />
       </Frame>
    4. Review and verify your created intent
       <Frame>
         <img src="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c6d88a6d-8ed7-b081-15da-70d53ed004a6.png?fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=143377a1543512b11d487d8e65a70dd8" data-og-width="1558" width="1558" data-og-height="986" height="986" data-path="image/uuid-c6d88a6d-8ed7-b081-15da-70d53ed004a6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c6d88a6d-8ed7-b081-15da-70d53ed004a6.png?w=280&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=889a8941ffbe64b1fb0cb28086b46706 280w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c6d88a6d-8ed7-b081-15da-70d53ed004a6.png?w=560&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=3448f9a3c7ccdfdb3eb110af413786ba 560w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c6d88a6d-8ed7-b081-15da-70d53ed004a6.png?w=840&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=582fcc67ef406b3113eed2820f390356 840w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c6d88a6d-8ed7-b081-15da-70d53ed004a6.png?w=1100&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=2b249f9efc2ef045712436370623d048 1100w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c6d88a6d-8ed7-b081-15da-70d53ed004a6.png?w=1650&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=c8f0fbd79bef9471b0ec1d1af3959942 1650w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c6d88a6d-8ed7-b081-15da-70d53ed004a6.png?w=2500&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=3c98fab3f177153b49133cf2ea96a84c 2500w" />
       </Frame>

    ## FAQs

    * **What file formats are supported for uploading intents label hierarchy?**

      ASAPP's Intent Self-Serve tooling supports CSV and Excel file formats for uploading intents.

    * **Can I edit or update my intents hierarchy after uploading?**

      Yes, the tooling functionality allows you to edit or update your intents at any time after uploading them, ensuring you can refine and improve your intent classification as needed.

    * **Do I need to have technical expertise to use the Intent Self-Serve tooling?**

      No, intent front-end tooling is designed to be user-friendly, with no API configuration required. The intent labels can be easily uploaded, created, and managed without needing any technical assistance.
  </Accordion>
</Update>

<Update label="2024-03-01 - Structured Data">
  ## Structured Data

  Structured Data is a powerful, fully customizable feature for extracting customizable data points from conversations through:

  * **Entity extraction**: Automatically identifies key information like product names, dates, amounts, and more
  * **Question extraction**: Answers predefined questions about conversations (e.g., "Was the issue resolved?")

  The dynamic nature of Structured Data allows you to extract data for:

  * Generating automated insights and reports at scale
  * Populating CRM fields directly from conversations
  * Monitoring compliance and script adherence automatically
  * And more.

  <Card title="Structured Data" href="/ai-productivity/ai-summary/structured-data">
    Learn how to configure and manage Structured Data
  </Card>
</Update>

<Update label="2023-10-27 - Salesforce Integration">
  ## Salesforce Integration

  ASAPP's native [Salesforce plugin](/ai-productivity/ai-summary/salesforce-plugin) now includes AI Summary integration. This enables Salesforce administrators to quickly install and configure AI Summary within their Lightning environment.

  The low-code plugin allows administrators to deploy AI Summary in hours without complex integration work. Once enabled, the system automatically generates and saves conversation summaries to Salesforce records, eliminating the need for manual note-taking by agents.

  <Frame>
    <img src="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4973dbae-72a6-597a-2126-759bb3fb3df8.png?fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=230c82d989d946cbd8c937f40b58688d" data-og-width="1245" width="1245" data-og-height="517" height="517" data-path="image/uuid-4973dbae-72a6-597a-2126-759bb3fb3df8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4973dbae-72a6-597a-2126-759bb3fb3df8.png?w=280&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=88d3a5998dd03313abbe69bc6480385c 280w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4973dbae-72a6-597a-2126-759bb3fb3df8.png?w=560&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=a5814ac43e0a183c08ee75f25609e224 560w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4973dbae-72a6-597a-2126-759bb3fb3df8.png?w=840&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=74f9e37c6476af098e6f695e5d077ae7 840w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4973dbae-72a6-597a-2126-759bb3fb3df8.png?w=1100&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=9db808913e35bd83fe9ddf2205bcb21c 1100w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4973dbae-72a6-597a-2126-759bb3fb3df8.png?w=1650&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=f3056a4111c3109b47d0a4d66d48d534 1650w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4973dbae-72a6-597a-2126-759bb3fb3df8.png?w=2500&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=25ac0d3e02b70dbd9ea41ab535d299c8 2500w" />
  </Frame>

  <Note>
    AI Summary works seamlessly alongside ASAPP's AI Compose for Salesforce.
  </Note>

  <Accordion title="How It Works video">
    Watch the video below for an overview on AI Summary for Salesforce:

    <iframe width="560" height="315" allow="fullscreen *" src="https://fast.wistia.net/embed/iframe/4g7sfy7qg1" />
  </Accordion>
</Update>

<Update label="2023-10-18 - Free-Text and Feedback Feeds for AI Summary">
  ## Free-Text and Feedback Feeds for AI Summary

  ASAPP introduces two feeds to retrieve data for free-text summaries generated by AI Summary and edited versions of summaries submitted by agents as feedback.

  These two feeds enable administrators to retrieve AI Summary data using the [File Exporter API](/reporting/file-exporter):

  * **Free-text feed**: Retrieves data from free-text summaries generated by AI Summary.
    * This feed has one record per free-text summary produced and can have multiple summaries per conversation.
    * [Schema: autosummary\_free\_text](/reporting/fileexporter-feeds#table%3A-autosummary-free-text)
  * **Feedback feed**: Retrieves data from feedback summaries submitted by the agents.
    * This feed contains the text of the feedback submitted by the agent.
    * Developers can join this feed to the AI Summary free-text feed using the summary ID.
    * [Schema: autosummary\_feedback](/reporting/fileexporter-feeds#table%3A-autosummary-feedback)

  <Accordion title="How it works video">
    Watch the following video walkthrough to learn about the Free-Text and Feedback feeds:

    <iframe width="500" height="315" allow="fullscreen *" src="https://fast.wistia.net/embed/iframe/p7ejx6f8xv" />
  </Accordion>
</Update>

<Update label="2023-09-05 - Sandbox for AI Summary">
  ## Sandbox for AI Summary

  ASAPP introduces the AI Summary Sandbox, a testing environment in AI-Console that allows administrators to validate and experiment with summary generation before deploying to production. The Sandbox supports both voice and messaging conversations, letting users simulate interactions or upload existing transcripts to preview how AI Summary will perform.

  <Frame caption="AI Summary's intent and free-text summary generated in the Sandbox.">
    <img src="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-99bc91b0-52d7-1a3a-29fe-820195a57fac.png?fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=1da7132fb6e4cc5554f36713e58568ad" data-og-width="1981" width="1981" data-og-height="1228" height="1228" data-path="image/uuid-99bc91b0-52d7-1a3a-29fe-820195a57fac.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-99bc91b0-52d7-1a3a-29fe-820195a57fac.png?w=280&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=58a35811cfcfc090b61047b40c271503 280w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-99bc91b0-52d7-1a3a-29fe-820195a57fac.png?w=560&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=e684a55299b1e94cb1e460a75191663a 560w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-99bc91b0-52d7-1a3a-29fe-820195a57fac.png?w=840&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=41a024c1c5d2221d5539c5e8c95812de 840w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-99bc91b0-52d7-1a3a-29fe-820195a57fac.png?w=1100&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=4f7049f353d2b1c7e867357ebbb259ed 1100w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-99bc91b0-52d7-1a3a-29fe-820195a57fac.png?w=1650&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=d250493f08959f8ad9d7729119ef6462 1650w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-99bc91b0-52d7-1a3a-29fe-820195a57fac.png?w=2500&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=d3616c89dac9fc080f5808be3387f17c 2500w" />
  </Frame>

  The Sandbox starts with baseline contact center models and can be upgraded to use your custom-trained models once deployed. This allows teams to preview summary formatting and validate outputs throughout their implementation journey.

  <Note>
    Free-text summaries are always available, while intent and structured data require additional configuration.
  </Note>

  <Accordion title="How It Works video">
    Watch the following video walkthrough to learn how to use the AI Summary Sandbox:

    <iframe width="500" height="315" allow="fullscreen *" src="https://fast.wistia.net/embed/iframe/oqtyu0glyz" />
  </Accordion>
</Update>

<Update label="2023-02-08 - Feedback for AI Summary">
  AI Summary now supports model retraining using agent feedback. The [feedback endpoint](/apis/autosummary/provide-feedback) receives free-text paragraph summaries submitted by agents, and uses the difference between the automatically generated summary and the final submission to improve the model over time.

  <Frame>
    <img src="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-db6d12ed-a88a-17bb-5e75-afef51ab48df.png?fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=a40cfd4eccef2196a89d6dc9342692e2" data-og-width="1680" width="1680" data-og-height="889" height="889" data-path="image/uuid-db6d12ed-a88a-17bb-5e75-afef51ab48df.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-db6d12ed-a88a-17bb-5e75-afef51ab48df.png?w=280&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=6f9f12f790b4ccc723b5907691bc8932 280w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-db6d12ed-a88a-17bb-5e75-afef51ab48df.png?w=560&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=73ab83d024f4c329c8589b9b42d04827 560w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-db6d12ed-a88a-17bb-5e75-afef51ab48df.png?w=840&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=e41dfc48c368b08160a7db140268e555 840w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-db6d12ed-a88a-17bb-5e75-afef51ab48df.png?w=1100&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=3dc3121acf6587aa9dfbc821bd5d1ca4 1100w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-db6d12ed-a88a-17bb-5e75-afef51ab48df.png?w=1650&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=231cad142cf0dfb4b8ff6afcf322900b 1650w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-db6d12ed-a88a-17bb-5e75-afef51ab48df.png?w=2500&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=7ffbac324ce41ff20889c3c881a4c5b7 2500w" />
  </Frame>
</Update>
