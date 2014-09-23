"""
Script to render all markdown documents in the repository

Uses the Github Markdown API
"""

import requests
import json
import sys
import os
import logging
import base64

import settings
import secrets as auth

# Configuration
FLAGS = ['-d', '-f']
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
    headers = {'Authorization': 'Basic {:s}'.format(base64.b64encode(auth.AUTH_INFO))}
    response = requests.post(settings.GITHUB_API_URL + '/markdown', data=json.dumps(params), headers=headers)

    # Change to .html file
    md_file_path = md_file_path.replace('.md', '.html')

    # Remove source directory from write path
    md_file_path = md_file_path.replace(settings.SOURCE_PATH, './')

    # Write contents to destination path
    write_file = open(os.path.join(settings.RENDER_PATH, md_file_path), 'w')
    write_file.write(response.text)

    # Return path to file created
    return md_file_path


def render_all_markdown():
    """
    Renders all markdown present in current directory and all subdirectories

    Returns a list of paths to the rendered files
    """
    print 'Rendering all markdown...'
    rendered = []

    # Run through and render all .md files in repo
    for dirname, subdirs, files in os.walk(settings.SOURCE_PATH):
        # Skip directory if it is part of a directory to be excluded
        if any(excluded in dirname for excluded in settings.EXCLUDED):
            continue

        # Create destination directory, stripping source directory from path
        write_path = os.path.join(settings.RENDER_PATH, dirname).replace(settings.SOURCE_PATH, './')

        # Make render directory if it doesn't already exist
        # NOTE: There's a race condition here. Should be okay though
        if not os.path.exists(write_path):
            os.makedirs(write_path)

        rendered += [render_markdown(os.path.join(dirname, fname)) for fname in files if fname.lower().endswith('.md')]

    return rendered


def render_markdown_in_dir(directory):
    print 'Rendering markdown in dir: ' + directory
    return

def write_out_directory(current_dir, dir_tree, outfile, path_to):
    """
    Recursively writes out the directory tree

    Links to .html files are created, and subdirs written out as lists
    within the parent directory list element
    """
    outfile.write('<li>')

    if '.html' in current_dir:
        outfile.write('<a href=\'' + path_to + current_dir + '\'>' + current_dir + '</a>')
    else:
        directory = current_dir + '/'
        outfile.write(directory)
        sub_files = dir_tree[current_dir]
        outfile.write('<ul>')
        for sub_file in sub_files:
            write_out_directory(sub_file, dir_tree, outfile, path_to + directory)
        outfile.write('</ul>')

    outfile.write('</li>')

def make_table_of_contents(rendered):
    """ Renders the table of contents page """
    # TODO: Replace this with a better, templatized approach
    outfile = open(os.path.join(settings.RENDER_PATH, 'index.html'), 'w')
    outfile.write('<h1>Table of Contents</h1>')

    # Start recursive writing of directory tree from current directory
    outfile.write('<ul>')
    write_out_directory('.', rendered, outfile, './')
    outfile.write('</ul>')

    outfile.close()

def sort_by_directories(files_list):
    """
    Sorts the given files list based on directories in which they reside

    Returns a dict of directories mapped to files/subdirs within them
    """
    result = {}
    for file_path in files_list:
        while '/' in file_path:
            # Split path on the first / character
            split_path = file_path.split('/', 1)
            directory = split_path[0]
            file_path = split_path[1]

            # Split again to get next piece, either file or subdir
            next_file = file_path.split('/', 1)[0]

            # Create new set of files to map dir to, or add to existing
            result.setdefault(directory, set([])).add(next_file)

    return result



def main(arguments):
    """ Handles argument parsing """

    if len(arguments) > 3:
        print 'render.py: Too many arguments'
        return

    if len(arguments) == 1:
        # Called with no additional args, render everything
        'render.py: Rendering all markdown files'
        rendered = render_all_markdown()
        rendered = sort_by_directories(rendered)
        make_table_of_contents(rendered)
        return

    # Otherwise must have been called with specific flags
    if arguments[1] not in FLAGS:
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
