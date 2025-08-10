#PROMPT LIBRARY
from typing import Union, Dict

def prompt(template: str, values: Union[Dict[str, str], list, tuple]) -> str:
    try:
        return template.format(**values) if isinstance(values, dict) else template.format(*values)
    except KeyError as e:
        raise ValueError(f"Missing key for placeholder: {e}")
    except IndexError as e:
        raise ValueError(f"Not enough values for positional placeholders: {e}")
    except Exception as e:
        raise ValueError(f"Failed to fill prompt: {e}")

INITIAL_SEARCHRESULT = """The provided blob of text is the seach result of {keyword}, you have to return the title, description, and links.
You must only include title that was relevant for example, the keyword is John Doe and one of the links shows John Mark Doe, DO NOT INCLUDE THAT, ONLY INCLUDE 100% match, if it contains the keyword letter by letter its called a match!
the blob of text:
{blob}
"""

SEARCH_SUMMARY = """Give me a summary of what have you found on the previous research that has been done, give a short but compact and meaningfull sentences, do not skip over any details!
You also may include any links that are relevant to the results"""