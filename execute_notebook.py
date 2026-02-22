import nbformat
from nbclient import NotebookClient

notebook_filename = 'Analisis_Sentimen_Banjir_Sumatera_2025.ipynb'

print(f"Loading notebook {notebook_filename}...")
with open(notebook_filename, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

client = NotebookClient(nb, timeout=600, kernel_name='python3')

print("Executing notebook cells...")
client.execute()

with open(notebook_filename, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

print("Notebook executed and saved successfully!")
