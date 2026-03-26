Statistik mit R für Umweltwissenschaftler:innen

Master Modul "Research Methods" Version 41, 2026

Jürgen Dengler & Stefan Widmer

Inhaltsverzeichnis

[Vorwort 7](#page-5-0)

[Empfohlene weiterführende Literatur 8](#page-6-0)

[Statistik 1 9](#page-7-0)

[Lernziele 9](#page-7-1)

[Warum brauchen wir Statistik? 9](#page-7-2)

[Ein Beispiel 9](#page-7-3)

[Fazit 11](#page-10-0)

[Warum mit R? 11](#page-10-1)

[Was spricht dagegen? 12](#page-11-0)

[Was spricht dafür? 12](#page-11-1)

[Fazit 12](#page-11-2)

[Die Rolle von Hypothesen in der Wissenschaft 13](#page-12-0)

[Rekapitulation 13](#page-12-1)

[Was ist eine Hypothese? 13](#page-12-2)

[Wissenschaftliches Arbeiten \(](#page-13-0)*[in a nutshell](#page-13-0)*) 14

[Die Rolle der Statistik beim Hypothesengenerieren und -testen 15](#page-14-0)

[Von der Hypothese zur Nullhypothese… 15](#page-14-1)

[Einschub: Wichtige Termini in der Statistik 16](#page-15-0)

[Einschub: Parameter vs. Prüfgrössen 17](#page-16-0)

[Statistische Implementierung des Hypothesentestens \(am Beispiel des](#page-17-0) *[t](#page-17-0)*-Tests) 17

[Fehler I. und II. Art 19](#page-18-0)

*[p](#page-20-0)*[-Werte und Signifikanzniveaus 21](#page-20-0)

*[t](#page-21-0)*[-Test \(für eine metrische Variable im Vergleich von zwei Gruppen\) 22](#page-21-0)

[Students und Welch](#page-22-0) *[t](#page-22-0)*-Test 22

[Ein- und zweiseitiger](#page-22-1) *[t](#page-22-1)*-Test 23

[Gepaarter und ungepaarter](#page-23-0) *[t](#page-23-0)*-Test 24

[Binomial-Test \(für die Häufigkeitsverteilung einer binomialen Variablen\) 24](#page-23-1)

[Möglichkeiten, zwei Stichproben zu vergleichen, und Implikationen für das Samplingdesign 26](#page-25-0)

[Gepaarte vs. ungepaart Tests 26](#page-25-1)

[Nutzung des Vorzeichentests bei gepaarten Erhebungen 27](#page-26-0)

[Chi-Quadrat- bzw. Fishers Test \(für die Assoziation zweier binomialer Variablen\) 28](#page-27-0)

[Chi-Quadrat-Test 29](#page-28-0)

[Fishers exakter Test 30](#page-30-0)

[Wie berichtet man statistische Ergebnisse? 31](#page-31-0)

[Welche relevanten Informationen benötige ich und wo finde ich sie? 31](#page-31-1)

[Text, Tabelle oder Abbildung? 32](#page-32-0)

[Abbildungen in wissenschaftlichen Arbeiten 33](#page-33-0)

[Abbildungen mit "base R" oder mit ggplot2? 33](#page-33-1)

[Inferenzstatistik vs. beschreibende Statistik 36](#page-38-0)

[Zusammenfassung 36](#page-39-0)

[Weiterführende Literatur 37](#page-39-1)

[Statistik 2 38](#page-39-2)

[Lernziele 38](#page-40-0)

[Einfaktorielle Varianzanalyse \(](#page-40-1)*[One-Way](#page-40-1)* ANOVA) 38

[Die Idee dahinter 38](#page-40-2)

[Praktische Durchführung 40](#page-41-0)

[Post-hoc-Test \(Tukey\) 42](#page-44-0)

[Mehrfaktorielle ANOVA 45](#page-47-0)

[Voraussetzung statistischer Verfahren 49](#page-52-0)

[Parametrische vs. nicht-parametrische Verfahren 49](#page-52-1)

[Wie testet man die Voraussetzungen? \(klassischer Weg\) 50](#page-53-0)

[Wie testet man die Voraussetzungen? \(empfohlener Weg\) 51](#page-54-0)

[Was tun, wenn die Voraussetzungen verletzt sind? \(nicht-parametrische Verfahren\) 52](#page-59-0)

[Was tun, wenn die Voraussetzungen \(erheblich\) verletzt sind? \(Transformationen\) 54](#page-60-0)

[Zusammenfassung 57](#page-64-0)

[Weiterführende Literatur 57](#page-64-1)

[Statistik 3 58](#page-65-0)

| Lernziele 58                                                               |
|----------------------------------------------------------------------------|
| Korrelationen 58                                                           |
| Einfache lineare Regressionen 60                                           |
| Idee 60                                                                    |
| Statistische Umsetzung 61                                                  |
| Implementierung in R 62                                                    |
| Voraussetzungen 64                                                         |
| Alternativen zur Methode der kleinsten Quadrate (OLS) 65                   |
| Polynomische Regressionen 66                                               |
| Kovarianzanalyse (ANCOVA) 69                                               |
| Lineare Modelle allgemein 71                                               |
| Was macht ein lineares Modell aus? 71                                      |
| Welche Verfahren gehören zu den linearen Modellen? 72                      |
| Testen der Voraussetzungen von linearen Modellen (Modelldiagnostik) 74     |
| Genereller Ablauf einer statistischen Analyse 77                           |
| Zusammenfassung 78                                                         |
| Weiterführende Literatur 78                                                |
| Statistik 4 79                                                             |
| Lernziele 79                                                               |
| Multiple lineare Regressionen 79                                           |
| Vorgehen 79                                                                |
| Problem 1: Korrelation zwischen den Prädiktoren 81                         |
| Problem 2: Overfitting 82                                                  |
| Modellvereinfachung 84                                                     |
| Varianzpartitionierung 85                                                  |
| Ergebnisdarstellung: partielle Regressionen und 3-D-Grafiken 86            |
| Information theoretician approach und multimodel inference 87              |
| Vergleich mit frequentist statistics 87                                    |
| Masse der Modellgüte: AIC, BIC, AICc, , Evidence ratios, Akaike weights 88 |
|                                                                            |

[Zusammenfassung 91](#page-102-0)

| Weiterführende Literatur 92                                      |
|------------------------------------------------------------------|
| Statistik 5 93                                                   |
| Lernziele 93                                                     |
| Von linearen Modellen zu GLMs 93                                 |
| Zwei Beispiele 93                                                |
| Die Idee der Generalized linear models (GLMs) 95                 |
| Die drei Komponenten eines GLM 95                                |
| Mögliche Verteilungen von Werten und von Varianzen 96            |
| Typen von GLMs 98                                                |
| Das Fitten und die Modellgüte von GLMs 99                        |
| Erklärte Varianz in GLMs 100                                     |
| Testen der Modellvoraussetzungen (Modellvalidierung) in GLMs 100 |
| Poisson-Regressionen für Zähldaten 101                           |
| Berechnung 101                                                   |
| Interpretation und Visualisierung der Ergebnisse 101             |
| Overdispersion als Problem 103                                   |
| Logistische Regressionen für Binärdaten 104                      |
| Prinzipielles Vorgehen 104                                       |
| Die Theorie dahinter 105                                         |
| Modelldiagnostik und Ergebnisse 105                              |
| Umsetzung in R 106                                               |
| Binomial-Regressionen für Proportionen 108                       |
| Beispiel und Umsetzung in R 108                                  |
| Zusammenfassung 111                                              |
| Weiterführende Literatur 111                                     |
| Statistik 6 113                                                  |
| Lernziele 113                                                    |
| Split-plot- und Repeated-measures-Designs 113                    |
| Die Idee 113                                                     |
| ANOVA mit Error-Term als Lösung für einfache Fälle 116           |

[Beispiel: Repeated measures 116](#page-127-1)

Welche Unterschiede bestehen zu einer normalen ANOVA? 117 Umsetzung in R und Interpretation der Ergebnisse 117 Linear mixed effect models (LMMs) allgemein 118 Die Idee 118 Random und fixed factors 118 Pseudo- $R^2$  120 Linear mixed effect models (LMMs) in der Praxis 120 Beispiel 1: Repeated measures-Design 120 Beispiel 2: Split plot-Design 121 Beispiel 3: LMM mit "random slope" und "random intercept" 125 Generalized linear mixed effect models (GLMMs) 127 Die Idee 127 Ein Beispiel und seine Umsetzung in R 127 Random vs. fixed factors 130 LMs, GLMs, LMMs und GLMMs im Rückblick und Überblick 131 Zusammenfassung 132 Weiterführende Literatur 132 Quelle des Beispiels 132 Statistik 7 133 Lernziele 133 Einführung in "multivariate" Methoden 133 Was ist mit "multivariat" gemeint? 133 Inferenzstatistik vs. deskriptive Statistik 134 Beispiele multivariater Datensätze 134 Ziele multivariat-deskriptiver Analysen 134 Zwei komplementäre Ansätze 135 Hauptkomponentenanalyse (PCA) – das Prinzip 135 PCA: Voraussetzungen und Anwendung 137

Beispiel in R: Umweltvariablen im Fluss Doubs 138

Beispiele von Anwendungen von PCAs 144

**Zusammenfassung 146** 

[Weiterführende Literatur 147](#page-159-1)

[Quellen der Beispiele 147](#page-159-2)

[Statistik 8 148](#page-160-0)

[Lernziele 148](#page-160-1)

[Clusteranalysen allgemein 148](#page-160-2)

*[k](#page-161-0)*[-means clustering: Theorie 149](#page-161-0)

[Beispiel in R: Fischvorkommen im Fluss Doubs 149](#page-161-1)

[Zusammenfassung 153](#page-165-0)

[Weiterführende Literatur 153](#page-165-1)

[Anhang I 154](#page-166-0)

[Anhang II 155](#page-166-1)

# <span id="page-5-0"></span>**Vorwort**

*Jürgen Dengler*

Ich bin Ökologe, kein Statistiker. Trotzdem (oder vielleicht gerade deswegen) wurde ich 2017, als ich am IUNR als Professor und Leiter der Forschungsgruppe Vegetationsökologie begann, gefragt, ob ich nicht den Statistikteil im "Research Methods"-Modul des neuen Masterstudiengangs "Umwelt und Natürliche Ressourcen" übernehmen würde. Ich habe zugesagt, obwohl ich mir der doppelten Herausforderung klar war: (1) als statistische Autodidakt Statistik zu lehren und (2) dies nicht nur für Ökolog:innen, sondern für angehende Umweltingenieur:innen im Allgemeinen zu tun, deren Interessen von Umweltbildung bis zu Umwelttechnologien reichen und die gleichermassen im naturwissenschaftlichen wie im sozialwissenschaftlichen Bereichen unterwegs sind.

Der Kurs hat sich über die Jahre weiterentwickelt, vor allem durch konstruktiv-kritisches Feedback der Studierenden. Während nur wenige der ehemaligen Teilnehmer:innen vermutlich von sich behaupten würden, im Modul zu begeisterten Statistikfans geworden zu sein, so konnte ich doch in nachfolgenden Mastermodulen (etwa der "Summer School Biodiversity Monitoring" oder bei Präsentationen von Masterarbeiten) feststellen, dass viele das Handwerkszeug sehr solide gelernt haben und souverän anwenden konnten. Manche konnten am Ende des Masterstudium durch stetiges «*Learning by doing*» in der offenen Plattform R sogar statistische Fähigkeiten vorweisen, die deutlich über das im Kurs selbst vermittelte hinausgehen. Acht halbe Kurstage sind sehr wenig, um auch nur die wichtigsten Grundlagen der Statistik zu lernen. Wenn ihr erfolgreich sein wollt, müsst ihr also aktiv mitmachen und mehr Quellen nutzen als nur unsere Inputs im Modul.

Ich hatte eigentlich nicht vor, ein Skript zum Kurs zu erstellen, obwohl das Studierende auch in den Vorjahren immer wieder gewünscht haben. Der Aufwand dafür schien mir zu gross. Dann kam Covid-19 und im Herbstsemester 2020 war alles anders. Wir haben entschieden das "Methodenmodul" aus epidemiologischen Gründen ohne physischen Kontakt mit euch durchzuführen. Ich hätte in dieser Situation wie andere Dozierende mit Screencasts arbeiten können, aber ohne die Möglichkeit, dabei auf eure Fragen direkt eingehen zu können, schien mir das wenig erfolgsversprechend. Auch den ganzen Vormittag lang einen Online-Kurs zu halten, schien mir für euch wie für uns Dozierende unzumutbar. Insofern habe ich mich nach Diskussionen mit den anderen Beteiligten entschieden, doch ein Skript zu erstellen. Die Idee war, dass die

Studierende es vorgängig zu den Kurstagen gelesen haben und wir dann in einem gemeinsamen Online-Raum auf Zoom, im Sinne eines «*inverted classroom*» die offenen Fragen diskutiert haben. Das hat sich so gut bewährt, dass wir dieses Prinzip auch nach Covid-19 beibehalten haben, nur dass wir uns jetzt für den *«inverted classroom»* wieder live im Kursraum treffen.

Das hier vorliegende Skript war ursprünglich eine Verschriftlichung der Vorlesungsfolien der ersten Jahre. Seither haben wir die Inhalte an statistische Bedürfnisse angepasst, d. h. Methoden in den Vordergrund gestellt, die über viele Disziplinen in den Umweltwissenschaften relevant sind, und die verwendeten R-packages den Weiterentwicklungen in R angepasst. Da wir im Zuge der Überarbeitungen auch grössere Themenblöcke gestrichen haben, die vor allem für die Ökolog:innen unter den Umweltwissenschaftler:innen relevant sind, gibt es jetzt ein Individual Specialisation Module (ISM) im Frühjahrssemester, in dem Weiterführende Methoden, die besonders in der Vertiefung «Biodiversity and Ecosystems» häufig gebraucht werden, bieten wir künftig als «Individual Specialization Module» (ISM) «Statistik-Vertiefung» an (siehe Anhang I).

Wichtig ist, dass dieses Skript nicht als alleiniges Lehrmaterial gedacht ist. Genauso wichtig sind die gemeinsamen Präsenz-Lektionen mit Diskussion des theoretischen Stoffes und der Vorführung (Demo) exemplarischer R-Codes sowie die Übungen und deren Besprechung. Ich empfehle euch auch, begleitend auch andere Quellen zu nutzen, insbesondere wenn einige von euch meine Erklärungen schwer verständlich finden sollten. Welche Form der Informationsbereitstellung jemand eingängig findet, ist individuell sehr verschieden. Da nahezu alle aus meiner Sicht empfehlenswerten aktuellen Statistikbücher auf Englisch sind, dieses Skript jedoch auf Deutsch, habe ich im Skript wichtige Fachtermini in beiden Sprachen angegeben (Englisch ist dann *kursiv*), um eine leichtere Verknüpfung zu schaffen.

Im Skript wird die Theorie beginnend mit den einfachsten statistischen Verfahren (die den Masterstudierenden schon geläufig sein sollten) sukzessive aufgebaut, wobei an geeigneten Stellen wichtige Grundsätze (z. B. Unabhängigkeit der Messwerte, Voraussetzungen für Tests etc.) erklärt werden, die für die Statistik insgesamt relevant sind. Die Theorie ist immer mit dem entsprechenden R-Code kombiniert, einschliesslich der Interpretation der textlichen und grafischen Ausgaben von R. Das Skript enthält nur Auszüge des zugrunde liegenden R-Codes, der ausführlicher im Unterricht (in der jeweils zweiten Lektion) vorgestellt und besprochen wird. Da es in diesem Kursteil um das Verständnis der Statistik geht, wurde kein grosser Aufwand auf das "Optimieren" des visuellen Outputs gelegt, welches den Code wesentlich verlängert und den Blick vom "Eigentlichen" abgelenkt hätte.

Wir hoffen, dass dieses Skript sich als nützlicher Begleiter in eurem Studium und danach erweist. Hinweise zu Fehlern und Verbesserungsvorschläge könnt ihr gerne jederzeit an [juergen.dengler@zhaw.ch](mailto:juergen.dengler@zhaw.ch) melden.

### <span id="page-6-0"></span>**Empfohlene weiterführende Literatur**

- Borcard, D., Gillet, F. & Legendre, P. 2018. *Numerical ecology with R*. 2nd ed. Springer, Cham, CH: 435 pp. •
- Crawley, M.J. 2013. *The R book*. 2nd ed. John Wiley & Sons, Chichester, UK: 1051 pp. •
- Crawley, M.J. 2015. *Statistics An introduction using R*. 2nd ed. John Wiley & Sons, Chichester, UK: 339 pp. •
- Leps, J. & Smilauer, P. 2020. *Biostatistics with R An introductory guide for field biologists*. Cambridge University Press, Cambridge, UK: 365 pp. •

- Logan, M. 2010. *Biostatistical design and analysis using R: a practical guide*. Wiley-Blackwell, Chichester, UK: 546 pp. •
- Quinn, G.P. & Keough, M.J. 2002. *Experimental design and data analysis for biologists*. Cambridge University Press, Cambridge, UK: 537 pp. •

# <span id="page-7-0"></span>**Statistik 1**

Grundlagen der Statistik

**In Statistik 1 lernen die Studierenden, was (Inferenz-) Statistik im Kern leistet und warum sie für wissenschaftliche Erkenntnis (in den meisten Disziplinen) unentbehrlich ist. Nach einer Wiederholung der Rolle von Hypothesen wird erläutert, wie Hypothesentests in der**  *frequentist***-Statistik umgesetzt werden, einschliesslich** *p***-Werten und Signifikanz-Levels. Die praktische Statistik beginnt mit den beiden einfachsten Fällen, dem Chi-Quadrat-Test für die Assoziation zwischen zwei kategorialen Variablen und dem -Test auf Unterschiede in Mittelwerten zwischen zwei Gruppen. Abschliessend beschäftigen wir uns damit, wie man Ergebnisse statistischer Analysen am besten in Abbildungen, Tabellen und Text darstellt.**

### <span id="page-7-1"></span>**Lernziele**

#### Ihr…

- versteht, was Statistik im Kern leistet und warum Statistik für wissenschaftliche Erkenntnis (in den meisten Disziplinen) unentbehrlich ist; •
- könnt Angaben zu p-Werten oder Signifikanzlevels kritisch würdigen; •
- wisst, wann man einen *t*-Test, einen Chi-Quadrat-Test oder einen Binomial-Test verwendet und wie man das praktisch in R durchführt; •
- versteht, dass die räumliche und zeitliche Anordnung von Beobachtungen bestimmt, welchen Test man verwenden kann; und •
- habt eine grundlegende Idee, worauf es beim Berichten statistischer Ergebnisse, insbesondere in Abbildungen ankommt. •

### <span id="page-7-2"></span>**Warum brauchen wir Statistik?**

### <span id="page-7-3"></span>**Ein Beispiel**

Ich möchte die grundlegende Notwendigkeit von Statistik mit einem fiktiven Beispiel visualisieren. Gehen wir von einer einfachen Frage aus dem Zierpflanzenbau aus:

*Unterscheiden sich zwei verschiedene Sorten (Cultivare) in der Blütengrösse?*

![](_page_8_Picture_0.jpeg)

![](_page_8_Picture_1.jpeg)

Um diese Frage zu beantworten, vermessen wir die Blüten der beiden abgebildeten Individuen:

- Individuum A: 20 cm<sup>2</sup> •
- Individuum B: 12 cm<sup>2</sup> •

Mithin wäre unsere naive Antwort auf die Eingangsfragen: **Ja, die Blüten von Sorte A sind grösser als jene von B**. Wir können sogar sagen, um wie viel grösser (8 cm<sup>2</sup> oder 67 %).

Nun haben Pflanzen (wie fast alle Objekte, mit denen wir uns beschäftigen, mit Ausnahme vielleicht von Elementarteilchen) eine gewisse Variabilität:

![](_page_9_Picture_0.jpeg)

Folglich ist es sinnvoller, für die Beantwortung der Frage jeweils mehrere Individuen zu vermessen. Wir greifen nun 10 Individuen jeder Sorte heraus und erzielen folgende Messergebnisse:

- Individuen A1-A10 [cm<sup>2</sup>]: 20; 19; 25; 10; 8; 15; 13; 18; 11; 14
- Individuen B1–B10 [cm<sup>2</sup>]: 12; 15; 16; 7; 8; 10; 12; 11; 13; 10

Wir erhalten für A einen Mittelwert von 15.3 cm<sup>2</sup> und für B einen Mittelwert von 11.4 cm<sup>2</sup> (was wir einfach in Excel ausrechnen können). **Wir schliessen daher, dass die Blüten von A im Mittel 3.9** cm<sup>2</sup> grösser sind als jene von B.

Wir könnten uns also zufrieden zurücklehnen und unserem Ergebnis, das wir mit etwas **deskriptiver Statistik** (Mittelwerte) erzielt haben, vertrauen. Wo liegt der Haken? Wir haben nicht alle existierenden Individuen der Sorten A und B vermessen (die "Grundgesamtheit"), sondern nur eine Stichprobe von jeweils 10 Individuen. Nun könnte es sein, dass KollegInnen von uns die gleiche Untersuchung mit jeweils anderen Stichproben von je 10 Individuen durchgeführt haben, etwa folgendermassen (mit ihren jeweiligen Schlussfolgerungen):

#### Mess-Serie 1:

- ° Individuen A1–A10 [cm<sup>2</sup>]: 20; 19; 25; 10; 8; 15; 13; 18; 11; 14
- ° Individuen B1-B10 [cm<sup>2</sup>]: 12; 15; 16; 7; 8; 10; 12; 11; 13; 10
- $^{\circ}$  Ergebnis: A = 15.3; B = 11.4; A B = 3.9 cm<sup>2</sup>  $\rightarrow$  **A ist grösser als B**

#### Mess-Serie 2:

° Individuen A1–A10 [cm<sup>2</sup>]: 12; 19; 17; 10; 8; 13; 11; 15; 11; 9

- ° Individuen B1-B10 [cm<sup>2</sup>]: 12; 15; 16; 7; 8; 10; 12; 11; 13; 10
- $^{\circ}$  Ergebnis: A = 12.5; B = 11.4; A B = 1.2 cm<sup>2</sup>  $\rightarrow$  **A ist (wenig) grösser als**

#### Mess-Serie 3:

- ° Individuen A1–A10 [cm<sup>2</sup>]: 20; 19; 25; 10; 8; 15; 13; 15; 11; 14
- ° Individuen B1-B10 [cm<sup>2</sup>]: 12; 15; 16; 7; 8; 10; 12; 11; 13; 10
- ° Ergebnis: A = 11.0; B = 11.0; A B = 0.0 cm<sup>2</sup> → A ist gleich gross wie B

#### Mess-Serie 4:

- ° Individuen A1–A10 [cm<sup>2</sup>]: 20; 19; 25; 10; 8; 15; 13; 18; 11; 14
- ° Individuen B1–B10 [cm<sup>2</sup>]: 12; 15; 16; 16; 14; 10; 12; 11; 13; 10
- $^{\circ}$  Ergebnis: A = 11.0; B = 12.9; A B = 1.9 cm<sup>2</sup>  $\rightarrow$  **A ist kleiner als B**

Wer hat nun Recht? Um das zu beantworten, benötigen wir die **schliessende Statistik** (Inferenzstatistik).

#### <span id="page-10-0"></span>**Fazit**

- In der Regel wollen wir nicht wissen, ob ein einzelnes Individuum der Sorte A sich von einem einzelnen Individuum der Sorte B unterscheidet.
- Meist interessiert uns, ob sich die Sorte A als solche von der Sorte B unterscheidet.
- Da es in der Regel nicht möglich ist, sämtliche existierenden Individuen beider Sorten (**Grundgesamtheiten**; engl. *populations*) zu vermessen, vermessen wir die Individuen in zwei **Stichproben** (engl. *samples*).
- Die Inferenzstatistik sagt uns dann, wie wahrscheinlich ein festgestellter Unterschied in den Mittelwerten der Stichproben einem tatsächlichen Unterschied in den Mittelwerten der Grundgesamtheiten entspricht.

### <span id="page-10-1"></span>Warum mit R?

Zugegeben: wir haben euch nicht gefragt...

![](_page_11_Picture_0.jpeg)

### <span id="page-11-0"></span>**Was spricht dagegen?**

Auf den ersten Blick mag aus eurer Sicht ja einiges dagegensprechen

- **keine GUI** (grafische Benutzeroberfläche) zum Klicken •
- auf Englisch •
- **schwerer** zu erlernen •

### <span id="page-11-1"></span>**Was spricht dafür?**

- R ist **kostenlos & open source** (unabhängig von teuren Lizenzen) •
- R ist extrem **leistungsfähig** und immer **up-to-date** (da Tausende "ehrenamtlich" mitprogrammieren) •
- R ist nah an den **speziellen Bedürfnissen** der einzelnen Disziplinen (durch zahlreiche spezielle *Packages*) •
- R "zwingt" die Benutzenden dazu, ihr **statistisches Vorgehen zu durchdenken** (was zu besseren Ergebnissen führt) •
- R gewährleistet eine sehr **gute Dokumentation** des eigenen Vorgehens ("Reproduzierbarkeit"), da der geschriebene R Code anders als eine Klickabfolge in einem kommerziellen Statistikprogramm mit GUI eingesehen und erneut durchgeführt werden kann •
- R ist effizient, da man Code, den man einmal entwickelt hat, **immer wieder verwenden bzw. für neue Projekte anpassen** kann •
- Für R gibt es **umfangreiche Hilfe im Internet** (googlen, spezielle Foren,…) •

### <span id="page-11-2"></span>**Fazit**

Der Kursleiter (J.D.) hat Statistik nicht in seinem Studium gelernt und es sich später im Laufe seiner Forscherlaufbahn mühsam sich selbst beigebracht. Damals gab es noch kein R. Dafür gab es teure kommerzielle Statistikprogramme wie SPSS und STATISTICA, durch die man sich mit einer grafischen Benutzeroberfläche durchklicken konnte und am Ende ein Ergebnis bekam. Nicht immer war ganz klar, was das Programm da gerechnet hatte, aber immerhin bekam man mit relativ wenigen Klicks ein numerisches Ergebnis oder eine Abbildung (oft allerdings in bescheidenem

Layout) heraus. Häufig musste man aber erleben, dass das gewünschte statistische Verfahren im jeweiligen Programm in der gewünschten Version nicht implementiert war oder ein teures Zusatzpaket nötig gewesen wäre, das die eigene Universität nicht erworben hatte. Und wenn man dann an eine andere Universität wechselte, musste man oft feststellen, dass dort ein anderes Statistikprogramm erworben und genutzt wurde, für das man viele Dinge umlernen musste. Ganz zu schweigen von Zeiten ausserhalb einer Hochschule, wenn man keinen Zugriff auf ein kommerzielles Statistikprogramm hatte.

Aus dieser Sicht könnt ihr euch also glücklich schätzen, dass es heute R gibt und so leistungsfähig ist wie nie zuvor und auch dass das IUNR in der Ausbildung im Bachelor- und Masterlevel konsequent auf R setzt. Während es auf den ersten Blick vielleicht schwieriger erscheinen mag als die Benutzung von SPSS oder STATISTICA, bin ich überzeugt, dass ein Statistikkurs mit R euch bei gleichem Aufwand ein anderes Verständnislevel für Statistik ermöglichen wird als es Statistikkurse zu meiner Studienzeit taten. Nebenher bekommt ihr noch ein implizites Verständnis wie Algorithmen funktionieren, auch nicht ganz unwichtig in einer zunehmend digitalen Welt.

## <span id="page-12-0"></span>**Die Rolle von Hypothesen in der Wissenschaft**

### <span id="page-12-1"></span>**Rekapitulation**

Im Methodenmodul und sicher auch in euren vorausgehenden Studiengängen habt ihr euch bereits mit Hypothesen beschäftigt. Daher beginnen wir mit einem Arbeitsauftrag (allein oder im Austausch mit KommilitonInnen):

#### **Arbeitsauftrag**

Formuliert jeweils in einem Satz die folgenden Punkte:

- Eine beispielhafte Aussage, die den Ansprüchen an eine Hypothese genügt •
- Eine beispielhafte Aussage, die keine Hypothese ist •

### <span id="page-12-2"></span>**Was ist eine Hypothese?**

Es gibt in der Literatur wie fast immer in der Wissenschaft verschiedene Formulierungen. Ich schlage die folgende vor:

Eine Hypothese ist eine aus einer allgemeinen Theorie abgeleitete Vorhersage für eine spezifische Situation.

Leider wird der Begriff "Hypothese" heutzutage in der Wissenschaft "inflationär" und aus meiner Sicht sogar häufig falsch verwendet.

Zweifelhaft sind "ad hoc"-Hypothesen auf der Basis einer Vorabuntersuchung bzw. eines "Bauchgefühls", aber ohne eine Erklärung des für das vorhergesagte Ergebnis verantwortlichen Mechanismus (also letztlich ohne Theorie dahinter). Wissenschaftstheoretisch sollte man nie dieselben Daten zum Aufstellen und zum Testen einer Hypothese verwenden!

Gänzlich falsch sind angebliche "Hypothesen", die nachträglich aus den schon erzielten Ergebnissen abgeleitet werden.

Warum findet man in der wissenschaftlichen Literatur wie auch in studentischen Arbeiten so viele "Hypothesen", die wissenschaftstheoretisch dem Konzept einer Hypothese nicht gerecht werden? Der Grund dürfte darin liegen, dass viele von der Annahme geleitet werden, dass nur eine hypothesentestende Forschung eine gute/richtige Forschung ist. Tatsächlich ist aber hypothesengenierende Forschung genauso wichtig und richtig wie hypothesentestende Forschung. Es gilt also:

Wenn das Vorwissen nicht für eine **plausibel begründete Hypothese** ausreicht (**hypothesentestende Forschung**), formuliert man das Forschungsthema korrekterweise besser als **offene Frage** (**hypothesengenerierende Forschung**).

Dabei können offene Fragen meist mit (fast) den gleichen statistischen Verfahren adressiert werden wie Hypothesen. Allerdings sollten Hypothesen konkret sein, also nicht "A unterscheidet sich von B", sondern entweder "A ist grösser als B" oder "A ist kleiner als B". Hier würde also im Fall einer Hypothese ein einseitiger Test, im Fall einer offenen Frage ein zweiseitiger Test zur Anwendung kommen. Dazu aber später mehr.

### <span id="page-13-0"></span>**Wissenschaftliches Arbeiten (***in a nutshell***)**

Wenn wir modernes wissenschaftliches Arbeiten knapp visualisieren, ergibt sich folgendes Bild:

![](_page_13_Figure_6.jpeg)

![](_page_13_Picture_8.jpeg)

Bei den ersten Schritten von den Beobachtungen bis zur Spekulation über die Musterursachen handelt es sich um hypothesengenerierende Forschung. Erst wenn man regelmässig, ähnliche Befunde hat, macht das Formulieren einer echten Hypothese Sinn, die nicht nur das gefundene Muster vorhersagt, sondern auch einen Mechanismus bereithält, der erklärt, wie es zustande gekommen ist. Eine solche Hypothese kann dann in einer neuen Untersuchung (mit neuen Daten!) getestet werden, die spezifisch darauf ausgelegt ist, alternative Erklärungsmöglichkeiten auszuschliessen ("Experiment"). Hypothesengenierende und hypothesentestende Forschung sind im modernen Forschungsablauf also beide gleichermassen nötig, aber in der Regel getrennt voneinander.

In einer Forschungsarbeit, die für das Testen einer zuvor in anderen Arbeiten erarbeiteten Hypothese, entwickelt wurde ("Experiment"), kann das Ergebnis entweder eine Bestätigung oder eine Falsifizierung sein. Wichtig ist, dass eine einmalige Bestätigung keine Verifizierung einer Hypothese ist, während eine einmalige Falsifizierung zur Widerlegung genügt. **Eine Verifizierung einer Hypothese in einem absoluten Sinn ist grundsätzlich nicht möglich, absolute Wahrheit gibt es in der Wissenschaft nicht!** Wenn man jedoch eine Hypothese mit immer neuen "Experimenten" unter immer neuen Rahmenbedingungen "herausfordert" und sie dabei nie falsifiziert wird, dann wird aus einer **einfachen Hypothese** zunehmend **gesichertes Wissen**. Wenn man dagegen eine Hypothese widerlegt hat, muss man zurückgehen. Die vorgeschlagene Erklärung für das gefundene Muster oder sogar das Muster an sich hat sich als nicht korrekt/nicht allgemeingültig herausgestellt. Man muss sich also einen anderen Mechanismus/eine andere Hypothese ausdenken und diese erneut testen. Dies geschieht dann nicht in derselben, sondern in einer folgenden wissenschaftlichen Arbeit.

Mit diesem Wissen über den Ablauf von wissenschaftlicher Erkenntnis und der Rolle des Hypothesentestens dabei habe ich noch eine Frage, zu der ihr euch bis zum Kurstag Gedanken machen solltet:

#### **Frage**

Profitiert Wissenschaft mehr von der Bestätigung oder von der Falsifizierung von Hypothesen? (Bitte begründet eure Antwort!)

# <span id="page-14-0"></span>**Die Rolle der Statistik beim Hypothesengenerieren und -testen**

Wir haben gesehen, dass Hypothesen zentral für die moderne Wissenschaft sind, sowohl ihr Generieren als auch ihr Test. Doch welche Rolle spielt die Statistik dabei?

Statistische Verfahren, die implizit oder explizit Hypothesen testen, bezeichnet man als **Inferenzstatistik (schliessende Statistik)** – im Gegensatz zur **deskriptiven Statistik**.

### <span id="page-14-1"></span>**Von der Hypothese zur Nullhypothese…**

Die Herausforderung ist nun aber, wie oben gesehen, dass man eine **Hypothese (H<sup>a</sup> )** (auch **Forschungshypothese** oder *a***lternative Hypothese** genannt) nicht verifizieren kann, sondern nur falsifizieren. In der Statistik behilft man sich daher mit einem Trick, der sogenannten **Nullhypothese (H<sup>0</sup> )**. Die Nullhypothese ist die Negation der Hypothese, d. h. die Summe aller möglichen Beobachtungen, die mit der Hypothese nicht im Einklang sind. Wenn man nun die Nullhypothese falsifiziert, kann man indirekt die Hypothese bestätigen.

In unserem Beispiel von oben:

- Hypothese  $(H_{\Delta})$ : Sorte A und Sorte B unterscheiden sich in ihrer Blütengrösse
- Nullhypothese ( $H_{A0}$ ): Sorte A und Sorte B haben die gleiche Blütengrösse

Das ist formal korrekt, wissenschaftlich ist die Forschungshypothese aber wenig überzeugend, weil schwerlich ein Mechanismus vorstellbar ist, der in Sorte B sowohl kleinere als auch grössere, nur keine gleich grossen Blüten hervorbringt. Insofern wäre das folgende Paar sinnvoller:

- Hypothese (H<sub>R</sub>): Sorte A hat grössere Blüten als Sorte B
- Nullhypothese ( $H_{B0}$ ): Sorte A hat kleinere oder gleich grosse Blüten wie Sorte B

Die erste Forschungshypothese ( $H_A$ ) ist eine ungerichtete Hypothese und entspricht dem, was man in hypothesengenerierender Forschung implizit macht (wenn man also offene Fragen, aber keine konkreten Hypothesen hat). In diesem Fall wäre die zugehörige Forschungsfrage: "Unterscheiden sich die Sorten A und B in ihren Blütengrössen?". Die zweite Forschungshypothese ( $H_B$ ) ist dagegen gerichtet und wäre für hypothesentestenden Forschung adäquat. In der hypothesentestenden Forschung sollten wir auch eine Begründung/einen Mechanismus anführen, der vermutlich zu dem vorhergesagten Ergebnis führt, etwa dass die Sorte A polyploid ist. Dies gehört zur Begründung der Forschungshypothese, aber ist nicht Bestandteil der Forschungshypothese.

### <span id="page-15-0"></span>Einschub: Wichtige Termini in der Statistik

Bis hierher sind uns schon einige wichtige statistische Begriffe (wie Stichprobe und Grundgesamtheit) begegnet, deshalb sollen sie hier samt ihren englischen Pendants noch einmal rekapituliert werden:

| Deutscher Begriff | Englischer<br>Begriff | Definition                                                                    | Beispiel(e)                               |
|-------------------|-----------------------|-------------------------------------------------------------------------------|-------------------------------------------|
| Beobachtung       | Observation           | experimentelle bzw.<br>Beobachtungseinheit                                    | Pflanzenindividuum                        |
| Stichprobe        | Sample                | alle beprobten Einheiten                                                      | die 20 untersuchten<br>Pflanzenindividuen |
| Grundgesamtheit   | Population            | Gesamtheit aller Einheiten, über<br>die eine Aussage getroffen<br>werden soll | alle Individuen der<br>beiden Sorten      |

| Deutscher Begriff | Englischer<br>Begriff | Definition                             | Beispiel(e)                       |
|-------------------|-----------------------|----------------------------------------|-----------------------------------|
| Messung           | Measurement           | einzelne erhobene Information          | Blütengrösse eines<br>Individuums |
| Variable          | Variable              | Kategorie der erhobenen<br>Information | Blütengrösse, Sorte               |

Der englische Begriff *population* führt oft zu Verwirrung, da er in der Statistik etwas anderes meint als in der Biologie. *Population* ist schlicht die Grundgesamtheit, die in seltenen Fällen einer biologischen Population entspricht, in den meisten Fällen aber nicht (etwa *population of chairs*). Auch Messung/*measurement* wird in der Statistik weiter als in der Allgemeinsprache verwendet, d. h. auch für Zählungen oder Erhebung von kategorialen Variablen.

### <span id="page-16-0"></span>**Einschub: Parameter vs. Prüfgrössen**

Wenn wir in Inferenzstatistik betreiben, also von einer Stichprobe auf die Grundgesamtheit schliessen wollen, müssen wir zudem zwischen Parametern und Prüfgrössen unterscheiden. Unter Parameter (*parameter*) wird eine Grösse der deskriptiven Statistik für eine bestimmte Variable in der Grundgesamtheit verstanden, über die wir eine Aussage treffen wollen, die wir aber nicht kennen. Dagegen ist eine Prüfgrösse (*statistic*) eine aus den Messungen der Variablen in der Stichprobe berechnete Grösse, die zur Schätzung des Parameters dient. Etwas verwirrend ist, dass *stastitic* (Prüfgrösse) und *statistics* (die Statistik als Fach) fast gleich lauten. Oft wird die Konvention verwendet, dass die Prüfgrössen mit kursiven lateinischen Buchstaben (z. B. ) und die korrespondierenden Parameter mit den äquivalenten griechischen Buchstaben (z. B. ) bezeichnet werden (siehe [Abbildung 1.2](#page-17-1)).

| Parameter                                        | Statistic      | Formula                                                                                             |
|--------------------------------------------------|----------------|-----------------------------------------------------------------------------------------------------|
| Mean (µ)                                         | ÿ              | $\frac{\sum_{i=1}^{n} y_i}{n}$                                                                      |
| Median                                           | Sample median  | $y_{(n+1)/2}$ if $n$ odd                                                                            |
| Variance $(\sigma^2)$                            | s <sup>2</sup> | $(y_{n/2} + y_{(n/2)+1})/2$ if $n$ even $\sum_{i=1}^{n} \frac{(y_i - \bar{y})^2}{n-1}$              |
| Standard deviation $(\sigma)$                    | S              | $\sqrt{\sum_{i=1}^{n} \frac{(y_i - \bar{y})^2}{n-1}}$                                               |
| Median absolute deviation (MAD)                  | Sample MAD     | $median[ y_i - median ]$                                                                            |
| Coefficient of variation (CV)                    | Sample CV      | $\frac{s}{\bar{y}} \times 100$                                                                      |
| Standard error of $\bar{y}$ $(\sigma_{\bar{y}})$ | S <sub>ÿ</sub> | $\frac{s}{\sqrt{n}}$                                                                                |
| 95% confidence interval for $\mu$                |                | $\bar{y} - t_{0.05(n-1)} \frac{s}{\sqrt{n}} \le \mu \le \bar{y} + t_{0.05(n-1)} \frac{s}{\sqrt{n}}$ |

<span id="page-17-1"></span>Abbildung 1.2

# <span id="page-17-0"></span>Statistische Implementierung des Hypothesentestens (am Beispiel des *t*-Tests)

Wie lässt sich das Hypothesentesten nun mathematisch und statistisch umsetzen. Wir bleiben bei unserer offenen Forschungsfrage "Unterscheiden sich die Sorten A und B in ihren Blütengrössen?", woraus sich die Forschungshypothese "Sorten A und B unterscheiden sich in ihren Blütengrössen" ergibt. Mit dem Mittelwert  $\mu$  der Variablen (Blütengrösse) in den jeweiligen Grundgesamtheiten (A und B) lassen sich Forschungshypothese und Nullhypothese mathematisch wie folgt formulieren:

- H<sub>a</sub>:
- **H**<sub>0</sub>: oder

Für die Überprüfung der H<sub>0</sub> gibt es eine Teststatistik (Prüfgrösse) den *t*-Wert, der wie folgt definiert ist

Da für die gilt , lässt sich das vereinfachen zu:

Die Prüfgrösse t ist also die Differenz der beiden Mittelwerte dividiert durch den Standardfehler der Differenz der beiden Mittelwerte. Wenn also die Differenz der Mittelwerte gross und/oder der Standardfehler dieser Differenz klein ist, so ist t weit von Null entfernt.

Was sagt uns der berechnete *t*-Wert nun? Um daraus etwas schlussfolgern zu können, müssen wir ihn mit der theoretischen *t*-Verteilung vergleichen. Für diese gilt:

- Sie ist symmetrisch, mit einem Maximum bei 0.
- Der genaue Kurvenverlauf variiert in Abhängigkeit von den Freiheitsgraden (*degrees of freedom* = df). Bei vielen Freiheitsgraden, d. h. einer grossen Stichprobengrösse (mehr dazu, wie sich die Stichprobenzahl in Freiheitsgrade übersetzt, folgt später), nähert sicht die *t*-Verteilung einer Normalverteilung (auch *z*-Verteilung genannt).

Die allgemeine Konvention in der Statistik ist, dass die Nullhypothese dann verworfen wird, wenn die berechnete Prüfgrösse extremer ist als 95 % aller möglichen Werte bei der gegebenen Stichprobengrösse. Beim t-Test fragt man also, ob der berechnete t-Wert extremer ist als 95 % aller t-Werte der der Stichprobengrösse entsprechenden t-Verteilung. Da unsere Hypothese ungerichtet ist (also ist verschieden und nicht ist grösser/ist kleiner), benötigen wir einen zweiseitigen t-Test. Dieser bestimmt die "kritischen" t-Werte ( $t_c$ ), indem auf beiden Seiten quasi 2.5 % der Fläche des Integrals unter der Wahrscheinlichkeitsverteilung abgeschnitten werden, wie die Abbildung 1.3

![](_page_18_Figure_4.jpeg)

<span id="page-18-1"></span>Wenn also der berechnete t-Wert >  $t_c$  (oder <  $-t_c$ ) ist, dann sind wir **hinreichend sicher**, dass sich die Mittelwerte nicht nur in der Stichprobe, sondern auch in der Grundgesamtheit unterscheiden.

### <span id="page-18-0"></span>Fehler I. und II. Art

veranschaulicht:

Wichtig ist, dass es in der physischen Realität nie eine absolute Sicherheit gibt. Wenn wir also wir feststellen, dass die Wahrscheinlichkeit, dass die Nullhypothese zutrifft (oder präziser: dass das vorliegende Ergebnis oder ein extremeres bei Zutreffen der Nullhypothese aufgetreten wäre) kleiner als 5 % ist, gibt es eben doch Fälle gibt, in denen wir fälschlich die Nullhypothese verwerfen, d. h. das Vorliegend eines Effektes bejahen, obwohl er in der Realität (d. h. der Grundgesamtheit) nicht auftritt. Das bezeichnet man als **Typ I-Fehler**. Umgekehrt kann es aber auch passieren, dass man die Nullhypothese aufgrund des statistischen Tests beibehält, also einen Effekt nicht nachweist, obwohl er in der Realität existiert (**Typ II-Fehler**). Diese beiden Phänomene sind in der folgenden beiden Abbildungen visualisiert:

|                                                        |                           | Statistische Sc                                                | hlussfolgerung                                                                  |
|--------------------------------------------------------|---------------------------|----------------------------------------------------------------|---------------------------------------------------------------------------------|
|                                                        |                           | H0 wird verworfen                                              | H0 wird beibehalten                                                             |
| <b>der Realität</b><br>Idgesamtheit)                   | Effekt existiert          | Korrekte Entscheidung:<br>Effekt vorhanden und<br>nachgewiesen | Typ II-Fehler:<br>Effekt nicht nachgewiesen,<br>obwohl vorhanden                |
| Situation in der Realität<br>(d.h. der Grundgesamtheit | Effekt existiert<br>nicht | Typ I-Fehler:<br>Effekt nachgewiesen, aber<br>nicht vorhanden  | Korrekte Entscheidung:<br>Effekt nicht vorhanden und<br>auch nicht nachgewiesen |
| P(t)                                                   | Region wh                 | nere H <sub>0</sub> retained Region                            | where H₀ rejected                                                               |

Wie man der zweiten Visualisierung entnehmen kann, steigt die Wahrscheinlichkeit eines Typ II-Fehlers, je weiter man die akzeptierte Wahrscheinlichkeit eines Typ I-Fehlers reduziert. In der Statistik wir im Allgemeinen sehr viel stärker auf die Minimierung von Typ I-Fehlern fokussiert, d. h. man will vermeiden, dass man fälschlich einen Effekt behauptet, der in Realität nicht existiert, während es als weniger problematisch angesehen wird, einen vorhandenen, aber dann sehr schwachen Effekt, nicht nachgewiesen zu haben.

(aus Quinn & Keough 2002)

### <span id="page-20-0"></span>*p***-Werte und Signifikanzniveaus**

Signifikanzniveaus und p-Werte sind zentrale Termini in der am weitesten verbreiteten inferenzstatistischen Schule, der *frequentist statistics* ("Frequentistische Statistik", aber ich habe den Begriff noch nie im Deutschen gehört). Deren Grundideen sind:

- Die beobachteten Werte werden als eine Beobachtung unter vielen möglichen Beobachtungen interpretiert, die zusammen eine **Häufigkeitsverteilung** ergeben. •
- Es wird eine **einzige wahre Beschreibung der Realität** angenommen, der man sich mit bestimmten Irrtumswahrscheinlichkeiten annähern kann. •

In der *frequentist statistics*, sind die *p*-Werte das zentrale "Gütemass". Als *p***-Wert** bezeichnet man dabei die berechnete **Wahrscheinlichkeit eines Typ I-Fehlers**. Der *p*-Wert bezeichnet also die Wahrscheinlichkeit, dass man aufgrund des statistischen Tests einen Zusammenhang feststellt, ohne dass dieser in Realität existiert.

Als **statistisch signifikant** bezeichnet man Ergebnisse, die unter einem bestimmten *p*-Wert liegen. Diese Schwellenwerte sind Konventionen und nicht "gottgegeben". Traditionell werden drei Signifikanzniveaus verwendet (wozu R noch ein viertes hinzugefügt hat, das man mit "marginal signifikant" bezeichnen könnte), die wie folgt notiert werden:

| *** | p < 0.001 | höchst signifikant; highly significant       |
|-----|-----------|----------------------------------------------|
| **  | p < 0.01  | hoch signifikant; very significant           |
| *   | p < 0.05  | signifikant; significant                     |
|     | p < 0.1   | marginal signifikant; marginally significant |

Die Schwellenwerte der Signifikanzniveaus (d. h. Schwellenwerte für akzeptierte Typ I-Fehler) werden auch mit α bezeichnet. Was man in einer Arbeit als signifikant betrachtet, sollte man vor Beginn der Untersuchung festlegen und im Methodenteil schreiben ("als Signifikanzschwelle verwenden wir " oder "als signifikant sehen wir Ergebnisse mit an"). Es bietet sich normalerweise an, bei der allgemeinen Konvention von zu bleiben, es sei denn es sprechen spezifische Gründe dagegen. Ein Grund könnte sein, dass die Verwerfung der Nullhypothese/Annahme der Forschunshypothese schwerwiegende Folgen hätte und man sich daher besonders sicher sein will.

Da sich ober- und unterhalb der genannten Schwellen nichts Fundamentales ändert, sollte man grundsätzlich die exakten *p*-Werte mit drei Nachkommastellen (z. B. "" bzw. wenn noch niedriger als "") angeben. Zur besseren Lesbarkeit können zusätzlich die korrespondierenden Signifikanzniveaus angegeben werden.

Es ist wichtig, sich bewusst zu sein, dass **statistisch signifikant nicht gleichbedeutend ist mit biologisch bzw. sozialwissenschaftlich bedeutsam**. Ein Effekt kann statistisch hoch signifikant sein (wg. grosser Stichprobengrösse) und trotzdem inhaltlich bedeutungslos (da die Effektgrösse minimal ist). Umgekehrt kann ein inhaltlich bedeutsamer Effekt evtl. nicht statistisch signifikant nachgewiesen werden, wenn man extrem wenige Replikate hatte.

Mit dem Kriterium "statistische Signifikanz"/*p*-Wert trennen wir unsere Ergebnisse in einem ersten Schritt in jene, die wir für **belastbar** halten und jene, die mit grosser Wahrscheinlichkeit "zufällig" ("Rauschen in den Daten", Messungenauigkeit, etc.) zustande gekommen sind. Bei den belastbaren müssen wir dann immer noch ihre **Relevanz** (also die Effektstärke) beurteilen.

# <span id="page-21-0"></span>*t***-Test (für eine metrische Variable im Vergleich von zwei Gruppen)**

Dear *t*-Test ist eines der einfachsten inferenzstatistischen Verfahren Er vergleicht zwei Gruppen statistisch, wenn die abhängige Variable metrisch ist.

**Sorte Andro Sorte Bullie**

| 20 | 12 |
|----|----|
| 19 | 15 |
| 25 | 16 |
| 10 | 7  |
| 8  | 8  |
| 15 | 10 |
| 13 | 12 |
| 28 | 11 |
| 11 | 13 |

Sorte Andro Sorte Bullie

| 14 | 10 |
|----|----|
|    |    |

 $\rm H_{\hbox{\scriptsize 0}}$ : Die beiden Sorten unterscheiden sich nicht in der Blütengrösse.

#### <span id="page-22-0"></span>Students und Welch t-Test

Als statistisches Verfahren kommt **Students** *t*-**Test für zwei unabhängige Stichproben** zum Einsatz ("Student" ist das Pseudonym für William Sealy Gosset, dem Erfinder des Tests, dessen Arbeitsvertrag in der Privatwirtschaft das Publizieren von Ergebnissen verbot).

Wobei der gepoolten Varianz entspricht:

Der berechnete t-Wert wird mit der t-Verteilung für  $(n_1 - 1) + (n_2 - 1)$  Freiheitsgraden verglichen. Der klassische t-Test setzt Normalverteilung und gleiche Varianzen voraus:

t.test(size ~ cultivar, var.equal = T, data = blume)

Wenn Varianzgleichheit nicht gegeben ist, verwendet man Welch' *t*-Test. Dieser approximiert die Freiheitsgrade mit der Welch-Satterthwaite-Gleichung. Er setzt weiterhin Normalverteilung voraus, benötigt aber keine gleichen Varianzen. Welch' *t*-Test kann/sollte also immer verwendet werden, wenn keine vorherigen Tests auf Varianzgleichheit durchgeführt werden und ist daher Standard (default) in R:

Wobei

```
t.test(size ~ cultivar, var.equal = FALSE, data = blume)
t.test(size ~ cultivar, data = blume)
```

### <span id="page-22-1"></span>Ein- und zweiseitiger t-Test

Bislang war unsere Hypothese, dass irgendein Unterschied vorliegt (was, wie oben dargelegt, keine adäquate Forschungshypothese ist, sondern die implizite Hypothese, wenn man eine offene Frage formuliert, aber keine klare Theorie hat). Wenn es eine Theorie gibt, aus der sich eine klare Vorhersage treffen lässt, so enthält diese normalerweise auch eine Aussage über die Richtung des Effekts, also ob die Blüten von Andro grösser als jene von Bulliesind oder umgekehrt. Dann verwendet man einen einseitigen t-Test, denn man je nach Richtung der Hypothese mit greater oder less spezifizieren muss. Bildlich gesprochen werden beim gängigen Signifikanzniveau von  $\alpha = 0.05$  beim beidseitigen t-Test je 2.5 % der Integralfläche links und rechts "abgeschnitten", beim einseitigen t-Test dagegen 5 % auf einer Seite. Wenn der berechnete t-Wert in einem der abgeschnittenen "Dreiecke" liegt, ist das Ergebnis signifikant.

![](_page_23_Figure_0.jpeg)

![](_page_23_Figure_1.jpeg)

(aus Quinn & Keough 2002)

t.test(size ~ cultivar, data = blume) # zweiseitig

t.test(size ~ cultivar, alternative = "greater", data = blume ) # einseitig

t.test(size ~ cultivar, alternative = "less", data = blume) # einseitig

### <span id="page-23-0"></span>**Gepaarter und ungepaarter** *t***-Test**

Bislang haben wir angenommen, dass die Individuen der beiden Sorten unabhängig voneinander jeweils zufällig ausgewählt wurden. Dann ist ein ungepaarter *t*-Test (*default*-Einstellung in R) richtig. Wenn jedoch je zwei Messwerte zusammengehören, etwa wenn je eine Pflanze der Sorten Andro und Bullie gemeinsam in einem Topf wuchs, so kommt ein gepaarter *t*-Test zur Anwendung. Da dieser mehr "Informationen" zur Verfügung hat, hat er mehr statistische "*power*", wird i. d. R. also zu stärker signifikanten Ergebnissen führen:

t.test(blume\$size[blume\$cultivar == "Andro"], blume\$size[blume\$cultivar == "Bullie"], paired = TRUE)

# <span id="page-23-1"></span>**Binomial-Test (für die Häufigkeitsverteilung einer binomialen Variablen)**

Der Binomial-Test testet, ob die Verteilung einer binären Variable von einer Zufallsverteilung abweicht. Eine binomiale (binäre) Variable ist eine, die zwei mögliche Zustände hat, etwa lebend/tot, männlich/weiblich oder besser/schlechter. Wenn das Ergebnis zufällig wäre, müssten in der Stichprobe beide Ausprägungen ungefähr gleich häufig vertreten sein. Folglich testet der Binomialtest, wie wahrscheinlich es ist, dass die vorgefundene Häufigkeitsverteilung in der

Stichprobe zustande gekommen wäre, wenn beide Zustände gleich häufig sind. Wenn diese Wahrscheinlichkeit < 0.05 ist, nimmt man in der Statistik gewöhnlich an, dass der Unterschied in der Stichprobe einem realen Unterschied in der Grundgesamtheit ist.

Betrachten wir den Frauenanteil im schweizerischen Nationalrat als Beispiel. Im Jahr 2019 waren 84 von 200 Mitgliedern weiblich (42%). Nehmen wir in guter Näherung an, dass im Stimmvolk das Geschlechterverhältnis 1:1 ist: Kann die Abweichung von 50 % unter den Mitgliedern noch durch Zufall erklärt werden oder deutet das auf eine "Bevorzugung" von Männern bei der Kandidat:innenaufstellung und im Wahlvorgang hin. Die Antwort liefert der Binomialtest, dem man die Zahl der "Erfolge" (weiblich: 84) und die Stichprobengrösse (200) übergeben muss:

binom.test(84, 200)

Exact binomial test

data: 84 and 200 number of successes = 84, number of trials = 200, p-value = 0.02813 alternative hypothesis: true probability of success is not equal to 0.5 95 percent confidence interval: 0.3507439 0.4916638 sample estimates: probability of success 0.42

Der Unterschied ist also signifikant (*p* < 0.05), wir können die Nullhypothese ("keine Bevorzugung von Männern") also verwerfen. Der Output sagt uns auch noch, dass ohne Bevorzugung / Benachteiligung eines Geschlechts der gegenwärtige Frauenanteil im Nationalrat nur zustande hätte kommen können, wenn der Frauenanteil im Stimmvolk zwischen 35 % und 49 % läge. Da dieser Bereich 50 % (also den der Nullhypothese entsprechenden Wert) nicht einschliesst, ist es logisch, dass diese verworfen wird. Der Test ist "symmetrisch": Wir können also statt der Anzahl der weiblichen Nationalratsmitglieder auch jene der männlichen eingeben und bekommen den gleichen *p*-Wert

binom.test(116, 200)

Exact binomial test

data: 116 and 200 number of successes = 116, number of trials = 200, p-value = 0.02813 alternative hypothesis: true probability of success is not equal to 0.5 95 percent confidence interval: 0.5083362 0.6492561 sample estimates: probability of success 0.58

Man kann den Binomial-Test auch als **Vorzeichen-Test** (*sign test*) verwenden. Der Code ist der gleiche, die Bedeutung aber eine etwas andere. Der Vorzeichen-Test wird verwendet, wenn man testen will, ob es eine gerichtete Veränderung einer Zielvariablen über die Zeit gegeben hat. Beispielsweise könnte man fragen, wie sich eine Art in einer Anzahl von Untersuchungsflächen zwischen Zeitpunkt A und Zeitpunkt B in ihrer Häufigkeit verändert hat:

Dann gibt es für jede Untersuchungsfläche vier Möglichkeiten:

1. Die Art kam zum Zeitpunkt A und B vor

- Die Art kam weder zum Zeitpunkt A noch zum Zeitpunkt B vor 2.
- Die Art kam zum Zeitpunkt A vor, ist aber zum Zeitpunkt B verschwunden 3.
- Die Art kam zum Zeitpunkt A nicht vor, trat aber zum Zeitpunkt B neu auf 4.

Um den Vorzeichen-Test anzuwenden, ignorieren wir die Fälle 1 und 2 (ohne Veränderung) und berücksichtigen nur die Fälle 3 und 4 (mit Veränderung). Angenommen es gäbe 10 Flächen mit negativer, und 2 mit positiver Entwicklung, dann lautet der R Code folgendermassen (die Grundgesamtheit sind hier die Flächen mit Veränderung, also 10 + 2 =12).

binom.test(10, 12)

# alternative notion binom.test(c(10, 2))

# <span id="page-25-0"></span>**Möglichkeiten, zwei Stichproben zu vergleichen, und Implikationen für das Samplingdesign**

Bislang haben wir verschiedene Verfahren angeschaut, die auf Unterschieden zwischen zwei Stichproben testen. Welcher dieser Tests Verwendung finden kann, hängt (a) von der raumzeitlichen Anordnung der Beobachtungen und (b) von der Residual-Verteilung der abhängigen Variablen ab. Das **Sampling oder Experimentaldesign** muss also immer passend zur geplanten Statistik und die verwendete Statistik passend zum Samplingdesign gewählt werden. Passen Samplingdesign und statistisches Verfahren nicht zusammen, liefert R falsche Ergebnisse, da das Programm ja nicht weiss, wie die Beobachtungen raum-zeitlich angeordnet waren.

Grundsätzlich müssen die Beobachtungen in der Stichprobe so räumlich-zeitlich verteilt werden, dass sie zufällig oder ggf. systematisch in demjenigen Raum verteilt sind, den sie repräsentieren sollen. Erhebungen nur in Zürich zu machen, dann aber eine Aussage für die ganze Schweiz treffen zu wollen, geht also nicht.

### <span id="page-25-1"></span>**Gepaarte vs. ungepaart Tests**

Wir haben den ungepaarten und den gepaarten *t*-Test kennen gelernt. Gepaart bedeutet im einfachsten Fall, dass an den gleichen Untersuchungsobjekten zu zwei Zeitpunkten eine abhängige Grösse erhoben wurde. Vielfach wird mit gepaarten Tests aber auch bei räumlicher Nähe gearbeitet. In der folgenden Abbildung ist das visualisiert für den Vergleich von zwei Sorten im Gewächshaus (die beiden Farben). Das könnten genauso Individuen einer Art in einem Naturschutzgebiet sein usw. Dargestellt sind vier mögliche Anordnungen (wobei aus statistischer Sicher eine Zufallsverteilung optimal wäre, aber meist eine systematische Verteilung ebenfalls ohne Verzerrungen (*bias*) angewandt werden kann und vielfach einfacher zu implementieren ist).

![](_page_26_Figure_0.jpeg)

Mögliche räumliche Verteilung von Objekten in einem Sampling- oder Experimentaldesign. Der schwarze Rahmen könnte das Gewächshaus sein und die roten und blauen Kreise die Töpfe der Versuchspflanzen der beiden Sorten. Die vier Anordnungen sind im Text erklärt.

**Anordnung a** ist statistisch korrekt für einen Vergleich der beiden Sorten, aber man macht dann keine Aussage über das ganze Gewächshaus, sondern nur über seine obere rechte Ecke. **Anordnung b** erlaubt dagegen keinen Vergleich zwischen den beiden Sorten, da die roten Töpfe alle links und die blauen Töpfe alle rechts stehen. Wenn man hier einen Unterschied zwischen rot und blau mit dem t-Test gefunden hat, könnte das in Wahrheit auch ein Unterschied zwischen der linken und rechten Seite des Gewächshauses sein. Der *t*-Test spuckt dann zwar eine *p*-Wert aus, aber der beantwortet nicht unsere Frage. Man nennt das **Pseudoreplikation**, da R glaubt, es hätte sechs rote und sechs blaue Pflanzen, die unabhängig voneinander sind (*n* = 12). De facto hat man aber nur ein rotes und ein blaues Cluster (*n* = 2). **Anordnung c** ist optimal für die Anwendung eines ungepaarten *t*-Tests (die Töpfe der beiden Sorten sind unabhängig voneinander zufällig im Gewächshaus verteilt). **Anordnung d** schliesslich ist gut für einen gepaarten t-Test, da die sechs Gruppen zufällig (oder hier: systematisch) im Gewächshaus verteilt wurden, und innerhalb jedes Paars die Sorte wiederum zufällig oder in einem Schachbrettmuster den beiden Töpfen zugewiesen wurde.

### <span id="page-26-0"></span>**Nutzung des Vorzeichentests bei gepaarten Erhebungen**

Wenn man den Binomial-Test als Vorzeichen-Test verwendet, kann dieser auch gut bei gepaarten Erhebungen (Anordnung d in der Abbildung oben) Anwendung finden. Dies gilt für zwei Fälle: (a) die Residuen sind so ungünstig, dass weder eine Transformation noch der Wilcoxon-Text hilft, (b) es

wird eine nicht messbare ordinale Grösse erhoben (z.B. Geschmack von Kulturpflanzen). Das Vorgehen ist dann jeweils so, dass für jedes Paar entschieden wird, ob Sorte A grösser/besser ist also Sorte B oder umgekehrt. Die Paare, bei denen man nicht unterscheiden kann, weil die Messwerte gleich oder die ordinale Grösse zu ähnlich ist, werden vor der Anwendung des Tests ausgeschlossen. Wären beide Sorten hinsichtlich der Zielgrösse gleich, müsste in 50% der Fälle Sorte A grösser/besser sein, und in 50% der Fälle Sorte B. Gibt es eine signifikante Abweichung von 50 zu 50 schliessen wir auf einen Unterschied.

# <span id="page-27-0"></span>**Chi-Quadrat- bzw. Fishers Test (für die Assoziation zweier binomialer Variablen)**

Die Frage beim Assoziationstest ist eine ähnliche wie beim Binomialtest. Wiederum geht es um binomiale Variablen, dieses Mal aber nicht um eine einzige, sondern um zwei an denselben Objekten erhobene Variablen, deren Zusammenhang man wissen will.

Im folgenden Beispiel wollen wir wissen, ob die Augenfarbe und die Haarfarbe von Personen miteinander zusammenhängen. Die einfachste Form des Assoziationstests setzt zwei binomiale/ binäre Variablen voraus, wir müssen also z. B. grüne Augen ausschliessen oder mit einer der beiden anderen Augenfarben zusammenfassen. Unsere Beobachtungsergebnisse von 114 Personen könnten wie folgt aussehen:

|              | Blaue Augen | Braune Augen |
|--------------|-------------|--------------|
| Helle Haare  | 38          | 11           |
| Dunkle Haare | 14          | 51           |

Sind diese Werte so erwartbar unter der Nullhypothese, dass Augenfarbe und Haarfarbe unabhängig voneinander sind? Anders als beim Binomialtest oben ist die Nullhypothese jedoch nicht die Gleichverteilung aller Merkmale bzw. Merkmalskombinationen. Vielmehr gehen wir von der gegebenen Häufigkeit der vier Einzelmerkmale aus. Wir müssen also berechnen, mit welcher Wahrscheinlichkeit die Kombination blaue Augen – helle Haare unter den 114 Probant:innen auftreten sollte, wenn beide Merkmale unabhängig voneinander sind. Das geht folgendermassen:

|              | Blaue Augen | Braune Augen | Zeilen Total |
|--------------|-------------|--------------|--------------|
| Helle Haare  |             |              | 49           |
| Dunkle Haare |             |              | 65           |
| Reihen Total | 52          | 62           | 114          |

|              | Blaue Augen | Braune Augen | Zeilen total |
|--------------|-------------|--------------|--------------|
| Helle Haare  | 22.35       | 26.65        | 49           |
| Dunkle Haare | 29.65       | 33.35        | 65           |
| Reihen Total | 52          | 62           | 114          |

Die beobachteten Werte (z. B. 38 Personen mit blauen Augen/hellen Haare) unterscheiden sich deutlich von den erwarteten Werten unter der Nullhypothese (22.35 Personen). Aber ist das auch statistisch signifikant?

### <span id="page-28-0"></span>**Chi-Quadrat-Test**

Der traditionelle statistische Test für diese Frage ist Pearsons Chi-Quadrat-Test (auch  $X^2$ -Test geschrieben). Wie t ist  $X^2$  eine Teststatistik, die abhängig von den Freiheitsgraden (df) einer ganz bestimmten Kurve folgt.

Wobei,

![](_page_29_Picture_0.jpeg)

(aus Quinn & Keough 2002)

Wir können den  $\chi^2$ -Wert in unserem Fall einfach händisch berechnen:

O E

| Helle Haare & blaue Augen   | 38 | 22.35 | 244.92 | 10.96 |
|-----------------------------|----|-------|--------|-------|
| Helle Haare & braune Augen  | 11 | 26.65 | 244.92 | 9.19  |
| Dunkle Haare & blaue Augen  | 14 | 29.65 | 244.92 | 8.26  |
| Dunkle Haare & braune Augen | 51 | 35.35 | 244.92 | 6.93  |

| X<br>2 | 35.33 |  |
|--------|-------|--|
|--------|-------|--|

Ist nun signifikant oder nicht? Dazu müssen wir noch die Freiheitsgrade berechnen und das Signifikanzniveau festlegen:

**Freiheitsgrade:** •

**Signifikanzlevel:** z. B. •

Traditionell hätte man den kritischen Wert für diese Kombination in einer gedruckten Tabelle nachgeschlagen. Wir fragen einfach R, wobei wir 1 – α (in unserem Fall 1-0.05) eingeben müssen, da wir wissen wollen, ob wir im äussersten rechten Teil der Verteilungskurve liegen, also extremer als 95 % der Werte unter der Nullhypothese keiner Assoziation.

qchisq(0.95, 1)

3.841495

Unser berechneter *Χ*²-Wert (35.33) ist viel grösser als der kritische Wert (3.84), also gibt es eine Assoziation zwischen den Variablen (d. h. die Kombinationen blau/hell und braun/dunkel sind überproportional häufig). Wenn wir, wie oben empfohlen, einen präzisen p-Wert für die Assoziation wollen, erhalten wir ihn folgendermassen (beachte, dass chisq.test eine Matrix oder ein data frame als Argument benötigt):

count <- matrix(c(38, 14, 11, 51), nrow = 2)

chisq.test(count)

Pearson's Chi-squared test with Yates' continuity correction

data: count

X-squared = 33.112, df = 1, p-value = 8.7e-09

Der ausgegebene *Χ*²-Wert (33.11) ist etwas niedriger als der oben händisch berechnete (35.33), da R noch die Yates-Korrektur anwendet, um zu kompensieren, dass wir es hier mit Ganzzahlen (diskreten Werten) zu tun haben, während die *Χ*²-Verteilung kontinuierliche Werte unterstellt. Die Assoziation bleibt aber trotzdem höchst signifikant (*p* < 0.001).

### <span id="page-30-0"></span>**Fishers exakter Test**

Für kleine Erwartungswerte in den Zellen (< 5) ist der Chi-Quadrat-Test nicht zuverlässig. Dafür gibt es Fishers exakten Test.

count2 <- matrix(c(3, 5, 9, 1), nrow = 2) fisher.test(count2)

Fisher's Exact Test for Count Data

data: count p-value = 0.04299

alternative hypothesis: true odds ratio is not equal to 1

95 percent confidence interval: 0.001280876 1.102291244 sample estimates: odds ratio 0.08026151

Man kann/sollte Fishers exakten Test jedoch grundsätzlich verwenden, da er mit der heutigen Rechenleistung von Computern kein Problem mehr darstellt. Angewandt auf unseren Haarfarben / Augenfarben-Datensatz ergibt sich:

count

[,1] [,2] [1,] 38 11 [2,] 14 51

fisher.test(count)

Fisher's Exact Test for Count Data

data: count p-value = 2.099e-09 alternative hypothesis: true odds ratio is not equal to 1 95 percent confidence interval: 4.746351 34.118920 sample estimates: odds ratio 12.22697

Wie man der Ausgabe entnehmen kann, ist die Teststatistik hier anstelle von *Χ*² die sogenannte *odds ratio*, ein Begriff, für den es keine gute deutsche Übersetzung gibt. Sie bezeichnet die **Wahrscheinlichkeit des Eintretens geteilt durch die Wahrscheinlichkeit des Nichteintretens**. Aus der Umgangssprache und Wettspielen sind wir bereits vertraut mit *odds ratios*: "50:50-Chancen" bezeichnen nichts anderes als eine *odds ratio* von 1 (50 / 50 = 1). Bei einem Assoziationstest ist entspricht der *odds rati*o die Multiplikation der Wahrscheinlichkeiten auf der einen Diagonalen geteilt durch jene der anderen Diagonalen, also (38 x 51) / (14 x 11).

# <span id="page-31-0"></span>**Wie berichtet man statistische Ergebnisse?**

### <span id="page-31-1"></span>**Welche relevanten Informationen benötige ich und wo finde ich sie?**

Die Ergebnisausgaben in R sind mitunter umfangreich. Da kommt es darauf an, effizient herausfiltern zu können, was welche Information darin bedeutet und welche davon man in einer wissenschaftlichen Arbeit braucht. Hier ist die Ausgabe des vorhergehenden gepaarten *t*-Tests, und was die jeweiligen Zeilen bedeuten:

```
data: blume$a and blume$b

t = 3.4821, df = 9, p-value = 0.006916
alternative hypothesis: true difference in means is not equal to 0

95 percent confidence interval:
1.366339 6.433661
sample estimates:
mean of the differences
3.9
```

Welche Informationen davon werden benötigt:

- 1. Name des Tests (Methode)
- 2. Signifikanz/p-Wert (Verlässlichkeit des Ergebnisses))
- 3. Effektgrösse und -richtung (unser eigentliches Ergebnis!)
- 4. ggf. Wert der Teststatistik und Freiheitsgrade ("Zwischenergebnisse")

Wichtig ist es, bei aller "Begeisterung" für die p-Werte nicht unser eigentliches Ergebnis zu vergessen, d. h. die Antwort auf die Frage ob die Blüten von A oder von B grösser sind und wenn ja wie stark (blau). Ob Freiheitsgrade und der Wert der Teststatistik angegeben werden müssen, darüber gehen die Geschmäcker auseinander. Wenn man die Daten korrekt in R eingegeben hat, spezifiziert R die Freiheitsgrade automatisch und bei gegebenen Freiheitsgraden ist die Beziehung von t zu p eindeutig. Deshalb genügt es m. E. p anzugeben. (Aber wenn der Betreuer oder die Editorin auch noch t und df haben wollen, dann sollte man sie parat haben). Ein adäquater Satz im Ergebnisteil, der den obigen R output zusammenfasst, lautet daher:

Die Blütengrösse unterschied sich hochsignifikant zwischen den beiden Sorten mit einem Mittelwert von 15.3 cm<sup>2</sup> für Sorte A und 11.4 cm<sup>2</sup> für Sorte B (gepaarter t-Test, p = 0.007, , FG = 9).

#### Oder auf Englisch:

Flower sizes differed very significantly between the two cultivars with a mean size of 15.3 cm<sup>2</sup> in cultivar A and 11.4 cm<sup>2</sup> in the cultivar B (paired t-test, p = 0.007, df = 9).

### <span id="page-32-0"></span>Text, Tabelle oder Abbildung?

Hier kommen ein paar wichtige Vorgaben und Empfehlungen:

- Jedes Ergebnis nur 1x ausführlich darstellen, entweder als Abbildung, in einer Tabelle oder als Text
- Wenn als Abbildung oder Tabelle, dann im Text mit einem zusammenfassenden Statement darauf verweisen, das nicht alle Details wiederholt
- Signifikante und nicht signifikante Ergebnisse berichten

- **Gängige Strategie:** •
  - **Abbildungen:** für die wichtigsten signifikanten Ergebnisse ◦
  - **Tabellen:** für die weiteren signifikanten Ergebnisse ◦
  - **Nur Text:** für die nicht signifikanten Ergebnisse ◦

### <span id="page-33-0"></span>**Abbildungen in wissenschaftlichen Arbeiten**

Zumindest für die wichtigsten signifikanten Ergebnisse produzieren wir normalerweise Abbildungen. Dabei ist es wichtig, die folgenden Prinzipien zu beherzigen:

- Abbildungen (und Tabellen) sollten **ohne den zugehörigen Text informativ** sein, d. h. normalerweise *p*-Werte in der Abbildung/Tabelle bzw. Unter-/ Überschrift angeben •
- **Achsen sind verständlich beschriftet** (ausgeschriebene Variablennamen mit Einheit) •
- **Keine Abbildungsüberschrift** (es gibt die Legende in der Abbildungsunterschrift) •
- Keine überflüssigen Elemente (z. B. Rahmen, farbiger Hintergrund, horizontale und vertikale Linien) •
- Klarer **Kontrast**, ausreichende **Linienstärke** und **Schriftgrösse.** •

### <span id="page-33-1"></span>**Abbildungen mit "base R" oder mit ggplot2?**

Im Folgenden visualisiert mit den Boxplots, die zum *t*-Test gehören.

In "base R" geht das folgendermassen:

boxplot(size~cultivar, data = blume)

![](_page_34_Figure_0.jpeg)

In ggplot2 geht es folgendermassen (mit *default*-Einstellungen):

library(ggplot2)

ggplot(blume, aes(cultivar, size)) + geom\_boxplot()

![](_page_35_Figure_0.jpeg)

Gut ist, dass die Achsen automatisch beschriftet wurden. Störend ist der graue Hintergrund (reduziert Kontrast) und die weissen Gitternetzlinien (überflüssig und dank des zu geringen Kontrasts eh kaum zu sehen).

Man kann das in ggplot2 durch Wahl des vordefinierten theme\_classic optimieren:

ggplot(blume, aes(cultivar, size)) + geom\_boxplot() + theme\_classic()

![](_page_36_Figure_0.jpeg)

Das Ergebnis ist insgesamt OK, allerdings sind die Linien zu fein und die Schrift zu klein – jeweils relativ zur Gesamtgrösse der Abbildung.

Man kann weiter optimieren durch Hinzufügen weiterer Steuerelemente (siehe [https://](https://researchmethods-zhaw.github.io/HS25/infovis/Infovis1_Demo.html#themes) [researchmethods-zhaw.github.io/HS25/infovis/Infovis1\\_Demo.html#themes\)](https://researchmethods-zhaw.github.io/HS25/infovis/Infovis1_Demo.html#themes):

```
mytheme <- 
theme_classic() + 
theme(axis.line = element_line(linewidth = 0.8, color = "black"), 
axis.text = element_text(size = 13, color = "black"), 
axis.title = element_text(size = 15, color = "black"), 
axis.ticks = element_line(linewidth = 0.8, color = "black"), 
axis.ticks.length = unit(0.2, "cm"),
axis.title.y = element_text(vjust = 2.5),
plot.margin = margin(t = 5.5, r = 5.5, b = 5.5, l = 7)
)ggplot(blume, aes(cultivar, size)) +
geom_boxplot(size = 1) +
```

```
labs(x = "Cultivar", y = "Size (cm)") +
mytheme
ggplot(blume, aes(cultivar, size)) + 
geom_boxplot() + 
mytheme
```

![](_page_37_Figure_1.jpeg)

Jetzt passt es… Einzig könnte man noch den *p*-Wert einblenden

Ob man die Grafiken mit ggplot2 oder base R gestaltet, sei jedem selbst überlassen. Beides hat Vorund Nachteile. Was man aber vermeiden sollte, sind die Ausgaben von ggplot2 mit default-Einstellungen, da diese gängigen Standards für gute Grafiken widerspechen. Hier noch einmal zusammengefasst die Vor- und Nachteile beider Systeme:

#### Base R:

- Einfache Syntax, daher geeignet für schnelles Plotten •
- ABER: Syntax variiert zwischen verschiedenen Plottbefehlen •
- ABER: "Finetunen" von Grafiken oftmals umständlich oder gar nicht möglich •
- Geeignet für Vektoren (ggplot2 braucht dataframes o.ä) •
- Geeignet für das Plotten von Modellen (plot(lm()) •
- Einfaches Plotten der Modelldiagnostik (plot(summary()) •

#### Vorteile ggplot2:

- Leistungsfähige, universelle Syntax, daher leicht anpassbar an den Bedarf, wenn man das Prinzip erst einmal verstanden hat •
- Viele Funktionen "out of the box" •
- Einfachere Gestaltungsmöglichkeit (Farbskalen usw.) •

### <span id="page-38-0"></span>**Inferenzstatistik vs. beschreibende Statistik**

In diesem Kapitel ging es um die Frage, wie Statistik beim Hypothesentesten helfen kann. Die statistischen Verfahren, die man dazu anwendet, nennt man **schliessende Statistik** oder **Inferenzstatistik.** Hier wird abgeschätzt, wie wahrscheinlich ein gefundener Effekt in unserer Stichprobe einem tatsächlichen Effekt in der Grundgesamtheit entspricht. Diese Form der Statistik ist in der modernen quantitativen Forschung zentral, egal in welcher Disziplin. Die schliessende Statistik macht daher den Hauptteil des Kurses aus, von Statistik 1 – Statistik 6.

Daneben ist aber auch die **beschreibende** oder **deskriptive Statistik** relevant. Hier geht um die Berechnung statistischer Kenngrössen wie Mittelwert, Median oder Standardabweichung oder die Visualisierung von Werteverteilungen, etwa mittels Boxplots. Wie ihre im Weiteren sehen werdet, wird fast jede inferenzstatistische Untersuchung mit einer deskriptiven Statistik begleitet, sei es in der Form der Angabe von Mittelwerten oder der Visualisierung mittels Boxplots. Daneben gibt es auch Datensätze, die so komplex sind, dass von vornherein das statistische Ziel eine Visualisierung und nicht das Testen von Hypothesen ist. Das betrifft insbesondere die deskriptiv-multivariaten Verfahren, die wir in Statistik 7 und 8 kennenlernen.

### <span id="page-39-0"></span>**Zusammenfassung**

- Wissenschaftliche Forschung zielt in der Regel entweder auf das **Generieren oder das Testen von Hypothesen**. •
- **Inferenzstatistik** ist das Set statistischer Verfahren (Tests), das sowohl für das Testen als auch das Generieren von Hypothesen) verwendet wird. •
- Inferenzstatistik ist notwendig, um zu bestimmen, **wie wahrscheinlich ein beobachtetes Muster durch angenommenen Einflussgrössen (Variablen)** und nicht durch (a) Messfehler oder (b) andere "Störgrössen" **hervorgerufen wurde**. •
- Der *p***-Wert ist die Wahrscheinlichkeit eines Typ I-Fehlers**, d. h. einen Effekt zu berichten, wo keiner ist; nach üblicher Konvention wird ein Effekt dann als hinreichend sicher (signifikant) angesehen, wenn *p* < 0.05. •
- Mit einem **Chi-Quadrat-Test** (oder besser mit Fishers exaktem Test) kann man auf eine **Assoziation zwischen zwei kategorialen Variablen** testen. •
- Mit einem *t***-Test kann man** auf **Unterschiede in den Mittelwerten einer metrischen Variablen** zwischen zwei Gruppen testen. •
- **Inferenzstatistik** dient dem Testen von Analysen, **deskriptive Statistik** dem Beschreiben und Visualisieren von Daten. •

# <span id="page-39-1"></span>**Weiterführende Literatur**

- **Crawley, M.J. 2015.** *Statistics An introduction using R***. 2nd ed. John Wiley & Sons, Chichester, UK: 339 pp.** •
  - **Chapter 1 Fundamentals** ◦
  - **Chapter 6 Two Samples** ◦
- Quinn, G.P. & Keough, M.J. 2002. *Experimental design and data analysis for biologists*. Cambridge University Press, Cambridge, UK: 537 pp. •

# <span id="page-39-2"></span>**Statistik 2**

Einführung in lineare Modelle, ein- und mehrfaktorielle Varianzanalysen (ANOVAs)

**In Statistik 2 lernen die Studierenden die Voraussetzungen und die praktische Anwendung "einfacher" linearer Modelle in R (sowie teilweise ihrer "nicht-parametrischen" bzw. "robusten" Äquivalente). Am Anfang steht die Varianzanalyse (ANOVA) als Verallgemeinerung des** *t***-Tests, einschliesslich post-hoc-Tests und mehrfaktorieller ANOVA. Dann geht es um die Voraussetzungen parametrischer (und nicht-parametrischer) Tests und Optionen, wenn diese verletzt sind.** 

# <span id="page-40-0"></span>**Lernziele**

#### Ihr…

- wisst, welche Voraussetzungen parametrische (und nicht-parametrische) Tests haben und welche Alternativen euch bei wesentlichen Verletzungen zur Verfügung stehen; •
- könnt eine ANOVA in R durchführen, versteht ihre Ergebnisse und könnt diese adäquat in Text und Abbildungen dokumentieren; und •
- versteht, was eine Interaktion in einer mehrfaktoriellen ANOVA ist. •

### <span id="page-40-1"></span>**Einfaktorielle Varianzanalyse (***One-Way* **ANOVA)**

### <span id="page-40-2"></span>**Die Idee dahinter**

Eine ANOVA (*Analysis of variance*) ist die Verallgemeinerung des *t*-Tests für mehr als zwei Gruppen (*Factor levels*). Auch hier wollen wir wissen, **ob/wie sich die Mittelwerte der abhängigen Variablen zwischen den Gruppen unterscheiden**. Varianzanalyse heisst das Verfahren, weil der statistische Test zur Beantwortung der Frage das **Verhältnis zweier Varianzen** testet. Was es mit den zwei Varianzen auf sich hat, ist im Folgenden erklärt.

Gehen wir zurück zu unserem Blumenbeispiel. Die Idee der ANOVA ist, dass die Mittelwerte der Blütengrössen der beiden Sorten dann verschieden sind, wenn die Summe der Abweichungen (Residuen) vom Gesamtmittelwert "signifikant" grösser ist als die Summe der Abweichungen von den Sortenmittelwerten. Das ist in der folgenden Abbildung veranschaulicht. Die Punkte stellen die 20 Messwerte der Blütengrössen dar, wobei sie in der rechten Teilabbildung nach Sorten gruppiert sind. Der Gesamtmittelwert links und die beiden Sortenmittelwerte rechts sind als horizontale Linien dargestellt. Die vertikalen Linien sind die Residuen, also die Abweichung der beobachteten von den durch das Modell vorhergesagten Werten. Zusammen ergeben sie den Anteil der Varianz, welcher durch das jeweilige statistische Modell nicht erklärt wird. Das Modell links nimmt an, dass die Blüten einheitlich gross sind, unabhängig von der Sorte, während das komplexere Modell rechts unterschiedliche Mittelwerte abhängig von der Sorte annimmt.

![](_page_41_Figure_0.jpeg)

Varianz ist ein Mass für die Streuung von Werten um ihren Mittelwert. Mathematisch wird die Varianz wie folgt berechnet:

(Summe der Abweichungsquadrate = Sum of squares = SS)

Abweichungsquadrate sind dabei die quadrierten Werte der grünen (bzw. schwarzen und roten) vertikalen Linien in der obigen Abbildung. Die Distanzen werden quadriert, so dass negative Abweichungen gleichermassen zählen. Würde man nur die unquadrierten Werte aufsummieren, wäre das Ergebnis immer 0, da die horizontale Linie (der Mittelwert) ja so gelegt wurde, dass die positiven und negativen Abweichungen betragsmässig gleich sind. Ein zentraler Punkt der Varianzanalyse ist, dass sich die Gesamtsumme der Abweichungsquadrate (*Total* s*um of squares*) als die Summe zweier Teile (SSE und SSA) darstellen lässt:

- SSY = *Total sum of squares* •
- SSE = *Error sum of squares* (entsprechend der unerklärten Varianz = Residuen) •
- SSA = *Sum of squares attributable to treatment* (hier: Sorte) •

### <span id="page-41-0"></span>**Praktische Durchführung**

Schauen wir das zunächst beim Blumen-Datensatz an.

head(blume)

cultivar size

1 a 20

```
2 a 19
3 a 25
4 a 10
[…]
11 b 8
12 b 12
13 b 9
```

Schauen wir uns zunächst noch einmal das Ergebnis als "normalen" t-Test an:

t.test(size~cultivar, var.equal = TRUE, data = blume)

Two Sample t-test

data: size by cultivar t = 2.0797, df = 18, p-value = 0.05212 alternative hypothesis: true difference in means between group a and group b is not equal to 0 95 percent confidence interval: -0.03981237 7.83981237 sample estimates: mean in group a mean in group b 15.3 11.4

Nun nehmen wir dieselben Daten und analysieren sie mit einer Varianzanalyse. Der Befehl dazu ist aov (was für *a*nalysis *o*f *v*ariance steht). Man kann sich die Ergebnisse der ANOVA mit summary und summary.lm anzeigen lassen und bekommt jeweils unterschiedliche Informationen (die wir beide benötigen):

```
aov_1 <- aov(size ~ cultivar, data = blume)
summary(aov_1) 
Df Sum Sq Mean Sq F value Pr(>F) 
cultivar 1 76.0 76.05 4.325 0.0521 .
Residuals 18 316.5 17.58 
summary.lm(aov_1)
[…]
Coefficients:
Estimate Std. Error t value Pr(>|t|) 
(Intercept) 15.300 1.326 11.54 9.47e-10 ***
cultivarb -3.900 1.875 -2.08 0.0521 .
```

Beim ersten Output (summary) sehen wir eine typische "ANOVA-Tabelle" wie man sie als Ergebnis linearer Modelle erhält. Die Bedeutung der Abkürzungen ist wie folgt:

- Df = *Degrees of freedom* (Freiheitsgrade) •
- Sum Sq = *Sum of squares* (Summe der Abweichungsquadrate) •
- Mean Sq = *Sum of squares / degrees of freedom* (Quotient der beiden Werte) •
- F value = *Mean Sq (Treatment) / Mean Sq (Residuals)* (Quotient der beiden mittleren Abweichungsquadrate) •
- Pr(>F) = *Probability to obtain a more extreme F value under the null hypothesis* (*p*-Wert) •

Der *F*-Wert ist das Verhältnis der durch die Variable und die Residuen erklärten Varianzen (*Mean squares*), also . Der *F*-Wert (4.33) entsprichtdem quadrierte *t*-Wert (–2.08) aus der unteren Tabelle. Der *p*-Wert (0.052) in der obigen Tabelle ist also genau der gleiche wie im *t*-Test, was die Äquivalenz von ANOVA und *t*-Test zeigt. Dieser *p*-Wert steht für die Nullhypothese, dass sich die beiden Sorten nicht in ihrer Blütengrösse unterscheiden.

Derselbe *p*-Wert taucht im summary.lm-Output unten in der zweiten Zeile auf. Aber für was steht der extrem kleine *p*-Wert in der ersten Zeile des summary.lm-Outputs (9.47 x 10–10)? In der Zeile steht *(Intercept)*, also Achsenabschnitt. Hier ist der vorhergesagte Mittelwert für die erste Sorte (Cultivar a) gemeint. Die Nullhypothese zu dieser Zeile ist, dass die Blütengrösse dieser Sorte = 0 ist. Da Blütengrössen immer positive Werte haben (nie negativ und für eine existierende Blüte auch nie 0), ist das keine sinnvolle/relevante Nullhypothese. In den allermeisten Fällen bezieht sich der *p*-Wert in der ersten Zeile eines summary.lm-Outputs auf eine unsinnige/irrelevante Nullhypothese und wir können ihn ignorieren.

Eine weitere wichtige Information liefert uns die zweite Tabelle aber noch: die Effektgrösse und richtung. Dazu müssen wir in die Spalte *Estimates* schauen, welche die sogenannten Parameterschätzungen enthält. Im Falle einer ANOVA enthält die *(Intercept)*-Zeile den geschätzten Mittelwert für die alphabetisch erste Kategorie (bei uns also Cultivar a), währen das *Estimate* in der Zeile cultivarb für den Unterschied im Mittelwert von Cultivar b vs. Cultivar a steht, hier steht also die biologisch relevante Information, sprich: **die Blüten von Cultivar b sind im Mittel 3.9 cm<sup>2</sup> kleiner als jene von Cultivar a**. Allerdings sind wir uns dieser Aussage nicht besonders sicher, da sie statistisch nur marginal signifikant ist ().

Wenn wir eine "echte" ANOVA mit drei oder mehr Kategorien durchführen, die also nicht mehr mit dem *t*-Test analysiert werden kann, sieht der Output vergleichbar aus, nur hat sich die Zahl der Freiheitsgrade in der ersten Zeile erhöht (immer Zahl der Kategorien – 1, bei 3 Kategorien also 2).

aov\_2 <- aov(size ~ cultivar, data = blume2)

summary(aov\_2)

Df Sum Sq Mean Sq F value Pr(>F) cultivar 2 736.1 368.0 18.8 7.68e-06 \*\*\* Residuals 27 528.6 19.6

In diesem Fall gibt es also höchstsignifikante Unterschiede in der Blütengrösse zwischen den drei Sorten. Wir könnten das Ergebnis kurz und prägnant wie folgt wiedergeben:

![](_page_44_Figure_0.jpeg)

Zwei Anmerkungen: (1) Bei drei und mehr Kategorien kann man im Text nicht mehr effizient schreiben, welche Sorte sich wie von welcher anderen unterscheidet, deshalb bietet sich hier eher eine Visualisierung an (sofern die ANOVA insgesamt ein signifikantes Muster anzeigt). (2) Wenn man den *F*-Wert angeben möchte, so muss man im Subskript nachgestellt die Freiheitsgrade im Zähler (2) und im Nenner (27) angeben, die man der ANOVA-Tabelle entnehmen kann.

### <span id="page-44-0"></span>**Post-hoc-Test (Tukey)**

Aufgrund der vorhergehenden ANOVA wissen wir nun, dass es insgesamt ein signifikantes Muster gibt, dass also nicht alle drei Sorten der gleichen Grundgesamtheit angehören. Was wir nicht wissen, ist, welche Sorte sich von welcher anderen unterscheidet, und ggf. wie stark. Wenn die ANOVA insgesamt signifikant ist, muss das längst nicht heissen, dass jede Sorte sich von jeder anderen unterscheidet. Nun könnte man auf die Idee kommen, einfach für jedes Sortenpaar einen *t*-Test durchzuführen. Das Problem ist, dass man dann u. U. ziemlich viele Tests mit denselben Daten macht, und da summieren sich die Typ I-Fehlerraten schnell auf, sprich: bei vielen Tests werden rein zufällig manche ein signifikantes Ergebnis ergeben (mit α = 0.05 wird 5 % Irrtum zugelassen, d. h. im Durchschnitt liefert jeder zwanzigste Test ein falsch-positives Ergebnis). Um diesem Problem Rechnung zu tragen, gibt es sogenannte posthoc-Tests, die nach einer signifikanten ANOVA angewandt werden. Wenn die ANOVA nicht signifikant war, darf dagegen kein posthoc-Test

angewandt werden! Der gängigste posthoc-Test ist jener von Tukey und findet sich u. a. im agricolae-Paket:

```
library(agricolae)
aov_2 <- aov(size~cultivar, data = blume2)
posthoc <- HSD.test(aov_2, "cultivar", group = FALSE, console = TRUE)
[…]
```

Comparison between treatments means difference pvalue signif. LCL UCL

Andro - Bulli 3.9 0.1388 -1.006213 8.806213

Andro - Chroma -8.0 0.0011 \*\* -12.906213 -3.093787

Bulli - Chroma -11.9 0.0000 \*\*\* -16.806213 -6.993787

Das Ergebnis sagt uns, dass sich Chroma von Andro und Chroma von Bulli, nicht aber Bulli von Andro signifikant unterscheiden. Bei nur drei Kategorien kann man das noch so formulieren, bei vier, fünf oder mehr wird es aber schnell langatmig und komplex. Das lässt sich mit sogenannten homogenen Gruppen lösen. Hier versieht man die Kategorien mit gleichen Buchstaben, die sich nicht signifikant voneinander unterscheiden, ggf. kann dann eine Kategorie auch mehrere Buchstaben tragen. In unserem Fall wäre die Lösung also:

Cultivar Andro: b Cultivar Bulli: b Cultivar Chroma: a • • •

Diese Buchstaben kann man in die Ergebnisabbildung plotten oder als Superskript in einer Ergebnistabelle der Mittelwerte. Die [Abbildung 2.1](#page-46-0) zeigt ein Beispiel. Hier unterscheiden sich nur *High* und *Low* signifikant voneinander, da dies das einzige Paar ist, das keine gemeinsamen Buchstaben hat.

![](_page_46_Figure_0.jpeg)

<span id="page-46-0"></span>Hier ist noch gezeigt, wie man die Beschriftung in die Boxplots bekommt:

labels <- HSD.test(aov\_2, "cultivar", console = TRUE)

Treatments with the same letter are not significantly different.

size groups

Chroma 23.3 a

Andro 15.3 b

Bulli 11.4 b

Die Buchstaben für die homogenen Gruppen aus dem Output muss man dann manuell zur jeweiligen Art plotten (Reihenfolge der Arten beachten!)

```
labels <- posthoc$groups
labels$cultivar <- rownames(labels)
ggplot(blume2, aes(cultivar, size)) +
geom_boxplot() +
geom_text(data = labels, aes(x = cultivar, y = 33, label = groups)) +
stat_summary(fun = mean, geom = "point")
```

![](_page_47_Figure_2.jpeg)

# <span id="page-47-0"></span>**Mehrfaktorielle ANOVA**

Bislang haben wir uns eine ANOVA mit nur einem Prädiktor, d. h. einer kategorialen Variablen mit zwei bis vielen Ausprägungen, angeschaut. Das Prinzip lässt sich aber auch auf zwei und mehr kategoriale Prädiktoren ausweiten. Man spricht dann von einer **mehrfaktoriellen ANOVA**. Im Optimalfall hat man das Erhebungsdesign so gewählt, dass alle Kombinationen Faktorlevels aller Prädiktorvariablen auftreten (dann spricht man von einem **vollfaktoriellen Design**), am besten sogar in gleicher/ähnlicher Häufigkeit.

Betrachten wir exemplarisch die Situation mit zwei Prädiktoren (zweifaktorielle Varianzanalyse, *twoway ANOVA*). Hierzu haben wir in unserem Blumenbeispiel neben den drei Sorten noch ein weiteres

"Treatment" hinzugefügt, nämlich, ob die Pflanzen im Gewächshaus (house = yes) oder im Freiland (house = no) aufgezogen wurden. Der Boxplot in der explorativen Datenanalyse ist in Abbildung 2.5 dargestellt.

![](_page_48_Figure_1.jpeg)

Wir haben nun zwei Möglichkeiten, die zweifaktorielle Varianzanalyse durchzuführen, **mit oder ohne Berücksichtigung von Interaktionen**:

```
aov_3 <- aov(size ~ cultivar + house, data = blume3)
```

summary(aov\_3)

Df Sum Sq Mean Sq F value Pr(>F) cultivar 2 417.1 208.5 5.005 0.01 \* house 1 992.3 992.3 23.815 9.19e-06 \*\*\* Residuals 56 2333.2 41.7

aov\_4b <- aov(size ~ cultivar \* house, data = blume3)

summary(aov\_4b)

Df Sum Sq Mean Sq F value Pr(>F) cultivar 2 417.1 208.5 5.364 0.0075 \*\* house 1 992.3 992.3 25.520 5.33e-06 \*\*\* cultivar:house 2 233.6 116.8 3.004 0.0579 . Residuals 54 2099.6 38.9

Ohne Interaktion (oben) verknüpfen wir die beiden Prädiktoren einfach mit "+"; wenn wir die Interaktion auch analysieren wollen (unten), dann verwenden wir "\*" zur Verknüpfung. Eine Interaktion läge dann vor, wenn sich die Auswirkung von Gewächshaus vs. Freiland zwischen den Sorten unterschiede, etwa in einem Fall positiv, im anderen neutral oder negativ. Wir sehen, dass die untere ANOVA mit dem Interaktionsterm im Output eine dritte Zeile cultivar:house enhält, welche die Signifikanz der Interaktion angibt (in unserem Fall also marginal signifikant).

Liegt eine signifikante Interaktion vor, dann nimmt man zur Ergebnisdarstellung am besten eine Grafik, einen sogenannten Interaktionsplot, da sich die Interaktion schon bei zweifaktoriellen ANOVAs schwer in Worte fassen lässt und noch schwerer bei dreifaktoriellen ANOVAs mit potenziell einer Dreifachinteraktion und drei Zweifachinteraktionen. Bei Zweifachinteraktionen kann man sich zwei unterschiedliche Grafiken anzeigen lassen (R Code ist für die obere):

ggplot(blume3, aes(cultivar, size, color = house, group = house)) + stat\_summary(fun = mean, geom = "point", size = 3) + stat\_summary(fun = mean, geom = "line", linewidth = 1) ggplot(blume3, aes(house, size, color = cultivar, group = cultivar)) + stat\_summary(fun = mean, geom = "line", size = 1) + stat\_summary(fun = mean, geom = "point", size = 3)

![](_page_49_Figure_4.jpeg)

![](_page_50_Figure_0.jpeg)

Die Interaktion war nicht signifikant, was sich darin zeigt, dass die Linienzüge für yes und no einigermassen parallel sind, d. h. im Gewächshaus alle drei Kultivare grösser waren. Allerdings haben sich die drei Kultivare nicht völlig konsistent verhalten: der positive Einfluss von Gewächshaus war bei Sorte c viel grösser als bei den anderen beiden (was zu einem *p*-Wert der Interaktion nahe an der Signifikanzschwelle geführt hat).

Die folgende Abbildung zeigt, wie ein Interaktionsplots schematisch aussehen würden, je nachdem, welche der Prädiktoren (Cultivar, House, Interaktion) signifikant ist. Insgesamt gibt es 2<sup>3</sup> = 8 Kombinationen. Zur Vereinfachung zeigt die Abbildung eine Situation mit nur zwei Kultivaren (rot, blau). Schwarze Linien stehen für Linien der Kultivare, die fast deckungsgleich sind.

![](_page_51_Figure_0.jpeg)

# <span id="page-52-0"></span>**Voraussetzung statistischer Verfahren**

In Statistik 1 wurde kurz erwähnt, dass jeder statistische Test auf bestimmten Annahmen bezüglich der Werteverteilung in der Grundgesamtheit beruht. Beim klassischen *t*-Test nach Student sind das die Normalverteilung und die Varianzhomogenität.

### <span id="page-52-1"></span>**Parametrische vs. nicht-parametrische Verfahren**

Verfahren, die auf dem folgenden gängigen Set von Voraussetzungen beruhen, werden als **parametrische Verfahren** bezeichnet. Es sind dies zugleich die **"linearen Modelle"** (doch zu diesem Begriff später mehr):

- Normalverteilung der *Residuen* 1.
- Varianzhomogenität 2.
- Feste *x*-Werte 3.
- Unabhängigkeit der Beobachtungen / Zufällige Beprobung 4.

Dem gegenüber gestellt werden so-genannte "nicht-parametrische" Verfahren. Der Begriff ist allerdings sehr irreführend, da nicht-parametrische Verfahren nicht etwa keine Voraussetzungen haben, sondern meist nur geringfügig schwächere als parametrische Verfahren. Die **Voraussetzungen für die Anwendung gängiger nicht-parametrischer Verfahren** sind:

- Die Verteilung der Residuen kann einer beliebigen Funktion folgen, muss aber für die verschiedenen Faktorlevels (Kategorien) gleich sein 1.
- Feste *x*-Werte 2.
- Unabhängigkeit der Beobachtungen / Zufällige Beprobung 3.

Diese beiden Listen, weisen auf drei weitverbreitete Irrtümer in der Statistik hin, die in älteren Statistikbüchern regelmässig falsch dargestellt wurden und die auch heute noch in Statistikkursen an Hochschulen oft falsch gelehrt werden:

- **Irrtum 1: die abhängige oder gar die unabhängige Variable sollte normalverteilt sein.** Korrekt ist: Nur die Residuen des statistischen Models sollten normalverteilt sein. Dagegen ist es gleichgültig, ob die Werte der abhängigen Variablen normalverteilt sind, und erst recht gilt das für die unabhängigen Variablen. •
- **Irrtum 2: es kommt hauptsächlich auf die Normalverteilung an.** Korrekt ist: Die Varianzhomogenität ist wichtiger als Normalverteilung der Residuen. •
- **Irrtum 3: Bei kleinsten Abweichungen von der Varianzhomogenität oder Normalverteilung sollte auf ein nicht-parametrisches Äquivalent ausgewichen werden.** Korrekt ist: Dieses Vorgehen ist meist nicht nötig, aber unvorteilhaft (da nichtparametrische Verfahren meist eine geringere Teststärke haben), im schlimmsten Fall sogar falsch (wie die Voraussetzungen des nicht-parametrischen Verfahrens gleichermassen verletzt sind). •

In der Folge ist zu beobachten, dass vielfach vorschnell und unnötig auf "nicht-parametrische" Verfahren ausgewichen wird. **Dagegen sprechen viele Gründe dafür, in fast allen Fällen mit parametrischen Verfahren zu arbeiten**:

- Parametrische Verfahren sind recht robust gegen die Verletzung der Voraussetzungen, d. h. sie liefern selbst bei recht starken Abweichungen noch (fast) korrekte *p*-Werte, wie die folgende Simulation zeigte:
- Laut Quinn & Keough (2002) haben Simulationen Folgendes gezeigt:
  - : selbst bei bis zu vierfacher SD noch korrekte *p*-Werte
  - $^{\circ}$  , : Wenn  $SD_1$  = 4  $SD_2$ , dann entspricht ein berechneter in Wirklichkeit
- mit  $n_1$  und  $n_2$  = Stichprobengrösse für Faktorlevels 1 und 2 und SD = Standardabweichung
- Die meisten komplexeren statistischen Verfahren existieren ohnehin nur in einer parametrischen Variante.
- Dank Datentransformationen (s. Statistik 2 unten) und Generalisierungen linearer Modelle (s. Statistik 5) kann man auch mit Nicht-Normalität der Residuen und Varianzheterogenität = Heteroskedasitzität umgehen.

### <span id="page-53-0"></span>Wie testet man die Voraussetzungen? (klassischer Weg)

Der "klassische" (aber nicht zielführende!!!) Rat in vielen Statistikbüchern/-kursen ist die Anwendung statistischer Tests für Normalität und Varianzhomogenität. Für die Normalität (beachten, dass die Residuen, nicht die Rohdaten getestet werden müssen, also im Fall einer ANOVA die Werte jeder Kategorie für sich). Es gibt u.a. den Kolmogorov-Smirnov-Test (mit Lillefors-Korrektur) und den Sharpiro-Wilks-Test:

Für das Testen der Varianzhomogenität gibt es u.a. den *F*-Test zur Varianzhomogenität und den Levene-Test (im Paket car):

Wenn die *p*-Werte dieser Tests < 0.05 sind, dann liegt eine statistisch signifikante Abweichung von der jeweiligen Voraussetzung vor. Die klassische Konsequenz war, dann auf ein nicht-parametrisches Verfahren auszuweichen. Studierende und viele PraktikerInnen lieben diese scheinbar simple Schwarz-weiss-Sicht, die ein klares Prozedere vorzugeben scheint. Leider bringen diese Tests für die Entscheidung zwischen parametrischen und nicht-parametrischen Verfahren NICHTS. Die Gründe sind eigentlich einfach:

- Die genannten Tests testen allesamt die Wahrscheinlichkeit der Abweichung, nicht den Grad der Abweichung (wobei Letzteres der relevante Punkt ist).
- Damit werden einerseits bei kleinen Stichproben auch problematische Abweichungen nicht erkannt, bei grossen Stichproben harmlose Abweichungen dagegen "moniert" (man sollte sich bewusst sein, dass Variablen in der realen Welt niemals perfekt normalverteilt oder perfekt varianzhomogen sind)

Deshalb wird in modernen Lehrbüchern ausdrücklich davon abgeraten, die genannten Tests für diesen Zweck zu verwenden (z. B. Quinn & Keough 2002).

### <span id="page-54-0"></span>**Wie testet man die Voraussetzungen? (empfohlener Weg)**

Da die "klassischen" numerischen Tests nichts helfen, bleibt nur ein Weg, selbst wenn er zunächst unbefriedigend und subjektiv erscheinen mag. Moderne statistische Lehrbücher empfehlen heute, Normalverteilung der Residuen und Varianzhomogenität visuell zu prüfen und nur bei groben Verletzungen über alternative Vorgehensweisen nachzudenken.

Im Fall von *t*-Tests bzw. ANOVAs ist die einfachste Möglichkeit, nach Faktorlevels gruppierte Boxplots zu betrachten. Alternativ gingen auch Histogramme, allerdings sind diese nur bei grossen *n* aussagekräftig [\(Abbildung 2.2](#page-55-0)).

![](_page_55_Picture_0.jpeg)

![](_page_56_Figure_0.jpeg)

# Histogram of blume\$a

![](_page_57_Figure_1.jpeg)

![](_page_58_Figure_0.jpeg)

Für die **Beurteilung der Varianzhomogenität** betrachtet man am besten die Höhe der Boxen im Boxplot. Wenn sie ähnlich hoch sind, ist alles OK, wenn sie sehr stark abweichen, hat man evtl. ein Problem. Sehr stark meint aber, siehe [Abbildung 2.2,](#page-55-0) wirklich sehr stark, d. h. wenn die Box in einer Kategorie mehr als 4-mal so hoch ist wie in einer anderen (bei gleichen/ähnlichen Replikatzahen), und ab mehr als doppelt so hoch bei erheblich verschiedenen Replikatzahlen. Im vorliegenden Fall ist die Varianz in Gruppe 1 etwa 2.5-mal so hoch wie in Gruppe 2, da die Zahl der Replikate aber identisch war, wäre das noch OK.

Zur **Beurteilung der Normalverteilung** bzw. des entscheidenden Aspekts der Normalverteilung, der Symmetrie, sind ebenfalls die Boxplots aufschlussreich. Eine starke Verletzung liegt vor, wenn der Median weit ausserhalb der Mitte der Box liegt oder wenn der obere "whisker" viel länger als der untere ist (oder auch umgekehrt, aber das kommt in der Praxis so gut wie nie vor).

Ausserdem gibt es noch das *Central Limit Theorem* **(CLT)** in der Statistik. Dieses Theorem besagt, dass wenn eine betrachtete Variable selbst schon ein Mittelwert ist, sie zwingend einer Normalverteilung folgt. In diesem Fall ist also kein Test nötig/sinnvoll. Wenn man sich auf das CLT berufen will, kann man z. B. Quinn & Keough (2002) zitieren.

### <span id="page-59-0"></span>**Was tun, wenn die Voraussetzungen verletzt sind? (nichtparametrische Verfahren)**

Bei Verletzung der Voraussetzungen, kann man auf nicht-parametrische Verfahren ausweichen, was OK ist, wenn man sich völlig klar darüber ist, welche Voraussetzungen diese ihrerseits haben:

Das nicht-parametrische Äquivalent zum *t*-Test ist der **Wilcoxon-Rangsummen-Test**. Er funktioniert, indem Werte in Ränge transformiert und summiert werden (W-statistic). Nachteile sind, dass er sehr konservativ ist (d. h. tendenziell zu hohe *p*-Werte schätzt). Der klassische Wilcoxon-Test (wilcox.test aus base R) kann zudem keine exakten *p*-Werte berechnen, wenn Bindungen(*ties*) vorliegen, d.h. mehrere Beobachtungen identische Werte aufweisen. Deswegen verwenden wir hier einen permutationsbasierten Wilcoxon-Test aus dem Paket coin, der dieses Problem nicht hat. Ausserdem sei noch einmal betont, dass der Wilcoxon-Test zwar keine Annahme über die Verteilung der Werte pro Gruppe macht, jedoch voraussetzt, dass diese in jeder Gruppe gleich ist.

library(coin)

wilcox\_test(size ~ cultivar, data = blume)

Ferner gibt es **Randomisierungs-***t***-Tests**. Diese haben den Vorteil, dass keine Annahme über die Verteilung getroffen werden muss (die Verteilung wird aus den Daten generiert). Zugleich müssen die Beobachtungen noch nicht einmal unabhängig sein. Allerdings testet man hier strenggenommen auch nicht auf Unterschiede in den Grundgesamtheiten, sondern ermittelt die Wahrscheinlichkeit, die beobachteten Unterschiede zufällig erzielt zu haben. Wer mehr über Randomisierungs-Tests wissen will, findet in Logan (2010: 148–150) weitergehende Infos.

Im Fall eines ANOVA-Designs gibt es zwei Situationen, mit jeweils anderen Alternativen zur klassischen ANOVA:

- Wir haben starke **Abweichungen von der Normalverteilung** der Residuen, aber **ähnliche Varianzen**. Dann kann der Kruskal-Wallis-Test zum Einsatz kommen (ebenfalls ein Rangsummen-Test). Der zugehörige posthoc-Test ist der Dunn-Test mit Benjamin-Hochberg-Korrektur der *p*-Werte (wegen multiplem Testen): 1.
- kruskal\_test(size~cultivar, data = blume2,) •
- library(FSA) dunnTest(size~cultivar, method = "bh", data = blume2,) •
- Wenn dagegen die **Varianzen sehr heterogen** sind, die **Residuen aber relativ normal/symmetrisch**, wie in [Abbildung 2.3,](#page-60-1) kann der **Welch-Test** eingesetzt werden: 1.

<span id="page-60-1"></span>![](_page_60_Figure_0.jpeg)

Abbildung 2.3. Boxplot von Residuenverteilungen, die recht gut einer Normalverteilung entspricht (Mediane ungefähr in der Mitte jeder Box, Whisker jeder Box oben und unten ähnlich lang), wo aber die Varianzen deutlich, wenn auch nicht extrem verschieden sind (siehe die unterschiedliche Höhe der Boxen).

oneway.test(size~cultivar, var.equal = F, data = blume2,)

### <span id="page-60-0"></span>**Was tun, wenn die Voraussetzungen (erheblich) verletzt sind? (Transformationen)**

Statt auf nicht-parametrische Verfahren auszuweichen, kann man auch Transformationen anwenden. Da es um die Verteilung der Residuen geht, muss primär die abhängige Variable für Transformationen in Betracht gezogen werden, manchmal hilft aber auch die Transformation einer unabhängigen Variablen (weitergehende Infos siehe Fox & Weisberg 2019: 161–169).

Wenn man über die Anwendung von Transformationen nachdenkt, sind zwei Aspekte relevant: (1) Entgegen manchen Behauptungen sind untransformierte Daten (linear Skala) nicht *per se* natürlicher/richtiger. Auch die lineare Skala ist eine Konvention. Viele Naturgesetze (z. B. unsere Sinneswahrnehmung) funktionieren dagegen auf einer Logarithmusskala. (2) Wenn man die abhängige Variable transformiert, muss man sich aber klar darüber sein, dass man dann strenggenommen Hypothesen über die transformierten Daten, nicht über die ursprünglichen Werte testet. Achtung: Wenn man die Analysen mit transformierten Daten durchführt, darf man **für die**

### **Ergebnisdarstellung die Rücktransformation mittels der jeweiligen Umkehrfunktion** nicht vergessen!

Gängige Transformation für die abhängige Variable sind die folgenden:

#### **Logarithmus-Transformation:**

- Gut bei rechtsschiefen Daten/wenn die Varianz mit dem Mittelwert zunimmt. •
- Die "natürlichste" Transformation. •
- Natürlicher Logarithmus (log) oder Zehnerlogarithmus (log10) möglich. •
- Werte müssen > 0 sein. •

#### **log (***x* **+ Konstante)-Transformation:**

- Findet man häufig in der Literatur, wenn abhängige Variablen transformiert werden sollen, die auch Nullwerte enthalten •
- Es werden unterschiedliche Konstanten (*x*) addiert, mal 1, mal 0.01. Es ist aber völlig willkürlich, ob man 1000000 oder 0.00000001 oder 3.24567 addiert, hat aber starken Einfluss auf die Ergebnisse •
- Auch lassen sich die Ergebnisse nach so einer komplexen Transformation schlecht interpretieren (da man dann ja eine Hypothese über die transformierten Daten testet, s. o.) •
- In Übereinstimmung mit Wilson (2007) rate ich daher dringend von derlei Transformationen ab! •

#### **Wurzeltransformation:**

- Hat einen ähnlichen Effekt wie die Logarithmus-Transformation, lässt sich im Gegensatz zu dieser auch beim Vorliegen von Nullwerten anwenden (Werte müssen nur positiv sein). •
- Die "Stärke" der Transformation kann man durch die Art der Wurzel kontinuierlich einstellen: Quadratwurzel, Kubikwurzel, 4. Wurzel,… •

### **"arcsine"-Transformation:**

asin(sqrt(x))\*180/pi

- Wurde traditionell für Prozentwerte (Proportionen) und andere abhängige Variablen empfohlen, die zwischen 0 und 1 bzw. 0 und 100% begrenzt sind (z. B. Quinn & Keough 2002). •
- Nach neueren Untersuchungen (Warton & Hui 2011) wird eher davon abgeraten. •

#### **Rangtransformation:**

- Im Prinzip das, was "nicht-parametrische" Verfahren machen. •
- Grösster Informationsverlust von allen genannten Verfahren (noch grösser wäre der Informationsverlust nur bei Überführung der metrischen abhängigen Variablen in Kategorien oder gar in eine Binärvariable). •

[Abbildung 2.4](#page-63-0) visualisieren exemplarisch die Effekte unterschiedlicher Transformationen auf die Werteverteilung (ganz links sind jeweils die untransformierten Daten, die Transformation rechts hat jeweils eine deutlich bessere Annäherung an die Normalverteilung erzielt).

![](_page_63_Figure_0.jpeg)

![](_page_64_Figure_0.jpeg)

Abbildung 2.4. Auswirkungen von Wurzel-, Logarithmus- und Arcsin-Transformationen auf die Verteilung von Daten. Man sieht, dass bei den gezeigten Verteilungen in den Originaldaten die jeweiligen Transformationen eine Verbesserung bezüglich der Normalverteilungsannahme brachten (aus Quinn & Keough 2002).

Meist muss man nur die abhängige Variable transformieren. Es gibt aber Spezialfälle, wo man erst nach Transformation der abhängigen und der unabhängigen Variable eine adäquate Residuenverteilung erzielt. Dies ist insbesondere dann der Fall, wenn wir eine in Wirklichkeit nichtlineare Beziehung mit einem linearen Modell abbilden. Wenn etwa im Falle einer einfachen linearen Regression (s. u.) in Wirklichkeit ein Potenzgesetz (*y* = *a x<sup>b</sup>* ) vorliegt, erzielt man näherungsweise Varianzhomogenität und Normalverteilung der Residuen nur, wenn man a und b logarithmustransformiert.

## <span id="page-64-0"></span>**Zusammenfassung**

- *t***-Tests und ANOVAs** sind parametrische Verfahren, um auf **Unterschiede in den Mittelwerten einer metrischen Variablen** zwischen zwei bzw. beliebig vielen Gruppen zu testen. •
- **Parametrische Verfahren** basieren auf **bestimmten Annahmen** zur Streuung der Daten, sind aber **robust** gegenüber deren Verletzung. •
- Die **Voraussetzungen parametrischer Verfahren** beziehen sich auf die **Residuen**, nicht auf die unabhängigen, noch auf die abhängigen Variablen *per se*. •

# <span id="page-64-1"></span>**Weiterführende Literatur**

- **Crawley, M.J. 2015.** *Statistics An introduction using R***. 2nd ed. John Wiley & Sons, Chichester, UK: 339 pp.** •
  - **Chapter 7 Regression: pp. 114–139** ◦

#### **Chapter 8 – Analysis of Variance: pp. 150–167** ◦

- Fox, J. & Weisberg, S. 2019. *An R companion to applied regression*. 3rd ed. SAGE Publications, Thousand Oaks, CA, US: 577 pp. •
- Logan, M. 2010. *Biostatistical design and analysis using R. A practical guide*. Wiley-Blackwell, Oxford, UK: 546 pp. •
  - pp. 151-166 (lineare Modelle) ◦
  - pp. 167-207 (Korrelation und einfache lineare Regression) ◦
  - pp. 254-282 (Einfaktorielle ANOVA) ◦
  - pp. 311-359 (Mehrfaktorielle ANOVA) ◦
- Quinn, G.P. & Keough, M.J. 2002. *Experimental design and data analysis for biologists*. Cambridge University Press, Cambridge, UK: 537 pp. •
- Warton, D.I. & Hui, F.K.C. 2011. The arcsine is asinine: the analysis of proportions in ecology. *Ecology* 92: 3–10. •
- Wilson, J.B. 2007. Priorities in statistics, the sensitive feet of elephants, and don't transform data. *Folia Geobotanica* 42: 161–167. •

# <span id="page-65-0"></span>**Statistik 3**

Korrelationen, einfache und quadratische Regressionen, ANCOVAs

**In Statistik 3 beschäftigen wir uns mit Korrelationen, die auf einen linearen Zusammenhang zwischen zwei metrischen Variablen testen, ohne Annahme einer Kausalität. Es folgen einfache lineare Regressionen, die im Prinzip das Gleiche bei klarer Kausalität leisten. Dann wird die ANCOVA als eine Technik vorgestellt, die eine ANOVA mit einer linearen Regression verbindet. Danach geht es um komplexere Versionen linearer Regressionen. Hier betrachten wir polynomiale Regressionen, die z. B. einen Test auf unimodale Beziehungen erlauben, indem man dieselbe Prädiktorvariable linear und quadriert einspeist. Dann besprechen wir, was die grosse Gruppe linearer Modelle (Befehl lm in R) auszeichnet. Abschliessend fassen wir zu Beginn den generellen Ablauf inferenzstatistischer Analysen in einem Flussdiagramm zusammen.** 

# <span id="page-65-1"></span>**Lernziele**

#### Ihr…

- habt den Unterschied zwischen Korrelationen und Regressionen verstanden und könnt sie in R implementieren; •
- versteht, wann es Sinn macht, **quadratische Terme in eine Regression** einfliessen zu lassen und warum das dann trotzdem noch ein lineares Modell ist •
- wisst, wofür **ANCOVA** steht, wann dieses statistische Verfahren zum Einsatz kommt und wie das praktisch geht; •
- kennt die Voraussetzungen und Gemeinsamkeiten aller linearen Modelle; und •
- wisst, warum es nach der Berechnung eines linearen Modelles essenziell ist, die Residuen zu checken, und könnt die diagnostischen Grafiken von R dazu interpretieren. •

## <span id="page-66-0"></span>**Korrelationen**

**Pearson-Korrelationen** analysieren den Zusammenhang zwischen zwei metrischen Variablen und beantworten dabei die folgenden Fragen:

- Gibt es einen **linearen** Zusammenhang? •
- In welche Richtung läuft er? •
- Wie stark ist er? •

Wichtig dabei ist, dass Korrelationen keine Kausalität voraussetzen oder annehmen. Es gibt also keine abhängige und unabhängige Variable, keine Unterscheidung in Prädiktor- und Antwortvariable. Logischerweise liefern Korrelationen dann auch identische Ergebnisse, wenn *x*und *y-*Achse vertauscht werden.

Die folgenden fünf Abbildungen zeigen verschiedene Situationen. Bei (a) liegt eine positive Korrelation vor, bei (b) eine negative und bei (c)–(e) keine Korrelation. Bei (e) erkennt man zwar visuell eine Beziehung (ein "Peak" in der Mittel, also eine unimodale Beziehung), aber das ist eben kein linearer Zusammenhang.

![](_page_66_Figure_7.jpeg)

![](_page_66_Picture_8.jpeg)

![](_page_66_Picture_9.jpeg)

![](_page_66_Figure_10.jpeg)

![](_page_66_Figure_11.jpeg)

(aus Quinn & Keough 2002)

Bei der Pearson-Korrelation betrachtet man die beiden Parameter Kovarianz (reicht von −∞ bis +∞) und die Korrelation, welche die Kovarianz auf den Bereich von –1 bis +1 standardisiert. Pearsons Korrelationskoeffizient r ist der Schätzer für die Korrelation basierend auf der Stichprobe (Abbildung 2.6).

| Parameter                               | Estimate                                                                                                                                                            |
|-----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Covariance: $\sigma_{\gamma_1\gamma_2}$ | $s_{Y_1Y_2} = \frac{\sum_{i=1}^{n} (y_{i1} - \bar{y}_1)(y_{i2} - \bar{y}_2)}{n - 1}$                                                                                |
| Correlation: $\rho_{\gamma_1\gamma_2}$  | $r_{Y_1Y_2} = \frac{\sum_{i=1}^{n} [(y_{i1} - \bar{y}_1)(y_{i2} - \bar{y}_2)]}{\sqrt{\sum_{i=1}^{n} (y_{i1} - \bar{y}_1)^2 \sum_{i=1}^{n} (y_{i2} - \bar{y}_2)^2}}$ |

Abbildung 2.6. Definition von Kovarianz und Pearson Korrelation (griechische Buchstaben beziehen sich auf den Wert in der Grundgesamtheit, römische auf den Schätzwert basierend auf der Stichprobe).

Die implizite Nullhypothese ( $H_0$ ) ist nun  $\rho$  = 0. Die Teststatistik ist das uns schon bekannte t mit , wobei  $s_r$  für den Standardfehler von r steht und bei n – 2 Freiheitsgraden getestet wird.

Die Pearson-Korrelation ist die parametrische Variante der Korrelationen. Ihre Anwendung hat zwei Voraussetzungen (in Klammern ist angegeben, wie man ihr Vorliegen visuell überprüfen kann):

- Linearität (Überprüfung mit einem xy-Scatterplot)
- Bivariate Normalverteilung (Überprüfung mit Boxplots beider Variablen)

Wenn diese Voraussetzungen ungenügend erfüllt sind, kann man auf nicht-parametrische Äquivalente ausweichen. Diese testen auf monotone, nicht auf lineare Beziehungen, liefern allerdings keine exakten Ergebnisse bei Bindungen (d. h. wenn der gleiche Wert mehrfach vorkommt):

- Für  $7 \le n \le 30$ : **Spearman-Rang-Korrrelation** ( $r_s$ ) (im Prinzip Pearsons r für rangtransformierte Daten)
- Für *n* > 30: **Kendall's tao (τ)**

Hier noch der R Code für alle drei Möglichkeiten:

cor.test(df\$Species\_richness, df\$N.deposition, method = "pearson")
cor.test(df\$Species\_richness, df\$N.deposition, method = "spearman")
cor.test(df\$Species\_richness, df\$N.deposition, method = "kendall")

### <span id="page-67-0"></span>**Einfache lineare Regressionen**

#### <span id="page-67-1"></span>Idee

Einfache lineare Regressionen sind konzeptionell und mathematisch ähnlich zu Pearson-Korrelationen. Oft werden beide Verfahren daher fälschlicherweise auch begrifflich durcheinandergeworfen. Der **entscheidende Unterschied** ist, dass wir für eine Regression eine **theoretisch vermutete Kausalität** haben müssen. Damit haben wir, anders als bei einer Korrelation, eine fundamentalte Unterscheidung in:

- *X***: unabhängige Variable** (*independent variable*), Prädiktorvariable (*predictor*) •
- *Y***: abhängige Variable** (*dependent variable*), Antwortvariable (*response*) •

Bei Visualisierungen ist zu beachten, dass die unabhängige Variable immer auf der *x*-Achse dargestellt wird, die abhängige dagegen auf der nach oben gerichteten *y*-Achse.

Mathematisch wird eine lineare Regression analysiert, indem die bestangepasste Gerade durch die Punktwolke des *xy*-Scatterplots gelegt wird. Dabei sieht das lineare Modell folgendermassen aus:

- **Geradengleichung**: •
- **Statistisches Modell**: , wobei das Residuum des *i*-ten Datenpunktes ist, d. h. seine vertikale Abweichung vom vorhergesagten Wert •

Mit einer einfachen linearen Regression testet man die folgenden beiden Nullhypothesen:

- : (Achsenabschnitt [*intercept*] der Grundgesamtheit ist Null) (diese erste Nullhypothese ist, ähnlich wie bei Varianzanalysen, in den meisten Fällen wissenschaftlich nicht relevant) •
- : (Steigung [*slope*] der Grundgesamtheit ist Null) •

Die folgende Abbildung veranschaulicht die verschiedenen Möglichkeiten:

![](_page_68_Figure_11.jpeg)

Abb. Visualisierung, wie die Beziehung aussähe, abhängig von den Werten der beiden Parameter (aus Logan 2010).

### <span id="page-68-0"></span>**Statistische Umsetzung**

Es mag vielleicht zunächst überraschen, aber ähnlich wie beim Vergleich von Mittelwerten zwischen kategorischen Ausprägungen kategorischer Variablen, liegt auch der linearen Regression eine **Varianzanalyse** zugrunde wie die folgende Tabelle zeigt. Die Bedeutung der verschiedenen Differenzen ist in Abbildung 2.7 visualisiert.

| Table 5.3         Analysis of variance (ANOVA) table for simple linear regression of Y on X |                                          |       |                                                    |                                                                                 |
|---------------------------------------------------------------------------------------------|------------------------------------------|-------|----------------------------------------------------|---------------------------------------------------------------------------------|
| Source of variation                                                                         | SS                                       | df    | MS                                                 | Expected mean square                                                            |
| Regression                                                                                  | $\sum_{i=1}^{n} (\vec{y}_i - \vec{y})^2$ | I     | $\frac{\sum_{i=1}^{n} (\hat{y}_i - \bar{y})^2}{I}$ | $\sigma_{\varepsilon}^{2} + \beta_{1}^{2} \sum_{i=1}^{n} (X_{i} - \bar{X})^{2}$ |
| Residual                                                                                    | $\sum_{i=1}^{n} (y_i - \hat{y_i})^2$     | n – 2 | $\frac{\sum_{i=1}^{n}(y_i-\hat{y_i})^2}{n-2}$      | $\sigma_{\scriptscriptstyle E}^2$                                               |
| Total                                                                                       | $\sum_{i=1}^{n} (y_i - \bar{y})^2$       | n-1   |                                                    |                                                                                 |

![](_page_69_Figure_1.jpeg)

Abbildung 2.7. Visualisierung der verschiedenen Differenzen, die in die ANOVA-Tabelle einer linearen Regression einfliessen (aus Quinn & Keough 2002).

Wiederum ist die Teststatistik ein -ratio, nämlich , wobei MS für die mittleren Quadratsummen steht, also die Quadratsummen (SS) geteilt durch die Freiheitsgrade (df). Wie oben unter der Varianzanalyse schon erwähnt, folgt einer -Verteilung.

### <span id="page-69-0"></span>**Implementierung in R**

Das Kommando zum Berechnen einfacher linearer Regressionen lautet lm. Es legt eine gerade so in die Punktwolke, dass sie Summe der Abweichungsquadrate (quadrierte Residuen) minimal ist. Deswegen wird dieses gängige Regressionsverfahren auch als Ordinary least squares-Methode (OLS) bezeichnet. Wie bei einem Mittelwertvergleich mittels Varianzanalyse gibt es dann zwei verschiedene Ansichten des Ergebnis-Outputs, die jeweils verschiedene Teilaspekte zeigen (hier am Beispiel der Beziehung von Pflanzenartenreichtum zur Stickstoffdeposition):

Die **aov-Ansicht** liefert uns die oben besprochene ANOVA-Tabelle, einschliesslich der Signifikanz der Steigung (hier ).

```
lm_1 <- lm(Species_richness~N.deposition, data = df)
```

summary.aov(lm\_1) # ANOVA-Tabelle

Response: Species\_richness Df Sum Sq Mean Sq F value Pr(>F) N.deposition 1 233.91 233.908 28.028 0.0001453 \*\*\* Residuals 13 108.49 8.346

Weitere erforderliche Aspekte des Ergebnisses sehen wir in der **summary-Ansicht**:

summary(lm\_1) # Regressionskoeffizienten

#### Coefficients:

Estimate Std. Error t value Pr(>|t|) (Intercept) 25.60502 1.26440 20.251 3.25e-11 \*\*\* N.deposition -0.26323 0.04972 -5.294 0.000145 \*\*\* […]

Residual standard error: 2.889 on 13 degrees of freedom Multiple R-squared: 0.6831, Adjusted R-squared: 0.6588 F-statistic: 28.03 on 1 and 13 DF, p-value: 0.0001453

Wie wir sehen, tauchen wiederum der *F*-Wert (28.03) und sogar zweimal der *p*-Wert der Steigung (0.0001) auf, daneben auch der i. d. R. bedeutungslose *p*-Wert des Achsenabschnitts (*intercept*) (3.25 x 10-11).

Werfen wir noch einmal einen Blick auf den Output von R:

Wir benötigen für eine Darstellung der Ergebnisse:

- **Name des Verfahrens (Methode)**: Einfache lineare Regression (mit der Methode derkleinsten Quadrate). 1.
- **Signifikanz (Verlässlichkeit des Ergebnisses)**: p-Wert der Steigung, nicht der p-Wert des Achsenabschnittes (wird nach üblicher Konvention auf drei Nachkommastellen gerundet oder, wenn unter 0.001, dann als p < 0.001 angegeben). 2.
- **Effektgrösse und -richtung (unser eigentliches Ergebnis!)**: Im Falle einer linearen Regression ist das die Funktionsgleichung, die sich aus den Schätzungen der Koeffizienten ergibt. 3.

- **Erklärte Varianz (Relevanz des Ergebnisses)**: Wie viel der Gesamtvariabilität der Daten wird durch das Modell erklärt? Ob oder angegeben werden sollte, wird unterschiedlich gesehen, jedenfalls sollte man explizit sagen, was gemeint ist. *R*² ist übrigens der quadrierte Wert von Pearsons Korrelationskoeffizienten . 4.
- **ggf. Wert der Teststatistik mit den Freiheitsgraden ("Zwischenergebnisse")**: . 5.

Ein adäquater Ergebnistext könnte daher wie folgt lauten:

Der Artenreichtum nahm hochsignifikant mit der Stickstoffdeposition ab (Funktionsgleichung: , , , .

Bei einem signifikanten Ergebnis bietet sich auch noch eine Visualisierung mittels Scatterplots an, in den die Regressionsgerade geplottet ist:

ggplot(df, aes(x = N\_deposition, y = Species\_richness)) + geom\_point() + geom\_abline(intercept = lm1\$coefficients[1], slope = lm1\$coefficients[2], color = "blue")

![](_page_71_Figure_6.jpeg)

### <span id="page-72-0"></span>**Voraussetzungen**

Einfache lineare Regressionen basieren auf drei Voraussetzungen:

- **Linearität** 1.
- **Normalverteilung** (der Residuen!) 2.
- **Varianzhomogenität** 3.

Für das meistverwendete **Verfahren der kleinsten Abweichungsgquadrate** (wie bislang besprochen; *ordinary least squares* **= OLS = Befehl lm in R**), auch als **Modell I-Regressionen** bezeichnet, muss zudem gelten:

- **Feste** *x***-Werte**, d. h. 1.
  - *x*-Werte vom Experimentator gesetzt ODER ◦
  - Fehler in den *x*-Werten viel kleiner als in den *y*-Werten ◦
- **Sowie auch für folgende Fälle**: •
  - Hypothesentest im Fokus, nicht der exakte Wert von β~1 ◦
  - Für prädiktive Modelle ◦
  - Wenn keine bivariate Normalverteilung vorliegt ◦

### <span id="page-72-1"></span>**Alternativen zur Methode der kleinsten Quadrate (OLS)**

In den allermeisten Fällen wird in der Praxis angenommen, dass eine der Möglichkeiten unter dem vorstehenden Punkt 4 zutrifft, mithin also OLS/lm zur Anwendung kommen kann. Wenn keine der oben unter Punkt 4 genannten Voraussetzungen erfüllt ist, dann sollte eine sogenannte **Modell-II-Regression (Nicht-OLS-Regression)** durchgeführt werden. Hier stehen als Möglichkeiten die *Major axis regression*, die *Ranged major axis regression* und die *Reduced major axis regression* zur Verfügung., die wir aber im Kurs nicht weiter besprechen. Details finden sich in Logan (2010: 173– 175), woraus aus Abbildung 2.8 stammt:

![](_page_73_Figure_0.jpeg)

Abbildung 2.8. Visualisierung der Anwendung verschiedener Regressionstechniken auf den gleichen Datensatz (aus Logan 2010).

In R stehen solche Methoden u. a. im Paket lmodel2 zur Verfügung (hier illustriert für einen fiktionalen Datensatz):

library(lmodel2) lmodel2(b~a)

#### Regression results

Method Intercept Slope Angle (degrees) P-perm (1-tailed)

- 1 OLS 5.019254 0.4170422 22.63820 NA
- 2 MA 4.288499 0.4648040 24.92919 NA
- 3 SMA 3.067471 0.5446097 28.57314 NA

Wie man sieht, unterscheiden sich die beiden Modell-II-Ergebnisse deutlich von Modell I (OLS) bezüglich Achsenabschnitt, Steigung und damit auch Winkel.

### <span id="page-73-0"></span>**Polynomische Regressionen**

Eine quadratische Regression (Polynom 2. Ordnung) ist die einfachste Möglichkeit, eine sogenannte unimodale (*hump shaped*) Beziehung von abhängiger zur unabhängigen Variablen mathematisch

abzubilden. Unimodal/*humpshaped* meint, dass die Kurve ein Maximum hat, d. h. die abhängige Variable für mittlere Werte der Prädiktorvariablen den höchsten Wert aufweist. Für viele Beziehungen sind solche unimodalen Kurvenverläufe theoretische vorhergesagt und/oder theoretisch nachgewiesen. In der Ökologie gilt das z. B. für die Beziehung des Artenreichtums zu so unterschiedlichen Faktoren wie Störungshäufigkeit (*intermediate disturbance hypothesis*, IDH), Boden-pH-Wert und Produktivität/Biomasse.

Das statistische Modell für eine quadratische Beziehung ist:

In R wird eine quadratische Regression folgendermassen codiert:

```
lm_quad <- lm(resp ~ pred + I(pred^2))
summary(lm_quad)
```

#### Coefficients:

Estimate Std. Error t value Pr(>|t|) (Intercept) -2.239308 3.811746 -0.587 0.56777 pred 1.330933 0.360105 3.696 0.00306 \*\* I(pred^2) -0.031587 0.007504 -4.209 0.00121 \*\*

Wichtig ist, dass man den quadratischen Term im lm-Befehl nicht einfach als «e^2» eingeben kann, sondern «I(e^2)» schreiben muss. Eine signifikante unimodale Beziehung ist dann gegeben, wenn die Parameterschätzung für den quadratischen Term (also e^2) negativ ist – man hat eine nach unten offene Parabel. Ist der quadratische Term dagegen signifikant positiv, hat man eine nach oben offene Parabel, also eine u-förmige Beziehung (Minimum für die abhängige Variable bei intermediären Werten der Prädiktorvariablen).

Wichtig ist, dass man wie bei allen statistischen Modellen nachträglich die Modellvoraussetzungen prüft. Betrachten wir das jetzt für die simulierten Daten f und e, ohne Berücksichtigung eines quadratischen Terms, also f~e. Gezeigt sind die Ergebnisdarstellung des Modells (samt Code) und die vier Residualplots.

```
# Signifikantes Ergebnis visualisieren
ggplot(df, aes(x = N_deposition, y = Species_richness)) +
geom_point() +
geom_abline(intercept = lm_1$coefficients[1], slope = lm_1$coefficients[2], 
color = "blue")
```

![](_page_75_Figure_0.jpeg)

![](_page_75_Figure_1.jpeg)

Man ahnt schon im Scatterplot mit der gefitteten einfachen linearen Regression, dass das verwendete Modell für die Daten nicht adäquat ist, was durch die Bananenform im Residualplot links oben unterstrichen wird: die Beziehung ist evident nicht linear.

Wenn man einen quadratischen Term hinzufügt, also f~e + I(e^2), sieht man schon im Scatterplot mit der gefitteten Funktion, dass es viel besser passt, aber erst recht in den Residualplots. Mit

predict kann man jede Funktion plotten, die als Ergebnis einer Regressionsanalyse herauskommt. Im Prinzip zerlegt man die *x*-Achse in viele kleine Segmente und plottet dann jeweils Geraden zwischen zwei aufeinander folgenden vorhergesagten Punkten:

```
xv <- seq( min(df_2$pred), max(df_2$pred), length = 100) 
y_lm_quad <- predict(lm_quad, data.frame(pred = xv)) 
ModPred <- data.frame(xv, y_lm_quad)
ggplot(df_2, aes(x = pred, y = resp)) +
geom_point() +
geom_line(data = ModPred, aes(x = xv, y = y_lm_quad), color = "blue")
```

![](_page_76_Figure_2.jpeg)

![](_page_77_Figure_0.jpeg)

Bezüglich des statistischen Vorgehens ist zu beachten, dass man den quadratischen Term nur im Modell behalten sollte, wenn er signifikant ist. Wenn das Modell nur einen quadratischen Term beinhaltet, gibt der *p*-Wert aus summary für diesen die Signifikanz an, (ansonst ggf. mit anova testen oder mit AICc-Werten vergleichen, siehe später). Dagegen muss der lineare Term (hier: e) dann beibehalten werden, wenn der quadratische Term signifikant ist, selbst wenn der lineare Term nicht signifikant ist. (Wenn beide nicht signifikant sind, fallen dagegen beide raus).

Wenn es theoretische Gründe gibt, kann man in gleicher Weise auch Polynome höherer Ordnung implementieren. Wichtig ist, im Hinterkopf zu behalten, dass eine polynomische Regression fast immer eine deutliche Simplifizierung der Realität darstellt. Sie ist ein probates und einfaches Mittel, um zu testen, ob die Beziehung signifikant unimodal ist. Dagegen ist sie problematisch als prädiktives Modell, da sie oft negative Werte für die abhängige Variable voraussagt, zumindest ausserhalb des gefitteten Bereichs. Negative Werte sind aber vielfach theoretisch unmöglich (z. B. Artenzahlen, Stoffkonzentrationen,…).

### <span id="page-77-0"></span>**Kovarianzanalyse (ANCOVA)**

Wie wir schon bei "Lineare Modelle allgemein" in Statitik 2 gesehen haben, lassen sich metrische und kategoriale Variablen in einem einzigen linearen Modell kombinieren. Eine ANCOVA macht genau dieses, ist also im Prinzip eine Kombination aus ANOVA und linearer Regression. Stellen wir uns vor, wir hätten einen Datensatz von Körpergewichten von Kindern unterschiedlichen Alters (age: metrisch) und Geschlechts (sex: kategorial/binär, dargestellt als blau und rot). Eine ANCOVA testet nun, ob und wie sich das Gewicht in Abhängigkeit von beiden Faktoren verhält. Dabei gibt es im Prinzip sechs verschiedene Möglichkeiten/Ergebnisse, siehe [Abbildung 3.1](#page-78-0).

<span id="page-78-0"></span>![](_page_78_Figure_0.jpeg)

Abbildung 3.1: Visualisierung der sechs möglichen Ergebnisse einer ANCOVA mit einem kategorialen und einem metrischen Prädiktor. (aus Crawley 2015).

Wie andere lineare Modelle auch, kann man eine ANCOVA mittels aov oder mittels lm spezifizieren. Es ist zu beachten, dass hier die Reihenfolge der Variablen wichtig ist:

summary(aov(weight~age\*sex))

Im vollen Modell (*full model, global model*) wurden vier Parameter gefittet (2 Steigungen und 2 Achsenabschnitte). Das haben wir durch das "\*"-Zeichen spezifiziert. Dieses sagt, dass nicht nur Alter und Geschlecht unabhängig voneinander einen (additiven) Effekt haben, sondern dass der Effekt des Alters je nach Geschlecht unterschiedlich sein könnte, also die Gewichtszunahme mit zunehmendem Alter je nach Geschlecht unterschiedlich sein kann. Jedoch sind oft nicht alle gefitteten Parameter bedeutsam. Es ist daher wichtig, das Modell so lange zu vereinfachen, bis nur noch bedeutsame Parameter übrig sind. Dann hat man das minimal adäquate Modell.

Für die **Modellvereinfachung** gibt es unterschiedliche Strategien (mehr dazu später bei den "Multiplen linearen Regressionen"). Man muss jedenfalls schrittweise vorgehen, d. h. immer nur einen Parameter löschen und dann das neue Modell anschauen. Von den Parametern, welche nicht signifikant sind, könnte man z. B. zunächst den am wenigsten signifikanten löschen und dann das neue Model betrachten, usw.

Alternativ kann man auch ANOVAs zum Vergleich zweier unterschiedlich komplexer Modelle verwenden. Das klingt zunächst schräg, da wir bislang ANOVAs verwendet haben, um innerhalb eines Modelles zu sehen, ob etwa die durch die Steigung erklärte Varianz signifikant ist. Den gleichen Ansatz kann man aber auch verwenden, um zwei unterschiedlich komplexe Modelle miteinander zu vergleichen, um zu sehen, ob die durch das komplexere Modell zusätzlich erklärte Varianz signifikant ist. Wichtig ist dabei, dass das eine Modell im anderen geschachtelt ist:

anova(lm(weight ~ age + sex + age:sex), lm(weight~age+sex))

Das komplexere Modell ist jenes mit der Interaktion, das einfachere jenes ohne die Interaktion, da dort eine einheitliche Gewichtszunahme mit dem Alter angenommen wird. Wenn die ANOVA nun ein signifikantes Ergebnis liefert, heisst das, dass der zusätzliche Parameter des komplexeren Modells (die Interaktion Alter x Geschlecht) mehr erklärt als zufällig zu erwarten wäre und daher beibehalten werden sollte. Wenn die ANOVA ein nicht-signifikantes Ergebnis liefert, sollten wir uns für das einfachere Modell (jenes mit «+» statt mit «\*») entscheiden.

### <span id="page-79-0"></span>**Lineare Modelle allgemein**

### <span id="page-79-1"></span>**Was macht ein lineares Modell aus?**

Die meisten statistischen Verfahren, die wir bis zu diesem Punkt angeschaut haben, gehören zu den **linearen Modellen**. Dieser Begriff wird häufig weitgehend synonym mit "parametrischen Verfahren" verwendet, ist aber treffender. Von den bisherigen Verfahren gehören die folgenden zu den linearen Modellen:

- Pearson-Korrelation •
- *t*-Test •
- Varianzanalyse •
- Einfache lineare Regression •

Was macht nun lineare Modelle aus:

- Voraussetzungen: **Normalverteilung der Residuen und Varianzhomogenität** •
- In R kann man sie (mit Ausnahme der Pearson-Korrelation) mit dem **Befehl lm** abbilden (ja, auch die Varianzanalyse!) •

- Varianzanalysen und lineare Regressionen nutzen beide **ANOVA-Tabellen mit** *F***-ratios** als Testverfahren •
- Lineare Modelle lassen sich als **Linearkombination der Prädiktoren** schreiben, d. h.: •
  - Prädiktoren werden *nicht* als Multiplikator, Divisor oder Exponent anderer Prädiktoren verwendet ◦
  - die Beziehung muss aber *nicht zwingend linear* sein. ◦

### <span id="page-80-0"></span>**Welche Verfahren gehören zu den linearen Modellen?**

Neben den schon besprochenen einfachen Verfahren gehören auch eine ganze Reihe komplexerer Vefahren zu den linearen Modellen, die aber alle den vorstehenden Bedingungen entsprechen. Die meisten werden wir in Statistik 3 besprechen. Logan (2010: 165) hat eine recht umfassende folgende Übersicht erstellt (einschliesslich einiger Spezialfälle, die wir im Kurs nicht behandeln). Darin sind metrische Prädiktoren als x, x1 und x2 bezeichnet, kategoriale als A bzw. B. Was unter *R Model formula* steht, würde im jeweiligen Fall in die Klammern des lm-Befehls gesetzt (siehe Abbildung 2.9).

**Table 7.3** Statistical models in R. Lower case letters denote continuous numeric variables and uppercase letters denote factors. Note that the error term is always implicit.

| Effects model                                                                                          | R Model formula                               | Description                                                                                                                                   |
|--------------------------------------------------------------------------------------------------------|-----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| $y_i = \beta_0 + \beta_1 x_i$                                                                          | y ~ 1 + x<br>y ~ x                            | Simple linear regression model of y on x with intercept term included                                                                         |
| $y_i = \beta_1 x_i$                                                                                    | $y \sim 0 + x$ $y \sim -1 + x$ $y \sim x - 1$ | Simple linear regression model of y on x with intercept term excluded                                                                         |
| $y_i = \beta_0$                                                                                        | y ~ 1<br>y ~ 1 - x                            | Simple linear regression model of y against the intercept term                                                                                |
| $y_i = \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2}$                                                      | y ~ x1 + x2                                   | Multiple linear regression model of y on x1 and x2 with the intercept term included implicitly                                                |
| $y_i = \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i1}^2$                                                    | $y \sim 1 + x + I(x^2)$                       | Second order polynomial regression of $y$ on $x$                                                                                              |
|                                                                                                        | $y \sim poly(x, 2)$                           | As above, but using orthogonal polynomials                                                                                                    |
| $y_{ij} = \mu + \alpha_i$                                                                              | у ~ А                                         | Analysis of variance of y against a single factor A                                                                                           |
| $y_{ijk} = \mu + \alpha_i + \beta_j + \alpha \beta_{ij}$                                               | $y \sim A + B + A:B$<br>$y \sim A*B$          | Fully factorial analysis of variance of $_{\mathbf{Y}}$ against A and $_{\mathbf{B}}$                                                         |
| $y_{ijk} = \mu + \alpha_i + \beta_j$                                                                   | y ~ A*B - A:B                                 | Fully factorial analysis of variance of y against A and B without the interaction term (equivalent to A + B)                                  |
| $y_{ijk} = \mu + lpha_i + eta_{j(i)}$                                                                  | y ~ B %in% A<br>y ~ A/B                       | Nested analysis of variance of y against A and B nested within A                                                                              |
| $y_{ij} = \mu + \alpha_i + \beta(x_{ij} - \overline{x})$                                               | y ~ A*x<br>y ~ A/x                            | Analysis of covariance of $_{\mathbf{Y}}$ on $_{\mathbf{x}}$ at each level of $_{\mathbf{A}}$                                                 |
| $\gamma_{ijkl} = \mu + \alpha_i + \beta_{j(i)} + \gamma_k + \alpha \gamma_{ik} + \beta \gamma_{j(i)k}$ | y ~ A + Error(B) + C<br>+ A:C + B:C           | Partly nested ANOVA of y against a single between block factor (A), a single within block factor (C) and a single random blocking factor (B). |

Abbildung 2.9. Übersicht über die Vielzahl an linearen Modellen (Befehle lm, aov) in R möglich ist. Man beachte, dass in der R-Syntax «/» und «\*» nicht für Divisionen oder Multiplikationen steht, sondern für Schachtelungen bzw. den Einschluss von Interaktionen.

### <span id="page-82-0"></span>**Testen der Voraussetzungen von linearen Modellen (Modelldiagnostik)**

Wie geschrieben, haben lineare Modelle bestimmte Voraussetzungen. Selbst wenn lineare Modelle recht robust gegen Verletzungen der Vorassetzungen sind, so muss man doch jedes Mal, nachdem man ein lineares Modell gerechnet hat, prüfen, ob die Voraussetzungen erfüllt waren. Es geht hier primär um die Voraussetzungen Varianzhomogenität, Normalverteilung der Residuen und Linearität.

Wichtig ist, zu verstehen, dass man zunächst das lineare Modell rechnen muss und erst nachträglich prüfen kann, ob die Voraussetzungen erfüllt waren. Das liegt daran, dass die Kernannahmen Varianzhomogenität und Normalverteilung der Residuen sich auf das Modell, nicht auf die Originaldaten beziehen. Einzig für *t-*Tests und ANOVAs kann man diese beiden Punkte auch in der explorativen Datenanalyse vor dem Berechnen des Modells erkunden, für lineare Regressionen und komplexere Modelle geht das nicht. Wenn der nachträgliche Test zeigt, dass eine der Voraussetzungen schwerwiegend verletzt war, bedeutet das, dass man das Modell neu spezifizieren muss, etwa durch eine geeignete Transformation der abhängigen Variablen.

Das **Überprüfen der Voraussetzungen (= Modelldiagnostik)** erfolgt visuell mittels der sogenannten Residualplots, die man mit dem generische plot-Befehl bekommt, wenn man als Argument das Ergebnis eines linearen Modells hat. Man bekommt dann vier Plots, die man am besten in einem 2 x 2-Arrangement ausgibt (das macht der erste Befehl):

par(mfrow = c(2, 2)) # 4 Plots in einem Fenster plot(lm)

Betrachten wir zwei Fälle, zunächst das Beispiel von eben:

![](_page_83_Figure_0.jpeg)

und die zugehörigen Residualplots:

![](_page_84_Figure_0.jpeg)

In diesem Fall ist **alles OK**. Man muss vor allem die oberen beiden Teilabbildungen betrachten. Links oben kann man gut erkennen, wenn Linearität oder Varianzhomogenität verletzt wären, rechts oben dagegen, wenn die Normalverteilung der Residuen verletzt wäre. Zu berücksichtigen ist, dass reale Daten nie perfekt linear, varianzhomogen und normalverteilt sind.

Uns interessieren nur **massive Abweichungen**. Wir würden sie wie folgt erkennen:

- **Linearität:** Eine Verletzung erkennen wir in der linken oberen Abbildung, wenn wir eine **"Wurst" bzw. "Banane"** sehen, also wenn die linken Punkte alle unter der gepunktelten Linie, die mittleren alle darüber und die rechten wieder alle darunter lägen (oder umgekehrt). •
- **Varianzhomogenität:** Eine Verletzung erkennen wir in der linken oberen Abbildung, wenn die Punktwolke einen starken **Keil** (meist nach rechts offen) beschreibt. •
- **Normalverteilung der Residuen:** Eine Verletzung erkennen wir in der rechten oberen Abbildung, wenn die Punkte sehr stark von der gestrichelten Linie abweichen, insbesondere wenn sie eine ausgeprägte **Treppenkurve** bilden. •

Die beiden unteren Abbildungen sind für die Diagnostik weniger wichtig. Links unten haben wir eine skalierte Version der Abbildung links oben. Die Abbildung rechts unten zeigt uns, ob bestimmte Datenpunkte übermässigen Einfluss auf das Gesamtergebnis haben. Das wären Punkte mit einer *Cook's distance* über 0.5 und insbesondere über 1. In solchen Fällen sollten wir noch einmal kritisch prüfen, ob (a) evtl. ein Eingabefehler vorliegt und (b) der bezeichnete Punkt wirklich zur

Grundgesamtheit gerechnet werden sollte. Wenn aber beide Aspekte nicht zu beanstanden sind, dann gibt es auch keinen Grund, den entsprechenden Datenpunkt auszuschliessen; wir müssen uns nur bewusst sein, dass er das Gesamtergebnis überproportional beeinflusst.

![](_page_86_Figure_0.jpeg)

![](_page_87_Figure_0.jpeg)

Zum Schluss kommt noch ein Beispiel, bei dem die Modellvoraussetzungen einer linearen Regression klar nicht erfüllt sind (Abbildung 2.10): (a) es liegt starke **Varianzinhomogenität** vor (links oben als nach rechts offener Keil erkennbar, links unten als klar ansteigende Kurve); (b) die **Normalverteilung der Residuen ist auch nicht gegeben** (im Q-Q-Plot rechts oben weichen die Punkte stark von der theoretischen Kurve ab und bilden stattdessen eine Treppenkurve). Schliesslich sehen wir rechte unten auch noch, dass es einen extrem **einflussreichen Datenpunkt** mit *Cook's distance* > 1 und einen weiteren mit *Cook's distance* > 0.5 gibt.

In diesem Fall schlussfolgern wir, dass das **Modell fehlspezifiziert** war. Da die Varianz mit dem Mittelwert zunimmt, während zugleich keine Null-Werte unter der abhängigen Variablen auftreten, wäre eine Logarithmus-Transformation der abhängigen Variablen hier vermutlich ein zielführendes Vorgehen. Dieses sollten wir ausprobieren und anschliessend wiederum die Residualplots betrachten.

# <span id="page-88-0"></span>**Genereller Ablauf einer statistischen Analyse**

Abschliessend sei der generellen Ablauf einer statistischen Analyse noch einmal schematisch zusammengefasst,, wie er für alle schon besprochenen und auch alle noch kommenden Verfahren gilt:

![](_page_88_Figure_2.jpeg)

Ein zentrales Element ist die Modelldiagnostik, die wir gerade behandelt behandelt haben. Leider wird sie oft vergessen! Basierend auf den Ergebnissen der Modelldiagnostik kann man entweder die Ergebnisse fertigstellen oder aber man muss zu den initialen Schritten zurückgehen. Möglicherweise war das gewählte statistische Verfahren schon nicht adäquat oder das Verfahren war in Ordnung, nur die Details der Spezifizierung (etwa Transformationen von Daten) müssen nachgebessert werden.

## <span id="page-88-1"></span>**Zusammenfassung**

- **Korrelationen** testen auf einen linearen Zusammenhang zwischen zwei metrischen Variablen, **ohne Kausalität anzunehmen.** •
- Einfache **lineare Regressionen** machen das Gleiche unter Annahme eines **gerichteten Zusammenhangs** (d. h. wenn es eine unabhängige und eine abhängige Variable gibt). •
- Sowohl lineare Regressionen als auch ANOVAs gehören zu den **linearen Modellen** und können in R mit dem **Befehl lm** spezifiziert werden. •
- Ob eine bestimmte statistische Analyse zulässig war, kann man oft erst nach der Durchführung anhand der Residualplots/Diagnostikplots entscheiden. Wenn sich dabei zeigt, dass Voraussetzungen schwerwiegend verletzt wurden, muss man die Modellspezifikationen ändern. •

# <span id="page-89-0"></span>**Weiterführende Literatur**

- **Crawley, M.J. 2015.** *Statistics An introduction using R***. 2nd ed. John Wiley & Sons, Chichester, UK: 339 pp.** •
  - **Chapter 7 Regression: pp. 114–139** ◦
  - **Chapter 8 Analysis of Variance: pp. 150–167** ◦
- Fox, J. & Weisberg, S. 2019. *An R companion to applied regression*. 3rd ed. SAGE Publications, Thousand Oaks, CA, US: 577 pp. •
- Logan, M. 2010. *Biostatistical design and analysis using R. A practical guide*. Wiley-Blackwell, Oxford, UK: 546 pp. •
  - pp. 151-166 (lineare Modelle) ◦
  - pp. 167-207 (Korrelation und einfache lineare Regression) ◦
- Quinn, G.P. & Keough, M.J. 2002. *Experimental design and data analysis for biologists*. Cambridge University Press, Cambridge, UK: 537 pp. •
- Warton, D.I. & Hui, F.K.C. 2011. The arcsine is asinine: the analysis of proportions in ecology. *Ecology* 92: 3–10. •
- Wilson, J.B. 2007. Priorities in statistics, the sensitive feet of elephants, and don't transform data. *Folia Geobotanica* 42: 161–167. •

# <span id="page-89-1"></span>**Statistik 4**

Multiple lineare Regressionen und "Multimodel Inference"

**In Statistik 4 geht es um multiple Regressionen, die versuchen, eine abhängige Variable durch zwei oder mehr verschieden Prädiktorvariablen zu erklären. Wir thematisieren verschiedene dabei auftretende Probleme und ihre Lösung, insbesondere den Umgang mit korrelierten Prädiktoren und das Aufspüren des besten unter mehreren möglichen statistischen Modellen. Hieran wird auch der** *informatian theoretician***-Ansatz der Statistik und die** *multimodel inference* **eingeführt.**

# <span id="page-89-2"></span>**Lernziele**

#### Ihr…

- könnt **lineare Regressionen mit mehreren Prädiktoren** in R implementieren und wisst, welche Aspekte ihr bei der Modellspezifikation und bei der Auswahl des "besten" Modells beachten müsst; •
- wisst, warum **Kolinearität von Prädiktoren** in multiplen Regressionen ein Problem ist und wie ihr es lösen könnt; und •
- kennt die Gütemasse des *information theoretician approach* und könnt sie interpretieren. •

### <span id="page-90-0"></span>Multiple lineare Regressionen

### <span id="page-90-1"></span>Vorgehen

Analog zur mehrfaktoriellen ANOVA, sind multiple lineare Regressionen lineare Regressionen mit mehreren Prädiktoren. Das statistische Modell lautet also folgendermassen (wobei  $x_1 \dots x_j$  metrische Variablen sind):

In R wird das wie folgt codiert:

```
model1 <- lm(y \sim x1 + x2 + x3, data = mydata)
```

Möglich sind aber auch folgende komplexere Modelle:

```
model2 <- lm(y \sim x1 + x2 + I(x2^2), data = mydata)
model3 <- lm(y \sim x1 + x2 + log10(x3), data = mydata)
model4 <- lm(y \sim x1 + x2 + x1:x2, data = mydata)
```

Und für ein konkretes Beispiel (Abhängigkeit der Vogelabundanz in isolierten Waldinseln von verschiedenen Umweltvariablen (AREA = Fläche, AGE = Alter, DIST = Entfernung zum nächsten Waldstück, LDIST = Entfernung bis zum nächsten grösseren Waldstück, GRAZE = Beweidungsintensität, ALT = Meereshöhe):

```
Im_1 <- Im(ABUND ~ AGE + AREA + DIST + LDIST + GRAZE + ALT, data = loyn)
summary(Im_1)</pre>
```

Coefficients:

Estimate Std. Error t value Pr(>|t|)

(Intercept) 1.749e+01 6.599e+00 2.650 0.0109 \*

AGE -9.155e-02 5.430e-02 -1.686 0.0985.

AREA 1.232e-01 4.173e-02 2.953 0.0049 \*\*

DIST 3.751e-03 5.083e-03 0.738 0.4642

LDIST -5.331e-05 1.335e-03 -0.040 0.9683

GRAZE -1.783e+00 1.181e+00 -1.510 0.1378

ALT 4.731e-02 2.900e-02 1.631 0.1095

Und wie immer schauen wir die Residualplots an, die eigentlich ziemlich gut aussehen:

```
par(mfrow=c(2, 2))
plot(lm_1)
```

![](_page_91_Figure_0.jpeg)

Allerdings dürfen wir uns hier im Falle einer multiplen Regression noch nicht zufrieden zurücklehnen, sondern müssen uns zunächst noch zwei potenziellen Problemen annehmen: (1) Korrelation zwischen den Prädiktoren und (2) Overfitting.

### <span id="page-91-0"></span>**Problem 1: Korrelation zwischen den Prädiktoren**

Damit lm verlässliche Parameterschätzungen liefern kann, müssen die Prädiktoren (hinreichend) **unabhängig** (man spricht auch von: orthogonal) sein. Das muss man vor dem Fitten des Models testen und dann von Paaren hochkorrelierter Variablen jeweils eine ausschliessen.

Es gibt zwei gängige Testmöglichkeiten:

- **Korrelationmatrix:** nur Parameter mit einem Korrelationskoeffizenten von **| r| < 0.7** werden beibehalten (manchmal findet man auch andere Schwellenwerte, etwa 0.6 oder 0.75: wie eigentlich alles in der Statistik, ist es keine Schwarz-weiss-Welt). 1.
- *Variance inflation factor* **(VIF):** , mit aus dem Modell Prädiktor *i* gegen alle übrigen Prädiktoren 2.

Der VIF sagt uns, dass der Standardfehler (SE) des Prädiktors um grösser ist als im orthogonalen Fall. Oder in anderen Worten: je höher der VIF eines Prädiktors, desto problematischer ist seine Schätzung wegen der Korrelationen mit anderen Prädiktoren. Meist werden Variablen bis , manchmal bis akzeptiert.

Die Berechnung der Korrelationsmatrix geht in R sehr einfach (hier für den Datensatz loyn):

cor <- cor(loyn[, 2:7])

cor

Das Ergebnis ist allerdings unübersichtlich. Man kann es vereinfachen, indem man die Nachkommastellen reduziert und nur jene Werte darstellt, die über dem selbstgewählten Schwellenwert (hier 0.6) liegen.

cor[abs(cor)<0.6] <- NA cor

AREA AGE DIST LDIST GRAZE ALT

AREA 1 NA NA NA NA NA

AGE NA 1.000 NA NA 0.661 NA

DIST NA NA 1 NA NA NA

LDIST NA NA NA 1 NA NA

GRAZE NA 0.661 NA NA 1.000 NA

ALT NA NA NA NA NA 1

Keine der Variablen ist mit einer anderen mit |*r*| ≥ 0.7 korreliert. Nach gängigem Verständnis könnten wir also alle sechs im vollen Modell behalten. Wenn man die Schwelle bei 0.6 ansetzen würde, müsste man also von den beiden Variablen GRAZE und AGE eine aus dem Modell entfernen, da sie relativ stark positiv korreliert sind. Dabei sind drei Dinge wichtig:

- Statistisch gibt es kein klares Argument, welche von mehreren hochkorrelierten Variablen man im vollen Modell streichen sollte (man könnte höchstens zusätzlich den VIF heranziehen). Inhaltlich macht es Sinn, diejenige Variable beizubehalten, die (a) besser interpretierbar ist oder (b) häufiger in vergleichbaren Studien gebraucht wurde. •
- Man sollte im Methodenteil dokumentieren welche Variable(n) wegen positiver/negativer Korrelation mit welcher anderen aus dem vollen Modell gestrichen wurden. •
- Bei der Interpretation der Ergebnisse stehen die beibehaltenen Variablen auch für die jeweils gestrichenen hochkorrelierten Variablen (zumindest zu einem erheblichen Teil). •

Die Berechnung der VIF's (Variance inflation factors) geht wie folgt:

library(car) vif(lm\_1)

AGE AREA DIST LDIST GRAZE ALT

1.874993 1.763605 1.220125 1.465810 2.784577 1.346572

Hier sieht man nicht, welche Variable mit welcher anderen korreliert ist, man bekommt nur ein Gesamtranking. Da die VIF-Werte allersechs Variablen unter 5 sind, können alle beibehalten werden. Wenn mehrere Variablen einen VIF > 5 haben, muss man schrittweise immer die Variable mit dem höchsten VIF-Wert entfernen und die VIF-Werte dann neuberechnen. Sie ändern sich, wenn eine Variable wegfällt, da sie die Gesamt-Korrelationsstruktur des Datensatzes widerspiegeln.

### <span id="page-93-0"></span>**Problem 2: Overfitting**

Das Problem des Overfitting soll mit der folgenden Simulation veranschaulicht werden: zu einer Stichprobe von sechs Beobachtungen mit zwei numerischen Variablen werden schrittweise polynomische Modelle höher Ordnung gefittet.

<span id="page-93-2"></span><span id="page-93-1"></span>![](_page_93_Figure_3.jpeg)

![](_page_94_Figure_0.jpeg)

Abbildung 3.3: Overfitting. Die Simulation zeigt, dass die Anpassung des Models an die Daten immer besser wird, je komplexer ich das Modell mache (R2 steigt), in diesem Fall mit der Hinzunahme höherer Polynome.

Das Ergebnis ist in [Abbildung 3.2](#page-93-1) und [Abbildung 3.3](#page-93-2) ersichtlich. Wir sehen, dass die erklärte Varianz kontinuierlich vom 2-Parameter-Modell (Achsenabschnitt und Steigung) zum 6-Parameter-Modell (Achsenabschnitt, Parameter für bis ) zunimmt. Ein polynomisches Modell ()-ter Ordnung erzielt immer 100% Anpassung and die Daten (), wenn man Beobachtungen hat. Aber ist das Modell deswegen auch besonders korrekt oder aussagekräftig? Das darf bezweifelt werden. Ein gutes Modell wäre ja eines, welches die zugrunde liegende Gesetzmässigkeit erkennt und daher auch für die Interpolation und Extrapolation geeignet ist.

Es zeigt sich, dass die gute Anpassung an die Daten (good fit, hier gemessen als R2) nur der eine Aspekt eines guten Modells ist. Zugleich sollte es möglichst einfach (*parsimonous*) sein, d. h. das Beobachtete mit möglichst wenigen Annahmen erklären. Es gilt das folgende Prinzip, das auf den mittelalterlichen Philosophen Willliam of Ockham (ca. 1288–1347 zurückgeht).

![](_page_95_Picture_0.jpeg)

(Skizze aus einer Handschrift von Ockhams Summa logicae)

Ockham's razor = *Law of parsimony* (Sparsamkeitsprinzip)

*Wesenheiten dürfen nicht über das Notwendige hinaus vermehrt werden*

Formulierung von Johannes Clauberg (1622–1665)

### <span id="page-95-0"></span>**Modellvereinfachung**

Nun stellt sich die Frage, wie wir vom **vollen Modell (***full model, global model***)** also jenem nach Entfernung hochkorrelierter Variablen zum "besten" Modell gelangt, das also eine bestmögliche Kombination von guter Anpassung an die Daten (Fit) und Parsimonie aufweist. Dieses anzustrebende statistische Modell wird auch **minimal adäquates Modell (***minimum adequate model***)** genannt.

Ganz generell gilt: Man sollte **maximal Parameter fitten, besser nur** (wobei *n* = Zahl der Datenpunkte/Beobachtungen und bei auch der Achsenabschnitt [] mitgezählt wird).

Mögliche **Kriterien für das "beste" Modell** (*minimum adequate model*):

- **Höchster** (vgl. ) 1.
- Ist nicht wirklich zielführend, da der "Strafterm" (um den reduziert wird) zu gering ist, um wirklich für Parsimonität zu sorgen, trotzdem sehr gebräuchlich. •
- **Schrittweise Modellvereinfachung ausgehend vom "maximalen Modell"** 1.
- Durch: Entfernen von (a) nicht-signifikanten Interaktionen, (b) nichtsignifikanten quadratischen Termen und schliesslich (c) nicht-signifikanten linearen Variablen. •

Die schrittweise Modellvereinfachung kann wiederum auf drei verschiedene Weisen geschehen (die meist, aber nicht immer, die gleichen Ergebnisse liefern):

- **Schrittweise die am wenigsten signifikanten Terme entfernen**, bis alle signifikant sind: 1.
- **Mittels** *likelihood ratio***-Test schrittweise Modelle vergleichen** und Terme hinzufügen, wenn signifikant, bzw. entfernen, wenn nicht 2.

```
lm_1 <- lm(ABUND ~ AGE + AREA + DIST + LDIST + GRAZE + ALT, data = loyn)
drop1(lm_1, test = "F")
lm_2 <- update(lm_1, ~ . - LDIST)
drop1(lm_2, test = "F")
```

Eine **automatische Funktion** zum schrittweisen Hinzufügen (*forward selection*) oder Löschen (*backward selection*) oder beidem verwenden (funktion «step»). 1.

Varianten a bis c sind im Prinzip OK, man muss sich aber bewusst sein, dass gerade bei vielen Variablen dieses schrittweise Vorgehen nicht zwingend das wirklich beste Modell findet, sondern man in einem "lokalen Optimum" landen kann (als Alternative siehe die dredge-Funktion unter "*Information theoretician approach* und *multimodel inference*" weiter unten).

### <span id="page-96-0"></span>**Varianzpartitionierung**

Wenn man das minimal adäquate Modell gefunden hat, will man oft noch wissen, wie bedeutsam die einzelnen enthaltenen Variablen sind. Bedeutsamkeit/Relevanz haben wir weiter oben als (erklärte Varianz) ausgedrückt. Wir können uns also anschauen, **welche Anteile der erklärten Varianz auf welche Variablen zurückgehen**. Da Variablen (auch nach einem Korrelationstest und Ausschluss der besonders hoch korrelierten) nie völlig orthogonal = unabhängig voneinander sind, verhalten sich die Varianzen nicht additiv. Vielmehr ist die erklärte Varianz in einem Modell mit zwei Variablen meist niedriger als die Summe der Varianzen der beiden Einzelmodelle. In einer Varianzpartitionierung wird die Varianz jeder Variablen daher in eine unabhängige (*independent*, I) und eine gemeinsame (*joint*, J) Komponente zerlegt:

library(relaimpo)

```
lm_1 <- lm(ABUND~YR.ISOL+ AREA + DIST + LDIST + GRAZE + ALT, data = loyn)
metrics <- calc.relimp(lm_1, type = c("lmg", "first"))
cbind(I = metrics$lmg, 
J = metrics$first - metrics$lmg, Total = metrics$first)
```

I J Total

AGE 0.11351597 0.1539730784 0.267489048

AREA 0.17941694 0.1596031200 0.339020063

DIST 0.01986977 0.0307746481 0.050644413

LDIST 0.00827103 -0.0007561283 0.007514902

GRAZE 0.19052943 0.2548693094 0.445398737

ALT 0.06061495 0.0610176713 0.121632624

Der grösste Teil der Varianz wird in diesem Sechs-Parameter-Modell daher durch die Variable "grazing" erklärt. Wenn den Wert für GRAZE in der Spalte I in Relation zur Summe aller Werte in I setzt, also 0.1905 / 0.5722 erhält man 0.3768; mithin werden gut ein Drittel der «unabhängigen Varianzanteile» durch "grazing" erkärt.

### <span id="page-97-0"></span>**Ergebnisdarstellung: partielle Regressionen und 3-D-Grafiken**

Während sich die ermittelte Beziehung zwischen Antwort- und Prädiktor-Variable auch bei nichtlinearen Verläufen einfach mit predict visualisieren lässt, solange man nur eine Prädiktorvariable hat (selbst wenn sie in transformierter Weise im lm eingespeist wird), ist das bei mehreren Prädiktoren eine Herausforderung. Hier seien zwei Möglichkeiten kurz erwähnt:

- **Partielle Regressionen** (sie zeigen, wie die Beziehung aussähe, wenn alle übrigen Faktoren konstant wären 1.
- library(car) avPlots(lm\_5, layout = c(1, 2)) •

![](_page_98_Figure_1.jpeg)

**3D Response surfaces** (es gibt Packages, um dasselbe auch für zwei Prädiktoren gleichzeitig zu machen; dies mach insbesondere Sinn, wenn auch quadratische Terme dabei sind; bei Interesse bitte googlen) 1.

# <span id="page-98-0"></span>*Information theoretician approach* **und** *multimodel inference*

### <span id="page-98-1"></span>**Vergleich mit** *frequentist statistics*

Es gibt zwei grundlegende statistische Philosophien:

#### *Frequentist statistics* **("klassische" Statistik)**

- Alles, was wir bislang gemacht haben •
- *Grundannahme:* Es gibt ein einziges richtiges Modell der Wirklichkeit, dem man sich mit Irrtumswahrscheinlichkeitenannähern kann •
- Nutzt *p***-Werte** •

•

#### *Information theoretician approach*

- Das, was wir in diesem Unterkapitel besprechen •
- *Grundannahme:* Es kann ähnlich gute Modelle der Wirklichkeit geben, es gibt nicht das eine wahre Modell •

- Nutzt **keine** *p***-Werte** •
- Dafür **AIC** (*Akaike information criterion*) oder **BIC** (*Bayesian information criterion*) •
- **Modellmittelung** (*model averaging*) möglich •

### <span id="page-99-0"></span>**Masse der Modellgüte: AIC, BIC, AICc, ,** *Evidence ratios***,** *Akaike weights*

Die folgende Übersicht zeigt die wichtigsten Gütemasse im Vergleich. Wie schon besprochen, berücksichtigt (nahezu) ausschliesslich den Fit (also die Anpassung der Kurve an die Daten). Dagegen berücksichtigen die Informationskriterien Fit und Komplexität (Komplexität meint das Gegenteil von Parsimonität). Bei AICc und BIC = SC fliesst schliesslich auch noch die Zahl der Datenpunkte ein:

| Model selection method                        | Calculation <sup>a</sup>                                                         | Elements                                                             | Refs |
|-----------------------------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------|------|
| Adjusted R <sup>2</sup>                       | $R_{adj}^2 = 1 - \frac{RSS/n - p - 1}{\sum (y_i - \bar{y})^2/n - 1}$             | Fit                                                                  | [7]  |
| Likelihood ratio test                         | $LRT = -2\{ln[L(\hat{\theta}_p y] - ln[L(\hat{\theta}_{p+q} y)]\} \sim \chi_q^2$ | Fit and complexity                                                   | [7]  |
| Akaike information criterion (AIC)            | $AIC = -2ln[L(\hat{\theta}_p y] + 2p$                                            | Fit and complexity                                                   | [3]  |
| Small sample unbiased AIC (AIC <sub>c</sub> ) | $AIC_c = -2ln[L(\hat{\theta_p} y)] + 2p\left(\frac{n}{n-p-1}\right)$             | Fit and complexity (with bias correction term for small sample size) | [3]  |
| Schwarz criterion                             | $SC = -2\ln[L(\hat{\theta}_p y] + p \cdot \ln(n)$                                | Fit, complexity, and sample size                                     | [10] |

(aus Johnson & Omland 2004)

Dabei gilt für AIC:

mit:

- RSS = Residual sum of squares •
- *k* = Parameter des Models, inkl. Achsenabschnitt •
- *n* = Anzahl der Beobachtungen/Replikate •

**AICc ist das AIC für "kleine" Stichprobengrössen** (wobei "klein" bis zu 40 *k* reicht, also bei 2 Parametern wie in einer einfachen linearen Regression "gross" erst bei n = 81 Datenpunkten begänne). Deshalb und da sich für grosses *n* AICc asymptotisch AIC nähert, sollte man einfach immer AICc verwenden.

AIC und BIC entstammen wiederum etwas unterschiedlichen Philosophien. Auf die Unterschiede gehen wir nicht im Detail ein. Die Ergebnisse basierend auf BIC und AICc sind in dem Kontext wie wir sie hier vorstellen (BIC mit nicht-informativen *priors*) nahezu gleich. BIC wird relevant, wenn man informative *priors* verwenden kann (aber das sprengt den Kurs).

Es gilt folgendes für AIC, AICc und BIC analog:

Der **absolute Wert eines Informationskriteriums ist belanglos** (ob also -1000, 0.1 oder +1'000'000). Informationskriterien können nur im Vergleich zweier Modelle für die gleichen Daten sinnvoll angewandt werden. Dann ist •

das **Modell mit dem niedrigeren Wert das bessere** hinsichtlich Fit und Komplexität.

- ist die Differenz im AIC (oder eines anderen Informationskriteriums) zwischen einem bestimmten Modell i und dem jeweils besten Modell im Vergleich. Dabei wird meist die folgende Konvention verfolgt: •
  - wenn : Modelle sind statistisch "gleichwertig" ◦
  - wenn : Modell mit dem höheren Wert ist statistisch nicht relevant ◦
- *Likelihood* von Modell für die Daten (je grösser, desto besser): •
- *Evidence ratio***:** (etwa: wie vielfach besser ist das beste Modell verglichen mit Modell *i*? – je grösser, desto besser) •
- *Akaike weights***:** Normalisierte *Likelihoods* über alle verglichenen Modelle: •

, Likelihood, ER und Akaike weights stehen alle für die gleiche Information (statistische Eignung bezüglich Fit und Komplexität) in verschiedenen Darstellungen/Transformationen. Als besonders praktisch erweisen sich die **Akaike weights** . Nach ihrer Definition summieren sich die Akaike weights aller verglichenen Modelle zu 1. kann daher als die Wahrscheinlichkeit interpretiert werden, dass Modell unter den verglichenen Modellen das beste ist.

Da AIC und *p*-Werte aus verschiedenen und nicht kompatiblen statistischen Philosophien stammen, sollte man in einer mit Informationskriterien arbeitenden Studie nicht zusätzlich auch noch *p*-Werte angeben. -Werte sind dagegen in beiden "statistischen Welten" sinnvoll und wichtig.

### <span id="page-100-0"></span>*Multimodel inference*

Der Charme der Informationskriterien ist, dass sie sich besonders gut dann eignen, wenn man viele verschiedene Modelle vergleicht, etwa weil man viele potenziellen Prädiktoren erhoben hat, mit denen man eine abhängige Variable erklären will, etwas in einer multiplen Regression oder einer mehrfaktoriellen ANOVA oder einem sonstigen komplexen Modell. Denn die Anzahl aller möglichen Modellen steigt exponentiell mit der Anzahl berücksichtigten Terme. Wenn man sich ein globales Modell mit *n* Termen (Achsenabschnitt und n – 1 Steigungen (estimates) für Prädiktorvariablen, transformierte Prädiktorvariablen oder Interaktionen *zwischen* Prädiktorvariablen) vorstellt,

beinhaltet das 2*<sup>n</sup>* Einzelmodelle für alle möglichen Kombinationen der Terme von 0 bis *n* Prädiktoren. Bei *n* = 10 wären das bereits 1024 verschiedene Modelle. Diese alle zu berechnen ist ein grosser Aufwand, weswegen man früher versucht hat, in solchen Fällen das minimal adäquate Modell in einer weniger rechenaufwändigen Weise zu finden, indem man eine *stepwise forward/ backward variable selection* durchgeführt hat (siehe Kapitel "Modellvereinfachung" oben). Heute ist das Ausrechnen von 1000 Modellen selbst auf einem einfachen Notebook nur noch eine Sache von Sekunden, d. h. man kann seine Entscheidung effektiv auf dem Vergleich aller mit den verfügbaren Variablen möglichen Teilmodelle gründen. Die dredge-Funktion im MuMIn-Paket macht genau dieses. Bis etwa 15 Terme (d. h. 32768 zu vergleichende Modelle) funktioniert dredge auch auf einfachen Notebooks noch im Bereich weniger Minuten (aber man muss schon merklich auf das Ergebnis warten); jeder weitere Term führt aber zu einer Verdopplung der Rechenzeit.

Schauen wir uns das anhand des schon bekannten loyn-Datensatzes (Vogelvorkommen in Waldfragmenten) an:

```
library(MuMIn)
global_model <- lm(ABUND ~ AGE + AREA + DIST + LDIST + GRAZE + ALT, data = loyn)
options(na.action="na.fail")
allmodels <- dredge(global_model)
allmodels
```

Model selection table

(Intrc) AGE ALT AREA DIST GRAZE LDIST df logLik AICc delta weight

24 19.460 -0.09049 0.04249 0.1257 -1.954 6 -181.648 377.1 0.00 0.127

22 27.250 -0.09295 0.1187 -2.434 5 -183.025 377.3 0.22 0.114

23 20.180 0.04379 0.1120 -3.172 5 -183.186 377.6 0.54 0.097

8 13.020 -0.14830 0.05448 0.1607 5 -183.224 377.7 0.61 0.093

21 28.230 0.1045 -3.701 4 -184.568 378.0 0.87 0.082

16 10.990 -0.14310 0.06018 0.1522 0.005130 6 -182.621 379.0 1.95 0.048

32 17.440 -0.09167 0.04764 0.1226 0.003705 -1.787 7 -181.328 379.1 2.01 0.046

31 18.300 0.04861 0.1090 0.003463 -3.031 6 -182.922 379.6 2.55 0.035

[…]

Wie man sieht, wurde hier zunächst ein globales Modell mit den sechs Prädiktoren AGE, ALT, AREA, DIST, GRAZE und LDIST gerechnet. Im nächsten Schritt wurde dann mit der dredge-Funktion dann ein Objekt allmodels generiert, das die 2<sup>6</sup> = 64 möglichen Teilmodelle enthält. In der Tabellenausgabe sieht man, dass unter diesen Modell Nr. 24, das den Achsenabschnitt und die Prädiktoren AGE, ALT, AREA und GRAZE enthält mit einem *Akaike weight* von 0.127 das beste Modell ist. Allerdings unterscheiden sich die besten sieben Modelle um weniger als 2 AICc-Einheiten, sind also als praktisch gleichwertig zu betrachten.

Anders als bei der *frequentist statistician*-Ansatz geht es nicht darum, ein einziges bestes Modell zu finden, sondern eine Aussage über ein Ensemble von plausiblen Modellen zu treffen. Es gibt hier zwei gängige Vorgehensweisen, um die Ergebnisse in solch einem Fall (also mehrere Modelle innerhalb von delta-AIC < 2) zu synthetisieren: *Variable importance* und *Model averaging*.

*Variable importance* steht dabei für die Summe der *Akaike weights* () aller Teilmodelle, die eine bestimmte Variable enthalten. Da selbst von 0 bis 1 reicht, gilt dies auch für die Variable importance. Eine Variable importance von 1 bedeutet dabei, dass alle plausiblen Modelle die entsprechende Variable beinhalten. Mithin sagt uns die Variable importance wie bedeutsam eine bestimmte Variable innerhalb der Menge der verglichenen Teilmodelle ist. Aber Achtung: *Variable importance* hat nichts mit Signifikanz oder *p*-Werten zu tun! Es gibt keine generelle Konvention, ab welcher *Variable importance* eine Variable als bedeutsam angesehen wird, aber häufig wird 50 % als Schwelle verwendet. In R geht das folgendermassen (sw steht für *sum of weights*):

sw(allmodels)

AREA GRAZE AGE ALT DIST LDIST

Sum of weights: 0.97 0.76 0.66 0.58 0.27 0.23

N containing models: 32 32 32 32 32 32

Während logischerweise jede der sechs Variablen in jeweils 32 Teilmodellen vorkommt, unterscheiden sie sich erheblich in der *Variable importance*. So liegt die *Variable importance* von GRAZE nahe 1, während jene von DIST und LDIST unter 0.5 liegt.

*Model averaging* ist eine andere interessante Möglichkeit des *Information theoretician*-Ansatzes und der Multimodel inference. Hier werden quasi alle möglichen Modelle (oder alle Modelle mit einem

unter einem bestimmten Schwellenwert) zu einem gemittelten Modell zusammengefasst, gewichtet nach ihrem *W<sup>i</sup>* -Wert. Am Ende bekommt man eine einzige gemittelte Funktion, deren

avgmodel <- model.avg(allmodels)

summary(avgmodel)

(full average)

Estimate Std. Error Adjusted SE z value Pr(>|z|)

(Intercept) 2.125e+01 7.540e+00 7.618e+00 2.790 0.00528 \*\*

Funktionsparameter man interpretieren und die man plotten kann.

AGE -7.527e-02 7.177e-02 7.236e-02 1.040 0.29823

ALT 2.811e-02 3.196e-02 3.231e-02 0.870 0.38427

AREA 1.235e-01 4.745e-02 4.818e-02 2.564 0.01035 \*

GRAZE -2.080e+00 1.621e+00 1.633e+00 1.273 0.20292

DIST 9.132e-04 3.061e-03 3.117e-03 0.293 0.76950

LDIST -4.925e-05 6.691e-04 6.839e-04 0.072 0.94259

Man beachte, dass der Output auch einen *p*-Wert enthält, obwohl dieser im AIC-Kontext nicht sinnvoll ist.

### <span id="page-102-0"></span>**Zusammenfassung**

#### **Zusammenfassung**

- **Multiple Regressionen** sind lineare Regressionen mit mehreren Prädiktoren. •
- Bei multiplen Regressionen muss man die **weitgehende Unabhängigkeit** der ins globale Modell eingespeisten Variablen sicherstellen. •
- Für die Suche nach dem **minimalen adäquaten Modell** kommen unterschiedliche Strategien infrage, wie die schrittweise Entfernung nicht-signifikanter Terme aus dem globalen Modell oder Auswahl des besten Modells aus allen möglichen Modellen mittels AICc. •
- **AICc** ist ein Gütemass im *information theoretician approach*. AICc-Werte sind nur im Vergleich mit anderen AICc-Werten für die gleichen Daten informativ; dann bezeichnet der niedrigste AICc-Wert das beste Modell. •
- "*Frequentist approach*" ("Standardstatistik") und "*information theoretician approach*" sind **zwei verschiedene statistische "Philosophien"**, die man nicht in ein und derselben Auswertung kombinieren sollte: also entweder *p*-Werte oder AICc-Werte; macht dagegen in beiden "Welten" Sinn. •

## <span id="page-103-0"></span>**Weiterführende Literatur**

- **Crawley, M.J. 2015.** *Statistics An introduction using R***. 2nd ed. John Wiley & Sons, Chichester, UK: 339 pp.** •
  - **Chapter 7: Regression (pp. 140–141)** ◦
  - **Chapter 9: Analysis of Covariance** ◦
  - **Chapter 10: Multiple Regression** ◦
  - **Chapter 12: Other Response Variables (p. 233 [AIC])** ◦
- Burnham, K.P. & Anderson, D.R. 2002. *Model selection and multimodel inference – a practical information-theoretic approach*. 2nd ed. Springer, New York, US: 488 pp. •
- Johnson, J.B. & Omland, K.S. 2004. Model selection in ecology and evolution. *Trends in Ecology and Evolution* 19: 101–108. •
- Logan, M. 2010. *Biostatistical design and analysis using R. A practical guide*. Wiley-Blackwell, Oxford, UK: 546 pp., v.a. •
  - pp. 208-253 (Multiple und nicht-lineare Regressionen) ◦
- Quinn, P.Q. & Keough, M.J. 2002. *Experimental design and data analysis for biologists*. Cambridge University Press, Cambridge, UK: 537 pp. •

# <span id="page-103-1"></span>**Statistik 5**

Generalisierte Regressionsmodelle (GLMs)

**Heute geht es um** *generalized linear models* **(GLMs), die einige wesentliche Limitierungen von linearen Modellen überwinden. Indem sie Fehler- und Varianzstrukturen explizit modellieren, ist man nicht mehr an Normalverteilung der Residuen und Varianzhomogenität gebunden. Bei** *generalized linear regressions* **muss man sich zwischen verschiedenen Verteilungen und link-Strukturen entscheiden. Spezifisch werden wir uns die Poisson-Regressionen für Zähldaten und die binomiale Regression für ja/nein-Daten anschauen.**

## <span id="page-103-2"></span>**Lernziele**

Ihr…

- habt verstanden, worin sich **GLMs** von linearen Regressionen unterscheiden und wann sie zur Anwendung kommen; und •
- könnt die beiden häufigsten GLM-Typen **(Quasi-) Poisson-Regression** für Zähldaten und **binomiale Regression** für Binär- und Proportionsdaten in R richtig anwenden und die Ergebnisse interpretieren. •

# <span id="page-104-0"></span>**Von linearen Modellen zu GLMs**

### <span id="page-104-1"></span>**Zwei Beispiele**

Nehmen wir an, wir wollten modellieren, wie viele Besucher an einem Strandabschnitt zur Mittagszeit in Abhängigkeit von der herrschenden Lufttemperatur anzutreffen sind. Unsere Daten sehen folgendermassen aus und mit den bekannten Methoden können wir ein lm rechnen, dessen Ergebnis signifikant ist und sogar recht viel der Gesamtvarianz erklärt:

![](_page_104_Figure_3.jpeg)

Unsere abhängige Variable ist eine Zählung und verhält sich daher anders als eine echte metrische Variable (etwa einer Messung des pH-Wertes). **Zähldaten** stellen lineare Modelle (lm) vor **vier Probleme:**

- Lineare Modelle sagen immer auch das Auftreten **negativer Werte** voraus, wohingegen **absolute Häufigkeiten immer positive Ganzzahlen** sind (im obigen Beispiel würde das Modell bereits im gefitteten Bereich, unter etwa 12 °C, eine negative Anzahl Menschen vorhersagen). •
- Nahezu immer sind Zähldaten **rechtsschief verteilt**, also nicht normalverteilt und auch nicht symmetrisch •
- Bei Zähldaten nimmt nahezu immer die **Varianz mit dem Mittelwert zu**. •
- Zähldaten folgen keiner kontinuierlichen (wie die Normalverteilung), sondern einer **diskreten Verteilung**. •

Theoretisch sind also die Voraussetzungen für ein lineares Modell bei Zähldaten nie erfüllt. In der Praxis gibt es aber Situationen, wo die Verletzung der Annahmen für das Modell nicht weiter problematisch ist und man mit einem lm zu korrekten Aussagen gelangen kann. Relativ problemlos funktioniert das (und wird auch noch häufig getan), wenn (a) alle Werte der Antwortvariablen weit von 0 entfernt sind und (b) die Werte der Antwortvariable um deutlich weniger als eine

Grössenordnung (d. h. Faktor 10) variieren. Im obigen Beispiel beträgt der Quotient des grössten und kleinsten Wertes der Antwortvariablen 2000 / 12 = 167. Mit etwas Erfahrung sehen wir schon im Scatterplot, dass hier Linearität und Varianzhomogenität verletzt sind.

Ein anderes Beispiel, bei dem ein lineares Modell offensichtlich und immer scheitern würde, wäre eine Befragung von Touristen an Tagen unterschiedlicher Temperatur, ob sie schwimmen gegangen sind. Das Ergebnis könnte wie folgt aussehen (stark gekürzte Tabelle, an jedem Tag (d. h. bei gleicher Temperatur) wurden jeweils mehrere Touristen befragt):

| Temperatur (°C) | Geschwommen? |
|-----------------|--------------|
| 1               | nein (0)     |
| 2               | nein (0)     |
| 5               | nein (0)     |
| 9               | nein (0)     |
| 14              | ja (1)       |
| 14              | nein (0)     |
| []              |              |
| 28              | ja (1)       |
| 29              | ja (1)       |

Bei solchen "binären Daten" bestehen zwei hauptsächliche Probleme für lineare Modelle:

- Die Werteverteilung ist nach unten und nach oben begrenzt. •
- Es gibt überhaupt nur zwei mögliche Werte, nein und ja, als 0 und 1 codiert. •

### <span id="page-106-0"></span>**Die Idee der Generalized linear models (GLMs)**

**Generalized linear models (GLMs)** verallgemeinern **lineare Modelle (LMs)**, um Fälle wie die geschilderten (Zähldaten, Binärdaten, für weitere Beispiele siehe Crawley (2015)) modellieren zu können. "Generalisiert" heissen die GLMs aus folgenden drei Gründen:

- Alle LMs sind im Begriff GLM eingeschlossen (aber viele GLMs sind keine LMs). •
- Die **Verteilung der "Zufallskomponente"** (= Residuen) kann sich **von einer Normalverteilung unterscheiden** (muss aber aus der exponentiellen Familie von Verteilungen sein). •
- Die abhängige Variable kann **auf verschiedene Weise mit den Prädiktoren verknüpft** (*linked*) sein. •

### <span id="page-106-1"></span>**Die drei Komponenten eines GLM**

Ein GLM setzt sich aus drei Komponenten zusammen, die relativ frei kombiniert werden können (aber für bestimmte Zufallskomponenten gibt es Standard-Link-Funktionen):

- **Zufallskomponente (d. h. die Verteilung der Residuen):** 1.
  - normal ◦
  - binomial: z. B. ja/nein, tot/lebendig ◦
  - Poisson: Zähldaten (funktioniert aber nicht immer) ◦
  - gamma ◦
  - negativ binomial (Dispersionsparameter muss geschätzt werden) ◦
- **Systematische Komponente (d. h. die** *x***-Werte):** es ist alles möglich, was wir schon von LMs her kennen: 2.
  - kontinuierliche (metrische) Prädiktoren ◦
  - kategoriale Prädiktoren ◦
  - Interaktionen von Prädiktoren ◦
  - polynomiale Funktionen ◦
  - jewede Kombination aus den vorhergehenden Elementen ◦
- **Link-Funktion (d.h. was auf der linken Seite der Funktionsgleichung steht):** entweder y oder eine Transformation von y, siehe Details unten: 3.
  - Identität (*identity*) ◦
  - log (für Zähldaten) ◦
  - logit (für Binärdaten) ◦

### <span id="page-106-2"></span>**Mögliche Verteilungen von Werten und von Varianzen**

Was mit verschiedenen **Verteilungen der Residuen** gemeint ist, veranschaulichen die folgenden beiden Abbildungen von vier Häufigkeitsverteilungen mit dem gleichen Mittelwert. Oben sind die **kontinuierliche Normalverteilung** und unten drei unterschiedliche diskrete Verteilungen (Poisson, negativ-binomial) zu sehen:

![](_page_107_Figure_0.jpeg)

Auch die **Beziehung von Varianzen zum (vorhergesagten) Mittelwert** müssen keinesfalls immer konstant sein, wie wir das von den linearen Modellen kennen. Vielmehr zeigen viele Datentypen eine systematische Veränderung der Varianz mit dem Mittelwert:

![](_page_108_Figure_0.jpeg)

(aus Crawley 2015)

### <span id="page-108-0"></span>**Typen von GLMs**

Eine Übersicht gängige GLM-Typen bietet die folgende Tabelle (man beachte die uneinheitliche Gross-/Kleinschreibung der Verteilungen):

| Name der          | Link-Funktion |                                           | Abhängige Variable                                  |                                                                                      |
|-------------------|---------------|-------------------------------------------|-----------------------------------------------------|--------------------------------------------------------------------------------------|
| Verteilung in R   | Name          | Definition                                | Mögliche Werte                                      | Mögliche Datentypen                                                                  |
| binomial          | logit         | $\eta = \ln(\frac{\hat{y}}{1 - \hat{y}})$ | Relative Anteile                                    | Wahrscheinlichkeit von<br>Ereignissen oder<br>Ergebnissen                            |
| poisson           | log           | $\eta = \ln(\hat{y})$                     | Nicht-negative<br>Ganzzahlen                        | Anzahl von Fällen (inkl.<br>Kontingenztabellen)                                      |
| negative.binomial | log           | $\eta = \ln(\hat{y})$                     | Nicht-negative<br>Ganzzahlen                        | Anzahl von Individuen in<br>aggregierten räumlichen<br>Verteilungen                  |
| Gamma             | reciprocal    | $\eta = \frac{1}{\hat{y}}$                | Positive reelle<br>Zahlen                           | Abmessungen, Gewichte, etc. und deren Verhältnisse                                   |
| gaussian          | identity      | $\eta = \hat{y}$                          | Beliebige reelle<br>Zahlen (d. h.<br>auch negative) | (wenn man die<br>vorstehenden Möglichkeiten<br>berücksichtigt, dann nahezu<br>keine) |

(übersetzt und modifiziert nach Šmilauer 2017)

Man beachte, dass ein GLM mit Normalverteilung (gaussian) und identity-Link identisch mit einem LM ist.

Wenn man dieser Anleitung strikt folgen würde (was auch Šmilauer 2017 nicht tut), dürfte man LMs nur dann verwenden, wenn die Antwortvariable auch negative Werte annehmen kann. De facto können viele/die meisten Antwortvariablen, mit denen wir arbeiten, nur positive Werte annehmen (etwa Biomasse, Niederschläge, Stoffkonzentrationen, Einkommen). Die Abweichungen von der Normalverteilung (durch die fehlenden negativen Werte) sind aber in der Praxis so gering, dass in solchen Fällen meist trotzdem ein Gaussian-GLM = LM das beste Verfahren darstellt.

GLMs mit binomialer, Poisson, Gamma- und Gauss (Normal)-Verteilung sind in Base R implementiert, für negative binomial («glm.nb») benötigt man das Package MASS. In diesem Kurs gehen wir im Detail nur auf die beiden meistbenutzten GLM-Typen ein, **Poisson-Regression für Zähldaten** und **binomiale Regressionen für Binärdaten und Proportionaldaten**. Mehr zu den übrigen Typen findet man u. a. in Crawley (2015), Dunn & Smyth (2018) und Fox & Weisberg (2019)

### <span id="page-109-0"></span>**Das Fitten und die Modellgüte von GLMs**

Bei einem **linearen Modell (LM)** wird die Lösung durch **Minimierung der Summe der Abweichungsquadrate** erzielt. Diese Lösung lässt sich direkt, immer eindeutig und sogar von Hand ausrechnen. GLMs dagegen fitten die Modelle in einem iterativen Verfahren, indem die *Likelihood* **maximiert** wird. Deswegen spricht man auch von *Maximum likelihood* (ML). Nach erfolgtem Fitten werden die Werte mit der **Umkehrfunktion der Link-Funktion** auf die originale Skala zurücktransformiert.

Als Mass der Variabilität oder lack of fit wird bei GLMs die Devianz *D* verwendet, die folgendermassen definiert ist:

Je nach GLM-Typ wird die Devianz anders berechnet:

| Model      | Deviance                                                                                   | Error    | Link       |
|------------|--------------------------------------------------------------------------------------------|----------|------------|
| linear     | $\sum (y - \hat{y})^2$                                                                     | Gaussian | identity   |
| log linear | $2\sum y\log\left(\frac{y}{\hat{y}}\right)$                                                | Poisson  | log        |
| logistic   | $2\sum y \log\left(\frac{y}{\hat{y}}\right) + (n-y)\log\left(\frac{n-y}{n-\hat{y}}\right)$ | binomial | logit      |
| gamma      | $2\sum \frac{(y-\hat{y})}{y} - \log\left(\frac{y}{\hat{y}}\right)$                         | gamma    | reciprocal |

(aus Crawley 2015)

### <span id="page-110-0"></span>Erklärte Varianz in GLMs

Im strikten Sinne gibt es eine erklärte Varianz ( $R^2$ ) nur für lineare Modelle, die mit der Methode der kleinsten Abweichungsquadrate ermittelt wurden (lineare Regressionen, ANOVAs, ANCOVAs). Da aber auch in GLMs der Wunsch besteht, zu quantifizieren, wie umfänglich ein Modell die Realität abbildet (also wie vollständig die Prädiktoren sind), wurden dafür sogenannte Pseudo- $R^2$ -Werte geschaffen. Analog zu  $R^2$  reichen sie auch von 0 (Modell erklärt Muster in der abhängigen Variable gar nicht) bis 1 (Modell erklärt Muster in der abhängigen Variable vollständig).

Es gibt je nach GLM-Typ unterschiedliche Pseudo- $R^2$ -Werte als Masse für die Modellgüte. Bis vor einiger Zeit, musste man sie «händisch» aus Parametern des Modell-Outputs berechnen. Jetzt kann man das mit dem Befehl r2 aus dem performance-Package machen. Der Befehlt r2 erkennt, um welche Art von Regressionsmodell es sich handelt und berechnet (und benennt) automatisch den passenden Pseudo- $R^2$ -Wert (oder manchmal mehrere Alternativen), etwa Nagelkerkes, McFaddens oder Tjurs  $R^2$ . In einem Ergebnistext bitte immer angeben, um welches Pseudo- $R^2$  es sich handelt. Man beachte, dass  $R^2$ -Werte zwischen verschiedenen Modelltypen nicht direkt vergleichbar sind, innerhalb eines GLM-Typs dagegen schon.

### <span id="page-110-1"></span>Testen der Modellvoraussetzungen (Modellvalidierung) in GLMs

Der höheren Komplexität von GLMs verglichen mit linearen Modellen ist auch die Modellvalidierung zwar genauso wichtig, aber komplexer. Bis vor einiger Zeit, musste man sich die jeweils passenden Diagnostik-Plots oder -Kennzahlen mehr oder weniger «händisch» erstellen. Jetzt leistet der das Package DHARMa die Arbeit.

# <span id="page-111-0"></span>**Poisson-Regressionen für Zähldaten**

### <span id="page-111-1"></span>**Berechnung**

Die Struktur des glm-Befehls in R ist genau identisch mit jenem des lm-Befehls. Nur muss man zusätzlich die Verteilung (family) und ggf. die Link-Funktion (wenn nicht die Standard-Link-Funktion der jeweiligen Verteilung) angeben. Schauen wir uns nun die Ergebnisse für unsere Zähldaten der Strandbesucher an, zunächst mit einem LM, dann mit einem Gauss-GLM und schliesslich mit einem Poisson-GLM:

```
lm_strand <- lm(Besucher~Temperatur)
glm_gaussian <- glm(Besucher~Temperatur, family = gaussian)
glm_poisson <- glm(Besucher~Temperatur, family = poisson)
```

summary(lm\_strand)

Coefficients:

Estimate Std. Error t value Pr(>|t|) (Intercept) -855.01 290.54 -2.943 0.021625 \* Temperatur 67.62 11.80 5.732 0.000712 \*\*\*

summary(glm\_gaussian)

Coefficients:

Estimate Std. Error t value Pr(>|t|) (Intercept) -855.01 290.54 -2.943 0.021625 \* Temperatur 67.62 11.80 5.732 0.000712 \*\*\*

summary(glm\_poisson)

Coefficients:

Estimate Std. Error z value Pr(>|z|) (Intercept) 3.500301 0.056920 61.49 <2e-16 \*\*\* Temperatur 0.112817 0.001821 61.97 <2e-16 \*\*\*

Wie nach den Erläuterungen im vorigen Kapitel zu erwarten war, sind die Ergebnisse des LMs und des Gauss-GLMs vollkommen identisch. Jene des Poisson-GLMs sind dagegen anders, insbesondere viel höher signifikant.

### <span id="page-111-2"></span>**Interpretation und Visualisierung der Ergebnisse**

Im Falle des lm können wir aus den Parameter-Schätzungen (Spalte Estimate im summary) direkt die sich ergebende Funktionsgleichung aufschreiben:

Bei einem glm sind die Parameter-Schätzungen dagegen nicht direkt interpretierbar, da sie sich auf eine transformierte Skala beziehen, welche durch die Link-Funktion angegeben ist. Die Standard-Link-Funktion bei einem Poisson-GLM ist log, also der natürliche Logarithmus (ln). Unser Ergebnis lässt sich damit wie folgt schreiben:

Da uns aber nicht ln (Besucher), sondern die Besucherzahl selbst interessiert, müssen wir die Umkehrfunktion der Link-Funktion anwenden. Die Umkehrfunktion von ln ist exp. Es ergibt sich:

Damit können wir auch die vorhergesagten Werte für verschiedene Temperaturen berechnen.

Wenn wir das Ganze plotten wollen, benötigen wir die funktion geom\_smooth welche den Befehl im Hintergrund ausführt. und die die Umkehrfunktion (exp) anwendet:

```
ggplot(data = strand, aes(x = Temperatur, y = Besucher)) +
geom_point() +
xlim(0, 40) + 
stat_smooth(method = "lm", color = "blue", se = FALSE) +
geom_smooth(method = "glm", method.args = list(family = "poisson"), 
color = "red", se = FALSE) +
geom_smooth(method = "glm", method.args = list(family = "quasipoisson"), 
color = "green", linetype = "dashed", se = FALSE) +
annotate(geom = "text", x = 4, y = 2000, label = "gaussian", color = "blue") +
annotate(geom = "text", x = 4, y = 1800, label = "poisson", color = "red") +
annotate(geom = "text", x = 4, y = 1600, label = "quasipoisson", 
color = "green") +
theme_classic()
```

![](_page_112_Figure_2.jpeg)

### <span id="page-113-0"></span>**Overdispersion als Problem**

Mathematisch beschreibt die Poisson-Verteilung Ereignisse pro Zeiteinheit, wenn sie mit einer bestimmten Rate (Mittelwert) erfolgen, die Ereignisse selbst aber unabhängig voneinander sind. Für ökologische/umweltwissenschaftliche Zähldaten sind diese Voraussetzungen oft nicht exakt gegeben, sie folgen daher nicht immer genau einer Poisson-Verteilung, sondern weisen teilweise eine *Overdispersion* auf. *Overdispersion* bedeutet dass die gemessene Variation in den Daten die theoretisch erwartete Variation übersteigt. Für eine Poisson-Regression wird eine angenommen. Wenn die Dispersion wesentlich/signifkant grösser als 1 ist, liegt *Overdispersion* vor. Residual deviance und Residual degrees of freedom findet man im summary des glm:

summary(glm\_poisson)

[…]

(Dispersion parameter for poisson family taken to be 1)

Null deviance: 6011.8 on 8 degrees of freedom Residual deviance: 1113.7 on 7 degrees of freedom

AIC: 1185.1

Man sieht hier, dass der Quotient von 1113.7 und 7 weit höher als 1 ist. Mit dem Dispersionstest im Package performance kann man formal auf einen signifikanten Unterschied testen:

p\_load("performance") check\_overdispersion(glm\_poisson)

# Overdispersion test

dispersion ratio = 149.683

Pearson's Chi-Squared = 1047.778

p-value = < 0.001

Overdispersion detected.

Wenn man eine signifikante *Overdispersion* gefunden hat, gibt es zwei Lösungsmöglichkeiten:

- **Quasi-Poisson-Verteilung:** Hierbei schätzt der Algorithmus den Dispersionsparameter aus den Daten und passt die angenommene Verteilung entsprechend an. Die Methode ist im Befehl glm in Base R implementiert: 1.
- glm\_quasipoisson <- glm(Besucher~Temperatur, family = quasipoisson) summary(glm\_quasipoisson) •
- Coefficients: •

```
Estimate Std. Error t value Pr(>|t|) 
(Intercept) 3.50030 0.69639 5.026 0.00152 **
Temperatur 0.11282 0.02227 5.065 0.00146 **
---
```

Signif. codes: 0 '\*\*\*' 0.001 '\*\*' 0.01 '\*' 0.05 '.' 0.1 ' ' 1

(Dispersion parameter for quasipoisson family taken to be 149.6826)

- Man sieht, dass im Vergleich zur Berechnung mit einem einfachen Poisson-GLM die Parameterschätzungen nicht verändert haben, jedoch die Signifikanzen niedriger ausgefallen sind (d. h. höhere *p*-Werte). •
- **Negativ-binomiale Verteilung:** Oftmals erzielt man damit ähnliche, in besonderen Fällen allerdings auch deutlich andere Ergebnisse. Was besser ist, hängt vom Einzelfall ab und ist u. U. recht "tricky". Weitere Details, siehe Ver Hoef & Boveng (2007). 1.

# <span id="page-114-0"></span>**Logistische Regressionen für Binärdaten**

Logistische Regressionen werden für alle binären Antwortvariablen verwendet, etwa für Vorkommensdaten (Inzidenzdaten). Das folgende Abbildungspaar zeigt links, was passieren würde, wenn man solche Daten mit einem lm fitten würde und rechts, die korrekte Modellierung mit einem logistischen glm:

![](_page_114_Figure_4.jpeg)

(aus Logan 2010)

### <span id="page-114-1"></span>**Prinzipielles Vorgehen**

- Die abhängige Variable muss als Vektor vorliegen, der entweder nur die Ganzzahlen 0 und 1 enthält oder aber ein Faktor mit genau zwei Levels ist. •
- Es wird ein **glm mit family=binomial** gerechnet. •
- Der voreingestellte **Link ist logit**, alternativ geht auch log-log. •
- Overdispersion ist bei Binärdaten nicht relevant. •
- Wie bei allen (multiplen) Modellen müssen wir eine **Modellvereinfachung** des vollen Modells vornehmen, wofür im Prinzip die gleichen drei Methoden zur Verfügung stehen, die wir schon kennen: •
  - **Modellselektion I:** sukzessive Vereinfachung durch Entfernen nichtsignifkanter Terme. ◦

- Modellselektion II: sukzessive Vereinfachung mittels Vergleich der Devianzen zweier Modelle mit Chi-Quadrat-Test (Achtung: Unterschied zu Im, wo wir eine ANOVA, d. h. einen F-Test verwendet haben).
- Modellselektion III: mittels AICc: Berechnung aller möglichen Modelle und dann entweder Auswahl jenes mit dem niedrigsten AICc oder Multimodel inference.

#### <span id="page-115-0"></span>Die Theorie dahinter

Das "logit" (L) ist ein zentrales Element der logistischen Regression. Ein «logit» ist als der natürliche Logarithmus eines "odds" definiert. "Odds" hatten wir im Prinzip (ohne es so zu nennen) schon kurz beim Vierfelder-Assoziationstest (Chi-Quadrat- bzw. Fishers exakter Test). Sie bezeichnen die Wahrscheinlichkeit eines Ereignisses durch die "Gegenwahrscheinlichkeit". Es gilt also Folgendes:

Warum arbeitet man mit "odds" und "logits"? Wenn man nur p modellieren würde, wären die möglichen Werte auf 0 ... 1 begrenzt. "Odds" dagegen können Werte zwischen 0 und  $\infty$  annehmen. Der Logarithmus schliesslich sorgt für eine symmetrische Verteilung der originalen Wahrscheinlichkeiten unter 50 % (jetzt zwischen  $-\infty$  und 0) und der originalen Wahrscheinlichkeiten über 50 % (jetzt zwischen 0 und  $+\infty$ ).

Bei GLMs wir ja immer die abhängige Variable mit der Link-Funktion transformiert. Damit modelliert eine logistische Regression das folgende Modell (in einer multiplen logistischen Regression ggf. auch mit  $x_1$ ,  $x_2$  usw.):

### <span id="page-115-1"></span>**Modelldiagnostik und Ergebnisse**

Die Beurteilung von Validität und Güte/Relevanz eines logistischen Modells unterscheidet sicher erheblich von einem Im:

- Eine visuelle Inspektion der Residualplots ist hier nicht informativ.
- Es gibt diverse numerische *Goodness-of-fit-*Tests für das Modell, am einfachten der Vergleich der Abweichung der Devianz () von der geforderten Verteilung.
- Das konventionelle Gütemass funktioniert ebenfalls nicht. Stattdessen kann man die Modellgüte mit einem **Pseudo**- ausdrücken:

Da nicht die abhängige Variable (d. h. die Auftretenswahrscheinlichkeit), sondern ihr *logit* modelliert wurde, muss man die beiden Parameterschätzungen erst in informative Grössen übersetzen. Es sind diese:

- **Lagemass** (d. h. bei welchem  $x_1$ -Wert ist die Wahrscheinlichkeit von 0 und 1 gleich hoch; auch als "LD50" = "lethal" dose for 50% of the individuals" bezeichnet, basierend auf Anwendungen on logistischen Regressionen in Toxizitätstests):
- **Steilheitsmass** (d. h. wie scharf/steil ist der Übergang von 0 zu 1, ausgedrückt als die relative Änderung der "odds" bei Zunahme von  $x_1$  um eine Einheit):

### <span id="page-116-0"></span>**Umsetzung in R**

Schauen wir uns diese ganzen Schritte im Fall unseres Bade-Beispiels an, also der Wahrscheinlichkeit, dass eine Person am Strand schwimmen geht in Abhängigkeit von der Temperatur. Die Definition des Modells in R ist wie gehabt einfach:

glm\_logistic <- glm(bathing~temperature, family = "binomial", data = bathing) summary(glm\_logistic)

Coefficients Estimate Std. Error z value Pr(>|z|) (Intercept) -5.4652 2.8501 -1.918 0.0552 . temperature 0.2805 0.1350 2.077 0.0378 \*

Die uns interessierenden Aspekte **Modelldiagnostik, Modellgüte und Kurvenverlauf** müssen wir händisch aus dem abgespeicherten Objekt model extrahieren, indem wir auf einzelne darin abgespeicherte Daten zurückgreifen (manches geht auch mit den Packages MASS oder performance):

# Modeldiagnostik (wenn nicht signifikant, dann OK) 1 - pchisq(glm\_logistic \$deviance, glm\_logistic \$df.resid) [1] 0.6251679 # Area Under the ROC Curve (AUC) library("performance") performance\_roc(glm\_logistic) # Modellgüte (Eine Version von pseudo-R2) 1 - (glm\_logistic\$dev/ glm\_logistic\$null) [1] 0.4775749 # Modellgüte (Tjur's pseudo-R2) r2(glm\_logistic) # R2 for Logistic Regression Tjur's R2: 0.538 # Steilheit der Beziehung (relative Änderung der # odds von x + 1 vs.x) exp(glm\_logistic\$coefficients[2]) temperature 1.323807

# LD50 (also hier: Temperatur, bei der 50% der Touristen baden)

- glm\_logistic\$coefficients[1]/ glm\_logistic\$coefficients[2]

(Intercept) 19.48311

```
# LD50-Berechnung mit dem MASS-package
p_load(MASS)
dose.p(glm_logistic, p = 0.5)
Dose SE
p = 0.5: 19.48311 2.779485
```

Der erste Wert gibt die Steilheit der Beziehung an und ob sie ansteigend oder fallend ist, wobei 1 keinen Effekt, >1 eine ansteigende Häufigkeit und < 1 eine fallende Häufigkeit bezeichnen. Der zweite Wert (man beachte das Minus-Zeichen in der Formel!) gibt den *x*-Wert an, für den die berechnete Wahrscheinlichkeit (Vorkommenswahrscheinlichkeit, Sterbewahrscheinlichkeit, usw.) genau 50 % ist.

Ganz einfach vorzustellen ist eine logistische Funktion auch mit diesen Werten noch nicht. Deswegen sollten wir im Falle signifkanter logistischer Regressionen immer zwei Dinge tun: (1) Die Funktionsgleichung angeben und (2) Das Ergebnis visualisieren.

Die Funktionsgleichung zu extrahieren, ist etwas vertrackt, da wir ja nicht die Auftretenswahrscheinlichkeit *y*, sondern ihren *logit* modelliert haben. Übersetzt bedeuten die Estimate-Werte unseres summary also: 1.

Wir formen sukzessive um, um nach y aufzulösen:

Oder mit den Werten in unserem Fall:

Zum Visualisieren den geom\_smooth verwenden 1.

```
# Plotting
ggplot(data = bathing, aes(x = temperatur, y = badend)) +
geom_point() +
xlim(0, 30) +
labs(x = "Temperature (°C)", y = "% Bathing") +
geom_smooth(method = "glm", method.args = list(family = "binomial"), se = FALSE) +
theme_classic()
```

![](_page_118_Figure_0.jpeg)

## <span id="page-118-0"></span>**Binomial-Regressionen für Proportionen**

Stellen wir uns nun vor, im vorigen Beispiel, hätten wir für jedes Temperaturintervall nicht die ja/ nein-Daten für jede einzelne Person erhoben, sondern vielmehr viele Personen beobachtet und den Anteil Badender/Nicht-Badender Personen ermittelt. Inhaltlich hat sich nicht viel verändert: Statt der Wahrscheinlichkeit des Badens für eine Einzelperson würden wir jetzt den vorhergesagten Anteil der Badenden unter allen Personen am Strand ermitteln. Wiederum sind die Werte zwischen 0 (0 %) und 1 (100 %) beschränkt und die Varianz ist zu den extremen Enden gering, bei 50 % jedoch am grössten.

Das bedeutet, wir können diesen Fall wiederum mit einem binomialen Modell mit logit-Link berechnen. Allerdings können wir nicht die Proportionen der Badenden für die einzelnen Temperaturen direkt übergeben, da R sonst nicht wüsste, auf wie vielen Einzelbeobachtungen jede Proportion beruht, was aber essenziell ist, um die Modellparameter und die *p*-Werte verlässlich zu schätzen. Insofern muss man R für jeden Temperaturwert nicht einen einzelnen y-Wert, sondern zwei übergeben. Dafür gibt es zwei Optionen (siehe im Beispiel).

### <span id="page-118-1"></span>**Beispiel und Umsetzung in R**

Wir haben Daten zum Überleben von Raupen der Mottenart (*Choristoneura frumiferana*; englisch «budworm») bei einer Behandlung mit Insektizid in unterschiedlichen Dosen (eingebauter Datensatz budworm aus dem Paket MASS). Es wurden jeweils 20 männliche und 20 weibliche Raupen bei Insektizidgaben von sechs unterschiedlichen Konzentrationen (1, 2, 4, 8, 16, 32) untersucht und ermittelt, wie viele davon gestorben sind. Der Dataframe hat daher vier Spalten:

'data.frame': 12 obs. of 4 variables:

\$ sex : Factor w/ 2 levels "female","male": 2 2 2 2 2 2 1 1 1 1 ...

\$ dose : int 1 2 4 8 16 32 1 2 4 8 ...

\$ ndead : int 1 4 9 13 18 20 0 2 6 10 ...

\$ ntotal: int 20 20 20 20 20 20 20 20 20 20 ...

Da die Insektiziddosen geometrisch mit sukzessiven Verdopplungen skaliert sind, macht es Sinn, sie vor der Erstellung des Modells mit log2 zu transformieren (einer der relativ seltenen Fälle, in denen man eine Prädiktorvariable transformieren sollte):

budworm\$ldose <- log2(budworm\$dose)

Das Modell (hier globales Modell mit zwei Prädiktoren und ihrer Interaktion) können wir nun auf zwei alternative Weisen spezifizieren:

- Statt eines Vektors der y-Werte, übergeben wir einen Dataframe mit zwei Spalten, bestehend aus den toten und lebenden Individuen. Dann können wir das binomiale Modell wie oben in der logistischen Regression spezifizieren. •
- Alternativ übergeben wir den Anteil der toten Individuen, müssen dann aber zusätzlich die Zahl der untersuchten Individuen pro Kombination von Dosis und Geschlecht im Parameter weights übergeben. •

glm\_binomial <- glm(cbind(ndead, ntotal-ndead) ~ ldose\*sex, family = binomial, data = budworm)

glm\_binom <- glm(ndead/ntotal ~ ldose\*sex, family = binomial, weights = ntotal, data = budworm)

Die Ergebnisse sind identisch (hier nur für das erste Modell gezeigt):

coef(glm\_binomial)

(Intercept) ldose sexmale ldose:sexmale

-2.9935418 0.9060364 0.1749868 0.3529130

Wie üblich folgt die Modellvereinfachung (die Interaktion ist nicht signifikant und fällt heraus, die beiden einzelnen Prädiktoren sind signifikant und verbleiben im Modell):

# Model optimierung

drop1(glm\_binomial, test = "Chisq")

Single term deletions

Model:

cbind(ndead, ntotal - ndead) ~ ldose \* sex

Df Deviance AIC LRT Pr(>Chi)

<none> 4.9937 43.104

ldose:sex 1 6.7571 42.867 1.7633 0.1842

glm\_binomial\_2 <- update( glm\_binomial, .~.-sex:ldose)

```
drop1(glm_binomial_2, test = "Chisq")
Single term deletions
Model:
cbind(ndead, ntotal - ndead) ~ ldose + sex
Df Deviance AIC LRT Pr(>Chi) 
<none> 6.757 42.867 
ldose 1 118.799 152.909 112.042 < 2.2e-16 ***
sex 1 16.984 51.094 10.227 0.001384 ** 
---
Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
Danach müssen wir das Modell noch validieren und ggf. anpassen (das umfasst bei GLMs den Test
auf «overdispersion» und die normale Modellvalidierung (letzere derzeit am besten mit dem
Package DHARMa):
# Validate Model
check_overdispersion(glm_binomial_2)
# Overdispersion test
dispersion ratio = 0.929
p-value = 0.592
No overdispersion detected.
# Validate Model
library(DHARMa)
set.seed(123)
simulateResiduals(glm_binomial_2, plot = TRUE, n = 1000)
```

#### DHARMa residual

![](_page_121_Figure_1.jpeg)

Hier gibt es keine Probleme. glm\_binomial\_2 ist daher unser minimal adäquates Modell. Wir brauchen jetzt nur noch ein Pseudo-*R*<sup>2</sup> und eine Visualisierung (siehe Demo-Vorführung).

# <span id="page-121-0"></span>Zusammenfassung

- *Generalized linear models* (GLMs) erlauben Regressionen mit anderen Varianzstrukturen und Residuenverteilungen als lineare Regressionen.
- Unter den GLMs sind zwei besonders gebräuchlich: (Quasi-) Poisson-Regressionen werden für Zähldaten, binomiale Regressionen werden für binäre Daten («logistische Regression») und Proportionen, verwendet.

### <span id="page-121-1"></span>Weiterführende Literatur

- Crawley, M.J. 2015. *Statistics An introduction using R*. 2nd ed. John Wiley & Sons, Chichester, UK: 339 pp.
  - Chapter 12: Other Response Variables
  - Chapter 13: Count Data
  - Chapter 14: Proportion Data
  - Chapter 15: Binary Response Variable

- Dunn, P.K. & Smyth, G.K. 2018. *Generalized linear models with examples in R*. Springer, New York, US: 562 pp. •
- Fox, J. & Weisberg, S. 2019. *An R companion to applied regression*. 3rd ed. SAGE Publications, Thousand Oaks, CA, US: 577 pp. •
- Logan, M. 2010. *Biostatistical design and analysis using R. A practical guide*. Wiley-Blackwell, Oxford, UK: 546 pp., v.a. •
  - pp. 483-530 (GLMs) ◦
- Quinn, P.Q. & Keough, M.J. 2002. *Experimental design and data analysis for biologists*. Cambridge University Press, Cambridge, UK: 537 pp. •
- Šmilauer, P. 2017. *Modern regression methods. Chapter 2: Generalised linear models for counts and ratios*. Unpublished script, České Budějovice*,* CZ. •
- Ver Hoef, J.M. & Boveng, P.L. 2007. Quasi-Poisson vs. negative binomial regression: how should we model overdispersed count data? *Ecology* 88:2766– 2772. •

# <span id="page-122-0"></span>**Statistik 6**

Gemischte Modelle (LMMs, GLMMs) [1.5 Tage]

**In Statistik 6 lernen die Studierenden Lösungen kennen, welche die diversen Limitierungen von linearen Modellen überwinden. Während** *generalized linear models* **(GLMs) aus Statistik 5 bekannt sind, geht es jetzt um** *linear mixed effect models* **(LMMs) und** *generalized linear mixed effect models* **(GLMMs). Dabei bezeichnet** *generalized* **die explizite Modellierung anderer Fehler- und Varianzstrukturen und** *mixed* **die Berücksichtigung von Abhängigkeiten bzw. Schachtelungen unter den Beobachtungen. Einfachere Fälle von LMMs, wie** *split-plot* **und**  *repeated-measures* **ANOVAs, lassen sich noch mit dem aov-Befehl in Base R bewältigen, für komplexere Versuchsdesigns/Analysen gibt es spezielle R packages. Abschliessend gibt es eine kurze Einführung in GLMMs, die eine Analyse komplexerer Beobachtungsdaten z. B. mit räumlichen Abhängigkeiten, erlauben.**

### <span id="page-122-1"></span>**Lernziele**

Ihr…

- habt verstanden, welche Versuchsdesigns mit einer **normalen (Typ I) zweifaktoriellen ANOVA** analysiert werden können und welche die **Spezifikation eines random factors** erfordern; •
- könnt einfache Fälle von **Repeated measures- und Split-plot ANOVAs** in R spezifizieren und durchführen (mit aov bzw. glmmTMB); •
- versteht den Unterschied zwischen **random intercept** und **random slope**; und •
- wisst, wann man **generalized linear mixed effect models (GLMMs)** anwenden sollte und wie das im Prinzip geht. •

# <span id="page-123-0"></span>*Split-plot***- und** *Repeated-measures***-Designs**

### <span id="page-123-1"></span>**Die Idee**

Beginnen wir mit einer **konventionellen mehraktoriellen ANOVA** wie wir sie aus Statistik 2 kennen. Wie in allen linearen Modellen (und ebenso in GLMs) ist eine wesentliche Modellvoraussetzung die Unabhängigkeit der Beobachtungen voneinander. In der folgenden Abbildung ist das für ein experimentelles Setting veranschaulicht, etwa unseren Sortenversuch mit Sorte A und B und den beiden Treatments Freiland und Gewächshaus:

![](_page_123_Picture_3.jpeg)

Abb. 6.1. Versuchsdesign für eine klassische ANOVA, d.h. alle Faktorkombinationen vorhanden und unabhängig voneinander (aus Logan 2010).

Wir sehen, dass alle denkbaren Faktorenkombinationen (hier vier) auftreten (optimalerweise gleich häufig: balanciertes Design), sie aber räumlich zufällig, d. h. voneinander unabhängig angeordnet sind.

Im Gegensatz dazu stehen mehrfaktorielle ANOVAs, bei denen **nicht alle Faktorenkombinationen existieren oder es Abhängigkeiten zwischen den Treatments** gibt. Hier gibt es zwei Typen:

*Split plot***-Design**: Dies bezeichnet Situationen, bei denen die Kombinationen der beiden Faktoren nicht unabhängig voneinander räumlich verteilt sind, etwa weil dies mit zu grossem Aufwand verbunden wäre. Stellen wir etwa das Beispiel mit dem Gewächshaus-Freiland-Versuch von oben vor: Schon für die geringe Replizierung von nur drei Wiederholungen pro Faktorenkombination müsste man sechs Gewächshäuser haben, jedes entweder mit Sorte A oder mit Sorte B, die man zudem räumlich zufällig platzieren kann. Logischerweise geht das oftmals nicht. Stattdessen könnte man drei Gewächshäuser haben, in denen man jeweils beide Sorten pflanzt. Dann wäre das Gewächshaus bzw. das entsprechende Freilandbeet der "*plot*", der dann zwischen den beiden Sorten aufgeteilt (*split*) wird. Damit ist aber die Unabhängigkeitsannahme linearer Modelle verletzt, da sich ja die Gewächshäuser unterscheiden könnten, etwa in ihrer Thermoregulation, ihrer Lichtdurchlässigkeit oder ihrer Beschattung durch umstehende Bäume oder Gebäude. Deshalb hat potenziell die Frage, in welche Gewächshaus die Pflanzen standen, auch einen Einfluss auf das Ergebnis, muss mithin im statistischen Modell berücksichtigt werden. 1.

![](_page_125_Picture_1.jpeg)

Abb. 6.2. Versuchsdesign für Split-plot-Design, wo der eine Faktor im anderen geschachtelt du damit nicht unabhängig vom Block ist (aus Logan 2010).

*Repeated measures***-Design**: Hier geht es nicht um eine räumliche Bindung (enges Nebeneinander), sondern um eine zeitliche Bindung (zeitliches Nacheinander). Das heisst, an bestimmten Untersuchungsobjekten (Personen, Pflanzenindividuen, Untersuchungsflächen) wird zu verschiedenen Zeitpunkten eine Untersuchung vorgenommen, wie die folgende Abbildung es veranschaulicht: 1.

![](_page_126_Picture_1.jpeg)

Abb. 6.3. Repeated-measures-Design (aus Logan 2010).

Während *split plot*-Design und *repeated measures*-Design auf den ersten Blick wie etwas Verschiedenes aussehen, so sind sie statistisch doch äquivalent.

#### **Frage**

Wir hatten eine Situations wie im split plot/repeated measures-Design schon einmal: Bei welchem Verfahren war das?

# <span id="page-127-0"></span>**ANOVA mit Error-Term als Lösung für einfache Fälle**

### <span id="page-127-1"></span>**Beispiel: Repeated measures**

Es handelt sich um einen Düngeversuch (Daten aus Lepš & Šmilauer 2020). 18 Pflanzenindividuen wurden zufällig einer von drei Düngevarianten zugewiesen und dabei zu vier Zeitpunkten ihre Wuchshöhe gemessen. Abhängigkeiten sind hier in zwei Aspekten vorhanden: einerseits wurde jedes Pflanzenindividuum mehrfach gemessen, andererseits hat es nur jeweils eine Düngervariante erhalten. Die Struktur des Datensatzes ist wie folgt:

```
str(plantf)
tibble [72 × 4] (S3: tbl_df/tbl/data.frame)
$ PlantHeight: num [1:72] 5 7 9 11 6 9 12 15 7 8 ...
$ Treatment : Factor w/ 3 levels "Nitrogen","Phosporhus",..: 3 3 3 3 1 1 1 1 2 2 ...
$ Time : Factor w/ 4 levels "T0","T1","T2",..: 1 2 3 4 1 2 3 4 1 2 ...
$ PlantID : Factor w/ 18 levels "P01","P02","P03",..: 1 1 1 1 2 2 2 2 3 3 ...
```

### <span id="page-127-2"></span>**Welche Unterschiede bestehen zu einer normalen ANOVA?**

Wir haben hier drei wesentliche Abweichungen von einer normalen Typ-I-ANOVA:

- Wir sind nicht am spezifischen Verhalten der Pflanzenindividuen P01–P18 interessiert, sondern haben sie "zufällig" ausgewählt, um alle möglichen Individuen dieser Art zu repräsentieren. •
- Jedes Pflanzenindividuum bekommt nur ein "Treatment", d. h. es gibt nicht alle möglichen Kombination aus Treatment × PlantID. •
- Die vier gemessenen Wuchshöhen sind nicht unabhängig voneinander (eine der Grundvoraussetzungen von Typ-I-ANOVAs und anderen linearen Modellen): So könnten bestimmte Pflanzenindividuen z.B. durchgängig schneller oder langsamer wachsen als andere. •

Es liegen also erhebliche Verletzungen der Voraussetzung eines linearen Modells vor. Wir brauchen stattdessen ein **gemischtes Modell**. Einfache Fälle für balancierte Designs lassen sich noch gut mit dem aov-Befehl in Base R umsetzen.

### <span id="page-127-3"></span>**Umsetzung in R und Interpretation der Ergebnisse**

Man spezifiziert im Error-Term den Faktor der zu Abhängigkeiten führt. Hier ist es PlantID, da einerseits das gleiche Pflanzenindividuum vier mal gemessen wird, andererseits aber nur ein Düngertreatment erhält. Abgesehen von dieser einfachen Ergänzung bleibt der Befehlt gleich:

```
# Mit aov
pf_eaov <- aov(PlantHeight ~ Treatment * Time + Error(PlantID), data = plantf)
```

Im Ergebnis erhalten wir eine zweigeteilte ANOVA-Tabelle: Der obere Teil sagt uns, dass der Effekt von Treatment (Art des Düngers), der in den Pflanzenindividuen (PlantID) geblockt ist,

höchstsignifikant (*p* < 0.001) ist. Der untere Teil sagt uns, dass es einen signifikanten Effekt der Zeit sowie eine signifikante Interaktion Düngertyp × Zeit gibt.

summary(pf\_eaov)

Error: PlantID

Df Sum Sq Mean Sq F value Pr(>F)

Treatment 2 115.36 57.68 21.68 3.76e-05 \*\*\*

Residuals 15 39.92 2.66

---

Signif. codes: 0 '\*\*\*' 0.001 '\*\*' 0.01 '\*' 0.05 '.' 0.1 ' ' 1

Error: Within

Df Sum Sq Mean Sq F value Pr(>F)

Time 3 588.1 196.02 382.13 < 2e-16 \*\*\*

Treatment:Time 6 64.9 10.81 21.07 1.37e-11 \*\*\*

Residuals 45 23.1 0.51

Wir sollten hier noch einen Interaktionsplot darstellen. Achtung: Residualplots funktionieren für ANOVAs mit Error-Term nicht. In solchen Fällen rechnet man am besten die normale ANOVA ohne Error-Term und beurteilt, ob evtl. eine Transformation der abhängigen Variablen nötig ist.

In realen Versuchsdesigns kann es auch geschachtelte Error-Terme geben, wobei die oberste Ebene immer links steht, wie die folgende allgemeine Syntax zeigt. Dabei können auch die Interessierenden Faktoren (hier: A, B, C) teilweise zugleich Teil der Schachtelung und damit des Error-Terms sein:

model2 <- aov (Y ~ A \* B \* C + Error (Block/A/B), data = beispiel)

### <span id="page-128-0"></span>*Linear mixed effect models* **(LMMs) allgemein**

### <span id="page-128-1"></span>**Die Idee**

*Linear mixed effect models* (LMMs) verallgemeinern LMs, um Folgendes modellieren zu können:

- Abhängigkeiten/Schachtelungen zwischen Faktoren (um der Verletzung der LM-Voraussetzungen Rechnung zu tragen). •
- Faktoren, die uns nicht interessieren. Diese werden als sogenannte random factors modelliert, damit "sparen" wir Freiheitsgrade und gewinnen Teststärke für die uns interssierenden Faktoren. •

Die einfachsten LMMs, d. h. *Repeated measures*- und *Split plot*-ANOVA gehen (mit Limitierungen) noch mit dem aov-Befehl (s. o.). Für komplexere Situationen bzw. im allgemeinen Fall (einschliesslich Regressionen und ANCOVAs) benötigt man dagegen ein spezifisches Package für gemischte Modelle. Das gilt insbesondere für **nicht-balancierte Designs** (d.h. unterschiedliche Faktorkombinationen kommen unterschiedlich häufig vor). Es gibt mehrere, die ständig

weiterentwickelt werden. Aktuell ist das Package glmmTMB mit dem gleichnamigen Befehl besonders mächtig und wir verwenden es daher im Folgenden.

### <span id="page-129-0"></span>*Random* **und** *fixed factors*

Analog zum **Error-Term in aov** spezifiziert man hier einen **random-Term**, der aus mehreren ggf. auch geschachtelten Variablen bestehen kann. Darüberhinausgehend kann man in LMMs (und GLMMs) entscheiden, ob man nur einen **zufälligen Achsenabschnitt (***random intercept***)** oder auch eine **zufällige Steigung (***random slope***)** modellieren möchte:

![](_page_129_Figure_3.jpeg)

Abb. 6.4. Unterschiedliche Möglichkeiten, wie fixed effects und random effects in einem Modell kombiniert sein können.

Mit **«random factors»** bezeichnet man diejenigen Prädiktoren, die potenziell einen Einfluss haben, aber inhaltlich nicht interessieren (insbesondere die räumlichen und zeitlichen Abhängigkeiten). Mit **«fixed factors»** dagegen bezeichnet man jene Prädiktoren, deren Einfluss auf die abhängige Variable man testen möchte. Dadurch, dass die nicht interessierenden Variablen als «random factors» codiert werden, «verbrauchen» sie weniger Freiheitsgrade, da keine Schätzung (estimate) für jedes Faktorlevel generiert wird, sondern einfach modelliert wird, dass alle Levels eines «random factors» aus einer Normalverteilung stammen (für die das Modell nur die Standardabweichung schätzen muss).

Wichtig ist dabei, dass die Unterscheidung zwischen «fixed factors» und «random factors» nicht in Stein gemeisselt, sondern zu einem gewissen Grad auch kontextabhängig ist. Stellen wir uns etwa einen Düngeversuch vor, bei dem geschaut wird, wie mehrere Nährstoffe und ihre Kombination auf das Wachstum von Pflanzenarten wirken. Dabei wären sicherlich die Nährstoffe und ihre Interaktionen «fixed factors», die Abhängigkeiten durch die räumliche Anordnung und ggf.

mehrfache Messung an denselben Individuen dagegen «random factors». Die Artidentität der Pflanzen könnte man dagegen mit guter Berechtigung sowohl als «fixed factors» wie als «random factors» definieren, primär abhängig vom Untersuchungsziel. Hat man die Versuchsarten gezielt gewählt, um spezifisch etwas über diese herauszufinden, wäre «fixed factor» richtig. Hat man sie dagegen zufällig aus der heimischen Flora gewählt, um eine generalisierte Aussage über die Reaktion von Gefässpflanzen auf Düngung zu erzielen, wäre die Codierung als «random factors» sinnvoller.

### <span id="page-130-0"></span>Pseudo-R<sup>2</sup>

Wie schon bei GLMs funktioniert das «normale»  $R^2$  hier nicht und man muss auf ein Pseudo-  $R^2$  ausweichen, hier Nakagawas  $R^2$ . Dieses ist in der performance-Package mit dem Befehlt r2\_nakagawa oder kurz r2 implementiert (performance wählt automatisch das passende  $R^2$ -Mass). Bei LMMs (und GLMMs) werden zwei  $R^2$ -Werte angegeben:

- Marginal R<sup>2</sup>: Varianz, die durch die «fixed factors» alleine erklärt wird
- Conditional  $R^2$ : Gesamtvarianz, die durch fixed und random factors zusammen erklärt wird.

LMMs, ihr korrekte Implementierung und Interpretation können u. U. sehr komplex sein, weswegen wir sie in unserem Kurs nicht in voller Tiefe besprechen können. Wer weitergehende benutzerfreundliche Informationen sucht, sei insbesondere auf Zuur et al. (2009, 2013) verwiesen.

### <span id="page-130-1"></span>Linear mixed effect models (LMMs) in der Praxis

Wie oben angedeutet finden gemischte Modelle v.a. bei experimentellen Settings Verwendung, wobei am häufigsten *Repeated measures*- und *Split plot*-Designs sowie Kombinationen daraus vorkommen. Aber auch bei nicht-experimentellen Beobachtungsdaten finden gemischte Modelle zunehmend Verwendung, um räumliche und zeitliche Abhängigkeiten korrekt in der Statistik abzubilden.

### <span id="page-130-2"></span>Beispiel 1: Repeated measures-Design

Wir schauen uns hier noch einmal das Beispiel des Düngeversuchs an, das wir oben mittels **aov** berechnet haben.

Hier wird das LMM mit dem Package glmmTMB und nur mit random intercept modelliert. Was in der ANOVA Error(PlantID) war, wird hier zu (1 | PlantID). Die Syntax in anderen Packages für gemischte Modelle kann geringfügig abweichen.

```
# Als Imm
pf_Imm <- glmmTMB(PlantHeight ~ Treatment * Time + (1 | PlantID),
family = gaussian,
REML = TRUE,
data = plantf)</pre>
```

Die Ergebnisse aus dem Modell kann man mit den Befehlen Anova (Kurzfassung) und summary (weitere Details) extrahieren:

Anova(pf\_lmm)

Analysis of Deviance Table (Type II Wald chisquare tests)

Response: PlantHeight

Chisq Df Pr(>Chisq)

Treatment 43.351 2 3.859e-10 \*\*\*

Time 1146.390 3 < 2.2e-16 \*\*\*

Treatment:Time 126.444 6 < 2.2e-16 \*\*\*

Verglichen mit der ANOVA mit Error-Term bleiben die Signifikanzlevels gleich, aber die exakten p-Werte unterscheiden sich. Da auch die Interaktion signifikant ist, braucht es keine Modellvereinfachung. Wir sollten aber noch das Modell validieren, Pseudo-*R*<sup>2</sup> berechnen (siehe hierzu das nächste Beispiel) und eine Visualisierung erzeugen, da sonst Interaktionen schwer zu verstehen sind:

# Darstellung (Interaktions Plot)

# Darstellung (Interaktions Plot)

library("ggeffects")

pred <- ggpredict(pf\_lmm, terms = c("Time", "Treatment"))</pre>

plot(pred) +

theme\_classic() +

theme(plot.title = element\_blank())

![](_page_132_Figure_0.jpeg)

Man sieht, dass die beiden Haupteffekte (Treatment und Time) sich beide stark auswirken: Das Wachstum nimmt über die Zeit zu und Stickstoffzugabe wirkt deutlich stärker als die beiden anderen Zusätze. Zudem gibt es einen synergistischen Effekt von Zeit und Stickstoff (der sich im signifikanten Interaktionsterm bemerkbar macht).

### <span id="page-132-0"></span>**Beispiel 2:** *Split plot***-Design**

Das folgende Beispiel zeigt eine typische Split-Plot-Versuchsanordnung, wobei zusätzlich auch eine Messwiederholung stattfand. Es geht um unterschiedliche Managementvarianten zur Erhaltung artenreichen Graslandes auf einem grossen Truppenübungsplatz in Deutschland. Die Studie ist veröffentlich und enthält in den Anhängen mustergültig alle Daten in wohldokumentierten Formaten (Riesch et al. 2020).

Es wurden zufällig fünf Untersuchungsgebiete (*sites*) ausgewählt, in denen jeweils der gleiche Versuchsblock implementiert wurde, bestehend aus dem Management (*treatment*) und der Frage, ob wilde Grossherbivoren Zugang zur Fläche hatten (*plot type*) (Abb. 6.1). Je ein Drittel jeder Untersuchungsfläche (zufällig zugewiesen) blieb gänzlich ungenutzt(U), wurde zu Beginn kontrolliert abgebrannt und danach sich selbst überlassen (B) oder wurde jährlich gemäht (M). Innerhalb jedes Drittels wiederum wurde (zufällig zugewiesen) die Hälfte eingezäunt (F = *fenced* vs. O = *open*), um die Beweidung durch Grossherbivoren zu verhindern. Innerhalb jedes Sechstels in jeder der fünf Untersuchungsgebiete wurde dann der Zustand der Vegetation auf kleinen zufälligen Probeflächen (dunkelgrün) in jedem Untersuchungsjahr erhoben.

Abb. 6.5. Versuchsdesgin (aus Riesch et al. 2020).

Dieses Samplingdesign kann man folgendermassen in einem LMM implementiere (hier wurde für SR = *species richness* eine Normalverteilung angenommen – und im Residualplot geprüft – obwohl es sich dabei um Ganzzahlen handelt und man auch für eine Poisson-Verteilung hätte plädieren können, siehe Abschnitt zu GLMMs weiter unten). Das globale Modell mit allen möglichen Interaktionen sieht folgendermassen aus (year wurde dabei als Faktor, nicht als Zahl behandelt, da nur zwei Jahre verglichen werden):

```
# REML = TRUE : (Restricted maximum likelihood) v.s 
# REML = FALSE: Maximum likelihood (ML) 
# Bei REML sind die estimates genauer, aber REML sollte nicht für likelihood 
# ratio test (drop1) benutzt werden
# Dies ist nur relevant für Gaussian mixed models (LMM) nicht für GLMMs
# 2.1 Model fitten
lmm_1 <- glmmTMB(SR ~ year * treatment * plot_type + 
(1| site_code/treatment/plot_type), 
family = gaussian, 
REML = FALSE,
data = glex)
Eine einfache Übersicht über die Ergebnisse (nur die Signifikanzen) erhält man mit dem Befehl
Anova:
Anova(lmm_1)
Analysis of Deviance Table (Type II Wald chisquare tests)
Response: SR
Chisq Df Pr(>Chisq) 
year 58.6751 1 1.860e-14 ***
treatment 5.3910 2 0.067509 . 
plot_type 3.1397 1 0.076406 . 
year:treatment 27.5733 2 1.029e-06 ***
year:plot_type 8.0419 1 0.004571 ** 
treatment:plot_type 3.6181 2 0.163812 
year:treatment:plot_type 0.9435 2 0.623917
```

Wie man sieht, sind viele Terme nicht signifikant, man muss das Modell also schrittweise vereinfachen. Das geschieht mit dem drop1-Befehl, hier aber anders als bei den linearen Modellen mit Chi<sup>2</sup> als Teststatistik:

# Model optimierung

```
drop1(lmm_1, test = "Chi")
```

Single term deletions

Model:

SR ~ year \* treatment \* plot\_type + (1 | site\_code/treatment/plot\_type)

Df AIC LRT Pr(>Chi)

<none> 385.27

year:treatment:plot\_type 2 382.20 0.92894 0.6285

Laut drop2 müssen wir also zunächst die Dreifachinteraktion streichen, die auch in der ANOVA-Tabelle den höchsten p-Wert hatte (also am wenigsten signfikant war):

lmm\_2 <- update(lmm\_1,~. -year:treatment:plot\_type)

Das macht man so lange (siehe Demo), bis nur noch signifikante Terme im Modell verbleiben. Allerdings muss man bei signifikanten Interaktionen jeweils die zugrundliegenden Basis-Terme beibehalten, selbst wenn diese nicht signifikant sind.

Das so erhaltene minimal adäquate Modell, muss man dann noch einer Modellvalidierung unterziehen, was für GLMs, LMMs und GLMMs am besten mit dem DHARMa-Package geschieht, das auf Randomisierungen/Simulationen beruht (wie schon kurz im Statistik 5 angesprochen). Praktischerweise warnt DHARMa im Output direkt, wenn irgendeine Modellvoraussetzung verletzt ist. Weitere Residualplots werden in der Demo gezeigt.

# Model validierung mit dem package "DHARMa"

# Detailierte Model validation mit dem package

set.seed(123)

simulationOutput <- simulateResiduals(fittedModel = lmm\_4, plot = TRUE, n = 1000)

![](_page_135_Figure_1.jpeg)

Anders als im base R-Output, sind die QQ-Plots (für das Überprüfung der Normalverteilung der Residuen) links, und der Residual vs. predicted-Plot (für die Überprüfung der Varianzhomogenität und Linearität) rechts. Als Lesehilfe sind im rechten Plot zudem drei geglättete Kurven für die 75 %, 50 % und 25 % Quantile gezeigt. Wenn die obere und untere Kurve einen Keil bilden, dann hätten wir Varianzinhomogenität. Wenn die Punkte einer zu jeder der drei Kurven eine «Wurst» bilden, wäre die Linearität verletzt.

Da hier keinerlei Verletzungen der Modellvoraussetzungen vorliegen, können wir noch (a) die Interaktionsgrafik plotten (es gibt ja zwei signifikante Interaktionen, siehe Demo) und die erklärte Varianz berechnen:

r2(lmm\_4)

# R2 for Mixed Models

Conditional R2: 0.688

Marginal R2: 0.502

Fixed und random factors zusammen erklären also 68.8% der Varianz, die Faktoren year, treatment und plot\_type dagegen 50.2%,

### <span id="page-135-0"></span>**Beispiel 3: LMM mit "random slope" und "random intercept"**

Die beiden bisherigen LMM-Beispiele hatten nur Kategorien (Faktoren) als Prädiktoren, entsprachen daher im Prinzip einer ANOVA. Daher hatten sie nur einen sogenannten random intercept (s.o.) LMMs kann man aber auch analog zu linearen Regressionen und ANCOVAs anwenden. Dann kann

zwischen den Kategorien des random factors (Versuchsblöcke, Versuchsindividuen) nicht nur der Achsenabschnitt (random intercept), sondern auch die Steigung (random slope) zufällig variieren (siehe Abb. 6.4). Im Prinzip hätten wir das im vorigen Beispiel des

Graslandmanagementexperiments schon so angehen können, wenn wir das Jahr als metrische Variable belassen hätten. Da es aber nur zwei Jahre gab, wurden diese zu einem Faktor umgruppiert.

Im folgenden Beispiel (eingebauter Datensatz sleepstudy aus dem Package lme4) wurde bei 18 Versuchspersonen die Wirkung von zunehmenden Schlafentzug auf die Reaktionszeit (in ms) gemessen. Bei jeder Versuchsperson wurde der Effekt an den Tagen 2–9 des Versuchs je einmal gemessen (Tage 0 und 1 sind die Trainingsphase und bleiben daher unberücksichtigt).

Die Visualisierung mit einem Interaktions-Plot (Code in der Demo), legt nahe, dass sich die Versuchspersonen nicht nur in ihrer Baseline der Reaktionszeit (Achsenabschnitt), sondern auch in der Auswirkung des Schlafentzugs (Steigung) unterscheiden:

![](_page_136_Figure_4.jpeg)

Statt eines Modells nur mit random intercept (lmm\_1) fitten wir hier also ein Modell mit random intercept und random slope (lmm\_2). Die Möglichkeit, dass die Veränderung der Reaktionszeit über die Tage je nach Versuchsperson unterschiedlich ausfällt, wird dadurch (Days | Subject) anstelle von (1 | Subject) codiert.

lmm\_1 <- glmmTMB(Reaction ~ Days + (1 | Subject),

family = gaussian,

data = sleepstudy\_2)

```
lmm_2 <- qlmmTMB(Reaction ~ Days + (Days | Subject),</pre>
family = gaussian, data = sleepstudy 2)
Der Output ergibt Folgendes:
summary(lmm 2)
Family: gaussian (identity)
Formula: Reaction ~ Davs + (Davs | Subject)
Data: sleepstudy_2
AIC BIC logLik deviance df.resid
1416.1 1433.9 -702.0 1404.1 140
Random effects:
Conditional model:
Groups Name Variance Std.Dev. Corr
Subject (Intercept) 992.63 31.506
Davs 45.78 6.766 -0.25
Residual 651.60 25.526
Number of obs: 144, groups: Subject, 18
Dispersion estimate for gaussian family (sigma^2): 652
Conditional model:
Estimate Std. Error z value Pr(>|z|)
(Intercept) 245.097 9.260 26.469 < 2e-16 ***
Days 11.435 1.845 6.197 5.75e-10 ***
Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
```

Man sieht im mittleren Teil des Outputs, dass zwei *random effects* geschätzt wurden (Intercept und Days), wie bei *random effects* üblich nur als Varianz (ohne estimates für die Effektgrösse/-richtung). Am Ende kommen die Schätzwerte und Signifikanzen für die eigentlich interessierenden Variablen (*fixed effects*), wiederum Intercept und Days. Hier gibt es estimates und *p*-Werte. Das ist also unser Modell (Reaction = 245 ms + 11 ms/day) unter Berücksichtigung der Variation zwischen den Versuchspersonen. Da intercept und days signifikant sind, sind wir schon beim finalen Modell.

Es folgt dann noch, wie üblich, die Modelldiagnostik, die Berechnung des Pseudo- $\mathbb{R}^2$  und ggf. die Erstellung einer Ergebnisgrafik (siehe Demo).

# <span id="page-138-0"></span>**Generalized linear mixed effect models (GLMMs)**

### <span id="page-138-1"></span>**Die Idee**

*Generalized linear mixed effect models* (GLMMs) verallgemeinern LMMs für Daten, deren Residuen die Erfordernisse von Normalität und Varianzhomogenität nicht erfüllen, insbesondere Binär- und Zähldaten. Zugleich verallgemeinern sie GLMs, um Folgendes modellieren zu können:

- Geschachtelte Daten •
- Zeitliche Korrelationen zwische Beobachtungen •
- Räumliche Korrelationen zwischen Beobachtungen •
- Heterogenität •
- Messwiederholungen •

Während dies alles wundervolle und oft benötigte Eigenschaften sind, sollte man sich auch der Nachteile/Limitierungen bewusst sein, wie die folgenden Zitate aus einem der führenden Lehrbücher zu GLMMs (Zuur et al. 2009) zeigen:

"GLMM are at the frontier of statistical research" "This means that available documentation is rather technical and there are only few, if any, textbooks aimed at ecologists" "There are multiple approaches for obtaining estimated parameters" "There are at least four packages in R that can be used for GLMM" "This makes model selection in GLMM more of an art than a science"

Durch erhebliche Weiterentwicklungen in GLMMs seit 2009 gilt das so heute nicht mehr. Die folgende Empfehlung zu Anwendung von GLMMs von Zuur et al. (2009) gilt aber weiterhin (der natürlich auch sonst in der Statistik gilt, hier aber besonders wichtig ist):

"**When applying GLMM, try to keep the models simple or you may get numerical estimation problems.**"

Da komplexe GLMMs computertechnisch aufwändig sind, sollten hier (ggf. auch schon bei LMMs) die metrischen (kontinuierlichen) Prädiktorvariablen vor der Analyse standardisiert werden, so dass sie jeweils einen Mittelwert von 0 und eine Standardabweichung von 1 aufweisen (so-genannter zscore). Das geht auf zwei Weisen:

- Eingebaute Funktion scale •
- Selbstgeschriebene Funktion function(x) { (x mean(x)) / sd(x)} •

### <span id="page-138-2"></span>**Ein Beispiel und seine Umsetzung in R**

Befall von Rothirschen (*Cervus elaphus*) in spanischen Farmen mit dem Parasiten *Elaphostrongylus cervi*. Modelliert wird Vorkommen/Nichtvorkommen von L1-Larven dieser Nematode in Abhängigkeit von Körperlänge und Geschlecht der Hirsche. Erhoben wurden die Daten auf 24 Farmen.

Wir können das Ganze wie bisher mit einem binomialen GLM analysieren:

DE.glm <- glm(Ecervi ~ Length \* Sex + Farm, family = binomial, data = DeerEcervi) summary(DE.glm)

#### Coefficients:

v Estimate Std. Error z value Pr(>|z|) (Intercept) -1.796e+00 5.900e-01 -3.044 0.002336 \*\* Length 4.062e-02 7.132e-03 5.695 1.24e-08 \*\*\* Sexmale 6.280e-01 2.292e-01 2.740 0.006150 \*\* FarmAU 3.340e+00 7.841e-01 4.259 2.05e-05 \*\*\* FarmBA 3.510e+00 7.150e-01 4.908 9.19e-07 \*\*\* […] FarmVY 3.974e+00 1.257e+00 3.162 0.001565 \*\*

Length:Sexmale 3.618e-02 1.168e-02 3.097 0.001953 \*\*

Das Modell, das wir erzeugt haben, liesse sich folgendermassen visualisieren:

![](_page_139_Figure_3.jpeg)

Abb. 6.6. Darstellung der Ergebnisse des GLM-Modells für den Parasiten-Datensatz (aus Zuur et al. 2009).

Für unseren Zweck hat die Lösung mit einem GLM zwei Nachteile:

- Farm "verbraucht" 23 Freiheitsgrade, obwohl wir nicht am Farmeffekt interessiert sind. •
- Wir bekommen ein Modell für jede einzelne Farm, aber kein farmunabhängiges Modell. •

Deshalb re-analysieren wir die Daten mit einem GLMM. Hier beispielhaft analysieren wir. dieses GLMM mit glmmTMB aus dem Package glmmTMB (nach erfolgter Standardisierung). Die GLMM-Definition ist identisch zu einer LMM-Definition, ausser dass statt family = gaussian, jetzt family = binomial steht (bzw. in einem Poisson-GLMM dann family = poisson):

# Model fitten. Die function "scale" standardisiert die kontinuierliche variable Hischlänge:

# ( DeerEcervi\$Length - mean(DeerEcervi\$Length)) / sd(DeerEcervi\$Length )

```
# Model fitten
```

glmm\_1 <- glmmTMB(Ecervi ~ scale(Length) \* Sex + (1 | Farm),

family = binomial,

data = DeerEcervi)

Das Ergebnis ist wie folgt:

summary(glmm\_1)

Family: binomial ( logit )

Formula: Ecervi ~ scale(Length) \* Sex + (1 | Farm)

Data: DeerEcervi

AIC BIC logLik deviance df.resid

832.6 856.1 -411.3 822.6 821

Random effects:

Conditional model:

Groups Name Variance Std.Dev.

Farm (Intercept) 2.393 1.547

Number of obs: 826, groups: Farm, 24

Conditional model:

Estimate Std. Error z value Pr(>|z|)

(Intercept) 0.9397 0.3579 2.625 0.00865 \*\*

Length\_std 0.7638 0.1363 5.604 2.09e-08 \*\*\*

Sexmale 0.6245 0.2242 2.785 0.00535 \*\*

Length\_std:Sexmale 0.7027 0.2241 3.135 0.00172 \*\*

Wie wir das schon von ANOVAs mit Error-Term oder LMMs kennen, ist die Ergebnistabelle in einen Teil für die Random effects und einen Teil für die Fixed effects aufgeteilt. Für Farm gibt es jetzt aber anders als beim GLM nicht 23 Schätzwerte, sondern nur einen für die Varianz/Standardabweichung. Der untere Teil entspricht dagegen dem Output eines GLMs, wenn wir Farm ignoriert hätten: wir haben die Effekte von Grösse, Geschlecht und deren Interaktion (alle signifikant).

Was sagen uns die Ergebnisse nun? Dazu visualisieren wir die Ergebnisse am besten. Da das Modell für die standardisierten Körperlängen gerechnet wurde, werden diese auch mittels predict\_response und ggplot dargestellt (Code in der Demo). Will man die Zahlen/Visualisierungen für die originalen Körpergrössen in cm haben, muss man sie zurücktransformieren (Code in Demo):

![](_page_141_Figure_0.jpeg)

### <span id="page-141-0"></span>**Random vs. fixed factors**

Wann sollten wir *random factors* nehmen, wann *fixed factors*? Im Hirsch-Beispiel ist statistisch klar, dass wir die Farm-Identität in unser statistisches Modell aufnehmen müssen, da auf jeder Farm mehrere Hirsche untersucht wurden und unser Wissen über das universelle Phänomen der **räumlichen Autokorrelation** es höchstwahrscheinlich macht, dass sich die Hirsche einer einzelnen Farm (wg. räumlicher Nähe) ähnlicher sind als zufällig herausgegriffene Farm-Hirsche aus ganz Spanien.

Ob wir die Farm-Identität dagegen als *fixed factor* aufnehmen (d. h. ein GLM rechnen) oder als random factor (d. h. ein GLMM rechnen), hängt von unserer Frage ab. In der Studie ging es um ein allgemeines farmunabhängiges Modell, wie sich der Parasitenbefall in Abhängigkeit von Geschlecht und Grösse entwickelt. Dann wäre unser Vorgehen richtig, Farm als random factor zu definieren. Wir dürfen und können dann aber keine Aussage über eine einzelne Farm treffen. Wenn uns dagegen interessiert, ob und wie sich die Farmen bezüglich Parasitenbefall unterscheiden, etwa weil sie unterschiedliche Hygienekonzepte oder Populationsdichten haben, dann müssen wir Farm als *fixed factor* behandeln (also ein GLM rechnen). Ob wir in einer solchen Situation ein GLM oder ein GLMM rechnen, hängt also von unserer genauen Fragestellung ab.

# <span id="page-142-0"></span>**LMs, GLMs, LMMs und GLMMs im Rückblick und Überblick**

Zum Abschluss der fünf inferenzstatistischen Lektionen seien noch einmal die grundlegenden Ähnlichkeiten und Unterschiede von LMs, GLMs, LMMs und GLMMs zusammengefasst:

LMs: *Linear models* •

GLMs: *Generalized linear models* LMMs: *Linear mixed effect models* • •

GLMMs: *Generalized linear mixed effects models* •

|                                                                                             |      | Varianzen konstant, Normalverteilung der Residuen             |                                            |
|---------------------------------------------------------------------------------------------|------|---------------------------------------------------------------|--------------------------------------------|
|                                                                                             |      | ja                                                            | nein                                       |
| gkeiten<br>essungen,<br>ngen von<br>random<br>ors                                           | ohne | LMs<br>(Im, aov)                                              | GLMs<br>(glm)                              |
| Abhängigkeiten<br>zwischen Messungen,<br>Schachtelungen von<br>Variablen, random<br>factors | mit  | LMMS (packages nlme, lme4, einfache Fälle auch aov in Base R) | GLMMs<br>(packages MASS,<br>Ime4, glmmPQL) |

Aktuell bietet sich sowohl **für LMMs und GLMMs das Package glmmTMB** als besonders leistungsstark an.

## <span id="page-142-1"></span>**Zusammenfassung**

- Wenn in einem ANOVA-Design **Schachtelungen oder Abhängigkeiten** vorliegen, muss man diese im Modell spezifizieren, was entweder als Error in aov oder als *«random factor»* in glmmTMB (package glmmTMB) geht. •
- Während GLMs lineare Modelle bezüglich der geforderten Residuen- und Varianzstruktur verallgemeinern, leisten *linear mixed effect models* **(LMMs)** dies bezüglich unterschiedlichster Abhängigkeiten zwischen Beobachtungen. •
- Meist verwendet man nur *random intercepts*; zusätzlich *random slopes* sollte man testen, wenn ein Prädiktor kein Faktor, sondern eine metrische Grösse ist. •
- *Generalized linear mixed effect models* **(GLMMs)** schliesslich ermöglichen, beide Typen von Abweichungen von den Voraussetzungen linearer Modelle zu berücksichtigen. •

# <span id="page-143-0"></span>**Weiterführende Literatur**

- **Crawley, M.J. 2015.** *Statistics An introduction using R***. 2nd ed. John Wiley & Sons, Chichester, UK: 339 pp.** •
  - **Chapter 8: Analysis of Variance (pp. 173–182)** ◦
- **Lepš, J. & Šmilauer, P. (2020)** *Biostatistics with R An introductory guide for field biologists***. Cambridge University Press, Cambridge: 365 pp.** •
- Logan, M. 2010. *Biostatistical design and analysis using R. A practical guide*. Wiley-Blackwell, Oxford, UK: 546 pp., v.a. •
  - pp. 399-447 (split-plot und repeated measures ANOVAs) ◦
- Zuur, A. E., Ieno, E. N., Walker, N. J., Saveliev, A. A., Smith, G. M. (eds.) 2009. *Mixed effects models and extension in ecology with R*. Springer, New York: 576 pp. •
- **Zuur, A.E., Hilbe, J.M. & Ieno, E.N. 2013.** *A beginner's guide to GLM and GLMM with R – A frequentist and Bayesian perspective for ecologists***. Highland Statistics, Newburgh: 253 pp.** •

## <span id="page-143-1"></span>**Quelle des Beispiels**

Riesch, F., Tonn, B., Stroh, H.G., Meißner, M., Balkenhol, N. & Isselstein, J. (2020) Grazing by wild red deer maintains chacteristic vegetation of seminatural open habitats: Evidence from three-year exclusion experiment. *Applied Vegetation Science* 23: 522–538. •

# <span id="page-143-2"></span>**Statistik 7**

Einführung in multivariat-deskriptive Methoden; Ordinationen

**Statistik 7 führt in multivariat-deskriptive Methoden ein, die dazu dienen Datensätze mit mehreren abhängigen und mehrenen unabhängigen Variablen zu analysieren. Dabei betonen Ordinationen kontinuierliche Gradienten und fokussieren auf zusammengehörende Variablen, während Cluster-Analysen Diskontinuitäten betonen und auf zusammengehörende Beobachtungen fokussieren. Ordinationen dienen dazu, die Strukturen in multivariaten Datensätzen via Dimensionsreduktion zu visualisieren. Das Prinzip und die praktische Implementierung wird detailliert am Beispiel der Hauptkomponentenanalyse (PCA) erklärt. Neben der Beschreibung der Datenstruktur in komplexen Datensätzen kann eine PCA auch dazu dienen, aus diesen unabhängie Variablen zu generieren, die anschliessend in einer multiplen Regression als Prädiktoren genutzt werden können.**

### <span id="page-144-0"></span>**Lernziele**

#### Ihr…

- versteht die grundlegenden Unterschiede **multivariat-deskriptive Verfahren** von den bislang besprochenen **inferenzstatistischen Verfahren** und für welche Art von Daten/ Fragen sie sich gut anwenden lassen; •
- versteht, **was Ordinationen sollen**, was sie leisten können und was nicht; und •
- könnt das **Prinzip einer PCA** beschreiben, sie implementieren, und ihren Ergebnisoutput interpretieren •

## <span id="page-144-1"></span>**Einführung in "multivariate" Methoden**

### <span id="page-144-2"></span>**Was ist mit "multivariat" gemeint?**

Was ist mit **"multivariat"** gemeint? Zunächst einmal sagt das nur, dass pro Beobachtung (*observation*) **mehr als zwei** Variablen erhoben werden, deren Beziehungen zueinander analysiert werden. Im Wortsinne waren also auch schon die zweifaktorielle ANOVA und die multiple Regression "multivariate" Methoden.

Die folgende Tabelle fasst die schon besprochenen und noch kommenden statistischen Verfahren bezüglich der Anzahl von Prädiktor- und Antwortvariablen zusammen:

| Prädiktor(en)        | Antwortvariable(n) | Verfahren                                            |
|----------------------|--------------------|------------------------------------------------------|
| 2 ohne               | Zuordnung          | Korrelation, Assoziationstest                        |
| 1                    | 1                  | einfache lineare Regression,<br>einfaktorielle ANOVA |
| ≥ 2                  | 1                  | multiple Regression, mehrfaktorielle ANOVA, ANCOVA   |
| viele ohne Zuordnung |                    | Ondination on Charten analyses                       |
| viele                | viele              | Ordinationen, <i>Cluster analyses</i>                |

In der Literatur wird der Begriff **"multivariat"** jedoch oft nur für die letzte Gruppe von Verfahren, also **Ordinationen und Cluster-Analysen**, gebraucht. Diese bilden den Gegenstand von Statistik 7– 8.

### <span id="page-144-3"></span>**Inferenzstatistik vs. deskriptive Statistik**

**Bislang** haben wir statistische Verfahren überwiegend zum Testen von Hypothesen verwendet (inklusive des impliziten Hypothesentestens, wenn man eine offene Forschungsfrage beantwortet): **Inferenzstatistik (schliessende Statistik)**.

\***Ordinationen und Cluster-Analysen** sind überwiegend **deskriptive Statistik** (ohne spezielle Zusatzschritte erlauben sie kein Testen von Hypothesen!).

### <span id="page-145-0"></span>**Beispiele multivariater Datensätze**

Multivariate Datensätze sind in unserer "datenreichen" Welt allgegenwärtig z. B.:

- **Bodenproben**, an denen viele unterschiedliche physikalische und chemische Variablen, ggf. auch noch in verschiedenen Horizonten gemessen wurden. •
- **Klimadaten** von Messstationen: zahlreiche Variablen wie Mittel/Minima/ Maxima von Temperatur/Niederschlag/Sonnenschein/Bewölkung/Windstärke usw. und das für jeden Monat. •
- Zusammensetzungen von lokalen **Pflanzengesellschaften oder Tiergemeinschaften**: hier sind die Deckungen bzw. Individuenzahlen der einzelnen Arten die Variablen •
- Ergebnisse von **Befragungen von Konsumenten**: viele Variablen zu Präferenzen, Einstellungen usw. •

### <span id="page-145-1"></span>**Ziele multivariat-deskriptiver Analysen**

Im Prinzip können wir auch bei solchen Beobachtungsdaten mit vielen abhängigen Variablen wie bisher jede einzeln testen:

- Das kann **vorteilhaft** sein, **wenn man konkrete Hypothesen testen will** (was ja mit multivariat-deskriptiven Methoden normalerweise nicht geht). •
- Ein Problem sind die vielen Tests mit dem gleichen Datensatz, die zu einer **"Inflation" der Typ I-Fehlerrate** führen (wenn ich 20 Tests durchführe, würde ja bei α = 0.05 einer rein zufällig eine Signifikanz anzeigen, selbst wenn eigentlich für keinen eine Beziehung besteht). Für dieses Problem gibt es aber Korrekturmöglichkeiten (z. B. "Bonferroni"-Korrektur). •
- Problematischer ist, dass es sehr **schwierig** ist, **aus den vielen Einzelergebnissen am Ende ein aussagekräftiges Gesamtbild zu synthetisieren**. •

Hier setzen die multivariat-deskriptiven Methoden mit ihren beiden Hauptzielen an:

- **Muster und Beziehungen** im *n*-dimensionalen Hyperraum erkennen und beschreiben. •
- **Dimensionsreduktion**: die wesentliche Information aus den n Dimensionen wird auf zwei bis wenige Dimensionen reduziert, die vorstellbar und visualisierbar sind. •

Der **-dimensionale Hyperraum** ist das Konzept, das uns durchgängig bei den multivariatdeskriptiven Methoden begleitet. Dahinter verbirgt sich die Idee, dass jede der *n* Variablen eine orthogonale Achse ist (d. h. rechtwinklig auf den anderen Achsen stehend), auf der die Ausprägungen der Variablen (metrisch oder kategorial) aufgetragen sind. Während wir uns einen 3 dimensionalen Raum noch vorstellen können, ist es mit der Vorstellungskraft bei vier oder gar 100 Dimensionen schnell zu Ende. Aber das ist ja genau der Grund für die multivariat-deskriptiven Methoden.

### <span id="page-146-0"></span>**Zwei komplementäre Ansätze**

Innerhalb der multivariat-deskriptiven Statistik stellen **Ordinationen** und **Cluster-Analysen (Klassifikationen)** zwei **komplementäre Ansätze** dar. Sie betonen unterschiedliche Aspekte des Datensatzes und können oftmals sogar sinnvoll parallel verwendet werden. Die wesentlichen Unterschiede zeigt die folgende Tabelle:

Was damit gemeint ist, werden wir sehen, wenn wir in den folgenden Lektionen teilweise Ordinationen und Cluster-Analysen auf denselben Datensatz anwenden.

# <span id="page-146-1"></span>**Hauptkomponentenanalyse (PCA) – das Prinzip**

Ordinationen versuchen, im *n*-dimensionalen Raum der (Antwort-) Variablen **diejenigen Ebenen zu finden, welche die meiste Varianz erklären**. Dies geschieht bei der Hauptkomponentenanalyse (*principle component analysis*, PCA) durch die folgenden Schritte (ähnlich bei anderen Ordinationsverfahren):

- **Zentrieren** der Punktwolke, so dass der Schwerpunkt im Ursprung des Koordinatensystems liegt. •
- **Rotieren** der Punktwolke, bis die erste Achse die maximal mögliche Varianz abbildet. •
- Nach Fixierung der ersten Achse Fortsetzen des Rotierens, bis die zweite Achse wiederum das maximal Mögliche der verbleibenden Varianz abbildet, usw. bis zur *n*-ten Achse. •
- **Visualisierung** der Ergebnisse bei Beschränkung auf die relevanten ersten Achsen. •

Um diese Idee zu visualisieren, nehmen wir ein System von nur zwei Variablen, da wir diese noch auf einer Ebene (d.  h. im gedruckten Skript) visualisieren können. Stellen wir uns sechs Beobachtungspunkte entlang eines Umweltgradienten (z.  B. Meereshöhe) vor. An jedem dieser Beobachtungspunkte wird die Häufigkeit von zwei Arten (Art 1: gefüllte Kreise, Art 2: offene Kreise) ermittelt, etwa folgendermassen:

![](_page_147_Figure_0.jpeg)

Wenn wir das jetzt **im "Artenraum"** zeigen, also mit der Häufigkeit von Art 1 auf der *x*-Achse und der Häufigkeit von Art 2 auf der *y*-Achse, dann bekämen wir das **grüne** Muster. **Zentriert** (d. h. so dass die Mittelwerte aller *x*- und *y*-Werte jeweils 0 sind), ergibt sich die **rote** Figur. Dies wird schliesslich so **rotiert**, dass die maximale Varianz (hier im simplen Fall einfach die Distanz zwischen den extremen Punkten) paralle zur *x*-Achse liegt (**blau**).

![](_page_148_Figure_0.jpeg)

### <span id="page-148-0"></span>**PCA: Voraussetzungen und Anwendung**

Das im vorigen Abschnitt skizzierte Vorgehen, ist genau das, was eine **Hauptkomponentenanalyse (***Principal component analysis***, PCA)** macht:

- Basiert auf einer **linearen Beziehung** zwischen den Attributen. •
- Achsen sind **orthogonal** (und die Varianzen daher additiv). •
- Die ursprünglichen **Distanzen** zwischen den Objekten (Beobachtungen) bleiben daher **unverändert**. •

#### PCAs eignen sich für:

Einfache Visualisierung, wenn die Linearität gegeben ist. •

Bei multiplen Regressionen mit vielen, korrelierten Prädiktoren kann man die PCA-Achsen als **synthetische Prädiktoren** verwenden, da sie vollständig unkorreliert sind. •

PCAs eignen sich *nicht* (und das gilt fast immer für Daten zur Artenzusammensetzung ökologischer Gemeinschaften) für:

- Nicht-lineare Beziehungen. •
- Viele Nullen in der Matrix. •

Die PCA findet die beste Rotation mittels der sogenannten **"Eigenanalyse"**, wie die folgende Abbildung veranschaulicht:

Species 
$$(1,...,b)$$

$$X'$$

$$G_{(1,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{(2,...,b)}$$

$$G_{$$

![](_page_149_Figure_7.jpeg)

(aus Wildi 2013)

#### Dabei gilt:

PCA als das einfachste Ordinationsverfahren sind bereits in Base R implementiert (Befehl prcomp). Es gibt daneben Packages, die PCA zusammen mit diversen anderen Ordinationstechniken enthalten, insbesondere vegan für ökologische Analysen.

### <span id="page-150-0"></span>**Beispiel in R: Umweltvariablen im Fluss Doubs**

In unserem Beispiel wurden an 29 Stellen des Flusses Doubs jeweils die 10 gleichen Umweltvariablen gemessen. Nun ist die Frage, wie sich diese 10-dimensionale Information vereinfache lässt.

Wir führen die PCA mit dem prcomp-Befehl aus. Da die verschiedenen Umweltvariablen auf unterschiedlichen Skalen gemessen wurden (z.B. mg L-1 oder m<sup>3</sup> s-1) sollte man sie sinnvollerweise vor der Durchführung der PCA standardisieren. Das geschieht mit dem Parameter scale = TRUE, der jede der Variablen so transformiert, dass sie einen Mittelwert von 0 und eine Standardabweichung von 1 hat.

*# Berechnen der PCA*

pca\_1 <- prcomp(env, scale = TRUE)

Jetzt kann man die Ergebnisse mit drei verschiedenen Outputs erkunden:

summary(pca\_1)

Importance of components:

PC1 PC2 PC3 PC4 PC5 PC6 PC7

Standard deviation 2.3261 1.4081 0.99377 0.82554 0.57389 0.54229 0.40525

Proportion of Variance 0.5411 0.1983 0.09876 0.06815 0.03293 0.02941 0.01642

Cumulative Proportion 0.5411 0.7393 0.83809 0.90624 0.93917 0.96858 0.98501

PC8 PC9 PC10

Standard deviation 0.33106 0.15186 0.13146

Proportion of Variance 0.01096 0.00231 0.00173

Cumulative Proportion 0.99597 0.99827 1.00000

Der Befehl summary zeigt uns die relative Bedeutung der 10 generierten PC-Achsen, in der ersten Zeile jeweils der Eigenwert, in der zweiten seine Übersetzung in einen Anteil erklärter Varianz und in der dritten schliesslich die kumulierte Varianz der 1. bis *i*. Achse. Die erklärte Varianz ist ein uns schon bekanntes Konzept. Die Gesamtvarianz ist alles, was im Datensatz mit seinen *n* Achsen drinsteckt (100%). Die PCA-Achsen sind nach absteigender erklärter Varianz nummeriert. Man sieht hier, dass die erste Achse allein schon mehr als die Hälfte der Varianz erklärt. Die erste und zweite Achse zusammen erklären bereits 74%.

pca\_1\$rotation

PC1 PC2 PC3 PC4 PC5 PC6

ele -0.32983498 0.37326508 0.206379458 0.19101532 -0.2108916 -0.13925126

slo -0.18939659 0.36225406 -0.317430615 -0.78012687 -0.2534671 -0.10409281 dis 0.29534136 -0.38102320 -0.289744571 -0.25273405 -0.2684698 0.30100160 pH -0.02798027 -0.30500230 0.833784024 -0.40105127 -0.1951586 0.07666589 har 0.29140671 -0.40748250 -0.128533282 0.05461084 -0.2491737 -0.71799621 pho 0.37752293 0.27210613 0.155636940 -0.10896147 0.1007383 -0.20179074 nit 0.39070251 0.01310715 -0.007977941 -0.20607662 0.5141959 0.23374094 amm 0.36361130 0.32397140 0.159353915 -0.06949906 0.2419581 -0.15450710 oxy -0.35471920 -0.20647070 -0.007373084 -0.25539560 0.5526433 -0.45522763 bod 0.35944351 0.32155396 0.106029560 0.05309465 -0.2837688 -0.17696504 PC7 PC8 PC9 PC10

ele 0.18472542 0.588745894 0.23188511 0.4176369609 slo -0.20463767 0.034575041 -0.01624550 -0.0715819377 dis 0.59712652 0.176111385 0.19635151 0.1759578515 pH -0.07146037 -0.007914091 0.02364683 -0.0214444926 har -0.28531107 0.261864429 0.04422096 0.0001391902 pho 0.34531100 0.146608797 -0.74268910 0.0644251748 nit -0.42339586 0.270495568 0.13496263 0.4636479419 amm 0.21872209 0.152261020 0.50422013 -0.5700251793 oxy 0.36532131 -0.222406219 0.12492546 0.2347031060 bod 0.03358753 -0.620662606 0.25544171 0.4357752560

Wie die PCA den *n*-dimensionalen Raum verdreht hat, sieht man, indem man auf \$rotation im PCA-Objekt zugreift. Diese Werte sind die Korrelationen der der Variablen mit den neuen synthetischen PC-Achsen, die sogenannten *Loadings*. Zur Interpretation einer Ordination werden diese oft als Pfeile in das Ordinationsdiagramm geplottet (s. u.).

pca\_1\$x

PC1 PC2 PC3 PC4 PC5 PC6

\$1 -4.06058121 3.3572582 -1.5353663864 -3.11664281 -0.440940815 0.023962858 \$2 -2.85884496 1.6453967 0.6199429169 0.81205916 0.462056595 1.198866058 \$3 -2.59500367 0.9087955 1.9223023314 0.08390276 -0.149900842 0.742123168 \$4 -2.42274201 0.5759475 0.2416999136 0.73737973 0.197031209 -0.175001441 \$5 -0.87891903 1.0132044 0.9242023016 0.92176239 -0.899225211 -0.317177629 \$6 -2.07214852 1.4521772 -0.0223558512 1.05958043 -0.018694903 0.245670558

S7 -2.16112216 0.1677976 0.4568713333 0.24335994 -0.322106920 -0.877019196 S8 -0.57361742 0.7209215 0.2639757108 1.22605607 -0.878760741 -0.203164295 S9 -1.35708234 0.9878134 -1.7146160465 0.66588881 -0.007739829 -0.393125521 S10 -0.79292243 -0.8705883 0.0009546047 -0.26509619 0.291231194 -0.650848271 S11 -1.36709366 -0.5303252 -0.8181608908 0.48791374 0.458423383 -0.563740808 S12 -1.22749339 -1.2640408 -0.0337087077 -0.04373209 0.156070410 -0.969587498 S13 -0.78848467 -1.4750236 1.0008336819 -0.52937272 0.125890673 -0.835849370 S14 -1.04150973 -1.8473507 2.4695198950 -1.16235808 -0.117675534 -0.019680069 S15 -0.49079952 -0.5350769 -0.3520651388 0.18345496 0.584620728 -0.025245565 S16 0.24701457 -0.6047699 -0.3687986865 0.13321152 0.579189656 -0.068332189 S17 0.09988521 -0.6508563 -0.3833031874 0.04976758 0.683326378 -0.024162612 S18 0.02438927 -0.7420695 0.1223176607 -0.23010483 0.691984141 0.214472693 S19 0.34858245 -0.6284685 -0.4163658010 -0.13136986 1.081653869 0.335357672 S20 0.25655489 -0.4423705 -0.9691575293 0.38503444 0.366563949 0.530706156 S21 0.14920132 -0.8509911 -0.0692153090 -0.02307061 -0.169105752 0.366684836 S22 4.40893902 1.7764650 1.0312263310 -0.27455931 -0.217479493 -0.607578015 S23 2.99431167 0.7625691 0.0170945415 0.48455983 -0.940755575 0.035682696 S24 7.11385299 3.0888496 0.4707839188 -0.34766485 0.841598956 -0.381766823 S25 2.49964796 0.2144704 -0.8136841889 0.34331209 -0.386714310 0.514435592 S26 1.60318946 -0.6308112 -0.1178042084 -0.23842040 -0.252238973 0.894423496 S27 1.90404098 -1.4844247 0.7045838208 -0.94039312 0.124061006 0.646597704 S28 1.42466912 -1.7701617 -2.2784706379 0.15724184 -0.607940975 0.004076669 S29 1.61408580 -2.3443369 -0.3532363923 -0.67170041 -1.234422275 0.359219148 PC7 PC8 PC9 PC10

S1 -0.16756651 -0.01661397 -0.0005434083 -0.027276628 S2 0.66409559 0.08312574 0.0453575992 -0.114126005 S3 0.36457987 -0.06164832 0.1363572490 0.106940451 S4 0.20481751 0.41948659 -0.1190803292 -0.057120717 S5 -0.33938509 0.29033210 0.1331611406 -0.012913680 S6 0.40988744 -0.32654553 -0.0386629851 0.296369679 S7 -0.11117406 0.48938544 0.0184021086 -0.012862367

S8 -0.67526691 0.44432628 -0.0427742137 -0.107371788 S9 -0.22123560 -0.10940926 -0.0297606988 0.019485234 S10 -0.17677815 0.17051596 -0.0891684003 0.197809147 S11 0.47423174 -0.36666506 0.0305048878 -0.036333811 S12 0.22914572 -0.15537004 0.0333334255 -0.133603754 S13 0.02658378 -0.24507682 0.0275604057 0.219092722 S14 0.17355943 -0.15968840 -0.2347153211 -0.143569558 S15 -0.48268849 -0.02834067 -0.1346994236 -0.055576670 S16 -0.32433001 -0.08783303 0.3085297270 0.140390082 S17 -0.07858369 0.12396263 -0.0949232855 -0.147315115 S18 0.06659440 -0.12827386 -0.2055645165 -0.014781123 S19 -0.24395665 0.13680466 0.2479536264 -0.103423285 S20 -0.31209067 -0.24618792 -0.0271824151 -0.091732053 S21 -0.25594533 -0.46246075 -0.0354205351 -0.180973464 S22 0.24323679 -0.72159949 0.1819244804 0.009669496 S23 -0.39736429 -0.53241824 0.0374850854 -0.145733335 S24 0.43932542 0.60742531 -0.0909990349 -0.048500568 S25 -0.15806719 -0.14778266 -0.4470511938 0.249196626 S26 -0.38708608 -0.06975558 0.1101065003 0.024382817 S27 -0.58223511 0.51151147 0.1409060157 0.199078478 S28 0.88253998 0.27851440 0.1417856127 0.037595473 S29 0.73515615 0.31027906 -0.0028221033 -0.066796286

Mit \$x im PCA-Objekt ist schliesslich codiert, wo im Ordinationsraum unsere 29 Beobachtungspunkte zu liegen kommen. Diese sogenannten *Scores* sind einfach die Koordinaten im n-dimensionalen Raum der PCA. Zur Interpretation einer Ordination werden diese oft als Punkte in das Ordinationsdiagramm geplottet (s. u.).

Ein wichtiges Ziel einer Ordination ist ja die Dimensionsreduktion. Hier stellt sich also die Frage, wie viele der ursprünglich 10 Achsen (Dimensionen) sind wirklich informativ. Das kann man mit einem sogenannten Screeplot visualisieren/testen, der die gefundenen Varianzen denen gegenüberstellt, die man mit einem Nullmodel (broken stick) erwarten würde. Screeplots kann man z.B. mit dem Package vegan erstellen:

p\_load("vegan")

# Visualisierung der Anteile erklärter Varianz, im Vergleich zu einem Broken-Stick-Modell screeplot(pca\_1, bstick = TRUE)

![](_page_154_Figure_0.jpeg)

In diesem Fall hat also die PC1 deutlich mehr Information als zu erwarten, die PC2 noch geringfügig mehr und alle weiteren Achsen haben weniger Information als zu erwarten. Hier können wir uns in der weiteren Interpretation also auf die Ordinationsebene beschränken, die von PC1 und PC2 gebildet wird.

Diese Visualisierung setzen wir jetzt um mit dem biplot-Befehl von Base R:

# Mit biplot von base R

biplot(pca\_1)

![](_page_155_Figure_0.jpeg)

Biplot meint, dass man sowohl die Loadings der Variablen (Pfeile) als auch die Positionen der Einzelbeobachtungen parallel darstellt. Das wird schnell etwas unübersichtlich und man kann mit verschiedenen Packages und diversen Einstellungen Ordinationsdiagramme übersichtlicher und schöner machen. In unserem Fall könnte das wie folgt aussehen (mit dem Package factoextra; R Code dazu in der Demo).

![](_page_156_Figure_0.jpeg)

Falls auch die dritte Achse noch bedeutsam wäre, könnte man zusätzlich einen Biplot der ersten und dritten Achse erstellen. Wenn es zu viele Variablen oder zu viele Beobachtungen gibt, kann man statt eines Biplots auch die Loadings und Scores in zwei separaten Abbildungen darstellen (Code dazu in der Demo).

Was sagt uns das Ordinationsdiagramm nun? Wir sehen, dass die erste Achse besonders hoch positiv mit Nitrat korreliert, während die zweite Achse stark negativ mit dem pH-Wert korreliert. Das bedeutet, dass Untersuchungsflächen mit hohen Nitrat- und niedrigen pH-Werten rechts oben im Diagramm auftauchen, etwa S22. Die Pfeile von slo (slope) und ele (elevation) sind fast parallel, was sagt, dass sich diese beiden Umweltvariablen im Datensatz weitgehend parallel verändern, d.h. bei hoher Meereshöhe hat man fast immer auch eine grössere Neigung. Schliesslich kann man sehen, welche Beobachtungsflächen sich in ihren Umweltvariablen stark ähneln (z. B. S17, S16 und S19) bzw. sehr unähnlich sind (z.B. S14 von S22).

### <span id="page-156-0"></span>**Beispiele von Anwendungen von PCAs**

Zunächst sollen aber einige gängige und korrekte Anwendungen auf sehr grossen Datensets gezeigt werden:

**(a) Visualisierung 1**: Hier wurden etwa 20 verschiedene bioklimatische Variablen für alle Rasterzellen der Erdoberfläche (Farbkodierung gibt die Häufigkeit wieder) einer PCA unterworfen. Die Klimadaten sind so hoch korreliert, dass die ersten beiden Achen (Hauptkomponenten) PC1 und PC2 zusammen 76 % der Varianz im Gesamtdatensatz kodieren. Es wäre also unsinnig, die 20 Variablen einzeln zu analysieren. Durch die rechts gezeigten Korrelationen der Originalvariablen mit

PC1 und PC2 kann man die beiden synthetischen Achsen näherungsweise interpretieren (siehe die Achsenbeschriftung links).

![](_page_157_Figure_1.jpeg)

Abbildung 6.1: Bruelheide et al. 2019

**(b) Visualisierung 2**: Hier wurden 6 funktionelle Merkmale (traits) von Pflanzenarten weltweit einer PCA unterworfen. Diese erweisen sich so weit korreliert, dass die ersten beiden Achen (Hauptkomponenten) PC1 und PC2 zusammen 74% der Varianz enthalten. Der eine wesentliche Gradient ist der von winizigen, kleinsamigen Arten zu grossen Arten mit schweren Samen (in der Abbildunge mit 1 resp. SM bezeichnet). Dazu weitgehend orthogonal ist der Gradient von Pflanzen mit stickstoffreichen Blättern (links oben) zu Pflanzen mit stickstoffarmen Blättern (rechts unten).

![](_page_158_Figure_0.jpeg)

**(c) Principal Components (PCs) in multiplen Regressionen**: Hier rechnet man zunächst eine PCA mit vielen Umweltvariablen ohne Rücksicht auf ihre wechselseitigen Korrelationen. Dann nimmt man die (ersten) PC-Achsen mit der meisten Information als sogenannte "synthetische" Prädiktoren.

- **Vorteil:** Die PC-Achsen sind vollständig unkorreliert. •
- **Nachteil:** Die PC-Achsen sind nicht so direkt interpretierbar wie die Original-Umweltparameter, das sie zwar oft stark mit mehreren Umweltparametern korrelieren, aber eben nicht 100 %. •
- **Wichtig:** Hochladende Achsen sind nicht unbedingt auch die wichtigsten für die Regression. •

# <span id="page-159-0"></span>**Zusammenfassung**

- **Ordinationen** sind im Kern **deskriptive Verfahren für multivariate** (abhängige) **Variablen** und komplementär zu Cluster-Analysen. •
- Ihre Ziele sind **Dimensionsreduktion und Visualisierung**. •
- Die basale Form einer Ordination ist die **PCA**. Sie setzt **lineare Beziehungen und wenige Nullwerte** in der Matrix voraus. •
- Abgesehen von Visualisierungen kann man PCAs auch zum **Generieren unkorrelierter synthetischer Variablen** für nachfolgende multiple Regressionsanalysen verwenden. •

## <span id="page-159-1"></span>**Weiterführende Literatur**

- **Borcard, D., Gillet, F. & Legendre, P. 2018.** *Numerical ecology with R***. 2nd ed. Springer, Cham: 435 pp. [mit R]** •
- Crawley, M.J. 2013. *The R book*. 2nd ed. John Wiley & Sons, Chichester, UK: 1051 pp. [mit R] •
- Everitt, B. & Hothorn, T. 2011. *An introduction to applied multivariate analysis with R*. Springer, New York: 273 pp. [mit R] •
- Leyer, I. & Wesche, K. 2007. *Multivariate Statistik in der Ökologie*. Springer, Berlin: 221 pp. [einfache Erklärung von Ordinationsmethoden, ohne R] •
- McCune, B., Grace, J.B. & Urban, D.L. 2002. *Analysis of ecological communities*. MjM Software Design, Gleneden Beach, Oregon, US: 300 pp. [gut erklärte und detaillierte Einführung in Ordinationen u.a., ohne R] •
- Oksanen, L. 2015. *Multivariate analysis of ecological communities in R: vegan tutorial*. URL: [http://cc.oulu.fi/~jarioksa/opetus/metodi/vegantutor.pdf.](http://cc.oulu.fi/~jarioksa/opetus/metodi/vegantutor.pdf) [gute Einführung in das R-package *vegan* mit vielen Ordinationsmethoden] •
- Wildi, O. 2013. *Data analysis in vegetation ecology*. 2nd ed.Wiley-Blackwell, Chichester, UK: 301 pp. [mit R] •
- Wildi, O. 2017. *Data analysis in vegetation ecology*. 3rd ed. CABI, Wallingford, UK: 333 pp. [mit R] •

## <span id="page-159-2"></span>**Quellen der Beispiele**

- Bruelheide, H., Dengler, J., Purschke, O., Lenoir, J., Jiménez-Alfaro, B., Hennekens, S.M., Botta-Dukát, Z., Chytrý, M., Field, R., (…) & Jandt, U. 2018. Global trait–environment relationships of plant communities. *Nature Ecology and Evolution* 2: 1906–1917. •
- Díaz, S., Kattge, J., Cornelissen, J.H.C., Wright, I.J., Lavorel, S., Dray, S., Reu, B., Kleyer, M., Wirth, C. (…) & Gorné, L.D. 2016. The global spectrum of plant form and function. *Nature* 529: 167–171. •

# <span id="page-160-0"></span>**Statistik 8**

Clusteranalysen, Rück- und Ausblick [1 Tag]

**In Statistik 8 lernen die Studierenden Clusteranalysen/Klassifikationen als eine den Ordinationen komplementäre Technik der deskriptiven Statistik multivariater Datensätze kennen. Es gibt Partitionierungen (ohne Hierarchie), divisive und agglomerative Clusteranalysen (die jeweils eine Hierarchie produzieren). Etwas genauer gehen wir auf die** *k***means Clusteranalyse (eine Partitionierung) ein.**

**Im Abschluss von Statistik 8 werden wir dann die an den acht Statistiktagen behandelten Verfahren noch einmal rückblickend betrachten und thematisieren, welches Verfahren wann gewählt werden sollte. Ebenfalls ist Platz, um den adäquaten Ablauf statistischer Analysen vom Einlesen der Daten bis zur Verschriftlichung der Ergebnisse, einschliesslich der verschiedenen zu treffenden Entscheidungen, zu thematisieren.**

### <span id="page-160-1"></span>**Lernziele**

Ihr…

- habt eine prinzipielle Idee, wie **Cluster-Analysen** funktionieren; und •
- könnt *k***-means clustering** auf Datensätze anwenden •

## <span id="page-160-2"></span>**Clusteranalysen allgemein**

Wie Ordinationen (Statistik 7) gehören Clusteranalysen zu den multivariat-deskriptiven Methoden. Wozu macht man dann Clusteranalysen?

- Clusteranalysen sind **komplementär zu Ordinationen**: Bei Clusteranalysen liegt der Fokus auf den Unterschieden, während bei der Ordination der Fokus auf dem allmählichen Wandel entlang von Gradienten liegt. Insofern sind Ordinationen und Clusteranalysen Methoden, die für die gleichen Datensätze und z. T. ähnliche Fragestellungen angewendet werden können, aber mit Betonung unterschiedlicher Aspekte. Oftmals werden in einer Studie sogar beide Verfahren angewandt. •
- Prinzipiell geht es bei Clusteranalysen um das Herausarbeiten von Gruppen von Objekten mit ähnlichen Eigenschaften, z. B.: •
  - um diese zu beschreiben, ◦
  - um diese auf Unterschiede zu testen oder ◦
  - um deren Verbreitung in Karten darstellen zu können. ◦

Es gibt drei grundlegende Typen von Clusteranalysen, jeweils mit mehreren Methoden:

**Partitionierung** (ohne Hierarchie) •

#### **Hierarchische Clusteranalyse** •

- **divisiv** (der Gesamtdatensatz wird sukzessive in immer feinere Gruppen aufgeteilt) ◦
- **agglomerativ** (beginnend mit den Einzelbeobachtungen werden diese immer weiter zu Gruppen zusammengefasst) ◦

Im Kurs behandeln wir nur die Partitionierung.

# <span id="page-161-0"></span>*k***-means clustering: Theorie**

Das *k-means clustering* ist die einfachste Clustermethode überhaupt. Ihre Kernaspekte lassen sich wie folgt beschreiben:

- Partitionierung (ohne Hierarchie) in vom Benutzer vorgegebene *k* Cluster. •
- Verfahren versucht, die Summe der quadratischen Abweichungen vom den Clusterzentren (Zentroide) zu minimieren. •
- In der Tendenz entstehen ± sphärische Cluster ähnlicher Grösse (sphärisch meint kugelförmig/isodiametrisch, aber eben nicht im dreidimensionalen, sondern im vieldimensionalen Variablenraum). •
- Da das Ganze mit einem iterativen Optimierungsalgorithmus passiert, der mit zufällig gewählten Startpunkten beginnt, unterscheiden sich unterschiedliche Durchläufe im Ergebnis. Wenn man immer das gleiche Ergebnis haben will, kann man set.seeed() vorher ausführen. •

Die Durchführung des *k-means clustering* eines multivariaten Datensatzes geschieht mit dem Befehl kmeans aus Base R:

### <span id="page-161-1"></span>**Beispiel in R: Fischvorkommen im Fluss Doubs**

Hier schauen wir uns die Fischartvorkommen im Fluss Doubs an den gleichen Beobachtungsstellen an, an denen wir im Ordinationskapitel schon die Umweltdaten betrachtet haben. Im Prinzip ist kmean-clustering nicht so gut für Daten von Artvorkommen geeignet, da solche Daten typischerweise sehr viele Nullwerte (Absenzen) enthalten. Man kann das das Problem durch eine Transformation reduzieren, welche die Randsumme der Quadrate gleich eins macht (während für Umweltvariablen eine scale-Transformation besser ist):

```
p_load(vegan)
```

spe\_norm <- decostand(spe, "normalize")

Das eigentliche Clustering geschieht dann wie folgt. Man muss vorab definieren, wie viele Cluster man haben will (hier 4). Da kmeans eine iterative Methode ist, kommt ggf. in jedem Durchlauf ein geringfügig anderes Ergebnis heraus. Wenn man immer exakt das gleiche Ergebnis will, kann man den Befehl set.seed() mit einer beliebigen Zahl vorausschalten:

# k-means-Clustering mit 4 Gruppen durchführen

set.seed(123)

kmeans\_1 <- kmeans(spe\_norm, centers = 4, nstart = 100)

kmeans\_1\$cluster

S1 S2 S3 S4 S5 S6 S7 S8 S9 S10 S11 S12 S13 S14 S15 S16 S17 S18 S19 S20

3 3 3 3 1 3 3 1 3 3 3 3 3 3 1 1 1 1 2 2

S21 S22 S23 S24 S25 S26 S27 S28 S29

2 4 4 4 2 2 2 2 2

Für jede der 29 Beobachtungsflächen zeigt der Output, zu welchem der vier Cluster er gehört, d. h. jedes der Cluster enthält jetzt faunistisch ähnliche Fischgemeinschaften.

Wenn man sehen will, wie diese vier Fischgemeinschaften (basierend auf der Clusterung der Artdaten) sich im Ordinationsraum verhalten, kann man die Clusterzugehörigkeit nutzen, um die Punkte im Ordinationsdiagramm (vgl. Statistik 7) entsprechend einzufärben (Code im Demoskript):

![](_page_162_Figure_7.jpeg)

Tatsächlich suggeriert das Ordinationsdiagramm eine klare Separierung der vier Cluster hinsichtlich der Artenzusammensetzung.

Aber wie entscheiden wir im allgemeinen Fall, wie viele Cluster Sinn machen? Vielfach ergibt sich schon aus der geplanten Anwendung, ob eher zwei oder eher zwanzig Einheiten sinnvoll sind. Man kann schauen, wie gut sich die Cluster in ihren Attributen unterscheiden (etwa mittels PCA, s.o., oder ANOVA, s.u.). Es gibt auch unterschiedliche numerische Kriterien, um die "beste" Partitionierung zu finden (allerdings liefern verschieden Gütemasse unterschiedliche Ergebnisse).

Ein Gütemass ist **SSI =** *Simple Structure Index*. Der SSI kombiniert drei Aspekte von Cluster-Güte: (a) maximale Differenz aller Variablen zwischen den Clustern, (b) Grössen der einzelnen Clusters und (c) Abweichung der Variablenwerte in den Clusterzentren vom Gesamtmittel. Der SSI reicht von 0 bis 1 und eine Partitionierung ist umso besser, je höher der Wert ist.

# k-means partionierung, 2 bis 10 Gruppen

set.seed(123)

km\_cascade <- cascadeKM(spe\_norm, inf.gr = 2, sup.gr = 10, iter = 100, criterion = "ssi")

km\_cascade\$results

[…]

# Visualisierung citerion Simple Structure Index

plot(km\_cascade, sortg = TRUE)

![](_page_163_Figure_8.jpeg)

Die farbige Visualisierung links zeigt, dass es eben keine hierarchische Clusteranalyse ist. Bei *k* > 2 bleibt die ursprüngliche Abgrenzung der zwei Hauptcluster nicht erhalten. Gemäss SSI wäre in diesem Fall die 3-Cluster-Lösung die beste (es sei aber empfohlen, solchen numerischen "Empfehlungen" nicht blindlings zu glauben). Im Ordinationsraum der Umweltvariablen, sieht die 3- Cluster-Lösung der Fischdaten wie folgt aus:

![](_page_164_Figure_0.jpeg)

Sobald wir uns auf eine Cluster-Auflösung festgelegt haben, gilt es auch noch, die Cluster zu charakterisieren und zu vergleichen. Das kann z.B. mit einer ANOVA geschehen (hier für die 3- Cluster-Lösung und die Fischartenzahl pro Beobachtungsstelle als abhängiger Variable). Den Code dafür und weitere Beispiele gibt es im R Demo Code.

![](_page_165_Figure_0.jpeg)

# <span id="page-165-0"></span>**Zusammenfassung**

- *k-means clustering* ist eine einfache nicht-hierarchische Clustermethode, bei der der Benutzer vorgibt, wie viele Einheiten er haben möchte. •
- **Agglomerative Clusterverfahren** fassen Einheiten sukzessive über ihre Ähnlichkeitsbeziehungen zusammen. Am Ende kann man dann subjektiv oder nach unterschiedlichen numerischen Kriterien entscheiden, welche Clusterauflösung dem Bedarf am besten entspricht. •
- Sobald man sich auf eine Cluster-Lösung festgelegt hat, sollte man die erhaltenen Cluster bezüglich ihrer Attribute noch charakterisieren und vergleiche, wozu insbesondere Ordinationen und ANOVAs geeignet sind. •

### <span id="page-165-1"></span>**Weiterführende Literatur**

- **Borcard, D., Gillet, F. & Legendre, P. 2018.** *Numerical ecology with R***. 2nd ed. Springer, Cham: 435 pp. [mit R]** •
- Crawley, M.J. 2013. *The R book*. 2nd ed. John Wiley & Sons, Chichester,UK: 1051 pp. [mit R] •
- Everitt, B. & Hothorn, T. 2011. *An introduction to applied multivariate analysis with R*. Springer, New York: 273 pp. [mit R] •

Wildi, O. 2017. *Data analysis in vegetation ecology*. 3rd ed. CABI, Wallingford, UK: 333 pp. [mit R] •

# <span id="page-166-0"></span>**Anhang I**

Weiterführende Methoden der Statistik vor allem, aber nicht exklusiv, für den Bereich Ökologie können in einem Individual Spezialisation Module (ISM) gelernt werden:

Im Rahmen eine 3 ECTS ISM könnt ihr euch im geleiteten Selbststudium vertiefte Statistik-Kenntnisse mit R aneignen. Dieser Kurs baut auf den Statistikteilen in «Research Methods» auf und richtet sich primär an Studierende, die mit ökologischen Daten aus der Vegetations-, Tier- oder Gewässerökologie arbeiten, kann aber auch für andere ENR-Studierende nützlich sein. Es werden Unterrichtsmaterialien auf Englisch und auf Deutsch zu Verfügung gestellt.

Es werden vor allem die folgenden Themen bearbeitet:

- Vertiefung mixed effect models (LMMs, GLMMs) •
- Nicht-lineare Regressionen •
- Vertiefung Ordinationstechniken (DCA, NMDS, passive Projektion von Umweltvariablen, «constrained» Ordinationen wie RDA) •
- Agglomerative Clusteranalysen •
- Umfassende Biodiversitätsanalysen (beta- und gamma-Diversität, funktionelle und phylogenetische Diversität) •

Dazu können in Absprache mit den Studierenden ausgewählte weitere Bereiche kommen, etwa:

- Generalized additive models (GAMs) und Glättungsfunktionen •
- Diagnostische Arten (IndVal, phi-Werte) •
- Regression trees •
- Structural equation models (SEMs) •

Für den Leistungsnachweis ist eine Erfahrungsnote in Form von zwei semesterbegleitenden Hausarbeiten vorgesehen.

[Jürgen Dengler](http://deng@zhaw.ch/) und Stefan Widmer leiten den Selbststudiumskurs und steht euch für weitere Informationen und Fragen gerne zur Verfügung.

# <span id="page-166-1"></span>**Anhang II**

Übersicht über statistische Verfahren