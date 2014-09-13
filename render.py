"""
Script to render all markdown documents in the repository

Uses the Github Markdown API
"""

import requests
import json
import sys
import settings
import logging

logging.basicConfig(filename='logs/render.log', level=logging.DEBUG)


def render_markdown(md_file_path):
    """ Renders the markdown file with the given filename """
    content = None
    with open(md_file_path, 'r') as md_file:
        content = md_file.read()

    if content is None:
        # Some error occurred, log it and return
        logging.info('Error occurred rendering markdown file at: ' + md_file_path)
        return

    # Setup and submit request
    params = {'text': content, 'mode': 'markdown'}
    response = requests.post(settings.GITHUB_API_URL + '/markdown', data=json.dumps(params))

    print response.text

def main(arguments):
    """ Handles argument parsing """
    render_markdown(arguments[1])

if __name__ == '__main__':
    main(sys.argv)

