"""
Script to render all markdown documents in the repository

Uses the Github Markdown API
"""

import requests
import json
import sys
import settings
import logging

# Configuration
flags = ['-d', '-f']
logging.basicConfig(filename='logs/render.log', level=logging.DEBUG)


def render_markdown(md_file_path):
    """ Renders the markdown file with the given filename """
    content = None
    try:
        content = open(md_file_path, 'r').read()
    except:
        # Some error occurred, log it and return
        logging.info('Error occurred rendering markdown file at: ' + md_file_path)
        print 'Rendering failed, see logs for details'
        return

    # Setup and submit request
    params = {'text': content, 'mode': 'markdown'}
    response = requests.post(settings.GITHUB_API_URL + '/markdown', data=json.dumps(params))

    print response.text


def render_all_markdown():
    print 'Rendering all markdown...'
    return


def render_markdown_in_dir(directory):
    print 'Rendering markdown in dir: ' + directory
    return


def main(arguments):
    """ Handles argument parsing """

    if len(arguments) > 3:
        print 'render.py: Too many arguments'
        return

    if len(arguments) == 1:
        # Called with no additional args, render everything
        'render.py: Rendering all markdown files'
        render_all_markdown()
        return

    # Otherwise must have been called with specific flags
    if arguments[1] not in flags:
        print 'render.py: Invalid flag given'
        return
    if arguments[1] == '-d':
        # Render all markdown in given directory
        if len(arguments) != 3:
            print 'render.py: Directory in which to render markdown not given'
            return
        render_markdown_in_dir(arguments[2])
        return
    if arguments[1] == '-f':
        # Render specific file
        if len(arguments) != 3:
            print 'render.py: Path to file to render not given'
            return
        render_markdown(arguments[2])
        return


if __name__ == '__main__':
    main(sys.argv)

