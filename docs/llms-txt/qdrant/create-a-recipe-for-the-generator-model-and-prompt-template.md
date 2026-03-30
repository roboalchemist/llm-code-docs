# Create a recipe for the generator model and prompt template
recipe_mistral = quotient.create_recipe(
    model_id=10,
    prompt_template_id=1,
    name='mistral-7b-instruct-qa-with-rag',
    description='Mistral-7b-instruct using a prompt template that includes context.'
)
recipe_mistral

#Outputs recipe JSON with the used prompt template
#'prompt_template': {'id': 1,