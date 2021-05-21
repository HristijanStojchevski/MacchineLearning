def get_letter_data():
    with open('letter-recognition.data') as data:
        lines = data.readlines()
    instances = [instance[:-1].split(',') for instance in lines]
    return instances[:len((instances*2)/3)], instances[len((instances*2)/3):]
