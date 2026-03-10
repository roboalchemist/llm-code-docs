# We have to create a recipe using the same prompt template and GPT-3.5-turbo
recipe_gpt = quotient.create_recipe(
    model_id=5,
    prompt_template_id=1,
    name='gpt3.5-qa-with-rag-recipe-v1',
    description='GPT-3.5 using a prompt template that includes context.'
)

recipe_gpt

#Outputs
#{'id': 495,