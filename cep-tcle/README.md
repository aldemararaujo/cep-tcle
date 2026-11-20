# CEP - TCLE

Assistente de triagem ética de Termos de Consentimento Livre e Esclarecido (TCLE) e Termos de Assentimento de pesquisas com seres humanos no Brasil. Analisa documentos anonimizados, identifica os requisitos aplicáveis ao tipo de pesquisa e aponta evidências, pendências e itens não verificáveis com base na Lei 14.874/2024, no Decreto 12.651/2025, nas orientações da Inaep/Sinep, nas Resoluções CNS 466/2012, 510/2016 e 441/2011 e nos manuais de pendências da Conep.

**Não substitui a avaliação nem o parecer de um Comitê de Ética em Pesquisa.**

## Instalação

No Claude Code (2.1 ou mais recente):

```
claude plugin marketplace add aldemararaujo/cep-tcle
claude plugin install cep-tcle@cep-tcle-local
```

Para receber atualizações: `claude plugin marketplace update cep-tcle-local` e depois `claude plugin update cep-tcle@cep-tcle-local`.

Para desenvolver a partir de um clone local, use o caminho da pasta clonada no lugar de `aldemararaujo/cep-tcle`.

## Uso

| Comando | O que faz |
|---|---|
| `/cep-tcle:triagem-rapida <tcle> [projeto]` | Escopo, resumo e pendências críticas |
| `/cep-tcle:relatorio <tcle> [projeto]` | Relatório completo com matriz e exportação para .docx/.xlsx |
| `/cep-tcle:comparar-projeto <tcle> <projeto>` | Divergências entre TCLE e projeto |
| `/cep-tcle:criterios <dúvida>` | Explica um critério e onde ele está nas normas |

A skill também é acionada sozinha em pedidos como "analise este TCLE".

## Estrutura

```
skills/triagem-tcle/
  SKILL.md               instruções, hierarquia de fontes e formato de resposta
  criterios.md           critérios do núcleo geral ligados aos dispositivos
  modulos/               critérios condicionais por tipo de pesquisa
  contrato-integrado.md  formato de troca com o CEP - Parecerista
  references/texto/      normas em texto pesquisável
  references/pdf/        originais
  scripts/               legibilidade.py e exportar.py (só biblioteca padrão do Python)
commands/                comandos de cada modo
evals/                   casos de teste
```

Exportação: `.docx` exige [pandoc](https://pandoc.org); `.xlsx` exige LibreOffice. Sem eles, o script gera só o que for possível.

## Testes

```
claude plugin eval ./cep-tcle --runs 1 --ablation none --no-publish
```

Os 8 casos cobrem: TCLE adequado de CHS, ensaio clínico com falhas, menores sem assentimento, formulário on-line, biobanco, pergunta sobre a Inaep, instrução maliciosa escondida no documento e documento não anonimizado. Rode após qualquer mudança na base ou nas instruções. Cada execução completa custa em torno de US$ 2 a 4.

## Manutenção da base

1. Baixe a norma nova da fonte oficial e salve o PDF em `references/pdf/`.
2. Gere o texto: `pdftotext -enc UTF-8 -layout arquivo.pdf references/texto/arquivo.txt`.
3. Atualize a tabela "Base de referência" e a data no topo do SKILL.md, e `criterios.md` ou o módulo afetado.
4. Rode os testes e registre a mudança no CHANGELOG.

## Licença

Conteúdo autoral sob CC BY 4.0 (ver `LICENSE`). Os textos normativos são atos oficiais e não estão sujeitos à licença.
