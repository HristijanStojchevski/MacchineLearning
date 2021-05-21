def get_bumps_data():
    with open('seismic-bumps.csv') as data:
        lines = data.readlines()
        # print(lines)
    instances = [instance[:-1].split(',') for instance in lines]
    print(instances)
    return instances

