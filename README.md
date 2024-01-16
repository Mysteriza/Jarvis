## Source
[Icris Studio: Virtual Assistant Jarvis](https://github.com/IcrisStudio/Build-Your-Own-Virtual-Assistant-Jarvis)

# Fitur Virtual Assistant Bahasa Indonesia
- Terintegrasi dengan GPT melalui library g4f/gpt4free, sehingga bisa menjawab dengan bantuan ChatGPT.
- Program sudah terintegrasi dengan Wit.ai, sebuah platform untuk membuat data latih dari input pengguna, sehingga virtual assistant dapat lebih mengerti apapun permintaan yang diucapkan user tanpa perlu menetapkan perintah baku pada kode (jika perintah tidak direspon dengan baik, artinya data latih milik saya belum lengkap, Anda bisa membuat data latih sendiri dengan Wit.ai lalu mengganti API-nya dengan API Client Wit.ai milik Anda).
- Program bisa mengatakan cuaca saat ini, kota yang ditetapkan adalah kota Bandung. Anda bisa mengubah ini dengan mengubah latitude dan longitude pada kode Weather.py.
- Program bisa mengatakan waktu/jam saat ini, menggunakan library datetime.
- Program bisa memutar video di YouTube, hanya dengan perintah "Putar (judul lagu/video)", secara otomatis program akan membuka browser dan masuk ke YouTube lalu memutar video yang sesuai dengan judul yang Anda sebut.
- Program bisa menerima perintah untuk pindah tab, tutup tab, dan tutup aplikasi/window yang aktif saat ini.
- Program akan otomatis sleep jika tidak menerima perintah suara dalam waktu tertentu, katakan "wake up" agar program bangun dan kembali bisa menerima input suara. Katakan "sleep" jika Anda ingin membuat program tertidur atau masuk ke mode sleep secara manual. Program bisa dihentikan agar tidak menerima input suara apapun dengan mengatakan "hentikan" atau "berhenti", jika perintah ini diucapkan, maka user harus membuka/menjalankan kembali programnya.
- Program masih belum sempurna dan masih butuh lebih banyak perbaikan. Untuk saat ini program masih berbasis CLI, belum GUI.

