import csv
import os


url_in = os.path.join("PyPoll", "Resources","election_data.csv")
url_out = os.path.join("PyPoll","Analysis","result.txt")

def read():
     with open(url_in,mode='r') as datafile:
        data =csv.DictReader(datafile, delimiter=',')
        data_lines = [lines for lines in data]
        Total_votes = len(data_lines)
        return(data_lines,Total_votes)
get_data,Tot_votes = read()
winner_dict = {}
def check_data(data,names):
    count = 0
    for lines in data:
        if(lines["Candidate"] == names):
            count += 1
            winner_dict[names] = count
    avg = round(count/Tot_votes*100,2)
    return lambda name: (f"{name}: {avg}% ({count})\n")



def display_res():
    dec1 = "\n"+("--"*15)+"\n"
   
    
    Results_text = f"Election Results {dec1}"
    votes = f"Total Votes: {Tot_votes} {dec1}"
    
    Result_Khan = check_data(get_data,"Khan")("Khan")
    Result_Correy = check_data(get_data,"Correy")("Correy")
    Result_Li = check_data(get_data,"Li")("Li")
    Result_Tooley = check_data(get_data,"O'Tooley")("O'Tooley")
    max_key = max(winner_dict, key=winner_dict.get)
    pmax_key = f"Winner: {max_key}{dec1}"
    text_out = [Results_text,votes,Result_Khan,Result_Correy,Result_Li,Result_Tooley,dec1,pmax_key]
    with open(url_out,'w') as out_file:
        out_file.writelines(text_out)

if __name__ == "__main__":
    display_res()

