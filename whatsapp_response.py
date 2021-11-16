def response(input_message):
    message = input_message.lower()

    if message == 'nice':
        return 'Very nice.'
    elif message == 'hello there':
        return 'General Kenobi!'
    else:
        return 'Cool!'
