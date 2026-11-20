"""Exporta o relatório de triagem para .docx e a matriz de análise para .csv/.xlsx.

Uso:
    python -I exportar.py <relatorio.md> [--saida <pasta>]

- .docx: converte o Markdown inteiro com o pandoc.
- .csv: extrai a primeira tabela Markdown cujo cabeçalho tenha "Classificação".
- .xlsx: converte o .csv com o LibreOffice (soffice), se estiver instalado.

Só usa a biblioteca padrão. Ferramentas ausentes são informadas e puladas.
"""
import csv
import shutil
import subprocess
import sys
from pathlib import Path


def tabela_matriz(md: str) -> list[list[str]] | None:
    linhas = md.splitlines()
    i = 0
    while i < len(linhas):
        l = linhas[i].strip()
        if l.startswith("|") and "classifica" in l.lower():
            bloco = []
            while i < len(linhas) and linhas[i].strip().startswith("|"):
                bloco.append(linhas[i].strip())
                i += 1
            linhas_tab = [r for r in bloco if not set(r.replace("|", "").strip()) <= set("-: ")]
            return [[c.strip().replace("**", "") for c in r.strip("|").split("|")] for r in linhas_tab]
        i += 1
    return None


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    src =Path(sys.argv[1]).resolve()
    out = Path(sys.argv[sys.argv.index("--saida") + 1]).resolve() if "--saida" in sys.argv else src.parent
    out.mkdir(parents=True, exist_ok=True)
    md = src.read_text(encoding="utf-8")
    base = out / src.stem

    pandoc = shutil.which("pandoc")
    if pandoc:
        subprocess.run([pandoc, str(src), "-f", "gfm", "-o", f"{base}.docx"], check=True)
        print(f"DOCX: {base}.docx")
    else:
        print("pandoc não encontrado; .docx não gerado.")

    tab = tabela_matriz(md)
    if not tab:
        print("Nenhuma tabela com coluna 'Classificação' encontrada; .csv/.xlsx não gerados.")
        return
    with open(f"{base}-matriz.csv", "w", newline="", encoding="utf-8-sig") as f:
        csv.writer(f, delimiter=";").writerows(tab)
    print(f"CSV: {base}-matriz.csv ({len(tab) - 1} linhas)")

    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    if not soffice:
        for c in (r"C:\Program Files\LibreOffice\program\soffice.exe",
                  "/Applications/LibreOffice.app/Contents/MacOS/soffice"):
            if Path(c).exists():
                soffice = c
                break
    if soffice:
        subprocess.run([soffice, "--headless", "--infilter=CSV:59,34,76", "--convert-to", "xlsx",
                        "--outdir", str(out), f"{base}-matriz.csv"],
                       check=True, capture_output=True)
        print(f"XLSX: {base}-matriz.xlsx")
    else:
        print("LibreOffice não encontrado; .xlsx não gerado (o .csv abre no Excel).")


if __name__ == "__main__":
    main()
