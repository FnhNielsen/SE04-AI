A = 'A'
B = 'B'

environment = {
    A: 'Dirty',
    B: 'Dirty',
    'Current': A
}


def reflex_vacuum_agent(loc_st):
    if loc_st[1] == 'Dirty':
        return 'Suck'
    if loc_st[0] == A:
        return 'Right'
    if loc_st[0] == B:
        return 'Left'


def sensors():
    location = environment['Current']
    return location, environment[location]


def actuators(action):
    location = environment['Current']
    if action == 'Suck':
        environment[location] = 'Clean'
    elif action == 'Right' and location == A:
        environment['Current'] = B
    elif action == 'Left' and location == B:
        environment['Current'] = A


if __name__ == '__main__':
    n = 10
    print("{:20s}{:22s}".format('Current', 'New'))
    print('location\tstatus\taction\tlocation\tstatus')
    for i in range(1, n):
        (location, status) = sensors()
        print("{:12s}{:8s}".format(location, status), end='')
        action = reflex_vacuum_agent(sensors())
        actuators(action)
        (location, status) = sensors()
        print("{:8s}{:12s}{:8s}".format(action, location, status))