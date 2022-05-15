#Dependencies
import os
import csv

def print_results(final_list, all_votes):
    winner = ''
    winner_count = 0
    print("Election Results")
    print("-------------------------")
    print (f'Total votes: {"{:,}".format(all_votes)}')
    print("-------------------------")

    for i in final_list :

        print (f'{i}: {"{:.3%}".format(round(final_list[i]/total_votes,1))} ({"{:,}".format(final_list[i])})')

        if  final_list[i] > winner_count:
            winner_count = final_list[i] 
            winner = {i}

    print("-------------------------")
    print (f'Winner: {winner}')
    print("-------------------------")

def print_results_to_csv(final_list, all_votes):
    winner = ''
    winner_count = 0

    output_file = os.path.join("..", "PyPoll\Resources", "election_summary.csv")  

    with open(output_file, "w") as summary_file:
        writer = csv.writer(summary_file)

        writer.writerow(["Election Results"])
        writer.writerow(["-------------------------"])
        writer.writerow([f'Total votes: {"{:,}".format(all_votes)}'])
        writer.writerow(["-------------------------"])

        for i in final_list :

            writer.writerow([f'{i}: {"{:.3%}".format(round(final_list[i]/total_votes,1))} ({"{:,}".format(final_list[i])})'])

            if  final_list[i] > winner_count:
                winner_count = final_list[i] 
                winner = {i}

        writer.writerow(["-------------------------"])
        writer.writerow ([f'Winner: {winner}'])
        writer.writerow(["-------------------------"])

# initialize variables

total_votes = 0
candidate_dict = {}

# set path

PyPoll_csv = os.path.join("..","PyPoll\Resources", "election_data_small.csv")

# Read file

with open(PyPoll_csv, encoding = "utf-8") as csv_file:
    csv_pypoll_reader = csv.reader(csv_file, delimiter=",")

    header = next(csv_pypoll_reader)

    for row in csv_pypoll_reader:
        total_votes = total_votes + 1

        if row[2] not in candidate_dict.keys():            
            candidate_dict[row[2]] = 1
        else:

            candidate_dict[row[2]] += 1


print_results(candidate_dict, total_votes)

print_results_to_csv(candidate_dict, total_votes)

           
            



    










