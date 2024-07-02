import argparse

parser = argparse.ArgumentParser(description='Enter fpath1')
parser.add_argument('numbers', type=str)
args = parser.parse_args()

def main():
    nums = []

    with open(args.numbers, mode='r') as input:
        ln = input.readline()

        while ln:
            nums.append(int(ln))
            
            ln = input.readline()
        
    if len(nums) <= 1:
        print(0)

    nums = sorted(nums)
    median = nums[len(nums) // 2]

    print(sum(abs(num - median) for num in nums))
    

if __name__ == "__main__":
    main() 
