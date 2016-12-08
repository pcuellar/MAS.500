import mediacloud
import json
import datetime

class TrumpClintonMediaPresence:

    # sentences related with Trump and Clinton
    def __init__(self):
        self.mc = None
        self.words_trump = None

    def clump_sentences(self):
        self.mc = mediacloud.api.MediaCloud('MY_API_KEY')
        self.clinton = self.mc.sentenceCount('( hillary AND clinton)', solr_filter=[self.mc.publish_date_query(datetime.date(2016, 10, 7), datetime.date(2016, 10, 14)), 'tags_id_media:1'])
        self.trump = self.mc.sentenceCount('( donald AND trump)', solr_filter=[self.mc.publish_date_query(datetime.date(2016, 10, 7), datetime.date(2016, 10, 14)), 'tags_id_media:1'])
        print self.clinton['count']
        print self.trump['count']
        # I decided to call this request for October given that Trump's tape was released in early October. I'm not sure how big of a difference 6K sentences are but given the
        # magnitude of the content of the tape I would expect a lot more coverage of Trump on mainstream media in the week right after the video was released.

    # Related words on stories talking about Clinton and Trump
    def clump_words(self):
        self.mc = mediacloud.api.MediaCloud('48d9fd877527e6c8c5ff25553c124b1634b8b2926310e2d259d6518221e2a5f2')
        self.words_trump = self.mc.wordCount('( donald AND trump)',  solr_filter=[self.mc.publish_date_query(datetime.date(2016, 10, 7), datetime.date(2016, 10, 14)), 'tags_id_media:1'])
        print self.words_trump[0]
        print self.words_trump[1]
        print self.words_trump[2]
        print self.words_trump[3]
        print self.words_trump[4]
        print self.words_trump[5]
        print self.words_trump[6]
        print self.words_trump[7]
        print self.words_trump[8]
        print self.words_trump[9]
        # also suprising no reference to the tape is showing in related words
