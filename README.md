# CEP - TCLE

Plugin do Claude Code para triagem ética de Termos de Consentimento Livre e Esclarecido (TCLE) e Termos de Assentimento de pesquisas com seres humanos no Brasil, com base na Lei 14.874/2024, no Decreto 12.651/2025, nos despachos e informes da Inaep, nas Resoluções CNS 466/2012, 510/2016 e 441/2011 e nas orientações da Conep.

**Não substitui a avaliação nem o parecer de um Comitê de Ética em Pesquisa.**

## Instalação

```
claude plugin marketplace add aldemararaujo/cep-tcle
claude plugin install cep-tcle@cep-tcle-local
```

Depois, em uma sessão nova do Claude Code:

- `/cep-tcle:triagem-rapida <arquivo do TCLE>`
- `/cep-tcle:relatorio <arquivo do TCLE> [projeto]`
- `/cep-tcle:comparar-projeto <TCLE> <projeto>`
- `/cep-tcle:criterios <dúvida>`

Ou simplesmente peça: "analise este TCLE". Use sempre documentos anonimizados.

Documentação completa, estrutura, testes e manutenção da base em [cep-tcle/README.md](cep-tcle/README.md). Histórico em [cep-tcle/CHANGELOG.md](cep-tcle/CHANGELOG.md).

## Licença

Conteúdo autoral sob [CC BY 4.0](cep-tcle/LICENSE). Os textos normativos incluídos são atos oficiais e não estão sujeitos a essa licença.
