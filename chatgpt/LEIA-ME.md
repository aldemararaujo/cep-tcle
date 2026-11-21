# CEP - TCLE no ChatGPT

Este pacote recria o assistente CEP - TCLE como um **GPT personalizado** no ChatGPT. Ele usa as mesmas regras, critérios e base normativa do plugin para Claude Code.

**Não substitui a avaliação nem o parecer de um Comitê de Ética em Pesquisa. Use sempre documentos anonimizados.**

## Do que você precisa

- Uma conta do ChatGPT em plano que permita criar GPTs.
- O arquivo `cep-tcle-gpt-chatgpt-<versão>.zip`, baixado da página de [releases](https://github.com/aldemararaujo/cep-tcle/releases/latest), ou o conteúdo desta pasta `chatgpt/`.

## Passo a passo

1. Descompacte o arquivo .zip. Ele tem:
   - `instrucoes-gpt.md`: as instruções do GPT;
   - `conhecimento/`: 13 arquivos com os critérios e o texto das normas.
2. No ChatGPT, abra **Explorar GPTs** e clique em **Criar**. Vá para a aba **Configurar**.
3. **Nome:** CEP - TCLE.
4. **Descrição:** Triagem ética de TCLEs com base na Lei 14.874/2024, no Decreto 12.651/2025, na Inaep e nas Resoluções CNS. Não substitui o CEP.
5. **Instruções:** abra `instrucoes-gpt.md` num editor de texto, copie todo o conteúdo e cole no campo.
6. **Conhecimento:** clique em "Carregar arquivos" e envie os 13 arquivos da pasta `conhecimento/`.
7. **Iniciadores de conversa** (sugestões):
   - Fazer uma triagem rápida deste TCLE anonimizado
   - Gerar relatório completo com matriz de conformidade
   - Comparar o TCLE com o projeto de pesquisa
   - O contato da Inaep é obrigatório no TCLE?
8. **Recursos:** deixe "Pesquisa na web" desmarcada (ou marcada, se quiser que ele possa confirmar a vigência de normas nos portais oficiais). "Criação de imagens" não é necessária.
9. Em **Compartilhar**, escolha quem pode usar (só você, quem tiver o link ou público) e clique em **Criar**.

## Como usar

Envie o TCLE anonimizado (PDF, Word ou texto colado) e peça, por exemplo, "Faça uma triagem rápida". O GPT pede a confirmação de anonimização, identifica o tipo de estudo e os módulos aplicáveis e devolve a análise com:

- classificação de cada critério (conforme, parcial, pendente, não aplicável, não verificável);
- evidência no termo, fundamento e natureza (exigência, orientação, recomendação ou melhoria);
- índice: 100 × (conformes + 0,5 × parciais) ÷ itens avaliáveis;
- inconsistências e próximos passos.

## Atualização

Quando sair uma versão nova, baixe o .zip do release mais recente, troque o texto das **Instruções** e substitua os arquivos de **Conhecimento** do seu GPT. A data da base normativa está no fim das instruções.

## Diferenças em relação ao plugin para Claude Code

- No GPT não há comandos (`/cep-tcle:...`) nem scripts: o índice de legibilidade e a exportação para Word e Excel não estão disponíveis.
- O ChatGPT busca trechos nos arquivos de conhecimento. Por isso, peça que ele confira o artigo no texto da norma quando a citação for importante.
- O limite de 8.000 caracteres das instruções exigiu uma versão mais curta das regras. Os detalhes de cada critério ficam no arquivo `01-criterios-e-modulos.md`.
