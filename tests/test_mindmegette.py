from tests import ScraperTest

from recipe_scrapers.mindmegette import Mindmegette


class TestMindmegetteScraper(ScraperTest):

    scraper_class = Mindmegette
    scraper_options = {
        'meta_http_equiv': True,
    }

    def test_host(self):
        self.assertEqual(
            'mindmegette.hu',
            self.harvester_class.host()
        )

    def test_language(self):
        self.assertEqual(
            'hu-HU',
            self.harvester_class.language()
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            'Tepsis krumpli céklával és répával'
        )

    def test_total_time(self):
        self.assertEqual(
            45,
            self.harvester_class.total_time()
        )

    def test_ingredients(self):
        self.assertListEqual(
            [
                '6 db nagyobb burgonya',
                '2 db cékla',
                '8 db közepes méretű répa',
                '4 db lilahagyma',
                '6 gerezd fokhagyma',
                'friss rozmaring',
                'só',
                'bors'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        return self.assertEqual(
            "A zöldségeket megpucoljuk és megmossuk.\n" +
            "A burgonyát vastagabb szeletekre vágjuk, a répákat hosszában elfelezzük, a lilahagymát félbe vagy negyedbe vágjuk, a céklát szeleteljük, a fokhagymát egészben hagyjuk.\n" +
            "Az összes, előkészített zöldséget egy tepsibe tesszük, meglocsoljuk olívaolajjal, sózzuk és borsozzuk, kézzel összeforgatjuk az egészet, majd friss rozmaringot teszünk rá.\n" +
            "Lefedjük alufóliával, 180 fokon 20 percig sütjük, majd fólia nélkül, amíg minden zöldség meg nem puhul. Grill funkció esetén az utolsó 5 percben meg is piríthatjuk. Sült húsok mellé kiváló, laktató köret.",
            self.harvester_class.instructions()
        )

    def test_yields(self):
        self.assertEqual(
            "4 serving(s)",
            self.harvester_class.yields()
        )

    def test_image(self):
        self.assertEqual(
            'http://mindmegette.hu/images/283/O/tepsis-ceklas.jpg',
            self.harvester_class.image()
        )
