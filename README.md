# LP9DPBO2023C2
Saya Bayu Wicaksono NIM 2106836 mengerjakan lp9 dalam mata kuliah Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

## Deskripsi Tugas
1. Lengkapi fitur summary
2. Buat landing Page (button yg ngarah ke halaman daftar residen)
3. Tampilin gambar
4. Tambahin 1 metode yang masih relevan untuk setiap kelas

## Desain program
Pada program ini terdapat 4 class, yaitu :
1. Class Hunian
Class Hunian merepresentasikan suatu tempat hunian, Class ini memiliki beberapa atribut seperti jenis, jml_penghuni, jml_kamar, dan alamat. Selain itu, class ini juga memiliki beberapa method seperti get_jenis(), get_jml_penghuni(), get_jml_kamar(), get_alamat(), get_dokumen(), dan get_summary(). Method get_summary() mengembalikan sebuah string yang berisi informasi tentang jenis hunian, alamat, jumlah penghuni, dan jumlah kamar yang ada pada hunian tersebut. Method get_jenis(), get_jml_penghuni(), get_jml_kamar(), get_alamat() berfungsi untuk mengembalikan nilai dari atribut-atribut yang ada pada class.

2. Class Apartemen
Class apartemen merupakan turunan dari class Hunian dan merepresentasikan sebuah apartemen. Class Apartemen memiliki beberapa atribut yaitu nama_pemilik, jml_penghuni, jml_kamar, alamat, dan fasilitas. class Apartemen memiliki beberapa method yaitu get_dokumen(), get_nama_pemilik(), get_fasilitas(), dan add_fasilitas(fasilitas). Method get_dokumen() digunakan untuk mengembalikan dokumen sertifikat hak milik atas satuan rumah susun (SHMSRS) atas nama pemilik apartemen. Method get_nama_pemilik() digunakan untuk mengembalikan nama pemilik apartemen. Method get_fasilitas() digunakan untuk mengembalikan fasilitas yang dimiliki oleh apartemen. Method add_fasilitas(fasilitas) digunakan untuk menambahkan fasilitas baru ke dalam list fasilitas yang dimiliki oleh apartemen.

3. Class Rumah
Class Rumah merupakan turunan dari class Hunian dan merepresentasikan sebuah rumah. Class Rumah memiliki beberapa atribut yaitu nama_pemilik, harga, jml_penghuni, jml_kamar, dan alamat. Class ini memiliki beberapa method seperti method get_dokumen() yang mengembalikan dokumen izin mendirikan bangunan (IMB) atas nama pemilik rumah, method get_nama_pemilik() yang mengembalikan nama pemilik rumah, dan method get_harga() yang mengembalikan harga rumah.

4. Class Indekos
class Indekos merupakan turunan dari class Hunian dan merepresentasikan sebuah kos. Class Indekos memiliki atribut nama_pemilik, nama_penghuni, hargaPerBulan. class ini memiliki beberapa method seperti get_dokumen, get_nama_pemilik, get_nama_penghuni, dan get_hargaPerBulan. Method get_dokumen mengembalikan string “Bukti kontrak indekos oleh (nama penghuni) dari (nama pemilik).” sedangkan method get_nama_pemilik, get_nama_penghuni, dan get_hargaPerBulan masing-masing mengembalikan nilai dari atribut yang ada pada class.

## Penjelasan alur
1. Pada landing page, user dapat menekan tombol home untuk mengarah ke page daftar residen dan tombol exit untuk keluar dari program
2. Pada home page, user dapat melihat data daftar residen, untuk melihat detail dari tiap residen, user dapat menekan tombol detail dari data residen yang ingin dilihat detailnya. Jika ingin kembali ke landing page, user dapat menekan tombol back dan untuk keluar dari program user dapat menekan exit
3. Pada halaman detail, user dapat melihat data detail dari suatu residen, atribut yang terdapat di detail tiap residen itu berbeda beda tergantung pada jenis hunian yang ditempati oleh residen tersebut, karena tiap jenis hunian memiliki atribut uniknya masing-masing.
4. Untuk menambahkan data residen, user harus menambahkannya secara hard code pada program main

## Dokumentasi
- Landing Page

![landingpage](https://github.com/bwbayu/LP9DPBO2023C2/assets/100755457/9c17c885-2573-4f7c-9552-864e60ba25f9)


- Home page

![home](https://github.com/bwbayu/LP9DPBO2023C2/assets/100755457/ea154d7f-7dc2-41fc-98c0-96328286b73a)


- Detail Apartemen

![apartemen](https://github.com/bwbayu/LP9DPBO2023C2/assets/100755457/a89d6483-0a5c-4f9d-b11d-04060ddcbf5a)


- Detail Rumah

![rumah](https://github.com/bwbayu/LP9DPBO2023C2/assets/100755457/afcf922f-c2c9-495f-82e3-e151659a6590)


- Detail Indekos

![indekos](https://github.com/bwbayu/LP9DPBO2023C2/assets/100755457/428033f9-df23-4e96-a360-46830f893ec3)


- Video preview



https://github.com/bwbayu/LP9DPBO2023C2/assets/100755457/ecca52fb-087e-460b-a70a-e71af45f11f3

