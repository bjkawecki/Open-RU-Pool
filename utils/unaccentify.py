import unicodedata

ACCENT_MAPPING = {
    "а́": "а",
    "е́": "е",
    "и́": "и",
    "о́": "о",
    "у́": "у",
    "ы́": "ы",
    "э́": "э",
    "ю́": "ю",
    "я́": "я",
    "А́": "А",
    "Е́": "Е",
    "И́": "И",
    "О́": "О",
    "У́": "У",
    "Ы́": "Ы",
    "Э́": "Э",
    "Ю́": "Ю",
    "Я́": "Я",
}

ACCENT_MAPPING = {
    unicodedata.normalize("NFKC", i): j for i, j in ACCENT_MAPPING.items()
}


def unaccentify(s):
    source = unicodedata.normalize("NFKC", s)
    for old, new in ACCENT_MAPPING.items():
        source = source.replace(old, new)
    return source
