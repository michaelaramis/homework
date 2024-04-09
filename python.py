import vlc

lavacalola = vlc.MediaPlayer("La Vaca Lola - Canciones de La Granja de Zenón 2.mp3") 
lasruedasdelbus = vlc.MediaPlayer("Las Ruedas del Bus.mp3")
laoldskul = vlc.MediaPlayer("La old skul.mp3")
dondeseaprendeaquerer = vlc.MediaPlayer("Donde se aprende a querer.mp3")
diluvio = vlc.MediaPlayer("Diluvio.mp3")
songs = [lavacalola,lasruedasdelbus, laoldskul, dondeseaprendeaquerer, diluvio ]

print('''
1.la vaca lola
2.las ruedas del camion
3.la old skul
4.donde se aprende a querer
5.diluvio
''')
songnumber = int(input("Elige el numero de la cancion que desee braulio: "))

if songnumber == 1:
    lavacalola.play()

elif songnumber == 2:
    lasruedasdelbus.play()

elif songnumber == 3:
    laoldskul.play()

elif songnumber == 4:
    dondeseaprendeaquerer.play()

elif songnumber == 5:
    diluvio.play()

else:
    print("Eso no existe braulio")

input()

