import glob
import yaml

yaml_file_names = sorted(glob.glob("./collections/**/*.yaml", recursive=True))


def write_a1_to_b2():
    existing_words = []
    for i, yaml_file in enumerate(yaml_file_names):
        with open(yaml_file) as file:
            data = yaml.safe_load(file)
            existing_words.append(data["name"])
    with open("files/a1_to_b2.txt", "w") as f:
        for line in list(existing_words):
            f.write(f"{line}\n")


def remove_dublicates_from_c1():
    c1_text_file = open("c1.txt", "r")
    data = c1_text_file.read()
    c1_list = data.split("\n")
    without_dubs = sorted(list(set(c1_list)))
    without_dubs.sort()
    with open("files/c1_no_dubs.txt", "w") as f:
        for line in without_dubs:
            f.write(f"{line}\n")


def keep_only_new_in_c1():
    c1_no_dubs = open("files/c1_no_dubs.txt", "r")
    c1_no_dubs_data = c1_no_dubs.read()
    c1_no_dubs_list = c1_no_dubs_data.split("\n")

    a1_to_b2 = open("files/a1_to_b2.txt", "r")
    a1_to_b2_data = a1_to_b2.read()
    a1_to_b2_list = a1_to_b2_data.split("\n")

    only_new_in_c1 = list(set(c1_no_dubs_list) - set(a1_to_b2_list))
    only_new_in_c1.sort()
    print("only new:", len(only_new_in_c1))
    with open("files/only_new_in_c1.txt", "w") as f:
        for line in only_new_in_c1:
            f.write(f"{line}\n")


def count_existing():
    f = open("files/a1_to_b2.txt", "r")
    nr_of_lines = sum(1 for line in f)
    print("existing:", nr_of_lines)


def count_c1_without_dubs():
    f = open("files/c1_no_dubs.txt", "r")
    nr_of_lines = sum(1 for line in f)
    print("c1:", nr_of_lines)


def make_new_c1():
    print("Make new C1 ...")
    new_in_c1 = open("files/only_new_in_c1.txt", "r")
    new_in_c1_lines = new_in_c1.readlines()
    stripped = []
    for line in new_in_c1_lines:
        stripped.append(line.strip())
    stripped = list(filter(None, stripped))

    c1 = open("c1.txt", "r")
    c1_lines = c1.readlines()
    c1_lines = list(filter(None, c1_lines))
    c1_lines = list(set(c1_lines))
    with open("files/new_c1.txt", "w") as f:
        for line in c1_lines:
            if line and line.strip() in stripped:
                line.rstrip()
                f.write(line)


write_a1_to_b2()
remove_dublicates_from_c1()
keep_only_new_in_c1()

count_existing()
count_c1_without_dubs()

make_new_c1()
