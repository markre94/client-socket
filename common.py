import csv
import hashlib
import random

from faker import Faker

BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

sha1 = hashlib.sha1()


def calc_sha1_sum(file: str):
    with open(file, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha1.update(data)
            return sha1.hexdigest()


def generate_random_file():
    with open("data.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name", "age", "email", "occupation"])
        writer.writeheader()
        for i in range(1, 501):
            f = Faker()
            writer.writerow({"id": i,
                             "name": f.name(),
                             "age": random.randint(10, 55),
                             "email": f.email(),
                             "occupation": f.job()})


if __name__ == '__main__':
    # generate_random_file()
    pass
