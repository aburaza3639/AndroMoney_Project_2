from AndroMoney import andro_control
import sys
"""
parser = argparse.ArgumentParser(description='Input money diary')
parser.add_argument('start', metavar="start", type=str, help='start date of money diary input')
parser.add_argument('end', metavar="end", type=str, help='end date of money diary input')
args = parser.parse_args()
start_date = args.start
end_date = args.end
"""
try:
    args = sys.argv
    if args[1].isdigit():
        if args[2].isdigit():
            start_date = args[1]
            end_date = args[2]
except:
    start_date = "20251101"
    end_date = "20251130"

def func(start_date, end_date):

    andro_control.start_andro(start_date, end_date)


if __name__ == '__main__':
    func(start_date, end_date)