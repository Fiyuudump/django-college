from django.db import models

class Jenis(models.Model):
    nama = models.CharField(max_length=20)
    deskripsi = models.TextField()

    def _str_(self):
        return self.nama

class Barang(models.Model):
    kdbrg = models.CharField(max_length=8)
    nama = models.CharField(max_length=75)
    stok = models.IntegerField()
    harga = models.BigIntegerField()
    link_gambar = models.CharField(max_length=150, blank=True)
    waktu_posting = models.DateTimeField(auto_now_add=True)
    jenis_id = models.ForeignKey(Jenis, on_delete=models.CASCADE, null=True)

    def _str_(self):
        return self.nama

class About(models.Model):
    judul = models.CharField(max_length=200)
    isi = models.TextField()
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.judul

class Project(models.Model):
    category = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    project_link = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.title
