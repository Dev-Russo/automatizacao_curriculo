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

print("\n--- Habilidades em Comum e Ordenadas ---")
print(habilidades_ordenadas)

print("\nGerando o currículo personalizado...")

nome_arquivo_saida = "curriculo_personalizado.md"

with open(nome_arquivo_saida, 'w', encoding='utf-8') as f:
    info = meu_curriculo['informacoes_pessoais']
    f.write(f"# {info['nome']}\n")
    f.write(f"_{info['email']} | {info['telefone']} | {info['linkedin']}\n\n")

    f.write("## Resumo Profissional\n")
    f.write(f"{meu_curriculo['perfil_profissional']}\n\n")

    f.write("## Habilidades\n")
    for habilidade in habilidades_ordenadas:
        f.write(f"- {habilidade.capitalize()}\n")
    f.write("\n")

    f.write("## Experiências Profissionais\n\n")

    for experiencia in experiencias_relevantes:
    
        f.write(f"### {experiencia['cargo']} na {experiencia['empresa']}\n")

        f.write(f"*{experiencia['periodo']}*\n")
        for ponto_descricao in experiencia['descricao']:
            f.write(f"- {ponto_descricao}\n")
        
        f.write("\n")