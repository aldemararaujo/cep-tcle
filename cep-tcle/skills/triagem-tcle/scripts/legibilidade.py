"""Indicadores de legibilidade de um TCLE em português.

Uso:
    python -I legibilidade.py <arquivo.txt|.md|.pdf|.docx> [--json]

Calcula o Índice de Legibilidade de Flesch adaptado ao português
(Martins et al., 1996): 248,835 - 1,015 x (palavras/frase) - 84,6 x (sílabas/palavra),
além de tamanho médio das frases e a lista das frases mais longas.

O resultado é um dado auxiliar para o critério de linguagem acessível. A contagem de
sílabas é heurística e o índice não mede compreensão real nem adequação ao público.
Só usa a biblioteca padrão; para PDF precisa do pdftotext (Poppler) no PATH.
"""
import json
import re
import shutil
import subprocess
import sys
import unicodedata
import zipfile
from pathlib import Path

VOGAIS = "aeiouáéíóúâêôãõàüy"
# Ditongos e tritongos comuns que contam como uma sílaba (heurística).
DITONGOS = re.compile(
    r"(uai|uei|uão|uõe|ai|ei|oi|ui|au|eu|iu|ou|ão|ãe|õe|ua(?=[^aeiou]|$)|ue(?=[^aeiou]|$)|uo)"
)


def ler_texto(caminho: Path) -> str:
    suf = caminho.suffix.lower()
    if suf in (".txt", ".md"):
        return caminho.read_text(encoding="utf-8", errors="replace")
    if suf == ".pdf":
        exe = shutil.which("pdftotext")
        if not exe:
            sys.exit("pdftotext não encontrado; converta o PDF para .txt antes.")
        return subprocess.run([exe, "-enc", "UTF-8", str(caminho), "-"],
                              capture_output=True, text=True, encoding="utf-8").stdout
    if suf == ".docx":
        with zipfile.ZipFile(caminho) as z:
            xml = z.read("word/document.xml").decode("utf-8")
        xml = re.sub(r"</w:p>", "\n", xml)
        return re.sub(r"<[^>]+>", "", xml)
    sys.exit(f"Formato não suportado: {suf}")


def silabas(palavra: str) -> int:
    p = palavra.lower()
    # í e ú acentuados depois de vogal formam hiato (sa-ú-de, pa-ís, pre-ju-í-zo).
    p = re.sub(f"(?<=[{VOGAIS}])([íú])", r"-\1", p)
    p = DITONGOS.sub("a", p)
    n = len(re.findall(f"[{VOGAIS}]+", p))
    return max(1, n)


def frases(texto: str) -> list[str]:
    texto = re.sub(r"\s+", " ", texto)
    # Não quebra em abreviaturas comuns.
    texto = re.sub(r"\b(Sr|Sra|Dr|Dra|art|Art|nº|n|inc|p|ex|etc)\.", r"\1<P>", texto)
    partes = re.split(r"(?<=[.!?;:])\s+(?=[A-ZÁÉÍÓÚÂÊÔÃÕÀÇ0-9\"“(])", texto)
    return [p.replace("<P>", ".").strip() for p in partes if re.search(r"\w", p)]


def palavras(frase: str) -> list[str]:
    return re.findall(r"[A-Za-zÀ-ÿ]+(?:-[A-Za-zÀ-ÿ]+)*", frase)


def faixa(indice: float) -> str:
    if indice >= 75:
        return "muito fácil (até ~4ª série do ensino fundamental)"
    if indice >= 50:
        return "fácil (~5ª a 8ª série do ensino fundamental)"
    if indice >= 25:
        return "difícil (ensino médio ou superior)"
    return "muito difícil (área acadêmica)"


def analisar(texto: str) -> dict:
    texto = unicodedata.normalize("NFC", texto)
    fs = frases(texto)
    pals_por_frase = [palavras(f) for f in fs]
    fs_validas = [(f, p) for f, p in zip(fs, pals_por_frase) if p]
    todas = [w for _, p in fs_validas for w in p]
    if not todas:
        return {"erro": "texto vazio ou ilegível"}
    n_frases, n_pal = len(fs_validas), len(todas)
    n_sil = sum(silabas(w) for w in todas)
    pf, sp = n_pal / n_frases, n_sil / n_pal
    indice = 248.835 - 1.015 * pf - 84.6 * sp
    longas = sorted(fs_validas, key=lambda x: len(x[1]), reverse=True)
    return {
        "frases": n_frases,
        "palavras": n_pal,
        "palavras_por_frase": round(pf, 1),
        "silabas_por_palavra": round(sp, 2),
        "indice_flesch_pt": round(indice, 1),
        "faixa": faixa(indice),
        "frases_acima_de_30_palavras": sum(1 for _, p in fs_validas if len(p) > 30),
        "maiores_frases": [{"palavras": len(p), "inicio": f[:160]} for f, p in longas[:5]],
        "aviso": "Indicador heurístico; não mede compreensão nem substitui avaliação humana.",
    }


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    r = analisar(ler_texto(Path(sys.argv[1])))
    if "--json" in sys.argv:
        print(json.dumps(r, ensure_ascii=False, indent=2))
        return
    if "erro" in r:
        sys.exit(r["erro"])
    print(f"Frases: {r['frases']} | Palavras: {r['palavras']}")
    print(f"Palavras por frase: {r['palavras_por_frase']} | Sílabas por palavra: {r['silabas_por_palavra']}")
    print(f"Índice de Flesch (pt): {r['indice_flesch_pt']} -> {r['faixa']}")
    print(f"Frases com mais de 30 palavras: {r['frases_acima_de_30_palavras']}")
    print("Maiores frases:")
    for f in r["maiores_frases"]:
        print(f"  ({f['palavras']} palavras) {f['inicio']}...")
    print(r["aviso"])


if __name__ == "__main__":
    main()
