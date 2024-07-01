import argparse

parser = argparse.ArgumentParser(description='Enter fpath1, fpath2')
parser.add_argument('circle_file', type=str)
parser.add_argument('points_file', type=str)
args = parser.parse_args()


def main():
    x = 0
    y = 0
    radius = 0
    
    with (
        open(args.circle_file, mode='r') as circle,
        open(args.points_file, mode='r') as points
    ):
        (x, y) = map(float, circle.readline().split(' '))
        radius = float(circle.readline())

        point = points.readline().split()

        while point:
            # shift 
            p_x = float(point[0]) - x
            p_y = float(point[1]) - y
            
            # x ^ 2 + y ^ 2 = r ^ 2
            # on the circle
            if p_x**2 + p_y**2 == radius**2:
                print(0)

            # inside
            if p_x**2 + p_y**2 < radius**2:
                print(1)
            
            if p_x**2 + p_y**2 > radius**2:
                print(2)


            point = points.readline().split()


if __name__ == "__main__":
   main() 
