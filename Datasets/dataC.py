def get_iris_data():
    with open('iris.data') as data:
        lines = data.readlines()
    instances = [instance[:-1].split(',') for instance in lines]
    return instances
