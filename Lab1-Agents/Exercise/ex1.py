A = 'A'
B = 'B'

percepts = []

table = {
    ((A, 'Clean'),): 'Right',
    ((A, 'Dirty'),): 'Suck',
    ((B, 'Clean'),): 'Left',
    ((B, 'Dirty'),): 'Suck',
    ((A, 'Clean'), (A, 'Clean')): 'Right',
    ((A, 'Clean'), (A, 'Dirty')): 'Suck',

    ((A, 'Clean'), (A, 'Clean'), (A, 'Clean')): 'Right',
    ((A, 'Clean'), (A, 'Clean'), (A, 'Dirty')): 'Suck',
    ((A, 'Clean'), (A, 'Dirty'), (B, 'Clean')): 'Left',
}


def lookup(percepts, table):
    return table.get(tuple(percepts))


def table_driven_agent(percept):
    percepts.append(percept)
    return lookup(percepts, table)

if __name__ == "__main__":
    print('Action\tPercepts')
    print(table_driven_agent((A, 'Clean')), '\t', percepts)
    print(table_driven_agent((A, 'Dirty')), '\t', percepts)
    print(table_driven_agent((B, 'Clean')), '\t', percepts)