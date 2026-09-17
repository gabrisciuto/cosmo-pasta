COSMO PASTA WEB — VERSIONE DEFINITIVA
======================================

Questa versione mantiene LO STILE DEL PRIMO FILE COSMO PASTA e usa le immagini locali fornite.
I prezzi della prima versione sono stati ripristinati:
- Pasta: €8,00
- Pasta sfusa: €9,80 / kg
- Drink: €2,50 (Coca-Cola/Fanta/Sprite), acqua €1,50
- Birre: Ceres €4,00, Heineken €3,50, Moretti €3,00, Messina €3,50

DEBUG FLASK
-----------
Il template evita il problema Jinja del metodo dict.items usando group['items'].

AVVIO
-----
1. Estrai lo ZIP.
2. Apri il CMD dentro la cartella Cosmo_Pasta_Web.
3. Esegui:
   py -m pip install -r requirements.txt
4. Esegui:
   py app.py
5. Apri:
   http://127.0.0.1:5000

Le immagini sono già nella cartella static/images, quindi non devi scaricarle separatamente.
