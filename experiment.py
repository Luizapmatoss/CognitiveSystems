import time
import random

def run_single_trial(trial_number):
    print(f"\n> Tentativa {trial_number}")
    print("Prepare-se...")
    
    # espera aleatória entre 2 e 5 segundos
    delay = random.uniform(2, 5)
    time.sleep(delay)
    
    input("> AGORA! Pressione ENTER (2 vezes) o mais rápido possível!")
    
    start_time = time.perf_counter()
    input()
    end_time = time.perf_counter()
    
    reaction_time_ms = (end_time - start_time) * 1000
    
    return reaction_time_ms