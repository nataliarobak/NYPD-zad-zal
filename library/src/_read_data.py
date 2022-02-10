def read_data(source_filename: str) -> dict:
    # int: ID, Age, Gender | float: test_time, ...
    with open(source_filename, 'r', errors="ignore", encoding="utf-8") as plik:
        dane_parkinson = plik.readlines()[1:]
    przetworzone_dane = {}
    for wiersz in dane_parkinson:
        wiersz = wiersz.strip().split(',')
        for pozycja in range(len(wiersz)):
            if pozycja < 3:
                wiersz[pozycja] = int(wiersz[pozycja])
            else:
                wiersz[pozycja] = float(wiersz[pozycja])
        # Grupowanie
        identyfikator = wiersz[0]
        if identyfikator in przetworzone_dane:
            przetworzone_dane[identyfikator]["test-time"].append(wiersz[3])
            przetworzone_dane[identyfikator]["motor_UPDRS"].append(wiersz[4])
            przetworzone_dane[identyfikator]["total_UPDRS"].append(wiersz[5])
            # Jitter
            przetworzone_dane[identyfikator]["jitter"]["jitter%"].append(wiersz[6])
            przetworzone_dane[identyfikator]["jitter"]["jitter-abs"].append(wiersz[7])
            przetworzone_dane[identyfikator]["jitter"]["jitter-rap"].append(wiersz[8])
            przetworzone_dane[identyfikator]["jitter"]["jitter-ppq5"].append(wiersz[9])
            przetworzone_dane[identyfikator]["jitter"]["jitter-ddp"].append(wiersz[10])
            # Shimmer
            przetworzone_dane[identyfikator]["shimmer"]["shimmer"].append(wiersz[11])
            przetworzone_dane[identyfikator]["shimmer"]["shimmer-db"].append(wiersz[12])
            przetworzone_dane[identyfikator]["shimmer"]["shimmer-apq3"].append(wiersz[13])
            przetworzone_dane[identyfikator]["shimmer"]["shimmer-apq11"].append(wiersz[14])
            przetworzone_dane[identyfikator]["shimmer"]["shimmer-dda"].append(wiersz[15])
            # Inne dane
            przetworzone_dane[identyfikator]["NHR"].append(wiersz[16])
            przetworzone_dane[identyfikator]["HNR"].append(wiersz[17])
            przetworzone_dane[identyfikator]["RPDE"].append(wiersz[18])
            przetworzone_dane[identyfikator]["DFA"].append(wiersz[19])
            przetworzone_dane[identyfikator]["PPE"].append(wiersz[20])
        else:
            przetworzone_dane[identyfikator] = {
                "age": wiersz[1],
                "gender": "female" if wiersz[2] else "male",
                "test-time": [wiersz[3]],
                "motor_UPDRS": [wiersz[4]],
                "total_UPDRS": [wiersz[5]],
                "jitter": {"jitter%": [wiersz[6]],
                           "jitter-abs": [wiersz[7]],
                           "jitter-rap": [wiersz[8]],
                           "jitter-ppq5": [wiersz[9]],
                           "jitter-ddp": [wiersz[10]]},
                "shimmer": {"shimmer": [wiersz[11]],
                            "shimmer-db": [wiersz[12]],
                            "shimmer-apq3": [wiersz[13]],
                            "shimmer-apq11": [wiersz[14]],
                            "shimmer-dda": [wiersz[15]]},
                "NHR": [wiersz[16]],
                "HNR": [wiersz[17]],
                "RPDE": [wiersz[18]],
                "DFA": [wiersz[19]],
                "PPE": [wiersz[20]]
            }
    return przetworzone_dane
