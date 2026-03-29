import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

CSV_ROOT = 'Etape3_csv'
RESULTS_DIR = 'Etape3_results'
os.makedirs(RESULTS_DIR, exist_ok=True)

ALGOS = ['Poems', 'Pso', 'RandomSearch']
PROBLEMS = [f'bbobexp_f{i}_DIM10.csv' for i in range(1, 6)]

all_stats = []

for problem in PROBLEMS:
    plt.figure(figsize=(10, 6))
    for algo in ALGOS:
        csv_path = os.path.join(CSV_ROOT, algo, problem)
        if not os.path.exists(csv_path):
            continue
        df = pd.read_csv(csv_path)
        # Statistiques descriptives pour ce couple algo/problème
        stats = {
            'algo': algo,
            'problem': problem,
            'mean': df['fitness'].mean(),
            'median': df['fitness'].median(),
            'std': df['fitness'].std(),
            'min': df['fitness'].min(),
            'max': df['fitness'].max()
        }
        all_stats.append(stats)
        # Courbe de convergence
        plt.plot(df['evaluation'], df['fitness'], label=algo)
    plt.xlabel('Évaluation')
    plt.ylabel('Fitness')
    plt.title(f'Convergence - {problem.replace(".csv","")}')
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(RESULTS_DIR, f'convergence_{problem.replace(".csv","")}.png'))
    plt.close()

# DataFrame des stats comparatives
stats_df = pd.DataFrame(all_stats)
stats_df.to_csv(os.path.join(RESULTS_DIR, 'comparative_stats.csv'), index=False)

# Boxplot comparatif par problème
for problem in PROBLEMS:
    plt.figure(figsize=(10, 6))
    data = []
    labels = []
    for algo in ALGOS:
        csv_path = os.path.join(CSV_ROOT, algo, problem)
        if not os.path.exists(csv_path):
            continue
        df = pd.read_csv(csv_path)
        data.append(df['fitness'])
        labels.append(algo)
    if data:
        sns.boxplot(data=data)
        plt.xticks(ticks=range(len(labels)), labels=labels)
        plt.title(f'Boxplot Fitness - {problem.replace(".csv","")}')
        plt.ylabel('Fitness')
        plt.savefig(os.path.join(RESULTS_DIR, f'boxplot_{problem.replace(".csv","")}.png'))
        plt.close()

print('Analyse comparative terminée. Résultats dans le dossier Etape3_results.')
