X = int ( input ("masukkan bilangan 1: " ))
Y = int ( input ("masukkan bilangan 2: " ))
Z = int ( input ("masukkan bilangan 3: " ))
if X < Y and X < Z:
    if Y < X:
        print("Urutan bilangan dari yang terkecil adalah", X,Y,Z)
    else:
        print("Urutan bilangan dari yang terkecil adalah", X, Z, Y)
elif Y < X and Y < Z:
    if X < Z:
        print("Urutan bilangan dari yang terkecil adalah", Y,X,Z)
    else:
        print("Urutan bilangan dari yang terkecil adalah", Y,Z,X )
else:
    if X < Y:
        print("Urutan bilangan dari yang terkecil adalah", Z,X,Y)
    else:
        print("Urutan bilangan dari yang terkecil adalah", Z, Y, X)    
