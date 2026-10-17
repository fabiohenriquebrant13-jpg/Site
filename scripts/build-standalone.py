#!/usr/bin/env python3
"""Gera a versão independente a partir do index.html, sem dependências externas."""
import argparse
import base64
import mimetypes
from pathlib import Path
import re


def build(source: Path) -> str:
    root = source.parent
    html = source.read_text(encoding="utf-8")
    css_images: dict[str, str] = {}

    def data_uri(relative: str) -> str:
        target = (root / relative).resolve()
        if not target.is_relative_to(root.resolve()):
            raise ValueError(f"Recurso fora do projeto: {relative}")
        mime = mimetypes.guess_type(target.name)[0] or "application/octet-stream"
        encoded = base64.b64encode(target.read_bytes()).decode("ascii")
        return f"data:{mime};base64,{encoded}"

    def embed_img(match: re.Match) -> str:
        tag = re.sub(r'\s+(?:srcset|sizes)="[^"]*"', "", match.group(0))
        return re.sub(
            r'\bsrc="(assets/[^\"]+)"',
            lambda item: f'src="{data_uri(item.group(1))}"',
            tag,
        )

    def embed_css(match: re.Match) -> str:
        relative = match.group(1)
        if relative not in css_images:
            css_images[relative] = f"--embedded-image-{len(css_images)}"
        return f"var({css_images[relative]})"

    # Uma única imagem adequada por <img> mantém o HTML portátil enxuto.
    # A versão publicada conserva srcset/sizes para seleção pelo navegador.
    html = re.sub(r'<img\b[^>]*>', embed_img, html)
    html = re.sub(r"url\(['\"]?(assets/[^'\")]+)['\"]?\)", embed_css, html)
    html = re.sub(
        r'(<link\b[^>]*\bhref=")((?:assets/[^\"]+|favicon\.ico))(")',
        lambda match: match.group(1) + data_uri(match.group(2)) + match.group(3),
        html,
    )
    variables = ":root{" + "".join(
        f'{name}:url("{data_uri(relative)}");'
        for relative, name in css_images.items()
    ) + "}"
    html = html.replace("<style>", "<style>\n" + variables, 1)
    return html


def main() -> None:
    project = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=project / "index.html")
    parser.add_argument("--output", type=Path, default=project / "ferreira-motores-completo.html")
    args = parser.parse_args()
    if args.source.resolve() == args.output.resolve():
        parser.error("A saída deve ser diferente do HTML de origem.")
    html = build(args.source.resolve())
    args.output.write_text(html, encoding="utf-8")
    print(f"HTML independente gerado: {args.output.name} ({len(html.encode('utf-8'))} bytes)")


if __name__ == "__main__":
    main()
