#!/usr/bin/env python3
"""Monta o ZIP da Hostinger com as páginas, configuração 404 e recursos locais."""
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED


class Assets(HTMLParser):
    def __init__(self):
        super().__init__()
        self.paths = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for name in ("src", "href"):
            if name in attrs:
                self.add(attrs[name])
        if "srcset" in attrs:
            for candidate in attrs["srcset"].split(","):
                self.add(candidate.strip().split()[0])

    def add(self, value):
        parsed = urlsplit(value)
        if not parsed.scheme and not parsed.netloc and parsed.path.strip("/"):
            self.paths.add(unquote(parsed.path).lstrip("/"))


def main():
    root = Path(__file__).resolve().parent.parent
    source = root / "index.html"
    parser = Assets()
    published = {"index.html", "404.html", ".htaccess", "favicon.ico"}
    for page in (source, root / "404.html"):
        html = page.read_text(encoding="utf-8")
        parser.feed(html)
        for ref in re.findall(r"url\(['\"]?([^'\")]+)['\"]?\)", html):
            parser.add(ref)
    files = [root / name for name in sorted(published)]
    for name in sorted(parser.paths):
        target = (root / name).resolve()
        if not target.is_relative_to((root / "assets").resolve()):
            if name in published:
                continue
            raise ValueError(f"Recurso não publicável: {name}")
        if not target.is_file():
            raise FileNotFoundError(name)
        files.append(target)
    archive = root / "Ferreira-Motores-Site-v2.zip"
    with ZipFile(archive, "w", compression=ZIP_DEFLATED, compresslevel=9) as output:
        for file in files:
            info = ZipInfo(file.relative_to(root).as_posix(), datetime.now().timetuple()[:6])
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = ZIP_DEFLATED
            output.writestr(info, file.read_bytes())
    with ZipFile(archive) as output:
        assert output.testzip() is None
        assert output.read("index.html") == source.read_bytes()
    print(f"ZIP gerado: {archive.name}, {len(files)} arquivos, {archive.stat().st_size} bytes")


if __name__ == "__main__":
    main()
