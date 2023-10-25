random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

# Filter untuk memisahkan float, integer, dan string
float_data = list(filter(lambda x: isinstance(x, float), random_list))
int_data = list(filter(lambda x: isinstance(x, int), random_list))
string_data = list(filter(lambda x: isinstance(x, str), random_list))


# Fungsi untuk memetakan nilai integer ke satuan, puluhan, ratusan, dan seterusnya
def map_int(x):
    digits = [int(d) for d in str(x)]
    mapped_data = {}
    for i, digit in enumerate(digits):
        place = len(digits) - i
        if place == 1:
            place_name = "satuan"
        elif place == 2:
            place_name = "puluhan"
        else:
            place_name = "ratusan"
        mapped_data[place_name] = digit
    return mapped_data


mapped_int_data = list(map(map_int, int_data))

print("Data Float:", float_data)
print("Data Int:", int_data)
print("Mapped Data Int:", mapped_int_data)
print("Data String:", string_data)