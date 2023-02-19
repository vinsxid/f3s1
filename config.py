import os

api_id = int(os.environ.get("API_ID", "27200202"))
api_hash = os.environ.get("API_HASH", "d7f267b4e32cb2e86b2e807c1b1f1c0c")
bot_token = os.environ.get("BOT_TOKEN", "6235791848:AAG2ULtzvHLY06KRLmpeGeu4XxdAkmfU1Z4")
# =========================================================== #

db_url = os.environ.get("DB_URL", "mongodb+srv://fess1:fess1@cluster0.faqansq.mongodb.net/?retryWrites=true&w=majority")
db_name = os.environ.get("DB_NAME", "menfes1")
# =========================================================== #

#Channel Utama sambungin ke Grup Base
channel_1 = int(os.environ.get("CHANNEL_1", "-1001549513372"))
#Grup Base
channel_2 = int(os.environ.get("CHANNEL_2", "-1001811659938"))
#Channel Log sambungin ke Grup Log (Private)
channel_log = int(os.environ.get("CHANNEL_LOG", "-1001811659938"))
# =========================================================== #

id_admin = int(os.environ.get("ID_ADMIN", "1243599890"))
# =========================================================== #

batas_kirim = int(os.environ.get("BATAS_KIRIM", "5"))
batas_talent = int(os.environ.get("BATAS_TALENT", "10"))
batas_daddy_sugar = int(os.environ.get("BATAS_DADDY_SUGAR", "10"))
batas_moansgirl = int(os.environ.get("BATAS_MOANSGIRL", "10"))
batas_moansboy = int(os.environ.get("BATAS_MOANSBOY", "10"))
batas_gfrent = int(os.environ.get("BATAS_GFRENT", "10"))
batas_bfrent = int(os.environ.get("BATAS_BFRENT", "10"))
# =========================================================== #

biaya_kirim = int(os.environ.get("BIAYA_KIRIM", "20"))
biaya_talent = int(os.environ.get("BIAYA_TALENT", "80"))
biaya_daddy_sugar = int(os.environ.get("BIAYA_DADDY_SUGAR", "70"))
biaya_moansgirl = int(os.environ.get("BIAYA_MOANSGIRL", "60"))
biaya_moansboy = int(os.environ.get("BIAYA_MOANSBOY", "50"))
biaya_gfrent = int(os.environ.get("BIAYA_GFRENT", "40"))
biaya_bfrent = int(os.environ.get("BIAYA_BFRENT", "30"))
# =========================================================== #

hastag = os.environ.get("HASTAG", "#Girl #Boy #Ask #Find #Spill #Story").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.environ.get("PIC_BOY", "")
pic_girl = os.environ.get("PIC_GIRL", "")
# =========================================================== #

pesan_join = os.environ.get("PESAN_JOIN", "Tidak dapat diakses harap join terlebih dahulu")
start_msg = os.environ.get("START_MSG", "Hai {fullname} 🌱 Untuk mengirimkan pesan secara anonim ke channel . Silahkan sampaikan pesanmu atau pap cute atau video konten positif kamu\n\nSebelum menggunakan silakan baca rules terlebih dahulu ya\n\nButuh bantuan? Hubungi Admin")
menu_msg = os.environ.get("MENU_MSG","""
#Boy / #Girl untuk Mencari Pasangan, Teman , Partner FWB
#Ask untuk Bertanya
#Story untuk Berbagi Cerita
#Spill untuk Spill Masalah
#Find untuk Mencari Pasangan, Teman, Partner FWB

Wajib pake username..""")

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
{mention}, pesan mu gagal terkirim silahkan gunakan hastag:

#Boy / #Girl untuk Mencari Pasangan, Teman , Partner FWB
#Ask untuk Bertanya
#Story untuk Berbagi Cerita
#Spill untuk Spill Masalah
#Find untuk Mencari Pasangan, Teman, Partner FWB


Wajib pake username..""")
