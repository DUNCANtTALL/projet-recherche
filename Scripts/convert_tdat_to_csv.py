import os
import re
import pandas as pd
from io import StringIO

DATA_DIR = 'probleme'
CSV_DIR = 'csv_data'

os.makedirs(CSV_DIR, exist_ok=True)

def parse_filename(filename):
    match = re.match(r'bbobexp_f(\d+)_DIM(\d+)\.t?dat', filename)
    if match:
        return {
            'function': int(match.group(1)),
            'dimension': int(match.group(2))
        }
    return None

def convert_to_csv(filepath, outdir):
    with open(filepath, 'r') as f:
        lines = [line for line in f if not line.startswith('%')]
    data_str = ''.join(lines)
    df = pd.read_csv(StringIO(data_str), sep=r'\s+', header=None, engine='python')
    base = os.path.basename(filepath)
    csv_name = os.path.splitext(base)[0] + '.csv'
    outpath = os.path.join(outdir, csv_name)
    df.to_csv(outpath, index=False)
    return outpath

def main():
    for fname in os.listdir(DATA_DIR):
        if fname.endswith(('.tdat', '.dat')):
            path = os.path.join(DATA_DIR, fname)
            convert_to_csv(path, CSV_DIR)
    print(f'Conversion terminée. Fichiers CSV dans le dossier {CSV_DIR}')

if __name__ == '__main__':
    main()
