# Javascript dan AJAX

Tugas 6 Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## Creator

> Nama : Fitria Dwi Cahya
> NPM : 2106751410
> Kelas : PBP - D

## Link Deployment:

[Todolist App 🧾](https://new-catalog-app.herokuapp.com/todolist)

## Perbedaan antara asynchronous programming dengan synchronous programming

1. Asynchronous Programming

- memiliki pendekatan pemrograman yang tidak terikat pada I/O Protocol.
- program dieksekusi tanpa harus terikat dengan proses lain

2. Synchronous Programming

- memiliki pendekatan pemrograman gaya lama dimana program akan dieksekusi satu persatu sesuai dengan urutan dan prioritasnya.
- waktu eksekusi lama karena tiap proses harus menunggu proses lain selesai.

## Paradigma Event-Driven Programming dalam Java Script dan AJAX

Event-driven adalah suatu paradigma pemrograman di mana program berjalan dengan alur berdasarkan event atau perilaku yang dilakukan antar user dan client.

Pada tugas 6, paradigma ini diterapkan ketika user menekan tombol "Add Task", maka program akan menampilkan modal berisikan form. User kemudian akan mengisi form tersebut, dan ketika user menekan tombol "Create Task" maka program akan menambahkan data baru ke dalam Todolist.

## Penerapan asynchronous programming pada AJAX

Penerapan asyncronous programming pada AJAX membuat browser dapat terus berjalan dan melaksanakan perintah lain. Oleh karena itu, AJAX dapat digunakan untuk mengubah tampilan website tanpa memerlukan _reload_. AJAX juga menggunakan paradigma _Event-Driven Programming_, di mana ketika AJAX diterapkan, dapat memanggil fungsi untuk menambahkan secara otomatis task baru ke program todolist.

Tahapan :

1. Tambahkan <script> yang memuat sebuah program JavaScript
2. Tambahkan library AJAX pada <head> <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script> di base.
3. Tambahkan program AJAX di dalam tag sesuai dengan keinginan.
4. Saat user melakukan sebuah event, event akan diproses dimana AJAX akan menampung semua event tersebut
5. AJAX akan melakukan transfer data secara server-side dengan metode asynchronous
6. Jika berhasil, maka halaman telah terperbarui secara otomatis dengan data baru.

## Implementasikan AJAX dan Java Script pada program

1. Menambahkan library AJAX pada <head> <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script> di base.
2. Membuat path `/todolist/json` pada urls.py dengan function yg sesuai untuk mengembalikan seluruh data task dalam bentuk json dan menggunakan AJAX GET untuk menampilkan data
3. Membuat tombol `Add Task `unutk membuka sebuah modal dengan form
4. Membuat path `/todolist/add` dengan funciton yang sesuai untuk menambahkan task baru
5. Hubungkan form yang telah dibuat di dalam modal ke path /todolist/add
6. Tutup modal setelah penambahan task telah berhasil dilakukan.
