def print_tables(num):
    for i in range(1,11):
        yield (f"{num} X {i} = {num * i}")


if __name__ == "__main__":
    print_tables(5)


