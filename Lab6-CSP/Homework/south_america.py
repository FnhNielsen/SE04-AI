from random import shuffle


class CSP:
    def __init__(self, variables, domains, neighbours, constraints):
        self.variables = variables
        self.domains = domains
        self.neighbours = neighbours
        self.constraints = constraints

    def backtracking_search(self):
        return self.recursive_backtracking({})

    def recursive_backtracking(self, assignment):
        if self.is_complete(assignment):
            return assignment
        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment):
            if self.is_consistent(var, value, assignment):
                assignment[var] = value
                result = self.recursive_backtracking(assignment)
                if result is not None:
                    return result
        return None

    def select_unassigned_variable(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return variable

    def is_complete(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return False
        return True

    def order_domain_values(self, variable, assignment):
        all_values = self.domains[variable][:]
        # shuffle(all_values)
        return all_values

    def is_consistent(self, variable, value, assignment):
        if not assignment:
            return True

        for constraint in self.constraints.values():
            for neighbour in self.neighbours[variable]:
                if neighbour not in assignment:
                    continue

                neighbour_value = assignment[neighbour]
                if not constraint(variable, value, neighbour, neighbour_value):
                    return False
        return True


def create_south_america_csp():
    # French Guyana is FR
    co, ve, gu, su, fr, ec, pe, br, bo, ch, pa, ar, ur = 'CO', 'VE', 'GU', 'SU', 'FR', 'EC', 'PE', 'BR', 'BO', 'CH', 'PA', 'AR', 'UR'

    values = ['Red', 'Green', 'Blue', 'Yellow']
    variables = [co, ve, gu, su, fr, ec, pe, br, bo, ch, pa, ar, ur]
    domains = {
        co: values[:],
        ve: values[:],
        gu: values[:],
        su: values[:],
        fr: values[:],
        ec: values[:],
        pe: values[:],
        br: values[:],
        bo: values[:],
        ch: values[:],
        pa: values[:],
        ar: values[:],
        ur: values[:]
    }
    neighbours = {
        co: [ve, br, ec, pe],
        ve: [co, gu, br],
        gu: [ve, su, br],
        su: [gu, fr, br],
        fr: [su, br],
        ec: [co, pe],
        pe: [co, ec, br, bo, ch],
        br: [co, ve, gu, su, fr, pe, bo, pa, ar, ur],
        bo: [pe, br, ch, ar, pa],
        ch: [pe, bo, ar],
        ar: [br, bo, ch, pa, ur],
        pa: [bo, br, ar],
        ur: [br, ar]
    }

    def constraint_function(first_variable, first_value, second_variable, second_value):
        return first_value != second_value

    constraints = {
        co: constraint_function,
        ve: constraint_function,
        gu: constraint_function,
        su: constraint_function,
        fr: constraint_function,
        ec: constraint_function,
        pe: constraint_function,
        br: constraint_function,
        bo: constraint_function,
        ch: constraint_function,
        pa: constraint_function,
        ar: constraint_function,
        ur: constraint_function
    }

    return CSP(variables, domains, neighbours, constraints)

if __name__ == '__main__':
    south_america = create_south_america_csp()
    result = south_america.backtracking_search()
    for area, color in sorted(result.items()):
        print("{}: {}".format(area, color))

    # Check at https://mapchart.net/australia.html