Dim speaks, speech
speaks="Sisteminizde ciddi bir hata var..."
Set speech=CreateObject("sapi.spvoice")
speech.Speak speaks

Do
    MsgBox "Sisteminizde geri dönülemez bir hata tespit edildi!", 16, "Kritik Hata"
    MsgBox "Bilgisayarınız çökmek üzere!", 16, "KRPUZUN İNTİKAMI"
    MsgBox "AHAHHAHA!", 16, "YOKLAN?"
Loop
