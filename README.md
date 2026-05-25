# Klimadaten Lahr (DWD)

Analyse der Jahresdurchschnittstemperaturen der DWD-Wetterstation **Lahr** (ID 02812, Baden-Württemberg) von 1995 bis 2024.

## Datenquelle

- **Quelle:** Deutscher Wetterdienst (DWD) Open Data
- **URL:** https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/air_temperature/historical/stundenwerte_TU_02812_19950101_20241231_hist.zip
- **Station:** Lahr, 155 m ü. NN (48.365°N, 7.828°E)
- **Zeitraum:** 01.01.1995 – 31.12.2024
- **Auflösung:** stündlich

## Ergebnisse

| Kennzahl | Wert |
|---|---|
| Gesamterwärmung (1995–2024) | **+1,80 °C** |
| Trend | **+0,62 °C pro Dekade** |
| Kältestes Jahr | 1996 (9,3 °C) |
| Wärmstes Jahr | 2023 (12,9 °C) |
| Referenz-Ø (1995–2014) | 10,94 °C |

## Datenqualität

Die Rohdaten enthalten **52 fehlende Messstunden** (von ~262.000 gesamt, ~0,02 %), die der DWD mit dem Platzhalterwert `-999` kennzeichnet. Diese Werte treten an folgenden Zeiträumen auf:

- 13.01.2014, 01–04 Uhr (4 Stunden)
- 29.06.2021, 14 Uhr (1 Stunde)
- 28.02.2023 – 02.03.2023 (47 Stunden)

Im Analyse-Skript werden alle Werte unter −90 °C herausgefiltert (`df[df["TT_TU"] > -90]`), sodass die −999-Einträge nicht in die Berechnung einfließen. Der Einfluss auf die Jahresdurchschnitte ist aufgrund des geringen Anteils vernachlässigbar.

## Dateien

- `produkt_tu_stunde_19950101_20241231_02812.txt` – Rohdaten (stündliche Temperaturen)
- `Metadaten_Geographie_02812.txt` – Stationsmetadaten
- `analyse.py` – Analyse- und Plot-Skript
- `klimatrend_lahr.png` – Ergebnisgraph
