context = "you are a rock star"
question = "what is your favourite song"
question_template = """answer the question {question} based on this context {context}"""
formatted_template = question_template.format(question=question, context=context)
print(formatted_template)