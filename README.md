# Datathon FIAP - POS Tech Data Analytics
## Sobre o Projeto
Este projeto foi desenvolvido como uma solução para otimizar a fase inicial do processo de recrutamento: a triagem de currículos. A ferramenta auxilia o time de recrutamento a identificar rapidamente os talentos mais promissores para uma vaga e, inversamente, as vagas mais adequadas para um determinado candidato.

### Objetivo
O objetivo principal é substituir a triagem manual e subjetiva por uma análise quantitativa e orientada por dados, economizando tempo e aumentando a precisão na seleção inicial de candidatos.

### Como Funciona
O fluxo do sistema pode ser resumido em 4 etapas:

Input de Dados: Os dataframes de candidatos, de vagas e das aplicações entre eles (relação candidato-vaga) são carregados 

Pré-processamento: As colunas com dados estruturados (ex: nivel_profissional, nivel_academico, nivel_ingles, area_atuacao) são tratadas para que o match entre os dados do candidato e as respectivas exigências da vaga possam ser comparadas e utilizadas em modelos de machine learning.

Geração de Embeddings: Utilizando técnicas de Processamento de Linguagem Natural (PLN), o texto do currículo de cada candidato, seus conhecimentos técnicos, bem como as principais atividades e as competencias exigidas na descrição de cada vaga são convertidos em vetores numéricos (embeddings), que representam seu significado semântico.

Cálculo de Compatibilidade: A similaridade de cosseno é calculada entre os embeddings dos candidatos e das vagas. O resultado é um score de compatibilidade que permite a identificação das melhores combinações.
