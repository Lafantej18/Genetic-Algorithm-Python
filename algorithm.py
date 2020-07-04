import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-ch', '--ilosc_ch', help="ilość chromosomów", type=int, nargs='?', default=6, required=False)
parser.add_argument('-pm', '--ilosc_pm', help="wwspółczynnik mutacji", type=float, default=0.2, required=False)
parser.add_argument('-pk', '--ilosc_pk', help="współczynnik krzyżowania", type=float, default=0.8, required=False)
parser.add_argument('-i', '--ilosc_i', help="maksymalna ilość iteracji", type=int, default=1000, required=False)
parser.add_argument('-f', '--ilosc_f', help="funkcja", default="1,0", required=False)

args = parser.parse_args()
ch = args.ilosc_ch
pm = args.ilosc_pm
pk = args.ilosc_pk
i_max = args.ilosc_i
f =  args.ilosc_f
