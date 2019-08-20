#!/usr/bin/python

paths = []

from os import listdir
from os.path import isdir, isfile, join
import datetime

top_years = [ _ for _ in listdir('docs/') if isdir(join('docs', _)) ]
top_years.remove('css')
top_years.remove('fonts')
top_years = sorted(top_years)

def month_to_str(m):
    return datetime.date(1900, int(m), 1).strftime('%B')

PAGE_PREFIX = '''
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>DOHA Case Data Extraction</title>
        <link rel="stylesheet" href="/osd-ogc-doha-data-extract/css/uswds.min.css">
    </head>
    <body>
'''

INDEX_CONTENT_PREFIX = '''
        <section class="usa-section bg-base-lightest">
            <div class="grid-container">
                <div class="usa-logo site-logo" id="logo">
                    <em class="usa-logo__text">
                        <h1 class="site-title">DOHA Case Data Extraction</h1>
                    </em>
                </div>
                <div class="grid-row grid-gap tablet:margin-top-3">
                    <div class="tablet:grid-col">
                        <p>
                            The authoratative data source for this data is hosted at <a href="http://ogc.osd.mil/doha/industrial/">http://ogc.osd.mil/doha/industrial/</a>.
                        </p>
                        <p>
                            This data was extracted from PDF to text for automated analysis of the case data.
                        </p>
                        <p>
                            Please expect certain data to be lost in the transition, and refer to the official data source to validate as needed.
                        </p>
                    </div>
                </div>
            </div>
        </section>

        <section class="usa-section bg-base-light">
            <div class="grid-container">
                <h2 class="font-lang-xl margin-y-0 line-height-serif-2">Summary</h2>
                <div class="grid-row grid-gap tablet:margin-top-3">
                    <div class="tablet:grid-col">
                        <p><a href="/osd-ogc-doha-data-extract/data.txt">data.txt</a></p>
                        <p>A summary of case data</p>
                    </div>
                </div>
            </div>
        </section>

        <section class="usa-section bg-base-lightest">
            <div class="grid-container">
                <h2 class="font-lang-xl margin-y-0 line-height-serif-2">Cases</h2>
                <div class="grid-row grid-gap tablet:margin-top-3">
                    <div class="tablet:grid-col">
'''

SUB_CONTENT_PREFIX = '''
        <section class="usa-section bg-base-lightest">
            <div class="grid-container">
                <div class="usa-logo site-logo" id="logo">
                    <em class="usa-logo__text">
                        <h1 class="site-title">DOHA Case Data Extraction</h1>
                    </em>
                </div>
            </div>
        </section>

        <section class="usa-section bg-base-lightest">
            <div class="grid-container">
                <h2 class="font-lang-xl margin-y-0 line-height-serif-2">Cases</h2>
                <div class="grid-row grid-gap tablet:margin-top-3">
                    <div class="tablet:grid-col">
'''

SUB_CONTENT_SUFFIX = '''
                </div>
            </div>
        </div>
    </section>
'''

INDEX_CONTENT_SUFFIX = '''
                </div>
            </div>
        </div>
    </section>
'''

PAGE_SUFFIX = '''
    </body>
</html>
'''

with open('docs/index.html', 'w') as f:
    f.write(PAGE_PREFIX)
    f.write(INDEX_CONTENT_PREFIX)
    for year in top_years:
        f.write('<p><a href="/osd-ogc-doha-data-extract/' + year + '/index.html">' + year + '</a></p>')
    f.write(INDEX_CONTENT_SUFFIX)
    f.write(PAGE_SUFFIX)

for year in top_years:
    with open(join('docs', year, 'index.html'), 'w') as f:
        f.write(PAGE_PREFIX)
        f.write(SUB_CONTENT_PREFIX)

        if year == 'unknown':
            files = [ _ for _ in listdir(join('docs', year)) if isfile(join('docs', year, _)) ]
            if 'index.html' in files:
                files.remove('index.html')
            files = sorted(files)
            for file in files:
                f.write('<p><a href="/osd-ogc-doha-data-extract/' + join(year, file) + '">' + file + '</a></p>')
        else:
            months = [ _ for _ in listdir(join('docs', year)) if isdir(join('docs', year, _)) ]
            months = sorted(months)
            for m in months:
                month_folder = join(year, m)
                f.write('<h4>' + month_to_str(m) + '</h4>')
                files = [ _ for _ in listdir(join('docs', month_folder)) if isfile(join('docs', month_folder, _)) ]
                if 'index.html' in files:
                    files.remove('index.html')
                files = sorted(files)
                for file  in files:
                    f.write('<p><a href="/osd-ogc-doha-data-extract/' + join(month_folder, file) + '">' + file + '</a></p>')


        f.write(SUB_CONTENT_SUFFIX)
        f.write(PAGE_SUFFIX)


