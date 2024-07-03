import argparse

parser = argparse.ArgumentParser(description='Enter n, m')
parser.add_argument('n', type=int)
parser.add_argument('m', type=int)
args = parser.parse_args()

def generate_answer(left: int, right: int, arr: list) -> None:
    # danger case: left = n, right = 2n
    slice = arr[left : right]
    ans = ""

    while slice[len(slice) - 1] != arr[0]:
        ans += str(slice[0])

        left = (left + args.m - 1) % args.n
        right = (right + args.m - 1) % args.n
        
        if left >= right:
            slice = arr[left : args.n]
            slice += arr[:right]

        else:
            slice = arr[left : right]
    
    ans += str(slice[0])
    print(ans)


def main():
    # objective print arrays until first element is the last
    # n >= 1
    # m ? 
    arr = [(i+1) for i in range(args.n)]
    left = 0
    right = args.m

    while (right > args.n):
        right -= args.n

    generate_answer(left, right, arr)


if __name__ == "__main__":
    main()
