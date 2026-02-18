import sqlite3

def create_connection():
    conn = sqlite3.connect("cognitive_data.db") # cria ou abre o arquivo "cognitive_data.db"
    return conn

def create_tables():
    conn = create_connection()
    cursor = conn.cursor() # objeto que executa comando SQL
    
    print("> Criando tabela sessions...")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sessions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    print("> Criando tabela trials...")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS trials (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id INTEGER,
        trial_number INTEGER,
        reaction_time_ms REAL,
        FOREIGN KEY(session_id) REFERENCES sessions(id)
    )
    """)
    
    conn.commit()
    conn.close()
    
def create_session():
    conn = create_connection()
    cursor = conn.cursor()
    
    # cria uma nova sessão usando os valores padrão da tabela
    cursor.execute("INSERT INTO sessions DEFAULT VALUES")
    conn.commit()
    
    session_id = cursor.lastrowid
    conn.close()
    
    return session_id

def save_trial(session_id, trial_number, reaction_time):
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
    INSERT INTO trials (session_id, trial_number, reaction_time_ms)
    VALUES (?, ?, ?) 
    """, (session_id, trial_number, reaction_time))
    
    conn.commit()
    conn.close() 

if __name__ == "__main__":
    create_tables()
    print("> Banco e tabelas criados com sucesso")
    
# buscar dados da sessão
def get_trials_by_session(session_id):
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
    SELECT trial_number, reaction_time_ms
    FROM trials
    WHERE session_id = ?
    ORDER BY trial_number
    """, (session_id,))
    
    data = cursor.fetchall()
    
    conn.close()
    return data
