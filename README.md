# Open RU Pool

![Static Badge](https://img.shields.io/badge/Data-YAML-%23CB171E?style=flat-square)
![Static Badge](https://img.shields.io/badge/Script-Python3-%233776AB?style=flat-square)
![Static Badge](https://img.shields.io/badge/License-CC_BY–SA_4.0-%239E9E9E?style=flat-square)

Dieses Repository enthält einen einfach zu verwaltenden russischen Wortbestand, der als Sammlung von yaml-Dateien organisiert ist. Pro Wort gibt es eine yaml-Datei mit allen Informationen.

Die Sprache der Ordner und Übersetzungen ist derzeit Deutsch. Für das Quellmaterial siehe den Abschnitt [Literaturhinweise](#Literaturhinweise).

## Über die Zuordnung zu Themen

Das Problem der Sortierung von Wörtern ist, dass sie meist in vielen verschiedenen Kontexten vorkommen können.
Die Herausforderung besteht darin, ein Wort möglichst genau einem Thema zuzuordnen.

Die Zuordnung eines Wortes zu einem Thema zielt auf höchstmögliche Intuitivität und schließt nicht die Möglichkeit der Zuordnung zu einem anderen Thema aus.

Die Wortsammlung ist hier zweigeteilt.
Die erste Reihenfolge ist allgemein, die zweite ist spezifisch.
Die Ordnernamen sollten selbsterklärend sein.
Für manche Themen gibt es im Folgenden zusätzlich Hinweise, was sie unter anderem enthalten.

Als Faustregel gilt: Je allgemeiner die Bedeutung eines Wortes, je mehr Konktext möglich sind, desto allgemeiner ist das zugeordnete Thema (und umgekehrt).
Wenn möglich sollte ein Wort einem Thema mit hoher Spezifität zugeordnet werden.

**Beispiel 1**

Das Wort "работать" (arbeiten) ist ein intransitives Verb und könnte dem Thema "Ungerichtete Handlungen" (Spezifität 0) zugeordnet werden. Das spezifischere Thema ist hingegen "Arbeit und Beruf".

**Beispiel 2**

Das Wort "бестактность" (Taktlosigkeit) ist ein Begriff oder eine Idee (Speziftiät 0). Das spezifischere Thema ist hingegen "Etikette und Sitten".

**Beispiel 3**

Da Wort "блестящий" (glänzend) beschreibt etwas, das man objektiv über den Augensinn wahrnimmt. Ebenso wird das Wort figurativ gebraucht, um etwas subjektiv als hervorragend zu bewerten. Da beide Kontexte gleichwertig sind, ist das unspezifische Thema "Eigenschaften" am passendsten.

## Themen und Unterthemen

| Thema                              | Unterthema                  | Enthält u. a.                             | Spezifität |
| ---------------------------------- | --------------------------- | ----------------------------------------- | ---------: |
| Mensch als Lebewesen               | Aussehen und Körper         |                                           |          3 |
| Mensch als Lebewesen               | Essen und Lebensmittel      |                                           |          3 |
| Mensch als Lebewesen               | Gesundheit und Hygiene      |                                           |          3 |
| Mensch als Lebewesen               | Haushalt und Wohnen         |                                           |          3 |
| Mensch als Lebewesen               | Kleidung und Schuhe         |                                           |          3 |
| Mensch als Lebewesen               | Lebensabschnitte            |                                           |          3 |
| Mensch als Lebewesen               | Sinne und Wahrnehmung       |                                           |          3 |
| Mensch&#160;als&#160;Vernunftwesen | Ausdruck und Handeln        | Keine Verben oder Adjektive               |          3 |
| Mensch&#160;als&#160;Vernunftwesen | Bedürfnisse und Gefühle     |                                           |          3 |
| Mensch&#160;als&#160;Vernunftwesen | Begriffe und Ideen          |                                           |          0 |
| Mensch&#160;als&#160;Vernunftwesen | Eigenschaften               | beschreibende Adjektive                   |          0 |
| Mensch&#160;als&#160;Vernunftwesen | Gemüt und Wille             |                                           |          3 |
| Mensch&#160;als&#160;Vernunftwesen | Gerichtete Handlungen       | transitive Verben                         |          0 |
| Mensch&#160;als&#160;Vernunftwesen | Intellekt und Geist         | geistige Prozesse                         |          2 |
| Mensch&#160;als&#160;Vernunftwesen | Technik und Technologie     |                                           |          3 |
| Mensch&#160;als&#160;Vernunftwesen | Ungerichtete Handlungen     | instransitive Verben                      |          0 |
| Mensch&#160;als&#160;Vernunftwesen | Wertung und Urteil          | wertende Adjektive                        |          1 |
| Mensch und Gesellschaft            | Arbeit und Beruf            |                                           |          2 |
| Mensch und Gesellschaft            | Bewegung                    |                                           |          3 |
| Mensch und Gesellschaft            | Beziehungen und Familie     |                                           |          3 |
| Mensch und Gesellschaft            | Bildung und Unterricht      |                                           |          3 |
| Mensch und Gesellschaft            | Dokumente und Drucksachen   |                                           |          3 |
| Mensch und Gesellschaft            | Etikette und Sitten         | umgangssprachliche Ausdrücke              |          3 |
| Mensch und Gesellschaft            | Feiertage und Freizeit      |                                           |          3 |
| Mensch und Gesellschaft            | Finanzen und Handel         |                                           |          3 |
| Mensch und Gesellschaft            | Forschung und Wissenschaft  |                                           |          3 |
| Mensch und Gesellschaft            | Güter und Stoffe            |                                           |          3 |
| Mensch und Gesellschaft            | Herkunft und Identität      |                                           |          3 |
| Mensch und Gesellschaft            | Hobby und Sport             |                                           |          3 |
| Mensch und Gesellschaft            | Ideologie und Politik       |                                           |          3 |
| Mensch und Gesellschaft            | Industrie und Wirtschaft    |                                           |          3 |
| Mensch und Gesellschaft            | Kommunikation und Medien    |                                           |          3 |
| Mensch und Gesellschaft            | Krieg und Militär           |                                           |          3 |
| Mensch und Gesellschaft            | Kriminalität und Recht      |                                           |          3 |
| Mensch und Gesellschaft            | Kunst und Kultur            | Kulturelle Güter und Instutitionen        |          3 |
| Mensch und Gesellschaft            | Land und Stadt              | Objekte und Vorgänge im öffentlichen Raum |          3 |
| Mensch und Gesellschaft            | Literatur und Sprache       | bildhafte oder blumige Redewendungen      |          3 |
| Mensch und Gesellschaft            | Medizin und Therapie        |                                           |          3 |
| Mensch und Gesellschaft            | Musik und Theater           |                                           |          3 |
| Mensch und Gesellschaft            | Staat und Verwaltung        |                                           |          3 |
| Mensch und Gesellschaft            | Transport und Verkehr       |                                           |          3 |
| Natur                              | Geographie und Umwelt       |                                           |          3 |
| Natur                              | Klima und Wetter            |                                           |          3 |
| Natur                              | Merkmale und Vorgänge       | Farben                                    |          2 |
| Natur                              | Mineralien, Pflanzen, Tiere |                                           |          3 |
| Abstrakte Konzepte                 | Grammatik und Linguistik    |                                           |          3 |
| Abstrakte Konzepte                 | Maß und Quantität           |                                           |          1 |
| Abstrakte Konzepte                 | Qualität                    | Adverbien, Konjunktionen, Präpositionen   |          1 |
| Abstrakte Konzepte                 | Raum                        |                                           |          1 |
| Abstrakte Konzepte                 | Zeit                        |                                           |          1 |

## Weitere Hinweise zum Aufbau des Wortschatzes

- Von Adjektiven abgeleitete Adverbien werden in der Regel nicht aufgeführt.

## Literaturhinweise

- Andrjuša, N. P., Kozlova, T. V. (2014). Leksičeskij minimum po russkomy jazyku kak inostrannomy.<br>Ėlementarnyj uroven', Sank-Peterburg: Zlatoust. (ISBN 978-5-86547-858-4)

- Andrjuša, N. P., Kozlova, T. V. (2013). Leksičeskij minimum po russkomy jazyku kak inostrannomy.<br>Bazovyj uroven', Sank-Peterburg: Zlatoust. (ISBN 978-5-86547-601-6)

- Andrjuša, N. P., Kozlova, T. V. (2014). Leksičeskij minimum po russkomy jazyku kak inostrannomy.<br>Pervyj sertifikacionnyj uroven', Sank-Peterburg: Zlatoust. (ISBN 978–5–86547–862–1)

- Andrjuša, N. P., Kozlova, T. V. (2014). Leksičeskij minimum po russkomy jazyku kak inostrannomy.<br>Vtoroj sertifikacionnyj uroven', Sank-Peterburg: Zlatoust. (ISBN 978-5-86547-799-0)

- Andrjuša, N. P., Kozlova, T. V. (2019). Leksičeskij minimum po russkomy jazyku kak inostrannomy.<br>Tretij sertifikacionnyj uroven', Sank-Peterburg: Zlatoust. (ISBN 978-5-86547-970-3)

<!-- - [udarenie.ru](https://udarenieru.ru/index.php): Grammatičeskij slovar'.   -->

## Lizenz

Diese Arbeit unterliegt den Bestimmungen einer
[Creative Commons Namensnennung-Share Alike 4.0 International-Lizenz](http://creativecommons.org/licenses/by-sa/4.0/).
