# CEP - TCLE

Assistente de triagem ética de Termos de Consentimento Livre e Esclarecido (TCLE) e Termos de Assentimento de pesquisas com seres humanos no Brasil, com base na Lei 14.874/2024, no Decreto 12.651/2025, nos despachos e informes da Inaep, nas Resoluções CNS 466/2012, 510/2016 e 441/2011 e nas orientações da Conep.

**Não substitui a avaliação nem o parecer de um Comitê de Ética em Pesquisa. Use sempre documentos anonimizados.**

Funciona em três lugares. Escolha o seu:

| Você usa | Caminho |
|---|---|
| Claude Code | [Plugin para Claude Code](#claude-code) |
| ChatGPT no app para computador (Windows ou Mac) ou Codex | [Plugin para ChatGPT e Codex](#chatgpt-no-app-para-computador-e-codex) |
| ChatGPT no navegador (chatgpt.com) ou no celular | [GPT personalizado](#chatgpt-no-navegador-ou-no-celular-gpt-personalizado) |

Também existe uma versão web, sem instalação, que usa a sua chave de API do Gemini, Claude, ChatGPT ou DeepSeek: [aldemararaujo.github.io/tcle](https://aldemararaujo.github.io/tcle/).

## Claude Code

```
claude plugin marketplace add aldemararaujo/cep-tcle
claude plugin install cep-tcle@cep-tcle
```

Depois, em uma sessão nova do Claude Code:

- `/cep-tcle:triagem-rapida <arquivo do TCLE>`
- `/cep-tcle:relatorio <arquivo do TCLE> [projeto]`
- `/cep-tcle:comparar-projeto <TCLE> <projeto>`
- `/cep-tcle:criterios <dúvida>`

Ou simplesmente peça: "analise este TCLE".

## ChatGPT no app para computador e Codex

O plugin segue também o formato de plugins da OpenAI (`.codex-plugin/plugin.json` e `.agents/plugins/marketplace.json`). Para instalar, é preciso o [Codex CLI](https://developers.openai.com/codex) instalado.

1. No terminal, adicione este repositório como catálogo de plugins:

   ```
   codex plugin marketplace add aldemararaujo/cep-tcle
   ```

2. **No app do ChatGPT para computador:** feche e abra o app de novo. No modo Work ou no Codex, abra o **Diretório de plugins**, escolha o catálogo **CEP - TCLE**, instale o plugin **CEP - TCLE** e comece uma conversa nova.

   **No Codex CLI:** rode `codex`, digite `/plugins`, instale o **CEP - TCLE** e comece uma sessão nova.

3. Peça, por exemplo: "Faça uma triagem rápida deste TCLE anonimizado".

Para receber atualizações: `codex plugin marketplace upgrade cep-tcle`.

Segundo a [documentação da OpenAI](https://developers.openai.com/codex/plugins/build), catálogos adicionados a partir de repositórios aparecem no app para computador e no Codex, mas não necessariamente no chatgpt.com ou no celular. Nesses casos, use o GPT personalizado abaixo.

## ChatGPT no navegador ou no celular: GPT personalizado

1. Baixe o arquivo **`cep-tcle-gpt-chatgpt-<versão>.zip`** na página de [releases](https://github.com/aldemararaujo/cep-tcle/releases/latest).
2. Siga o passo a passo do [LEIA-ME do ChatGPT](chatgpt/LEIA-ME.md): criar um GPT, colar as instruções e enviar os 13 arquivos de conhecimento.

O GPT pode ser compartilhado com outras pessoas pelo link, sem que elas precisem repetir a configuração.

## O que o assistente faz

- Identifica o tipo de estudo e os módulos aplicáveis: ambiente virtual, material biológico e dados, grupos especiais e assentimento, pesquisa clínica, Ciências Humanas e Sociais, multicêntrica.
- Classifica cada critério como conforme, parcial, pendente, não aplicável ou não verificável, com a evidência no termo, o fundamento e a natureza (exigência, orientação, recomendação ou melhoria).
- Calcula o índice 100 × (conformes + 0,5 × parciais) ÷ itens avaliáveis, aponta inconsistências e sugere redações a adaptar.

Documentação completa, estrutura, testes e manutenção da base em [cep-tcle/README.md](cep-tcle/README.md). Histórico em [cep-tcle/CHANGELOG.md](cep-tcle/CHANGELOG.md).

## Licença

Conteúdo autoral sob [CC BY 4.0](cep-tcle/LICENSE). Os textos normativos incluídos são atos oficiais e não estão sujeitos a essa licença.
