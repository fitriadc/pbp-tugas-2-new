# Pengimplementasian Form dan Autentikasi Menggunakan Django

Tugas 3 Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## Creator

> Nama : Fitria Dwi Cahya
> NPM : 2106751410
> Kelas : PBP - D

## Link Deployment:

[Todolist App 🧾](https://new-catalog-app.herokuapp.com/todolist)

## Kegunaan `{% csrf_token %}` pada elemen `<form>` dan apa yang terjadi apabila tidak ada potongan kode tersebut

- Token CSRF (Cross Site Request Forgery) adalah nilai unik, rahasia, dan tidak terduga yang dihasilkan oleh aplikasi sisi server dan dikirimkan ke klien sehingga disertakan dalam permintaan HTTP berikutnya yang dibuat oleh klien. Saat permintaan dibuat, aplikasi sisi server memvalidasi bahwa reques tersebut menyertakan token yang diharapkan dan menolak request jika token tidak ada atau tidak valid.
- Token CSRF berguna untuk melindungi semua data dari form yang menggunakan method POST dan mencegah serangan CSRF dengan cara membuat penyerang tidak dapat membuat permintaan HTTP yang valid sehingga penyerang tidak dapat membuat permintaan dengan semua parameter yang diperlukan aplikasi untuk memenuhi permintaan tersebut.
- Program yang tidak menggunakan token csrf_token pada <form> akan lebih mudah terserang oleh attacker sehingga akan berdampak buruk bagi keamanan data dari form tersebut. Attacker akan dengan mudah menggunakan authenticated state seorang user untuk mengirimkan request yang tidak sesuai dengan keinginan user.

## Membuat elemen `<form>` secara manual

- Formulir didefinisikan dalam HTML sebagai kumpulan elemen di dalam tag <form>…</form>, yang mengandung setidaknya satu elemen input type="submit".`<form>` dapat dibuat secara manual dengan cara membuat tag `<form> .... </form>` . dan menambahkan atribut method="<http-request>" dan tag <input> untuk menerima input dari user diantara tag tersebut. Hal ini memungkinkan user untuk dapat memasukkan teks, memilih opsi, memanipulasi objek atau kontrol, dan seterusnya, dan kemudian mengirimkan informasi itu kembali ke server. Metode HTTP URL berguna untuk mengembalikan input pengguna. Kemudian, di dalam tag <input> tambahkan atribut `name="<nama-variable>"` agar data input dapat diambil oleh views.py dengan memanggil suatu perintah sesuai HTTP request.

```html
<form action="/team_name_url/" method="post">
  <label for="team_name">Enter name: </label>
  <input
    id="team_name"
    type="text"
    name="name_field"
    value="Default name for team."
  />
  <input type="submit" value="OK" />
</form>
```

- `action` : URL tempat data dikirim untuk diproses saat formulir dikirimkan. Jika ini tidak disetel (atau disetel ke string kosong), maka formulir akan dikirimkan kembali ke URL halaman saat ini.
- `method` : Metode HTTP yang digunakan untuk mengirim data. Jenisnya ada dua, yaitu `post` dan `get`. Metode POST harus selalu digunakan jika terdapat perubahan pada database server, karena dapat dibuat lebih tahan terhadap serangan permintaan pemalsuan lintas situs. Sementara itu, Method GET hanya boleh digunakan untuk formulir yang tidak mengubah data pengguna (misalnya, formulir pencarian). Disarankan ketika Anda ingin dapat mem-bookmark atau membagikan URL.

## Proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan pada database, hingga munculnya pada _template_ HTML

![Bagan](assets/form_handling_-_standard.png "form-handling-image")

- User terlebih dahulu mengisi `form` kemudian data akan divalidasi. Jika data tersebut tidak valid, maka server akan mengirimi pesan error dan meminta user mengisi kembali data yang valid. Jika data valid, data akan disimpan pada browser/internet pengguna. Setelah pengguna menekan tombol submit, form akan terkirim sebagai HTTP request POST dengan method dan url yang sudah ditentukan oleh attribute dari form tersebut.
- Pada saat user klik submit maka data-data yang diinput oleh user akan masuk ke dalam database melalui views.py yang akan menghubungkannya ke models kemudian ke database. Data akan disimpan ke dalam variabel. Selanjutnya, akan dibuat object baru (dalam project ini `Todolist`) yang akan langsung disimpan ke dalam database menggunakan perintah <object>.save().
- Jika data ingin ditampilkan, kita dapat menampilkan data tersebut di template HTML. Pada main function di Views (dalam hal ini `show_todolist`), akan didapatkan semua data (dalam hal ini objects Todolist) sesuai dengan kepemilikan masing-masing dengan cara menggunakan perintah `Task.objects.filter(user_id=request.user.id)`. Data dapat diakses dari database melalui http request method "GET" seperti berikut `request.POST.get("<name>")` dan disimpan ke suatu variabel. Data kemudian dikirimkan dengan cara melakukan `render`ke template HTML sebagai contex sehingga user dapat melihat tampilan data tersebut dalam format html.

## Implementasi checklist untuk todolist app

### Membuat aplikasi todolist di proyek tugas Django yang sudah digunakan sebelumnya.

Pembuatan django app `todolist` dengan perintah `python manage.py startapp todolist`

### Menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist.

Menambahkan `path('', include('todolist.urls'))` pada urls.py di project_django. Selain itu tambahakan `'todolist',`pada `INSTALLED_APPS`pada settings.py di project_django.

### Membuat sebuah model Task dengan atribut user, date, title, dan description

Membuat models.py dengan menambahkan beberapa atribut, atribut-atributnya adalah user, date, title, description, dan is_finished seperti berikut :

```python
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(datetime.now, default=datetime.now)
    title = models.CharField(max_length=280)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)
```

Lakukan migrasi data untuk memasukan models dengan cara `python manage.py makemigration` dan `python manage.py migrate`.

### Mengimplementasikan form registrasi, login, dan logout

Membuat form registrasi menggunakan `UserCreationForm()` di views.py. kemudian membuat fungsi pada views.py untuk login dan logout yang diintegrasikan dengan form pada html dengan method POST. Berikut adalah fungsi yang diperlukan.

- Fungsi `show_todolist` untuk menghubungkan data user dan todolistnya ke file `todolist.html`

```python
def show_todolist(request):
    username = request.user.username
    #id = request.user.id
    todo = Task.objects.filter(user=request.user)
    context = {
        'data_todolist': todo,
        'username': username,
        # 'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)
```

- Fungsi create_todo untuk menghubungkan data input baru dari halaman `create_todo.html` ke database

```python
def create_todo(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        new_todo = Task(user=request.user, title=title,
                        description=description)
        new_todo.save()
        return redirect('todolist:show_todolist')
    return render(request, "create_todo.html")

```

- Fungsi registrasi akun

```python
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')

    context = {'form': form}
    return render(request, 'register.html', context)

```

- Fungsi untuk login user

```python

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(
                reverse("todolist:show_todolist"))  # membuat response
            # membuat cookie last_login dan menambahkannya ke dalam response
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

```

- Fungsi untuk log out akun user

```python

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

```

- (BONUS) Fungsi untuk memperbarui status pengerjaan tugas di todolist. User dapat merubah status pengerjaan dari belum selesai (unfinished) ke selesai(finished) atau sebaliknya.

```python
def update_task_status(request, id):
    task = Task.objects.get(pk=id)
    if task.is_finished:
        task.is_finished = False
    else:
        task.is_finished = True
    task.save()
    return redirect('todolist:show_todolist')

```

- (BONUS) Fungsi untuk menghapus data tugas.

```python
def delete_task(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('todolist:show_todolist')

```

### Membuat halaman utama todolist

Membuat file `todolist.html`yang berisi label bertuliskan user yang terlogin, tombol untuk membuat task baru, tombol logout yang terhubung ke function logout, dan tabel dengan kolom sesuai attribute Task untuk menampilkan semua task dari user yang terlogin. Fungsi pada views.py akan melakukan render todolist.html yang sebelumnya perlu ditambahkan routing ke function tersebut.

```html
<right>
  <button><a href="{% url 'todolist:logout' %}">Logout</a></button>
</right>
<button><a href="{% url 'todolist:create_todo' %}">Add New Task</a></button>

<center>
  <table border="1" cellspacing="2" cellpadding="8" align="left">
    <tr>
      <th>Date Create</th>
      <th>Task Name</th>
      <th>Description</th>
      <th>Status</th>
    </tr>
    {% for task in data_todolist %}
    <tr>
      <td align="center">{{task.date}}</td>
      <td align="left">{{task.title}}</td>
      <td align="center">{{task.description}}</td>
      {% if task.is_finished %}
      <td>Finished</td>
      {% else %}
      <td>Unfinished</td>
      {% endif %}

      <td>
        <a href="update/{{task.pk}}"><button>Update Status</button></a>
      </td>

      <td>
        <a href="delete/{{task.pk}}"><button>Delete Task</button></a>
      </td>
    </tr>
    {% endfor %}
  </table>
</center>
```

### Membuat halaman form untuk pembuatan task

Saat membuat todolist baru diperlukan beberapa data baru seperti judul dan deskripsi. Melalui form dan fungsi `create_todo`pada views, data baru akan terbuat. Fungsi ini akan ditampilkan pada HTML berikut

```HTML
<form method="POST" action="">
  {% csrf_token %}
  <div>
    <label for="title">Task Title: </label>
    <input id="title" type="text" name="title" placeholder="Title" required />
  </div>
  <div>
    <label for="description">Description: </label>
    <input
      id="description"
      type="text"
      name="description"
      placeholder="Description"
      required
    />
  </div>
  <input type="submit" value="Create" />
</form>
```

### Membuat routing sehingga beberapa fungsi dapat diakses melalui URL tertentu

Pada urls.py, tambahkan path ke dalam urlpatters

```python
 path('', show_todolist, name="show_todolist"),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-todo/', create_todo, name="create_todo"),
    path('delete/<int:id>', delete_task, name="delete_task"),
    path('update/<int:id>', update_task_status, name="update_task_status"),
```

### Melakukan deployment aplikasi todolist ke Heroku

Jalankan proyek Django dengan perintah python manage.py runserver dan bukalah http://localhost:8000/todolist di browser. Pastikan template todolist.html tampil dengan baik dan data dari model dapat dirender oleh views ke todolist.html. Lakukanlah tahapan `git add, commit, and push` terhadap changes yang kamu lakukan.

## Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.

Buka aplikasi [Todolist App 🧾](https://new-catalog-app.herokuapp.com/todolist). Kemudian buat 2 akun pengguna baru. Pada tiap akunnya lakukan login, kemudian buat 3 tugas baru dengan cara menekan tombol `Create New Task`. Di halaman Creat Your New Task, isi data yang dibutuhkan kemudian tekan tombol `Create` untuk menyimpan data. Pastikan data baru telah muncul pada tabel todolist di halaman utama.

## Referensi

Flow Data 🧾 : [https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms)

# Web Design Using HTML, CSS, and CSS Framework

## Perbedaan Inline, Internal, dan External CSS

1. Inline CSS: kode CSS ditulis langsung pada atribut elemen HTML dengan cara mendeklarasikan atribut `style` pada tag HTML. Contoh: `<h1 style="color:orange;">Contoh dari inline CSS</h1>`
   - Kelebihan: perubahan pada satu elemen HTML sehingga membantu memperbaiki kode dengan cepat.
   - Kekurangan: struktur file HTML terlihat berantakan karena banyaknya styling dan style CSS hanya dapat diterapkan pada satu elemen HTML saja.
2. Internal CSS: kode CSS ditulis di dalam tag style dan kode HTML dituliskan di bagian atas (header) file HTML dengan cara mendeklarasikan tag `<style>` di dalam `<head>` HTML, kemudian menulis kode css di dalam tag tersebut
   - Kelebihan: tidak perlu membuat file CSS terpisah karena bisa langsung menambahkan styling CSS pada file HTML dan perubahan tersebut hanya berlaku pada satu halaman saja.
   - Kekurangan: meningkatkan loading time pada website karena styling yang ditambahkan langsung pada file HTML, tidak efisien jika CSS yang sama ingin digunakan di beberapa file.
3. External CSS: kode CSS ditulis terpisah dengan kode HTML, kita perlu pembuat file khusus berektensi `.css` dan menggunakan tag `<link>` pada head HTML untuk menghubungkan file HTMl dengan file khusus CSS yang terpisah.
   - Kelebihan: ukuran file HTML lebih ringan dan kode lebih rapi. Selain itu, file khusus CSS dapat digunakan untuk banyak file HTML lainnya.
   - Kekurangan: dibutuhkan waktu loading bagi laman website untuk membentuk styling yang ada di file CSS ke file HTML, selain itu jika proses ini gagal dilakukan maka halaman akan menjadi berantakan dan ekternal CSS diprioritaskan paling rendah dibanding CSS lain.

## Tag HTML5

1. `<textarea>`: multiline text input
2. `<nav>`: navigasi pada website
3. `<section>`: section pada website
4. `<table>`: mendefinisikan sel di tabel
5. `<footer>`: footer pada website
6. `<main>`: main content pada website
7. `<body>`: mendefinisikan body
8. `a`: hyperlink ke halaman atau tautan lain
9. `b` : membuat teks lebih tebal
10. `<p>`: mendefinisikan paragraf

## CSS selector

1. ID: menggunakan `#` sebagai tanda id pada HTML
2. Class : menggunakan `.` sebagai tanda class pada HTML
3. Element: menggunakan nama tag HTML sebagai selector atau `#` atau `.`.

## Implementasi checklist

- Tambahkan tag `<link>` pada base.html untuk menggunakan CDN dari tailwind css.
- Tambahkan styling dan membuatnya responsive pada file html untuk halaman registrasi, login, todolist, dan create_todo. Styling menggunakan tailwind.
- Referensi 🧾 : [https://tailwindcss.com] tailwind documentation
