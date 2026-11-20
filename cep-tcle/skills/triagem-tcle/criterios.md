# Tabela de critérios → fontes

Cada dispositivo abaixo foi conferido no texto da base (`references/texto/`) em 2026-11-20. Antes de citar, localize o trecho com busca no arquivo indicado e cite somente o que confirmar. Esta tabela orienta onde procurar e não substitui a leitura.

**Siglas dos arquivos** (todos em `references/texto/`):

| Sigla | Arquivo |
|---|---|
| LEI | `lei-14874-2024-compilada-planalto.txt` |
| DEC | `decreto-12651-2025-planalto.txt` |
| R466 | `res-cns-466-2012.txt` |
| R510 | `res-cns-510-2016.txt` |
| R441 | `res-cns-441-2011.txt` |
| OC11 | `conep-oficio-circular-11-2023-assentimento.txt` |
| LGPD | `lgpd-lei-13709-2018-planalto.txt` |
| D03 | `inaep-despacho-03-2026-dou.txt` |
| IMC | `inaep-informe-tecnico-multicentricas-despacho-03-2026.txt` |
| D05 | `inaep-despacho-05-2026-dou.txt` |
| MCL | `conep-manual-pendencias-clinica-2015.txt` (itens 1.1 a 1.22 tratam do TCLE) |
| MCH | `conep-manual-pendencias-chs-2023.txt` (seções "Registro do Consentimento / Assentimento") |

**Natureza:** N = exigência normativa (lei, decreto, resolução vigente); O = orientação oficial (Inaep, Conep); R = recomendação ética; E = melhoria editorial.

**Regra de transição:** o DEC art. 39 mantém válidas as normas do CNS que não contrariem a Lei 14.874/2024 e o Decreto, até que a Inaep publique normas próprias. Cite uma resolução do CNS como exigência apenas quando não houver conflito com LEI ou DEC; havendo dúvida, classifique como orientação e indique conferência.

## Núcleo geral

| ID | Critério | Fontes verificadas | Nat. | Observações |
|---|---|---|---|---|
| G01 | Linguagem clara, objetiva e de fácil compreensão | LEI art. 2º, LIII; LEI art. 18, § 1º; R466 IV.1 "b"; R510 art. 15 | N | Use `scripts/legibilidade.py` como dado auxiliar, nunca como critério isolado. |
| G02 | Convite, identificação da pesquisa e do pesquisador | R466 IV.2; OC11 item 11 "a" (para assentimento) | N/O | |
| G03 | Justificativa, objetivos e procedimentos, com métodos | R466 IV.3 "a"; R510 art. 17, I; R510 art. 10 | N | Compatibilidade com o projeto: não verificável sem protocolo. |
| G04 | Possibilidade de grupo controle ou experimental | R466 IV.3 "a"; R466 IV.4 "b" | N | Só quando houver alocação. |
| G05 | Riscos e desconfortos, com medidas de minimização | R466 IV.3 "b"; R510 art. 17, II | N | |
| G06 | Benefícios esperados, sem promessa indevida | R466 IV.3 "b"; R510 art. 17, V | N | |
| G07 | Acompanhamento e assistência, inclusive após o término ou interrupção | R466 IV.3 "c"; R510 art. 17, V; LEI art. 23; IMC 5.7 | N/O | IMC 5.7: canais, horários e conduta em intercorrência, proporcionais ao risco. |
| G08 | Liberdade de recusar e de retirar o consentimento sem penalização | LEI art. 18, § 7º; R466 IV.3 "d"; R510 art. 9º, II e art. 17, III | N | |
| G09 | Sigilo, privacidade e confidencialidade | LEI art. 19; R466 IV.3 "e"; R510 art. 9º, III-IV e art. 17, IV | N | R510 art. 9º, V: participante decide se a identidade será divulgada. |
| G10 | Tratamento e armazenamento de dados pessoais | LEI art. 51 (guarda por 5 anos; 10 anos em terapias avançadas); LEI art. 61 (LGPD subsidiária); LGPD art. 7º, IV; LGPD art. 11, II, "c" | N | Ver módulo de dados e uso futuro. |
| G11 | Ressarcimento de despesas | LEI art. 20, § 1º; R466 IV.3 "g"; R510 art. 9º, VII e art. 17, VII | N | |
| G12 | Vedação de remuneração ou vantagem | LEI art. 20, caput (exceção do § 2º para fase I e bioequivalência com voluntários sadios) | N | |
| G13 | Indenização por danos | LEI art. 23; R466 IV.3 "h"; R510 art. 9º, VI | N | |
| G14 | Ausência de cláusula de renúncia de direitos ou de isenção de responsabilidade | LEI art. 18, § 3º; R466 IV.4 "c" | N | MCL itens 1.8, 1.11 e 1.15 listam expressões a evitar. |
| G15 | Acesso aos resultados | LEI art. 54; R510 art. 17, VI | N | |
| G16 | Contatos do pesquisador responsável | R510 art. 17, VIII; R466 IV.5 "d" | N | |
| G17 | Contatos do CEP, com breve explicação do que é o CEP | R510 art. 17, IX; R466 IV.5 "d"; D03 item V (multicêntricas); IMC 5.5 e 5.6 | N/O | Em multicêntricas, ver `modulos/multicentrico.md`. IMC 5.6: contato da Inaep não é exigência geral. Menção à Conep na R466/R510 deve ser lida à luz da transição. |
| G18 | Entrega de via ao participante | R466 IV.3 "f"; R510 art. 17, § 3º | N | |
| G19 | Data e assinaturas do pesquisador e do participante ou representante | LEI art. 18, § 1º; R466 IV.5 "d" | N | Rubrica em todas as páginas e assinaturas na mesma folha: R466 IV.5 "d" (orientação de norma do CNS mantida pelo DEC art. 39; conferir entendimento atual). |
| G20 | Participante que não sabe ler: testemunha imparcial | LEI art. 2º, LIV; LEI art. 18, § 5º; R510 art. 15, § 2º | N | Condicional. |
| G21 | Tempo e momento adequados para decidir | R466 IV.1 "a" e "c"; R510 art. 5º, § 2º e art. 6º | N | Avalia o processo; costuma ser verificável só no protocolo. |
| G22 | Informação sobre aprovação pelo CEP | LEI art. 18, § 4º | N | |
| G23 | Atualização do TCLE diante de nova informação relevante | LEI art. 18, § 2º | N | Aplica-se a emendas; em TCLE inicial, normalmente não aplicável. |
| G24 | Coerência interna e paginação | R466 IV.5 "d"; IMC 5.8 e 5.9 (controle de versões) | O/E | |

## Módulos condicionais

Detalhes de cada módulo em `modulos/`. Fontes principais:

| Módulo | Arquivo | Fontes verificadas |
|---|---|---|
| Ensaio clínico / intervenção | `modulos/clinico.md` | LEI arts. 21 (placebo), 22, 30 (plano de acesso pós-estudo); DEC art. 31; R466 IV.4; D05 (farmacocinéticos de alta toxicidade); MCL itens 1.x |
| Menores e pessoas sem plena capacidade | `modulos/menores-assentimento.md` | LEI art. 2º, II; LEI art. 24 e § 1º-§ 2º; DEC art. 32; R466 IV.6 "a"; R510 arts. 12 e 17, § 4º; OC11 itens 10 e 11 |
| Autonomia limitada por dependência ou autoridade | `modulos/menores-assentimento.md` | R466 IV.6 "b"; R510 art. 11; DEC art. 32, § 1º, IV |
| Povos e comunidades tradicionais | `modulos/menores-assentimento.md` | DEC art. 32, § 1º, III; R466 IV.6 "e"; R510 art. 13; LEI art. 24, § 3º (promulgação de parte vetada) |
| Ciências Humanas e Sociais / registro não escrito | `modulos/chs-registro.md` | R510 arts. 4º-8º, 14-17; DEC art. 35; MCH |
| Pesquisa em ambiente virtual | `modulos/online-digital.md` | R510 art. 5º e art. 17; MCH seção "Pesquisa em ambiente virtual" |
| Material biológico, biobanco e biorrepositório | `modulos/biobanco.md` | LEI arts. 39-48; DEC arts. 33-34; R441 itens 5, 6 e 10; MCL itens 1.21 e 1.22 |
| Dados, uso futuro e transferência internacional | `modulos/biobanco.md` | LEI art. 40, X-XI; LEI art. 45; LEI art. 51, § 2º; DEC art. 34; LGPD arts. 7º, 11 e 13 |
| Multicêntrico | `modulos/multicentrico.md` | LEI art. 14, § 7º; DEC art. 27; D03 item V; IMC seção 5 |
| Emergência sem consentimento prévio | `modulos/clinico.md` | LEI art. 18, § 6º |
| Dispensa de TCLE ou de registro | `modulos/chs-registro.md` | R466 IV.8; R510 arts. 14 e 16 |
