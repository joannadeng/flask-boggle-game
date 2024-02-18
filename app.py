from boggle import Boggle
from flask import Flask,render_template,session,request,jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = "iamthekey"

boggle_game = Boggle()


@app.route('/')
def homepage():
    """ home page of the game"""
    board = boggle_game.make_board()
    session['board'] = board
    highscore = session.get('highscore',0)
    numplays = session.get('numplays',0)

    session['highscore'] = highscore
    session['numplays'] = numplays

    # score = 0

    # print(f'highscore is {session['highscore']}')
    # print(f'number plays is {session['numplays']}')
    return render_template("index.html",board=board)

@app.route('/word')
def get_word():
    """check if a guess word valid"""
    word = request.args['word']
    print(word)
    board = session['board']
    result = boggle_game.check_valid_word(board,word)
    print(result)
    return jsonify({"result":result})

@app.route('/gameOver',methods=['POST'])
def game_over():
    """update game score"""

    score = request.json['score']
    # import pdb
    # pdb.set_trace()
    highscore = session['highscore']
    session['highscore'] = max(highscore,score)
    highscore = session['highscore']

    numplays = session['numplays']
    numplays = numplays + 1
    session['numplays'] = numplays

    return jsonify({"highscore":highscore})



