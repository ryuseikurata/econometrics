from god_step import getOutcome

b2_spec = 4

def isSpe(b2_spec):
    y_vector = getOutcome(b2_spec)
    only_y_vector = list(filter(lambda y: y > 0, y_vector))
    true_size = len(only_y_vector)
    if (true_size > 20 & true_size < 80):
        print('ok!!')
        print(true_size)
        return True
    else:
        print('More Challenge!!')
        print(true_size)
        return False
