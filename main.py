from database import create_tables, create_session, save_trial, get_trials_by_session
from experiment import run_single_trial
from analysis import analyze_session

def run_experiment():
    create_tables()
    
    session_id = create_session()
    print(f"\nSessão criada com ID: {session_id}")
    
    for trial in range(1, 21): # python exclui o último valor, garantindo 20 tentativas
        reaction_time = run_single_trial(trial)
        print(f"Tempo de reação: {reaction_time:.2f} ms")
        
        # cada tentativa é salva imediatamente
        save_trial(session_id, trial, reaction_time)
        
    print("\n>> Experimento finalizado!")
    
    # parte científica
    trials = get_trials_by_session(session_id)
    results = analyze_session(trials)
    
    print("\n=== RESULTADOS DA SESSÃO ===")
    print(f"Outliers removidos: {results['removed_outliers']}")
    print(f"Média: {results['mean']:.2f} ms")
    print(f"Desvio Padrão: {results['stdev']:.2f} ms")
    print(f"Variância: {results['variance']:.2f}")
    print(f"Minímo: {results['min']:.2f} ms")
    print(f"Máximo: {results['max']:.2f} ms")
        
if __name__ == "__main__":
    run_experiment()