#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import Bottle, run, view, request,template,post,route,error
import json
from bottle import  run, request,template,post,route,error
import json
import time
import os






@route('/')
def formulaire():
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
                    position:absolute;
                    bottom:50px;
                    right:50px
                }
                h1{
                    color:white;
                    font-size:50px;
                    text-align:center;
                }
                article{
                    text-align:center;
                }

            </style>
        </head>
        <body>
            <h1>Bienvenue au salon de bière</h1>
            <article>
                <iframe width="500" height="300" src="https://www.youtube.com/embed/l0Jbuz_JEDs" frameborder="0" allowfullscreen></iframe>
            </article>
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
@route('/sinscrire')
def formulaire1():
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
                td,tr{
                    color:white;
                }

            </style>
        </head>
        <body>
        <div align='center'>
            <form method="post" action="/traitement">
                <table>
                <tr>
                    <td><label for="Identifiant">Votre pseudo</label></td> <td><input type="text" name="pseudo"/></td>
                </tr>
                <tr>
                    <td><label for="pass">Mot de passe</label></td><td><input type="password" name="pass"/></td>
                </tr>
                <tr>
                    <td><label for="date">Date de naissance</label></td><td><input type="date" name="date"/></td>
                </tr>
                </table>
            <input type="submit" value = "s'enregistrer"/>
            </form>
        </div>

        </body>
        </html>'''
    return c
@post("/traitement")
def traitement():
    document=open("indentifiant.txt","r")
    enreg1=json.load(document)
    document.close()
    id=request.forms.get("pseudo")
    mp=request.forms.get("pass")
    date=request.forms.get("date")
    print(date)
    l=[]
    l.append(mp)
    l.append(date)
    enreg1[id]=l
    réintegration=open("indentifiant.txt","w")
    réintegration.write(json.dumps(enreg1,sort_keys=True,indent=4,ensure_ascii=False))
    réintegration.close()
    return login()
@post("/login")
def login():
    document=open("indentifiant.txt","r")
    enreg1=json.load(document)
    document.close()
    id=request.forms.get("pseudo")
    mp=request.forms.get("pass")
    for n in enreg1:
        if n == id :
            a=enreg1[n]
            if a[0]== mp:
                return salon()
@post('/salon')
def salon():
    return '''
    <html>
    <head>
    <meta charset="UTF-8"/>
    <title>Le salon de la bière </title>
    <style>
        body{
            background-image:url("http://photos.up-wallpaper.com/images248/euj0c1zssmt.jpg");
            background-repeat: no repeat;
            background-size:cover;
        }
        header h1{
                width:100%;
                text-align:center;
                color:white;
                font-size: XX-large;
                font-family: Lucida Calligraphy;
        }

        nav{

            text-align: center;
        }


        nav li
        {
            display: inline-block;
            margin-right: 30px;


        }
        a{
            font-size:large;
            color: white;
            text-decoration:none;
            font-family: Lucida Calligraphy;
        }
        a:hover{
            color:rgb(240,245,0);
        }
        footer{
            font-family: comic sans MS;
            color:white;
            margin-left:5%;
            position:absolute;
            bottom:2%;
        }
        section{
            margin-left:5%;
        }
        article{
            width:33%;
        }
        p{
            color:white;
            font-family: comic sans MS;
        }
    </style>
</head>
<body>
    <div id="page principal">
        <div id="Titre">
            <header>
                <h1>Bienvenue chez nous!</h1>
            </header>
        </div>
        <nav>
            <ul>
                <li><a href="http://localhost:8088/couleur">Couleur</a></li>
                <li><a href="http://localhost:8088/type">Type/fermentation</a> </li>
                <li><a href="http://localhost:8088/contact">Contact</a> </li>
            </ul>

        </nav>
        <section>
            <article>
                <p> Vous êtes un amateur de bonnes bières ? Vous passez constamment un temps dingue dans le rayon bières en quête de nouvelles aventures ? Ce site est fait pour vous ! Vous trouverez ici de quoi sustenter votre soif de nouveautés et élargir votre horizon brassicole, et tout cela, en un rien de temps ! </p>
            </article>
            <article>
                <iframe width="500" height="300" src="https://www.youtube.com/embed/l0Jbuz_JEDs" frameborder="0" allowfullscreen></iframe>
            </article>
        </section>
        <footer>
            <p>fondateur:</p>
            <p>Stilmant Julien, Herbert Louis</p>
        </footer>

    </div>

</body>
</html>'''
@route('/couleur')
def couleur():
    return '''
    <!DOCTYPE html>
    <html>
    <head lang="en">
    <meta charset="UTF-8">
    <title>Les couleur</title>
    <style>
         body{
            background-image:url("http://photos.up-wallpaper.com/images248/euj0c1zssmt.jpg");
            background-repeat: no repeat;
            background-size:cover;
        }
        header h1{
                width:100%;
                text-align:center;
                color:white;
                font-size: XX-large;
                font-family: Lucida Calligraphy;
        }
        nav{
            text-align: center;
        }
        nav li
        {
            display: inline-block;
            margin-right: 30px;
        }
        a{
            font-size:large;
            color: white;
            text-decoration:none;
            font-family: Lucida Calligraphy;
        }
        a:hover{
            color:rgb(240,245,0);

    </style>
</head>
<body>
    <header>
        <h1>Les couleurs des bières</h1>
    </header>
    <nav>
        <ul>
            <li><a href="http://localhost:8088/couleur/blanche">Blanche</a></li>
            <li><a href="http://localhost:8088/couleur/rouge" >Rouge</a></li>
            <li><a href="http://localhost:8088/couleur/blonde">Blonde</a></li>
            <li><a href="http://localhost:8088/couleur/ambree">Ambrée</a> </li>
            <li><a href="http://localhost:8088/couleur/brune">Brune</a> </li>
            <li><a href="http://localhost:8088/couleur/noire">Noire</a> </li>
        </ul>
    </nav>
</body>
</html>'''
@route('/couleur/<nom>')
def categoriecouleur(nom):
    if nom=="blonde":
        document=open("traitement.txt",'r')
        enreg=json.load(document)
        document.close()
        for n in enreg:
            if n=="Blonde":
                a=enreg[n]
        b='''
        <!DOCTYPE html>
        <html>
        <head lang="en">
            <meta charset="UTF-8">
            <title> Bière blonde </title>
            <style>
                h1 {
                    color : white;
                    font-size:50px;
                    text-align: center;
                    font-family:Lucida Calligraphy;
                    font-style: italic;
                }
                h2{
                    color : white;
                    font-size:40px;
                    text-align: center;
                }
                #intro{
                    width=33%;
                }
                u{
                text-decoration: underline;
                }
                p{
                    color: white;
                    font-size:20px;
                    font-family:Comic sans ms;
                    font-style: italic;
                    margin-left:60px;
                    margin-top:40px;
                }
                body{
                    background-image: url("http://waquid.com/wp-content/uploads/2015/07/bi%C3%A8re1.jpg");
                }
                section{
                    width:40%
                }
                #basededonné{
                    color:white;
                }
                table{
                    border-collapse: collapse;
                    color:red;

                }
                td, th {
                    border: 1px solid black;
                    color:white;
                }

            </style>
        </head>
        <body>
            <h1> La bière blonde</h1>
            <section>
                <p> La blonde,</p>
                <p>Bière existant depuis les origines de la bière et brassée avec du froment ou de l'avoine en plus de l'orge. Cela leur donne un goût légèrement piquant. Les blanches sont également souvent brassées comme autrefois avec des épices : coriandre, curaçao, écorces d’orange. Elles peuvent être de fermentation haute ou basse (plus rare) et sont généralement refermentées en bouteille.</p>
                <p><u>Quelques exemples:</u></p>
                <p>
                    Hoegaarden - Vedett - Moinette - Omer - Ciney - Leffe blond
                </p>
                <div align="center">'''
        b+='''
            <table><caption>Liste des bière blondes</caption><thead><tr><th>Nom de la bière</th><th>note</th><th>type/fermentation</th> </tr></thead>'''
        b+='''<tbody>'''
        for n in a:
            for t in n:
                p=n[t]
                b+='''
                    <tr><th>'''+str(t)+'''</th><th>'''+str(p[0])+'''</th><th>'''+str(p[1])+'''</th> </tr>'''
        b+='''
            </tbody></table>
            '''
        b+='''
                </div>
            '''
        return b
    if nom=="brune":
        document=open("traitement.txt",'r')
        enreg=json.load(document)
        document.close()
        for n in enreg:
            if n=="Brune":
                a=enreg[n]
        r='''
        <!DOCTYPE html>
        <html>
        <head lang="en">
            <meta charset="UTF-8">
            <title> Bière brune </title>
            <style>
                    h1 {
                    color : white;
                    font-size:50px;
                    text-align: center;
                    font-family:Lucida Calligraphy;
                    font-style: italic;

                }
                h2{
                    color : white;
                    font-size:40px;
                    text-align: center;
                }
                #intro{
                    width=33%;
                }
                a{
                color:red}
                u{
                text-decoration: underline;
                }
                p{
                    color: white;
                    font-size:20px;
                    font-family:Comic sans ms;
                    font-style: italic;
                    margin-left:60px;
                    margin-top:40px;
                }
                body{
                    background-image: url("http://chimay.com/wp-content/uploads/2015/01/chimay_bleue1.jpg");
                    background-repeat:no repeat;
                    background-size:cover;
                }
                section{
                    width:40%
                }
                #basededonné{
                    color:white;
                }
                table{
                    border-collapse: collapse;
                    color:red;

                }
                td, th {
                    border: 1px solid black;
                    color:white;
                }

            </style>
        </head>
        <body>
            <h1> La bière brune</h1>
            <p> <a href="http://localhost:8080/allo"> >Acceuil</a> </p>
            <section>
                <p> La bière brune,</p>
                <p>Bière existant depuis les origines de la bière et brassée avec du froment ou de l'avoine en plus de l'orge. Cela leur donne un goût légèrement piquant. Les blanches sont également souvent brassées comme autrefois avec des épices : coriandre, curaçao, écorces d’orange. Elles peuvent être de fermentation haute ou basse (plus rare) et sont généralement refermentées en bouteille.</p>
                <p><u>Quelques exemples:</u></p>
                <p>
                    Vedett - Moinette - Omer - Chimay bleu - Leffe brune
                </p>
            </section>
            <div align="center">'''
        r+='''
            <table><caption>Liste des bière blondes</caption><thead><tr><th>Nom de la bière</th><th>note</th><th>type/fermentation</th> </tr></thead>'''
        r+='''<tbody>'''
        for n in a:
            for t in n:
                p=n[t]
                r+='''
                    <tr><th>'''+str(t)+'''</th><th>'''+str(p[0])+'''</th><th>'''+str(p[1])+'''</th> </tr>'''
        r+='''
            </tbody></table>
            '''
        r+='''
                </div>


        </body>
        </html>'''
        return r
    if nom=="ambree":
        document=open("traitement.txt",'r')
        enreg=json.load(document)
        document.close()
        for n in enreg:
            if n=="Ambree":
                a=enreg[n]
        r='''
        <!DOCTYPE html>
        <html>
        <head lang="en">
        <meta charset="UTF-8">
        <title> Ambree </title>
        <style>
            h1 {
                color : white;
                font-size:50px;
                text-align: center;
                font-family:Lucida Calligraphy;
                font-style: italic;

            }
            h2{
                color : white;
                font-size:40px;
                text-align: center;
            }
            #intro{
                width=33%;
            }
            a{
            color:red}
            u{
            text-decoration: underline;
            }
            p{
                color: white;
                font-size:20px;
                font-family: Comic sans ms;
                font-style: italic;

            }
            body{
                background-image: url("http://www.brasserie-lagermanoise.fr/DataGermanoise/downloads/Media/19_Fotolia_61530573_M.jpg");
                background-repeat:no repeat;
                background-size:cover;
            }
            section{
                width:40%
                margin-top:60px;
                margin-left:1100px;

            }
            article{
                position: absolute;
                leftt: 200px;
                bottom: 250px;
            }
            table{
                    border-collapse: collapse;
                    color:red;

                }
            td, th {
                    border: 1px solid black;
                    color:white;
            }

    </style>
</head>
<body>
    <h1> La bière ambrée </h1>
    <p> <a href="http://localhost:8000/allo"> >Acceuil</a> </p>
    <section>
        <p> La pils ou pilsner,</p>
        <p> Après la première guerre mondiale, s'inspirant des anglais, beaucoup de brasseurs belges passent de la lager brune traditionnelle à la bière de type « lager » (bière de fermentation haute). Cette bière, à la robe bronze ou rouge-ambrée à cuivrée, est une bière légère, qui se boit souvent comme alternative à la pils, avec une teneur en alcool comparable (5°). Elle possède une saveur douce, un petit goût de levure et une légère touche épicée. La plupart d'entr'elles ont un léger apport de houblon et un arôme légèrement fruité, voire caramelisé. Presque toutes sont filtrées et pasteurisées, et à part la couleur, les ales ambrées belges n'ont que peu de choses en commun avec les ales anglaises. </p>
        <p><u>Quelques exemples:</u></p>
        <p>
            Orval - Lilly Blue - Gouden Carolus - Bush - Gauloise - Chimay Rouge
        </p>
    </section>
     <div align="center">'''
        r+='''
            <table><caption>Liste des bière blondes</caption><thead><tr><th>Nom de la bière</th><th>note</th><th>type/fermentation</th> </tr></thead>'''
        r+='''<tbody>'''
        for n in a:
            for t in n:
                p=n[t]
                r+='''
                    <tr><th>'''+str(t)+'''</th><th>'''+str(p[0])+'''</th><th>'''+str(p[1])+'''</th> </tr>'''
        r+='''
            </tbody></table>
            '''
        r+='''
                </div>

    <iframe width="840" height="472.5" src="https://www.youtube.com/embed/B5UedfCySQk" frameborder="0" allowfullscreen></iframe>

</body>
'''
        return r
@error(404)
def erreur404():
        r='''
        <!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title>Erreur 404 </title>
    <style>
        body{
            background-image:url(http://apollo-eu-uploads.s3.amazonaws.com/1440122138/maxresdefault.jpg);
        }
        h1{
            color:white;
        }
    </style>
</head>
<body>
    <h1>Error 404</h1>

</body>
</html>'''
        return r
@error(405)
def erreur405():
        r='''
        <!DOCTYPE html>
        <html>
        <head lang="en">
        <meta charset="UTF-8">
        <title>Erreur 405 </title>
        <style>
            body{
            background-image:url(http://apollo-eu-uploads.s3.amazonaws.com/1440122138/maxresdefault.jpg);
            }
            h1{
                color:white;
            }
        </style>
        </head>
        <body>
            <h1>Error 405</h1>

        </body>
        </html>'''
        return r
run(host='0.0.0.0', port=int(os.environ.get('PORT', 5005)))
