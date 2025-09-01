# Automatizador de Currículos e Vagas 📝  

## 📌 Descrição  
Este projeto é um script em **Python** que automatiza a personalização de currículos para vagas de emprego específicas.  
A ferramenta lê um currículo "mestre" (em formato **YAML**) e a descrição de uma vaga, e então gera uma nova versão do currículo em formato **Markdown**, destacando as habilidades e experiências mais relevantes para aquela oportunidade.  

O objetivo é **otimizar o processo de candidatura**, economizando tempo e aumentando a relevância do currículo para os sistemas de triagem automática (ATS) e para os recrutadores.  

---

## ✨ Funcionalidades Principais  
- **Análise de Vagas**: utiliza a biblioteca **NLTK** para processar o texto da descrição da vaga, extraindo palavras-chave relevantes.  
- **Correspondência de Habilidades**: identifica as habilidades em comum entre o seu currículo mestre e os requisitos da vaga.  
- **Filtragem de Experiências**: seleciona e exibe apenas as experiências profissionais que estão diretamente relacionadas às habilidades pedidas.  
- **Priorização de Habilidades**: reordena sua lista de competências para que as mais relevantes para a vaga apareçam no topo.  
- **Resumo Profissional Dinâmico**: gera um resumo que se adapta para incluir as principais palavras-chave da vaga.  
- **Geração de Arquivo**: cria um novo arquivo de currículo, formatado em **Markdown (.md)**, pronto para ser revisado ou convertido.  

---

## 🛠️ Tecnologias Utilizadas  
- **Python 3**  
- **PyYAML** → leitura e interpretação do currículo mestre.  
- **NLTK (Natural Language Toolkit)** → processamento de linguagem natural (tokenização e remoção de stopwords).  

---

## 🚀 Como Executar o Projeto  

### Pré-requisitos  
- **Python 3.8 ou superior**  
- **Pip** (gerenciador de pacotes do Python)  

---

### 1️⃣ Instalação  

#### a. Clone o repositório:  
```bash
git clone https://github.com/Dev-Russo/automatizacao_curriculo.git
cd automatizacao_curriculo
```

#### b. Crie e ative um ambiente virtual:
```bash
python -m venv venv
venv\Scripts\activate
```
#### macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```
#### c. Instale as dependências:
Crie um arquivo chamado requirements.txt com o seguinte conteúdo:
```bash
PyYAML
nltk
```
E instale com:
```bash
pip install -r requirements.txt
```
