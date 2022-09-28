# Pengimplementasian Form dan Autentikasi Menggunakan Django

Tugas 3 Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## Creator

> Nama : Fitria Dwi Cahya
> NPM : 2106751410
> Kelas : PBP - D

## Link Deployment:

[Todolist App 🧾](https://new-catalog-app.herokuapp.com/todolist)

## Kegunaan `{% csrf_token %}` pada elemen `<form>` dan apa yang terjadi apabila tidak ada potongan kode tersebut

- Token CSRF adalah nilai unik, rahasia, dan tidak terduga yang dihasilkan oleh aplikasi sisi server dan dikirimkan ke klien sehingga disertakan dalam permintaan HTTP berikutnya yang dibuat oleh klien. Saat permintaan dibuat, aplikasi sisi server memvalidasi bahwa permintaan tersebut menyertakan token yang diharapkan dan menolak permintaan jika token tidak ada atau tidak valid.
- Token CSRF berguna untuk melindungi semua data dari form yang menggunakan method POST dan mencegah serangan CSRF dengan cara membuat penyerang tidak dapat membuat permintaan HTTP yang valid sehingga penyerang tidak dapat membuat permintaan dengan semua parameter yang diperlukan aplikasi untuk memenuhi permintaan tersebut.
- Program yang tidak menggunakan token csrf_token pada <form> akan lebih mudah terserang oleh attacker sehingga akan berdampak buruk bagi keamanan data dari form tersebut. Attacker akan dengan mudah menggunakan authenticated state seorang user untuk mengirimkan request yang tidak sesuai dengan keinginan user.

## Membuat elemen `<form>` secara manual

`<form>` dapat dibuat secara manual dengan cara membuat tag `<form> .... </form>` . dan menambahkan atribut method="<http-request>" dan tag <input> untuk menerima input dari user diantara tag tersebut. Hal ini memungkinkan user untuk dapat memasukkan teks, memilih opsi, memanipulasi objek atau kontrol, dan seterusnya, dan kemudian mengirimkan informasi itu kembali ke server. Metode HTTP URL berguna untuk mengembalikan input pengguna. Kemudian, di dalam tag <input> tambahkan atribut `name="<nama-variable>"` agar data input dapat diambil oleh views.py dengan memanggil suatu perintah sesuai HTTP request.

## Proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan pada database, hingga munculnya pada _template_ HTML

## Implementasi checklist untuk todolist app
