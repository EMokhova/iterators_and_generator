import hashlib


def get_hash(file_path):
    with open(file_path) as file:
        for line in file:
            yield hashlib.md5(line.encode()).hexdigest()


if __name__ == '__main__':
    for hash_str in get_hash('links.txt'):
        print(hash_str)
