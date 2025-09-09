import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='password',
         autocommit=True,

        # mysql.connector.errors.DatabaseError: 1273 (HY000): Unknown collation: 'utf8mb4_0900_ai_ci'
        # if you see above error, fix could be to define collation as shown below:
        collation='utf8mb3_general_ci'
         )

def hae_lentokentät():
    kursori = yhteys.cursor()
    kursori.execute("SELECT ident, name FROM airport LIMIT 5")

    # kaikki -muuttuja pitää sisällän listan tupleja
    kaikki = kursori.fetchall()
    print(kaikki)

    """
    #sql = f"SELECT name, ident FROM airport LIMIT 5"
    #print(sql)
    # tulostetaan listan ensimmäinen alkio
    print(kaikki[0])
    # tulostetaan listan toinen alkio
    print(kaikki[1])
    #tulostetaan listan viimeinen alkio
    print(kaikki[-1])

    viimeisen_kentän_nimi = kaikki[-1][1]
    (ident, nimi) = kaikki[-1]
    print(viimeisen_kentän_nimi)
    print(f"ident: {ident}, nimi: {nimi}")

    for arvo in kaikki:
        print(arvo)
        print(arvo[0])
        print(arvo[1])

    print(kursori.rowcount)
    """

def hae_kenttä_ident_koodilla(ident):
    sql = f"SELECT * FROM airport WHERE ident = \"{ident}\""
    sql = f"SELECT * FROM airport WHERE ident = '{ident}'"
    sql = f'SELECT * FROM airport WHERE ident = "{ident}"'
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    data = kursori.fetchall()
    print(data)

def muokkaa_kentän_nimeä(ident, uusi_nimi):
    sql = f"UPDATE airport SET name = '{uusi_nimi}' WHERE ident = '{ident}' LIMIT 1"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    if kursori.rowcount == 1:
        print("Jee update toimi")

hae_kenttä_ident_koodilla("00A")
hae_kenttä_ident_koodilla("00KS")
muokkaa_kentän_nimeä("00KS", "Kiva kenttä")

#hae_lentokentät()