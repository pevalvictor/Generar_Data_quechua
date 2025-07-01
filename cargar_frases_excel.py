import pandas as pd
from sqlalchemy import create_engine, text
from app.models import Base
from app.database import engine

# 1. Leer archivo Excel
archivo = "FRASES_A_QUECHUA.xlsx"
df = pd.read_excel(archivo)

# 2. Renombrar columnas por seguridad
df.columns = [col.strip().lower() for col in df.columns]

# 3. Verifica que exista una columna de español
if "español" not in df.columns:
    raise Exception("No se encontró la columna 'Español' en el Excel.")

# 4. Conectarse a la base de datos
conn = engine.connect()

# 5. Insertar frases que no existen
nuevas = 0
for frase in df["español"].dropna().unique():
    # Buscar si ya existe
    resultado = conn.execute(text(
        "SELECT 1 FROM traducciones WHERE texto_origen = :frase"
    ), {"frase": frase}).fetchone()

    if not resultado:
        conn.execute(text("""
            INSERT INTO traducciones (texto_origen, idioma_origen, idioma_destino, fuente)
            VALUES (:texto, 'es', 'qu', 'manual')
        """), {"texto": frase})
        nuevas += 1

conn.commit()
conn.close()

print(f"✅ Frases insertadas: {nuevas}")
