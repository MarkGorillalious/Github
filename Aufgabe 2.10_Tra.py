
#a)
import math
pi=math.pi


def rechteckumfang(länge,breite):
    umfang=2*(länge+breite)
    return umfang
def rechteckfläche(länge,breite):
    fläche=länge*breite
    return fläche


def kreisumfang(radius):
    umfang=radius*2*pi
    return umfang
def kreisfläche(radius):
    fläche=radius**2*pi
    return fläche


def quadervolumen(länge,breite,höhe):
    volumen=rechteckfläche(länge,breite)*höhe
    return volumen
def quaderoberfläche(länge,breite,höhe):
    oberfläche=2*(rechteckfläche(länge,breite)+rechteckfläche(breite,höhe)+rechteckfläche(höhe,länge))
    return oberfläche


def zylindervolumen(radius,höhe):
    volumen=kreisfläche(radius)*höhe
    return volumen
def zylindermantelfläche(radius,höhe):
    mantelfläche=kreisumfang(radius)*höhe
    return mantelfläche
def zylinderoberfläche(radius,höhe):
    oberfläche=zylindermantelfläche(radius,höhe)+2*kreisfläche(radius)
    return oberfläche



#b)

#Körper 1:
länge1=8
breite1=8
höhe1=4
radius1=(länge1-4)/2

körper1volumen=quadervolumen(länge1,breite1,höhe1)-(zylindervolumen(radius1,breite1))/2

körper1oberfläche=quaderoberfläche(länge1,breite1,höhe1)+(zylindermantelfläche(radius1,höhe1))/2-kreisfläche(radius1)-rechteckfläche(breite1,2*radius1)


#Körper 2:
kante2=5
radius2=kante2/2

körper2volumen=quadervolumen(kante2,kante2,kante2)+zylindervolumen(radius2,kante2)/2

körper2oberfläche=quaderoberfläche(kante2,kante2,kante2)-rechteckfläche(kante2,kante2)+kreisfläche(radius2)+zylindermantelfläche(radius2,kante2)/2


#Körper 3:
rklein=1
rgroß=3.5
hklein=9.2
hgroß=3

körper3volumen=zylindervolumen(rklein,hklein)+zylindervolumen(rgroß,hgroß)

körper3oberfläche=zylindermantelfläche(rklein,hklein)+zylindermantelfläche(rgroß,hgroß)+2*kreisfläche(rgroß)


#Körper 4:
radius4=7
höhe4=18

körper4volumen=3/4*zylindervolumen(radius4,höhe4)

körper4oberfläche=3/4*zylinderoberfläche(radius4,höhe4)+2*rechteckfläche(radius4,höhe4)


##Überprüfen:
print('köper1', körper1volumen, 'und', körper1oberfläche)
print('köper2', körper2volumen, 'und', körper2oberfläche)
print('köper3', körper3volumen, 'und', körper3oberfläche)
print('köper4', körper4volumen, 'und', körper4oberfläche)

