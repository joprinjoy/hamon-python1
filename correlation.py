from sys import argv
import json
from math import sqrt

events = []
script, filename = argv


def load_journal():
    with open(filename,'r') as file:
        journal_data = json.load(file)
    return journal_data   

#calling load  function ,runs compute phi function and returns dictionary with events and its correlation   
def compute_correlations():
    
    #calling the load function which loads the json file and return its data as a list
    journal = load_journal() 

    #picking each events and append ti a list
    for outer_dict in journal:
        for i in outer_dict['events']:
            events.append(i)

    #converting the list to set for removing duplicate values
    uniq_events = set(events)

    #calling compute_phi function and storing its returned value into variable
    result_compute_phi = compute_phi(uniq_events,journal) 
    #returning the result of compute phi  
    return result_compute_phi

"""function to calculate the correlation of each event , it has two arguments which are 
unique_events and journal which is data of json file """

def compute_phi(uniq_events,journal):
        #expecting a dict of events and its count
        corelation_event_dict = {}
        #itering through every unique event
        for event in uniq_events:
            #4 variables to store the count to excute the formula
            n00 = 0
            n11 = 0
            n01 = 0
            n10 = 0  
            
            #itering through the parsed json files to match the events 
            for entry in journal: 
                #checking weather unique event present in every dict of json file and weather he turned squirrell or not
                if event in entry['events'] and entry['squirrel']:
                    #if yes n11 will incremented by 1
                    n11 = n11 + 1
                elif event in entry['events'] and not entry['squirrel']:
                    n10 = n10 + 1
                elif event not in entry['events'] and not entry['squirrel']:
                    n00 = n00 + 1
                elif event not in entry['events'] and entry['squirrel']:
                    n01 = n01 + 1 
            #for the formula 
            #(n11*n00*-n10*n01)/sqrt(n1+ * n0+ * n+1 * n+0)
            n1plus = n11 + n10
            n0plus = n01 + n00
            nplus0 = n00 + n10
            nplus1 = n11 + n01 
            #to avaoid devision by 0 ,calculating the dinominator first and make sure it is not 0
            denominator = sqrt(n1plus * n0plus * nplus1 * nplus0)
            if denominator == 0:
                correlation_event = 0
            else:
                correlation_event = (n11 * n00 - n10 * n01) / denominator
            #appending all the events and its correlation to a dict
            corelation_event_dict[event] = correlation_event
        #returning the value
        return corelation_event_dict


#recieves a dictionary with all unique events as keys and its count as value return by compute_correlation function
def diagnose():
    events_corelation = compute_correlations()
    #taking the first key of dict 
    first_key = next(iter(events_corelation))
    max_value =events_corelation[first_key] 
    min_value =events_corelation[first_key]    
    max_item = first_key
    min_item = first_key

    #itering through the dict to compare all events
    for item in events_corelation:
        #findinf the maximum value
        if events_corelation[item] > max_value:
             max_value = events_corelation[item]
             max_item = item
    #finding the minimum value
        if events_corelation[item] < min_value:
            min_value = events_corelation[item]
            min_item = item

    print(f"The most correlated event is : { max_item} and the value is : {max_value}")
    
    print(f"The least correlated event is : {min_value} and the value is : {min_item}")

    print(f"\nThe  most adviced event is : {min_item}")


#runs from here
if __name__=="__main__":
   diagnose()
