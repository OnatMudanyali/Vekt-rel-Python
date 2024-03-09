print("\033[1;32;40m")
#print("╔"+"═"*20+"╗")
import hesaplamalar.hesapmakinesi
import oyunlar.oyun
import çizimler.çizim
import sağlık.sağlık
import dersler.ders
print("╔═════════════════════╗")
print("║    Vektörel Ders    ║")
print("║                     ║")
print("║  1-Hesap Makinası   ║")
print("║  2-Oyunlar          ║")
print("║  3-Çizimler         ║")
print("║  4-Sağlık           ║")
print("║  5-Dersler          ║")
print("║                     ║")
print("║    Seçimiz nedir?   ║")
print("╚═════════════════════╝")
secim = input()
if secim == "1" :
    hesaplamalar.hesapmakinesi.hmmenü()
secim = input()
if secim == "2" :
    oyunlar.oyun.oyunlarmenü()
secim = input()
if secim == "3":
    çizimler.çizim.çizimmenü()
secim = input()
if secim == "4" :
    sağlık.sağlık.sağlıkmenü()
secim = input()
if secim == "5" :
    dersler.ders.derslermenü()
# 201 ╔
# 205 ═
# 187 ╗
# 186 ║
# 200 ╚
# 188 ╝
