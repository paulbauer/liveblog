import liveblog.themes as themeapp
import liveblog.blogs as blogapp
from superdesk.tests import TestCase
from bson import ObjectId
from superdesk import get_resource_service
import liveblog.blogs.embeds as embeds


class Foo():

    def __init__(self):
        self.setup_call = False

    def setup_called(self):
        self.setup_call = True
        return self.setup_call

foo = Foo()


class ThemeSettingsTestCase(TestCase):

    def setUp(self):
        if not foo.setup_call:
            foo.setup_called()
            themeapp.init_app(self.app)
            blogapp.init_app(self.app)
        self.themeservice = get_resource_service('themes')

        self.angular_theme = {
            'name': 'angular',
            'abstract': True,
            'version': '3.3.4',
            'options': [
                {
                    'name': 'postsPerPage',
                    'label': 'Number of posts per page',
                    'type': 'number',
                    'default': 10,
                    'help': 'Set the number of posts you want to see at the initialization'
                },
                {
                    'name': 'postOrder',
                    'label': 'Default posts order of the timeline',
                    'type': 'select',
                    'options': [
                        {
                            'value': 'editorial',
                            'label': 'Editorial'
                        },
                        {
                            'value': 'newest_first',
                            'label': 'Newest first'
                        },
                        {
                            'value': 'oldest_first',
                            'label': 'Oldest first'
                        }
                    ],
                    'default': 'editorial'
                },
                {
                    'name': 'permalinkDelimiter',
                    'label': 'Permalink Delimiter',
                    'type': 'select',
                    'options': [
                        {
                            'value': '?',
                            'label': 'Query delimiter (?)'
                        },
                        {
                            'value': '#',
                            'label': ' Fragment identifier delimiter (#)'
                        }
                    ],
                    'default': '?',
                    'help': 'Sets the delimiter used to send the permalink. \
                    ex: permalinkHashMark=?, http://example.com/?...'
                },
                {
                    'name': 'datetimeFormat',
                    'label': 'Date time Format',
                    'type': 'datetimeformat',
                    'default': 'lll',
                    'help': 'Sets the date time format to be used in the embed.\ Please \
                    enter a custom format in valid moment.js format http://momentjs.com/docs/#/parsing/string-format'
                },
                {
                    'name': 'datetimeFormattest',
                    'label': 'Date time Format test',
                    'type': 'datetimeFormattest',
                    'default': 'lll',
                    'help': 'Test'
                }
            ]
        }
        self.classic_theme = {
            'name': 'classic',
            'version': '3.3.11',
            'extends': 'angular',
            'options': [
                {
                    'name': 'language',
                    'label': 'Theme language',
                    'type': 'select',
                    'options': [
                        {
                            'value': 'en',
                            'label': 'English'
                        },
                        {
                            'value': 'fi',
                            'label': 'Finnish'
                        },
                        {
                            'value': 'de',
                            'label': 'Deutsch'
                        },
                        {
                            'value': 'fr',
                            'label': 'Français'
                        },
                        {
                            'value': 'nl',
                            'label': 'Nederlands'
                        },
                        {
                            'value': 'no',
                            'label': 'Norsk'
                        },
                        {
                            'value': 'cs',
                            'label': 'Čeština'
                        },
                        {
                            'value': 'ro',
                            'label': 'Română'
                        }
                    ],
                    'default': 'en'
                },
                {
                    'name': 'postsPerPage',
                    'label': 'Number of posts per page',
                    'type': 'number',
                    'default': 10,
                    'help': 'Set the number of posts you want to see per page'
                },
                {
                    'name': 'datetimeFormattest',
                    'label': 'Date time Format test',
                    'type': 'datetimeFormattest',
                    'default': 'lll',
                    'help': 'Test'
                },
                {
                    'name': 'postOrder',
                    'label': 'Default posts order of the timeline',
                    'type': 'select',
                    'options': [
                        {
                            'value': 'editorial',
                            'label': 'Editorial'
                        },
                        {
                            'value': 'newest_first',
                            'label': 'Newest first'
                        },
                        {
                            'value': 'oldest_first',
                            'label': 'Oldest first'
                        }
                    ],
                    'default': 'editorial'
                },
                {
                    'name': 'loadNewPostsManually',
                    'label': 'User needs to click a button to retrieve the new posts',
                    'type': 'checkbox',
                    'default': True,
                    'help': 'Otherwise they will be loaded periodically'
                },
                {
                    'name': 'infinitScroll',
                    'label': 'Use infinite scroll to load more pages',
                    'type': 'checkbox',
                    'default': True,
                    'help': 'if true, more pages are automatically loaded \
                    when the bottom of the page is reached. Otherwise a button is added at the bottom of the posts list'
                },
                {
                    'name': 'showImage',
                    'label': 'Show the blog image',
                    'type': 'checkbox',
                    'default': True
                },
                {
                    'name': 'showTitle',
                    'label': 'Show the blog title',
                    'type': 'checkbox',
                    'default': True
                },
                {
                    'name': 'showDescription',
                    'label': 'Show the blog description',
                    'type': 'checkbox',
                    'default': True
                },
                {
                    'name': 'showAuthor',
                    'label': 'Show author',
                    'type': 'checkbox',
                    'default': True,
                    'help': 'Show the author information on posts'
                },
                {
                    'name': 'showAuthorAvatar',
                    'label': 'Show author avatar',
                    'type': 'checkbox',
                    'default': True,
                    'dependsOn': {
                        'showAuthor': True
                    },
                    'help': 'Show the author avatar on posts'
                },
                {
                    'name': 'authorNameFormat',
                    'label': 'Author name format',
                    'type': 'select',
                    'default': 'display_name',
                    'dependsOn': {
                        'showAuthor': True
                    },
                    'options': [
                        {
                            'value': 'display_name',
                            'label': 'Full name'
                        },
                        {
                            'value': 'byline',
                            'label': 'Byline'
                        },
                        {
                            'value': 'sign_off',
                            'label': 'Sign off'
                        }
                    ],
                    'help': 'How to show the author name'
                },
                {
                    'name': 'authorNameLinksToEmail',
                    'label': 'The author name links to email',
                    'type': 'checkbox',
                    'default': False,
                    'dependsOn': {
                        'showAuthor': True
                    },
                    'help': 'A click on the author name will create a new email to be sent to the author.'
                },
                {
                    'name': 'permalinkDelimiter',
                    'label': 'Permalink delimiter',
                    'type': 'select',
                    'options': [
                        {
                            'value': '?',
                            'label': 'Query delimiter (?)'
                        },
                        {
                            'value': '#',
                            'label': ' Fragment identifier delimiter (#)'
                        }
                    ],
                    'default': '?',
                    'help': 'Sets the delimiter used to send the permalink. \
                    ex: permalinkHashMark=?, http://example.com/?...'
                },
                {
                    'name': 'canComment',
                    'label': 'Users can comment',
                    'type': 'checkbox',
                    'default': False,
                    'help': 'If the users can comment on the blog'
                },
                {
                    'name': 'hasHighlights',
                    'label': 'Display highlights',
                    'type': 'checkbox',
                    'default': False,
                    'help': 'If the users see the highlight button in the blog'
                },
                {
                    'name': 'blockSearchEngines',
                    'label': 'Block search engines',
                    'type': 'checkbox',
                    'default': False,
                    'help': 'Block search engines from indexing my blogs'
                },
                {
                    'name': 'showGallery',
                    'label': 'Show slideshow gallery',
                    'type': 'checkbox',
                    'default': False,
                    'help': 'If the users will see the slideshow gallery for multiple images posts'
                },
                {
                    'name': 'showSocialShare',
                    'label': 'Show social sharing options',
                    'type': 'checkbox',
                    'default': True,
                    'help': 'If the users will see the social sharing options'
                },
                {
                    'name': 'livestream',
                    'label': 'Pinned post behaviour',
                    'type': 'select',
                    'options': [
                        {
                            'value': False,
                            'label': 'Show below menu bar'
                        },
                        {
                            'value': True,
                            'label': 'Show above menu bar'
                        }
                    ],
                    'default': False
                },
                {
                    'name': 'livestreamAutoplay',
                    'label': 'Autoplay for livestream videos',
                    'type': 'checkbox',
                    'default': False,
                    'help': 'if the users will see the video autoplay for livestream'
                },
                {
                    'name': 'showSyndicatedAuthor',
                    'label': 'Show syndicated author',
                    'type': 'checkbox',
                    'default': False,
                    'help': 'If the users will see the syndicated author'
                }
            ]
        }
        self.default_theme = {
            'name': 'default',
            'version': '3.3.56',
            'asyncTheme': True,
            'seoTheme': True,
            'contributors': [
                'Paul Solbach <psolbach@dpa-newslab.com>',
                'Massimo Scamarcia <massimo.scamarcia@sourcefabric.org>',
                'Löic Nogues <loic.nogues@sourcefabric.org>',
                'Aleksandar Backo Jelicic <aleksandar.jelicic@sourcefabric.org>'
            ],
            'options': [
                {
                    'name': 'datetimeFormat',
                    'label': 'Date time Format',
                    'type': 'datetimeformat',
                    'default': 'lll',
                    'help': 'Sets the date time format to be used in the \
                    embed. Please enter a custom format in valid moment.js \
                    format http://momentjs.com/docs/#/parsing/string-format'
                },
                {
                    'name': 'showUpdateDatetime',
                    'label': 'Show post update time',
                    'type': 'checkbox',
                    'default': False,
                    'help': 'If activated, users will see an additional timestamp, when the post has been updated'
                },
                {
                    'name': 'postsPerPage',
                    'label': 'Number of posts per page',
                    'type': 'number',
                    'default': 20,
                    'help': 'Set the number of posts you initially want to show to your readers'
                },
                {
                    'name': 'datetimeFormattest',
                    'label': 'Date time Format test',
                    'type': 'datetimeFormattest',
                    'default': 'lll',
                    'help': 'Test'
                },
                {
                    'name': 'postOrder',
                    'label': 'Default posts order',
                    'type': 'select',
                    'options': [
                        {
                            'value': 'editorial',
                            'label': 'Editorial'
                        },
                        {
                            'value': 'newest_first',
                            'label': 'Newest first'
                        },
                        {
                            'value': 'oldest_first',
                            'label': 'Oldest first'
                        }
                    ],
                    'default': 'editorial'
                },
                {
                    'name': 'autoApplyUpdates',
                    'label': 'All updates are auto-applied periodically',
                    'type': 'checkbox',
                    'default': True,
                    'help': 'Turn off to prompt user to load updates'
                },
                {
                    'name': 'canComment',
                    'label': 'Users can comment',
                    'type': 'checkbox',
                    'default': False,
                    'help': 'Enables a commenting form for users'
                },
                {
                    'name': 'showImage',
                    'label': 'Show the blog image',
                    'type': 'checkbox',
                    'default': False
                },
                {
                    'name': 'showTitle',
                    'label': 'Show the blog title',
                    'type': 'checkbox',
                    'default': False
                },
                {
                    'name': 'showDescription',
                    'label': 'Show the blog description',
                    'type': 'checkbox',
                    'default': False
                },
                {
                    'name': 'showLiveblogLogo',
                    'label': 'Show Liveblog logo',
                    'type': 'checkbox',
                    'default': True,
                    'help': 'Turn off to hide the “powered by Live Blog” logo'
                },
                {
                    'name': 'showAuthor',
                    'label': 'Show the author',
                    'type': 'checkbox',
                    'default': True,
                    'help': 'Show the author information on posts'
                },
                {
                    'name': 'authorNameFormat',
                    'label': 'Author name format',
                    'type': 'select',
                    'default': 'display_name',
                    'dependsOn': {
                        'showAuthor': True
                    },
                    'options': [
                        {
                            'value': 'display_name',
                            'label': 'Full name'
                        },
                        {
                            'value': 'byline',
                            'label': 'Byline'
                        },
                        {
                            'value': 'sign_off',
                            'label': 'Sign off'
                        }
                    ],
                    'help': 'How to show the author info'
                },
                {
                    'name': 'showAuthorAvatar',
                    'label': 'Show author avatar',
                    'type': 'checkbox',
                    'default': True,
                    'dependsOn': {
                        'showAuthor': True
                    },
                    'help': 'Shows an author image besides the author name'
                },
                {
                    'name': 'hasHighlights',
                    'label': 'Show highlight button',
                    'type': 'checkbox',
                    'default': False,
                    'help': 'Introduces a button for the readers to filter the timeline by highlights'
                },
                {
                    'name': 'permalinkDelimiter',
                    'label': 'Permalink delimiter',
                    'type': 'select',
                    'options': [
                        {
                            'value': '?',
                            'label': 'Query delimiter (?)'
                        },
                        {
                            'value': '#',
                            'label': ' Fragment identifier delimiter (#)'
                        }
                    ],
                    'default': '?',
                    'help': 'Sets the delimiter used to send the permalink. \
                    ex: permalinkHashMark=?, http://example.com/?...'
                },
                {
                    'name': 'blockSearchEngines',
                    'label': 'Block search engines',
                    'type': 'checkbox',
                    'default': True,
                    'help': 'Will block search engines from indexing the blog content'
                },
                {
                    'name': 'showGallery',
                    'label': 'Show slideshow gallery',
                    'type': 'checkbox',
                    'default': False,
                    'help': 'Multiple image posts will show up as an image gallery'
                },
                {
                    'name': 'stickyPosition',
                    'label': 'Pinned post behaviour',
                    'type': 'select',
                    'options': [
                        {
                            'value': 'bottom',
                            'label': 'Show below menu bar'
                        },
                        {
                            'value': 'top',
                            'label': 'Show above menu bar'
                        }
                    ],
                    'default': 'bottom',
                    'help': 'Please note: Pinned posts above the menu bar will \
                  not show the author info nor a timestamp. This setting is \
                  especially useful if you want to show a (streaming) video on top of your timeline.'
                },
                {
                    'name': 'gaCode',
                    'label': 'Google analytics code',
                    'type': 'text',
                    'placeholder': 'UA-XXXXX-Y',
                    'default': '',
                    'help': 'Please enter your google analytics account ID.'
                },
                {
                    'name': 'renderForESI',
                    'label': 'Optimise the Live Blog output for ESI',
                    'type': 'checkbox',
                    'default': False,
                    'help': 'Strips the head and body tags from the Live Blog \
                    output to publish it using Edge Side Includes'
                },
                {
                    'name': 'removeStylesESI',
                    'label': 'Remove stylesheet from the Live Blog output for ESI',
                    'type': 'checkbox',
                    'default': False,
                    'help': 'Removes the link to the stylesheet from the Live \
                    Blog output to publish it using Edge Side Includes '
                },
                {
                    'name': 'language',
                    'label': 'Theme language',
                    'type': 'select',
                    'options': [
                        {
                            'value': 'en',
                            'label': 'English'
                        },
                        {
                            'value': 'fi',
                            'label': 'Finnish'
                        },
                        {
                            'value': 'de',
                            'label': 'Deutsch'
                        },
                        {
                            'value': 'fr',
                            'label': 'Français'
                        },
                        {
                            'value': 'nl',
                            'label': 'Nederlands'
                        },
                        {
                            'value': 'no',
                            'label': 'Norsk'
                        },
                        {
                            'value': 'cs',
                            'label': 'Čeština'
                        },
                        {
                            'value': 'ro',
                            'label': 'Română'
                        }
                    ],
                    'default': 'en'
                },
                {
                    'name': 'showSyndicatedAuthor',
                    'label': 'Show syndicated author',
                    'type': 'checkbox',
                    'default': False,
                    'help': 'If the users will see the syndicated author'
                },
                {
                    'name': 'clientDatetimeOnly',
                    'label': 'Show datetime only on client',
                    'type': 'checkbox',
                    'default': False,
                    'help': 'If the users will see the datetime only on client rendered'
                }
            ],
            'i18n': {
                'cs': {
                    'Highlights': 'Hlavní body',
                    'Comment by': 'Komentář',
                    'Powered by': 'Poháněno',
                    'Advertisement': 'reklama',
                    'Cancel': 'Zrušit',
                    'Comment': 'Váš příspěvek',
                    'Comment *': 'Text *',
                    'Comment should be maximum 300 characters in length': 'Maximální délka textu je 300 znaků',
                    'Editorial': 'redakční',
                    'Load more posts': 'Načíst další',
                    'Loading': 'Načítám',
                    'Name *': 'Jméno *',
                    'Name should be maximum 30 characters in length': 'Maximální délka jména je 30 znaků',
                    'Newest first': 'nejnovější',
                    'No posts for now': 'Žádné příspěvky',
                    'Oldest first': 'nejstarší',
                    'One pinned post': 'Jeden připnutý příspěvek',
                    'pinned posts': 'připnuté příspěvky',
                    'Post a comment': 'Otázka / komentář',
                    'See one new update': 'Zobraz 1 nový příspěvek',
                    'See new updates': 'Zobraz nové příspěvky',
                    'Send': 'Odeslat',
                    'Show all posts': 'Zobrazit všechny',
                    'Show highlighted post only': 'Zobraz jen zvýrazněné příspěvky',
                    'Sort by:': 'Řazení:',
                    'Updated': 'Aktualizace',
                    'Your comment was sent for approval': 'Váš text byl úspěšně odeslán Čeká na schválení',
                    'credit:': ' autor:'
                },
                'de': {
                    'Highlights': 'Highlights',
                    'Comment by': 'Kommentar von',
                    'Powered by': 'Unterstützt von',
                    'Advertisement': 'Werbung',
                    'Cancel': 'Abbrechen',
                    'Comment': 'Kommentar',
                    'Comment *': 'Kommentar',
                    'Comment should be maximum 300 characters in length': 'Kommentar \
                        darf maximal 300 Zeichen lang sein',
                    'Editorial': 'Redaktionell',
                    'Load more posts': 'Weitere Beiträge',
                    'Loading': 'Lade',
                    'Name *': 'Name',
                    'Name should be maximum 30 characters in length': 'Name darf maximal 30 Zeichen lang sein',
                    'Newest first': 'Neueste zuerst',
                    'No posts for now': 'Kein Beitrag vorhanden',
                    'Oldest first': 'Älteste zuerst',
                    'One pinned post': 'Angehefteter Eintrag',
                    'pinned posts': 'Angeheftete Einträge',
                    'Please fill in your Comment': 'Bitte Kommentar hier eintragen',
                    'Please fill in your Name': 'Bitte Namen hier eintragen',
                    'Post a comment': 'Kommentar posten',
                    'See one new update': 'Neuen Beitrag anzeigen',
                    'See new updates': 'Neue Beiträge anzeigen',
                    'Send': 'Abschicken',
                    'Show all posts': 'Alle Beiträge anzeigen',
                    'Show highlighted post only': 'Anzeigen hervorgehoben Beitrag ist nur',
                    'Sort by:': 'Ordnen nach',
                    'Updated': 'Aktualisiert am',
                    'Your comment was sent for approval': 'Ihr Kommentar wartet auf Freischaltung',
                    'credit:': 'Bild:'
                },
                'fi': {
                    'Highlights': 'Kohokohtia',
                    'Comment by': 'Comment by',
                    'Powered by': 'Powered by',
                    'Advertisement': 'Mainos',
                    'Cancel': 'Peruuta',
                    'Comment': 'Kommentoi',
                    'Comment *': 'Kommentti *',
                    'Comment should be maximum 300 characters in length': 'Kommentin enimmäispituus on 300 merkkiä',
                    'Editorial': 'Toimituksellinen',
                    'Load more posts': 'Lataa lisää julkaisuja',
                    'Loading': 'Lataa',
                    'Name *': 'Nimi *',
                    'Name should be maximum 30 characters in length': 'Nimen enimmäispituus on 30 merkkiä',
                    'Newest first': 'Uusimmat ensin',
                    'No posts for now': 'Ei uusia julkaisuja',
                    'Oldest first': 'Vanhimmat ensin',
                    'One pinned post': 'Yksi kiinnitetty julkaisu',
                    'pinned posts': 'kiinnitettyä julkaisua',
                    'Please fill in your Comment': 'Lisää kommenttisi',
                    'Please fill in your Name': 'Lisää nimesi',
                    'Post a comment': 'Lähetä kommentti',
                    'See one new update': 'Lataa yksi uusi julkaisu',
                    'See new updates': 'Lataa uutta julkaisua',
                    'Send': 'Lähetä',
                    'Show all posts': 'Näytä kaikki julkaisut',
                    'Show highlighted post only': 'Näytä vain korostettu julkaisu',
                    'Sort by:': 'Järjestä:',
                    'Updated': 'Päivitetty',
                    'Your comment was sent for approval': 'Kommenttisi lähetettiin hyväksyttäväksi',
                    'credit:': '©'
                },
                'fr': {
                    'Highlights': 'Messages en surbrillance',
                    'Comment by': 'Commentaire de',
                    'Powered by': 'Alimenté par',
                    'Advertisement': 'Publicité',
                    'Cancel': 'Annuler',
                    'Comment': 'Commentaire',
                    'Comment *': 'Commentaire *',
                    'Comment should be maximum 300 characters in length': 'Un commentaire ne peut excéder 300 signes',
                    'Editorial': 'Éditorial',
                    'Load more posts': 'Afficher plus de messages',
                    'Loading': 'Chargement',
                    'Name *': 'Nom *',
                    'Name should be maximum 30 characters in length': 'Le nom ne peut excéder 30 signes',
                    'Newest first': "Le plus récent d'abord",
                    'No posts for now': 'Aucun message pour le moment',
                    'Oldest first': 'Plus ancien en premier',
                    'One pinned post': 'Voir le nouveau message',
                    'pinned posts': 'Voir nouveaux messages',
                    'Please fill in your Comment': 'Votre commentaire',
                    'Please fill in your Name': 'Votre nom',
                    'Post a comment': 'Envoyer un commentaire',
                    'See one new update': 'Voir le nouveau message',
                    'See new updates': 'Voir nouveaux messages',
                    'Send': 'Envoyer',
                    'Show all posts': 'Afficher tous les messages',
                    'Show highlighted post only': 'Afficher uniquement les messages en surbrillance',
                    'Sort by:': 'Trier par:',
                    'Updated': 'Mise à jour',
                    'Your comment was sent for approval': 'Votre commentaire \
                        a été envoyé et est en attente de validation',
                    'credit:': 'crédit:'
                },
                'nl': {
                    'Highlights': 'Highlights',
                    'Comment by': 'Commentaar door',
                    'Powered by': 'Aangedreven door',
                    'Advertisement': 'Advertentie',
                    'Cancel': 'Annuleren',
                    'Comment': 'Reactie',
                    'Comment *': 'Tekst *',
                    'Comment should be maximum 300 characters in length': 'Uw reactie van maximaal 300 tekens',
                    'Editorial': 'Redactioneel',
                    'Load more posts': 'Meer',
                    'Loading': 'Laden',
                    'Name *': 'Naam *',
                    'Name should be maximum 30 characters in length': 'Uw naam kan maximaal 30 tekens lang zijn',
                    'Newest first': 'Toon nieuwste eerst',
                    'No posts for now': 'Nog geen berichten beschikbaar',
                    'Oldest first': 'Toon oudste eerst',
                    'One pinned post': 'Bekijk nieuw bericht',
                    'pinned posts': 'Bekijk nieuwe berichten',
                    'Please fill in your Comment': 'Uw reactie',
                    'Please fill in your Name': 'Vul hier uw naam in',
                    'Post a comment': 'Schrijf een reactie',
                    'See one new update': 'Bekijk nieuw bericht',
                    'See new updates': 'Bekijk nieuwe berichten',
                    'Send': 'Verzenden',
                    'Sort by:': 'Sorteer:',
                    'Your comment was sent for approval': 'Uw reactie is ontvangen ter beoordeling',
                    'credit:': 'credit:'
                },
                'no': {
                    'Highlights': 'Høydepunkter',
                    'Comment by': 'Kommentar av',
                    'Powered by': 'Drevet av',
                    'Advertisement': 'Annonse',
                    'Cancel': 'Avbryt',
                    'Comment': 'Kommentar',
                    'Comment *': 'Kommentar*',
                    'Comment should be maximum 300 characters in length': 'Kommentarer kan være inntil 300 tegn',
                    'Editorial': 'Redaksjonelt',
                    'Load more posts': 'Henter flere poster',
                    'Loading': 'Henter',
                    'Name *': 'Navn*',
                    'Name should be maximum 30 characters in length': 'Navn kan ikke ha mer enn 30 tegn',
                    'Newest first': 'Nyeste først',
                    'No posts for now': 'Ingen poster for øyeblikket',
                    'Oldest first': 'Eldste først',
                    'One pinned post': 'Én post festet til toppen',
                    'pinned posts': 'poster festet til toppen',
                    'Please fill in your Comment': 'Skriv inn din kommentar',
                    'Please fill in your Name': 'Skriv inn navn',
                    'Post a comment': 'Post en kommentar',
                    'See one new update': 'Se én ny oppdatering',
                    'See new updates': 'Se nye oppdateringer',
                    'Send': 'Send',
                    'Show all posts': 'Vis alle poster',
                    'Show highlighted post only': 'Vis bare høydepunkter',
                    'Sort by:': 'Sortér etter:',
                    'Updated': 'Oppdatert',
                    'Your comment was sent for approval': 'Din kommentar er sendt til godkjenning',
                    'credit:': 'credit:'
                },
                'ro': {
                    'Highlights': 'Repere',
                    'Comment by': 'Comentariu de',
                    'Powered by': 'Cu sprijinul',
                    'Advertisement': 'Reclamă',
                    'Cancel': 'Anulează',
                    'Comment': 'Comentează',
                    'Comment *': 'Comentariu *',
                    'Comment should be maximum 300 characters in length': 'Comentariu \
                        nu poate fi mai lung de 300 de caractere',
                    'Editorial': 'Editorial',
                    'Load more posts': 'Încarcă mai multe posturi',
                    'Loading': 'Se încarcă',
                    'Name *': 'Numele *',
                    'Name should be maximum 30 characters in length': 'Numele nu poate fi mai lung de 30 de caractere',
                    'Newest first': 'Cele mai noi',
                    'No posts for now': 'Deocamdata nu sunt articole',
                    'Oldest first': 'Cele mai vechi',
                    'One pinned post': 'Vezi un articol nou',
                    'pinned posts': 'Vezi articole noi',
                    'Please fill in your Comment': 'Completează comentariu',
                    'Please fill in your Name': 'Completează numele',
                    'Post a comment': 'Scrie un comentariu',
                    'See one new update': 'Vezi un articol nou',
                    'See new updates': 'Vezi articole noi',
                    'Send': 'Trimite',
                    'Sort by:': 'Ordonează după:',
                    'Your comment was sent for approval': 'Comentariul tău a fost trimis spre aprobare',
                    'credit:': 'credit:'
                }
            }
        }
        self.amp_theme = {
            'name': 'amp',
            'version': '3.3.22',
            'seoTheme': True,
            'ampTheme': True,
            'extends': 'default',
            'onlyOwnCss': 'true',
            'contributors': [
                'Massimo Scamarcia <massimo.scamarcia@sourcefabric.org>',
                'Aleksandar Backo Jelicic <aleksandar.jelicic@sourcefabric.org>',
                'Tomasz Rondio <tomasz.rondio@sourcefabric.org>'
            ],
            'options': [
                {
                    'name': 'postsPerPage',
                    'label': 'Number of posts per page',
                    'type': 'number',
                    'default': 110,
                    'help': 'Be aware that paging is not yet available for the Liveblog 3 AMP theme'
                },
                {
                    'name': 'datetimeFormattest',
                    'label': 'Date time Format test',
                    'type': 'datetimeFormattest',
                    'default': 'lll',
                    'help': 'Test'
                },
                {
                    'name': 'canComment',
                    'type': None
                },
                {
                    'name': 'autoApplyUpdates',
                    'type': None
                },
                {
                    'name': 'hasHighlights',
                    'type': None
                },
                {
                    'name': 'permalinkDelimiter',
                    'type': None
                },
                {
                    'name': 'stickyPosition',
                    'type': None
                }
            ],
            'i18n': {
                'cs': {
                    'Highlights': 'Hlavní body',
                    'Comment by': 'Komentář',
                    'Powered by': 'Poháněno',
                    'Advertisement': 'reklama',
                    'Cancel': 'Zrušit',
                    'Comment': 'Váš příspěvek',
                    'Comment *': 'Text *',
                    'Comment should be maximum 300 characters in length': 'Maximální délka textu je 300 znaků',
                    'Editorial': 'redakční',
                    'Load more posts': 'Načíst další',
                    'Loading': 'Načítám',
                    'Name *': 'Jméno *',
                    'Name should be maximum 30 characters in length': 'Maximální délka jména je 30 znaků',
                    'Newest first': 'nejnovější',
                    'No posts for now': 'Žádné příspěvky',
                    'Oldest first': 'nejstarší',
                    'One pinned post': 'Jeden připnutý příspěvek',
                    'pinned posts': 'připnuté příspěvky',
                    'Post a comment': 'Otázka / komentář',
                    'See one new update': 'Zobraz 1 nový příspěvek',
                    'See new updates': 'Zobraz nové příspěvky',
                    'Send': 'Odeslat',
                    'Show all posts': 'Zobrazit všechny',
                    'Show highlighted post only': 'Zobraz jen zvýrazněné příspěvky',
                    'Sort by:': 'Řazení:',
                    'Updated': 'Aktualizace',
                    'Your comment was sent for approval': 'Váš text byl úspěšně odeslán Čeká na schválení',
                    'credit:': 'autor:'
                },
                'de': {
                    'Highlights': 'Highlights',
                    'Comment by': 'Kommentar von',
                    'Powered by': 'Unterstützt von',
                    'Advertisement': 'Werbung',
                    'Cancel': 'Abbrechen',
                    'Comment': 'Kommentar',
                    'Comment *': 'Kommentar',
                    'Comment should be maximum 300 characters in length': 'Kommentar \
                        darf maximal 300 Zeichen lang sein',
                    'Editorial': 'Redaktionell',
                    'Load more posts': 'Mehr Einträge laden',
                    'Loading': 'Lade',
                    'Name *': 'Name',
                    'Name should be maximum 30 characters in length': 'Name darf maximal 30 Zeichen lang sein',
                    'Newest first': 'Neueste zuerst',
                    'No posts for now': 'Kein Beitrag vorhanden',
                    'Oldest first': 'Älteste zuerst',
                    'One pinned post': 'Angehefteter Eintrag',
                    'pinned posts': 'Angeheftete Einträge',
                    'Please fill in your Comment': 'Bitte Kommentar hier eintragen',
                    'Please fill in your Name': 'Bitte Namen hier eintragen',
                    'Post a comment': 'Kommentar posten',
                    'See one new update': 'Neuen Beitrag anzeigen',
                    'See new updates': 'Neue Beiträge anzeigen',
                    'Send': 'Abschicken',
                    'Show all posts': 'Alle Beiträge anzeigen',
                    'Show highlighted post only': 'Anzeigen hervorgehoben Beitrag ist nur',
                    'Sort by:': 'Ordnen nach',
                    'Updated': 'Aktualisiert am',
                    'Your comment was sent for approval': 'Ihr Kommentar wartet auf Freischaltung',
                    'credit:': 'Bild:'
                },
                'fi': {
                    'Highlights': 'Kohokohtia',
                    'Comment by': 'Comment by',
                    'Powered by': 'Powered by',
                    'Advertisement': 'Mainos',
                    'Cancel': 'Peruuta',
                    'Comment': 'Kommentoi',
                    'Comment *': 'Kommentti *',
                    'Comment should be maximum 300 characters in length': 'Kommentin enimmäispituus on 300 merkkiä',
                    'Editorial': 'Toimituksellinen',
                    'Load more posts': 'Lataa lisää julkaisuja',
                    'Loading': 'Lataa',
                    'Name *': 'Nimi *',
                    'Name should be maximum 30 characters in length': 'Nimen enimmäispituus on 30 merkkiä',
                    'Newest first': 'Uusimmat ensin',
                    'No posts for now': 'Ei uusia julkaisuja',
                    'Oldest first': 'Vanhimmat ensin',
                    'One pinned post': 'Yksi kiinnitetty julkaisu',
                    'pinned posts': 'kiinnitettyä julkaisua',
                    'Please fill in your Comment': 'Lisää kommenttisi',
                    'Please fill in your Name': 'Lisää nimesi',
                    'Post a comment': 'Lähetä kommentti',
                    'See one new update': 'Lataa yksi uusi julkaisu',
                    'See new updates': 'Lataa uutta julkaisua',
                    'Send': 'Lähetä',
                    'Show all posts': 'Näytä kaikki julkaisut',
                    'Show highlighted post only': 'Näytä vain korostettu julkaisu',
                    'Sort by:': 'Järjestä:',
                    'Updated': 'Päivitetty',
                    'Your comment was sent for approval': 'Kommenttisi lähetettiin hyväksyttäväksi',
                    'credit:': '©'
                },
                'fr': {
                    'Highlights': 'Messages en surbrillance',
                    'Comment by': 'Commentaire de',
                    'Powered by': 'Alimenté par',
                    'Advertisement': 'Publicité',
                    'Cancel': 'Annuler',
                    'Comment': 'Commentaire',
                    'Comment *': 'Commentaire *',
                    'Comment should be maximum 300 characters in length': 'Un commentaire ne peut excéder 300 signes',
                    'Editorial': 'Éditorial',
                    'Load more posts': 'Afficher plus de messages',
                    'Loading': 'Chargement',
                    'Name *': 'Nom *',
                    'Name should be maximum 30 characters in length': 'Le nom ne peut excéder 30 signes',
                    'Newest first': "Le plus récent d'abord",
                    'No posts for now': 'Aucun message pour le moment',
                    'Oldest first': 'Plus ancien en premier',
                    'One pinned post': 'Voir le nouveau message',
                    'pinned posts': 'Voir nouveaux messages',
                    'Please fill in your Comment': 'Votre commentaire',
                    'Please fill in your Name': 'Votre nom',
                    'Post a comment': 'Envoyer un commentaire',
                    'See one new update': 'Voir le nouveau message',
                    'See new updates': 'Voir nouveaux messages',
                    'Send': 'Envoyer',
                    'Show all posts': 'Afficher tous les messages',
                    'Show highlighted post only': 'Afficher uniquement les messages en surbrillance',
                    'Sort by:': 'Trier par:',
                    'Updated': 'Mise à jour',
                    'Your comment was sent for approval': 'Votre commentaire \
                        a été envoyé et est en attente de validation',
                    'credit:': 'crédit:'
                },
                'nl': {
                    'Highlights': 'Highlights',
                    'Comment by': 'Commentaar door',
                    'Powered by': 'Aangedreven door',
                    'Advertisement': 'Advertentie',
                    'Cancel': 'Annuleren',
                    'Comment': 'Reactie',
                    'Comment *': 'Tekst *',
                    'Comment should be maximum 300 characters in length': 'Uw reactie van maximaal 300 tekens',
                    'Editorial': 'Redactioneel',
                    'Load more posts': 'Meer',
                    'Loading': 'Laden',
                    'Name *': 'Naam *',
                    'Name should be maximum 30 characters in length': 'Uw naam kan maximaal 30 tekens lang zijn',
                    'Newest first': 'Toon nieuwste eerst',
                    'No posts for now': 'Nog geen berichten beschikbaar',
                    'Oldest first': 'Toon oudste eerst',
                    'One pinned post': 'Bekijk nieuw bericht',
                    'pinned posts': 'Bekijk nieuwe berichten',
                    'Please fill in your Comment': 'Uw reactie',
                    'Please fill in your Name': 'Vul hier uw naam in',
                    'Post a comment': 'Schrijf een reactie',
                    'See one new update': 'Bekijk nieuw bericht',
                    'See new updates': 'Bekijk nieuwe berichten',
                    'Send': 'Verzenden',
                    'Sort by:': 'Sorteer:',
                    'Your comment was sent for approval': 'Uw reactie is ontvangen ter beoordeling',
                    'credit:': 'credit:'
                },
                'no': {
                    'Highlights': 'Høydepunkter',
                    'Comment by': 'Kommentar av',
                    'Powered by': 'Drevet av',
                    'Advertisement': 'Annonse',
                    'Cancel': 'Avbryt',
                    'Comment': 'Kommentar',
                    'Comment *': 'Kommentar*',
                    'Comment should be maximum 300 characters in length': 'Kommentarer kan være inntil 300 tegn',
                    'Editorial': 'Redaksjonelt',
                    'Load more posts': 'Henter flere poster',
                    'Loading': 'Henter',
                    'Name *': 'Navn*',
                    'Name should be maximum 30 characters in length': 'Navn kan ikke ha mer enn 30 tegn',
                    'Newest first': 'Nyeste først',
                    'No posts for now': 'Ingen poster for øyeblikket',
                    'Oldest first': 'Eldste først',
                    'One pinned post': 'Én post festet til toppen',
                    'pinned posts': 'poster festet til toppen',
                    'Please fill in your Comment': 'Skriv inn din kommentar',
                    'Please fill in your Name': 'Skriv inn navn',
                    'Post a comment': 'Post en kommentar',
                    'See one new update': 'Se én ny oppdatering',
                    'See new updates': 'Se nye oppdateringer',
                    'Send': 'Send',
                    'Show all posts': 'Vis alle poster',
                    'Show highlighted post only': 'Vis bare høydepunkter',
                    'Sort by:': 'Sortér etter:',
                    'Updated': 'Oppdatert',
                    'Your comment was sent for approval': 'Din kommentar er sendt til godkjenning',
                    'credit:': 'credit:'
                },
                'ro': {
                    'Highlights': 'Repere',
                    'Comment by': 'Comentariu de',
                    'Powered by': 'Cu sprijinul',
                    'Advertisement': 'Reclamă',
                    'Cancel': 'Anulează',
                    'Comment': 'Comentează',
                    'Comment *': 'Comentariu *',
                    'Comment should be maximum 300 characters in length': 'Comentariu \
                        nu poate fi mai lung de 300 de caractere',
                    'Editorial': 'Editorial',
                    'Load more posts': 'Încarcă mai multe posturi',
                    'Loading': 'Se încarcă',
                    'Name *': 'Numele *',
                    'Name should be maximum 30 characters in length': 'Numele nu poate fi mai lung de 30 de caractere',
                    'Newest first': 'Cele mai noi',
                    'No posts for now': 'Deocamdata nu sunt articole',
                    'Oldest first': 'Cele mai vechi',
                    'One pinned post': 'Vezi un articol nou',
                    'pinned posts': 'Vezi articole noi',
                    'Please fill in your Comment': 'Completează comentariu',
                    'Please fill in your Name': 'Completează numele',
                    'Post a comment': 'Scrie un comentariu',
                    'See one new update': 'Vezi un articol nou',
                    'See new updates': 'Vezi articole noi',
                    'Send': 'Trimite',
                    'Sort by:': 'Ordonează după:',
                    'Your comment was sent for approval': 'Comentariul tău a fost trimis spre aprobare',
                    'credit:': 'credit:'
                }
            }
        }
        # Create themes
        self.themeservice.save_or_update_theme(self.angular_theme)
        self.themeservice.save_or_update_theme(self.classic_theme)
        self.themeservice.save_or_update_theme(self.default_theme)
        self.themeservice.save_or_update_theme(self.amp_theme)

    def test_a_angular_save_theme_settings(self):
        angular_previous_theme = {
            '_id': ObjectId('5abc9d69fd16ad1ba3e92689'),
            'name': 'angular',
            'abstract': True,
            'version': '3.3.4',
            'options': [
                {
                    'name': 'postsPerPage',
                    'label': 'Number of posts per page',
                    'type': 'number',
                    'default': 20,
                    'help': 'Set the number of posts you want to see at the initialization'
                },
                {
                    'name': 'postOrder',
                    'label': 'Default posts order of the timeline',
                    'type': 'select',
                    'options': [
                        {
                            'value': 'editorial',
                            'label': 'Editorial'
                        },
                        {
                            'value': 'newest_first',
                            'label': 'Newest first'
                        },
                        {
                            'value': 'oldest_first',
                            'label': 'Oldest first'
                        }
                    ],
                    'default': 'editorial'
                },
                {
                    'name': 'permalinkDelimiter',
                    'label': 'Permalink Delimiter',
                    'type': 'select',
                    'options': [
                        {
                            'value': '?',
                            'label': 'Query delimiter (?)'
                        },
                        {
                            'value': '#',
                            'label': ' Fragment identifier delimiter (#)'
                        }
                    ],
                    'default': '?',
                    'help': 'Sets the delimiter used to send the permalink. \
                        ex: permalinkHashMark=?, http://example.com/?...'
                },
                {
                    'name': 'datetimeFormat',
                    'label': 'Date time Format',
                    'type': 'datetimeformat',
                    'default': 'lll',
                    'help': 'Sets the date time format to be used in the embed.\
                     Please enter a custom format in valid moment.js format \
                     http://momentjs.com/docs/#/parsing/string-format'
                }
            ],
            'settings': {
                'postsPerPage': 20,
                'postOrder': 'editorial',
                'permalinkDelimiter': '?',
                'datetimeFormat': '2018-03-29T13:35:51+05:30'
            },
            '_etag': '1b1239c1a88e3386226e84260bfd7c4d1c5e96c7'
        }
        angular_result = self.themeservice._save_theme_settings(self.angular_theme, angular_previous_theme)
        # Keep user settings, saved by user in database
        self.assertEqual(
            angular_previous_theme.get('settings').get('datetimeFormat'), angular_result[0].get('datetimeFormat'))
        # Override the default value present in theme
        self.assertNotEqual(angular_result[1], angular_previous_theme.get('settings'))
        self.assertNotEqual(
            angular_result[1].get('postsPerPage'), angular_previous_theme.get('settings').get('postsPerPage'))
        # Injected new value in theme
        self.assertNotEqual(len(angular_result[1]), len(angular_previous_theme.get('settings')))
        self.assertFalse(angular_previous_theme.get('datetimeFormattest'))
        self.assertTrue(angular_result[1].get('datetimeFormattest'))

    def test_c_classic_save_theme_settings(self):
        # assert self.test_a_angular_save_theme_settings()
        classic_previous_theme = {
            '_id': ObjectId('5abcbf73fd16ad623375bfa3'),
            'name': 'classic',
            'version': '3.3.11',
            'extends': 'angular',
            'options': [
                {
                    'name': 'language',
                    'label': 'Theme language',
                    'type': 'select',
                    'options': [
                        {
                            'value': 'en',
                            'label': 'English'
                        },
                        {
                            'value': 'fi',
                            'label': 'Finnish'
                        },
                        {
                            'value': 'de',
                            'label': 'Deutsch'
                        },
                        {
                            'value': 'fr',
                            'label': 'Français'
                        },
                        {
                            'value': 'nl',
                            'label': 'Nederlands'
                        },
                        {
                            'value': 'no',
                            'label': 'Norsk'
                        },
                        {
                            'value': 'cs',
                            'label': 'Čeština'
                        },
                        {
                            'value': 'ro',
                            'label': 'Română'
                        }
                    ],
                    'default': 'en'
                },
                {
                    'name': 'postsPerPage',
                    'label': 'Number of posts per page',
                    'type': 'number',
                    'default': 20,
                    'help': 'Set the number of posts you want to see per page'
                },
                {
                    'name': 'postOrder',
                    'label': 'Default posts order of the timeline',
                    'type': 'select',
                    'options': [
                        {
                            'value': 'editorial',
                            'label': 'Editorial'
                        },
                        {
                            'value': 'newest_first',
                            'label': 'Newest first'
                        },
                        {
                            'value': 'oldest_first',
                            'label': 'Oldest first'
                        }
                    ],
                    'default': 'editorial'
                },
                {
                    'name': 'loadNewPostsManually',
                    'label': 'User needs to click a button to retrieve the new posts',
                    'type': 'checkbox',
                    'default': True,
                    'help': 'Otherwise they will be loaded periodically'
                },
                {
                    'name': 'infinitScroll',
                    'label': 'Use infinite scroll to load more pages',
                    'type': 'checkbox',
                    'default': True,
                    'help': 'if true, more pages are automatically loaded when the \
                    bottom of the page is reached. Otherwise a button is added at the bottom of the posts list'
                },
                {
                    'name': 'showImage',
                    'label': 'Show the blog image',
                    'type': 'checkbox',
                    'default': True
                },
                {
                    'name': 'showTitle',
                    'label': 'Show the blog title',
                    'type': 'checkbox',
                    'default': True
                },
                {
                    'name': 'showDescription',
                    'label': 'Show the blog description',
                    'type': 'checkbox',
                    'default': True
                },
                {
                    'name': 'showAuthor',
                    'label': 'Show author',
                    'type': 'checkbox',
                    'default': True,
                    'help': 'Show the author information on posts'
                },
                {
                    'name': 'showAuthorAvatar',
                    'label': 'Show author avatar',
                    'type': 'checkbox',
                    'default': True,
                    'dependsOn': {
                        'showAuthor': True
                    },
                    'help': 'Show the author avatar on posts'
                },
                {
                    'name': 'authorNameFormat',
                    'label': 'Author name format',
                    'type': 'select',
                    'default': 'display_name',
                    'dependsOn': {
                        'showAuthor': True
                    },
                    'options': [
                        {
                            'value': 'display_name',
                            'label': 'Full name'
                        },
                        {
                            'value': 'byline',
                            'label': 'Byline'
                        },
                        {
                            'value': 'sign_off',
                            'label': 'Sign off'
                        }
                    ],
                    'help': 'How to show the author name'
                },
                {
                    'name': 'authorNameLinksToEmail',
                    'label': 'The author name links to email',
                    'type': 'checkbox',
                    'default': False,
                    'dependsOn': {
                        'showAuthor': True
                    },
                    'help': 'A click on the author name will create a new email to be sent to the author.'
                },
                {
                    'name': 'permalinkDelimiter',
                    'label': 'Permalink delimiter',
                    'type': 'select',
                    'options': [
                        {
                            'value': '?',
                            'label': 'Query delimiter (?)'
                        },
                        {
                            'value': '#',
                            'label': ' Fragment identifier delimiter (#)'
                        }
                    ],
                    'default': '?',
                    'help': 'Sets the delimiter used to send the permalink. \
                    ex: permalinkHashMark=?, http://example.com/?...'
                },
                {
                    'name': 'canComment',
                    'label': 'Users can comment',
                    'type': 'checkbox',
                    'default': False,
                    'help': 'If the users can comment on the blog'
                },
                {
                    'name': 'hasHighlights',
                    'label': 'Display highlights',
                    'type': 'checkbox',
                    'default': False,
                    'help': 'If the users see the highlight button in the blog'
                },
                {
                    'name': 'blockSearchEngines',
                    'label': 'Block search engines',
                    'type': 'checkbox',
                    'default': False,
                    'help': 'Block search engines from indexing my blogs'
                },
                {
                    'name': 'showGallery',
                    'label': 'Show slideshow gallery',
                    'type': 'checkbox',
                    'default': False,
                    'help': 'If the users will see the slideshow gallery for multiple images posts'
                },
                {
                    'name': 'showSocialShare',
                    'label': 'Show social sharing options',
                    'type': 'checkbox',
                    'default': True,
                    'help': 'If the users will see the social sharing options'
                },
                {
                    'name': 'livestream',
                    'label': 'Pinned post behaviour',
                    'type': 'select',
                    'options': [
                        {
                            'value': False,
                            'label': 'Show below menu bar'
                        },
                        {
                            'value': True,
                            'label': 'Show above menu bar'
                        }
                    ],
                    'default': False
                },
                {
                    'name': 'livestreamAutoplay',
                    'label': 'Autoplay for livestream videos',
                    'type': 'checkbox',
                    'default': False,
                    'help': 'if the users will see the video autoplay for livestream'
                },
                {
                    'name': 'showSyndicatedAuthor',
                    'label': 'Show syndicated author',
                    'type': 'checkbox',
                    'default': False,
                    'help': 'If the users will see the syndicated author'
                }
            ],
            '_etag': 'eae938b66f3d4dcafd46165eb0a2976c7b884a98',
            'settings': {
                'datetimeFormat': '2018-03-29T15:57:08+05:30',
                'language': 'en',
                'postsPerPage': 20,
                'postOrder': 'editorial',
                'loadNewPostsManually': True,
                'infinitScroll': True,
                'showImage': True,
                'showTitle': True,
                'showDescription': True,
                'showAuthor': True,
                'showAuthorAvatar': True,
                'authorNameFormat': 'display_name',
                'authorNameLinksToEmail': False,
                'permalinkDelimiter': '?',
                'canComment': False,
                'hasHighlights': False,
                'blockSearchEngines': False,
                'showGallery': False,
                'showSocialShare': True,
                'livestream': False,
                'livestreamAutoplay': False,
                'showSyndicatedAuthor': False
            }
        }
        classic_result = self.themeservice._save_theme_settings(self.classic_theme, classic_previous_theme)
        # Keep user settings, saved by user in database
        self.assertEqual(
            classic_previous_theme.get('settings').get('datetimeFormat'), classic_result[0].get('datetimeFormat'))
        # Override the default value present in theme
        self.assertNotEqual(classic_result[1], classic_previous_theme.get('settings'))
        self.assertNotEqual(
            classic_result[1].get('postsPerPage'), classic_previous_theme.get('settings').get('postsPerPage'))
        # Injected new value in theme
        self.assertNotEqual(len(classic_result[1]), len(classic_previous_theme.get('settings')))
        self.assertFalse(classic_previous_theme.get('datetimeFormattest'))
        self.assertTrue(classic_result[1].get('datetimeFormattest'))

    def test_b_default_save_theme_settings(self):
        default_previous_theme = {
            '_id': ObjectId('5abcd99afd16ad7de3d3f34a'),
            'name': 'default',
            'version': '3.3.56',
            'asyncTheme': True,
            'seoTheme': True,
            'options': [
                {
                    'name': 'datetimeFormat',
                    'label': 'Date time Format',
                    'type': 'datetimeformat',
                    'default': 'lll',
                    'help': 'Sets the date time format to be used in the \
                    embed. Please enter a custom format in valid moment.js \
                    format http://momentjs.com/docs/#/parsing/string-format'
                },
                {
                    'name': 'showUpdateDatetime',
                    'label': 'Show post update time',
                    'type': 'checkbox',
                    'default': False,
                    'help': 'If activated, users will see an additional timestamp, when the post has been updated'
                },
                {
                    'name': 'postsPerPage',
                    'label': 'Number of posts per page',
                    'type': 'number',
                    'default': 10,
                    'help': 'Set the number of posts you initially want to show to your readers'
                },
                {
                    'name': 'postOrder',
                    'label': 'Default posts order',
                    'type': 'select',
                    'options': [
                        {
                            'value': 'editorial',
                            'label': 'Editorial'
                        },
                        {
                            'value': 'newest_first',
                            'label': 'Newest first'
                        },
                        {
                            'value': 'oldest_first',
                            'label': 'Oldest first'
                        }
                    ],
                    'default': 'editorial'
                },
                {
                    'name': 'autoApplyUpdates',
                    'label': 'All updates are auto-applied periodically',
                    'type': 'checkbox',
                    'default': True,
                    'help': 'Turn off to prompt user to load updates'
                },
                {
                    'name': 'canComment',
                    'label': 'Users can comment',
                    'type': 'checkbox',
                    'default': False,
                    'help': 'Enables a commenting form for users'
                },
                {
                    'name': 'showImage',
                    'label': 'Show the blog image',
                    'type': 'checkbox',
                    'default': False
                },
                {
                    'name': 'showTitle',
                    'label': 'Show the blog title',
                    'type': 'checkbox',
                    'default': False
                },
                {
                    'name': 'showDescription',
                    'label': 'Show the blog description',
                    'type': 'checkbox',
                    'default': False
                },
                {
                    'name': 'showLiveblogLogo',
                    'label': 'Show Liveblog logo',
                    'type': 'checkbox',
                    'default': True,
                    'help': 'Turn off to hide the “powered by Live Blog” logo'
                },
                {
                    'name': 'showAuthor',
                    'label': 'Show the author',
                    'type': 'checkbox',
                    'default': True,
                    'help': 'Show the author information on posts'
                },
                {
                    'name': 'authorNameFormat',
                    'label': 'Author name format',
                    'type': 'select',
                    'default': 'display_name',
                    'dependsOn': {
                        'showAuthor': True
                    },
                    'options': [
                        {
                            'value': 'display_name',
                            'label': 'Full name'
                        },
                        {
                            'value': 'byline',
                            'label': 'Byline'
                        },
                        {
                            'value': 'sign_off',
                            'label': 'Sign off'
                        }
                    ],
                    'help': 'How to show the author info'
                },
                {
                    'name': 'showAuthorAvatar',
                    'label': 'Show author avatar',
                    'type': 'checkbox',
                    'default': True,
                    'dependsOn': {
                        'showAuthor': True
                    },
                    'help': 'Shows an author image besides the author name'
                },
                {
                    'name': 'hasHighlights',
                    'label': 'Show highlight button',
                    'type': 'checkbox',
                    'default': False,
                    'help': 'Introduces a button for the readers to filter the timeline by highlights'
                },
                {
                    'name': 'permalinkDelimiter',
                    'label': 'Permalink delimiter',
                    'type': 'select',
                    'options': [
                        {
                            'value': '?',
                            'label': 'Query delimiter (?)'
                        },
                        {
                            'value': '#',
                            'label': ' Fragment identifier delimiter (#)'
                        }
                    ],
                    'default': '?',
                    'help': 'Sets the delimiter used to send the permalink. \
                    ex: permalinkHashMark=?, http://example.com/?...'
                },
                {
                    'name': 'blockSearchEngines',
                    'label': 'Block search engines',
                    'type': 'checkbox',
                    'default': True,
                    'help': 'Will block search engines from indexing the blog content'
                },
                {
                    'name': 'showGallery',
                    'label': 'Show slideshow gallery',
                    'type': 'checkbox',
                    'default': False,
                    'help': 'Multiple image posts will show up as an image gallery'
                },
                {
                    'name': 'stickyPosition',
                    'label': 'Pinned post behaviour',
                    'type': 'select',
                    'options': [
                        {
                            'value': 'bottom',
                            'label': 'Show below menu bar'
                        },
                        {
                            'value': 'top',
                            'label': 'Show above menu bar'
                        }
                    ],
                    'default': 'bottom',
                    'help': 'Please note: Pinned posts above the menu bar will \
                    not show the author info nor a timestamp. This setting is \
                    especially useful if you want to show a (streaming) video on top of your timeline.'
                },
                {
                    'name': 'gaCode',
                    'label': 'Google analytics code',
                    'type': 'text',
                    'placeholder': 'UA-XXXXX-Y',
                    'default': '',
                    'help': 'Please enter your google analytics account ID.'
                },
                {
                    'name': 'renderForESI',
                    'label': 'Optimise the Live Blog output for ESI',
                    'type': 'checkbox',
                    'default': False,
                    'help': 'Strips the head and body tags from the Live \
                    Blog output to publish it using Edge Side Includes'
                },
                {
                    'name': 'removeStylesESI',
                    'label': 'Remove stylesheet from the Live Blog output for ESI',
                    'type': 'checkbox',
                    'default': False,
                    'help': 'Removes the link to the stylesheet from the \
                    Live Blog output to publish it using Edge Side Includes '
                },
                {
                    'name': 'language',
                    'label': 'Theme language',
                    'type': 'select',
                    'options': [
                        {
                            'value': 'en',
                            'label': 'English'
                        },
                        {
                            'value': 'fi',
                            'label': 'Finnish'
                        },
                        {
                            'value': 'de',
                            'label': 'Deutsch'
                        },
                        {
                            'value': 'fr',
                            'label': 'Français'
                        },
                        {
                            'value': 'nl',
                            'label': 'Nederlands'
                        },
                        {
                            'value': 'no',
                            'label': 'Norsk'
                        },
                        {
                            'value': 'cs',
                            'label': 'Čeština'
                        },
                        {
                            'value': 'ro',
                            'label': 'Română'
                        }
                    ],
                    'default': 'en'
                },
                {
                    'name': 'showSyndicatedAuthor',
                    'label': 'Show syndicated author',
                    'type': 'checkbox',
                    'default': False,
                    'help': 'If the users will see the syndicated author'
                },
                {
                    'name': 'clientDatetimeOnly',
                    'label': 'Show datetime only on client',
                    'type': 'checkbox',
                    'default': False,
                    'help': 'If the users will see the datetime only on client rendered'
                }
            ],
            'i18n': {
                'cs': {
                    'Highlights': 'Hlavní body',
                    'Comment by': 'Komentář',
                    'Powered by': 'Poháněno',
                    'Advertisement': 'reklama',
                    'Cancel': 'Zrušit',
                    'Comment': 'Váš příspěvek',
                    'Comment *': 'Text *',
                    'Comment should be maximum 300 characters in length': 'Maximální délka textu je 300 znaků',
                    'Editorial': 'redakční',
                    'Load more posts': 'Načíst další',
                    'Loading': 'Načítám',
                    'Name *': 'Jméno *',
                    'Name should be maximum 30 characters in length': 'Maximální délka jména je 30 znaků',
                    'Newest first': 'nejnovější',
                    'No posts for now': 'Žádné příspěvky',
                    'Oldest first': 'nejstarší',
                    'One pinned post': 'Jeden připnutý příspěvek',
                    'pinned posts': 'připnuté příspěvky',
                    'Post a comment': 'Otázka / komentář',
                    'See one new update': 'Zobraz 1 nový příspěvek',
                    'See new updates': 'Zobraz nové příspěvky',
                    'Send': 'Odeslat',
                    'Show all posts': 'Zobrazit všechny',
                    'Show highlighted post only': 'Zobraz jen zvýrazněné příspěvky',
                    'Sort by:': 'Řazení:',
                    'Updated': 'Aktualizace',
                    'Your comment was sent for approval': 'Váš text byl úspěšně odeslán Čeká na schválení',
                    'credit:': ' autor:'
                },
                'de': {
                    'Highlights': 'Highlights',
                    'Comment by': 'Kommentar von',
                    'Powered by': 'Unterstützt von',
                    'Advertisement': 'Werbung',
                    'Cancel': 'Abbrechen',
                    'Comment': 'Kommentar',
                    'Comment *': 'Kommentar',
                    'Comment should be maximum 300 characters in length': 'Kommentar \
                    darf maximal 300 Zeichen lang sein',
                    'Editorial': 'Redaktionell',
                    'Load more posts': 'Weitere Beiträge',
                    'Loading': 'Lade',
                    'Name *': 'Name',
                    'Name should be maximum 30 characters in length': 'Name darf maximal 30 Zeichen lang sein',
                    'Newest first': 'Neueste zuerst',
                    'No posts for now': 'Kein Beitrag vorhanden',
                    'Oldest first': 'Älteste zuerst',
                    'One pinned post': 'Angehefteter Eintrag',
                    'pinned posts': 'Angeheftete Einträge',
                    'Please fill in your Comment': 'Bitte Kommentar hier eintragen',
                    'Please fill in your Name': 'Bitte Namen hier eintragen',
                    'Post a comment': 'Kommentar posten',
                    'See one new update': 'Neuen Beitrag anzeigen',
                    'See new updates': 'Neue Beiträge anzeigen',
                    'Send': 'Abschicken',
                    'Show all posts': 'Alle Beiträge anzeigen',
                    'Show highlighted post only': 'Anzeigen hervorgehoben Beitrag ist nur',
                    'Sort by:': 'Ordnen nach',
                    'Updated': 'Aktualisiert am',
                    'Your comment was sent for approval': 'Ihr Kommentar wartet auf Freischaltung',
                    'credit:': 'Bild:'
                },
                'fi': {
                    'Highlights': 'Kohokohtia',
                    'Comment by': 'Comment by',
                    'Powered by': 'Powered by',
                    'Advertisement': 'Mainos',
                    'Cancel': 'Peruuta',
                    'Comment': 'Kommentoi',
                    'Comment *': 'Kommentti *',
                    'Comment should be maximum 300 characters in length': 'Kommentin enimmäispituus on 300 merkkiä',
                    'Editorial': 'Toimituksellinen',
                    'Load more posts': 'Lataa lisää julkaisuja',
                    'Loading': 'Lataa',
                    'Name *': 'Nimi *',
                    'Name should be maximum 30 characters in length': 'Nimen enimmäispituus on 30 merkkiä',
                    'Newest first': 'Uusimmat ensin',
                    'No posts for now': 'Ei uusia julkaisuja',
                    'Oldest first': 'Vanhimmat ensin',
                    'One pinned post': 'Yksi kiinnitetty julkaisu',
                    'pinned posts': 'kiinnitettyä julkaisua',
                    'Please fill in your Comment': 'Lisää kommenttisi',
                    'Please fill in your Name': 'Lisää nimesi',
                    'Post a comment': 'Lähetä kommentti',
                    'See one new update': 'Lataa yksi uusi julkaisu',
                    'See new updates': 'Lataa uutta julkaisua',
                    'Send': 'Lähetä',
                    'Show all posts': 'Näytä kaikki julkaisut',
                    'Show highlighted post only': 'Näytä vain korostettu julkaisu',
                    'Sort by:': 'Järjestä:',
                    'Updated': 'Päivitetty',
                    'Your comment was sent for approval': 'Kommenttisi lähetettiin hyväksyttäväksi',
                    'credit:': '©'
                },
                'fr': {
                    'Highlights': 'Messages en surbrillance',
                    'Comment by': 'Commentaire de',
                    'Powered by': 'Alimenté par',
                    'Advertisement': 'Publicité',
                    'Cancel': 'Annuler',
                    'Comment': 'Commentaire',
                    'Comment *': 'Commentaire *',
                    'Comment should be maximum 300 characters in length': 'Un commentaire ne peut excéder 300 signes',
                    'Editorial': 'Éditorial',
                    'Load more posts': 'Afficher plus de messages',
                    'Loading': 'Chargement',
                    'Name *': 'Nom *',
                    'Name should be maximum 30 characters in length': 'Le nom ne peut excéder 30 signes',
                    'Newest first': "Le plus récent d'abord",
                    'No posts for now': 'Aucun message pour le moment',
                    'Oldest first': 'Plus ancien en premier',
                    'One pinned post': 'Voir le nouveau message',
                    'pinned posts': 'Voir nouveaux messages',
                    'Please fill in your Comment': 'Votre commentaire',
                    'Please fill in your Name': 'Votre nom',
                    'Post a comment': 'Envoyer un commentaire',
                    'See one new update': 'Voir le nouveau message',
                    'See new updates': 'Voir nouveaux messages',
                    'Send': 'Envoyer',
                    'Show all posts': 'Afficher tous les messages',
                    'Show highlighted post only': 'Afficher uniquement les messages en surbrillance',
                    'Sort by:': 'Trier par:',
                    'Updated': 'Mise à jour',
                    'Your comment was sent for approval': 'Votre commentaire \
                    a été envoyé et est en attente de validation',
                    'credit:': 'crédit:'
                },
                'nl': {
                    'Highlights': 'Highlights',
                    'Comment by': 'Commentaar door',
                    'Powered by': 'Aangedreven door',
                    'Advertisement': 'Advertentie',
                    'Cancel': 'Annuleren',
                    'Comment': 'Reactie',
                    'Comment *': 'Tekst *',
                    'Comment should be maximum 300 characters in length': 'Uw reactie van maximaal 300 tekens',
                    'Editorial': 'Redactioneel',
                    'Load more posts': 'Meer',
                    'Loading': 'Laden',
                    'Name *': 'Naam *',
                    'Name should be maximum 30 characters in length': 'Uw naam kan maximaal 30 tekens lang zijn',
                    'Newest first': 'Toon nieuwste eerst',
                    'No posts for now': 'Nog geen berichten beschikbaar',
                    'Oldest first': 'Toon oudste eerst',
                    'One pinned post': 'Bekijk nieuw bericht',
                    'pinned posts': 'Bekijk nieuwe berichten',
                    'Please fill in your Comment': 'Uw reactie',
                    'Please fill in your Name': 'Vul hier uw naam in',
                    'Post a comment': 'Schrijf een reactie',
                    'See one new update': 'Bekijk nieuw bericht',
                    'See new updates': 'Bekijk nieuwe berichten',
                    'Send': 'Verzenden',
                    'Sort by:': 'Sorteer:',
                    'Your comment was sent for approval': 'Uw reactie is ontvangen ter beoordeling',
                    'credit:': 'credit:'
                },
                'no': {
                    'Highlights': 'Høydepunkter',
                    'Comment by': 'Kommentar av',
                    'Powered by': 'Drevet av',
                    'Advertisement': 'Annonse',
                    'Cancel': 'Avbryt',
                    'Comment': 'Kommentar',
                    'Comment *': 'Kommentar*',
                    'Comment should be maximum 300 characters in length': 'Kommentarer kan være inntil 300 tegn',
                    'Editorial': 'Redaksjonelt',
                    'Load more posts': 'Henter flere poster',
                    'Loading': 'Henter',
                    'Name *': 'Navn*',
                    'Name should be maximum 30 characters in length': 'Navn kan ikke ha mer enn 30 tegn',
                    'Newest first': 'Nyeste først',
                    'No posts for now': 'Ingen poster for øyeblikket',
                    'Oldest first': 'Eldste først',
                    'One pinned post': 'Én post festet til toppen',
                    'pinned posts': 'poster festet til toppen',
                    'Please fill in your Comment': 'Skriv inn din kommentar',
                    'Please fill in your Name': 'Skriv inn navn',
                    'Post a comment': 'Post en kommentar',
                    'See one new update': 'Se én ny oppdatering',
                    'See new updates': 'Se nye oppdateringer',
                    'Send': 'Send',
                    'Show all posts': 'Vis alle poster',
                    'Show highlighted post only': 'Vis bare høydepunkter',
                    'Sort by:': 'Sortér etter:',
                    'Updated': 'Oppdatert',
                    'Your comment was sent for approval': 'Din kommentar er sendt til godkjenning',
                    'credit:': 'credit:'
                },
                'ro': {
                    'Highlights': 'Repere',
                    'Comment by': 'Comentariu de',
                    'Powered by': 'Cu sprijinul',
                    'Advertisement': 'Reclamă',
                    'Cancel': 'Anulează',
                    'Comment': 'Comentează',
                    'Comment *': 'Comentariu *',
                    'Comment should be maximum 300 characters in length': 'Comentariu \
                    nu poate fi mai lung de 300 de caractere',
                    'Editorial': 'Editorial',
                    'Load more posts': 'Încarcă mai multe posturi',
                    'Loading': 'Se încarcă',
                    'Name *': 'Numele *',
                    'Name should be maximum 30 characters in length': 'Numele nu poate fi mai lung de 30 de caractere',
                    'Newest first': 'Cele mai noi',
                    'No posts for now': 'Deocamdata nu sunt articole',
                    'Oldest first': 'Cele mai vechi',
                    'One pinned post': 'Vezi un articol nou',
                    'pinned posts': 'Vezi articole noi',
                    'Please fill in your Comment': 'Completează comentariu',
                    'Please fill in your Name': 'Completează numele',
                    'Post a comment': 'Scrie un comentariu',
                    'See one new update': 'Vezi un articol nou',
                    'See new updates': 'Vezi articole noi',
                    'Send': 'Trimite',
                    'Sort by:': 'Ordonează după:',
                    'Your comment was sent for approval': 'Comentariul tău a fost trimis spre aprobare',
                    'credit:': 'credit:'
                }
            },
            '_etag': '96e02349a2ebf6c526ea1eda40f647349b7dbbd8',
            'settings': {
                'datetimeFormat': '2018-03-29T17:48:50+05:30',
                'showUpdateDatetime': False,
                'postsPerPage': 10,
                'postOrder': 'editorial',
                'autoApplyUpdates': True,
                'canComment': False,
                'showImage': False,
                'showTitle': False,
                'showDescription': False,
                'showLiveblogLogo': True,
                'showAuthor': True,
                'authorNameFormat': 'display_name',
                'showAuthorAvatar': True,
                'hasHighlights': False,
                'permalinkDelimiter': '?',
                'blockSearchEngines': True,
                'showGallery': False,
                'stickyPosition': 'bottom',
                'gaCode': '',
                'renderForESI': False,
                'removeStylesESI': False,
                'language': 'en',
                'showSyndicatedAuthor': False,
                'clientDatetimeOnly': False
            }
        }
        default_result = self.themeservice._save_theme_settings(self.default_theme, default_previous_theme)
        # Keep user settings, saved by user in database
        self.assertEqual(
            default_previous_theme.get('settings').get('datetimeFormat'), default_result[0].get('datetimeFormat'))
        # Override the default value present in theme
        self.assertNotEqual(default_result[1], default_previous_theme.get('settings'))
        self.assertNotEqual(
            default_result[1].get('postsPerPage'), default_previous_theme.get('settings').get('postsPerPage'))
        # Injected new value in theme
        self.assertNotEqual(len(default_result[1]), len(default_previous_theme.get('settings')))
        self.assertFalse(default_previous_theme.get('datetimeFormattest'))
        self.assertTrue(default_result[1].get('datetimeFormattest'))

    def test_d_amp_save_theme_settings(self):
        # assert self.test_b_default_save_theme_settings()
        amp_previous_theme = {
            '_id': ObjectId('5abcd99afd16ad7de3d3f349'),
            'name': 'amp',
            'version': '3.3.22',
            'seoTheme': True,
            'ampTheme': True,
            'extends': 'default',
            'options': [
                {
                    'name': 'postsPerPage',
                    'label': 'Number of posts per page',
                    'type': 'number',
                    'default': 100,
                    'help': 'Be aware that paging is not yet available for the Liveblog 3 AMP theme'
                },
                {
                    'name': 'canComment',
                    'type': None
                },
                {
                    'name': 'autoApplyUpdates',
                    'type': None
                },
                {
                    'name': 'hasHighlights',
                    'type': None
                },
                {
                    'name': 'permalinkDelimiter',
                    'type': None
                },
                {
                    'name': 'stickyPosition',
                    'type': None
                }
            ],
            'i18n': {
                'cs': {
                    'Highlights': 'Hlavní body',
                    'Comment by': 'Komentář',
                    'Powered by': 'Poháněno',
                    'Advertisement': 'reklama',
                    'Cancel': 'Zrušit',
                    'Comment': 'Váš příspěvek',
                    'Comment *': 'Text *',
                    'Comment should be maximum 300 characters in length': 'Maximální délka textu je 300 znaků',
                    'Editorial': 'redakční',
                    'Load more posts': 'Načíst další',
                    'Loading': 'Načítám',
                    'Name *': 'Jméno *',
                    'Name should be maximum 30 characters in length': 'Maximální délka jména je 30 znaků',
                    'Newest first': 'nejnovější',
                    'No posts for now': 'Žádné příspěvky',
                    'Oldest first': 'nejstarší',
                    'One pinned post': 'Jeden připnutý příspěvek',
                    'pinned posts': 'připnuté příspěvky',
                    'Post a comment': 'Otázka / komentář',
                    'See one new update': 'Zobraz 1 nový příspěvek',
                    'See new updates': 'Zobraz nové příspěvky',
                    'Send': 'Odeslat',
                    'Show all posts': 'Zobrazit všechny',
                    'Show highlighted post only': 'Zobraz jen zvýrazněné příspěvky',
                    'Sort by:': 'Řazení:',
                    'Updated': 'Aktualizace',
                    'Your comment was sent for approval': 'Váš text byl úspěšně odeslán Čeká na schválení',
                    'credit:': 'autor:'
                },
                'de': {
                    'Highlights': 'Highlights',
                    'Comment by': 'Kommentar von',
                    'Powered by': 'Unterstützt von',
                    'Advertisement': 'Werbung',
                    'Cancel': 'Abbrechen',
                    'Comment': 'Kommentar',
                    'Comment *': 'Kommentar',
                    'Comment should be maximum 300 characters in length': 'Kommentar \
                    darf maximal 300 Zeichen lang sein',
                    'Editorial': 'Redaktionell',
                    'Load more posts': 'Mehr Einträge laden',
                    'Loading': 'Lade',
                    'Name *': 'Name',
                    'Name should be maximum 30 characters in length': 'Name darf maximal 30 Zeichen lang sein',
                    'Newest first': 'Neueste zuerst',
                    'No posts for now': 'Kein Beitrag vorhanden',
                    'Oldest first': 'Älteste zuerst',
                    'One pinned post': 'Angehefteter Eintrag',
                    'pinned posts': 'Angeheftete Einträge',
                    'Please fill in your Comment': 'Bitte Kommentar hier eintragen',
                    'Please fill in your Name': 'Bitte Namen hier eintragen',
                    'Post a comment': 'Kommentar posten',
                    'See one new update': 'Neuen Beitrag anzeigen',
                    'See new updates': 'Neue Beiträge anzeigen',
                    'Send': 'Abschicken',
                    'Show all posts': 'Alle Beiträge anzeigen',
                    'Show highlighted post only': 'Anzeigen hervorgehoben Beitrag ist nur',
                    'Sort by:': 'Ordnen nach',
                    'Updated': 'Aktualisiert am',
                    'Your comment was sent for approval': 'Ihr Kommentar wartet auf Freischaltung',
                    'credit:': 'Bild:'
                },
                'fi': {
                    'Highlights': 'Kohokohtia',
                    'Comment by': 'Comment by',
                    'Powered by': 'Powered by',
                    'Advertisement': 'Mainos',
                    'Cancel': 'Peruuta',
                    'Comment': 'Kommentoi',
                    'Comment *': 'Kommentti *',
                    'Comment should be maximum 300 characters in length': 'Kommentin enimmäispituus on 300 merkkiä',
                    'Editorial': 'Toimituksellinen',
                    'Load more posts': 'Lataa lisää julkaisuja',
                    'Loading': 'Lataa',
                    'Name *': 'Nimi *',
                    'Name should be maximum 30 characters in length': 'Nimen enimmäispituus on 30 merkkiä',
                    'Newest first': 'Uusimmat ensin',
                    'No posts for now': 'Ei uusia julkaisuja',
                    'Oldest first': 'Vanhimmat ensin',
                    'One pinned post': 'Yksi kiinnitetty julkaisu',
                    'pinned posts': 'kiinnitettyä julkaisua',
                    'Please fill in your Comment': 'Lisää kommenttisi',
                    'Please fill in your Name': 'Lisää nimesi',
                    'Post a comment': 'Lähetä kommentti',
                    'See one new update': 'Lataa yksi uusi julkaisu',
                    'See new updates': 'Lataa uutta julkaisua',
                    'Send': 'Lähetä',
                    'Show all posts': 'Näytä kaikki julkaisut',
                    'Show highlighted post only': 'Näytä vain korostettu julkaisu',
                    'Sort by:': 'Järjestä:',
                    'Updated': 'Päivitetty',
                    'Your comment was sent for approval': 'Kommenttisi lähetettiin hyväksyttäväksi',
                    'credit:': '©'
                },
                'fr': {
                    'Highlights': 'Messages en surbrillance',
                    'Comment by': 'Commentaire de',
                    'Powered by': 'Alimenté par',
                    'Advertisement': 'Publicité',
                    'Cancel': 'Annuler',
                    'Comment': 'Commentaire',
                    'Comment *': 'Commentaire *',
                    'Comment should be maximum 300 characters in length': 'Un commentaire ne peut excéder 300 signes',
                    'Editorial': 'Éditorial',
                    'Load more posts': 'Afficher plus de messages',
                    'Loading': 'Chargement',
                    'Name *': 'Nom *',
                    'Name should be maximum 30 characters in length': 'Le nom ne peut excéder 30 signes',
                    'Newest first': "Le plus récent d'abord",
                    'No posts for now': 'Aucun message pour le moment',
                    'Oldest first': 'Plus ancien en premier',
                    'One pinned post': 'Voir le nouveau message',
                    'pinned posts': 'Voir nouveaux messages',
                    'Please fill in your Comment': 'Votre commentaire',
                    'Please fill in your Name': 'Votre nom',
                    'Post a comment': 'Envoyer un commentaire',
                    'See one new update': 'Voir le nouveau message',
                    'See new updates': 'Voir nouveaux messages',
                    'Send': 'Envoyer',
                    'Show all posts': 'Afficher tous les messages',
                    'Show highlighted post only': 'Afficher uniquement les messages en surbrillance',
                    'Sort by:': 'Trier par:',
                    'Updated': 'Mise à jour',
                    'Your comment was sent for approval': 'Votre commentaire\
                     a été envoyé et est en attente de validation',
                    'credit:': 'crédit:'
                },
                'nl': {
                    'Highlights': 'Highlights',
                    'Comment by': 'Commentaar door',
                    'Powered by': 'Aangedreven door',
                    'Advertisement': 'Advertentie',
                    'Cancel': 'Annuleren',
                    'Comment': 'Reactie',
                    'Comment *': 'Tekst *',
                    'Comment should be maximum 300 characters in length': 'Uw reactie van maximaal 300 tekens',
                    'Editorial': 'Redactioneel',
                    'Load more posts': 'Meer',
                    'Loading': 'Laden',
                    'Name *': 'Naam *',
                    'Name should be maximum 30 characters in length': 'Uw naam kan maximaal 30 tekens lang zijn',
                    'Newest first': 'Toon nieuwste eerst',
                    'No posts for now': 'Nog geen berichten beschikbaar',
                    'Oldest first': 'Toon oudste eerst',
                    'One pinned post': 'Bekijk nieuw bericht',
                    'pinned posts': 'Bekijk nieuwe berichten',
                    'Please fill in your Comment': 'Uw reactie',
                    'Please fill in your Name': 'Vul hier uw naam in',
                    'Post a comment': 'Schrijf een reactie',
                    'See one new update': 'Bekijk nieuw bericht',
                    'See new updates': 'Bekijk nieuwe berichten',
                    'Send': 'Verzenden',
                    'Sort by:': 'Sorteer:',
                    'Your comment was sent for approval': 'Uw reactie is ontvangen ter beoordeling',
                    'credit:': 'credit:'
                },
                'no': {
                    'Highlights': 'Høydepunkter',
                    'Comment by': 'Kommentar av',
                    'Powered by': 'Drevet av',
                    'Advertisement': 'Annonse',
                    'Cancel': 'Avbryt',
                    'Comment': 'Kommentar',
                    'Comment *': 'Kommentar*',
                    'Comment should be maximum 300 characters in length': 'Kommentarer kan være inntil 300 tegn',
                    'Editorial': 'Redaksjonelt',
                    'Load more posts': 'Henter flere poster',
                    'Loading': 'Henter',
                    'Name *': 'Navn*',
                    'Name should be maximum 30 characters in length': 'Navn kan ikke ha mer enn 30 tegn',
                    'Newest first': 'Nyeste først',
                    'No posts for now': 'Ingen poster for øyeblikket',
                    'Oldest first': 'Eldste først',
                    'One pinned post': 'Én post festet til toppen',
                    'pinned posts': 'poster festet til toppen',
                    'Please fill in your Comment': 'Skriv inn din kommentar',
                    'Please fill in your Name': 'Skriv inn navn',
                    'Post a comment': 'Post en kommentar',
                    'See one new update': 'Se én ny oppdatering',
                    'See new updates': 'Se nye oppdateringer',
                    'Send': 'Send',
                    'Show all posts': 'Vis alle poster',
                    'Show highlighted post only': 'Vis bare høydepunkter',
                    'Sort by:': 'Sortér etter:',
                    'Updated': 'Oppdatert',
                    'Your comment was sent for approval': 'Din kommentar er sendt til godkjenning',
                    'credit:': 'credit:'
                },
                'ro': {
                    'Highlights': 'Repere',
                    'Comment by': 'Comentariu de',
                    'Powered by': 'Cu sprijinul',
                    'Advertisement': 'Reclamă',
                    'Cancel': 'Anulează',
                    'Comment': 'Comentează',
                    'Comment *': 'Comentariu *',
                    'Comment should be maximum 300 characters in length': 'Comentariu \
                    nu poate fi mai lung de 300 de caractere',
                    'Editorial': 'Editorial',
                    'Load more posts': 'Încarcă mai multe posturi',
                    'Loading': 'Se încarcă',
                    'Name *': 'Numele *',
                    'Name should be maximum 30 characters in length': 'Numele nu poate fi mai lung de 30 de caractere',
                    'Newest first': 'Cele mai noi',
                    'No posts for now': 'Deocamdata nu sunt articole',
                    'Oldest first': 'Cele mai vechi',
                    'One pinned post': 'Vezi un articol nou',
                    'pinned posts': 'Vezi articole noi',
                    'Please fill in your Comment': 'Completează comentariu',
                    'Please fill in your Name': 'Completează numele',
                    'Post a comment': 'Scrie un comentariu',
                    'See one new update': 'Vezi un articol nou',
                    'See new updates': 'Vezi articole noi',
                    'Send': 'Trimite',
                    'Sort by:': 'Ordonează după:',
                    'Your comment was sent for approval': 'Comentariul tău a fost trimis spre aprobare',
                    'credit:': 'credit:'
                }
            },
            '_etag': '6264fdae8e153dae910caeebfd3124819bee4a93',
            'settings': {
                'datetimeFormat': '2018-03-29T17:48:50+05:30',
                'showUpdateDatetime': False,
                'postOrder': 'editorial',
                'showImage': False,
                'showTitle': False,
                'showDescription': False,
                'showLiveblogLogo': True,
                'showAuthor': True,
                'authorNameFormat': 'display_name',
                'showAuthorAvatar': True,
                'blockSearchEngines': True,
                'showGallery': False,
                'gaCode': '',
                'renderForESI': False,
                'removeStylesESI': False,
                'language': 'en',
                'showSyndicatedAuthor': False,
                'clientDatetimeOnly': False,
                'postsPerPage': 100
            }
        }
        amp_result = self.themeservice._save_theme_settings(self.amp_theme, amp_previous_theme)
        # Keep user settings, saved by user in database
        self.assertEqual(amp_previous_theme.get('settings').get('datetimeFormat'), amp_result[0].get('datetimeFormat'))
        # Override the default value present in theme
        self.assertNotEqual(amp_result[1], amp_previous_theme.get('settings'))
        self.assertNotEqual(amp_result[1].get('postsPerPage'), amp_previous_theme.get('settings').get('postsPerPage'))
        # Injected new value in theme
        self.assertNotEqual(len(amp_result[1]), len(amp_previous_theme.get('settings')))
        self.assertFalse(amp_previous_theme.get('datetimeFormattest'))
        self.assertTrue(amp_result[1].get('datetimeFormattest'))

    def test_classic_theme(self):
        # Load the template in classic theme, template found
        template = embeds.collect_theme_assets(self.classic_theme)[1]
        self.assertIsNotNone(template, True)

    def test_angular_theme(self):
        # Load the template in angular theme, template not found
        template = embeds.collect_theme_assets(self.angular_theme)[1]
        self.assertIsNone(template, True)

    def test_default_theme(self):
        # Load the template in default theme, template found
        template = embeds.collect_theme_assets(self.default_theme)[1]
        self.assertIsNotNone(template, True)

    def test_amp_theme(self):
        # Load the template in amp theme, template found
        template = embeds.collect_theme_assets(self.amp_theme)[1]
        self.assertIsNotNone(template, True)
