Set objShell = CreateObject("Wscript.Shell")

' Rastgele zamanla jumpscare yarat
Wscript.Sleep (Int((15000 - 5000 + 1) * Rnd + 5000)) ' 5 ile 15 saniye arası rastgele bekleme
objShell.Run "mplay32 /play /close korku.wav" ' Korku sesini oynat
objShell.Run "mspaint adsız" ' Korkutucu resmi aç