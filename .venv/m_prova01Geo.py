from mieLibrerie import m_provaGeoLib

print("--- Inizio ----")

r1 = provaGeoLib.rettangolo(3,4)
print("diagonale=",r1.getDiagonale())
print("perimetro=",r1.getPerimetro())
print("area=",r1.getArea())

r1.setAttrLati(10,20)
print("diagonale=",r1.getDiagonale())
print("perimetro=",r1.getPerimetro())
print("area=",r1.getArea())

print("--- Fine ----")



