# CEP - TCLE: critérios e módulos

Gerado do plugin CEP - TCLE versão 1.4.4 (github.com/aldemararaujo/cep-tcle).

## Onde estão as normas neste GPT

Os arquivos citados nas tabelas abaixo (pasta references/texto do plugin) foram agrupados nestes arquivos de conhecimento:

| Sigla | Arquivo de conhecimento |
|---|---|
| LEI | 02-lei-14874-2024.txt |
| DEC | 03-decreto-12651-2025.txt |
| D03 | 04-inaep-despachos-informes-notas.txt |
| D05 | 04-inaep-despachos-informes-notas.txt |
| IMC | 04-inaep-despachos-informes-notas.txt |
| R466 | 05-res-cns-466-2012.txt |
| R510 | 06-res-cns-510-2016.txt |
| R441 | 07-res-cns-441-2011.txt |
| OC11 | 09-conep-oficios-e-cartas.txt |
| CC01 | 09-conep-oficios-e-cartas.txt |
| OC23 | 09-conep-oficios-e-cartas.txt |
| MCL | 10-manual-pendencias-clinica-2015.txt |
| MCH | 11-manual-pendencias-chs-2023.txt |
| LGPD | 12-lgpd-lei-13709-2018.txt |
| L14063 | 13-lei-14063-2020.txt |

Os caminhos `modulos/...` citados nas tabelas correspondem às seções "Módulo" mais abaixo neste mesmo arquivo.

---

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
| CC01 | `conep-carta-circular-01-2021-ambiente-virtual.txt` |
| OC23 | `conep-oficio-circular-23-2022-consentimento-eletronico.txt` |
| L14063 | `lei-14063-2020-assinaturas-eletronicas-planalto.txt` |
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
| G11 | Ressarcimento de despesas, com formas, quantias e periodicidade | LEI art. 12, VII; LEI art. 20, § 1º; R466 IV.3 "g"; R510 art. 9º, VII e art. 17, VII | N | LEI art. 12, VII: cabe ao CEP assegurar que o ressarcimento ou provimento material prévio esteja claramente especificado no TCLE, "incluídas as formas, as quantias e a respectiva periodicidade". |
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
| Pesquisa em ambiente virtual e consentimento eletrônico | `modulos/online-digital.md` | CC01; OC23 (revoga o item 4.5 da CC01); R510 art. 5º e art. 17; MCH seção "Pesquisa em ambiente virtual" |
| Material biológico, biobanco e biorrepositório | `modulos/biobanco.md` | LEI arts. 39-48; DEC arts. 33-34; R441 itens 5, 6 e 10; MCL itens 1.21 e 1.22 |
| Dados, uso futuro e transferência internacional | `modulos/biobanco.md` | LEI art. 40, X-XI; LEI art. 45; LEI art. 51, § 2º; DEC art. 34; LGPD arts. 7º, 11 e 13 |
| Multicêntrico | `modulos/multicentrico.md` | LEI art. 14, § 7º; DEC art. 27; D03 item V; IMC seção 5 |
| Emergência sem consentimento prévio | `modulos/clinico.md` | LEI art. 18, § 6º |
| Dispensa de TCLE ou de registro | `modulos/chs-registro.md` | R466 IV.8; R510 arts. 14 e 16 |


---

# Módulo: ensaio clínico e pesquisa intervencional

Aplique quando houver intervenção em saúde: medicamento, produto, dispositivo, procedimento experimental, alocação em grupos ou placebo. Siglas dos arquivos em `../criterios.md`.

| ID | Critério | Fontes verificadas | Nat. |
|---|---|---|---|
| C01 | Métodos terapêuticos alternativos existentes, quando pertinente | R466 IV.4 "a" | N |
| C02 | Possibilidade de grupo controle ou placebo, com o significado explicado | R466 IV.4 "b"; R466 IV.3 "a" | N |
| C03 | Uso de placebo justificado; participante não privado do melhor tratamento disponível | LEI art. 21 e parágrafo único | N |
| C04 | Acesso pós-estudo ao produto sob investigação, coerente com o plano submetido | LEI art. 30; DEC art. 31 e § 1º | N |
| C05 | Assistência e plano de atendimento a intercorrências, com canais e horários reais | LEI art. 23; IMC 5.7 | N/O |
| C06 | Indenização e assistência a cargo do patrocinador | LEI art. 23, parágrafo único | N |
| C07 | Remuneração só nas exceções legais (fase I ou bioequivalência com voluntário sadio cadastrado) | LEI art. 20, § 2º | N |
| C08 | Estudos farmacocinéticos com fármaco citotóxico, genotóxico ou de alta toxicidade: preferência por pacientes; voluntário sadio só em caráter excepcional e justificado; riscos imediatos, cumulativos e tardios descritos | D05 itens I a III | O |
| C09 | Contracepção e gestação, quando houver risco teratogênico ou desconhecido | MCL item 1.6 ("Contracepção") | O |
| C10 | Emergência sem consentimento prévio: informar na primeira oportunidade e colher decisão de permanência | LEI art. 18, § 6º | N |
| C11 | Interrupção do estudo por superioridade ou segurança, quando relevante para o participante | LEI art. 22 | N |

**Pendências típicas:** o MCL (itens 1.1 a 1.22) traz problema, o que fazer e a fonte para ressarcimento (1.2), assistência por danos (1.3), indenização (1.5), contracepção (1.6), riscos e benefícios (1.9), expressões inadequadas (1.8, 1.11, 1.15) e material biológico ou genético (1.21, 1.22). O manual é de 2015: confira cada fundamento citado nele contra LEI e DEC antes de reproduzi-lo.


---

# Módulo: grupos especiais, assentimento e autonomia limitada

Aplique quando houver crianças, adolescentes, pessoas sem plena capacidade de decidir, pessoas sob relação de dependência ou autoridade, povos indígenas ou comunidades tradicionais. Siglas dos arquivos em `../criterios.md`.

## Grupos especiais

O DEC art. 32, § 1º lista: crianças e adolescentes; gestantes e lactantes; povos indígenas, comunidades quilombolas e demais populações tradicionais; pessoas privadas de liberdade; pessoas com deficiência que comprometa a capacidade de consentimento. O § 2º exige medidas específicas de proteção.

| ID | Critério | Fontes verificadas | Nat. |
|---|---|---|---|
| V01 | TCLE assinado pelo representante legal ou constituído judicialmente | LEI art. 24, I; R466 IV.6 "a"; R510 art. 12, parágrafo único | N |
| V02 | Termo ou registro de assentimento sempre que o participante puder compreender e decidir | LEI art. 2º, II; LEI art. 24, § 1º; R510 art. 17, § 4º | N |
| V03 | Justificativa da escolha do grupo (pesquisa essencial para essa população) | LEI art. 24, II; R466 IV.6 "a"; R510 art. 12 | N |
| V04 | Comunicação ao Ministério Público do roteiro de participação do incapaz | LEI art. 24, § 2º | N |
| V05 | Participação indígena comunicada ao Ministério Público | LEI art. 24, § 3º (parte vetada promulgada) | N |
| V06 | Assentimento com linguagem própria, sem copiar o TCLE dos responsáveis | OC11 item 10 | O |
| V07 | Conteúdo do assentimento: apresentação, objetivos, voluntariedade, produto investigacional, procedimentos, riscos, desconfortos, benefícios, ausência de indução, ressarcimento, confidencialidade, divulgação, direito de recusa e contatos | OC11 item 11, alíneas "a" a "n" | O |
| V08 | Liberdade reforçada para quem está sob autoridade ou dependência (estudantes, empregados, militares, pessoas privadas de liberdade, internos) | R466 IV.6 "b"; R510 art. 11 | N |
| V09 | Autorização coletiva em comunidades que reconhecem a autoridade do líder, sem prejuízo do consentimento individual | R466 IV.6 "e"; R510 art. 13 | N |
| V10 | Gestantes: pesquisa precedida de estudo fora do período gestacional, salvo quando a gestação é o objeto | LEI art. 25 | N |

**Atenção:** o OC11 item 11 "i" fundamenta a vedação de incentivos na R466; hoje a base legal é a LEI art. 20. Cite a LEI.


---

# Módulo: Ciências Humanas e Sociais e formas de registro

Aplique a pesquisas regidas pela R510 (metodologias das ciências humanas e sociais) e a qualquer pesquisa que proponha registro do consentimento não escrito ou dispensa. Siglas dos arquivos em `../criterios.md`.

## Princípio

O consentimento é um processo, não só um documento (R510 art. 4º). O registro pode ser escrito, sonoro, imagético ou outro adequado (R510 art. 15). O DEC art. 35, I prevê consentimento "inclusive em formatos adaptados aos contextos socioculturais", com norma específica da Inaep ainda a editar. Não aplique o checklist clínico a estas pesquisas.

| ID | Critério | Fontes verificadas | Nat. |
|---|---|---|---|
| H01 | Conteúdo mínimo do registro: os 10 incisos do art. 17 | R510 art. 17, I a X | N |
| H02 | Itens ausentes no formato escolhido entregues em documento complementar | R510 art. 17, § 1º | N |
| H03 | Meio de registro justificado conforme risco, processo e participante | R510 art. 16 | N |
| H04 | Sem registro: documento com as informações entregue ao participante | R510 art. 15, § 1º | N |
| H05 | Testemunha externa à equipe como comprovação, quando cabível | R510 art. 15, § 2º | N |
| H06 | Acesso ao registro sempre que solicitado | R510 art. 17, X e § 2º | N |
| H07 | Registro escrito: via assinada pelo participante e pelo pesquisador | R510 art. 17, § 3º | N |
| H08 | Decisão sobre divulgação da identidade e de quais informações podem ser públicas | R510 art. 9º, V; R510 art. 17, IV | N |
| H09 | Comunicação espontânea, sem formalismo excessivo, com tempo para decidir | R510 art. 5º, §§ 1º e 2º; art. 6º | N |
| H10 | Dispensa do processo ou do registro justificada e aprovada pelo CEP | R510 art. 14; art. 16, §§ 1º a 3º; R466 IV.8 | N |

**Pendências típicas:** o MCH traz modelos de pendência para descrição do processo, linguagem inadequada, registro inadequado a grupos diferentes, ausência da garantia de retirada e assentimento.

**Atenção:** a R510 é anterior à Lei 14.874/2024. A LEI art. 18 fala em "assinatura do TCLE"; a compatibilidade dos formatos de registro não escritos com essa regra depende da norma de CHS que a Inaep ainda vai editar (DEC art. 35). Ao avaliar registro oral ou imagético, sinalize esse ponto como incerteza normativa, sem classificar como pendência.


---

# Módulo: pesquisa em ambiente virtual e consentimento eletrônico

Aplique quando qualquer etapa ocorrer por internet, e-mail, formulário eletrônico, telefone, chamada de vídeo ou aplicativo, ou quando o consentimento for registrado eletronicamente. Siglas dos arquivos em `../criterios.md`.

Fontes: **Carta Circular nº 1/2021-Conep (CC01)**, sobre pesquisas com etapa em ambiente virtual, e **Ofício Circular nº 23/2022-Conep (OC23)**, sobre consentimento e assentimento eletrônico. O OC23, item 5.5, revoga o item 4.5 da CC01 (TCLE físico obrigatório quando houver presença na área biomédica). Ambos são orientações da Conep, anteriores à Lei 14.874/2024. Valem como orientação oficial no que não contrariarem LEI e DEC (DEC art. 39).

## No TCLE ou registro de consentimento

| ID | Critério | Fontes verificadas | Nat. |
|---|---|---|---|
| D01 | Riscos próprios do ambiente virtual e limites para garantir confidencialidade, com as medidas adotadas | CC01 item 1.2.1; OC23 item 2.1, I | O |
| D02 | Explicação simples de como o consentimento será registrado (presencial ou remoto) | CC01 item 4.4; OC23 item 2.2, IV | O |
| D03 | Destaque para o participante guardar cópia do documento eletrônico | CC01 item 2.2 | O |
| D04 | Envio ao participante do documento assinado por ele e pelo pesquisador | OC23 item 4.3, VII; R510 art. 17, § 3º; R466 IV.3 "f" | O/N |
| D05 | Direito de não responder qualquer pergunta; se houver pergunta obrigatória, o TCLE deve dizer que ele pode não respondê-la | CC01 itens 2.2.1 e 2.2.2 | O |
| D06 | Acesso prévio aos tópicos do instrumento; perguntas só depois do consentimento | CC01 itens 2.2.3 e 2.2.4 | O |
| D07 | Link ou instruções para retirar o consentimento, com resposta de ciência do pesquisador | CC01 item 4.2; OC23 item 5.4 | O |
| D08 | Se o questionário não for identificável, informar que os dados enviados não poderão ser excluídos | CC01 item 4.3 | O |
| D09 | Pesquisa de CHS: manifestação expressa sobre divulgação da identidade e das informações | CC01 item 3.4; R510 art. 9º, V | O/N |
| D10 | Custos: como serão assumidos quando a pesquisa usar só ferramentas gratuitas ou do pesquisador | CC01 item 2.6 | O |
| D11 | Possibilidade de acesso ao termo em papel ou em formato adequado à especificidade do participante | OC23 item 2.3, I | O |
| D12 | Horários e formas de contato com a equipe durante o processo de consentimento | OC23 item 2.2, VI | O |

## No convite e no processo (verificar no protocolo; no TCLE, só se o texto tratar disso)

| ID | Critério | Fontes verificadas | Nat. |
|---|---|---|---|
| D13 | Convite sem listas que exponham contatos: um remetente e um destinatário, ou lista oculta | CC01 itens 2.1 e 2.1.1 | O |
| D14 | Convite informa que o TCLE será apresentado antes das perguntas e que responder significa anuência | CC01 itens 2.1.2 e 2.5 (exceto os processos do art. 4º da R510, item 2.5.1) | O |
| D15 | Menores de 18 anos: primeiro contato com pais ou responsáveis; depois, assentimento | CC01 item 2.3 | O |
| D16 | Pesquisador conhece a política de privacidade da ferramenta e o risco de compartilhamento com terceiros | CC01 item 2.4 | O |
| D17 | Após a coleta, baixar os dados para dispositivo local e apagar da nuvem; o mesmo vale para gravações de consentimento | CC01 itens 3.2 e 3.3 | O (recomendação) |
| D18 | Sistema com acesso restrito e criptografia (ou medida equivalente justificada), envio individualizado, integridade e armazenamento seguro | OC23 itens 4.1 e 4.3 | O |
| D19 | Assinatura eletrônica conforme a classificação do art. 4º da Lei 14.063/2020 (ver nota abaixo) | OC23 item 4.3, I; L14063 art. 4º | O |
| D20 | Oportunidade de discutir as informações em tempo real antes de consentir | OC23 item 2.2, V | O |
| D21 | Orientação sobre a segurança do local onde o participante fará o consentimento | OC23 item 2.2, VII | O |
| D22 | Responsabilidade do pesquisador não se transfere à plataforma | OC23 item 2.2, III | O |

**Incerteza normativa:** a Lei 14.874/2024, art. 18, § 1º, exige TCLE "datado e assinado". A assinatura eletrônica e o "aceite" por clique em formulário não são tratados expressamente na Lei nem no Decreto. Não classifique o aceite eletrônico como pendência por si só: sinalize a incerteza e indique conferir o entendimento do CEP e eventual norma da Inaep.

**Lei 14.063/2020** (`references/texto/lei-14063-2020-assinaturas-eletronicas-planalto.txt`): o art. 4º, que o OC23 item 4.3, I, manda observar, classifica as assinaturas eletrônicas em:
- **simples:** identifica o signatário ou associa dados dele ao documento (art. 4º, I);
- **avançada:** vinculada ao signatário de forma unívoca, sob controle exclusivo dele, e que torna detectável qualquer alteração posterior (art. 4º, II);
- **qualificada:** usa certificado digital ICP-Brasil (art. 4º, III).

Ao citar essa lei, observe dois limites:
- O capítulo do art. 4º trata das interações com entes públicos. O art. 2º, parágrafo único, II, "a", exclui as interações entre particulares. A lei não fixa, por si, o nível de assinatura exigido para um TCLE. Use a classificação para descrever o mecanismo proposto (por exemplo, "o aceite por clique corresponde, no máximo, a assinatura simples"), não como exigência legal autônoma.
- O nível exigido depende do entendimento do CEP. Não há norma da Inaep sobre o tema na base.


---

# Módulo: material biológico, dados, uso futuro e transferência internacional

Aplique quando houver coleta ou armazenamento de material biológico humano, biobanco, biorrepositório, uso futuro de dados ou envio de dados ou amostras para fora do País. Siglas dos arquivos em `../criterios.md`.

**Transição:** o DEC art. 33 atribui à Inaep a nova norma de biobancos. A proposta de resolução foi objeto da Consulta Pública nº 01/2026, com prazo prorrogado até 02/07/2026 pelo Despacho Inaep nº 4/2026 (`references/texto/inaep-despacho-04-2026-dou.txt`). Em 20/11/2026, a página de legislação da Inaep não listava a resolução publicada. Até a publicação, a R441 vale no que não contrariar LEI e DEC (DEC art. 39). Recomende conferir se a nova resolução já foi publicada.

| ID | Critério | Fontes verificadas | Nat. |
|---|---|---|---|
| B01 | Consentimento para disposição de material e dados formalizado em TCLE, gratuito e altruísta | LEI art. 39 | N |
| B02 | Todos os direitos do art. 40 constam do TCLE | LEI art. 40, parágrafo único | N |
| B03 | Retirada do consentimento de guarda e uso, por escrito, com devolução das amostras | LEI art. 40, III; R441 item 10 e I | N |
| B04 | Acesso às informações associadas e orientação sobre achados, com aconselhamento genético quando cabível | LEI art. 40, V; R441 item 5 "b" | N |
| B05 | Opção expressa sobre uso futuro de dados e material | LEI art. 40, X; LEI art. 45; DEC art. 34 | N |
| B06 | Opção expressa sobre envio de dados e material para fora do País | LEI art. 40, XI; LEI art. 51, § 2º | N |
| B07 | Biobanco: escolha entre novo consentimento a cada pesquisa ou dispensa | R441 item 5, I e II | N |
| B08 | Biobanco: tipos de informação que poderão ser obtidos em pesquisas futuras | R441 item 5 "a" | N |
| B09 | Designação de representante para decidir em caso de óbito ou incapacidade | LEI art. 40, IX; R441 item 5 "c" | N |
| B10 | Informação sobre transferência, perda, descarte ou dissolução do repositório | LEI art. 40, VII e VIII; R441 item 5 "e" | N |
| B11 | Prazo de armazenamento: indeterminado em biobanco; conforme cronograma em biorrepositório | LEI arts. 41 e 42 | N |
| B12 | Propriedade do material é do participante; guarda institucional | LEI art. 43 | N |
| B13 | Dados compartilhados só anônimos ou codificados | LEI art. 51, § 1º | N |
| B15 | Consentimento obtido antes da incorporação da amostra ao biobanco; se a coleta for só para o biobanco, antes da coleta | OC23 item 3.1 e I | O |
| B16 | Consentimento eletrônico em biobanco: riscos do ambiente virtual, contato com a equipe e acesso ao termo em papel | OC23 itens 3.3, 3.5 e 3.6; ver `online-digital.md` | O |
| B14 | Base legal de tratamento de dados para pesquisa | LEI art. 61; LGPD art. 7º, IV; LGPD art. 11, II, "c"; LGPD art. 13 (saúde pública) | N |

**Pendências típicas:** MCL itens 1.21 (R441) e 1.22 (genes ou marcadores genéticos).


---

# Módulo: pesquisa multicêntrica

Aplique quando a pesquisa ocorrer em mais de um centro. Siglas dos arquivos em `../criterios.md`.

Fontes: Lei 14.874/2024, art. 14, § 7º; Decreto 12.651/2025, art. 27; **Despacho Inaep nº 3/2026 (D03)**, DOU de 01/06/2026, em vigor desde 08/06/2026, cujo item V trata do TCLE; e o Informe Técnico da Inaep (IMC, v1.1 de 30/09/2026), que o explica. Em divergência, prevalece o texto do despacho.

| ID | Critério | Fontes verificadas | Nat. |
|---|---|---|---|
| M01 | Protocolo único, analisado por um único CEP, preferencialmente o do centro coordenador | LEI art. 14, § 7º; DEC art. 27, §§ 1º e 2º; D03 item I, "a" a "c" | N |
| M02 | Endereço, telefone e e-mail do CEP responsável pela análise ética do protocolo único, de forma clara | D03 item V, "a" ("é obrigatório constar"); IMC 5.5 | O* |
| M03 | Contato do CEP local recomendado como canal complementar, sem gerar confusão sobre quem decide | D03 item V, "b"; IMC 5.5 | O |
| M04 | A ausência do contato do CEP local não é falha | D03 item V, "c" | O |
| M05 | Contato da Inaep é opcional; não substitui CEP e equipe | IMC 5.6 | O |
| M06 | Particularidades locais relevantes contempladas na versão final, com contribuição dos CEPs locais | D03 item V, "d"; IMC 5.3 e 5.4 | O |
| M07 | Modelo-base com campos locais delimitados; campos em aberto não podem conter elementos essenciais à decisão | IMC 5.2 e 5.8 | O |
| M08 | Canais de intercorrência e assistência reais no local do participante | IMC 5.3 e 5.7 | O |
| M09 | Controle documentado das versões usadas em cada centro | IMC 5.8 | O |

\* O D03 é um despacho de orientação para uniformizar entendimento no Sinep, mas usa a expressão "é obrigatório". Classifique a falta do contato do CEP responsável como pendência e cite D03 item V, "a", junto com R510 art. 17, IX, ou R466 IV.5 "d".

**Não peça como pendência:** contato do CEP local (D03 V, "c") nem contato da Inaep (IMC 5.6).

Mudanças só administrativas (telefone, endereço, cabeçalho, logomarca, formatação) podem seguir por notificação; mudanças que afetem compreensão, riscos, direitos, procedimentos ou assistência exigem emenda (IMC 5.9).

