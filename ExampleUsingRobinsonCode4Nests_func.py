import numpy as np
import PlotSummaryDataRobinson as psdr
import OutputRobinsonDataExcel as orde
import RobinsonCode as rc
# import matplotlib.pyplot as plt

max_Visited = []

# ExampleUsingRobinsonCodeNew
def runIt(threshold_mean):
    # this sets the name of the output file. It stores the data for each of
    # your tests so you'll need to call it something that indicates what
    # experiment it is
    # output_file='RobinsonTestExperimentTest1.mat'
    output_file_xls = 'RobinsonTestExperimentTest3.xlsx'
    


    # these parameters are for the first experiment

    # the following parameters are for different geographical positions of the nests
    # probabilities of visiting each site from each other
    probs = np.array([[0.76, 0.10, 0.09, 0.05], [0.10, 0.82, 0.05, 0.03], [0.09, 0.05, 0.82, 0.1], [0.05, 0.03, 0.1, 0.82]])
    

    # mean time to get between each nest
    time_means = np.array([[1, 36, 46, 56], [46, 1, 30, 40], [46, 30, 1 , 20], [56, 40, 20, 1]])
    # standard deviation of time to get between each nest
    time_stddevs = time_means / 5



    # mean quality of each nest. Note home is -infinity so it never gets picked
    quals = np.array([-np.inf, 3, 4, 6])

    # standard deviation of quality: essentially this controls
    # how variable the ants assessment of each nest is. This is currently set
    # as in the 1st experiment where the variability is the same for each nest
    qual_stddev = np.array([1, 1, 1, 1])
    
    # However, if you want to change is so nests perceived w different accuracy
    # you could do eg qual_stddev = [1, 1, 4]
    
    # the following changes in variability to the poor nest
    # qual_stddev = np.array([1, 2, 1, 1])
    # qual_stddev = np.array([1, 3, 1, 1])
    # qual_stddev = np.array([1, 4, 1, 1])
    
    # the following changes in variability to the mediocre nest
    # qual_stddev = np.array([1, 1, 2, 1])
    # qual_stddev = np.array([1, 1, 3, 1])
    # qual_stddev = np.array([1, 1, 4, 1])
    
    # the following changes in variability to the good nest
    # qual_stddev = np.array([1, 1, 1, 2])
    # qual_stddev = np.array([1, 1, 1, 3])
    # qual_stddev = np.array([1, 1, 1, 4])
    
    # the following changes in variability to the poor nest and the mediocre nest
    # qual_stddev = np.array([1, 3, 2, 1])

    


    # set the number of ants
    n = 30

    # these govern the ant's threshold
    # threshold_mean = 6
    threshold_stddev = 1
    
    # threshold_stddev = 2
    # threshold_stddev = 3
    # threshold_stddev = 4

    current_time, discovers, visits, accepts, Ants, rnd_seed, preqtimes, preqdiscovers, preqvisits, preqaccepts = \
    rc.RobinsonCode(n, quals, probs, threshold_mean, threshold_stddev, qual_stddev, time_means, time_stddevs, [], [])

    # note: I have changed the order of saving data and plotting, as the matplotlib figure was blocking execution as long
    # as it was open

    max_Visited.append(np.bincount(accepts).argmax())

    # save the data as matlab variables - NOT IMPLEMENTED IN PYTHON
    # save(output_file)
    # save some of the data as excel
    orde.OutputRobinsonDataExcel(output_file_xls, Ants, current_time, accepts, discovers, visits)


    # Plot Summary data
    psdr.PlotSummaryDataRobinson(current_time, accepts, discovers, visits, Ants)



# We run the simulation 10 times; 10 trials
for b in range(10):
    Y = runIt(6)
    # store.append(Y)

# this gives us the most visited sites across the 10 trials, a list of 10 values
print(max_Visited)


# x_val = [x[0] for x in store]
# y_val = [x[1] for x in store]

# plt.plot(x_val,y_val)
# plt.plot(x_val,y_val,'or')
# plt.show()