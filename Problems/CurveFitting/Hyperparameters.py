IS_MAXIMIZATION = False            # Is this a maximization problem? 

DO_PARALLEL = True                 # Execute individual evaluation's process in parallel 

POP_SIZE = 250                     # population size
GENERATIONS = 200                   # maximal number of generations to run evolution
TOURNAMENT_SIZE = POP_SIZE//5      # size of tournament for tournament selection
ELITES_SIZE = POP_SIZE//10         # number of best individuals to keep to apply elitisim

STOP_ON_UNCHANGED = GENERATIONS    # number of iterations to stop which a little change has made to the best fitness value
STOP_ON_UNCHANGED_TOLERANCE = 0.5  # stop if the SSE value of the best fitness values of STOP_ON_UNCHANGED generations remain almost unchanged by this tolerance
STOP_ON_TOLERANCE = 0.1            # stop if the best fitness value crosses this value (this also takes IS_MAXIMIZATION in to the account)

MAX_DEPTH = 6                      # maximum tree depth

PROB_MUTATION = 0.2                # per-node mutation probability
PROB_CROSSOVER = 0.9               # crossover rate
PROB_PERMUTATION = 0.1             # permutation on terminals