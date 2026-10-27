def cari(data, nim):
    return data.get(nim, "Data tidak ditemukan")
mahasiswa = {
    "A001": {"nama": "Dita Amalia Veronica", "nilai": 100},
    "A002": {"nama": "Budi", "nilai": 78}
}
print(cari(mahasiswa, "A002"))
print(cari(mahasiswa, "A003"))