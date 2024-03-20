def yemekmenü():    
    print("╔═════════════════════════════════════════════════╗")                                                     ╗")
    print("║                   Yemekler                      ║")
    print("║                                                 ║")
    print("║  0-Aşağıdaki Menüye Yemek Ekle                  ║")
    print("║  1-Tarhana                                      ║")
    print("║  2-Mercimek                                     ║")
    print("║  3-Makarna                                      ║")
    print("║  4-Mantı                                        ║")
    print("║  5-Döner                                        ║")
    print("║                                                 ║")
    print("║                                                 ║")
    print("║  6-Ana Menü                                     ║")
    print("║                                                 ║")
    print("║    Seçimiz nedir?                               ║")
    print("╚═════════════════════════════════════════════════╝") 
    print()
    secim=input("Yapmak istediğiniz işlemin başındaki sayıyı yazınız:")
    if secim=="0":
    corbalar = ["Tarhana","Mercimek"]
    print(corbalar)
    #print(corbalar[1])

    yemek1 = "Makarna"
    yemek2 = "Mantı"
    yemek3 = "Döner"
    yemekler =[yemek1,yemek2,yemek3]
    print(yemekler)
    ey = input("Eklenecek yemek nedir?")
    #yemekler.append(ey)
    yemekler.insert(1,ey)

    print("\nÇORBALAR:")
    for a in corbalar:
        print(a)

    print("\nYEMEKLER:")
    for a in yemekler:
        print(a)

    #print(yemekler[-1])
    #print(yemekler[-2]) 
