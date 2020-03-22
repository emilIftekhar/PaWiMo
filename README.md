# Lokale wirtschaftliche Auswirkungen von COVID19 in Deutschland

Hier geht es zum Projekt auf [Devpost](https://devpost.com/software/1_047_b_wirtschaftliche_auswirkungen_806).

Erstellung eines georäumlich-zeitlichen Modells für die Ausbreitung von COVID-19 und die Bewertung der Auswirkung auf die Bevölkerung und Wirtschaft. 

Das Dashboard ist aktuell nur ein Prototyp, der mit Jupyter, Vuetify und Voila erstellt wurde. In den nächsten Tagen müssen noch die Modelle fertiggestellt, evaluiert und integriert werden.

Um das Dashboard zu starten, müssen die Dependencies aus conda_environment.yml installiert sein. Gestartet wird es mit:

    voila --template project_path\template Dashboard.ipynb

## Quellen
Das Infektionsmodell basiert auf dem Bayesian spatio-temporal interaction model: [GitHub](https://github.com/ostojanovic/BSTIM), [Paper](https://www.biorxiv.org/content/10.1101/617795v1)

Die Wirtschaftsdaten (data/economic/) sind von DeStatis (Statistisches Bundesamt).

Die Meldezahlen vom Robert Koch Institut werden per API über die [Nationale Plattform für geographische Daten (NPGEO-DE)](https://npgeo-corona-npgeo-de.hub.arcgis.com/datasets/dd4580c810204019a7b8eb3e0b329dd6_0?orderBy=Meldedatum) abgefragt.

## Haftungsausschluss
Wir stellen den Code zur Weiterentwicklung zur Verfügung. Aktuell können noch keine Prognosen getroffen werden. Des Weiteren ist zu beachten, dass auch die Ergebnisse des fertigen statistischen Modells von der tatsächlichen Entwicklung abweichen können.

---

# Local Business Impact of COVID19 in Germany
View it on [Devpost](https://devpost.com/software/1_047_b_wirtschaftliche_auswirkungen_806).

Geospatial-temporal modelling of COVID-19 and its impact on population and economy.

Currently, the dashboard is just a prototype, which was created using Jupyter, Vuetify and Voila. In the next days, we have to complete and evaluate the models as well as integrating them into the dashboard.

To run the Dashboard install the dependencies from conda_environment.yml and run:

    voila --template project_path\template Dashboard.ipynb
    
## References
The infection model is based on the Bayesian spatio-temporal interaction model: [GitHub](https://github.com/ostojanovic/BSTIM), [Paper](https://www.biorxiv.org/content/10.1101/617795v1)

The economic data (data/economic/) is from DeStatis (German Federal Statistical Office).

The reporting figures from the Robert Koch Institute are queried via API through the [National Platform for Geographic Data (NPGEO-DE)](https://npgeo-corona-npgeo-de.hub.arcgis.com/datasets/dd4580c810204019a7b8eb3e0b329dd6_0?orderBy=Meldedatum).

## Disclaimer
We provide the code (as it is) for further development. At the moment no forecasts can be made. Furthermore, it should be noted that even the results of the finished statistical model may deviate from the actual development.
