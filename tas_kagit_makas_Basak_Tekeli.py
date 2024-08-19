# random modülü dahil edildi.
import random

# Taş, kağıt ve makas seçenekleri için liste oluşturuldu.
choices = [0, 1, 2]


def print_colored(text, color_code, style_code=0):
  
    ''' Renkli ve farklı sillerde metinler elde etmek için print_colored fonksiyonu oluşturuldu. 
        30: Siyah, 31: Kırmızı, 32: Yeşil, 33: Sarı, 34: Mavi, 35: Mor, 36: Camgöbeği (Cyan), 37: Beyaz
        0: Normal yazı stili, 1: Kalın yazı stili, 4: Altı çizili yazı stili'''
        
    # '\033['  : metni renklendirmek ve stil vermek için
    # '\033[0m': metin stilini ve rengini sıfırlayarak, metnin geri kalanının varsayılan biçiminde olmasını sağlar. 
    print(f"\033[{style_code};{color_code}m{text}\033[0m")

# Taş kağıt ve makas için renkli ascii karakterler eklendi.
rock = '''
\033[31m
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
\033[0m
'''

paper = '''
\033[33m
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
\033[0m
'''

scissors = '''
\033[34m
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
\033[0m
'''

def what_is_your_name():

    ''' Oyuncu adını player_name değişkenine atayan fonksiyon oluşturuldu, kullanıcı bir giriş yapmadığı taktirde random isim seçiliyor. '''
    
    print_colored("\n\n                           TAŞ KAĞIT MAKAS OYUNU BAŞLIYOR !!  ", "36", "1")
    global player_name     # player_name değişkeni fonksiyon dışındada kullanılacağı için global olarak tanımlandı.
    print_colored("\n\nAdınız Cemil olabilir mi Cemil, peki ya Suat ? Yok değilse adınızı girin ya da sizin için seçilmiş isme razı olun...\n", "34", "1" )
    player_name = input("")
    if len(player_name) == 0:   # player_name değişkeninin değer alıp almadığı kontrol ediliyor.
        player_name = random.choice(['Cemil', 'Suat', 'Yusuf', 'Orhan'])  # 
        return player_name

def welcome_and_rules():

    ''' Oyuncunun karşılanması ve kuralların belirtilmesi için welcome_and_rules() fonksiyonu oluşturuldu.
        Bu fonksiyonda bir işlem yapılmaz, sadece bilgilendirme içindir.  '''

    print_colored(f"\nHoş geldin {player_name.capitalize()}, önce kurallara göz atalım.\n"
             "\n1. Taş, Kağıt veya Makas seçmek için 0, 1 veya 2 sayılarını kullanmalısın."
             "\n2. Taş makası kırar, kağıt taşı sarar, makas kağıdı keser."
             "\n3. Bir oyunda 3 tur var ve iki tur kazanan oyunu kazanır."
             "\n4. Oyuna devam edebilmek için hem blgisayarın hem de oyuncunun devam etmeyi kabul etmesi gerekir."
             "\n5. Oyundan çıkmak için 'çık' yazman yeterli."
             "\n   Bol Şans :)" , "36", "0" )

def player_choice():

    ''' Oyuncu taş, kağıt, makas arasından seçim yapar ya da oyunu bırakmak için 'çık' yazar. 
        Seçimlerin daha kolay olabilmesi ve yazım hatalarını en aza indirmek için tam sayı değerleri kullanılıyor.
        Oyuncu tanımlı olmayan bir giriş yaptığı sürece while döngüsü ile kullanıcıdan doğru giriş yapılması istenir.
        While döngüsünden doğru giriş yapıldığında ya da 'çık' yazıldığında çıkılır.
        '''
        
    while True:
     
        print_colored(" 0 (Taş), 1 (Kağıt), 2 (Makas) ?\n", "34", "0")
        choice = input(f"{player_name.capitalize()}: ")       # Kullannıcı seçimi alınır ve choice string değişkenine atanır. 
        
        if choice.lower() == 'çık':                            # choice değişkenine atanan değer kontrol edilir.
            print(f"\n{player_name.capitalize()} oyundan çıkıyor. Görüşmek üzere!")  
            return 'Çık'
        try:
            choice = int(choice)   # Değişken tiplerinin farklı olması nedeniyle hata almamak için choice değişkeni int tipine dönüştürülüyor.
            if choice in choices:  # choice değişkenine atanan değer liste içeri ile eşleşiyor mu? Eşleşiyorsa choice değişkeni döndürülür.
                return choice      
            print_colored("\nGeçersiz giriş, Lütfen 0 (Taş), 1 (Kağıt) veya 2 (Makas) seçin, çıkmak için 'çık' yazın.\n", "31", "4") # Eşleşmiyorsa uyarı gösterilir.
        except ValueError:         # Kullanıcı tam sayı girmedi ise Value Error hatası oluşur. 
            print(f"\nGeçersiz giriş, lütfen tekrar dene {player_name.capitalize()}.\n") 

def computer_choice():
    
    ''' Bilgisayar seçimi random yaptılıyor ve yerel choice değişkenine atanıp bu değer döndürülüyor.'''
    
    choice = random.choice(choices)
    print("Bilgisayar: ", choice)
    return choice

def tour_winner(player_choice, computer_choice):
  
    ''' Tur kazananı belirleniyor. Koşullu durumlar kullanılarak kazanan belirleniyor.
        player_choice ve compter_choice değişkenlerini parametre olarak alır.
        Berabere olma durumunda puan artışı yok, bilgisayarın kazanması durumunda computer_score değişkeni; 
        kullanıcının kazanması durumunda player_score değişkeni 1 artıtılır.
        '''

    global player_score, computer_score     # Değişkenler fonksiyon dışında da kullanılacağı için global değişkenlerdir.

    # Berabere olan durumlar:
    if player_choice == computer_choice:    
        if player_choice == 0:
            print(rock , "x" ,  rock)
        elif player_choice == 1:
            print(paper , "x" ,  paper)
        elif player_choice == 2:
            print(scissors , "x" ,  scissors)

    # Oyuncunun kazandığı durumlar (score arttırılıyor):
    elif player_choice == 0 and computer_choice == 2:
        print(rock  , "x" ,  scissors)
        player_score = player_score + 1
    elif player_choice == 1 and computer_choice == 0:
        print(paper , "x" ,  rock)
        player_score = player_score + 1
    elif player_choice == 2 and computer_choice == 1:
        print(scissors , "x" ,  paper)
        player_score = player_score + 1

    # Bilgisayarın kazandığı durumlar (score arttırılıyor):
    elif computer_choice == 0 and player_choice == 2:
        print(scissors, "x" ,  rock)
        computer_score = computer_score + 1
    elif computer_choice == 1 and player_choice == 0:
        print(rock , "x" ,  paper)
        computer_score = computer_score + 1
    elif computer_choice == 2 and player_choice == 1:
        print(paper , "x" , scissors )
        computer_score = computer_score + 1

    # Tur sonucu scorlar ekrana yazdırılıyor.
    print("{0}-> {1}   Bilgisayar-> {2}" .format(player_name.capitalize(), player_score, computer_score)) 
    return player_score, computer_score   # Puanlar döndürülüyor.

def game_winner(player_score, computer_score):
 
    ''' tour_winner fonksiyonundan dönen değişkenleri parametre olarak alır ve karşılaştırma yapıp oyun kazananını bulur. 
        Fonksiyon sonucunda boolen değerler döndürülür.'''

    print ("\n\nBilgisayar: {0}  x  {1}: {2}\n" .format(computer_score, player_name.upper(), player_score))
    if computer_score > player_score:
        print_colored("\nKAYBETTİN!", "36", "1")
    elif player_score > computer_score:
        print_colored(f"\nTEBRİKLER {player_name.upper()} KAZANDIN!" , "36", "1")
    elif computer_score == player_score:
        print_colored("\nBERABERE!", "36", "1")

def ask_to_play_again():

    ''' Oyuncuya tekrar oynamak isteyip istemediği sorulur ve cevabı değişkene atanır, bilgisayarın random cevap oluşturulması sağlanır.
        iki cevabında olumlu olması durumunda oyun devam eder aksi halde oyun biter. 
        Fonksiyon oyuna devam edilecekse 'True' edilmeyecekse 'False' değerini döndürür. '''
        
    answer_of_player = input(f"\nYeni bir oyun oynamak ister misin {player_name.capitalize()}? (Evet/Hayır)\n").lower()
    if answer_of_player != 'evet':
        answer_of_player = input("\nEmin misin, bak tekrar soruyorum, bir oyun daha? \n").lower()
        if answer_of_player != 'evet':
            print("\n'Hayır dedik ya !' dediğini duyar gibiyim.\n\n OYUN BİTTİ !!! ")
            return False

    answer_of_computer = random.choice(['Tabiki', 'Yeterli'])
    print("\nBilgisayar tekrar oynamayı düşünür mü ?\n",answer_of_computer)

    if answer_of_computer == 'Tabiki' and answer_of_player == 'evet':
        print(f"\nBİLGİSAYAR ve {player_name.upper()} yeni oyunu kabul etti.\n\n")
        return True
    else:
        print_colored("\nOYUN BİTTİ!\n\n", "36", "1")
        return False

def tas_kagit_makas_Basak_Tekeli():

    
   
    global player_score, computer_score
    print("\n\n                    ********************************************************" )
    what_is_your_name()
    welcome_and_rules()

    player_score = 0
    computer_score = 0
    played_game = 0

    while(True):  

        tour = 1
        played_game += 1
        
        print("\n\n********************************************************" )
        
        while player_score < 2 and computer_score <2:

            print_colored(f"\n                    {played_game}. OYUN  {tour}. TUR\n", "35", "1")
            p_choice = player_choice()
            c_choice = computer_choice()
            
            if p_choice == 'Çık':
                print(f"\n{player_name.capitalize()} oyundan çıkıyor. Görüşmek üzere!\n\n")
                return

            tour_winner(p_choice, c_choice)

            if player_score == 2 or computer_score == 2:
                game_winner(player_score, computer_score)
                player_score = 0
                computer_score = 0

                if not ask_to_play_again():  # ask_to_play_again fonksiyonu false dönerse return ile döngüden çıkarız ve oyun biter.     
                    return

                tour = 1
                break

            print("\n********************************************************\n")
            tour += 1
            
if __name__ == "__main__":
    tas_kagit_makas_Basak_Tekeli()
    
