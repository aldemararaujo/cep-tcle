"""Gera o pacote para GPT personalizado do ChatGPT a partir dos arquivos do plugin.

Uso (na raiz do repositório):
    python ferramentas/gerar_pacote_chatgpt.py

Saídas:
    chatgpt/conhecimento/   arquivos de conhecimento (13 arquivos, abaixo do limite de 20 do ChatGPT)
    dist/cep-tcle-gpt-chatgpt-<versão>.zip   instruções + conhecimento + guia, para anexar ao release

Rode sempre que a base normativa ou os critérios do plugin mudarem.
"""
import json
import shutil
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SKILL = RAIZ / "cep-tcle" / "skills" / "triagem-tcle"
TEXTO = SKILL / "references" / "texto"
SAIDA = RAIZ / "chatgpt" / "conhecimento"
DIST = RAIZ / "dist"

# arquivo de saída -> (título, [arquivos de origem em references/texto])
NORMAS = {
    "02-lei-14874-2024.txt": ("Lei nº 14.874/2024 (texto compilado do Planalto)", ["lei-14874-2024-compilada-planalto.txt"]),
    "03-decreto-12651-2025.txt": ("Decreto nº 12.651/2025", ["decreto-12651-2025-planalto.txt"]),
    "04-inaep-despachos-informes-notas.txt": ("Inaep: despachos, informes técnicos e notas técnicas", [
        "inaep-despacho-01-2026-dou.txt", "inaep-despacho-02-2026-dou.txt", "inaep-despacho-03-2026-dou.txt",
        "inaep-despacho-04-2026-dou.txt", "inaep-despacho-05-2026-dou.txt",
        "inaep-informe-tecnico-multicentricas-despacho-03-2026.txt", "inaep-informe-tecnico-despacho-05-2026.txt",
        "inaep-decit-nota-tecnica-43-2025-transicao-risco.txt", "inaep-decit-nota-tecnica-01-2026-transicao-biobancos.txt",
    ]),
    "05-res-cns-466-2012.txt": ("Resolução CNS nº 466/2012", ["res-cns-466-2012.txt"]),
    "06-res-cns-510-2016.txt": ("Resolução CNS nº 510/2016", ["res-cns-510-2016.txt"]),
    "07-res-cns-441-2011.txt": ("Resolução CNS nº 441/2011", ["res-cns-441-2011.txt"]),
    "08-norma-operacional-cns-001-2013.txt": ("Norma Operacional CNS nº 001/2013", ["norma-operacional-cns-001-2013.txt"]),
    "09-conep-oficios-e-cartas.txt": ("Conep: Ofício-Circular 11/2023, Carta Circular 1/2021 e Ofício Circular 23/2022", [
        "conep-oficio-circular-11-2023-assentimento.txt", "conep-carta-circular-01-2021-ambiente-virtual.txt",
        "conep-oficio-circular-23-2022-consentimento-eletronico.txt",
    ]),
    "10-manual-pendencias-clinica-2015.txt": ("Manual de pendências em pesquisa clínica (Conep, 2015)", ["conep-manual-pendencias-clinica-2015.txt"]),
    "11-manual-pendencias-chs-2023.txt": ("Manual de pendências em Ciências Humanas e Sociais (Conep, 2023)", ["conep-manual-pendencias-chs-2023.txt"]),
    "12-lgpd-lei-13709-2018.txt": ("LGPD, Lei nº 13.709/2018 (texto compilado do Planalto)", ["lgpd-lei-13709-2018-planalto.txt"]),
    "13-lei-14063-2020.txt": ("Lei nº 14.063/2020, assinaturas eletrônicas (texto compilado do Planalto)", ["lei-14063-2020-assinaturas-eletronicas-planalto.txt"]),
}

# sigla usada em criterios.md e nos módulos -> arquivo de conhecimento
SIGLAS = {
    "LEI": "02-lei-14874-2024.txt", "DEC": "03-decreto-12651-2025.txt",
    "D03": "04-inaep-despachos-informes-notas.txt", "D05": "04-inaep-despachos-informes-notas.txt",
    "IMC": "04-inaep-despachos-informes-notas.txt", "R466": "05-res-cns-466-2012.txt",
    "R510": "06-res-cns-510-2016.txt", "R441": "07-res-cns-441-2011.txt",
    "OC11": "09-conep-oficios-e-cartas.txt", "CC01": "09-conep-oficios-e-cartas.txt",
    "OC23": "09-conep-oficios-e-cartas.txt", "MCL": "10-manual-pendencias-clinica-2015.txt",
    "MCH": "11-manual-pendencias-chs-2023.txt", "LGPD": "12-lgpd-lei-13709-2018.txt",
    "L14063": "13-lei-14063-2020.txt",
}

MODULOS = ["clinico.md", "menores-assentimento.md", "chs-registro.md", "online-digital.md", "biobanco.md", "multicentrico.md"]


def versao():
    return json.loads((RAIZ / "cep-tcle" / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))["version"]


def ler(caminho: Path) -> str:
    return caminho.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n")


def gerar_criterios(v: str) -> str:
    linhas = [
        "# CEP - TCLE: critérios e módulos",
        "",
        f"Gerado do plugin CEP - TCLE versão {v} (github.com/aldemararaujo/cep-tcle).",
        "",
        "## Onde estão as normas neste GPT",
        "",
        "Os arquivos citados nas tabelas abaixo (pasta references/texto do plugin) foram agrupados nestes arquivos de conhecimento:",
        "",
        "| Sigla | Arquivo de conhecimento |",
        "|---|---|",
    ]
    linhas += [f"| {s} | {a} |" for s, a in SIGLAS.items()]
    linhas += ["", "Os caminhos `modulos/...` citados nas tabelas correspondem às seções \"Módulo\" mais abaixo neste mesmo arquivo.", "", "---", ""]
    linhas.append(ler(SKILL / "criterios.md"))
    for nome in MODULOS:
        linhas += ["", "---", "", ler(SKILL / "modulos" / nome)]
    return "\n".join(linhas) + "\n"


def main():
    v = versao()
    if SAIDA.exists():
        shutil.rmtree(SAIDA)
    SAIDA.mkdir(parents=True)

    (SAIDA / "01-criterios-e-modulos.md").write_text(gerar_criterios(v), encoding="utf-8", newline="\n")

    for destino, (titulo, origens) in NORMAS.items():
        partes = [f"{titulo}\nGerado do plugin CEP - TCLE versão {v}.\n"]
        for o in origens:
            partes.append(f"\n{'=' * 70}\nARQUIVO: {o}\n{'=' * 70}\n\n{ler(TEXTO / o)}")
        (SAIDA / destino).write_text("".join(partes), encoding="utf-8", newline="\n")

    arquivos = sorted(SAIDA.iterdir())
    assert len(arquivos) <= 20, "O ChatGPT aceita no máximo 20 arquivos de conhecimento"

    DIST.mkdir(exist_ok=True)
    zip_path = DIST / f"cep-tcle-gpt-chatgpt-{v}.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(RAIZ / "chatgpt" / "LEIA-ME.md", "LEIA-ME.md")
        z.write(RAIZ / "chatgpt" / "instrucoes-gpt.md", "instrucoes-gpt.md")
        for a in arquivos:
            z.write(a, f"conhecimento/{a.name}")

    instr = len((RAIZ / "chatgpt" / "instrucoes-gpt.md").read_text(encoding="utf-8"))
    print(f"Versão {v}: {len(arquivos)} arquivos de conhecimento; instruções com {instr} caracteres (limite 8000).")
    print(f"Pacote: {zip_path.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
