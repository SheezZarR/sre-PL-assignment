import argparse
import copy 
import json

parser = argparse.ArgumentParser(description='Enter fpath1, fpath2, fpath3')
parser.add_argument('values_json', type=str)
parser.add_argument('tests_json', type=str)
parser.add_argument('report_json', type=str)
args = parser.parse_args()


# mad scientist solution
def mad_science():
    # parse a single line and find id and the number 
    # then store it before upcoming value
    # then write the value directly from the source
    # if it is not the id line then copy the whole thing to the source
    vals = []

    with open(args.values_json, mode='r') as input:
        temp = json.load(input)
        vals = temp.get('values')
    
    print(len(vals))

    def find_value(lookup_id: int) -> str:
        for dikt in vals:
            if dikt.get('id') == lookup_id:
                return dikt.get('value')

        return "ERROR"


    iters = 0

    upcoming_id = 0

    with (
        open(args.tests_json, mode='r') as source,
        open(args.report_json, mode='w') as target
    ):
        
        test_line = source.readline()
        
        while test_line:
            
            try: 
                id_start = test_line.index('id')
                upcoming_id = int(test_line[id_start + 5:].split(',')[0])
                print(f'id line: {repr(test_line)}, {id_start = }') 
            except ValueError:
                pass

            try:
                test_line.index('value')
                line_copy = copy.deepcopy(test_line)
                empty_start = line_copy.index('""')
                test_line = line_copy[:empty_start + 1] + find_value(upcoming_id) + line_copy[empty_start + 1:]
                
            except ValueError:
                pass

            target.write(test_line)

            test_line = source.readline()
        



def main():
    mad_science()
    # potential problem -> loading a file that is too large?? 
    # if using naive approach
    


if __name__ == "__main__":
    main()
