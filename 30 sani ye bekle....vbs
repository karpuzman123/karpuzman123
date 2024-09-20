WScript.Sleep 30000 ' 30 saniye bekler (30.000 milisaniye = 30 saniye). İstersen bunu uzatabilirsin.
Do
    Randomize
    waitTime = Int((10 * Rnd) + 1) * 1000 ' 1-10 saniye arasında rastgele bekleme süresi
    WScript.Sleep waitTime
    MsgBox "Neden bu mesajı görüyorsun? Bir şeyler ters gidiyor olabilir...", 16, "Gizli Mesaj"
Loop