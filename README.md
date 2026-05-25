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

## Dateien

- `produkt_tu_stunde_19950101_20241231_02812.txt` – Rohdaten (stündliche Temperaturen)
- `Metadaten_Geographie_02812.txt` – Stationsmetadaten
- `analyse.py` – Analyse- und Plot-Skript
- `klimatrend_lahr.png` – Ergebnisgraph
