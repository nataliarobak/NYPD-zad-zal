from ._srednie_gender import srednie_gender
from ._srednie_wiek import srednie_wiek
from ._korelacje import korelacje

def analize_data(dane: dict) -> dict:
    #srednie dla plci
    sg = srednie_gender(dane)

    # Srednia dla grup wiekowych
    sw = srednie_wiek(dane)

    #korelacje
    kor = korelacje(dane, plot=True)

    return {"srednie_gender": sg, "srednie_wiek": sw, "korelacje": kor}
