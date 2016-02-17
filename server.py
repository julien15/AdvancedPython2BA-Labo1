# server.py
# Math tools web application
# Author: Sébastien Combéfis
# Version: February 3, 2016

import os
from bottle import route, run

@route('/salon')
def home():
    c='''
        <!DOCTYPE html>
        <html>
        <head lang="en">
            <meta charset="UTF-8">
            <title> Le salon de la bière </title>
            <style>
                body{
                    background-image:url("http://photos.up-wallpaper.com/images248/euj0c1zssmt.jpg");
                    background-repeat: no repeat;
                    background-size:cover;
                }
                #indentificateur{
                    color:white;
                    text-align:center;
                }
                h1{
                    color:white;
                    font-size:50px;
                    text-align:center;
                }
                a{
                    color:white;
                }
                a:hover{
                    color:rgb(240,245,0);
                }


            </style>
        </head>
        <body>
            <h1>Bienvenue au salon de bière</h1>
            <form method="post" action="/login" id="indentificateur">
                <p>
                <label for="Identifiant">Votre pseudo</label> : <input type="text" name="pseudo" />
                <br/>
                <label for="pass">Mot de passe</label> : <input type="password" name="pass" />
            </p>
            <p><a href="http://localhost:8088/sinscrire"> Pas encore de compte ? </p>
            <input type="submit" value = 'se connecter'/>
            </form>

        </body>
        </html>'''
    return c

run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))