import glob
import yaml

yaml_file_names = sorted(glob.glob("./collections/**/*.yaml", recursive=True))


def write_a1_to_b1():
    existing_words = []
    for i, yaml_file in enumerate(yaml_file_names):
        with open(yaml_file) as file:
            data = yaml.safe_load(file)
            existing_words.append(data["name"])
    with open("files/a1_to_b1.txt", "w") as f:
        for line in list(existing_words):
            f.write(f"{line}\n")


def remove_dublicates_from_b2():
    b2_text_file = open("b2.txt", "r")
    data = b2_text_file.read()
    b2_list = data.split("\n")
    without_dubs = sorted(list(set(b2_list)))
    without_dubs.sort()
    with open("files/b2_no_dubs.txt", "w") as f:
        for line in without_dubs:
            f.write(f"{line}\n")


def keep_only_new_in_b2():
    b2_no_dubs = open("files/b2_no_dubs.txt", "r")
    b2_no_dubs_data = b2_no_dubs.read()
    b2_no_dubs_list = b2_no_dubs_data.split("\n")

    a1_to_b1 = open("files/a1_to_b1.txt", "r")
    a1_to_b1_data = a1_to_b1.read()
    a1_to_b1_list = a1_to_b1_data.split("\n")

    only_new_in_b2 = list(set(b2_no_dubs_list) - set(a1_to_b1_list))
    only_new_in_b2.sort()
    print("only new:", len(only_new_in_b2))
    with open("files/only_new_in_b2.txt", "w") as f:
        for line in only_new_in_b2:
            f.write(f"{line}\n")


def count_existing():
    f = open("files/a1_to_b1.txt", "r")
    nr_of_lines = sum(1 for line in f)
    print("existing:", nr_of_lines)


def count_b2_without_dubs():
    f = open("files/b2_no_dubs.txt", "r")
    nr_of_lines = sum(1 for line in f)
    print("b2:", nr_of_lines)


def make_new_b2():
    print("Make new B2 ...")
    new_in_b2 = open("files/only_new_in_b2.txt", "r")
    new_in_b2_lines = new_in_b2.readlines()
    stripped = []
    for line in new_in_b2_lines:
        stripped.append(line.strip())
    stripped = list(filter(None, stripped))

    b2 = open("b2.txt", "r")
    b2_lines = b2.readlines()
    b2_lines = list(filter(None, b2_lines))
    b2_lines = list(set(b2_lines))
    with open("files/new_b2.txt", "w") as f:
        for line in b2_lines:
            if line and line.strip() in stripped:
                line.rstrip()
                f.write(line)


write_a1_to_b1()
remove_dublicates_from_b2()
keep_only_new_in_b2()

count_existing()
count_b2_without_dubs()

make_new_b2()
