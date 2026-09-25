# Experiment 1: Time vs length of push-only sequence
# In this experiment, you study the total running time (of the max-heap and the above array $A$, 
# respectively) vs the lengths $L$ of sequences consisting of push operations only. Specifically, 
# you first generate five push-only sequences s1, s2, ..., s5 respectively with 
# length L = 0.1M, 0.2M, 0.5M, 0.8M, 1M, where $M$ stands for one million, i.e., 10^6.
# Then you input the same s1, ..., s5 to each of the max-heap and the array A.
from datetime import datetime
from generator import gen_element, gen_push, gen_pop, write_to_file
import max_heap
import competitor


def experiment_1_generate():
    data = []
    
    # do your work
    # loop through and generate the data -> store in a list/array (ie data)

    # write the number of lines as first element of list/array (ie data)
    data.insert(0, 10) # example size - this will put 10 in the first element

    # pick either of the output file name options.
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    outputfilename = "./experiment_1_data" # example one - manual naming 
    outputfilename = f"./data_{len(data)}_{timestamp}.out" # example 2 - automatic naming - replace 'data' with the generated array
    write_to_file(outputfilename, data)

def experiment_1_run():
    # read the file s1-s5
    # start a timer
    # run the max heap 
    # stop the timer
    # start the timer
    # run against competitor
    # stop the timer
    # write the results to output file or to screen
    # you can use code from max heap and competitor as:
    # max_heap.push(), competitor.push(), max_heap.pop(), competitor...
    pass # remove this line when code is setup


#
# This is the part that is actually necessary for you to run this speciific python code 
# Technically we don't need to use this structure but it keeps it simple for you to say
# This is the start.
# you can leave this block alone and just update the generate/run section.
# you can also then clone this structure for other experiments
#
if __name__ == "__main__":
    experiment_1_generate()
    experiment_1_run()
