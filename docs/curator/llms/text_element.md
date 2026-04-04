# Source: https://docs.curator.interworks.com/site_content_design/pages/text_element.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Text Element

> WYSIWYG text elements for adding formatted text, links, and images to your Curator pages.

## Adding a Text Element

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Content** > **Pages** section from the left-hand menu.
3. Find the page you want to add your form to from the Pages list or click "New Page" to create a new page.
4. Add a new element to your page, and when the modal pops-up select the "Text" option.
   <img src="https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/site_content_design/pages/add_text_element.png?fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=b094f6dfe54c0ab4a7725a62ed0dc419" alt="Curator Text element" data-og-width="930" width="930" data-og-height="917" height="917" data-path="assets/images/site_content_design/pages/add_text_element.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/site_content_design/pages/add_text_element.png?w=280&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=3684ea8967bbd647b1ad1929d7ac30bb 280w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/site_content_design/pages/add_text_element.png?w=560&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=1336b386cc00eeca648f1e9556b7f314 560w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/site_content_design/pages/add_text_element.png?w=840&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=21949408f05416a7356ad1af717bae2b 840w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/site_content_design/pages/add_text_element.png?w=1100&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=cb687c9f0dabb4d03a2e0a495af76dc3 1100w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/site_content_design/pages/add_text_element.png?w=1650&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=58d32dcb99171c898ebb3bad71793144 1650w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/site_content_design/pages/add_text_element.png?w=2500&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=9ec6d2cf93b1a938b5cb6512afce8e20 2500w" />
5. You will then be prompted with the WYSIWYG editor, where you can add and format your text, add links, and images.
   <img src="https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/site_content_design/pages/add_text_to_text_element.png?fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=2101721bf2151b6c53123135a9faebbe" alt="Curator Text element" data-og-width="958" width="958" data-og-height="610" height="610" data-path="assets/images/site_content_design/pages/add_text_to_text_element.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/site_content_design/pages/add_text_to_text_element.png?w=280&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=8533fc4eee67b0f6e96ed488bb61eb4a 280w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/site_content_design/pages/add_text_to_text_element.png?w=560&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=909669dc15b40379114c189eb3ec0c58 560w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/site_content_design/pages/add_text_to_text_element.png?w=840&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=d5004c41363cd6805faac5e4d8b85319 840w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/site_content_design/pages/add_text_to_text_element.png?w=1100&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=8805b4fa5b842e46fd40bb788e7ad5f9 1100w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/site_content_design/pages/add_text_to_text_element.png?w=1650&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=7642ae6477ebcc32409a2bf6b433efd9 1650w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/site_content_design/pages/add_text_to_text_element.png?w=2500&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=1f17f8cff69a7041a8e5ca1484d29f14 2500w" />

## Page Variables

Page variables can be used to display important user or session based information on pages.

* `{{ full_name }}` : Displays the full name for the logged in user
* `{{ first_name }}` : Displays the first name for the logged in user
* `{{ last_name }}` : Displays the last name for the logged in user
* `{{ username }}` : Displays the Curator username for the logged in user
* `{{ original_username }}` : Displays the original username for the logged in user
