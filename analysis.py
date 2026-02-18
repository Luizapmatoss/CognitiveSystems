# módulo de análise

import statistics

def analyze_session(trials): 
    
    reaction_times = [trial[1] for trial in trials]
    
    # filtro de outliers
    filtered_times = [
        rt for rt in reaction_times
        if 100 <= rt <= 600
    ]
    
    removed = len(reaction_times) - len(filtered_times)
    
    if len(filtered_times) < 0:
        return {
            "mean": None,
            "stdev": None,
            "variance": None,
            "min": None,
            "max": None,
            "removed_outliers": removed
        }
    
    mean_rt = statistics.mean(filtered_times)
    stdev_rt = statistics.stdev(filtered_times)
    variance_rt = statistics.variance(filtered_times)
    min_rt = min(filtered_times)
    max_rt = max(filtered_times)
    
    return {
        "mean": mean_rt,
        "stdev": stdev_rt,
        "variance": variance_rt,
        "min": min_rt,
        "max": max_rt,
        "removed_outliers": removed
    }