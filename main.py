
def machine_epsilon(eps):
    # taking a floating type variable
    # run until condition satisfy
    prev_epsilon = 0
    while ((1 + eps) != 1):
        # copying value of epsilon
        # into previous epsilon
        prev_epsilon = eps

        # dividing epsilon by 2
        eps = eps / 2

    # print output of the program
    return prev_epsilon


print(abs(3.0 * ((machine_epsilon(4.0/3.0))-1)-1))

