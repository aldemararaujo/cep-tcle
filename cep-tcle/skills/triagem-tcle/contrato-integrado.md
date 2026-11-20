# Contrato do modo integrado (CEP - TCLE ↔ CEP - Parecerista)

Formato de troca para quando o CEP - Parecerista coordena a análise e delega ao CEP - TCLE a parte do consentimento.

## Entrada esperada do Parecerista

O Parecerista envia, em texto ou JSON, os campos abaixo. Campos ausentes são tratados como desconhecidos, nunca presumidos.

```json
{
  "origem": "cep-parecerista",
  "caso_id": "identificador interno do caso, sem dados pessoais",
  "anonimizacao_confirmada": true,
  "caso_ficticio": false,
  "documentos": ["caminho ou nome do TCLE", "caminho do projeto, se houver", "termo de assentimento, se houver"],
  "escopo": "relatorio | triagem | comparacao | criterios",
  "questoes": ["perguntas específicas do Parecerista, se houver"],
  "contexto_estudo": {
    "area": "biomédica | CHS | outra",
    "desenho": "texto livre",
    "populacao": "texto livre",
    "ambiente": "presencial | virtual | misto",
    "material_biologico": false,
    "multicentrico": false,
    "transferencia_internacional": false
  }
}
```

Se `anonimizacao_confirmada` e `caso_ficticio` forem ambos falsos ou ausentes, peça a confirmação uma única vez ao Parecerista e não prossiga até recebê-la.

## Saída devolvida ao Parecerista

Devolva um bloco JSON seguido de um resumo curto em texto. Não converse diretamente com o usuário final nem repita o aviso de anonimização.

```json
{
  "origem": "cep-tcle",
  "versao_plugin": "1.2.0",
  "base_atualizada_em": "2026-11-20",
  "caso_id": "o mesmo recebido",
  "modulos_aplicados": ["clinico", "menores-assentimento"],
  "documentos_analisados": ["..."],
  "limitacoes": ["projeto ausente: compatibilidade de riscos não verificável"],
  "achados": [
    {
      "id": "G08",
      "criterio": "Liberdade de recusar e retirar o consentimento",
      "evidencia": "trecho literal do TCLE ou \"não localizada\"",
      "localizacao": "página ou seção do TCLE, se houver",
      "classificacao": "conforme | parcial | pendente | nao_aplicavel | nao_verificavel",
      "fundamento": "Lei 14.874/2024, art. 18, § 7º",
      "fundamento_confirmado": true,
      "natureza": "exigencia_normativa | orientacao_oficial | recomendacao_etica | melhoria_editorial | pergunta",
      "impacto": "critico | importante | editorial",
      "sugestao": "minuta ou ação, a adaptar ao protocolo"
    }
  ],
  "inconsistencias": ["..."],
  "respostas_as_questoes": [{"questao": "...", "resposta": "..."}],
  "indice": {"conformes": 0, "parciais": 0, "denominador": 0, "valor": null},
  "incertezas_normativas": ["..."]
}
```

Regras:

- `fundamento_confirmado` só é `true` quando o dispositivo foi localizado no texto da base ou em fonte oficial consultada.
- `indice.valor` fica `null` quando não houver base suficiente.
- Nenhum campo pode conter nomes, contatos ou outros dados pessoais do material.
