import re 
camel = 'HelloWorld'
snake = re.sub(r"([A-Z])", r" \1", camel)
snake = snake.lower()
snake = snake.strip()
snake = re.sub(r'\s', '_', snake)
print(snake)