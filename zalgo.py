# encoding: utf-8

import sys
from workflow import Workflow, ICON_WEB, web

def main(wf):
    url = 'https://zalgo.io/api'
    query = wf.args[0]
    params = dict(text=query)
    r = web.get(url, params)

    # throw an error if request failed
    # Workflow will catch this and show it to the user
    r.raise_for_status()

    # Parse the JSON returned by pinboard and extract the posts
    result = r.text

    wf.add_item(title=result,
                subtitle="Copy to clipboard",
                valid=True,
                arg=result)
    
    # Send the results to Alfred as XML
    wf.send_feedback()


if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))