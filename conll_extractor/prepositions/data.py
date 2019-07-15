# -*- coding: utf-8 -*-

PREPOSITIONS = ['zu', 'an', 'auf', 'für', 'von', 'gegen', 'aus', 'in', 'durch', 'über', 'unter', 'hinter', 'bei']
DETERMINERS = ['das', 'dem', 'der']
CONTRACTED = ['zum', 'zur', 'ans', 'am', 'aufs', 'aufm', 'fürs', 'fürn', 'fürm', 'vom', 'gegens', 'ausm', 'im',
              'ins', 'durchs', 'übers', 'übern', 'überm', 'untern', 'unters', 'unterm', 'beim', 'hinters',
              'hinterm', 'gegens', 'ums', 'vorm']

FILTER_CONTRACTED = {'am': ['Himmel', 'Tag'],
                     'beim': ['Gedanke'],
                     'im': ['Augenblick', 'Dorf'],
                     'ins': ['Schloss'],
                     'übers': ['Land'],
                     'vom': ['Augenblick', 'Stein'],
                     'zum': ['Schloss', 'Stein']}

FILTER_PREP = {'an': ['Baum', 'Dienstag', 'Glas', 'Korridor', 'Lächeln', 'Schlosstor', 'Spalt', 'Himmel', 'Tag'],
               'auf': ['Bündel', 'Essen', 'Geräusch', 'Glas', 'Lenkrad', 'Motorrad', 'Paket', 'Schaufenster', 'Schild',
                       'Schloss', 'Schlossgelände', 'Sofa', 'Spielfeld', 'Türschloss', 'Wagendach',
                       'Wohnzimmerfenster'],
               'bei': ['Aufruhr', 'Buch', 'Stalaktit', 'Gedanke'],
               'durch': ['Dach', 'Fenster', 'Feuer', 'Glas', 'Loch', 'Porträtloch', 'purpurne', 'Rattern', 'Tor',
                         'Turmzimmer', 'Unterholz', 'Wohnzimmerfenster'],
               'für': ['Haus', 'Spiel'],
               'in': ['Brief', 'Buch', 'Gesicht', 'Hinsicht', 'Klassenzimmer', 'Licht', 'Päckchen', 'Paket',
                      'Schlafzimmer', 'Sofa', 'Sonnenlicht', 'Spiel', 'Stadion', 'Zimmer', 'Augenblick', 'Dorf',
                      'Schloss'],
               'über': ['Brett', 'Ding', 'Feld', 'Feuer', 'Gras', 'Kassenbuch', 'Leintuchbündel', 'Meer', 'Pult',
                        'Schloss', 'Schlossgelände', 'Spiel', 'Wetter', 'Land'],
               'von': ['Duft', 'Familie', 'Junge', 'Loch', 'Moment', 'Päckchen', 'Riese', 'Schinken', 'Schlag',
                       'Troll', 'Turban', 'Augenblick', 'Stein'],
               'zu': ['Frau', 'Haufe', 'Haus', 'Katze', 'Lichtfleck', 'Mann', 'Porträt', 'Riese', 'Schlange',
                      'Schluss', 'Schlüsselschwarm', 'Tribüne', 'Schloss', 'Stein']}

FILTER_CONTRACTED_123 = {
    'am': ['Brüllen', 'Computer', 'Eingang', 'Empfangsschalter', 'Ende', 'Ende', 'Fenster', 'Fleck', 'Genick', 'Glatze',
           'Kiste', 'Kopf', 'Ligusterweg', 'Morgen', 'Nachmittag', 'Rand', 'Schlüsselloch', 'Sonntagmorgen',
           'Stadtrand', 'Stiel', 'Terrarium'],
    'aufs': ['Bett', 'Meer'],
    'beim': ['Bäcker', 'Computerspiel', 'Einkaufen', 'Friseur', 'Frühstück', 'Frühstück', 'Geräusch', 'Name', 'Postamt',
             'Schritt', 'Waschen'],
    'fürs': ['Leben'],
    'im': ['Büro', 'Bus', 'Donner|Donnern', 'Eiswagen', 'Erdgeschoss', 'Fernsehen', 'Fernsehen', 'Flur', 'Haus',
           'Innere', 'Juli', 'Kopf', 'Land', 'Land', 'Land', 'Leben', 'Ligusterweg', 'Moment', 'Nachhinein', 'Nu',
           'Rückspiegel', 'Schrank', 'Schrank', 'Schrank', 'Sinn', 'Sprung', 'Stau', 'Stille|Stillen', 'Stock', 'Sturm',
           'Vergleich', 'Vorbeigleiten', 'Wagen', 'Wasser', 'Wohnzimmer', 'Zoo', 'Zoorestaurant'],
    'ins': ['Auto', 'Bett', 'Büro', 'Haus', 'Kino', 'Klo', 'Meer', 'Stolpern', 'Wohnzimmer'],
    'vom': ['Bäcker', 'Büro', 'Ende', 'Fleck', 'Friseur', 'Sofarand', 'Telefon'],
    'zum': ['Anziehen', 'Bäcker', 'Bahnblick', 'Beste', 'Fenster', 'Friseur', 'Frühstück', 'Himmel', 'Leben',
            'Ligusterweg', 'Mal', 'Schlafen', 'Schlafzimmerfenster', 'Teufel', 'Verstummen', 'Vordereingang',
            'Zoobesuch'],
    'zur': ['Abreise', 'Abwechslung', 'Arbeit.', 'Haustür', 'Mittagspause', 'Schnecke', 'Seite']}
