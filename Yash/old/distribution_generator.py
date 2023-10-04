# We have n bits (the user can choose n), every bits have two state
# The goal of this program is to attribute to every state x of the n bits string a probability
# and calculate the entropy of this distribution as Entropy = - sum D(x)*log(D(x))

# Imput = the user choose n the number of bit

# Output = a text file with the states, their probabilities and entropy of the distrivution 

import numpy as np
import scipy.stats as stats

n = 10 # number of states

def generate_states(n):
    states = []
    for i in range(pow(2,n)):
        states.append(np.binary_repr(i).zfill(n))
    return(states)

def generate_distribution(n):
    distribution = np.random.rand(pow(2,n))
    distribution /= np.sum(distribution)
    return(distribution)

states = generate_states(n)
distribution = generate_distribution(n)
# distribution = generate_distribution_with_entropy(n, desired_entropy)
entropy = -np.sum(distribution * np.log(distribution))


# Create and write to the text file
with open('output.txt', 'w') as file:
    file.write("Entropy: ")
    file.write(f"{entropy}\n")
    for i in range(len(states)):
        line = f"{states[i]}, {distribution[i]}\n"
        file.write(line)

print("File 'output.txt' has been created.")

# Bonus: choose the entropy and generate a corresponding distribution cf: generates_distributions_with_desired_entropy.ipynb



