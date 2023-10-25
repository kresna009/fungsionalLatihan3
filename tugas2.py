def konversi_menit(data):
    def minggu_ke_menit(minggu):
        def hari_ke_menit(hari):
            def jam_ke_menit(jam):
                def menit_ke_menit(menit):
                    return minggu * 7 * 24 * 60 + hari * 24 * 60 + jam * 60 + menit

                return menit_ke_menit

            return jam_ke_menit

        return hari_ke_menit

    def ekstrak_bilangan(entry):
        return list(filter(str.isdigit, entry.split()))

    output_data = []

    for entry in data:
        bilangan = ekstrak_bilangan(entry)
        output_data.append(bilangan)

    return output_data


data = [
    "3 minggu 3 hari 7 jam 21 menit",
    "5 minggu 5 hari 8 jam 11 menit",
    "7 minggu 1 hari 5 jam 33 menit",
]

outputData = konversi_menit(data)
for entry in outputData:
    print(entry)
