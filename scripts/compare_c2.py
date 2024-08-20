import glob
import yaml

yaml_file_names = sorted(glob.glob("./collections/**/*.yaml", recursive=True))


def write_a1_to_c1():
    existing_words = []
    for i, yaml_file in enumerate(yaml_file_names):
        with open(yaml_file) as file:
            data = yaml.safe_load(file)
            existing_words.append(data["name"])
    with open("files/a1_to_c1.txt", "w") as f:
        for line in list(existing_words):
            f.write(f"{line}\n")


def remove_dublicates_from_c2():
    c2_text_file = open("c2.txt", "r")
    data = c2_text_file.read()
    c2_list = data.split("\n")
    without_dubs = sorted(list(set(c2_list)))
    without_dubs.sort()
    with open("files/c2_no_dubs.txt", "w") as f:
        for line in without_dubs:
            f.write(f"{line}\n")


def keep_only_new_in_c2():
    c2_no_dubs = open("files/c2_no_dubs.txt", "r")
    c2_no_dubs_data = c2_no_dubs.read()
    c2_no_dubs_list = c2_no_dubs_data.split("\n")

    a1_to_c1 = open("files/a1_to_c1.txt", "r")
    a1_to_c1_data = a1_to_c1.read()
    a1_to_c1_list = a1_to_c1_data.split("\n")

    only_new_in_c2 = list(set(c2_no_dubs_list) - set(a1_to_c1_list))
    only_new_in_c2.sort()
    print("only new:", len(only_new_in_c2))
    with open("files/only_new_in_c2.txt", "w") as f:
        for line in only_new_in_c2:
            f.write(f"{line}\n")


def count_existing():
    f = open("files/a1_to_c1.txt", "r")
    nr_of_lines = sum(1 for line in f)
    print("existing:", nr_of_lines)


def count_c2_without_dubs():
    f = open("files/c2_no_dubs.txt", "r")
    nr_of_lines = sum(1 for line in f)
    print("c2:", nr_of_lines)


def make_new_c2():
    print("Make new C1 ...")
    new_in_c2 = open("files/only_new_in_c2.txt", "r")
    new_in_c2_lines = new_in_c2.readlines()
    stripped = []
    for line in new_in_c2_lines:
        stripped.append(line.strip())
    stripped = list(filter(None, stripped))

    c2 = open("c2.txt", "r")
    c2_lines = c2.readlines()
    c2_lines = list(filter(None, c2_lines))
    c2_lines = list(set(c2_lines))
    with open("files/new_c2.txt", "w") as f:
        for line in c2_lines:
            if line and line.strip() in stripped:
                line.rstrip()
                f.write(line)


write_a1_to_c1()
remove_dublicates_from_c2()
keep_only_new_in_c2()

count_existing()
count_c2_without_dubs()

make_new_c2()
