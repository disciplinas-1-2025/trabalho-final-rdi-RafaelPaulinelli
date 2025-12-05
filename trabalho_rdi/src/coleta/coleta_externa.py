import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def raspar_vagas():
    print("Iniciando coleta de dados externos (Python.org)...")
    vagas = []
    # Vamos raspar apenas 2 páginas para ser rápido
    for i in range(1, 3): 
        url = f"https://www.python.org/jobs/?page={i}"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        
        lista = soup.find_all('li')
        for item in lista:
            # Procura pelo elemento que tem o nome da empresa
            empresa_tag = item.find('span', class_='listing-company-name')
            if empresa_tag:
                # Extrai dados básicos
                titulo = empresa_tag.find('a').text.strip()
                cat_tag = item.find('span', class_='listing-job-type')
                categoria = cat_tag.text.strip() if cat_tag else "Geral"
                
                # Cria um texto "rico" para usarmos na busca depois
                texto_busca = f"{titulo} {categoria} python development sql data".lower()
                
                vagas.append({
                    'titulo': titulo,
                    'categoria': categoria,
                    'texto_busca': texto_busca
                })
        time.sleep(1) # Pausa educada para não bloquear
        
    df = pd.DataFrame(vagas)
    # Salva na pasta raw
    df.to_csv("data/raw/dados_externos.csv", index=False)
    print(f"Sucesso! {len(df)} vagas coletadas e salvas em data/raw/dados_externos.csv")

if __name__ == "__main__":
    raspar_vagas()
