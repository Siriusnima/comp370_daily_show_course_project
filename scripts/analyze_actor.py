import argparse
import csv

from comedic import is_comedic, read_actor_names



def main():
    """Print the names of comedic actors in the CSV file."""

    
    #Test run currently disabled
    #print('William Baldwin', is_comedic('Willian Baldwin'))
    #exit('test')
    

    parser = argparse.ArgumentParser(description="Find comedic actors in a CSV file.") #create an argument parser
    parser.add_argument('acting_csv', help="Path to the acting CSV file") #define the expected argument
    args = parser.parse_args() #read the argument and store to args     
    
    acting_names = read_actor_names(args.acting_csv)

    for name in acting_names:
        if is_comedic(name):
            print(name)
   

if __name__=="__main__":
    main()