def suhu(x):
    reamur = x * 4/5
    fahrenheit = (x * 9/5)+32
    kelvin = x + 273
    print("suhu dalam reamur : " + str(reamur))
    print("suhu dalam fahrenheit : " + str(fahrenheit))
    print("suhu dalam kelvin : " + str(kelvin))

a = int(input("masukkan suhu dalam celcius : "))
suhu(a)