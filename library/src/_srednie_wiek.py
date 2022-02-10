import pandas as pd

def srednie_wiek(dataset: dict) -> dict:
    wszyscy = []
    for osoba in dataset.values():
        wszyscy.append(osoba)
    wszyscy = pd.DataFrame(wszyscy)
    mediana = wszyscy["age"].median()

    mlodsi, starsi = [], []
    srednie_M_S = {"mlodsi": 0, "starsi": 0}

    for osoba in dataset.values():
        if osoba["age"] <= mediana:
            mlodsi.append(osoba)
        else:
            starsi.append(osoba)

    for ml in mlodsi:
        srednie_M_S["mlodsi"] += sum(ml["total_UPDRS"]) / len(ml["total_UPDRS"])
    srednie_M_S["mlodsi"] /= len(mlodsi)
    srednie_M_S["mlodsi"] = round(srednie_M_S["mlodsi"], 2)

    for st in starsi:
        srednie_M_S["starsi"] += sum(st["total_UPDRS"]) / len(st["total_UPDRS"])
    srednie_M_S["starsi"] /= len(starsi)
    srednie_M_S["starsi"] = round(srednie_M_S["starsi"], 2)

    return srednie_M_S
