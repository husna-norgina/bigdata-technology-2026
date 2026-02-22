# 💻 Praktikum 1 — Setup Environment & Git Workflow 

Praktikum ini membahas **pembangunan lingkungan kerja Data Engineer modern** menggunakan **Python**, **PySpark**, **MongoDB Atlas**, serta **Git & GitHub**. Fokus utama praktikum adalah memahami **setup environment profesional**, **distributed processing menggunakan Spark**, serta **integrasi cloud database** sebagai fondasi awal dalam pengembangan sistem Big Data.

Praktikum ini mensimulasikan workflow industri: mulai dari **local development**, **distributed engine**, **cloud database**, hingga **version control**.

**Topik:** PySpark, MongoDB Atlas, Cloud Database, Git Workflow, Distributed Processing, Data Engineering Environment

---

## 🧑‍🎓 Informasi Mahasiswa

| Informasi         | Data                                                     |
| ----------------- | -------------------------------------------------------- |
| Mata Kuliah       | Teknologi Big Data                                       |
| Dosen Pengampu    | Muhayat, M.IT                                            |
| Praktikum         | P1 – Setup Environment & Git Workflow                    |
| Nama Mahasiswa    | Husna Norgina                                            |
| NIM               | 230104040056                                             |
| Kelas             | TI23B                                                    |
| Repo GitHub       | https://github.com/husna-norgina/bigdata-technology-2026 |
| Tanggal Praktikum | 19-02-2026                                               |

---

## 🎯 Tujuan Praktikum

1. Menggunakan VS Code sebagai development environment.
2. Menggunakan PowerShell sebagai terminal utama.
3. Menginstal dan menjalankan PySpark.
4. Membuat cluster MongoDB Atlas (cloud database).
5. Membuat struktur project profesional data engineer.
6. Menggunakan Git dan GitHub sebagai version control.
7. Menjalankan Spark job sederhana.

---

## 🛠 Tools & Environment

* Python 3.10
* Visual Studio Code
* PowerShell
* PySpark
* MongoDB Atlas (Cloud Database)
* Git & GitHub
* Windows 10/11

---

## 🧱 Struktur Project

Struktur project praktikum:

```
bigdata-project/
│
├── data/
├── cloud_storage/
├── scripts/
│   ├── simple_job.py
│   └── test_mongo.py
├── notebooks/
├── reports/
├── requirements.txt
└── README.md
```

Struktur ini mengikuti standar project Data Engineer profesional agar mudah dikembangkan dan scalable.

---

## ☁️ Setup MongoDB Atlas (Cloud)

MongoDB Atlas digunakan sebagai **cloud database** untuk simulasi environment production.

Fitur yang dipelajari:

* Membuat cluster gratis (M0 Free Tier)
* Membuat database user
* Mengatur network access
* Mengambil connection string
* Menghubungkan Python ke MongoDB Atlas

Koneksi berhasil diuji menggunakan library **pymongo**.

---

## 🔥 Implementasi PySpark

### Membuat SparkSession

Spark digunakan sebagai distributed processing engine.

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("SimpleJob") \
    .getOrCreate()
```

### Membuat DataFrame & Agregasi

Spark digunakan untuk melakukan agregasi data sederhana:

```python
data = [("A", 10), ("B", 20), ("A", 30)]
columns = ["category", "value"]

df = spark.createDataFrame(data, columns)
df.groupBy("category").sum("value").show()
```

### Output

```
+--------+----------+
|category|sum(value)|
+--------+----------+
|       A|        40|
|       B|        20|
+--------+----------+
```

---

## 🌐 Git Workflow

Project menggunakan Git sebagai version control.

Perintah utama:

```
git init
git add .
git commit -m "initial project setup"
git branch -M main
git push -u origin main
```

Repository berhasil di-upload ke GitHub sebagai portfolio project Big Data.

---

## 📸 Screenshot Praktikum

Berikut dokumentasi hasil praktikum:

**1. Screenshot Spark Berjalan**

![Spark](evidence/1.%20Screenshot%20Spark%20Berjalan.png)

Menampilkan SparkSession berhasil dijalankan tanpa error.

---

**2. Screenshot MongoDB Atlas ACTIVE**

![MongoDB](evidence/2.%20Screenshot%20MongoDB%20Atlas%20Cluster%20Active.png)

Cluster M0 Free Tier berhasil dibuat dan status ACTIVE.

---

**3. Screenshot Repository GitHub**

![GitHub](evidence/3.%20Screenshot%20Link%20GitHub%20Repository.png)

Repository online berisi struktur project.

---

**4. Screenshot File simple_job.py**

![Code](evidence/4.%20Screenshot%20File%20simple_job.py.png)

Kode Spark job sederhana di VS Code.

---

**5. Screenshot Output Spark**

![Output Spark](evidence/5.%20Screenshot%20Hasil%20Eksekusi%20Spark.png)

Output agregasi berhasil dijalankan.

---

## 📄 Laporan Praktikum 1

[230104040056_Husna Norgina_P1.pdf](<evidence/230104040056_Husna Norgina_P1.pdf>)

---

> Semua screenshot disimpan dalam folder:
> 📂 `evidence/`

---

## 📊 Analisis Praktikum

* PySpark berhasil dijalankan di local environment.
* SparkSession dapat dibuat tanpa error.
* MongoDB Atlas cloud database berhasil dibuat dan terkoneksi.
* Struktur project tersusun profesional.
* Git dan GitHub digunakan untuk version control.
* Spark job sederhana berhasil dijalankan dengan output agregasi.

Praktikum ini memberikan pengalaman awal sebagai **Data Engineer** dengan workflow yang mendekati industri.

---

## ✅ Kesimpulan

Berdasarkan hasil **Praktikum 1 – Setup Environment & Git Workflow**, dapat disimpulkan bahwa pembangunan environment kerja merupakan langkah awal penting dalam pengembangan sistem Big Data. Integrasi antara PySpark, MongoDB Atlas, dan GitHub menunjukkan bagaimana workflow data engineer modern bekerja secara profesional dan cloud-ready.

Walaupun hanya menjalankan proses agregasi sederhana, praktikum ini telah mencakup konsep:

* Distributed computing
* Cloud database
* Version control
* Professional project structure

Praktikum ini menjadi fondasi sebelum masuk ke tahap lanjutan seperti ETL pipeline, data warehouse, dan machine learning.

---

## 📌 Catatan

* Praktikum dikerjakan sesuai modul pembelajaran.
* Semua instalasi dan konfigurasi berhasil dilakukan.
* Dokumentasi disertakan melalui screenshot.
* Proyek ini dibuat untuk keperluan pembelajaran Teknologi Big Data.

---

📝 *Disusun oleh Husna Norgina (230104040056) — Praktikum 1 Teknologi Big Data*

---