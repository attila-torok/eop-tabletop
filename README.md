# eop-tabletop
Playing the Elevation of Privilege threat modeling card game remotely is challenging. There are great online implementations like [https://eopgame.azurewebsites.net/](https://eopgame.azurewebsites.net/) and [http://eopgame.herokuapp.com/](http://eopgame.herokuapp.com/) but it felt that the *fun-factor* is missing.

EoP works because it's a game so it should feel like a game. That's why I ported it to different platforms:

- As a [Workshop](https://steamcommunity.com/sharedfiles/filedetails/?id=2097550051&searchtext=elevation+of+privilege) in Tabletop Simulator
- and an image and a text based version for playingcards.io
- a Tabletopia implementation is doable but other than a quick trial I haven't done anything there.

This repo contains files for the Tabletop Simulator Workshop and the two different versions for playingcards.io

![eop](https://cdn.zappy.app/011200738e3776c58164e840e0693674.png)
The Privacy expansion created by [PrivacyMV](https://twitter.com/PrivacyMV) is also included!


If you're looking for a physical copy, you can order it from [Agilestationery](https://agilestationery.co.uk/products/elevation-of-privilege-with-privacy-suit) or download for [free](https://blog.logmeininc.com/privacy-by-design-can-be-entertaining/) and print yourself.


# Playingcards.io

## Deck with the up-to-date text

This script downloads cards.yaml that has the latest changes, from Adam Shostack's [git repo](https://github.com/adamshostack/eop), append the Privacy suit and create a CSV to upload to playcards.io

### Setup

> pip3 install pyyaml

### Build and import CSV

1. run `python3 create_playingcards.py` to create playingcards_eop.csv 

    ```
    $python3 create_playingcards.py
    cards.yaml downloaded and cleaned: eop.yaml
    loading expansions from: expansion_cards.yaml
        expansion: Privacy
    decks merged to: eop.yaml
    exporting to csv
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
1. Now either start with a pre-built deck:
    
    2. On the Room Options tab click Import from File
    2. Select [playingcards.io__text.pcio](playingcards_pcio/playingcards.io__text.pcio)
1. Or build your own look:

    2. Remove the current deck and add a Custom Card Deck
    2. Click Edit Deck on the newly created custom deck (it has 0 cards)
    2. Go to Card Data and click Remove Everything
    2. On the Layers tab select Card Face and delete all layers
    2. Add the following Text layers as *Different Per-Card* fields:
    
        - Field name: suit
        - Field name: rank
        - Field name: threat
    
    2. Change the font size and alignment to your liking
    2. On General you can change the size of the cards if you want
    2. Clenup the play area by removing the surplus card holders and the spinner.

1. Click Import CSV on the Card Data tab and locate `playingcards_eop.csv` 
1. Don't forget to click ALL +1 
1. You're done. Go play!

## Deck with images, based on the LogMeIn EoP deck

Ready-to-import pcio file, using images from https://logmeincdn.azureedge.net/legal/gdpr-v2/eop-cards-ready-to-print.pdf 

1. Open http://playingcards.io/ and choose "Other/Custom" at the bottom then click 'Start Game'
or simply go directly to http://playingcards.io/room/new/generic
1. Click Edit Table (toolbox icon)
1. On the Room Options tab click Import from File
1. Select [playingcards.io__image.pcio](playingcards_pcio/playingcards.io__image.pcio)
1. You're done. Go play!


---

# Tabletop Simulator workshop

The [tabletop_simulator](tabletop_simulator/) folder contains the image files for the EoP workshop.

The Workshop is accessible on Steam at https://steamcommunity.com/sharedfiles/filedetails/?id=2097550051&searchtext=elevation+of+privilege

This special table supports up to 10 players.

The Privacy expansion is not added to the deck by default but put on the side. You can decide if you want to shuffle it in or not.

> **Pro-tipps**:
> - in TTS add Object\Components\Tools\Tablet to load a dataflow diagram while playing
> - Right click on the deck and Split by the number of players to easily deal out all cards

### Rules cheat sheet

1. Deal out the whole deck
2. Tampering 3 starts
3. Read the card
4. Identify threat
5. Record if applicable (+1 coin, +1 if own card)
6. Next player follows suit if can, else plays any
7. Highest card or EoP suit wins the round (+1 coin)
8. Winner selects new suit
9. At game end most coins takes the prize!
10. Create TM notes and tickets

### Elevation of Privilege Instructions

Draw a diagram of the system you want to threat model before you deal the cards.

1. Deal the deck to 3–10 players. 
1. Play starts with the 3 of Tampering. 
1. Play clockwise, and each player in turn continues using the suit if  they have a card in that suit. 
1. If the player doesn’t have a card from that suit, the player can use another suit. 
1. Each round is won by the highest card played in the suit that was led, unless an Elevation of Privilege (EoP) card is played. 
1. In that case the high value EoP card wins.
1. To play a card, read the card, announce your threat and record it. 
1. If the player can’t link the threat to the system play proceeds.
1. The winner of a hand selects the card (and suit) to lead the next hand. 
1. Take a few minutes between hands to think about threats.

Points:
1 for a threat on your card, +1 for taking the trick

Threats should be articulated clearly, testable, and addressable. In the event that a threat leads to an argument, you can resolve it by asking the question: “Would we take an actionable bug, feature request or design change for that?” If the answer is yes, it is a real threat. (This doesn’t mean that threats outside of that aren’t real, it’s simply a way to focus discussion on actionable threats.)<br> 
Questions that start with “There’s a way” should be read as “There’s a way…and here’s how…” while questions that start with “Your code” should be read “The code we’re collectively creating…and here’s how.”

The deck contains a number of special cards: trumps and open threats. EoP cards are trumps: They take the trick even if they have a lower value than the suit that was led.<br> 
The ace of each suit is an open threat card. When played, the player must identify a threat not listed on another card.<br>
When all the cards have been played, whoever has the most points wins.

Optional variants:
- You may pass cards after the third trick. This is helpful if you have cards that you can’t tie to the system. Someone else may be able to.
- Double the number of points, and give one point for threats on other people’s cards.
- Other players may “riff” on the threat and if they do, they get one point per additional threat.
- Limit riffing to no more than 60 seconds.
- Mark up the diagram where the threat occurs.
