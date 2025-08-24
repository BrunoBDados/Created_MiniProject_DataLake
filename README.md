```markdown

# Data Lake com Python

Este projeto é um exercício de aprendizado onde simulo a criação de um data lake usando Python.  
A ideia é organizar os dados em três camadas:

- **raw**: dados brutos  
- **processed**: dados tratados  
- **curated**: dados consolidados  

O código é simples e serve apenas para treinar o uso das bibliotecas **pandas** e **os**.

---

## Tecnologias utilizadas
- Python 3  
- Pandas  
- OS  
- Pyarrow (para salvar arquivos parquet)

---

## Estrutura de diretórios

```

data\_lake/
├── raw/          # dados brutos (json)
├── processed/    # dados processados (parquet)
└── curated/      # dados finais consolidados (parquet)

````

---

## Como executar

1. Clone este repositório:  
   ```bash
   git clone https://github.com/BrunoBDados/Created_MiniProject_DataLake
````

2. Instale as dependências:

   ```bash
   pip install pandas pyarrow
   ```

3. Execute o script:

   ```bash
   python processos.py
   ```

---

## Sobre

Esse projeto faz parte da minha rotina de prática em programação e engenharia de dados.
Ainda estou aprendendo, então qualquer sugestão ou crítica construtiva é muito bem-vinda.

```

---

Quer que eu adicione também um **exemplo de como ficam os dados em cada camada** (um trechinho do JSON e do parquet convertido em tabela), para deixar o README mais didático?
```
