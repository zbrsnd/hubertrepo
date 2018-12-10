#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy_orm.py

from model_orm import *

# ~def kw01():
    # ~query = Uczen.select().order_by(Uczen.nazwisko.asc())
    # ~query = Uczen.select().where(Uczen.imie.startswith('G'))
    # ~query = Uczen.select().where(Uczen.imie.endswith('a'))
    # ~query = Uczen.select().where(Uczen.imie == 'Rafał')
    # ~query = Uczen.select().where(Uczen.egz_mat > 40)
    # ~query = Uczen.select().where(Uczen.egz_mat.between(30,35)
    
    # ~for obj in query:
        # ~print(obj.nazwisko, obj.imie)
        

# ~def kw02():
    # ~query = (Uczen
        # ~.select(Uczen.nazwisko, Uczen.imie, Uczen.klasa.nazwa)
        # ~.join(Klasa).order_by(Uczen.klasa.asc())
    # ~)
    # ~for obj in query:
        # ~print(obj.nazwisko, obj.imie)
    
def kw03():
    query = (Ocena
        .select(Ocena.uczen.nazwisko, fn.AVG(Ocena.ocena).alias('ile_ocen'))
        .join(Uczen)
        .group_by(Ocena.uczen.nazwisko)
    )
    for obj in query:
        print(obj.uczen.nazwisko, obj.ile_ocen)
    
def kw04():
    query = (Ocena
        .select(Ocena.uczen, fn.COUNT(Ocena.ocena).alias('ile_ocen'))
        .join(Uczen)
        .group_by(Ocena.uczen.nazwisko)
        .order_by(SQL('ile_ocen').asc())
    )
    for obj in query:
        print(obj.uczen.nazwisko, obj.ile_ocen)
    
def kw05():
    query = (Ocena
        .select(Ocena.uczen.nazwisko, Ocena.przedmiot.przedmiot, fn.AVG(Ocena.ocena).alias('ile_ocen'))
        .join(Uczen)
        .switch(Ocena)
        .join(Przedmiot)
        .where(Ocena.uczen.nazwisko == 'Szymczak')
        .group_by(Ocena.przedmiot.przedmiot)
        .order_by(SQL('ile_ocen').asc())
    )
    for obj in query:
        print(obj.uczen.nazwisko, obj.przedmiot.przedmiot, obj.ile_ocen)
    
def kw06():
    query = (Ocena
        .select(Ocena.przedmiot.przedmiot, fn.AVG(Ocena.ocena).alias('ile_ocen'))
        .join(Przedmiot)
        .group_by(Ocena.przedmiot.przedmiot)
        .order_by(SQL('ile_ocen').asc())
    )
    for obj in query:
        print(obj.przedmiot.przedmiot, obj.ile_ocen)
    
def kw07():
    query = (Uczen
        .select(Uczen.nazwisko, fn.COUNT(Uczen.imie).alias('ile_uczniow'))
        .join(Klasa)
        .group_by(Uczen.klasa.klasa)
        .order_by(SQL('ile_uczniow').asc())
    )
    for obj in query:
        print(obj.klasa.nazwa, obj.ile_uczniow)
    

def main(args):
    baza.connect()
    
    # ~kw01()
    kw07()
    
    baza.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))