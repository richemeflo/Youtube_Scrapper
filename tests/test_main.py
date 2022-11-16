import sys

sys.path.append("./")
import pytest
import scrapper
from scrapper import LoadingError


class TestClass:
    def test_load_json(self):
        with pytest.raises(LoadingError):
            scrapper.load_json("input.txt")

    def test_one(self):
        id="CmgyUYCibwA"
        res=scrapper.scrap(id,1)
        assert res._get_id == id
        assert res._get_title == "L'histoire du projet le plus fou de ma vie"
        assert res._get_creator == "SQUEEZIE"
        assert res._get_likes > 0
        #tmp="On a pris notre temps mais voici enfin l'histoire du GP Explorer \u2764\ufe0f\nComme promis et pour votre plus grand bonheur, voici l'offre Deezer (0,99\u20ac par mois pendant 6 mois, puis 5,99\u20ac par mois pour tous les \u00e9tudiants) : https://DeezerFR.lnk.to/deezerxsqueezie\n\nCheck les derni\u00e8res pi\u00e8ces Yoko : http://www.yokoshop.com\n\nCollection Squeezie x RhinoShield : https://bit.ly/Squeezie-RhinoShield\n\nR\u00e9seaux :\n\nInsta : https://www.instagram.com/xsqueezie/\nTwitter : http://www.twitter.com/xSqueeZie\nFacebook : http://www.facebook.com/SqueeZiePageO...\n\nR\u00e8gles de l'espace commentaire (\u00e0 respecter sous peine d'\u00eatre banni par l'\u00e9quipe de mod\u00e9ration) :\n\n- \u00c9crire dans un fran\u00e7ais correct\n- Respecter les autres\n- Pas de commentaires type \"like si tu regardes la vid\u00e9o en chaussettes\"\n- Pas de pubs et de spams", "links": ["https://DeezerFR.lnk.to/deezerxsqueezie", "http://www.yokoshop.com", "https://bit.ly/Squeezie-RhinoShield", "https://www.instagram.com/xsqueezie/", "http://www.twitter.com/xSqueeZie", "http://www.facebook.com/SqueeZiePageO..."], "first_comments": []},{"id": "tR2LgBekZKw", "title": "L'INFLATION COSMIQUE", "creator": "ScienceEtonnante", "likes": 21000, "description": "L'inflation : un ph\u00e9nom\u00e8ne monstrueux, mais qui semble n\u00e9cessaire pour expliquer pourquoi notre Univers est tel qu'il est.\n\nD\u00e9tails et compl\u00e9ments dans le billet de blog qui accompagne la vid\u00e9o : https://scienceetonnante.com/2022/11/...\n\n\u00c9crit et r\u00e9alis\u00e9 par David Louapre \u00a9 Science \u00e9tonnante\n\nFacebook : http://www.facebook.com/sciencetonnante\nTwitter : http://www.twitter.com/dlouapre\nAbonnez-vous : https://www.youtube.com/scienceetonnante\nMe soutenir : https://utip.io/scienceetonnante/\nhttp://www.tipeee.com/science-etonnante\nMes livres : https://scienceetonnante.com/livres/"
        #assert res._get_description == tmp
        tab = ["https://scienceetonnante.com/2022/11/...", "http://www.facebook.com/sciencetonnante", "http://www.twitter.com/dlouapre", "https://www.youtube.com/scienceetonnante", "https://utip.io/scienceetonnante/", "http://www.tipeee.com/science-etonnante", "https://scienceetonnante.com/livres/"]
        assert res._get_links == tab
        assert res._get_first_comments == []