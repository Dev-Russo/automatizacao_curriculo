import yaml
import string
import nltk
import ssl
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

## Baixa todos os pacotes necessarios para o nltk
def baixar_pacotes_nltk():
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    try:
        nltk.data.find('tokenizers/punkt')
        print("Pacote 'punkt' já está baixado.")
    except LookupError:
        print("Pacote 'punkt' não encontrado. Baixando...")
        nltk.download('punkt')

    try:
        nltk.data.find('corpora/stopwords')
        print("Pacote 'stopwords' já está baixado.")
    except LookupError:
        print("Pacote 'stopwords' não encontrado. Baixando...")
        nltk.download('stopwords')

baixar_pacotes_nltk()

## Leitura dos arquivos vaga.txt e curriculo.yaml
try:
    with open('vaga.txt', 'r', encoding='utf-8') as f_vaga:
        descricao_vaga = f_vaga.read()
    print("Arquivo 'vaga.txt' lido com sucesso.")

    with open('curriculo_mestre.yaml', 'r', encoding='utf-8') as f_curriculo:
        meu_curriculo = yaml.safe_load(f_curriculo)
    print("Arquivo 'curriculo_mestre.yaml' lido com sucesso.")

except FileNotFoundError as e:
    print(f"Erro: Arquivo não encontrado - {e.filename}. Verifique se os arquivos estão na mesma pasta.")
    exit()

## Tratamento
conteudo_lower = descricao_vaga.lower()
lista_stopwords = stopwords.words('portuguese')
## pontuacao = list(string.punctuation)
tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(conteudo_lower)



palavras_chave_vaga = []
for palavra in tokens:
    if palavra not in lista_stopwords:
        palavras_chave_vaga.append(palavra)

print(f"Palavras-chave encontradas na vaga: {len(palavras_chave_vaga)}")

## Salva minhas habilidades
minhas_habilidades = [h['skill'].lower() for h in meu_curriculo['habilidades']]

## Compara as habilidades com as palavras-chave da vaga
habilidades_em_comum = set(palavras_chave_vaga) & set(minhas_habilidades) ## Interseção de Conjuntos



experiencias_relevantes = []
for experiencia in meu_curriculo['experiencias']:
    tags_da_experiencia = set(experiencia['tags'])

    if tags_da_experiencia.intersection(habilidades_em_comum):
        
        experiencias_relevantes.append(experiencia)

habilidades_ordenadas = []
for habilidades in habilidades_em_comum:
    habilidades_ordenadas.append(habilidades)

for habilidade in minhas_habilidades:
    if habilidade not in habilidades_ordenadas:
        habilidades_ordenadas.append(habilidade)

print("\n--- Análise de Compatibilidade ---")
print(f"Minhas habilidades: {', '.join(sorted(minhas_habilidades))}")

if habilidades_em_comum:
    print("\n✅ Habilidades correspondentes encontradas na vaga:")
    for habilidade in sorted(list(habilidades_em_comum)):
        print(f"- {habilidade.capitalize()}")
else:
    print("\n❌ Nenhuma habilidade correspondente encontrada na descrição da vaga.")


print("\n--- Experiências Relevantes Encontradas ---")
if experiencias_relevantes:
    for exp in experiencias_relevantes:
        print(f"✅ Cargo Relevante: {exp['cargo']} na empresa {exp['empresa']}")
else:
    print("❌ Nenhuma experiência profissional diretamente relevante foi encontrada.")

print("\n--- Habilidades em Comum e Ordenadas ---")
print(habilidades_ordenadas)