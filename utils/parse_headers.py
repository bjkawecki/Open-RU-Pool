from utils import enums

header_dict = {
    "substantive_declination_class": "dec_cls",
    "genus": "genus",
    "stress": "stress",
    "usage": "usage",
    "etymology": "etymol",
    "numeral_type": "num_type",
    "numeral_declination_type": "dec_type",
    "pronoun_declination_type": "dec_type",
    "preposition_type": "prep_type",
    "preposition_case": "prep_case",
    "pronoun_type": "pro_type",
    "aspect": "aspect",
    "direction": "direction",
    "conjugation_class": "con_cls",
    "object_case": "obj_case",
}

header_dict_booleans = {
    "is_animated": "is_animate",
    "singulare_tantum": "is_sin_tan",
    "plurale_tantum": "is_plu_tan",
    "is_gradable": "is_gradable",
    "is_verb_of_motion": "is_motion_verb",
    "reflexive": "is_reflexive",
}


def parse_headers(headers, dataMap, row):
    for header in headers:
        row_header = row[header]
        if row_header:
            dataMap[headers[header]] = row_header
            new_header = header_dict.get(header)
            if new_header:
                new_header_dict = getattr(enums, new_header)
                dataMap[new_header] = new_header_dict[int(row_header)]

            new_header_boolean = header_dict_booleans.get(header)
            if new_header_boolean:
                new_header_boolean = header_dict_booleans.get(header)
                dataMap[new_header_boolean] = True if row_header == "True" else False


def parse_translations(translations, dataMap, row):
    for translation in translations:
        row_translation = row[translation]
        if row_translation:
            dataMap[translations[translation]].append(row_translation)
