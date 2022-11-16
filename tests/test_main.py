import sys

sys.path.append("./")
from scrapper import *


class TestClass:
    id="CmgyUYCibwA"
    res=scrap(id,1)

    def test_id(self):
        assert self.res._get_id() == self.id
    
    def test_title(self):
        assert self.res._get_title() == "L'histoire du projet le plus fou de ma vie"
    
    def test_creator(self):
        assert self.res._get_creator() == "SQUEEZIE"
    def test_likes(self):
        assert self.res._get_likes() > 0

    def test_description(self):
        string_tmp = "On a pris notre temps mais voici enfin l'histoire du GP Explorer \u2764\ufe0f\nComme promis et pour votre plus grand bonheur, voici l'offre Deezer (0,99\u20ac par mois pendant 6 mois, puis 5,99\u20ac par mois pour tous les \u00e9tudiants) : https://DeezerFR.lnk.to/deezerxsqueezie\n\nCheck les derni\u00e8res pi\u00e8ces Yoko : http://www.yokoshop.com\n\nCollection Squeezie x RhinoShield : https://bit.ly/Squeezie-RhinoShield\n\nR\u00e9seaux :\n\nInsta : https://www.instagram.com/xsqueezie/\nTwitter : http://www.twitter.com/xSqueeZie\nFacebook : http://www.facebook.com/SqueeZiePageO...\n\nR\u00e8gles de l'espace commentaire (\u00e0 respecter sous peine d'\u00eatre banni par l'\u00e9quipe de mod\u00e9ration) :\n\n- \u00c9crire dans un fran\u00e7ais correct\n- Respecter les autres\n- Pas de commentaires type \"like si tu regardes la vid\u00e9o en chaussettes\"\n- Pas de pubs et de spams"
        assert self.res._get_description() == string_tmp

    ##def test_links(self):
        url = "https://scienceetonnante.com/2022/11/..."
        assert url in self.res._get_links()
    
    def test_comments(self):
        assert self.res._get_first_comments() == []