# eop-tabletop
Playing the Elevation of Privilege threat modeling card game remotely is challenging. There are great online implementations like [https://eopgame.azurewebsites.net/](https://eopgame.azurewebsites.net/) and [http://eopgame.herokuapp.com/](http://eopgame.herokuapp.com/) but it felt that the *fun-factor* is missing.

EoP works because it's a game so it should feel like a game. That's why I ported it to different platforms:

- As a [Workshop](https://steamcommunity.com/sharedfiles/filedetails/?id=2097550051&searchtext=elevation+of+privilege) in Tabletop Simulator
- and an [image](http://playingcards.io/ugfqgf) and a [text](http://playingcards.io/kesfys) based version for playingcards.io
- a Tabletopia implementation is doable but other than a quick trial I haven't done anything there.

This repo contains files for the Tabletop Simulator Workshop and the two different versions for playingcards.io

![eop](https://cdn.zappy.app/011200738e3776c58164e840e0693674.png)
The Privacy expansion created by [PrivacyMV](https://twitter.com/PrivacyMV) is also included!


If you're looking for a physical copy, you can order it from [Agilestationery](https://agilestationery.co.uk/products/elevation-of-privilege-with-privacy-suit) or download for [free](https://blog.logmeininc.com/privacy-by-design-can-be-entertaining/) and print yourself.


# Playingcards.io

Downloads the latest cards.yaml from Adam Shostack's git repo, append the Privacy suit and create a CVS to upload to playcards.io

## Setup

> pip3 install pyyaml

## Build CVS

1. run `python3 create_playingcards.py` to create playingcards_eop.csv 

    ```
    cards.yaml downloaded and cleaned: eop.yaml
    loading expansions from: expansion_cards.yaml
        expansion: Privacy
    decks merged to: eop.yaml
    exporting to cvs
        Spoofing
        Tampering
        Repudiation
        Information Disclosure
        Denial of Service
        Elevation of Privilege
        Privacy
    exported to: playingcards_eop.csv
    ```

1. Open http://playingcards.io/ and choose "Other/Custom" at the bottom then click 'Start Game'
or simply go directly to http://playingcards.io/room/new/generic
1. Click Edit Table (toolbox icon)
1. Remove the current deck and add a Custom Card Deck
1. Click Edit Deck on the newly created custom deck (it has 0 cards)
1. Go to Card Data and click Remove Everything
1. Click Import CSV and locate `playingcards_eop.csv` 
1. Don't forget to click ALL +1 
1. On the Layers tab select Card Face and delete all layers
1. Add the following Text layers as *Different Per-Card*:
    
    i. Field name: suit
    i. Field name: rank
    i. Field name: threat
    
1. Change the font size and alignment to your liking
1. On General you can change the size of the cards if you want
1. After clicking Done, clenup the player area by removing the surplus card holders and the spinner.




