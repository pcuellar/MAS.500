import ConfigParser, logging, datetime, os, collections

from flask import Flask, render_template, request

import mediacloud

CONFIG_FILE = 'settings.config'
basedir = os.path.dirname(os.path.realpath(__file__))
basedir = os.path.dirname(os.path.realpath(__file__))

# load the settings file
config = ConfigParser.ConfigParser()
config.read(os.path.join(basedir, 'settings.config'))

# set up logging
log_file_path = os.path.join(basedir,'logs','mcserver.log')
logging.basicConfig(filename=log_file_path,level=logging.DEBUG)
logging.info("Starting the MediaCloud example Flask app!")

# clean a mediacloud api client
mc = mediacloud.api.MediaCloud( config.get('mediacloud','api_key') )

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("search-form.html")

@app.route("/search",methods=['POST'])
def search_results():
    keywords = request.form['keywords']
    results = mc.sentenceCount(keywords, solr_filter=[mc.publish_date_query( datetime.date( 2015, 5, 01), datetime.date( 2016, 4, 01) ),
        'media_sets_id:1' ], split=True, split_start_date='2015-05-01', split_end_date='2016-04-01', split_daily=False)

    # I figured the split weeks issue with inspiration from Jasmin Rubinovitz code here https://github.com/jasrub/MediaCloud-Flask-Example
    sentenceCount = results['split']
    orderedSentenceCount = collections.OrderedDict(sorted(sentenceCount.items() ))
    splitDates = [key[:10] for key in orderedSentenceCount.keys()[:-3]]
    orderedCount = sorted(orderedSentenceCount.values()[:-3])

    # Turn arrays into strings to be sent to Highcharts
    stringDates = ','.join(splitDates)
    stringCounts = str(orderedCount).strip('[]').strip(' ')

    return render_template("search-results.html",
        keywords=keywords, sentenceCount=results['count'], xAxis=stringDates, ySeries=stringCounts)

if __name__ == "__main__":
    app.debug = True
    app.run()
