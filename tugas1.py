def minggu_ke_menit(minggu):
    def hari_ke_menit(hari):
        def jam_ke_menit(jam):
            def menit(menit):
                return minggu * 7 * 24 * 60 + hari * 24 * 60 + jam * 60 + menit

            return menit

        return jam_ke_menit

    return hari_ke_menit


def ekstrak_integer(entry):
    return list(map(int, filter(str.isdigit, entry.split())))


def konversi_ke_menit(entry):
    integers = ekstrak_integer(entry)
    if len(integers) >= 4:
        menit_ke_menit = minggu_ke_menit(integers[0])
        menit_ke_menit = menit_ke_menit(integers[1])
        menit_ke_menit = menit_ke_menit(integers[2])
        total_menit = menit_ke_menit(integers[3])
        return total_menit
    else:
        return None


def main():
    data = [
        "3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit",
    ]

    outputData = [konversi_ke_menit(entry) for entry in data]
    for entry in outputData:
        print(entry)


if __name__ == "__main__":
    main()
