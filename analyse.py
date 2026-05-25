import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from scipy import stats

# --- Daten laden ---
df = pd.read_csv(
    "produkt_tu_stunde_19950101_20241231_02812.txt",
    sep=";",
    dtype=str
)
df.columns = [c.strip() for c in df.columns]
df["TT_TU"] = pd.to_numeric(df["TT_TU"], errors="coerce")
df["MESS_DATUM"] = df["MESS_DATUM"].str.strip()
df["Jahr"] = df["MESS_DATUM"].str[:4].astype(int)

# Ungültige Werte filtern (-999 = fehlend im DWD-Format)
df = df[df["TT_TU"] > -90]

# --- Jahresdurchschnitte berechnen ---
jahres = df.groupby("Jahr")["TT_TU"].agg(["mean", "min", "max", "std"]).reset_index()
jahres.columns = ["Jahr", "Mittel", "Min", "Max", "Std"]

# Trend berechnen (lineare Regression)
slope, intercept, r, p, se = stats.linregress(jahres["Jahr"], jahres["Mittel"])
trend_line = intercept + slope * jahres["Jahr"]
gesamt_erwaermung = slope * (jahres["Jahr"].iloc[-1] - jahres["Jahr"].iloc[0])

print(f"Station: Lahr (ID 2812)")
print(f"Zeitraum: {jahres['Jahr'].iloc[0]}–{jahres['Jahr'].iloc[-1]}")
print(f"Erwärmungstrend: +{slope*10:.2f} °C pro Dekade")
print(f"Gesamterwärmung: +{gesamt_erwaermung:.2f} °C ({jahres['Jahr'].iloc[0]}–{jahres['Jahr'].iloc[-1]})")

# --- Referenzperiode 1995–2014 (erste 20 Jahre) ---
ref = jahres[jahres["Jahr"] <= 2014]["Mittel"].mean()

# --- Plot ---
fig, ax = plt.subplots(figsize=(14, 7))
fig.patch.set_facecolor("#0f0f1a")
ax.set_facecolor("#0f0f1a")

jahre = jahres["Jahr"].values
mittel = jahres["Mittel"].values

farben = ["#e05050" if t > ref else "#5090e0" for t in mittel]

bars = ax.bar(jahre, mittel, color=farben, alpha=0.85, width=0.7, zorder=3)
ax.axhline(ref, color="#aaaaaa", linestyle="--", linewidth=1.2, alpha=0.7,
           label=f"Referenz Ø 1995–2014: {ref:.2f} °C", zorder=4)
ax.plot(jahre, trend_line, color="#ffcc00", linewidth=2.5, linestyle="-",
        label=f"Trend: +{slope*10:.2f} °C/Dekade (r²={r**2:.2f})", zorder=5)

idx_max = jahres["Mittel"].idxmax()
idx_min = jahres["Mittel"].idxmin()
ax.annotate(f"{mittel[idx_max]:.1f} °C",
            xy=(jahre[idx_max], mittel[idx_max]),
            xytext=(0, 8), textcoords="offset points",
            ha="center", color="#ff8888", fontsize=8.5, fontweight="bold")
ax.annotate(f"{mittel[idx_min]:.1f} °C",
            xy=(jahre[idx_min], mittel[idx_min]),
            xytext=(0, -14), textcoords="offset points",
            ha="center", color="#88aaff", fontsize=8.5, fontweight="bold")

ax.set_xlim(1994.3, 2024.7)
ax.set_xlabel("Jahr", color="#cccccc", fontsize=12)
ax.set_ylabel("Jahresdurchschnittstemperatur (°C)", color="#cccccc", fontsize=12)
ax.tick_params(colors="#cccccc", labelsize=10)
for spine in ax.spines.values():
    spine.set_edgecolor("#333355")
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.grid(axis="y", color="#222244", linewidth=0.8, zorder=0)
ax.grid(axis="x", color="#1a1a2e", linewidth=0.5, zorder=0)

leg = ax.legend(framealpha=0.2, facecolor="#111122", edgecolor="#444466",
                labelcolor="#cccccc", fontsize=10)
ax.set_title(
    f"Jahresdurchschnittstemperatur – Station Lahr (DWD, 1995–2024)\n"
    f"Gesamterwärmung: +{gesamt_erwaermung:.2f} °C",
    color="white", fontsize=14, fontweight="bold", pad=15
)

from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor="#e05050", alpha=0.85, label="Wärmer als Referenz"),
    Patch(facecolor="#5090e0", alpha=0.85, label="Kälter als Referenz"),
]
ax2_leg = ax.legend(handles=legend_elements, loc="upper left",
                    framealpha=0.2, facecolor="#111122", edgecolor="#444466",
                    labelcolor="#cccccc", fontsize=9)
ax.add_artist(leg)

plt.tight_layout()
plt.savefig("klimatrend_lahr.png", dpi=150, bbox_inches="tight",
            facecolor=fig.get_facecolor())
print("Graph gespeichert: klimatrend_lahr.png")
