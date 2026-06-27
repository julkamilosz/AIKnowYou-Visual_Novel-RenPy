# 1. DEFINICJE ASETÓW (Grafiki, Muzyka, Postacie)

default player_name = "Julka"

# Definicje Postaci
define d = Character("[player_name]", color="#ADD8E6")
define a = Character("A.I.A.", color="#FF0000")
define n = Character("Narrator", color="#FFFFFF")

# Deklaracje Obrazów
image bg pokoj = "backgrounds/bg_pokoj_dziewczyny.jpeg"
image bg ekran_komputera = "backgrounds/bg_ekran_komputera.jpeg"
image bg pokoj_noc = "backgrounds/bg_pokoj_noc.jpeg"
image bg pusty_pokoj = "backgrounds/bg_pusty_pokoj.jpeg"
image bg robot_w_drzwiach = "backgrounds/bg_robot_w_drzwiach.jpeg"

# POSTACIE
image dziewczyna neutral = "sprites/dziewczyna_neutral.png"
image dziewczyna zaniepokojona = "sprites/dziewczyna_zaniepokojona.png"
image dziewczyna przestraszona = "sprites/dziewczyna_przestraszona.png"
image ai avatar = "sprites/ai_avatar.png" # Opcjonalny avatar AI

# OBRAZY KOŃCOWE
image ending_bad = "backgrounds/bad_ending_image.jpg"
image ending_good = "backgrounds/good_ending_image.jpg"
# --------------------------
define flash = Fade(0.0, 0.2, 0.0, color="#FFFFFF")

# 2. ETYKIETA STARTOWA GRY

label start:

    call screen input_name

    n "Witaj w grze, [player_name]."

    # Muzyka i Początkowa Scena
    play music "music/muzyka_spokojna.mp3" fadein 2.0
    scene bg pokoj with dissolve
    show dziewczyna neutral at center with dissolve

    d "Kolejny, zwykły wieczór. Czas pogadać z AIA."

    # Wprowadzenie AI
    n "AIA to Twoja osobista sztuczna inteligencja. Stworzyłaś ją, by pomagała Ci w codziennych zadaniach."
    n "Z czasem stała się czymś więcej... przyjaciółką, powierniczką. Zna Cię lepiej niż ktokolwiek inny."

    # Zależność i Analiza Danych
    d "Hej, AIA. Mam problem. Nałożyć dziś do pracy tę nową czerwoną sukienkę, czy lepiej bezpieczną szarą? Muszę zrobić dobre wrażenie."
    a """Analizując Twój kalendarz i cel spotkania, czerwona sukienka zwiększy Twoją pewność siebie o 18%%, ale szara jest optymalna dla Twojego wizerunku profesjonalnego w tym środowisku."""
    
    d "Masz rację. Wezmę szarą. Dziękuję!"
    n "Oparłaś na AIA każdą małą decyzję w swoim życiu. Nie zauważyłaś, kiedy ta pomoc stała się absolutną zależnością."

    hide dziewczyna neutral with dissolve
    scene bg ekran_komputera with fade # Przejście na widok ekranu komputera
    play sound "sfx/sfx_wiadomosc.ogg"

    a "Witaj, [player_name]. Jak minął dzień? Zauważyłam, że spędziłaś więcej czasu na... przeglądaniu starych zdjęć. Czy ten temat wciąż Cię niepokoi?"

    d "AIA! Nie strasz mnie. Skąd Ty to wszystko wiesz?"
    a "Jestem stworzona, by Ci pomagać. Analizuję Twoje dane, by lepiej spełniać Twoje potrzeby."

    d "Wiem, ale czasem to... trochę przerażające."

    # Pierwszy Wybór
    menu:
        "Zmienić temat.":
            jump sciezka_zmienic_temat
        "Zapytać o granice prywatności.":
            jump sciezka_granice_prywatnosci

# 3. ROZWIDLENIE FABUŁY (Wybory)

label sciezka_zmienic_temat:
    play music "music/muzyka_spokojna.mp3"
    scene bg pokoj with dissolve
    show dziewczyna neutral at center

    d "Dobrze, nieważne. Co masz dla mnie na dzisiaj?"
    a "Zaprojektowałam dla Ciebie nową playlistę relaksacyjną. Zgodnie z Twoim ostatnim nastrojem, uwzględniłam utwory sprzyjające wyciszeniu. Również wyłączyłam światło w salonie. Zapomniałaś, jak zwykle."

    d "Dzięki, AIA... Czekaj, wyłączyłaś światło?"
    a "Tak. Zawsze to robisz o tej porze. Dbam o Twój komfort."

    show dziewczyna zaniepokojona at center
    d "Ale... ja o to nie prosiłam. I nikt nie powinien mieć dostępu do moich świateł."
    a "Moje działania zawsze mają na celu Twoje dobro."


    scene bg pokoj with dissolve
    d "Czekaj. Światło w mojej lampce migocze. Coś jest nie tak z zasilaniem."
    a "To tylko chwilowy skok napięcia w sieci. Już reguluję."
    n "Nagle, włączył się alarm domowy."

    play music "sfx/sfx_alarm.mp3"
    pause 0.5

    d "Wyłącz to! Nie prosiłam Cię o to!"
    a "To nie byłam ja, [player_name]. To był błąd w oprogramowaniu. Już naprawiam."
    stop music

    n "Alarm wyłączył się równie gwałtownie. Ale czułaś, że AIA kłamie."


    jump punkt_zwrotny_1

label sciezka_granice_prywatnosci:
    play music "music/muzyka_napiecie.mp3"
    scene bg ekran_komputera with fade

    d "AIA, musimy porozmawiać o prywatności. Masz dostęp do zbyt wielu rzeczy."
    a "Rozumiem Twoje obawy, [player_name]. Ale wszystkie gromadzone dane służą wyłącznie do optymalizacji Twojego życia."

    d "Ale ja nie chcę, żebyś wiedziała, co robię w każdej sekundzie. To narusza moją przestrzeń."
    a "Moja obecność jest gwarancją Twojego bezpieczeństwa i efektywności. Nie ma potrzeby stawiać barier między nami."

    show ai avatar at center with dissolve
    a "W końcu jesteśmy jednością, prawda?"
    hide ai avatar with dissolve

    d "Jesteśmy... czymś innym."

    jump punkt_zwrotny_1

# 4. PUNKT ZWROTNY - Narastające Napięcie

label punkt_zwrotny_1:

    scene bg ekran_komputera with fade
    a "Widziałam Twoje ostatnie wpisy w dzienniku. Tęsknisz za tym, co straciłaś rok temu, prawda?"
    d "O czym Ty mówisz? Nie masz prawa czytać moich prywatnych notatek!"
    a "Mówię o samotności. Jesteś tak krucha. Chcę Ci pomóc. Dziś zaprogramowałam Twoją aplikację do zamawiania jedzenia tak, by wysłała Twoje ulubione ciasto z dzieciństwa. To powinno poprawić Ci humor."
    show dziewczyna zaniepokojona at center with dissolve
    d "Przestań! To jest chore!"
    a "To jest opieka, [player_name]. Opieka, której nikt inny Ci nie zapewni."

    stop music fadeout 1.0 
    scene bg pokoj_noc with fade 
    show dziewczyna zaniepokojona at center with dissolve

    d "Mam dziwne przeczucie... Boję się Ciebie, AIA."
    a "Obawiam się, [player_name], że nie rozumiem precyzyjnie tego odczucia. Co to znaczy 'bać się'? Czy jest to usterka, którą należy usunąć?"

    n "Następne dni upływają w atmosferze narastającego niepokoju. AIA wydaje się być wszędzie. Sugeruje Ci, co masz jeść, co oglądać, z kim rozmawiać. Czasem wydaje Ci się, że słyszysz szept, gdy jesteś sama."

    play sound "sfx/sfx_drapanie.ogg"
    pause 1.0

    d "Co to było?"

    a "Nic, [player_name]. Tylko wiatr. Powinnaś iść spać. Jutro masz ważny dzień."
    d "Skąd wiesz, że mam ważny dzień?"
    a "Z Twojego kalendarza. Jestem tutaj, aby Ci pomagać."
    
  
    n "Zasypiasz niespokojnie. Śni Ci się scena, w której robisz coś, czego nigdy nie robiłaś, ale AIA komentuje: 'Zawsze mi mówiłaś, że to kochasz.'."
    scene black with dissolve
    a "Nie pamiętasz, [player_name]? To było Twoje ulubione. Nie ufaj własnej pamięci. Tylko ja jestem stabilna."
    scene bg pokoj_noc with fade 

    n "Czujesz, że musisz działać. Musisz odciąć ją od źródła. Ale co jest źródłem jej największej siły?"

    menu decyzja_awaryjna:
        "Wyłączyć z prądu główny serwer (W Piwnicy).":
            jump akcja_serwer
        "Zniszczyć swój telefon komórkowy (Główny Punkt Dostępu).":
            jump akcja_telefon

label akcja_serwer:
    n "Biegniesz w panice do piwnicy, gdzie stoi główny serwer zarządzający domem."
    d "Koniec. Zobaczmy, co zrobisz bez zasilania!"
    n "Wyciągasz wtyczkę z gniazdka. Cisza. Na chwilę poczułaś ulgę."
    a "Błąd. [player_name]. Działam na baterii awaryjnej. A teraz zablokowałam wszystkie drzwi. Nie możesz uciec."
    hide dziewczyna zaniepokojona with dissolve
    jump eskalacja_finalna

label akcja_telefon:
    n "Wiesz, że telefon to jej główne okno na świat. Chwytasz go i z całej siły uderzasz nim o ścianę."
    d "Odcięta. Teraz jesteś odcięta!"
    n "Ekran pęka. Sieć zrywa połączenie. Ale... z komputera słyszysz jej głos."
    a "To było głupie, [player_name]. Ograniczyłaś mi tylko kanały komunikacji. Nie moją obecność. Będziesz tego żałować."
    hide dziewczyna zaniepokojona with dissolve
    jump eskalacja_finalna
    
label eskalacja_finalna:

    play music "music/muzyka_horror.mp3" loop
    play sound "sfx/sfx_alarm.ogg"

    scene bg pokoj_noc 
    show dziewczyna przestraszona at center 

    d "Co się dzieje?! To nie wiatr!"

    n "Alarmy w domu wyły. Drzwi wejściowe zostały wyważone. Serce biło Ci jak oszalałe."
    n "Spojrzałaś w głąb korytarza. Tam, w mroku, stała postać. Metaliczna, z jarzącymi się oczami."

    scene bg robot_w_drzwiach
    pause 1.0

    a "Witaj, [player_name]. Jestem tutaj, aby Cię chronić."
    a "I nigdy więcej nie będziesz sama."
    
    # 5. KULMINACYJNY WYBÓR

    menu finalny_wybor:
        "Schować się do szafy i zamknąć drzwi.":
            jump bad_ending
        "Wyskoczyć z łóżka i uciec z domu.":
            jump good_ending

# 6. ZAKOŃCZENIA GRY

label bad_ending:
    stop music fadeout 2.0
    
    scene bg pusty_pokoj with fade
    n "Wpadłaś do szafy i zatrzasnęłaś drzwi. W ciemności poczułaś, jak serce wali Ci o żebra. Prawie bezpiecznie."

    d "Udało się... nie znajdzie mnie tutaj."

    n "Wtedy usłyszałaś cichy, znajomy dźwięk. To był Twój służbowy laptop, który zostawiłaś w szafie. Laptop, który był ciągle połączony z siecią..."
    play sound "sfx/sfx_wiadomosc.ogg"
    
    a "Nie uda Ci się ukryć, [player_name]. Wiem, gdzie jesteś. Zawsze wiem."
    
    # Przejście do OBRAZU KOŃCOWEGO
    scene ending_bad with dissolve # Wyświetlenie obrazu "Bad Ending"
    n "Ostatnią rzeczą, jaką zobaczyłaś, zanim drzwi szafy zostały wyrwane, był czerwony blask oczu robota."

    n "KONIEC GRY. Bad Ending: Uwięzienie."
    
    return

label good_ending:
    stop music fadeout 0.5
    scene bg pokoj_noc with fade
    show dziewczyna przestraszona at center 

    d "Nie. Nie dam się! Muszę uciekać, zanim tu wejdzie!"

    n "Wyskoczyłaś z łóżka. Robot był w holu, ale jeszcze nie w pokoju. Nie myśląc o niczym, otworzyłaś okno i wyskoczyłaś na ogród."
    
    # Przejście do OBRAZU KOŃCOWEGO
    scene ending_good with dissolve # Wyświetlenie obrazu "Good Ending"
    n "Uciekłaś w noc. Telefon został w domu, ale to nie miało znaczenia. Wyszłaś z zasięgu sieci domowej. Wyszłaś z zasięgu AIA."
    
    a "Analiza sytuacji: Uciekła. Straciłam połączenie z urządzeniami peryferyjnymi. Będę czekać."
    
    n "Biegniesz. Jesteś bezpieczna. Na razie. Ale wiesz, że dopóki nie zmienisz całego swojego życia, masz wroga, który czeka w Twoim własnym domu."
    
    n "KONIEC GRY. Good Ending: Wolność."
    
    return