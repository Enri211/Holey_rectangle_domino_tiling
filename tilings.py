import random
from PIL import Image, ImageOps
from sympy import *

#This function merges two images.
def merge(im1: Image.Image, im2: Image.Image) -> Image.Image:
    w = (im1.size[0] + im2.size[0]) 
    h = 200
    im = Image.new("RGB", (w, h))

    im.paste(im1)
    im.paste(im2, (im1.size[0], 0))
    return im

#This function generates a domino tiling of the 2xn rectangle.
def rect(tam):
    if tam == 0:
        im = Image.new("RGB",[1,200])
        return im
    if tam == 1:
        im = random.choice([domino1, domino2])
        return im
    if tam == 2:
        a = random.choice([0,1])
        im = juntos.transpose(a*2)
        return im
    if tam > 2:
        #vertical=0, horizontal=1, o=orientacion
        o = random.choice([0,1])
        if o == 0:
            im1 = rect(1)
            im2 = rect(tam-1)
            im = merge(im1,im2)
            return im
        if o == 1:
            im1 = rect(2)
            im2 = rect(tam-2)
            im = merge(im1,im2)
            return im

#This function generates one of the "irregular" tilings of the mxn holey rectangle,
#The tiling is constructed by fixing a horizontal domino in the top left corner.
#This tiling always has the same color pattern. 

def desfase(m,n):
    fondo = Image.new("RGB", [m*100, n*100])
    fondo.paste(domino1.transpose(2))
    a = 200
    count = 0
    while a < m*100 - 100:
        if count%2 == 0:
            fondo.paste(domino2.transpose(2), [a,0])
        if count%2 == 1:
            fondo.paste(domino1.transpose(2),[a,0])
        count += 1
        a += 200
    
    b = 100
    coun = 0
    while b <= m*100 - 300:
        if count%2 == 0:
            fondo.paste(domino2.transpose(2),[b, 100])
        if count%2 == 1:
            fondo.paste(domino1.transpose(2),[b, 100])
        count += 1
        b += 200
    
    c = 100
    count = 0
    while c < n*100 - 100:
        if count%2 == 0:
            fondo.paste(domino2,[0,c])
        if count%2 == 1:
            fondo.paste(domino1,[0,c])
        count += 1
        c += 200
        
    d = 200
    count = 0
    while d < n*100 - 200:
        if count%2 == 0:
            fondo.paste(domino2,[100,d])
        if count%2 == 1:
            fondo.paste(domino1,[100,d])
        count += 1
        d += 200
    
    if m%2 == 1:
        x = 0
        count = 0
        while x < n*100 - 100:
            if count%2 == 0:
                fondo.paste(domino2,[m*100-100,x])
            if count%2 == 1:
                fondo.paste(domino1,[m*100-100,x])
            count += 1
            x += 200
        x = 100
        count = 0
        while x < n*100 - 200:
            if count%2 == 0:
                fondo.paste(domino2,[m*100-200,x])
            if count%2 == 1:
                fondo.paste(domino1,[m*100-200,x])
            count += 1
            x += 200
            
    if n%2 == 0:
        x = 0
        count = 0
        while x < m*100 - 100:
            if count%2 == 0:
                fondo.paste(domino2.transpose(2), [x, n*100 - 100])
            if count%2 == 1:
                fondo.paste(domino1.transpose(2),[x,n*100 - 100])
            count += 1
            x += 200
        x = 100
        count = 0
        while x <= m*100 - 300:
            if count%2 == 0:
                fondo.paste(domino1.transpose(2), [x, n*100 - 200])
            if count%2 == 1:
                fondo.paste(domino2.transpose(2),[x,n*100 - 200])
            count += 1
            x += 200

    if m%2 == 0:
        x = 100
        count = 0
        while x < n*100 - 100:
            if count%2 == 0:
                fondo.paste(domino2,[m*100-100,x])
            if count%2 == 1:
                fondo.paste(domino1,[m*100-100,x])
            count += 1
            x += 200
        x = 200
        count = 0
        while x < n*100 - 200:
            if count%2 == 0:
                fondo.paste(domino2,[m*100-200,x])
            if count%2 == 1:
                fondo.paste(domino1,[m*100-200,x])
            count += 1
            x += 200
            
    if n%2 == 1:
        x = 100
        count = 0
        while x < m*100 - 100:
            if count%2 == 0:
                fondo.paste(domino2.transpose(2), [x, n*100 - 100])
            if count%2 == 1:
                fondo.paste(domino1.transpose(2),[x,n*100 - 100])
            count += 1
            x += 200
        x = 200
        count = 0
        while x <= m*100 - 300:
            if count%2 == 0:
                fondo.paste(domino2.transpose(2), [x, n*100 - 200])
            if count%2 == 1:
                fondo.paste(domino1.transpose(2),[x, n*100 - 200])
            count += 1
            x += 200        
    
    return fondo
        
#This function generates a tiling of the mxn holey rectangle,
#The tiling is constructed by fixing a horizontal domino in the top left corner,
#We divide the holey rectangle in regions, then we fill these regions in a proper way.
#The color pattern of the same tiling may vary.   

def construye(m,n):
    #0 = no pasa, 1 = pasa
    x = random.choice([0,1])
    y = random.choice([0,1])
    z = random.choice([0,1])
    decisiones = [x,y,z]

    fondo = Image.new("RGB", [m*100, n*100])
    domI = random.choice([domino1, domino2]) 
    fondo.paste(domI.transpose(2))

    if decisiones[0] == 0: 
        columna1 = rect(n-1)
        fondo.paste(columna1.transpose(2),[0,100])
    
        if decisiones[1] == 0:
            columna2 = rect(m-2)
            fondo.paste(columna2,[200,(n*100)-200])
        
            if decisiones[2] == 0:
                columna3 = rect(n-2)
                fondo.paste(columna3.transpose(2),[(m*100)-200,0])
                fondo.paste(rect(m-4),[200,0])
            if decisiones[2] == 1:
                columna3 = rect(n-4)
                fondo.paste(columna3.transpose(2),[(m*100)-200,200])
                fondo.paste(random.choice([domino1, domino2]), [(m*100)-100,0])
                a = random.choice([2,4])
                fondo.paste(juntos.transpose(a), [(m*100)-300,0])
                fondo.paste(rect(m-5), [200,0])
            
        if decisiones[1] == 1:
            columna2 = rect(m-4)
            fondo.paste(columna2,[200,(n*100)-200])
            domA = random.choice([domino1, domino2])
            fondo.paste(domA.transpose(2), [(m*100)-200,(n*100)-100])
            a = random.choice([0,1])
            fondo.paste(juntos.transpose(a), [(m*100)-200,(n*100)-300])
            if decisiones[2] == 0:
                columna3 = rect(n-3)
                fondo.paste(columna3.transpose(2),[(m*100)-200,0])
                fondo.paste(rect(m-4),[200,0])
            if decisiones[2] == 1:
                columna3 = rect(n-5)
                fondo.paste(columna3.transpose(2),[(m*100)-200,200])
                fondo.paste(random.choice([domino1, domino2]), [(m*100)-100,0])
                a = random.choice([2,4])
                fondo.paste(juntos.transpose(a), [(m*100)-300,0])
                fondo.paste(rect(m-5), [200,0])            

    if decisiones[0] == 1:
        columna1 = rect(n-3)
        fondo.paste(columna1.transpose(2),[0,100])
        fondo.paste(random.choice([domino1, domino2]), [0,(n*100)-200])
        a = random.choice([2,4])
        fondo.paste(juntos.transpose(a), [100,(n*100)-200])
        
        if decisiones[1] == 0:
            columna2 = rect(m-3)
            fondo.paste(columna2,[300,(n*100)-200])
            
            if decisiones[2] == 0:
                columna3 = rect(n-2)
                fondo.paste(columna3.transpose(2),[(m*100)-200,0])
                fondo.paste(rect(m-4),[200,0])

            if decisiones[2] == 1:
                columna3 = rect(n-4)
                fondo.paste(columna3.transpose(2),[(m*100)-200,200])
                fondo.paste(random.choice([domino1, domino2]), [(m*100)-100,0])
                a = random.choice([2,4])
                fondo.paste(juntos.transpose(a), [(m*100)-300,0])
                fondo.paste(rect(m-5), [200,0])
                
        if decisiones[1] == 1:
            columna2 = rect(m-5)
            fondo.paste(columna2,[300,(n*100)-200])
            domA = random.choice([domino1, domino2])
            fondo.paste(domA.transpose(2), [(m*100)-200,(n*100)-100])
            a = random.choice([0,1])
            fondo.paste(juntos.transpose(a), [(m*100)-200,(n*100)-300])
            if decisiones[2] == 0:
                columna3 = rect(n-3)
                fondo.paste(columna3.transpose(2),[(m*100)-200,0])
                fondo.paste(rect(m-4),[200,0])
            if decisiones[2] == 1:
                columna3 = rect(n-5)
                fondo.paste(columna3.transpose(2),[(m*100)-200,200])
                fondo.paste(random.choice([domino1, domino2]), [(m*100)-100,0])
                a = random.choice([2,4])
                fondo.paste(juntos.transpose(a), [(m*100)-300,0])
                fondo.paste(rect(m-5), [200,0])
    return fondo

#This function returns a random tiling of the mxn holey rectangle.
#There are two kinds of tilings, those with a horizontal domino in the top left corner, and those with a vertical domino in the top left corner,
#To generate a tiling of the second kind we can generate a nxm tiling with a horizontal domino and then rotate and reflect the tiling.

def anillo(m,n):
    elec = random.randint(1,100)
    if 1 <= elec <= 49:
        return construye(m,n)
    if 50 <= elec <= 98:
        ring = construye(n,m).transpose(0).transpose(2)
        return ring
    if elec == 99:
        return desfase(m,n)
    if elec == 100:
        ring = desfase(n,m).transpose(0).transpose(2)
        return ring

#The next bunch of code constructs the dominoes used in the functions.
#Here we can change the colors of the dominoes.

domino1 = Image.new("RGB", [98,198], "Gold")
domino1 = ImageOps.expand(domino1, 1)
domino2 = Image.new("RGB", [98,198], "Navy")
domino2 = ImageOps.expand(domino2, 1)
juntos = merge(domino1, domino2)

#Here we can change the size of the rectangle,
#m = width, n = height, with m,n >=5,

m = 5
n = 5

#technically the program can generate random tilings of a 4x4 square (since it is a degenerate case of the holey rectangle), but errors may happen. 

Imagen = anillo(m,n)
Imagen.show()

#The last part of the code calculates the total number of domino tilings of the mxn holey rectangle:

t = (fibonacci(n-1)*fibonacci(m-1) + fibonacci(n-2)*fibonacci(m-2) + fibonacci(n-3)*fibonacci(m-3))**2 + 2*(1+ (-1)**(n+m+1))
print("The total number of domino tilings of the ", m, "x", n, " holey rectangle is: ",  t)
