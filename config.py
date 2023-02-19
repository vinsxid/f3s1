import os

api_id = int(os.environ.get("API_ID", "27200202"))
api_hash = os.environ.get("API_HASH", "d7f267b4e32cb2e86b2e807c1b1f1c0c")
bot_token = os.environ.get("BOT_TOKEN", "6235791848:AAG2ULtzvHLY06KRLmpeGeu4XxdAkmfU1Z4")
# =========================================================== #

db_url = os.environ.get("DB_URL", "mongodb+srv://fess1:fess1@cluster0.faqansq.mongodb.net/?retryWrites=true&w=majority")
db_name = os.environ.get("DB_NAME", "menfes1")
# =========================================================== #

#Channel Utama sambungin ke Grup Base
channel_1 = int(os.environ.get("CHANNEL_1", "-100"))
#Grup Base
channel_2 = int(os.environ.get("CHANNEL_2", "0"))
#Channel Log sambungin ke Grup Log (Private)
channel_log = int(os.environ.get("CHANNEL_LOG", "-1001811659938"))
# =========================================================== #

id_admin = int(os.environ.get("ID_ADMIN", "1243599890"))
# =========================================================== #

batas_kirim = int(os.environ.get("BATAS_KIRIM", "25"))
batas_talent = int(os.environ.get("BATAS_TALENT", "10"))
batas_daddy_sugar = int(os.environ.get("BATAS_DADDY_SUGAR", "10"))
batas_moansgirl = int(os.environ.get("BATAS_MOANSGIRL", "10"))
batas_moansboy = int(os.environ.get("BATAS_MOANSBOY", "10"))
batas_gfrent = int(os.environ.get("BATAS_GFRENT", "10"))
batas_bfrent = int(os.environ.get("BATAS_BFRENT", "10"))
# =========================================================== #

biaya_kirim = int(os.environ.get("BIAYA_KIRIM", "10"))
biaya_talent = int(os.environ.get("BIAYA_TALENT", "5"))
biaya_daddy_sugar = int(os.environ.get("BIAYA_DADDY_SUGAR", "5"))
biaya_moansgirl = int(os.environ.get("BIAYA_MOANSGIRL", "5"))
biaya_moansboy = int(os.environ.get("BIAYA_MOANSBOY", "5"))
biaya_gfrent = int(os.environ.get("BIAYA_GFRENT", "5"))
biaya_bfrent = int(os.environ.get("BIAYA_BFRENT", "5"))
# =========================================================== #

hastag = os.environ.get("HASTAG", "#Girl #Boy #Thriller #Romance #Horor #Comedy #Random").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.environ.get("PIC_BOY", "")
pic_girl = os.environ.get("PIC_GIRL", "")
# =========================================================== #

pesan_join = os.environ.get("PESAN_JOIN", "Tidak dapat diakses harap join terlebih dahulu")
start_msg = os.environ.get("START_MSG", "Hai {fullname} 🌱 \n\nIni adalah bot menfess, semua pesan yang kamu kirim akan masuk ke channel secara anonymous. Silakan tuliskan pesanmu dengan mencantumkan salah satu hastag:\n\n#Thriller pengakuan dosa/hal2 yang berbau kejahatan baik lu jdi korban atau pun pelaku\n#Romance asmara tentang cinta2an\n#Horor ceritakan kisah horor\n#Comedy ceritakan kisah lucu\n#Random buat nanya atau apalah\n\nButuh bantuan? Hubungi @Vinsxid")
menu_msg = os.environ.get("MENU_MSG","""
#Thriller pengakuan dosa/hal2 yang berbau kejahatan baik lu jdi korban atau pun pelaku
#Romance asmara tentang cinta2an
#Horor ceritakan kisah horor
#Comedy ceritakan kisah lucu
#Random buat nanya atau apalah

Wajib pake username..""")

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
{mention}, pesan mu gagal terkirim silahkan gunakan hastag:

#Thriller pengakuan dosa/hal2 yang berbau kejahatan baik lu jdi korban atau pun pelaku
#Romance asmara tentang cinta2an
#Horor ceritakan kisah horor
#Comedy ceritakan kisah lucu
#Random buat nanya atau apalah


Wajib pake username..""")
