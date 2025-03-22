from random import choice, randint


def get_response(user_input: str) -> str:
    lowered = user_input.lower().strip()

    if user_input.startswith('hey bot'):
        if 'hello' in lowered or 'how are you' in lowered:
            return "Hello there!"
        elif lowered in 'how are you':
            return "Amazing thanks for asking"
        elif 'roll dice' in lowered:
            return f'You rolled {randint(1, 6)}'
        else:
            return choice(['I do not understand',
                           'What are you talking about',
                           'Do you mind repeating that'])
