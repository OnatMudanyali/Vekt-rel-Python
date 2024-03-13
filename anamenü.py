print("\033[1;32;40m")
#print("╔"+"═"*20+"╗")
import hesaplamalar.hesapmakinesi
import oyunlar.oyun
import çizimler.çizim
import sağlık.sağlık
import dersler.dersler
import müziktürleri.müzikler
import ülkeler.ülke
import yemekler.yemek
import sporlar.spor
import nothesabı.harfnotu
print("╔═════════════════════╗")
print("║    Vektörel Ders    ║")
print("║                     ║")
print("║  1-Hesap Makinesi   ║")
print("║  2-Oyunlar          ║")
print("║  3-Çizimler         ║")
print("║  4-Sağlık           ║")
print("║  5-Dersler          ║")
print("║  6-Müzik Türleri    ║")
print("║  7-Ülkeler          ║")
print("║  8-Yemekler         ║")
print("║  9-Sporlar          ║")
print("║  10-Not Hesabı      ║")
print("║  ç-çıkış            ║")
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
    dersler.dersler.derslermenü()
secim = input()
if secim == "6" :
    müziktürleri.müzikler.müzikmenü()
secim = input()
if secim == "7" :
    ülkeler.ülke.ülkemenü()
secim = input()
if secim == "8" :
    yemekler.yemek.yemekmenü()
secim = input()
if secim == "9" :
    sporlar.spor.spormenü()
secim = input()
if secim == "10" :
    nothesabı.harfnotu.harfnotumenü ()
    
# 201 ╔
# 205 ═
# 187 ╗
# 186 ║
# 200 ╚
# 188 ╝
