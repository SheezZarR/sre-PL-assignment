import argparse
import json

parser = argparse.ArgumentParser(description='Enter fpath1, fpath2, fpath3')
parser.add_argument('values_json', type=str)
parser.add_argument('tests_json', type=str)
parser.add_argument('report_json', type=str)
args = parser.parse_args()


def walk(tests: dict, meta_data: dict):
    if tests.get('values'):
        for val in tests.get('values'):
            walk(val, meta_data)
    
    if 'value' in tests.keys():
        tests['value'] = meta_data.get(tests['id'])



def main():
    test_data = []
    vals = {}
    
    # load
    with (
        open(args.tests_json, 'r') as f,
        open(args.values_json, 'r') as f2
    ):
        test_data = json.load(f)
        
        if isinstance(test_data, dict):
            test_data = test_data.get('tests')

        temp = json.load(f2).get('values')
        
        for dikt in temp:
            vals[dikt.get('id')] = dikt.get('value')

    # we walk until there are no empty values left
    for test_case in test_data:
        walk(test_case, vals)

    # make the report
    with open(args.report_json, 'w') as report:
        json.dump({'tests': test_data}, report, indent=2)
    
    

if __name__ == "__main__":
    main()
