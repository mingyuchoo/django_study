from django.test import TestCase

import json
import yaml


class YamlTestCase(TestCase):

    def setUp(self) -> None:
        self.json_data = """{
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}"""

    def tearDown(self) -> None:
        pass

    def test_convert(self):
        jsonData = json.loads(self.json_data)
        print(yaml.dump(jsonData))
