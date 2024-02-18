from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!

    def test_homepage(self):
        with app.test_client() as client:
            # import pdb
            # pdb.set_trace()
            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code,200)
            
    def test_valid_word_check(self):
        """ test a word is valid"""
        with app.test_client() as client:
            with client.session_transaction() as session:
                session['board'] = [["A","P","P","L","E"],["A","P","P","L","E"],["A","P","P","L","E"],["A","P","P","L","E"],["A","P","P","L","E"]]
          
            resp = client.get('/word?word=apple')

            self.assertEqual(resp.status_code,200)
            self.assertEqual(resp.json['result'],'ok')
    def test_invalid_word_check(self):
        """test a word is invalid"""
        with app.test_client() as client:
            with client.session_transaction() as session:
                session['board'] = [["A","P","P","L","E"],["A","P","P","L","E"],["A","P","P","L","E"],["A","P","P","L","E"],["A","P","P","L","E"]]

            resp = client.get('/word?word=happy')

            self.assertEqual(resp.status_code,200)
            self.assertEqual(resp.json['result'],'not-on-board')

    def test_not_A_word_check(self):
        """test a word is invalid"""
        with app.test_client() as client:
            with client.session_transaction() as session:
                session['board'] = [["A","P","P","L","E"],["A","P","P","L","E"],["A","P","P","L","E"],["A","P","P","L","E"],["A","P","P","L","E"]]

            resp = client.get('/word?word=kdjlskdjflsdjls')

            self.assertEqual(resp.status_code,200)
            self.assertEqual(resp.json['result'],'not-word')
            
    # def test_game_over_score(self):
    #     with app.test_client() as client:
    #         resp = client.post('/gameOver',data={"score":"20"})

    #         self.assertEqual(resp.status_code,200)