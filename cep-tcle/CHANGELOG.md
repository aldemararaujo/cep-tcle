# Changelog

## 1.3.0 (2026-11-20)

- Despachos Inaep nº 2, 3 e 4/2026 nas versões do Diário Oficial. A cópia com timbre de entidade privada do Despacho nº 2 foi removida; o corpo do texto era idêntico ao oficial.
- Módulo multicêntrico refeito com base no item V do Despacho nº 3/2026: o contato do CEP responsável pela análise única é exigido; o contato do CEP local é recomendado e a ausência dele não é falha.
- Módulo de biobanco registra a consulta pública da nova resolução (Despacho nº 4/2026) e que, em 20/11/2026, ela não constava como publicada.
- Despacho nº 1 renomeado para o mesmo padrão dos demais (`-dou`).

## 1.2.0 (2026-11-20)

**Base normativa**
- Textos pesquisáveis de todas as normas em `references/texto/`, com os PDFs originais em `references/pdf/` sob nomes descritivos.
- Incluídos, a partir de fontes oficiais: Lei 14.874/2024 compilada e Decreto 12.651/2025 (Planalto); LGPD compilada (Planalto); Despacho Inaep nº 5/2026 (DOU); Notas Técnicas DECIT nº 43/2025 e nº 1/2026; Informes Técnicos da Inaep sobre multicêntricas (Despacho nº 3/2026) e sobre o Despacho nº 5/2026.
- Trechos revogados no texto compilado marcados como `[[TEXTO REVOGADO OU ALTERADO: ...]]`.
- Data da base registrada no SKILL.md, com aviso automático após 6 meses.

**Análise**
- `criterios.md`: 24 critérios do núcleo geral ligados a dispositivos conferidos no texto.
- Módulos condicionais em arquivos próprios: clínico, grupos especiais e assentimento, CHS e registro, ambiente virtual, biobanco e dados, multicêntrico.
- Regra de transição explícita (Decreto 12.651/2025, art. 39).
- Consulta à web permitida só em portais oficiais, para confirmar vigência.
- Contrato de entrada e saída para o modo integrado com o CEP - Parecerista.
- Correção encontrada pelos testes: o aviso de anonimização não reproduz mais os dados pessoais do documento, só descreve o tipo de dado.

**Ferramentas**
- `scripts/legibilidade.py`: índice de Flesch adaptado ao português e frases mais longas.
- `scripts/exportar.py`: relatório em .docx (pandoc) e matriz em .csv/.xlsx (LibreOffice).
- Comandos `/cep-tcle:triagem-rapida`, `/cep-tcle:relatorio`, `/cep-tcle:comparar-projeto` e `/cep-tcle:criterios`.
- Oito casos de teste em `evals/` para `claude plugin eval`.

**Projeto**
- Licença CC BY 4.0, changelog e repositório git.

## 1.1.0 (2026-11-20)
- Conversão do pacote CEP-TCLE 0.45.3 (formato OpenAI/Codex) para plugin do Claude Code.
