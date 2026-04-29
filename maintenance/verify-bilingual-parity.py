#!/usr/bin/env python3
from html.parser import HTMLParser
from pathlib import Path
import re
import sys


TRACKED_TAGS = {
    "section",
    "div",
    "h2",
    "h3",
    "h4",
    "p",
    "figure",
    "img",
    "figcaption",
    "ul",
    "ol",
    "li",
    "table",
    "thead",
    "tbody",
    "tr",
    "th",
    "td",
    "a",
    "strong",
    "em",
    "span",
    "code",
    "pre",
    "hr",
    "input",
    "label",
}


class SignatureParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.signature = []

    def handle_starttag(self, tag, attrs):
        if tag not in TRACKED_TAGS:
            return
        attr_map = dict(attrs)
        classes = " ".join((attr_map.get("class") or "").split())
        self.signature.append((tag, classes))

    handle_startendtag = handle_starttag


def extract_region(html, pattern, name):
    match = re.search(pattern, html, re.S)
    if not match:
        raise ValueError(f"Could not find {name}")
    return match.group(1)


def sections(region):
    return re.findall(r'<section class="chapter" id="([^"]+)">(.*?)</section>', region, re.S)


def signature(markup):
    parser = SignatureParser()
    parser.feed(markup)
    return parser.signature


def count(markup, needle):
    return markup.count(needle)


def main():
    html_path = Path(__file__).resolve().parents[1] / "chatgpt-codex-enterprise-settings.html"
    html = html_path.read_text()

    korean = extract_region(html, r'<main id="guide-main">(.*?)</main>', "Korean main")
    english = extract_region(html, r'<template id="english-main-template">(.*?)</template>', "English template")

    ko_sections = sections(korean)
    en_sections = sections(english)
    errors = []

    ko_ids = [section_id for section_id, _ in ko_sections]
    en_ids = [section_id for section_id, _ in en_sections]
    if ko_ids != en_ids:
        errors.append(f"section ids differ: KO={ko_ids} EN={en_ids}")

    for (section_id, ko_body), (_, en_body) in zip(ko_sections, en_sections):
        if signature(ko_body) != signature(en_body):
            errors.append(f"section signature differs: {section_id}")

    for needle, label in [
        ('<section class="chapter"', "sections"),
        ("<p", "paragraphs"),
        ("<a ", "links"),
        ("<code>", "code blocks"),
        ("<figure", "figures"),
        ("<table", "tables"),
    ]:
        ko_count = count(korean, needle)
        en_count = count(english, needle)
        if ko_count != en_count:
            errors.append(f"{label} differ: KO={ko_count} EN={en_count}")

    if errors:
        print("KO/EN parity check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("KO/EN structural parity check passed.")
    print("Manual review still required: confirm English matches Korean section-by-section in content depth and meaning.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
