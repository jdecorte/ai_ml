# Monte-Carlo simulatie van schakeling met vier condensatoren in serie. 
# Gezocht: frequentieverdeling van hoogste spanning over een condensator
# (meer bepaald: percentage dat hoger is dan 2.7 V)

# C<13.5 en C>19.5 wordt verwijderd

import sys
import numpy as np

# parameters
condensators = 4
avg = 15.9
sigma = 0.4985
samplesize = 100000
V_tot = 10.6
threshold = 2.7

def MaxVoltage(C,V_tot): 
    nominator = 0.0
    for c in C:
        nominator += 1/c

    C_tot =  1/nominator
    V = [C_tot/c * V_tot for c in C]
    return max(V)

def main(argv):
    samples = np.random.normal(loc=avg,scale=sigma,size=(samplesize,condensators))
    n = 0
    V_max = np.empty((0),dtype=float)
    for sample in samples:

        if (min(sample) >= 13.5) & (max(sample) <= 19.5):
            n += 1
            V_max = np.r_[V_max,[MaxVoltage(sample,V_tot)]]
        else:
            print(min(sample),max(sample))

    V_max = np.sort(V_max)    

    # V_max_threshold = [V_max > threshold]

    print(f'Totaal aantal samples van {condensators} condensatoren weerhouden: {n}')

    print(f'Percentage above threshold: {(V_max > threshold).sum()*100/n} %')
    # print(V_max)

    return    

if __name__ == "__main__":
   main(sys.argv[1:])




