
import pandas as pd
import requests
from bs4 import BeautifulSoup
import glob
import time

rango = range(2000,2024, 1)

def extract_wiki(rango):
    for r in rango:
        try:
            resposta = requests.get(f'https://es.wikipedia.org/wiki/Festival_de_la_Canci%C3%B3n_de_Eurovisi%C3%B3n_{r}')
            codi_web = (resposta.text)

            soup = BeautifulSoup(codi_web, 'html.parser')
            final = soup.find('span', id="Final")
            tabla = final.find_next("table")
            df = pd.read_html(str(tabla))[0]

            print(df)
            df.to_excel(f"final-{r}.xlsx", index=False)
            print(f"TODO BIEN EN {r}")
            time.sleep(1)
        except AttributeError:
            print(f"Problema en {r}")

extract_wiki(rango)

files = glob.glob("*.xlsx")
print(files)

    llista_dfs = []
    for f in files:
        df = pd.read_excel(f)
        any = f.split("-")[1].split(".")[0]
        df["año"]= any
    
        df.columns.values[2] = "cantante"
        df.columns.values[5] = "Puntos"
        df.columns.values[0] = "N."
    
    
        llista_dfs.append(df)


    final_df = pd.concat(llista_dfs)
    final_df.to_excel("final.xlsx", index=False)
    print(final_df)

