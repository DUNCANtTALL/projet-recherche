import os
import re
import pandas as pd
from io import StringIO

ROOT_DIR = 'Etape3'
CSV_ROOT = 'Etape3_csv'

os.makedirs(CSV_ROOT, exist_ok=True)

HEADER = ['evaluation','fitness','best_fitness','measured_fitness','best_measured_fitness'] + [f'x{i}' for i in range(1,11)]

def convert_algo_folder(algo_folder, out_folder):
    os.makedirs(out_folder, exist_ok=True)
    for fname in os.listdir(algo_folder):
        if fname.endswith('.tdat'):
            in_path = os.path.join(algo_folder, fname)
            with open(in_path, 'r') as f:
                lines = [line for line in f if not line.startswith('%')]
            data_str = ''.join(lines)
            df = pd.read_csv(StringIO(data_str), sep=r'\s+', header=None, engine='python')
            df.columns = HEADER
            out_name = os.path.splitext(fname)[0] + '.csv'
            out_path = os.path.join(out_folder, out_name)
            df.to_csv(out_path, index=False)

def main():
    for algo in os.listdir(ROOT_DIR):
        algo_path = os.path.join(ROOT_DIR, algo)
        if os.path.isdir(algo_path):
            out_algo = os.path.join(CSV_ROOT, algo)
            convert_algo_folder(algo_path, out_algo)
    print(f'Conversion terminée. Fichiers CSV dans {CSV_ROOT}')

if __name__ == '__main__':
    main()
