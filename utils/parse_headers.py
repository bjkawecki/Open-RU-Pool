from utils import enum


def parse_headers(headers, dataMap, row):
    for header in headers:
        row_header = row[header]
        if row_header:
            if header == "substantive_declination_class":
                dataMap["dec_cls"] = enum.declination[int(row_header)]
            elif header == "genus":
                dataMap["genus"] = enum.genus[int(row_header)]
            elif header == "stress":
                dataMap["stress"] = enum.stress[int(row_header)]
            elif header == "is_animated":
                dataMap["is_animate"] = True if row_header == "True" else False
            elif header == "singulare_tantum":
                dataMap["is_sin_tan"] = True if row_header == "True" else False
            elif header == "plurale_tantum":
                dataMap["is_plu_tan"] = True if row_header == "True" else False
            elif header == "is_gradable":
                dataMap["is_gradable"] = True if row_header == "True" else False
            elif header == "usage":
                dataMap["usage"] = enum.usage[int(row_header)]
            elif header == "etymology":
                dataMap["etymol"] = enum.etymol[int(row_header)]

            elif header == "numeral_type":
                dataMap["num_type"] = enum.num_type[int(row_header)]
            elif header == ("numeral_declination_type" or "pronoun_declination_type"):
                dataMap["dec_type"] = enum.dec_type[int(row_header)]

            elif header == "substantive_declination_class":
                dataMap["declination"] = enum.declination[int(row_header)]
            elif header == "preposition_type":
                dataMap["prep_type"] = enum.prep_type[int(row_header)]
            elif header == "preposition_case":
                dataMap["prep_case"] = enum.prep_case[int(row_header)]
            elif header == "pronoun_type":
                dataMap["pro_type"] = enum.pro_type[int(row_header)]
            elif header == "aspect":
                dataMap["aspect"] = enum.aspect[int(row_header)]
            elif header == "direction":
                dataMap["direction"] = enum.direction[int(row_header)]
            elif header == "conjugation_class":
                dataMap["conjugation"] = enum.conjugation[int(row_header)]
            elif header == "object_case":
                dataMap["obj_case"] = enum.obj_case[int(row_header)]
            elif header == "is_verb_of_motion":
                dataMap["is_motion_verb"] = True if row_header == "True" else False
            elif header == "reflexive":
                dataMap["is_reflexive"] = True if row_header == "True" else False
            else:
                dataMap[headers[header]] = row_header


def parse_translations(translations, dataMap, row):
    for translation in translations:
        row_translation = row[translation]
        if row_translation:
            dataMap[translations[translation]].append(row_translation)
